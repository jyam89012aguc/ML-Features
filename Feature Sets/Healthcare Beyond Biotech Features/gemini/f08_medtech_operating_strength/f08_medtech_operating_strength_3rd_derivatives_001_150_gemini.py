import pandas as pd
import numpy as np
import inspect

# ===== Healthcare High-Performance Alpha Helpers =====
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

def f08_medtech_operating_strength_netinc_mom_z_63d_v151_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_63d_v152_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_mom_z_126d_v153_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 126d window."""
    res = _z(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_mom_z_126d_v154_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_mom_z_126d_v155_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_126d_v156_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_mom_z_252d_v157_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 252d window."""
    res = _z(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_mom_z_252d_v158_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_mom_z_252d_v159_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_252d_v160_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_mom_z_504d_v161_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 504d window."""
    res = _z(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_mom_z_504d_v162_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_mom_z_504d_v163_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_504d_v164_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_mom_z_756d_v165_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 756d window."""
    res = _z(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_mom_z_756d_v166_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_mom_z_756d_v167_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_756d_v168_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_mom_z_1008d_v169_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 1008d window."""
    res = _z(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_mom_z_1008d_v170_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_mom_z_1008d_v171_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_1008d_v172_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_mom_z_1260d_v173_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 1260d window."""
    res = _z(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_mom_z_1260d_v174_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_mom_z_1260d_v175_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_mom_z_1260d_v176_signal(revenue, sgna):
    """Relative momentum strength for Revenue yield on sales spend over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, sgna), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_5d_v177_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 5d window."""
    res = _std(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_5d_v178_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_5d_v179_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_5d_v180_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_10d_v181_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 10d window."""
    res = _std(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_10d_v182_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_10d_v183_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_10d_v184_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_21d_v185_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 21d window."""
    res = _std(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_21d_v186_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_21d_v187_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_21d_v188_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_42d_v189_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 42d window."""
    res = _std(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_42d_v190_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_42d_v191_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_42d_v192_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_63d_v193_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 63d window."""
    res = _std(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_63d_v194_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_63d_v195_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_63d_v196_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_126d_v197_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 126d window."""
    res = _std(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_126d_v198_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_126d_v199_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_126d_v200_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_252d_v201_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 252d window."""
    res = _std(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_252d_v202_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_252d_v203_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_252d_v204_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_504d_v205_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 504d window."""
    res = _std(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_504d_v206_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_504d_v207_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_504d_v208_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_756d_v209_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 756d window."""
    res = _std(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_756d_v210_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_756d_v211_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_756d_v212_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_1008d_v213_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 1008d window."""
    res = _std(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_1008d_v214_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_1008d_v215_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_1008d_v216_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_vol_slope_1260d_v217_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 1260d window."""
    res = _std(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_vol_slope_1260d_v218_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_vol_slope_1260d_v219_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_vol_slope_1260d_v220_signal(revenue, sgna):
    """Volatility of momentum for Revenue yield on sales spend over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, sgna), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_5d_v221_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 5d window."""
    res = _ewma(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_5d_v222_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 5d window."""
    res = _ewma(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_5d_v223_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _ewma(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_5d_v224_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 5d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_10d_v225_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 10d window."""
    res = _ewma(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_10d_v226_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 10d window."""
    res = _ewma(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_10d_v227_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _ewma(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_10d_v228_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 10d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_21d_v229_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 21d window."""
    res = _ewma(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_21d_v230_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 21d window."""
    res = _ewma(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_21d_v231_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _ewma(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_21d_v232_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 21d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_42d_v233_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 42d window."""
    res = _ewma(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_42d_v234_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 42d window."""
    res = _ewma(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_42d_v235_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _ewma(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_42d_v236_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 42d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_63d_v237_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 63d window."""
    res = _ewma(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_63d_v238_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 63d window."""
    res = _ewma(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_63d_v239_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _ewma(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_63d_v240_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 63d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_126d_v241_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 126d window."""
    res = _ewma(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_126d_v242_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 126d window."""
    res = _ewma(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_126d_v243_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 126d window."""
    res = _ewma(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_126d_v244_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 126d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_252d_v245_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 252d window."""
    res = _ewma(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_252d_v246_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 252d window."""
    res = _ewma(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_252d_v247_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 252d window."""
    res = _ewma(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_252d_v248_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 252d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_504d_v249_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 504d window."""
    res = _ewma(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_504d_v250_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 504d window."""
    res = _ewma(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_504d_v251_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 504d window."""
    res = _ewma(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_504d_v252_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 504d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_756d_v253_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 756d window."""
    res = _ewma(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_756d_v254_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 756d window."""
    res = _ewma(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_756d_v255_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 756d window."""
    res = _ewma(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_756d_v256_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 756d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_1008d_v257_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 1008d window."""
    res = _ewma(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_1008d_v258_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1008d window."""
    res = _ewma(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_1008d_v259_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1008d window."""
    res = _ewma(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_1008d_v260_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 1008d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sgna_ewma_slope_1260d_v261_signal(sgna):
    """Exponential momentum smoothing for Raw level of sgna over 1260d window."""
    res = _ewma(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_revenue_ewma_slope_1260d_v262_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1260d window."""
    res = _ewma(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_netinc_ewma_slope_1260d_v263_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1260d window."""
    res = _ewma(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_medtech_operating_strength_sales_efficiency_ewma_slope_1260d_v264_signal(revenue, sgna):
    """Exponential momentum smoothing for Revenue yield on sales spend over 1260d window."""
    res = _ewma(_slope_pct(_ratio(revenue, sgna), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f08_medtech_operating_strength_netinc_mom_z_63d_v151_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_63d_v151_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_63d_v152_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_63d_v152_signal},
    "f08_medtech_operating_strength_sgna_mom_z_126d_v153_signal": {"func": f08_medtech_operating_strength_sgna_mom_z_126d_v153_signal},
    "f08_medtech_operating_strength_revenue_mom_z_126d_v154_signal": {"func": f08_medtech_operating_strength_revenue_mom_z_126d_v154_signal},
    "f08_medtech_operating_strength_netinc_mom_z_126d_v155_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_126d_v155_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_126d_v156_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_126d_v156_signal},
    "f08_medtech_operating_strength_sgna_mom_z_252d_v157_signal": {"func": f08_medtech_operating_strength_sgna_mom_z_252d_v157_signal},
    "f08_medtech_operating_strength_revenue_mom_z_252d_v158_signal": {"func": f08_medtech_operating_strength_revenue_mom_z_252d_v158_signal},
    "f08_medtech_operating_strength_netinc_mom_z_252d_v159_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_252d_v159_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_252d_v160_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_252d_v160_signal},
    "f08_medtech_operating_strength_sgna_mom_z_504d_v161_signal": {"func": f08_medtech_operating_strength_sgna_mom_z_504d_v161_signal},
    "f08_medtech_operating_strength_revenue_mom_z_504d_v162_signal": {"func": f08_medtech_operating_strength_revenue_mom_z_504d_v162_signal},
    "f08_medtech_operating_strength_netinc_mom_z_504d_v163_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_504d_v163_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_504d_v164_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_504d_v164_signal},
    "f08_medtech_operating_strength_sgna_mom_z_756d_v165_signal": {"func": f08_medtech_operating_strength_sgna_mom_z_756d_v165_signal},
    "f08_medtech_operating_strength_revenue_mom_z_756d_v166_signal": {"func": f08_medtech_operating_strength_revenue_mom_z_756d_v166_signal},
    "f08_medtech_operating_strength_netinc_mom_z_756d_v167_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_756d_v167_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_756d_v168_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_756d_v168_signal},
    "f08_medtech_operating_strength_sgna_mom_z_1008d_v169_signal": {"func": f08_medtech_operating_strength_sgna_mom_z_1008d_v169_signal},
    "f08_medtech_operating_strength_revenue_mom_z_1008d_v170_signal": {"func": f08_medtech_operating_strength_revenue_mom_z_1008d_v170_signal},
    "f08_medtech_operating_strength_netinc_mom_z_1008d_v171_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_1008d_v171_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_1008d_v172_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_1008d_v172_signal},
    "f08_medtech_operating_strength_sgna_mom_z_1260d_v173_signal": {"func": f08_medtech_operating_strength_sgna_mom_z_1260d_v173_signal},
    "f08_medtech_operating_strength_revenue_mom_z_1260d_v174_signal": {"func": f08_medtech_operating_strength_revenue_mom_z_1260d_v174_signal},
    "f08_medtech_operating_strength_netinc_mom_z_1260d_v175_signal": {"func": f08_medtech_operating_strength_netinc_mom_z_1260d_v175_signal},
    "f08_medtech_operating_strength_sales_efficiency_mom_z_1260d_v176_signal": {"func": f08_medtech_operating_strength_sales_efficiency_mom_z_1260d_v176_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_5d_v177_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_5d_v177_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_5d_v178_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_5d_v178_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_5d_v179_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_5d_v179_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_5d_v180_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_5d_v180_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_10d_v181_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_10d_v181_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_10d_v182_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_10d_v182_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_10d_v183_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_10d_v183_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_10d_v184_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_10d_v184_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_21d_v185_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_21d_v185_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_21d_v186_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_21d_v186_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_21d_v187_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_21d_v187_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_21d_v188_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_21d_v188_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_42d_v189_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_42d_v189_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_42d_v190_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_42d_v190_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_42d_v191_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_42d_v191_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_42d_v192_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_42d_v192_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_63d_v193_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_63d_v193_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_63d_v194_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_63d_v194_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_63d_v195_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_63d_v195_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_63d_v196_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_63d_v196_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_126d_v197_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_126d_v197_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_126d_v198_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_126d_v198_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_126d_v199_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_126d_v199_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_126d_v200_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_126d_v200_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_252d_v201_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_252d_v201_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_252d_v202_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_252d_v202_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_252d_v203_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_252d_v203_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_252d_v204_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_252d_v204_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_504d_v205_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_504d_v205_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_504d_v206_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_504d_v206_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_504d_v207_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_504d_v207_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_504d_v208_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_504d_v208_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_756d_v209_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_756d_v209_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_756d_v210_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_756d_v210_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_756d_v211_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_756d_v211_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_756d_v212_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_756d_v212_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_1008d_v213_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_1008d_v213_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_1008d_v214_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_1008d_v214_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_1008d_v215_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_1008d_v215_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_1008d_v216_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_1008d_v216_signal},
    "f08_medtech_operating_strength_sgna_vol_slope_1260d_v217_signal": {"func": f08_medtech_operating_strength_sgna_vol_slope_1260d_v217_signal},
    "f08_medtech_operating_strength_revenue_vol_slope_1260d_v218_signal": {"func": f08_medtech_operating_strength_revenue_vol_slope_1260d_v218_signal},
    "f08_medtech_operating_strength_netinc_vol_slope_1260d_v219_signal": {"func": f08_medtech_operating_strength_netinc_vol_slope_1260d_v219_signal},
    "f08_medtech_operating_strength_sales_efficiency_vol_slope_1260d_v220_signal": {"func": f08_medtech_operating_strength_sales_efficiency_vol_slope_1260d_v220_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_5d_v221_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_5d_v221_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_5d_v222_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_5d_v222_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_5d_v223_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_5d_v223_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_5d_v224_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_5d_v224_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_10d_v225_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_10d_v225_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_10d_v226_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_10d_v226_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_10d_v227_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_10d_v227_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_10d_v228_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_10d_v228_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_21d_v229_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_21d_v229_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_21d_v230_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_21d_v230_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_21d_v231_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_21d_v231_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_21d_v232_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_21d_v232_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_42d_v233_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_42d_v233_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_42d_v234_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_42d_v234_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_42d_v235_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_42d_v235_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_42d_v236_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_42d_v236_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_63d_v237_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_63d_v237_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_63d_v238_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_63d_v238_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_63d_v239_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_63d_v239_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_63d_v240_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_63d_v240_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_126d_v241_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_126d_v241_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_126d_v242_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_126d_v242_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_126d_v243_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_126d_v243_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_126d_v244_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_126d_v244_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_252d_v245_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_252d_v245_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_252d_v246_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_252d_v246_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_252d_v247_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_252d_v247_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_252d_v248_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_252d_v248_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_504d_v249_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_504d_v249_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_504d_v250_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_504d_v250_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_504d_v251_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_504d_v251_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_504d_v252_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_504d_v252_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_756d_v253_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_756d_v253_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_756d_v254_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_756d_v254_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_756d_v255_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_756d_v255_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_756d_v256_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_756d_v256_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_1008d_v257_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_1008d_v257_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_1008d_v258_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_1008d_v258_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_1008d_v259_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_1008d_v259_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_1008d_v260_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_1008d_v260_signal},
    "f08_medtech_operating_strength_sgna_ewma_slope_1260d_v261_signal": {"func": f08_medtech_operating_strength_sgna_ewma_slope_1260d_v261_signal},
    "f08_medtech_operating_strength_revenue_ewma_slope_1260d_v262_signal": {"func": f08_medtech_operating_strength_revenue_ewma_slope_1260d_v262_signal},
    "f08_medtech_operating_strength_netinc_ewma_slope_1260d_v263_signal": {"func": f08_medtech_operating_strength_netinc_ewma_slope_1260d_v263_signal},
    "f08_medtech_operating_strength_sales_efficiency_ewma_slope_1260d_v264_signal": {"func": f08_medtech_operating_strength_sales_efficiency_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "sbcomp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 08...")
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
