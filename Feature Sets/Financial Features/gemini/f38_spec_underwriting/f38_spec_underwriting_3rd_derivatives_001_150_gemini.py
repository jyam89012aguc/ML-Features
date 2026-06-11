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

def f38_spec_underwriting_revenue_mom_z_63d_v151_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_63d_v152_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 63d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_126d_v153_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 126d window."""
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_126d_v154_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 126d window."""
    res = _z(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_126d_v155_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_126d_v156_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 126d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_252d_v157_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 252d window."""
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_252d_v158_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 252d window."""
    res = _z(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_252d_v159_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_252d_v160_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 252d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_504d_v161_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 504d window."""
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_504d_v162_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 504d window."""
    res = _z(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_504d_v163_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_504d_v164_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 504d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_756d_v165_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 756d window."""
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_756d_v166_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 756d window."""
    res = _z(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_756d_v167_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_756d_v168_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 756d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_1008d_v169_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1008d window."""
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_1008d_v170_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 1008d window."""
    res = _z(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_1008d_v171_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_1008d_v172_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 1008d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_1260d_v173_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1260d window."""
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_1260d_v174_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 1260d window."""
    res = _z(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_1260d_v175_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_1260d_v176_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 1260d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_5d_v177_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 5d window."""
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_5d_v178_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 5d window."""
    res = _std(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_5d_v179_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_5d_v180_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 5d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_10d_v181_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 10d window."""
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_10d_v182_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 10d window."""
    res = _std(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_10d_v183_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_10d_v184_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 10d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_21d_v185_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 21d window."""
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_21d_v186_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 21d window."""
    res = _std(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_21d_v187_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_21d_v188_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 21d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_42d_v189_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 42d window."""
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_42d_v190_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 42d window."""
    res = _std(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_42d_v191_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_42d_v192_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 42d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_63d_v193_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 63d window."""
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_63d_v194_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 63d window."""
    res = _std(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_63d_v195_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_63d_v196_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 63d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_126d_v197_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 126d window."""
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_126d_v198_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 126d window."""
    res = _std(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_126d_v199_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_126d_v200_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 126d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_252d_v201_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 252d window."""
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_252d_v202_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 252d window."""
    res = _std(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_252d_v203_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_252d_v204_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 252d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_504d_v205_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 504d window."""
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_504d_v206_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 504d window."""
    res = _std(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_504d_v207_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_504d_v208_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 504d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_756d_v209_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 756d window."""
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_756d_v210_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 756d window."""
    res = _std(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_756d_v211_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_756d_v212_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 756d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_1008d_v213_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 1008d window."""
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_1008d_v214_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 1008d window."""
    res = _std(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_1008d_v215_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_1008d_v216_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 1008d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_vol_slope_1260d_v217_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 1260d window."""
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_vol_slope_1260d_v218_signal(ebitdamargin):
    """Volatility of momentum for Raw level of ebitdamargin over 1260d window."""
    res = _std(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_vol_slope_1260d_v219_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_vol_slope_1260d_v220_signal(ebitdamargin, grossmargin):
    """Volatility of momentum for Underwriting profit efficiency over 1260d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_5d_v221_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 5d window."""
    res = _ewma(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_5d_v222_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 5d window."""
    res = _ewma(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_5d_v223_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 5d window."""
    res = _ewma(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_5d_v224_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 5d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_10d_v225_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 10d window."""
    res = _ewma(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_10d_v226_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 10d window."""
    res = _ewma(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_10d_v227_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 10d window."""
    res = _ewma(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_10d_v228_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 10d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_21d_v229_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 21d window."""
    res = _ewma(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_21d_v230_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 21d window."""
    res = _ewma(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_21d_v231_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 21d window."""
    res = _ewma(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_21d_v232_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 21d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_42d_v233_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 42d window."""
    res = _ewma(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_42d_v234_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 42d window."""
    res = _ewma(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_42d_v235_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 42d window."""
    res = _ewma(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_42d_v236_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 42d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_63d_v237_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 63d window."""
    res = _ewma(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_63d_v238_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 63d window."""
    res = _ewma(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_63d_v239_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 63d window."""
    res = _ewma(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_63d_v240_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 63d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_126d_v241_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 126d window."""
    res = _ewma(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_126d_v242_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 126d window."""
    res = _ewma(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_126d_v243_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 126d window."""
    res = _ewma(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_126d_v244_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 126d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_252d_v245_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 252d window."""
    res = _ewma(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_252d_v246_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 252d window."""
    res = _ewma(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_252d_v247_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 252d window."""
    res = _ewma(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_252d_v248_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 252d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_504d_v249_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 504d window."""
    res = _ewma(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_504d_v250_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 504d window."""
    res = _ewma(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_504d_v251_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 504d window."""
    res = _ewma(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_504d_v252_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 504d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_756d_v253_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 756d window."""
    res = _ewma(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_756d_v254_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 756d window."""
    res = _ewma(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_756d_v255_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 756d window."""
    res = _ewma(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_756d_v256_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 756d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_1008d_v257_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 1008d window."""
    res = _ewma(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_1008d_v258_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 1008d window."""
    res = _ewma(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_1008d_v259_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1008d window."""
    res = _ewma(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_1008d_v260_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 1008d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_slope_1260d_v261_signal(grossmargin):
    """Exponential momentum smoothing for Raw level of grossmargin over 1260d window."""
    res = _ewma(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_slope_1260d_v262_signal(ebitdamargin):
    """Exponential momentum smoothing for Raw level of ebitdamargin over 1260d window."""
    res = _ewma(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_slope_1260d_v263_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1260d window."""
    res = _ewma(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_slope_1260d_v264_signal(ebitdamargin, grossmargin):
    """Exponential momentum smoothing for Underwriting profit efficiency over 1260d window."""
    res = _ewma(_slope_pct(_ratio(ebitdamargin, grossmargin), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f38_spec_underwriting_revenue_mom_z_63d_v151_signal": {"func": f38_spec_underwriting_revenue_mom_z_63d_v151_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_63d_v152_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_63d_v152_signal},
    "f38_spec_underwriting_grossmargin_mom_z_126d_v153_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_126d_v153_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_126d_v154_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_126d_v154_signal},
    "f38_spec_underwriting_revenue_mom_z_126d_v155_signal": {"func": f38_spec_underwriting_revenue_mom_z_126d_v155_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_126d_v156_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_126d_v156_signal},
    "f38_spec_underwriting_grossmargin_mom_z_252d_v157_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_252d_v157_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_252d_v158_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_252d_v158_signal},
    "f38_spec_underwriting_revenue_mom_z_252d_v159_signal": {"func": f38_spec_underwriting_revenue_mom_z_252d_v159_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_252d_v160_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_252d_v160_signal},
    "f38_spec_underwriting_grossmargin_mom_z_504d_v161_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_504d_v161_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_504d_v162_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_504d_v162_signal},
    "f38_spec_underwriting_revenue_mom_z_504d_v163_signal": {"func": f38_spec_underwriting_revenue_mom_z_504d_v163_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_504d_v164_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_504d_v164_signal},
    "f38_spec_underwriting_grossmargin_mom_z_756d_v165_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_756d_v165_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_756d_v166_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_756d_v166_signal},
    "f38_spec_underwriting_revenue_mom_z_756d_v167_signal": {"func": f38_spec_underwriting_revenue_mom_z_756d_v167_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_756d_v168_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_756d_v168_signal},
    "f38_spec_underwriting_grossmargin_mom_z_1008d_v169_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_1008d_v169_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_1008d_v170_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_1008d_v170_signal},
    "f38_spec_underwriting_revenue_mom_z_1008d_v171_signal": {"func": f38_spec_underwriting_revenue_mom_z_1008d_v171_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_1008d_v172_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_1008d_v172_signal},
    "f38_spec_underwriting_grossmargin_mom_z_1260d_v173_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_1260d_v173_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_1260d_v174_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_1260d_v174_signal},
    "f38_spec_underwriting_revenue_mom_z_1260d_v175_signal": {"func": f38_spec_underwriting_revenue_mom_z_1260d_v175_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_1260d_v176_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_1260d_v176_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_5d_v177_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_5d_v177_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_5d_v178_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_5d_v178_signal},
    "f38_spec_underwriting_revenue_vol_slope_5d_v179_signal": {"func": f38_spec_underwriting_revenue_vol_slope_5d_v179_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_5d_v180_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_5d_v180_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_10d_v181_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_10d_v181_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_10d_v182_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_10d_v182_signal},
    "f38_spec_underwriting_revenue_vol_slope_10d_v183_signal": {"func": f38_spec_underwriting_revenue_vol_slope_10d_v183_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_10d_v184_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_10d_v184_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_21d_v185_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_21d_v185_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_21d_v186_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_21d_v186_signal},
    "f38_spec_underwriting_revenue_vol_slope_21d_v187_signal": {"func": f38_spec_underwriting_revenue_vol_slope_21d_v187_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_21d_v188_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_21d_v188_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_42d_v189_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_42d_v189_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_42d_v190_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_42d_v190_signal},
    "f38_spec_underwriting_revenue_vol_slope_42d_v191_signal": {"func": f38_spec_underwriting_revenue_vol_slope_42d_v191_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_42d_v192_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_42d_v192_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_63d_v193_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_63d_v193_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_63d_v194_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_63d_v194_signal},
    "f38_spec_underwriting_revenue_vol_slope_63d_v195_signal": {"func": f38_spec_underwriting_revenue_vol_slope_63d_v195_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_63d_v196_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_63d_v196_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_126d_v197_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_126d_v197_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_126d_v198_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_126d_v198_signal},
    "f38_spec_underwriting_revenue_vol_slope_126d_v199_signal": {"func": f38_spec_underwriting_revenue_vol_slope_126d_v199_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_126d_v200_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_126d_v200_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_252d_v201_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_252d_v201_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_252d_v202_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_252d_v202_signal},
    "f38_spec_underwriting_revenue_vol_slope_252d_v203_signal": {"func": f38_spec_underwriting_revenue_vol_slope_252d_v203_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_252d_v204_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_252d_v204_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_504d_v205_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_504d_v205_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_504d_v206_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_504d_v206_signal},
    "f38_spec_underwriting_revenue_vol_slope_504d_v207_signal": {"func": f38_spec_underwriting_revenue_vol_slope_504d_v207_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_504d_v208_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_504d_v208_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_756d_v209_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_756d_v209_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_756d_v210_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_756d_v210_signal},
    "f38_spec_underwriting_revenue_vol_slope_756d_v211_signal": {"func": f38_spec_underwriting_revenue_vol_slope_756d_v211_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_756d_v212_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_756d_v212_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_1008d_v213_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_1008d_v213_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_1008d_v214_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_1008d_v214_signal},
    "f38_spec_underwriting_revenue_vol_slope_1008d_v215_signal": {"func": f38_spec_underwriting_revenue_vol_slope_1008d_v215_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_1008d_v216_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_1008d_v216_signal},
    "f38_spec_underwriting_grossmargin_vol_slope_1260d_v217_signal": {"func": f38_spec_underwriting_grossmargin_vol_slope_1260d_v217_signal},
    "f38_spec_underwriting_ebitdamargin_vol_slope_1260d_v218_signal": {"func": f38_spec_underwriting_ebitdamargin_vol_slope_1260d_v218_signal},
    "f38_spec_underwriting_revenue_vol_slope_1260d_v219_signal": {"func": f38_spec_underwriting_revenue_vol_slope_1260d_v219_signal},
    "f38_spec_underwriting_uw_efficiency_vol_slope_1260d_v220_signal": {"func": f38_spec_underwriting_uw_efficiency_vol_slope_1260d_v220_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_5d_v221_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_5d_v221_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_5d_v222_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_5d_v222_signal},
    "f38_spec_underwriting_revenue_ewma_slope_5d_v223_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_5d_v223_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_5d_v224_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_5d_v224_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_10d_v225_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_10d_v225_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_10d_v226_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_10d_v226_signal},
    "f38_spec_underwriting_revenue_ewma_slope_10d_v227_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_10d_v227_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_10d_v228_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_10d_v228_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_21d_v229_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_21d_v229_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_21d_v230_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_21d_v230_signal},
    "f38_spec_underwriting_revenue_ewma_slope_21d_v231_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_21d_v231_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_21d_v232_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_21d_v232_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_42d_v233_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_42d_v233_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_42d_v234_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_42d_v234_signal},
    "f38_spec_underwriting_revenue_ewma_slope_42d_v235_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_42d_v235_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_42d_v236_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_42d_v236_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_63d_v237_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_63d_v237_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_63d_v238_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_63d_v238_signal},
    "f38_spec_underwriting_revenue_ewma_slope_63d_v239_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_63d_v239_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_63d_v240_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_63d_v240_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_126d_v241_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_126d_v241_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_126d_v242_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_126d_v242_signal},
    "f38_spec_underwriting_revenue_ewma_slope_126d_v243_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_126d_v243_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_126d_v244_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_126d_v244_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_252d_v245_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_252d_v245_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_252d_v246_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_252d_v246_signal},
    "f38_spec_underwriting_revenue_ewma_slope_252d_v247_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_252d_v247_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_252d_v248_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_252d_v248_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_504d_v249_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_504d_v249_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_504d_v250_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_504d_v250_signal},
    "f38_spec_underwriting_revenue_ewma_slope_504d_v251_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_504d_v251_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_504d_v252_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_504d_v252_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_756d_v253_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_756d_v253_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_756d_v254_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_756d_v254_signal},
    "f38_spec_underwriting_revenue_ewma_slope_756d_v255_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_756d_v255_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_756d_v256_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_756d_v256_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_1008d_v257_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_1008d_v257_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_1008d_v258_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_1008d_v258_signal},
    "f38_spec_underwriting_revenue_ewma_slope_1008d_v259_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_1008d_v259_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_1008d_v260_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_1008d_v260_signal},
    "f38_spec_underwriting_grossmargin_ewma_slope_1260d_v261_signal": {"func": f38_spec_underwriting_grossmargin_ewma_slope_1260d_v261_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_slope_1260d_v262_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_slope_1260d_v262_signal},
    "f38_spec_underwriting_revenue_ewma_slope_1260d_v263_signal": {"func": f38_spec_underwriting_revenue_ewma_slope_1260d_v263_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_slope_1260d_v264_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 38...")
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
