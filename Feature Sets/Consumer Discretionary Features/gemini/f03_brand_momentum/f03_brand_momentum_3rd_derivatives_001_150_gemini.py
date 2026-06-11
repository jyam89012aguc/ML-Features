import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
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

def f03_brand_momentum_revenue_slope_diff_norm_756d_v151_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_slope_diff_norm_756d_v152_signal(sgna):
    """Normalized slope change for Raw level of sgna over 756d window."""
    res = (_slope_pct(sgna, 756).diff(756) / _sma(sgna.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_slope_diff_norm_756d_v153_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_slope_diff_norm_756d_v154_signal(revenue, sgna):
    """Normalized slope change for Sales generated per dollar of marketing/admin over 756d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 756).diff(756) / _sma(_ratio(revenue, sgna).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_756d_v155_signal(marketcap, revenue):
    """Normalized slope change for Valuation ascribed per unit of sales over 756d window."""
    res = (_slope_pct(_ratio(marketcap, revenue), 756).diff(756) / _sma(_ratio(marketcap, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_slope_diff_norm_1008d_v156_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_slope_diff_norm_1008d_v157_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1008d window."""
    res = (_slope_pct(sgna, 1008).diff(1008) / _sma(sgna.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_slope_diff_norm_1008d_v158_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_slope_diff_norm_1008d_v159_signal(revenue, sgna):
    """Normalized slope change for Sales generated per dollar of marketing/admin over 1008d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 1008).diff(1008) / _sma(_ratio(revenue, sgna).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_1008d_v160_signal(marketcap, revenue):
    """Normalized slope change for Valuation ascribed per unit of sales over 1008d window."""
    res = (_slope_pct(_ratio(marketcap, revenue), 1008).diff(1008) / _sma(_ratio(marketcap, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_slope_diff_norm_1260d_v161_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_slope_diff_norm_1260d_v162_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1260d window."""
    res = (_slope_pct(sgna, 1260).diff(1260) / _sma(sgna.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_slope_diff_norm_1260d_v163_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_slope_diff_norm_1260d_v164_signal(revenue, sgna):
    """Normalized slope change for Sales generated per dollar of marketing/admin over 1260d window."""
    res = (_slope_pct(_ratio(revenue, sgna), 1260).diff(1260) / _sma(_ratio(revenue, sgna).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_1260d_v165_signal(marketcap, revenue):
    """Normalized slope change for Valuation ascribed per unit of sales over 1260d window."""
    res = (_slope_pct(_ratio(marketcap, revenue), 1260).diff(1260) / _sma(_ratio(marketcap, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_5d_v166_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_5d_v167_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 5d window."""
    res = _z(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_5d_v168_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_5d_v169_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 5d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_5d_v170_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 5d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_10d_v171_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_10d_v172_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 10d window."""
    res = _z(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_10d_v173_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_10d_v174_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 10d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_10d_v175_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 10d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_21d_v176_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_21d_v177_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 21d window."""
    res = _z(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_21d_v178_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_21d_v179_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 21d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_21d_v180_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 21d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_42d_v181_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_42d_v182_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 42d window."""
    res = _z(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_42d_v183_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_42d_v184_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 42d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_42d_v185_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 42d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_63d_v186_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_63d_v187_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 63d window."""
    res = _z(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_63d_v188_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_63d_v189_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_63d_v190_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 63d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_126d_v191_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_126d_v192_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 126d window."""
    res = _z(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_126d_v193_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_126d_v194_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_126d_v195_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 126d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_252d_v196_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_252d_v197_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 252d window."""
    res = _z(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_252d_v198_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_252d_v199_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_252d_v200_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 252d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_504d_v201_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_504d_v202_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 504d window."""
    res = _z(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_504d_v203_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_504d_v204_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_504d_v205_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 504d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_756d_v206_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_756d_v207_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 756d window."""
    res = _z(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_756d_v208_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_756d_v209_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_756d_v210_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 756d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_1008d_v211_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_1008d_v212_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 1008d window."""
    res = _z(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_1008d_v213_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_1008d_v214_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_1008d_v215_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 1008d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_mom_z_1260d_v216_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_mom_z_1260d_v217_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 1260d window."""
    res = _z(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_mom_z_1260d_v218_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_mom_z_1260d_v219_signal(revenue, sgna):
    """Relative momentum strength for Sales generated per dollar of marketing/admin over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_mom_z_1260d_v220_signal(marketcap, revenue):
    """Relative momentum strength for Valuation ascribed per unit of sales over 1260d window."""
    res = _z(_slope_pct(_ratio(marketcap, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_5d_v221_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_5d_v222_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 5d window."""
    res = _std(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_5d_v223_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_5d_v224_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_5d_v225_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 5d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_10d_v226_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_10d_v227_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 10d window."""
    res = _std(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_10d_v228_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_10d_v229_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_10d_v230_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 10d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_21d_v231_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_21d_v232_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 21d window."""
    res = _std(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_21d_v233_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_21d_v234_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_21d_v235_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 21d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_42d_v236_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_42d_v237_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 42d window."""
    res = _std(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_42d_v238_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_42d_v239_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_42d_v240_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 42d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_63d_v241_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_63d_v242_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 63d window."""
    res = _std(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_63d_v243_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_63d_v244_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_63d_v245_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 63d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_126d_v246_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_126d_v247_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 126d window."""
    res = _std(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_126d_v248_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_126d_v249_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_126d_v250_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 126d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_252d_v251_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_252d_v252_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 252d window."""
    res = _std(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_252d_v253_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 252d window."""
    res = _std(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_252d_v254_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_252d_v255_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 252d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_504d_v256_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_504d_v257_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 504d window."""
    res = _std(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_504d_v258_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 504d window."""
    res = _std(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_504d_v259_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_504d_v260_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 504d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_756d_v261_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_756d_v262_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 756d window."""
    res = _std(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_756d_v263_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 756d window."""
    res = _std(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_756d_v264_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_756d_v265_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 756d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_1008d_v266_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_1008d_v267_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 1008d window."""
    res = _std(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_1008d_v268_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 1008d window."""
    res = _std(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_1008d_v269_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_1008d_v270_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 1008d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_vol_slope_1260d_v271_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_vol_slope_1260d_v272_signal(sgna):
    """Volatility of the momentum for Raw level of sgna over 1260d window."""
    res = _std(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_vol_slope_1260d_v273_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 1260d window."""
    res = _std(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_vol_slope_1260d_v274_signal(revenue, sgna):
    """Volatility of the momentum for Sales generated per dollar of marketing/admin over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_vol_slope_1260d_v275_signal(marketcap, revenue):
    """Volatility of the momentum for Valuation ascribed per unit of sales over 1260d window."""
    res = _std(_slope_pct(_ratio(marketcap, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_brand_momentum_revenue_slope_diff_norm_756d_v151_signal": {"inputs": [], "func": f03_brand_momentum_revenue_slope_diff_norm_756d_v151_signal},    "f03_brand_momentum_sgna_slope_diff_norm_756d_v152_signal": {"inputs": [], "func": f03_brand_momentum_sgna_slope_diff_norm_756d_v152_signal},    "f03_brand_momentum_marketcap_slope_diff_norm_756d_v153_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_slope_diff_norm_756d_v153_signal},    "f03_brand_momentum_brand_leverage_slope_diff_norm_756d_v154_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_slope_diff_norm_756d_v154_signal},    "f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_756d_v155_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_756d_v155_signal},    "f03_brand_momentum_revenue_slope_diff_norm_1008d_v156_signal": {"inputs": [], "func": f03_brand_momentum_revenue_slope_diff_norm_1008d_v156_signal},    "f03_brand_momentum_sgna_slope_diff_norm_1008d_v157_signal": {"inputs": [], "func": f03_brand_momentum_sgna_slope_diff_norm_1008d_v157_signal},    "f03_brand_momentum_marketcap_slope_diff_norm_1008d_v158_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_slope_diff_norm_1008d_v158_signal},    "f03_brand_momentum_brand_leverage_slope_diff_norm_1008d_v159_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_slope_diff_norm_1008d_v159_signal},    "f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_1008d_v160_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_1008d_v160_signal},    "f03_brand_momentum_revenue_slope_diff_norm_1260d_v161_signal": {"inputs": [], "func": f03_brand_momentum_revenue_slope_diff_norm_1260d_v161_signal},    "f03_brand_momentum_sgna_slope_diff_norm_1260d_v162_signal": {"inputs": [], "func": f03_brand_momentum_sgna_slope_diff_norm_1260d_v162_signal},    "f03_brand_momentum_marketcap_slope_diff_norm_1260d_v163_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_slope_diff_norm_1260d_v163_signal},    "f03_brand_momentum_brand_leverage_slope_diff_norm_1260d_v164_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_slope_diff_norm_1260d_v164_signal},    "f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_1260d_v165_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_slope_diff_norm_1260d_v165_signal},    "f03_brand_momentum_revenue_mom_z_5d_v166_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_5d_v166_signal},    "f03_brand_momentum_sgna_mom_z_5d_v167_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_5d_v167_signal},    "f03_brand_momentum_marketcap_mom_z_5d_v168_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_5d_v168_signal},    "f03_brand_momentum_brand_leverage_mom_z_5d_v169_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_5d_v169_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_5d_v170_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_5d_v170_signal},    "f03_brand_momentum_revenue_mom_z_10d_v171_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_10d_v171_signal},    "f03_brand_momentum_sgna_mom_z_10d_v172_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_10d_v172_signal},    "f03_brand_momentum_marketcap_mom_z_10d_v173_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_10d_v173_signal},    "f03_brand_momentum_brand_leverage_mom_z_10d_v174_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_10d_v174_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_10d_v175_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_10d_v175_signal},    "f03_brand_momentum_revenue_mom_z_21d_v176_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_21d_v176_signal},    "f03_brand_momentum_sgna_mom_z_21d_v177_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_21d_v177_signal},    "f03_brand_momentum_marketcap_mom_z_21d_v178_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_21d_v178_signal},    "f03_brand_momentum_brand_leverage_mom_z_21d_v179_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_21d_v179_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_21d_v180_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_21d_v180_signal},    "f03_brand_momentum_revenue_mom_z_42d_v181_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_42d_v181_signal},    "f03_brand_momentum_sgna_mom_z_42d_v182_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_42d_v182_signal},    "f03_brand_momentum_marketcap_mom_z_42d_v183_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_42d_v183_signal},    "f03_brand_momentum_brand_leverage_mom_z_42d_v184_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_42d_v184_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_42d_v185_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_42d_v185_signal},    "f03_brand_momentum_revenue_mom_z_63d_v186_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_63d_v186_signal},    "f03_brand_momentum_sgna_mom_z_63d_v187_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_63d_v187_signal},    "f03_brand_momentum_marketcap_mom_z_63d_v188_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_63d_v188_signal},    "f03_brand_momentum_brand_leverage_mom_z_63d_v189_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_63d_v189_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_63d_v190_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_63d_v190_signal},    "f03_brand_momentum_revenue_mom_z_126d_v191_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_126d_v191_signal},    "f03_brand_momentum_sgna_mom_z_126d_v192_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_126d_v192_signal},    "f03_brand_momentum_marketcap_mom_z_126d_v193_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_126d_v193_signal},    "f03_brand_momentum_brand_leverage_mom_z_126d_v194_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_126d_v194_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_126d_v195_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_126d_v195_signal},    "f03_brand_momentum_revenue_mom_z_252d_v196_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_252d_v196_signal},    "f03_brand_momentum_sgna_mom_z_252d_v197_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_252d_v197_signal},    "f03_brand_momentum_marketcap_mom_z_252d_v198_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_252d_v198_signal},    "f03_brand_momentum_brand_leverage_mom_z_252d_v199_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_252d_v199_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_252d_v200_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_252d_v200_signal},    "f03_brand_momentum_revenue_mom_z_504d_v201_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_504d_v201_signal},    "f03_brand_momentum_sgna_mom_z_504d_v202_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_504d_v202_signal},    "f03_brand_momentum_marketcap_mom_z_504d_v203_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_504d_v203_signal},    "f03_brand_momentum_brand_leverage_mom_z_504d_v204_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_504d_v204_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_504d_v205_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_504d_v205_signal},    "f03_brand_momentum_revenue_mom_z_756d_v206_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_756d_v206_signal},    "f03_brand_momentum_sgna_mom_z_756d_v207_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_756d_v207_signal},    "f03_brand_momentum_marketcap_mom_z_756d_v208_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_756d_v208_signal},    "f03_brand_momentum_brand_leverage_mom_z_756d_v209_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_756d_v209_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_756d_v210_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_756d_v210_signal},    "f03_brand_momentum_revenue_mom_z_1008d_v211_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_1008d_v211_signal},    "f03_brand_momentum_sgna_mom_z_1008d_v212_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_1008d_v212_signal},    "f03_brand_momentum_marketcap_mom_z_1008d_v213_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_1008d_v213_signal},    "f03_brand_momentum_brand_leverage_mom_z_1008d_v214_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_1008d_v214_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_1008d_v215_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_1008d_v215_signal},    "f03_brand_momentum_revenue_mom_z_1260d_v216_signal": {"inputs": [], "func": f03_brand_momentum_revenue_mom_z_1260d_v216_signal},    "f03_brand_momentum_sgna_mom_z_1260d_v217_signal": {"inputs": [], "func": f03_brand_momentum_sgna_mom_z_1260d_v217_signal},    "f03_brand_momentum_marketcap_mom_z_1260d_v218_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_mom_z_1260d_v218_signal},    "f03_brand_momentum_brand_leverage_mom_z_1260d_v219_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_mom_z_1260d_v219_signal},    "f03_brand_momentum_mkt_cap_per_rev_mom_z_1260d_v220_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_mom_z_1260d_v220_signal},    "f03_brand_momentum_revenue_vol_slope_5d_v221_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_5d_v221_signal},    "f03_brand_momentum_sgna_vol_slope_5d_v222_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_5d_v222_signal},    "f03_brand_momentum_marketcap_vol_slope_5d_v223_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_5d_v223_signal},    "f03_brand_momentum_brand_leverage_vol_slope_5d_v224_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_5d_v224_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_5d_v225_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_5d_v225_signal},    "f03_brand_momentum_revenue_vol_slope_10d_v226_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_10d_v226_signal},    "f03_brand_momentum_sgna_vol_slope_10d_v227_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_10d_v227_signal},    "f03_brand_momentum_marketcap_vol_slope_10d_v228_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_10d_v228_signal},    "f03_brand_momentum_brand_leverage_vol_slope_10d_v229_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_10d_v229_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_10d_v230_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_10d_v230_signal},    "f03_brand_momentum_revenue_vol_slope_21d_v231_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_21d_v231_signal},    "f03_brand_momentum_sgna_vol_slope_21d_v232_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_21d_v232_signal},    "f03_brand_momentum_marketcap_vol_slope_21d_v233_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_21d_v233_signal},    "f03_brand_momentum_brand_leverage_vol_slope_21d_v234_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_21d_v234_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_21d_v235_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_21d_v235_signal},    "f03_brand_momentum_revenue_vol_slope_42d_v236_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_42d_v236_signal},    "f03_brand_momentum_sgna_vol_slope_42d_v237_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_42d_v237_signal},    "f03_brand_momentum_marketcap_vol_slope_42d_v238_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_42d_v238_signal},    "f03_brand_momentum_brand_leverage_vol_slope_42d_v239_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_42d_v239_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_42d_v240_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_42d_v240_signal},    "f03_brand_momentum_revenue_vol_slope_63d_v241_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_63d_v241_signal},    "f03_brand_momentum_sgna_vol_slope_63d_v242_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_63d_v242_signal},    "f03_brand_momentum_marketcap_vol_slope_63d_v243_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_63d_v243_signal},    "f03_brand_momentum_brand_leverage_vol_slope_63d_v244_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_63d_v244_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_63d_v245_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_63d_v245_signal},    "f03_brand_momentum_revenue_vol_slope_126d_v246_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_126d_v246_signal},    "f03_brand_momentum_sgna_vol_slope_126d_v247_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_126d_v247_signal},    "f03_brand_momentum_marketcap_vol_slope_126d_v248_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_126d_v248_signal},    "f03_brand_momentum_brand_leverage_vol_slope_126d_v249_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_126d_v249_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_126d_v250_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_126d_v250_signal},    "f03_brand_momentum_revenue_vol_slope_252d_v251_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_252d_v251_signal},    "f03_brand_momentum_sgna_vol_slope_252d_v252_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_252d_v252_signal},    "f03_brand_momentum_marketcap_vol_slope_252d_v253_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_252d_v253_signal},    "f03_brand_momentum_brand_leverage_vol_slope_252d_v254_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_252d_v254_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_252d_v255_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_252d_v255_signal},    "f03_brand_momentum_revenue_vol_slope_504d_v256_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_504d_v256_signal},    "f03_brand_momentum_sgna_vol_slope_504d_v257_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_504d_v257_signal},    "f03_brand_momentum_marketcap_vol_slope_504d_v258_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_504d_v258_signal},    "f03_brand_momentum_brand_leverage_vol_slope_504d_v259_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_504d_v259_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_504d_v260_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_504d_v260_signal},    "f03_brand_momentum_revenue_vol_slope_756d_v261_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_756d_v261_signal},    "f03_brand_momentum_sgna_vol_slope_756d_v262_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_756d_v262_signal},    "f03_brand_momentum_marketcap_vol_slope_756d_v263_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_756d_v263_signal},    "f03_brand_momentum_brand_leverage_vol_slope_756d_v264_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_756d_v264_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_756d_v265_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_756d_v265_signal},    "f03_brand_momentum_revenue_vol_slope_1008d_v266_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_1008d_v266_signal},    "f03_brand_momentum_sgna_vol_slope_1008d_v267_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_1008d_v267_signal},    "f03_brand_momentum_marketcap_vol_slope_1008d_v268_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_1008d_v268_signal},    "f03_brand_momentum_brand_leverage_vol_slope_1008d_v269_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_1008d_v269_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_1008d_v270_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_1008d_v270_signal},    "f03_brand_momentum_revenue_vol_slope_1260d_v271_signal": {"inputs": [], "func": f03_brand_momentum_revenue_vol_slope_1260d_v271_signal},    "f03_brand_momentum_sgna_vol_slope_1260d_v272_signal": {"inputs": [], "func": f03_brand_momentum_sgna_vol_slope_1260d_v272_signal},    "f03_brand_momentum_marketcap_vol_slope_1260d_v273_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_vol_slope_1260d_v273_signal},    "f03_brand_momentum_brand_leverage_vol_slope_1260d_v274_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_vol_slope_1260d_v274_signal},    "f03_brand_momentum_mkt_cap_per_rev_vol_slope_1260d_v275_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_vol_slope_1260d_v275_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
