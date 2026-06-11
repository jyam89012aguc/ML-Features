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

def f49_capital_discipline_fcf_mom_z_63d_v151_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 63d window."""
    res = _z(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_63d_v152_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 63d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_mom_z_126d_v153_signal(capex):
    """Relative momentum strength for Raw level of capex over 126d window."""
    res = _z(_slope_pct(capex, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_mom_z_126d_v154_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_mom_z_126d_v155_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 126d window."""
    res = _z(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_126d_v156_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 126d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_mom_z_252d_v157_signal(capex):
    """Relative momentum strength for Raw level of capex over 252d window."""
    res = _z(_slope_pct(capex, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_mom_z_252d_v158_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_mom_z_252d_v159_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 252d window."""
    res = _z(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_252d_v160_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 252d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_mom_z_504d_v161_signal(capex):
    """Relative momentum strength for Raw level of capex over 504d window."""
    res = _z(_slope_pct(capex, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_mom_z_504d_v162_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_mom_z_504d_v163_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 504d window."""
    res = _z(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_504d_v164_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 504d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_mom_z_756d_v165_signal(capex):
    """Relative momentum strength for Raw level of capex over 756d window."""
    res = _z(_slope_pct(capex, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_mom_z_756d_v166_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_mom_z_756d_v167_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 756d window."""
    res = _z(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_756d_v168_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 756d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_mom_z_1008d_v169_signal(capex):
    """Relative momentum strength for Raw level of capex over 1008d window."""
    res = _z(_slope_pct(capex, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_mom_z_1008d_v170_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_mom_z_1008d_v171_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 1008d window."""
    res = _z(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_1008d_v172_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 1008d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_mom_z_1260d_v173_signal(capex):
    """Relative momentum strength for Raw level of capex over 1260d window."""
    res = _z(_slope_pct(capex, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_mom_z_1260d_v174_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_mom_z_1260d_v175_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 1260d window."""
    res = _z(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_mom_z_1260d_v176_signal(fcf, capex):
    """Relative momentum strength for Free cash flow generated per unit of capex over 1260d window."""
    res = _z(_slope_pct(_ratio(fcf, capex), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_5d_v177_signal(capex):
    """Volatility of the momentum for Raw level of capex over 5d window."""
    res = _std(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_5d_v178_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_5d_v179_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 5d window."""
    res = _std(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_5d_v180_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 5d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_10d_v181_signal(capex):
    """Volatility of the momentum for Raw level of capex over 10d window."""
    res = _std(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_10d_v182_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_10d_v183_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 10d window."""
    res = _std(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_10d_v184_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 10d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_21d_v185_signal(capex):
    """Volatility of the momentum for Raw level of capex over 21d window."""
    res = _std(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_21d_v186_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_21d_v187_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 21d window."""
    res = _std(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_21d_v188_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 21d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_42d_v189_signal(capex):
    """Volatility of the momentum for Raw level of capex over 42d window."""
    res = _std(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_42d_v190_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_42d_v191_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 42d window."""
    res = _std(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_42d_v192_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 42d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_63d_v193_signal(capex):
    """Volatility of the momentum for Raw level of capex over 63d window."""
    res = _std(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_63d_v194_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_63d_v195_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 63d window."""
    res = _std(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_63d_v196_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 63d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_126d_v197_signal(capex):
    """Volatility of the momentum for Raw level of capex over 126d window."""
    res = _std(_slope_pct(capex, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_126d_v198_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_126d_v199_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 126d window."""
    res = _std(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_126d_v200_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 126d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_252d_v201_signal(capex):
    """Volatility of the momentum for Raw level of capex over 252d window."""
    res = _std(_slope_pct(capex, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_252d_v202_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_252d_v203_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 252d window."""
    res = _std(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_252d_v204_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 252d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_504d_v205_signal(capex):
    """Volatility of the momentum for Raw level of capex over 504d window."""
    res = _std(_slope_pct(capex, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_504d_v206_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_504d_v207_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 504d window."""
    res = _std(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_504d_v208_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 504d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_756d_v209_signal(capex):
    """Volatility of the momentum for Raw level of capex over 756d window."""
    res = _std(_slope_pct(capex, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_756d_v210_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_756d_v211_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 756d window."""
    res = _std(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_756d_v212_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 756d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_1008d_v213_signal(capex):
    """Volatility of the momentum for Raw level of capex over 1008d window."""
    res = _std(_slope_pct(capex, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_1008d_v214_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_1008d_v215_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 1008d window."""
    res = _std(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_1008d_v216_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 1008d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_vol_slope_1260d_v217_signal(capex):
    """Volatility of the momentum for Raw level of capex over 1260d window."""
    res = _std(_slope_pct(capex, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_vol_slope_1260d_v218_signal(netinc):
    """Volatility of the momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_vol_slope_1260d_v219_signal(fcf):
    """Volatility of the momentum for Raw level of fcf over 1260d window."""
    res = _std(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_vol_slope_1260d_v220_signal(fcf, capex):
    """Volatility of the momentum for Free cash flow generated per unit of capex over 1260d window."""
    res = _std(_slope_pct(_ratio(fcf, capex), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f49_capital_discipline_fcf_mom_z_63d_v151_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_63d_v151_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_63d_v152_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_63d_v152_signal},    "f49_capital_discipline_capex_mom_z_126d_v153_signal": {"inputs": [], "func": f49_capital_discipline_capex_mom_z_126d_v153_signal},    "f49_capital_discipline_netinc_mom_z_126d_v154_signal": {"inputs": [], "func": f49_capital_discipline_netinc_mom_z_126d_v154_signal},    "f49_capital_discipline_fcf_mom_z_126d_v155_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_126d_v155_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_126d_v156_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_126d_v156_signal},    "f49_capital_discipline_capex_mom_z_252d_v157_signal": {"inputs": [], "func": f49_capital_discipline_capex_mom_z_252d_v157_signal},    "f49_capital_discipline_netinc_mom_z_252d_v158_signal": {"inputs": [], "func": f49_capital_discipline_netinc_mom_z_252d_v158_signal},    "f49_capital_discipline_fcf_mom_z_252d_v159_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_252d_v159_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_252d_v160_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_252d_v160_signal},    "f49_capital_discipline_capex_mom_z_504d_v161_signal": {"inputs": [], "func": f49_capital_discipline_capex_mom_z_504d_v161_signal},    "f49_capital_discipline_netinc_mom_z_504d_v162_signal": {"inputs": [], "func": f49_capital_discipline_netinc_mom_z_504d_v162_signal},    "f49_capital_discipline_fcf_mom_z_504d_v163_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_504d_v163_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_504d_v164_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_504d_v164_signal},    "f49_capital_discipline_capex_mom_z_756d_v165_signal": {"inputs": [], "func": f49_capital_discipline_capex_mom_z_756d_v165_signal},    "f49_capital_discipline_netinc_mom_z_756d_v166_signal": {"inputs": [], "func": f49_capital_discipline_netinc_mom_z_756d_v166_signal},    "f49_capital_discipline_fcf_mom_z_756d_v167_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_756d_v167_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_756d_v168_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_756d_v168_signal},    "f49_capital_discipline_capex_mom_z_1008d_v169_signal": {"inputs": [], "func": f49_capital_discipline_capex_mom_z_1008d_v169_signal},    "f49_capital_discipline_netinc_mom_z_1008d_v170_signal": {"inputs": [], "func": f49_capital_discipline_netinc_mom_z_1008d_v170_signal},    "f49_capital_discipline_fcf_mom_z_1008d_v171_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_1008d_v171_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_1008d_v172_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_1008d_v172_signal},    "f49_capital_discipline_capex_mom_z_1260d_v173_signal": {"inputs": [], "func": f49_capital_discipline_capex_mom_z_1260d_v173_signal},    "f49_capital_discipline_netinc_mom_z_1260d_v174_signal": {"inputs": [], "func": f49_capital_discipline_netinc_mom_z_1260d_v174_signal},    "f49_capital_discipline_fcf_mom_z_1260d_v175_signal": {"inputs": [], "func": f49_capital_discipline_fcf_mom_z_1260d_v175_signal},    "f49_capital_discipline_fcf_yield_on_capex_mom_z_1260d_v176_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_mom_z_1260d_v176_signal},    "f49_capital_discipline_capex_vol_slope_5d_v177_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_5d_v177_signal},    "f49_capital_discipline_netinc_vol_slope_5d_v178_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_5d_v178_signal},    "f49_capital_discipline_fcf_vol_slope_5d_v179_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_5d_v179_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_5d_v180_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_5d_v180_signal},    "f49_capital_discipline_capex_vol_slope_10d_v181_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_10d_v181_signal},    "f49_capital_discipline_netinc_vol_slope_10d_v182_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_10d_v182_signal},    "f49_capital_discipline_fcf_vol_slope_10d_v183_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_10d_v183_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_10d_v184_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_10d_v184_signal},    "f49_capital_discipline_capex_vol_slope_21d_v185_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_21d_v185_signal},    "f49_capital_discipline_netinc_vol_slope_21d_v186_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_21d_v186_signal},    "f49_capital_discipline_fcf_vol_slope_21d_v187_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_21d_v187_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_21d_v188_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_21d_v188_signal},    "f49_capital_discipline_capex_vol_slope_42d_v189_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_42d_v189_signal},    "f49_capital_discipline_netinc_vol_slope_42d_v190_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_42d_v190_signal},    "f49_capital_discipline_fcf_vol_slope_42d_v191_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_42d_v191_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_42d_v192_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_42d_v192_signal},    "f49_capital_discipline_capex_vol_slope_63d_v193_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_63d_v193_signal},    "f49_capital_discipline_netinc_vol_slope_63d_v194_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_63d_v194_signal},    "f49_capital_discipline_fcf_vol_slope_63d_v195_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_63d_v195_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_63d_v196_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_63d_v196_signal},    "f49_capital_discipline_capex_vol_slope_126d_v197_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_126d_v197_signal},    "f49_capital_discipline_netinc_vol_slope_126d_v198_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_126d_v198_signal},    "f49_capital_discipline_fcf_vol_slope_126d_v199_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_126d_v199_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_126d_v200_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_126d_v200_signal},    "f49_capital_discipline_capex_vol_slope_252d_v201_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_252d_v201_signal},    "f49_capital_discipline_netinc_vol_slope_252d_v202_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_252d_v202_signal},    "f49_capital_discipline_fcf_vol_slope_252d_v203_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_252d_v203_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_252d_v204_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_252d_v204_signal},    "f49_capital_discipline_capex_vol_slope_504d_v205_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_504d_v205_signal},    "f49_capital_discipline_netinc_vol_slope_504d_v206_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_504d_v206_signal},    "f49_capital_discipline_fcf_vol_slope_504d_v207_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_504d_v207_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_504d_v208_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_504d_v208_signal},    "f49_capital_discipline_capex_vol_slope_756d_v209_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_756d_v209_signal},    "f49_capital_discipline_netinc_vol_slope_756d_v210_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_756d_v210_signal},    "f49_capital_discipline_fcf_vol_slope_756d_v211_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_756d_v211_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_756d_v212_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_756d_v212_signal},    "f49_capital_discipline_capex_vol_slope_1008d_v213_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_1008d_v213_signal},    "f49_capital_discipline_netinc_vol_slope_1008d_v214_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_1008d_v214_signal},    "f49_capital_discipline_fcf_vol_slope_1008d_v215_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_1008d_v215_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_1008d_v216_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_1008d_v216_signal},    "f49_capital_discipline_capex_vol_slope_1260d_v217_signal": {"inputs": [], "func": f49_capital_discipline_capex_vol_slope_1260d_v217_signal},    "f49_capital_discipline_netinc_vol_slope_1260d_v218_signal": {"inputs": [], "func": f49_capital_discipline_netinc_vol_slope_1260d_v218_signal},    "f49_capital_discipline_fcf_vol_slope_1260d_v219_signal": {"inputs": [], "func": f49_capital_discipline_fcf_vol_slope_1260d_v219_signal},    "f49_capital_discipline_fcf_yield_on_capex_vol_slope_1260d_v220_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 49...")
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
