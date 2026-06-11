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

def f48_valuation_reversion_ev_mom_z_63d_v151_signal(ev):
    """Relative momentum strength for Raw level of ev over 63d window."""
    res = _z(_slope_pct(ev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_63d_v152_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 63d window."""
    res = _z(_slope_pct(_z(ps, 1260), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_mom_z_126d_v153_signal(pe):
    """Relative momentum strength for Raw level of pe over 126d window."""
    res = _z(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_mom_z_126d_v154_signal(ps):
    """Relative momentum strength for Raw level of ps over 126d window."""
    res = _z(_slope_pct(ps, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_mom_z_126d_v155_signal(ev):
    """Relative momentum strength for Raw level of ev over 126d window."""
    res = _z(_slope_pct(ev, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_126d_v156_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 126d window."""
    res = _z(_slope_pct(_z(ps, 1260), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_mom_z_252d_v157_signal(pe):
    """Relative momentum strength for Raw level of pe over 252d window."""
    res = _z(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_mom_z_252d_v158_signal(ps):
    """Relative momentum strength for Raw level of ps over 252d window."""
    res = _z(_slope_pct(ps, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_mom_z_252d_v159_signal(ev):
    """Relative momentum strength for Raw level of ev over 252d window."""
    res = _z(_slope_pct(ev, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_252d_v160_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 252d window."""
    res = _z(_slope_pct(_z(ps, 1260), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_mom_z_504d_v161_signal(pe):
    """Relative momentum strength for Raw level of pe over 504d window."""
    res = _z(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_mom_z_504d_v162_signal(ps):
    """Relative momentum strength for Raw level of ps over 504d window."""
    res = _z(_slope_pct(ps, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_mom_z_504d_v163_signal(ev):
    """Relative momentum strength for Raw level of ev over 504d window."""
    res = _z(_slope_pct(ev, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_504d_v164_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 504d window."""
    res = _z(_slope_pct(_z(ps, 1260), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_mom_z_756d_v165_signal(pe):
    """Relative momentum strength for Raw level of pe over 756d window."""
    res = _z(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_mom_z_756d_v166_signal(ps):
    """Relative momentum strength for Raw level of ps over 756d window."""
    res = _z(_slope_pct(ps, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_mom_z_756d_v167_signal(ev):
    """Relative momentum strength for Raw level of ev over 756d window."""
    res = _z(_slope_pct(ev, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_756d_v168_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 756d window."""
    res = _z(_slope_pct(_z(ps, 1260), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_mom_z_1008d_v169_signal(pe):
    """Relative momentum strength for Raw level of pe over 1008d window."""
    res = _z(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_mom_z_1008d_v170_signal(ps):
    """Relative momentum strength for Raw level of ps over 1008d window."""
    res = _z(_slope_pct(ps, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_mom_z_1008d_v171_signal(ev):
    """Relative momentum strength for Raw level of ev over 1008d window."""
    res = _z(_slope_pct(ev, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_1008d_v172_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 1008d window."""
    res = _z(_slope_pct(_z(ps, 1260), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_mom_z_1260d_v173_signal(pe):
    """Relative momentum strength for Raw level of pe over 1260d window."""
    res = _z(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_mom_z_1260d_v174_signal(ps):
    """Relative momentum strength for Raw level of ps over 1260d window."""
    res = _z(_slope_pct(ps, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_mom_z_1260d_v175_signal(ev):
    """Relative momentum strength for Raw level of ev over 1260d window."""
    res = _z(_slope_pct(ev, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_mom_z_1260d_v176_signal(ps):
    """Relative momentum strength for Z-score of Price-to-Sales relative to 5y history over 1260d window."""
    res = _z(_slope_pct(_z(ps, 1260), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_5d_v177_signal(pe):
    """Volatility of the momentum for Raw level of pe over 5d window."""
    res = _std(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_5d_v178_signal(ps):
    """Volatility of the momentum for Raw level of ps over 5d window."""
    res = _std(_slope_pct(ps, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_5d_v179_signal(ev):
    """Volatility of the momentum for Raw level of ev over 5d window."""
    res = _std(_slope_pct(ev, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_5d_v180_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 5d window."""
    res = _std(_slope_pct(_z(ps, 1260), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_10d_v181_signal(pe):
    """Volatility of the momentum for Raw level of pe over 10d window."""
    res = _std(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_10d_v182_signal(ps):
    """Volatility of the momentum for Raw level of ps over 10d window."""
    res = _std(_slope_pct(ps, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_10d_v183_signal(ev):
    """Volatility of the momentum for Raw level of ev over 10d window."""
    res = _std(_slope_pct(ev, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_10d_v184_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 10d window."""
    res = _std(_slope_pct(_z(ps, 1260), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_21d_v185_signal(pe):
    """Volatility of the momentum for Raw level of pe over 21d window."""
    res = _std(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_21d_v186_signal(ps):
    """Volatility of the momentum for Raw level of ps over 21d window."""
    res = _std(_slope_pct(ps, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_21d_v187_signal(ev):
    """Volatility of the momentum for Raw level of ev over 21d window."""
    res = _std(_slope_pct(ev, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_21d_v188_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 21d window."""
    res = _std(_slope_pct(_z(ps, 1260), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_42d_v189_signal(pe):
    """Volatility of the momentum for Raw level of pe over 42d window."""
    res = _std(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_42d_v190_signal(ps):
    """Volatility of the momentum for Raw level of ps over 42d window."""
    res = _std(_slope_pct(ps, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_42d_v191_signal(ev):
    """Volatility of the momentum for Raw level of ev over 42d window."""
    res = _std(_slope_pct(ev, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_42d_v192_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 42d window."""
    res = _std(_slope_pct(_z(ps, 1260), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_63d_v193_signal(pe):
    """Volatility of the momentum for Raw level of pe over 63d window."""
    res = _std(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_63d_v194_signal(ps):
    """Volatility of the momentum for Raw level of ps over 63d window."""
    res = _std(_slope_pct(ps, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_63d_v195_signal(ev):
    """Volatility of the momentum for Raw level of ev over 63d window."""
    res = _std(_slope_pct(ev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_63d_v196_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 63d window."""
    res = _std(_slope_pct(_z(ps, 1260), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_126d_v197_signal(pe):
    """Volatility of the momentum for Raw level of pe over 126d window."""
    res = _std(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_126d_v198_signal(ps):
    """Volatility of the momentum for Raw level of ps over 126d window."""
    res = _std(_slope_pct(ps, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_126d_v199_signal(ev):
    """Volatility of the momentum for Raw level of ev over 126d window."""
    res = _std(_slope_pct(ev, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_126d_v200_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 126d window."""
    res = _std(_slope_pct(_z(ps, 1260), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_252d_v201_signal(pe):
    """Volatility of the momentum for Raw level of pe over 252d window."""
    res = _std(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_252d_v202_signal(ps):
    """Volatility of the momentum for Raw level of ps over 252d window."""
    res = _std(_slope_pct(ps, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_252d_v203_signal(ev):
    """Volatility of the momentum for Raw level of ev over 252d window."""
    res = _std(_slope_pct(ev, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_252d_v204_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 252d window."""
    res = _std(_slope_pct(_z(ps, 1260), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_504d_v205_signal(pe):
    """Volatility of the momentum for Raw level of pe over 504d window."""
    res = _std(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_504d_v206_signal(ps):
    """Volatility of the momentum for Raw level of ps over 504d window."""
    res = _std(_slope_pct(ps, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_504d_v207_signal(ev):
    """Volatility of the momentum for Raw level of ev over 504d window."""
    res = _std(_slope_pct(ev, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_504d_v208_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 504d window."""
    res = _std(_slope_pct(_z(ps, 1260), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_756d_v209_signal(pe):
    """Volatility of the momentum for Raw level of pe over 756d window."""
    res = _std(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_756d_v210_signal(ps):
    """Volatility of the momentum for Raw level of ps over 756d window."""
    res = _std(_slope_pct(ps, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_756d_v211_signal(ev):
    """Volatility of the momentum for Raw level of ev over 756d window."""
    res = _std(_slope_pct(ev, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_756d_v212_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 756d window."""
    res = _std(_slope_pct(_z(ps, 1260), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_1008d_v213_signal(pe):
    """Volatility of the momentum for Raw level of pe over 1008d window."""
    res = _std(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_1008d_v214_signal(ps):
    """Volatility of the momentum for Raw level of ps over 1008d window."""
    res = _std(_slope_pct(ps, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_1008d_v215_signal(ev):
    """Volatility of the momentum for Raw level of ev over 1008d window."""
    res = _std(_slope_pct(ev, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_1008d_v216_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 1008d window."""
    res = _std(_slope_pct(_z(ps, 1260), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_vol_slope_1260d_v217_signal(pe):
    """Volatility of the momentum for Raw level of pe over 1260d window."""
    res = _std(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_vol_slope_1260d_v218_signal(ps):
    """Volatility of the momentum for Raw level of ps over 1260d window."""
    res = _std(_slope_pct(ps, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_vol_slope_1260d_v219_signal(ev):
    """Volatility of the momentum for Raw level of ev over 1260d window."""
    res = _std(_slope_pct(ev, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_vol_slope_1260d_v220_signal(ps):
    """Volatility of the momentum for Z-score of Price-to-Sales relative to 5y history over 1260d window."""
    res = _std(_slope_pct(_z(ps, 1260), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f48_valuation_reversion_ev_mom_z_63d_v151_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_63d_v151_signal},    "f48_valuation_reversion_ps_z_mom_z_63d_v152_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_63d_v152_signal},    "f48_valuation_reversion_pe_mom_z_126d_v153_signal": {"inputs": [], "func": f48_valuation_reversion_pe_mom_z_126d_v153_signal},    "f48_valuation_reversion_ps_mom_z_126d_v154_signal": {"inputs": [], "func": f48_valuation_reversion_ps_mom_z_126d_v154_signal},    "f48_valuation_reversion_ev_mom_z_126d_v155_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_126d_v155_signal},    "f48_valuation_reversion_ps_z_mom_z_126d_v156_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_126d_v156_signal},    "f48_valuation_reversion_pe_mom_z_252d_v157_signal": {"inputs": [], "func": f48_valuation_reversion_pe_mom_z_252d_v157_signal},    "f48_valuation_reversion_ps_mom_z_252d_v158_signal": {"inputs": [], "func": f48_valuation_reversion_ps_mom_z_252d_v158_signal},    "f48_valuation_reversion_ev_mom_z_252d_v159_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_252d_v159_signal},    "f48_valuation_reversion_ps_z_mom_z_252d_v160_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_252d_v160_signal},    "f48_valuation_reversion_pe_mom_z_504d_v161_signal": {"inputs": [], "func": f48_valuation_reversion_pe_mom_z_504d_v161_signal},    "f48_valuation_reversion_ps_mom_z_504d_v162_signal": {"inputs": [], "func": f48_valuation_reversion_ps_mom_z_504d_v162_signal},    "f48_valuation_reversion_ev_mom_z_504d_v163_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_504d_v163_signal},    "f48_valuation_reversion_ps_z_mom_z_504d_v164_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_504d_v164_signal},    "f48_valuation_reversion_pe_mom_z_756d_v165_signal": {"inputs": [], "func": f48_valuation_reversion_pe_mom_z_756d_v165_signal},    "f48_valuation_reversion_ps_mom_z_756d_v166_signal": {"inputs": [], "func": f48_valuation_reversion_ps_mom_z_756d_v166_signal},    "f48_valuation_reversion_ev_mom_z_756d_v167_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_756d_v167_signal},    "f48_valuation_reversion_ps_z_mom_z_756d_v168_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_756d_v168_signal},    "f48_valuation_reversion_pe_mom_z_1008d_v169_signal": {"inputs": [], "func": f48_valuation_reversion_pe_mom_z_1008d_v169_signal},    "f48_valuation_reversion_ps_mom_z_1008d_v170_signal": {"inputs": [], "func": f48_valuation_reversion_ps_mom_z_1008d_v170_signal},    "f48_valuation_reversion_ev_mom_z_1008d_v171_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_1008d_v171_signal},    "f48_valuation_reversion_ps_z_mom_z_1008d_v172_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_1008d_v172_signal},    "f48_valuation_reversion_pe_mom_z_1260d_v173_signal": {"inputs": [], "func": f48_valuation_reversion_pe_mom_z_1260d_v173_signal},    "f48_valuation_reversion_ps_mom_z_1260d_v174_signal": {"inputs": [], "func": f48_valuation_reversion_ps_mom_z_1260d_v174_signal},    "f48_valuation_reversion_ev_mom_z_1260d_v175_signal": {"inputs": [], "func": f48_valuation_reversion_ev_mom_z_1260d_v175_signal},    "f48_valuation_reversion_ps_z_mom_z_1260d_v176_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_mom_z_1260d_v176_signal},    "f48_valuation_reversion_pe_vol_slope_5d_v177_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_5d_v177_signal},    "f48_valuation_reversion_ps_vol_slope_5d_v178_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_5d_v178_signal},    "f48_valuation_reversion_ev_vol_slope_5d_v179_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_5d_v179_signal},    "f48_valuation_reversion_ps_z_vol_slope_5d_v180_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_5d_v180_signal},    "f48_valuation_reversion_pe_vol_slope_10d_v181_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_10d_v181_signal},    "f48_valuation_reversion_ps_vol_slope_10d_v182_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_10d_v182_signal},    "f48_valuation_reversion_ev_vol_slope_10d_v183_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_10d_v183_signal},    "f48_valuation_reversion_ps_z_vol_slope_10d_v184_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_10d_v184_signal},    "f48_valuation_reversion_pe_vol_slope_21d_v185_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_21d_v185_signal},    "f48_valuation_reversion_ps_vol_slope_21d_v186_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_21d_v186_signal},    "f48_valuation_reversion_ev_vol_slope_21d_v187_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_21d_v187_signal},    "f48_valuation_reversion_ps_z_vol_slope_21d_v188_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_21d_v188_signal},    "f48_valuation_reversion_pe_vol_slope_42d_v189_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_42d_v189_signal},    "f48_valuation_reversion_ps_vol_slope_42d_v190_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_42d_v190_signal},    "f48_valuation_reversion_ev_vol_slope_42d_v191_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_42d_v191_signal},    "f48_valuation_reversion_ps_z_vol_slope_42d_v192_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_42d_v192_signal},    "f48_valuation_reversion_pe_vol_slope_63d_v193_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_63d_v193_signal},    "f48_valuation_reversion_ps_vol_slope_63d_v194_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_63d_v194_signal},    "f48_valuation_reversion_ev_vol_slope_63d_v195_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_63d_v195_signal},    "f48_valuation_reversion_ps_z_vol_slope_63d_v196_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_63d_v196_signal},    "f48_valuation_reversion_pe_vol_slope_126d_v197_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_126d_v197_signal},    "f48_valuation_reversion_ps_vol_slope_126d_v198_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_126d_v198_signal},    "f48_valuation_reversion_ev_vol_slope_126d_v199_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_126d_v199_signal},    "f48_valuation_reversion_ps_z_vol_slope_126d_v200_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_126d_v200_signal},    "f48_valuation_reversion_pe_vol_slope_252d_v201_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_252d_v201_signal},    "f48_valuation_reversion_ps_vol_slope_252d_v202_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_252d_v202_signal},    "f48_valuation_reversion_ev_vol_slope_252d_v203_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_252d_v203_signal},    "f48_valuation_reversion_ps_z_vol_slope_252d_v204_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_252d_v204_signal},    "f48_valuation_reversion_pe_vol_slope_504d_v205_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_504d_v205_signal},    "f48_valuation_reversion_ps_vol_slope_504d_v206_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_504d_v206_signal},    "f48_valuation_reversion_ev_vol_slope_504d_v207_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_504d_v207_signal},    "f48_valuation_reversion_ps_z_vol_slope_504d_v208_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_504d_v208_signal},    "f48_valuation_reversion_pe_vol_slope_756d_v209_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_756d_v209_signal},    "f48_valuation_reversion_ps_vol_slope_756d_v210_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_756d_v210_signal},    "f48_valuation_reversion_ev_vol_slope_756d_v211_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_756d_v211_signal},    "f48_valuation_reversion_ps_z_vol_slope_756d_v212_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_756d_v212_signal},    "f48_valuation_reversion_pe_vol_slope_1008d_v213_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_1008d_v213_signal},    "f48_valuation_reversion_ps_vol_slope_1008d_v214_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_1008d_v214_signal},    "f48_valuation_reversion_ev_vol_slope_1008d_v215_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_1008d_v215_signal},    "f48_valuation_reversion_ps_z_vol_slope_1008d_v216_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_1008d_v216_signal},    "f48_valuation_reversion_pe_vol_slope_1260d_v217_signal": {"inputs": [], "func": f48_valuation_reversion_pe_vol_slope_1260d_v217_signal},    "f48_valuation_reversion_ps_vol_slope_1260d_v218_signal": {"inputs": [], "func": f48_valuation_reversion_ps_vol_slope_1260d_v218_signal},    "f48_valuation_reversion_ev_vol_slope_1260d_v219_signal": {"inputs": [], "func": f48_valuation_reversion_ev_vol_slope_1260d_v219_signal},    "f48_valuation_reversion_ps_z_vol_slope_1260d_v220_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 48...")
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
