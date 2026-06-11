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

def f11_premium_pricing_moat_marketcap_mom_z_63d_v151_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_63d_v152_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 63d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_mom_z_126d_v153_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 126d window."""
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_mom_z_126d_v154_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 126d window."""
    res = _z(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_mom_z_126d_v155_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_126d_v156_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 126d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_mom_z_252d_v157_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 252d window."""
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_mom_z_252d_v158_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 252d window."""
    res = _z(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_mom_z_252d_v159_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_252d_v160_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 252d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_mom_z_504d_v161_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 504d window."""
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_mom_z_504d_v162_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 504d window."""
    res = _z(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_mom_z_504d_v163_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_504d_v164_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 504d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_mom_z_756d_v165_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 756d window."""
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_mom_z_756d_v166_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 756d window."""
    res = _z(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_mom_z_756d_v167_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_756d_v168_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 756d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_mom_z_1008d_v169_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1008d window."""
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_mom_z_1008d_v170_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 1008d window."""
    res = _z(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_mom_z_1008d_v171_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_1008d_v172_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 1008d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_mom_z_1260d_v173_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1260d window."""
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_mom_z_1260d_v174_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 1260d window."""
    res = _z(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_mom_z_1260d_v175_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_mom_z_1260d_v176_signal(grossmargin, ebitdamargin):
    """Relative momentum strength for Compound index of manufacturing and operating efficiency over 1260d window."""
    res = _z(_slope_pct(grossmargin * ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_5d_v177_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 5d window."""
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_5d_v178_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 5d window."""
    res = _std(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_5d_v179_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_5d_v180_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 5d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_10d_v181_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 10d window."""
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_10d_v182_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 10d window."""
    res = _std(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_10d_v183_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_10d_v184_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 10d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_21d_v185_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 21d window."""
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_21d_v186_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 21d window."""
    res = _std(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_21d_v187_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_21d_v188_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 21d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_42d_v189_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 42d window."""
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_42d_v190_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 42d window."""
    res = _std(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_42d_v191_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_42d_v192_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 42d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_63d_v193_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 63d window."""
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_63d_v194_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 63d window."""
    res = _std(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_63d_v195_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_63d_v196_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 63d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_126d_v197_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 126d window."""
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_126d_v198_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 126d window."""
    res = _std(_slope_pct(ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_126d_v199_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_126d_v200_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 126d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_252d_v201_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 252d window."""
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_252d_v202_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 252d window."""
    res = _std(_slope_pct(ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_252d_v203_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 252d window."""
    res = _std(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_252d_v204_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 252d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_504d_v205_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 504d window."""
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_504d_v206_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 504d window."""
    res = _std(_slope_pct(ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_504d_v207_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 504d window."""
    res = _std(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_504d_v208_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 504d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_756d_v209_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 756d window."""
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_756d_v210_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 756d window."""
    res = _std(_slope_pct(ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_756d_v211_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 756d window."""
    res = _std(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_756d_v212_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 756d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_1008d_v213_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 1008d window."""
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_1008d_v214_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 1008d window."""
    res = _std(_slope_pct(ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_1008d_v215_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 1008d window."""
    res = _std(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_1008d_v216_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 1008d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_vol_slope_1260d_v217_signal(grossmargin):
    """Volatility of the momentum for Raw level of grossmargin over 1260d window."""
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_vol_slope_1260d_v218_signal(ebitdamargin):
    """Volatility of the momentum for Raw level of ebitdamargin over 1260d window."""
    res = _std(_slope_pct(ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_vol_slope_1260d_v219_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 1260d window."""
    res = _std(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_vol_slope_1260d_v220_signal(grossmargin, ebitdamargin):
    """Volatility of the momentum for Compound index of manufacturing and operating efficiency over 1260d window."""
    res = _std(_slope_pct(grossmargin * ebitdamargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f11_premium_pricing_moat_marketcap_mom_z_63d_v151_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_63d_v151_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_63d_v152_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_63d_v152_signal},    "f11_premium_pricing_moat_grossmargin_mom_z_126d_v153_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_mom_z_126d_v153_signal},    "f11_premium_pricing_moat_ebitdamargin_mom_z_126d_v154_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_mom_z_126d_v154_signal},    "f11_premium_pricing_moat_marketcap_mom_z_126d_v155_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_126d_v155_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_126d_v156_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_126d_v156_signal},    "f11_premium_pricing_moat_grossmargin_mom_z_252d_v157_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_mom_z_252d_v157_signal},    "f11_premium_pricing_moat_ebitdamargin_mom_z_252d_v158_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_mom_z_252d_v158_signal},    "f11_premium_pricing_moat_marketcap_mom_z_252d_v159_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_252d_v159_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_252d_v160_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_252d_v160_signal},    "f11_premium_pricing_moat_grossmargin_mom_z_504d_v161_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_mom_z_504d_v161_signal},    "f11_premium_pricing_moat_ebitdamargin_mom_z_504d_v162_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_mom_z_504d_v162_signal},    "f11_premium_pricing_moat_marketcap_mom_z_504d_v163_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_504d_v163_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_504d_v164_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_504d_v164_signal},    "f11_premium_pricing_moat_grossmargin_mom_z_756d_v165_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_mom_z_756d_v165_signal},    "f11_premium_pricing_moat_ebitdamargin_mom_z_756d_v166_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_mom_z_756d_v166_signal},    "f11_premium_pricing_moat_marketcap_mom_z_756d_v167_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_756d_v167_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_756d_v168_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_756d_v168_signal},    "f11_premium_pricing_moat_grossmargin_mom_z_1008d_v169_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_mom_z_1008d_v169_signal},    "f11_premium_pricing_moat_ebitdamargin_mom_z_1008d_v170_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_mom_z_1008d_v170_signal},    "f11_premium_pricing_moat_marketcap_mom_z_1008d_v171_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_1008d_v171_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_1008d_v172_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_1008d_v172_signal},    "f11_premium_pricing_moat_grossmargin_mom_z_1260d_v173_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_mom_z_1260d_v173_signal},    "f11_premium_pricing_moat_ebitdamargin_mom_z_1260d_v174_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_mom_z_1260d_v174_signal},    "f11_premium_pricing_moat_marketcap_mom_z_1260d_v175_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_mom_z_1260d_v175_signal},    "f11_premium_pricing_moat_pricing_power_index_mom_z_1260d_v176_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_mom_z_1260d_v176_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_5d_v177_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_5d_v177_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_5d_v178_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_5d_v178_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_5d_v179_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_5d_v179_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_5d_v180_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_5d_v180_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_10d_v181_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_10d_v181_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_10d_v182_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_10d_v182_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_10d_v183_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_10d_v183_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_10d_v184_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_10d_v184_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_21d_v185_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_21d_v185_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_21d_v186_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_21d_v186_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_21d_v187_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_21d_v187_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_21d_v188_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_21d_v188_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_42d_v189_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_42d_v189_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_42d_v190_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_42d_v190_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_42d_v191_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_42d_v191_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_42d_v192_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_42d_v192_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_63d_v193_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_63d_v193_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_63d_v194_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_63d_v194_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_63d_v195_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_63d_v195_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_63d_v196_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_63d_v196_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_126d_v197_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_126d_v197_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_126d_v198_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_126d_v198_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_126d_v199_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_126d_v199_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_126d_v200_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_126d_v200_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_252d_v201_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_252d_v201_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_252d_v202_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_252d_v202_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_252d_v203_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_252d_v203_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_252d_v204_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_252d_v204_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_504d_v205_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_504d_v205_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_504d_v206_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_504d_v206_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_504d_v207_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_504d_v207_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_504d_v208_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_504d_v208_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_756d_v209_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_756d_v209_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_756d_v210_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_756d_v210_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_756d_v211_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_756d_v211_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_756d_v212_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_756d_v212_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_1008d_v213_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_1008d_v213_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_1008d_v214_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_1008d_v214_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_1008d_v215_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_1008d_v215_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_1008d_v216_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_1008d_v216_signal},    "f11_premium_pricing_moat_grossmargin_vol_slope_1260d_v217_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_vol_slope_1260d_v217_signal},    "f11_premium_pricing_moat_ebitdamargin_vol_slope_1260d_v218_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_vol_slope_1260d_v218_signal},    "f11_premium_pricing_moat_marketcap_vol_slope_1260d_v219_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_vol_slope_1260d_v219_signal},    "f11_premium_pricing_moat_pricing_power_index_vol_slope_1260d_v220_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
