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

def f37_brand_margin_expansion_revenue_mom_z_63d_v151_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_63d_v152_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 63d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_mom_z_126d_v153_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 126d window."""
    res = _z(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_mom_z_126d_v154_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 126d window."""
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_mom_z_126d_v155_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_126d_v156_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 126d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_mom_z_252d_v157_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 252d window."""
    res = _z(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_mom_z_252d_v158_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 252d window."""
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_mom_z_252d_v159_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_252d_v160_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 252d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_mom_z_504d_v161_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 504d window."""
    res = _z(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_mom_z_504d_v162_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 504d window."""
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_mom_z_504d_v163_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_504d_v164_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 504d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_mom_z_756d_v165_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 756d window."""
    res = _z(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_mom_z_756d_v166_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 756d window."""
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_mom_z_756d_v167_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_756d_v168_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 756d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_mom_z_1008d_v169_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 1008d window."""
    res = _z(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_mom_z_1008d_v170_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1008d window."""
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_mom_z_1008d_v171_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_1008d_v172_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 1008d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_mom_z_1260d_v173_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 1260d window."""
    res = _z(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_mom_z_1260d_v174_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1260d window."""
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_mom_z_1260d_v175_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_mom_z_1260d_v176_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Conversion of gross profit to operating profit over 1260d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_5d_v177_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 5d window."""
    res = _std(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_5d_v178_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 5d window."""
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_5d_v179_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_5d_v180_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 5d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_10d_v181_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 10d window."""
    res = _std(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_10d_v182_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 10d window."""
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_10d_v183_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_10d_v184_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 10d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_21d_v185_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 21d window."""
    res = _std(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_21d_v186_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 21d window."""
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_21d_v187_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_21d_v188_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 21d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_42d_v189_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 42d window."""
    res = _std(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_42d_v190_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 42d window."""
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_42d_v191_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_42d_v192_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 42d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_63d_v193_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 63d window."""
    res = _std(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_63d_v194_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 63d window."""
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_63d_v195_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_63d_v196_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 63d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_126d_v197_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 126d window."""
    res = _std(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_126d_v198_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 126d window."""
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_126d_v199_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_126d_v200_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 126d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_252d_v201_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 252d window."""
    res = _std(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_252d_v202_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 252d window."""
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_252d_v203_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_252d_v204_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 252d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_504d_v205_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 504d window."""
    res = _std(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_504d_v206_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 504d window."""
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_504d_v207_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_504d_v208_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 504d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_756d_v209_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 756d window."""
    res = _std(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_756d_v210_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 756d window."""
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_756d_v211_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_756d_v212_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 756d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_1008d_v213_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 1008d window."""
    res = _std(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_1008d_v214_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 1008d window."""
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_1008d_v215_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_1008d_v216_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 1008d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_ebitdamargin_vol_slope_1260d_v217_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 1260d window."""
    res = _std(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_grossmargin_vol_slope_1260d_v218_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 1260d window."""
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_revenue_vol_slope_1260d_v219_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_brand_margin_expansion_operating_efficiency_vol_slope_1260d_v220_signal(ebitdamargin, grossmargin):
    """Volatility of the momentum for Conversion of gross profit to operating profit over 1260d window."""
    res = _std(_slope_pct(_ratio(ebitdamargin, grossmargin), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f37_brand_margin_expansion_revenue_mom_z_63d_v151_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_63d_v151_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_63d_v152_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_63d_v152_signal},    "f37_brand_margin_expansion_ebitdamargin_mom_z_126d_v153_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_mom_z_126d_v153_signal},    "f37_brand_margin_expansion_grossmargin_mom_z_126d_v154_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_mom_z_126d_v154_signal},    "f37_brand_margin_expansion_revenue_mom_z_126d_v155_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_126d_v155_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_126d_v156_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_126d_v156_signal},    "f37_brand_margin_expansion_ebitdamargin_mom_z_252d_v157_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_mom_z_252d_v157_signal},    "f37_brand_margin_expansion_grossmargin_mom_z_252d_v158_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_mom_z_252d_v158_signal},    "f37_brand_margin_expansion_revenue_mom_z_252d_v159_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_252d_v159_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_252d_v160_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_252d_v160_signal},    "f37_brand_margin_expansion_ebitdamargin_mom_z_504d_v161_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_mom_z_504d_v161_signal},    "f37_brand_margin_expansion_grossmargin_mom_z_504d_v162_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_mom_z_504d_v162_signal},    "f37_brand_margin_expansion_revenue_mom_z_504d_v163_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_504d_v163_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_504d_v164_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_504d_v164_signal},    "f37_brand_margin_expansion_ebitdamargin_mom_z_756d_v165_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_mom_z_756d_v165_signal},    "f37_brand_margin_expansion_grossmargin_mom_z_756d_v166_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_mom_z_756d_v166_signal},    "f37_brand_margin_expansion_revenue_mom_z_756d_v167_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_756d_v167_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_756d_v168_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_756d_v168_signal},    "f37_brand_margin_expansion_ebitdamargin_mom_z_1008d_v169_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_mom_z_1008d_v169_signal},    "f37_brand_margin_expansion_grossmargin_mom_z_1008d_v170_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_mom_z_1008d_v170_signal},    "f37_brand_margin_expansion_revenue_mom_z_1008d_v171_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_1008d_v171_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_1008d_v172_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_1008d_v172_signal},    "f37_brand_margin_expansion_ebitdamargin_mom_z_1260d_v173_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_mom_z_1260d_v173_signal},    "f37_brand_margin_expansion_grossmargin_mom_z_1260d_v174_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_mom_z_1260d_v174_signal},    "f37_brand_margin_expansion_revenue_mom_z_1260d_v175_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_mom_z_1260d_v175_signal},    "f37_brand_margin_expansion_operating_efficiency_mom_z_1260d_v176_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_mom_z_1260d_v176_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_5d_v177_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_5d_v177_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_5d_v178_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_5d_v178_signal},    "f37_brand_margin_expansion_revenue_vol_slope_5d_v179_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_5d_v179_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_5d_v180_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_5d_v180_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_10d_v181_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_10d_v181_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_10d_v182_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_10d_v182_signal},    "f37_brand_margin_expansion_revenue_vol_slope_10d_v183_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_10d_v183_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_10d_v184_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_10d_v184_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_21d_v185_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_21d_v185_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_21d_v186_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_21d_v186_signal},    "f37_brand_margin_expansion_revenue_vol_slope_21d_v187_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_21d_v187_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_21d_v188_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_21d_v188_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_42d_v189_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_42d_v189_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_42d_v190_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_42d_v190_signal},    "f37_brand_margin_expansion_revenue_vol_slope_42d_v191_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_42d_v191_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_42d_v192_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_42d_v192_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_63d_v193_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_63d_v193_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_63d_v194_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_63d_v194_signal},    "f37_brand_margin_expansion_revenue_vol_slope_63d_v195_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_63d_v195_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_63d_v196_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_63d_v196_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_126d_v197_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_126d_v197_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_126d_v198_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_126d_v198_signal},    "f37_brand_margin_expansion_revenue_vol_slope_126d_v199_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_126d_v199_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_126d_v200_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_126d_v200_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_252d_v201_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_252d_v201_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_252d_v202_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_252d_v202_signal},    "f37_brand_margin_expansion_revenue_vol_slope_252d_v203_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_252d_v203_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_252d_v204_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_252d_v204_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_504d_v205_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_504d_v205_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_504d_v206_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_504d_v206_signal},    "f37_brand_margin_expansion_revenue_vol_slope_504d_v207_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_504d_v207_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_504d_v208_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_504d_v208_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_756d_v209_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_756d_v209_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_756d_v210_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_756d_v210_signal},    "f37_brand_margin_expansion_revenue_vol_slope_756d_v211_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_756d_v211_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_756d_v212_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_756d_v212_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_1008d_v213_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_1008d_v213_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_1008d_v214_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_1008d_v214_signal},    "f37_brand_margin_expansion_revenue_vol_slope_1008d_v215_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_1008d_v215_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_1008d_v216_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_1008d_v216_signal},    "f37_brand_margin_expansion_ebitdamargin_vol_slope_1260d_v217_signal": {"inputs": [], "func": f37_brand_margin_expansion_ebitdamargin_vol_slope_1260d_v217_signal},    "f37_brand_margin_expansion_grossmargin_vol_slope_1260d_v218_signal": {"inputs": [], "func": f37_brand_margin_expansion_grossmargin_vol_slope_1260d_v218_signal},    "f37_brand_margin_expansion_revenue_vol_slope_1260d_v219_signal": {"inputs": [], "func": f37_brand_margin_expansion_revenue_vol_slope_1260d_v219_signal},    "f37_brand_margin_expansion_operating_efficiency_vol_slope_1260d_v220_signal": {"inputs": [], "func": f37_brand_margin_expansion_operating_efficiency_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 37...")
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
