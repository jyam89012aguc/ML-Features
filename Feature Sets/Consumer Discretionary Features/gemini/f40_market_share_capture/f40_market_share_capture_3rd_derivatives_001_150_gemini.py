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

def f40_market_share_capture_shareswa_mom_z_63d_v151_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 63d window."""
    res = _z(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_63d_v152_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_mom_z_126d_v153_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_mom_z_126d_v154_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_mom_z_126d_v155_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 126d window."""
    res = _z(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_126d_v156_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_mom_z_252d_v157_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_mom_z_252d_v158_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_mom_z_252d_v159_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 252d window."""
    res = _z(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_252d_v160_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_mom_z_504d_v161_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_mom_z_504d_v162_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_mom_z_504d_v163_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 504d window."""
    res = _z(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_504d_v164_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_mom_z_756d_v165_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_mom_z_756d_v166_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_mom_z_756d_v167_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 756d window."""
    res = _z(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_756d_v168_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_mom_z_1008d_v169_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_mom_z_1008d_v170_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_mom_z_1008d_v171_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 1008d window."""
    res = _z(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_1008d_v172_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_mom_z_1260d_v173_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_mom_z_1260d_v174_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_mom_z_1260d_v175_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 1260d window."""
    res = _z(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_mom_z_1260d_v176_signal(revenue, shareswa):
    """Relative momentum strength for Sales productivity per share over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, shareswa), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_5d_v177_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_5d_v178_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_5d_v179_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 5d window."""
    res = _std(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_5d_v180_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_10d_v181_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_10d_v182_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_10d_v183_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 10d window."""
    res = _std(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_10d_v184_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_21d_v185_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_21d_v186_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_21d_v187_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 21d window."""
    res = _std(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_21d_v188_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_42d_v189_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_42d_v190_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_42d_v191_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 42d window."""
    res = _std(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_42d_v192_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_63d_v193_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_63d_v194_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_63d_v195_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 63d window."""
    res = _std(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_63d_v196_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_126d_v197_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_126d_v198_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_126d_v199_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 126d window."""
    res = _std(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_126d_v200_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_252d_v201_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_252d_v202_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 252d window."""
    res = _std(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_252d_v203_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 252d window."""
    res = _std(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_252d_v204_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_504d_v205_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_504d_v206_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 504d window."""
    res = _std(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_504d_v207_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 504d window."""
    res = _std(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_504d_v208_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_756d_v209_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_756d_v210_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 756d window."""
    res = _std(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_756d_v211_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 756d window."""
    res = _std(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_756d_v212_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_1008d_v213_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_1008d_v214_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 1008d window."""
    res = _std(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_1008d_v215_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 1008d window."""
    res = _std(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_1008d_v216_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_vol_slope_1260d_v217_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_marketcap_vol_slope_1260d_v218_signal(marketcap):
    """Volatility of the momentum for Raw level of marketcap over 1260d window."""
    res = _std(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_shareswa_vol_slope_1260d_v219_signal(shareswa):
    """Volatility of the momentum for Raw level of shareswa over 1260d window."""
    res = _std(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_market_share_capture_revenue_per_share_vol_slope_1260d_v220_signal(revenue, shareswa):
    """Volatility of the momentum for Sales productivity per share over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, shareswa), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f40_market_share_capture_shareswa_mom_z_63d_v151_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_63d_v151_signal},    "f40_market_share_capture_revenue_per_share_mom_z_63d_v152_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_63d_v152_signal},    "f40_market_share_capture_revenue_mom_z_126d_v153_signal": {"inputs": [], "func": f40_market_share_capture_revenue_mom_z_126d_v153_signal},    "f40_market_share_capture_marketcap_mom_z_126d_v154_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_mom_z_126d_v154_signal},    "f40_market_share_capture_shareswa_mom_z_126d_v155_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_126d_v155_signal},    "f40_market_share_capture_revenue_per_share_mom_z_126d_v156_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_126d_v156_signal},    "f40_market_share_capture_revenue_mom_z_252d_v157_signal": {"inputs": [], "func": f40_market_share_capture_revenue_mom_z_252d_v157_signal},    "f40_market_share_capture_marketcap_mom_z_252d_v158_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_mom_z_252d_v158_signal},    "f40_market_share_capture_shareswa_mom_z_252d_v159_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_252d_v159_signal},    "f40_market_share_capture_revenue_per_share_mom_z_252d_v160_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_252d_v160_signal},    "f40_market_share_capture_revenue_mom_z_504d_v161_signal": {"inputs": [], "func": f40_market_share_capture_revenue_mom_z_504d_v161_signal},    "f40_market_share_capture_marketcap_mom_z_504d_v162_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_mom_z_504d_v162_signal},    "f40_market_share_capture_shareswa_mom_z_504d_v163_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_504d_v163_signal},    "f40_market_share_capture_revenue_per_share_mom_z_504d_v164_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_504d_v164_signal},    "f40_market_share_capture_revenue_mom_z_756d_v165_signal": {"inputs": [], "func": f40_market_share_capture_revenue_mom_z_756d_v165_signal},    "f40_market_share_capture_marketcap_mom_z_756d_v166_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_mom_z_756d_v166_signal},    "f40_market_share_capture_shareswa_mom_z_756d_v167_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_756d_v167_signal},    "f40_market_share_capture_revenue_per_share_mom_z_756d_v168_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_756d_v168_signal},    "f40_market_share_capture_revenue_mom_z_1008d_v169_signal": {"inputs": [], "func": f40_market_share_capture_revenue_mom_z_1008d_v169_signal},    "f40_market_share_capture_marketcap_mom_z_1008d_v170_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_mom_z_1008d_v170_signal},    "f40_market_share_capture_shareswa_mom_z_1008d_v171_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_1008d_v171_signal},    "f40_market_share_capture_revenue_per_share_mom_z_1008d_v172_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_1008d_v172_signal},    "f40_market_share_capture_revenue_mom_z_1260d_v173_signal": {"inputs": [], "func": f40_market_share_capture_revenue_mom_z_1260d_v173_signal},    "f40_market_share_capture_marketcap_mom_z_1260d_v174_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_mom_z_1260d_v174_signal},    "f40_market_share_capture_shareswa_mom_z_1260d_v175_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_mom_z_1260d_v175_signal},    "f40_market_share_capture_revenue_per_share_mom_z_1260d_v176_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_mom_z_1260d_v176_signal},    "f40_market_share_capture_revenue_vol_slope_5d_v177_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_5d_v177_signal},    "f40_market_share_capture_marketcap_vol_slope_5d_v178_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_5d_v178_signal},    "f40_market_share_capture_shareswa_vol_slope_5d_v179_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_5d_v179_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_5d_v180_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_5d_v180_signal},    "f40_market_share_capture_revenue_vol_slope_10d_v181_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_10d_v181_signal},    "f40_market_share_capture_marketcap_vol_slope_10d_v182_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_10d_v182_signal},    "f40_market_share_capture_shareswa_vol_slope_10d_v183_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_10d_v183_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_10d_v184_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_10d_v184_signal},    "f40_market_share_capture_revenue_vol_slope_21d_v185_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_21d_v185_signal},    "f40_market_share_capture_marketcap_vol_slope_21d_v186_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_21d_v186_signal},    "f40_market_share_capture_shareswa_vol_slope_21d_v187_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_21d_v187_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_21d_v188_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_21d_v188_signal},    "f40_market_share_capture_revenue_vol_slope_42d_v189_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_42d_v189_signal},    "f40_market_share_capture_marketcap_vol_slope_42d_v190_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_42d_v190_signal},    "f40_market_share_capture_shareswa_vol_slope_42d_v191_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_42d_v191_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_42d_v192_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_42d_v192_signal},    "f40_market_share_capture_revenue_vol_slope_63d_v193_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_63d_v193_signal},    "f40_market_share_capture_marketcap_vol_slope_63d_v194_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_63d_v194_signal},    "f40_market_share_capture_shareswa_vol_slope_63d_v195_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_63d_v195_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_63d_v196_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_63d_v196_signal},    "f40_market_share_capture_revenue_vol_slope_126d_v197_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_126d_v197_signal},    "f40_market_share_capture_marketcap_vol_slope_126d_v198_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_126d_v198_signal},    "f40_market_share_capture_shareswa_vol_slope_126d_v199_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_126d_v199_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_126d_v200_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_126d_v200_signal},    "f40_market_share_capture_revenue_vol_slope_252d_v201_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_252d_v201_signal},    "f40_market_share_capture_marketcap_vol_slope_252d_v202_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_252d_v202_signal},    "f40_market_share_capture_shareswa_vol_slope_252d_v203_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_252d_v203_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_252d_v204_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_252d_v204_signal},    "f40_market_share_capture_revenue_vol_slope_504d_v205_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_504d_v205_signal},    "f40_market_share_capture_marketcap_vol_slope_504d_v206_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_504d_v206_signal},    "f40_market_share_capture_shareswa_vol_slope_504d_v207_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_504d_v207_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_504d_v208_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_504d_v208_signal},    "f40_market_share_capture_revenue_vol_slope_756d_v209_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_756d_v209_signal},    "f40_market_share_capture_marketcap_vol_slope_756d_v210_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_756d_v210_signal},    "f40_market_share_capture_shareswa_vol_slope_756d_v211_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_756d_v211_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_756d_v212_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_756d_v212_signal},    "f40_market_share_capture_revenue_vol_slope_1008d_v213_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_1008d_v213_signal},    "f40_market_share_capture_marketcap_vol_slope_1008d_v214_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_1008d_v214_signal},    "f40_market_share_capture_shareswa_vol_slope_1008d_v215_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_1008d_v215_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_1008d_v216_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_1008d_v216_signal},    "f40_market_share_capture_revenue_vol_slope_1260d_v217_signal": {"inputs": [], "func": f40_market_share_capture_revenue_vol_slope_1260d_v217_signal},    "f40_market_share_capture_marketcap_vol_slope_1260d_v218_signal": {"inputs": [], "func": f40_market_share_capture_marketcap_vol_slope_1260d_v218_signal},    "f40_market_share_capture_shareswa_vol_slope_1260d_v219_signal": {"inputs": [], "func": f40_market_share_capture_shareswa_vol_slope_1260d_v219_signal},    "f40_market_share_capture_revenue_per_share_vol_slope_1260d_v220_signal": {"inputs": [], "func": f40_market_share_capture_revenue_per_share_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 40...")
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
