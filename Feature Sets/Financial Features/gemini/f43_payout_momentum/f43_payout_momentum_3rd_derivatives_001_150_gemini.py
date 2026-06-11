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

def f43_payout_momentum_divyield_mom_z_63d_v151_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 63d window."""
    res = _z(_slope_pct(divyield, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_63d_v152_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 63d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_mom_z_126d_v153_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 126d window."""
    res = _z(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_mom_z_126d_v154_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 126d window."""
    res = _z(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_mom_z_126d_v155_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 126d window."""
    res = _z(_slope_pct(divyield, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_126d_v156_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 126d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_mom_z_252d_v157_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 252d window."""
    res = _z(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_mom_z_252d_v158_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 252d window."""
    res = _z(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_mom_z_252d_v159_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 252d window."""
    res = _z(_slope_pct(divyield, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_252d_v160_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 252d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_mom_z_504d_v161_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 504d window."""
    res = _z(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_mom_z_504d_v162_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 504d window."""
    res = _z(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_mom_z_504d_v163_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 504d window."""
    res = _z(_slope_pct(divyield, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_504d_v164_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 504d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_mom_z_756d_v165_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 756d window."""
    res = _z(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_mom_z_756d_v166_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 756d window."""
    res = _z(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_mom_z_756d_v167_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 756d window."""
    res = _z(_slope_pct(divyield, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_756d_v168_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 756d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_mom_z_1008d_v169_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 1008d window."""
    res = _z(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_mom_z_1008d_v170_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 1008d window."""
    res = _z(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_mom_z_1008d_v171_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 1008d window."""
    res = _z(_slope_pct(divyield, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_1008d_v172_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 1008d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_mom_z_1260d_v173_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 1260d window."""
    res = _z(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_mom_z_1260d_v174_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 1260d window."""
    res = _z(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_mom_z_1260d_v175_signal(divyield):
    """Relative momentum strength for Raw level of divyield over 1260d window."""
    res = _z(_slope_pct(divyield, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_mom_z_1260d_v176_signal(fcf, marketcap):
    """Relative momentum strength for Free cash flow yield over 1260d window."""
    res = _z(_slope_pct(_ratio(fcf, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_5d_v177_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 5d window."""
    res = _std(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_5d_v178_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 5d window."""
    res = _std(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_5d_v179_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 5d window."""
    res = _std(_slope_pct(divyield, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_5d_v180_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 5d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_10d_v181_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 10d window."""
    res = _std(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_10d_v182_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 10d window."""
    res = _std(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_10d_v183_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 10d window."""
    res = _std(_slope_pct(divyield, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_10d_v184_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 10d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_21d_v185_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 21d window."""
    res = _std(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_21d_v186_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 21d window."""
    res = _std(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_21d_v187_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 21d window."""
    res = _std(_slope_pct(divyield, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_21d_v188_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 21d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_42d_v189_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 42d window."""
    res = _std(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_42d_v190_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 42d window."""
    res = _std(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_42d_v191_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 42d window."""
    res = _std(_slope_pct(divyield, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_42d_v192_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 42d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_63d_v193_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 63d window."""
    res = _std(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_63d_v194_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 63d window."""
    res = _std(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_63d_v195_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 63d window."""
    res = _std(_slope_pct(divyield, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_63d_v196_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 63d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_126d_v197_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 126d window."""
    res = _std(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_126d_v198_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 126d window."""
    res = _std(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_126d_v199_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 126d window."""
    res = _std(_slope_pct(divyield, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_126d_v200_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 126d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_252d_v201_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 252d window."""
    res = _std(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_252d_v202_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 252d window."""
    res = _std(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_252d_v203_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 252d window."""
    res = _std(_slope_pct(divyield, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_252d_v204_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 252d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_504d_v205_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 504d window."""
    res = _std(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_504d_v206_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 504d window."""
    res = _std(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_504d_v207_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 504d window."""
    res = _std(_slope_pct(divyield, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_504d_v208_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 504d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_756d_v209_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 756d window."""
    res = _std(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_756d_v210_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 756d window."""
    res = _std(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_756d_v211_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 756d window."""
    res = _std(_slope_pct(divyield, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_756d_v212_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 756d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_1008d_v213_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 1008d window."""
    res = _std(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_1008d_v214_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 1008d window."""
    res = _std(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_1008d_v215_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 1008d window."""
    res = _std(_slope_pct(divyield, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_1008d_v216_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 1008d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_vol_slope_1260d_v217_signal(fcf):
    """Volatility of momentum for Raw level of fcf over 1260d window."""
    res = _std(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_vol_slope_1260d_v218_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 1260d window."""
    res = _std(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_vol_slope_1260d_v219_signal(divyield):
    """Volatility of momentum for Raw level of divyield over 1260d window."""
    res = _std(_slope_pct(divyield, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_vol_slope_1260d_v220_signal(fcf, marketcap):
    """Volatility of momentum for Free cash flow yield over 1260d window."""
    res = _std(_slope_pct(_ratio(fcf, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_5d_v221_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 5d window."""
    res = _ewma(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_5d_v222_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 5d window."""
    res = _ewma(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_5d_v223_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 5d window."""
    res = _ewma(_slope_pct(divyield, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_5d_v224_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 5d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_10d_v225_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 10d window."""
    res = _ewma(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_10d_v226_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 10d window."""
    res = _ewma(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_10d_v227_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 10d window."""
    res = _ewma(_slope_pct(divyield, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_10d_v228_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 10d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_21d_v229_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 21d window."""
    res = _ewma(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_21d_v230_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 21d window."""
    res = _ewma(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_21d_v231_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 21d window."""
    res = _ewma(_slope_pct(divyield, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_21d_v232_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 21d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_42d_v233_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 42d window."""
    res = _ewma(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_42d_v234_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 42d window."""
    res = _ewma(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_42d_v235_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 42d window."""
    res = _ewma(_slope_pct(divyield, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_42d_v236_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 42d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_63d_v237_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 63d window."""
    res = _ewma(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_63d_v238_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 63d window."""
    res = _ewma(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_63d_v239_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 63d window."""
    res = _ewma(_slope_pct(divyield, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_63d_v240_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 63d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_126d_v241_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 126d window."""
    res = _ewma(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_126d_v242_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 126d window."""
    res = _ewma(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_126d_v243_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 126d window."""
    res = _ewma(_slope_pct(divyield, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_126d_v244_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 126d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_252d_v245_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 252d window."""
    res = _ewma(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_252d_v246_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 252d window."""
    res = _ewma(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_252d_v247_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 252d window."""
    res = _ewma(_slope_pct(divyield, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_252d_v248_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 252d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_504d_v249_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 504d window."""
    res = _ewma(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_504d_v250_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 504d window."""
    res = _ewma(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_504d_v251_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 504d window."""
    res = _ewma(_slope_pct(divyield, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_504d_v252_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 504d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_756d_v253_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 756d window."""
    res = _ewma(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_756d_v254_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 756d window."""
    res = _ewma(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_756d_v255_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 756d window."""
    res = _ewma(_slope_pct(divyield, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_756d_v256_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 756d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_1008d_v257_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 1008d window."""
    res = _ewma(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_1008d_v258_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 1008d window."""
    res = _ewma(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_1008d_v259_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 1008d window."""
    res = _ewma(_slope_pct(divyield, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_1008d_v260_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 1008d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_ewma_slope_1260d_v261_signal(fcf):
    """Exponential momentum smoothing for Raw level of fcf over 1260d window."""
    res = _ewma(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_shareswa_ewma_slope_1260d_v262_signal(shareswa):
    """Exponential momentum smoothing for Raw level of shareswa over 1260d window."""
    res = _ewma(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_divyield_ewma_slope_1260d_v263_signal(divyield):
    """Exponential momentum smoothing for Raw level of divyield over 1260d window."""
    res = _ewma(_slope_pct(divyield, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_momentum_fcf_yield_proxy_ewma_slope_1260d_v264_signal(fcf, marketcap):
    """Exponential momentum smoothing for Free cash flow yield over 1260d window."""
    res = _ewma(_slope_pct(_ratio(fcf, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f43_payout_momentum_divyield_mom_z_63d_v151_signal": {"func": f43_payout_momentum_divyield_mom_z_63d_v151_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_63d_v152_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_63d_v152_signal},
    "f43_payout_momentum_fcf_mom_z_126d_v153_signal": {"func": f43_payout_momentum_fcf_mom_z_126d_v153_signal},
    "f43_payout_momentum_shareswa_mom_z_126d_v154_signal": {"func": f43_payout_momentum_shareswa_mom_z_126d_v154_signal},
    "f43_payout_momentum_divyield_mom_z_126d_v155_signal": {"func": f43_payout_momentum_divyield_mom_z_126d_v155_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_126d_v156_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_126d_v156_signal},
    "f43_payout_momentum_fcf_mom_z_252d_v157_signal": {"func": f43_payout_momentum_fcf_mom_z_252d_v157_signal},
    "f43_payout_momentum_shareswa_mom_z_252d_v158_signal": {"func": f43_payout_momentum_shareswa_mom_z_252d_v158_signal},
    "f43_payout_momentum_divyield_mom_z_252d_v159_signal": {"func": f43_payout_momentum_divyield_mom_z_252d_v159_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_252d_v160_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_252d_v160_signal},
    "f43_payout_momentum_fcf_mom_z_504d_v161_signal": {"func": f43_payout_momentum_fcf_mom_z_504d_v161_signal},
    "f43_payout_momentum_shareswa_mom_z_504d_v162_signal": {"func": f43_payout_momentum_shareswa_mom_z_504d_v162_signal},
    "f43_payout_momentum_divyield_mom_z_504d_v163_signal": {"func": f43_payout_momentum_divyield_mom_z_504d_v163_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_504d_v164_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_504d_v164_signal},
    "f43_payout_momentum_fcf_mom_z_756d_v165_signal": {"func": f43_payout_momentum_fcf_mom_z_756d_v165_signal},
    "f43_payout_momentum_shareswa_mom_z_756d_v166_signal": {"func": f43_payout_momentum_shareswa_mom_z_756d_v166_signal},
    "f43_payout_momentum_divyield_mom_z_756d_v167_signal": {"func": f43_payout_momentum_divyield_mom_z_756d_v167_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_756d_v168_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_756d_v168_signal},
    "f43_payout_momentum_fcf_mom_z_1008d_v169_signal": {"func": f43_payout_momentum_fcf_mom_z_1008d_v169_signal},
    "f43_payout_momentum_shareswa_mom_z_1008d_v170_signal": {"func": f43_payout_momentum_shareswa_mom_z_1008d_v170_signal},
    "f43_payout_momentum_divyield_mom_z_1008d_v171_signal": {"func": f43_payout_momentum_divyield_mom_z_1008d_v171_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_1008d_v172_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_1008d_v172_signal},
    "f43_payout_momentum_fcf_mom_z_1260d_v173_signal": {"func": f43_payout_momentum_fcf_mom_z_1260d_v173_signal},
    "f43_payout_momentum_shareswa_mom_z_1260d_v174_signal": {"func": f43_payout_momentum_shareswa_mom_z_1260d_v174_signal},
    "f43_payout_momentum_divyield_mom_z_1260d_v175_signal": {"func": f43_payout_momentum_divyield_mom_z_1260d_v175_signal},
    "f43_payout_momentum_fcf_yield_proxy_mom_z_1260d_v176_signal": {"func": f43_payout_momentum_fcf_yield_proxy_mom_z_1260d_v176_signal},
    "f43_payout_momentum_fcf_vol_slope_5d_v177_signal": {"func": f43_payout_momentum_fcf_vol_slope_5d_v177_signal},
    "f43_payout_momentum_shareswa_vol_slope_5d_v178_signal": {"func": f43_payout_momentum_shareswa_vol_slope_5d_v178_signal},
    "f43_payout_momentum_divyield_vol_slope_5d_v179_signal": {"func": f43_payout_momentum_divyield_vol_slope_5d_v179_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_5d_v180_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_5d_v180_signal},
    "f43_payout_momentum_fcf_vol_slope_10d_v181_signal": {"func": f43_payout_momentum_fcf_vol_slope_10d_v181_signal},
    "f43_payout_momentum_shareswa_vol_slope_10d_v182_signal": {"func": f43_payout_momentum_shareswa_vol_slope_10d_v182_signal},
    "f43_payout_momentum_divyield_vol_slope_10d_v183_signal": {"func": f43_payout_momentum_divyield_vol_slope_10d_v183_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_10d_v184_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_10d_v184_signal},
    "f43_payout_momentum_fcf_vol_slope_21d_v185_signal": {"func": f43_payout_momentum_fcf_vol_slope_21d_v185_signal},
    "f43_payout_momentum_shareswa_vol_slope_21d_v186_signal": {"func": f43_payout_momentum_shareswa_vol_slope_21d_v186_signal},
    "f43_payout_momentum_divyield_vol_slope_21d_v187_signal": {"func": f43_payout_momentum_divyield_vol_slope_21d_v187_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_21d_v188_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_21d_v188_signal},
    "f43_payout_momentum_fcf_vol_slope_42d_v189_signal": {"func": f43_payout_momentum_fcf_vol_slope_42d_v189_signal},
    "f43_payout_momentum_shareswa_vol_slope_42d_v190_signal": {"func": f43_payout_momentum_shareswa_vol_slope_42d_v190_signal},
    "f43_payout_momentum_divyield_vol_slope_42d_v191_signal": {"func": f43_payout_momentum_divyield_vol_slope_42d_v191_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_42d_v192_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_42d_v192_signal},
    "f43_payout_momentum_fcf_vol_slope_63d_v193_signal": {"func": f43_payout_momentum_fcf_vol_slope_63d_v193_signal},
    "f43_payout_momentum_shareswa_vol_slope_63d_v194_signal": {"func": f43_payout_momentum_shareswa_vol_slope_63d_v194_signal},
    "f43_payout_momentum_divyield_vol_slope_63d_v195_signal": {"func": f43_payout_momentum_divyield_vol_slope_63d_v195_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_63d_v196_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_63d_v196_signal},
    "f43_payout_momentum_fcf_vol_slope_126d_v197_signal": {"func": f43_payout_momentum_fcf_vol_slope_126d_v197_signal},
    "f43_payout_momentum_shareswa_vol_slope_126d_v198_signal": {"func": f43_payout_momentum_shareswa_vol_slope_126d_v198_signal},
    "f43_payout_momentum_divyield_vol_slope_126d_v199_signal": {"func": f43_payout_momentum_divyield_vol_slope_126d_v199_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_126d_v200_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_126d_v200_signal},
    "f43_payout_momentum_fcf_vol_slope_252d_v201_signal": {"func": f43_payout_momentum_fcf_vol_slope_252d_v201_signal},
    "f43_payout_momentum_shareswa_vol_slope_252d_v202_signal": {"func": f43_payout_momentum_shareswa_vol_slope_252d_v202_signal},
    "f43_payout_momentum_divyield_vol_slope_252d_v203_signal": {"func": f43_payout_momentum_divyield_vol_slope_252d_v203_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_252d_v204_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_252d_v204_signal},
    "f43_payout_momentum_fcf_vol_slope_504d_v205_signal": {"func": f43_payout_momentum_fcf_vol_slope_504d_v205_signal},
    "f43_payout_momentum_shareswa_vol_slope_504d_v206_signal": {"func": f43_payout_momentum_shareswa_vol_slope_504d_v206_signal},
    "f43_payout_momentum_divyield_vol_slope_504d_v207_signal": {"func": f43_payout_momentum_divyield_vol_slope_504d_v207_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_504d_v208_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_504d_v208_signal},
    "f43_payout_momentum_fcf_vol_slope_756d_v209_signal": {"func": f43_payout_momentum_fcf_vol_slope_756d_v209_signal},
    "f43_payout_momentum_shareswa_vol_slope_756d_v210_signal": {"func": f43_payout_momentum_shareswa_vol_slope_756d_v210_signal},
    "f43_payout_momentum_divyield_vol_slope_756d_v211_signal": {"func": f43_payout_momentum_divyield_vol_slope_756d_v211_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_756d_v212_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_756d_v212_signal},
    "f43_payout_momentum_fcf_vol_slope_1008d_v213_signal": {"func": f43_payout_momentum_fcf_vol_slope_1008d_v213_signal},
    "f43_payout_momentum_shareswa_vol_slope_1008d_v214_signal": {"func": f43_payout_momentum_shareswa_vol_slope_1008d_v214_signal},
    "f43_payout_momentum_divyield_vol_slope_1008d_v215_signal": {"func": f43_payout_momentum_divyield_vol_slope_1008d_v215_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_1008d_v216_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_1008d_v216_signal},
    "f43_payout_momentum_fcf_vol_slope_1260d_v217_signal": {"func": f43_payout_momentum_fcf_vol_slope_1260d_v217_signal},
    "f43_payout_momentum_shareswa_vol_slope_1260d_v218_signal": {"func": f43_payout_momentum_shareswa_vol_slope_1260d_v218_signal},
    "f43_payout_momentum_divyield_vol_slope_1260d_v219_signal": {"func": f43_payout_momentum_divyield_vol_slope_1260d_v219_signal},
    "f43_payout_momentum_fcf_yield_proxy_vol_slope_1260d_v220_signal": {"func": f43_payout_momentum_fcf_yield_proxy_vol_slope_1260d_v220_signal},
    "f43_payout_momentum_fcf_ewma_slope_5d_v221_signal": {"func": f43_payout_momentum_fcf_ewma_slope_5d_v221_signal},
    "f43_payout_momentum_shareswa_ewma_slope_5d_v222_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_5d_v222_signal},
    "f43_payout_momentum_divyield_ewma_slope_5d_v223_signal": {"func": f43_payout_momentum_divyield_ewma_slope_5d_v223_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_5d_v224_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_5d_v224_signal},
    "f43_payout_momentum_fcf_ewma_slope_10d_v225_signal": {"func": f43_payout_momentum_fcf_ewma_slope_10d_v225_signal},
    "f43_payout_momentum_shareswa_ewma_slope_10d_v226_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_10d_v226_signal},
    "f43_payout_momentum_divyield_ewma_slope_10d_v227_signal": {"func": f43_payout_momentum_divyield_ewma_slope_10d_v227_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_10d_v228_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_10d_v228_signal},
    "f43_payout_momentum_fcf_ewma_slope_21d_v229_signal": {"func": f43_payout_momentum_fcf_ewma_slope_21d_v229_signal},
    "f43_payout_momentum_shareswa_ewma_slope_21d_v230_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_21d_v230_signal},
    "f43_payout_momentum_divyield_ewma_slope_21d_v231_signal": {"func": f43_payout_momentum_divyield_ewma_slope_21d_v231_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_21d_v232_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_21d_v232_signal},
    "f43_payout_momentum_fcf_ewma_slope_42d_v233_signal": {"func": f43_payout_momentum_fcf_ewma_slope_42d_v233_signal},
    "f43_payout_momentum_shareswa_ewma_slope_42d_v234_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_42d_v234_signal},
    "f43_payout_momentum_divyield_ewma_slope_42d_v235_signal": {"func": f43_payout_momentum_divyield_ewma_slope_42d_v235_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_42d_v236_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_42d_v236_signal},
    "f43_payout_momentum_fcf_ewma_slope_63d_v237_signal": {"func": f43_payout_momentum_fcf_ewma_slope_63d_v237_signal},
    "f43_payout_momentum_shareswa_ewma_slope_63d_v238_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_63d_v238_signal},
    "f43_payout_momentum_divyield_ewma_slope_63d_v239_signal": {"func": f43_payout_momentum_divyield_ewma_slope_63d_v239_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_63d_v240_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_63d_v240_signal},
    "f43_payout_momentum_fcf_ewma_slope_126d_v241_signal": {"func": f43_payout_momentum_fcf_ewma_slope_126d_v241_signal},
    "f43_payout_momentum_shareswa_ewma_slope_126d_v242_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_126d_v242_signal},
    "f43_payout_momentum_divyield_ewma_slope_126d_v243_signal": {"func": f43_payout_momentum_divyield_ewma_slope_126d_v243_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_126d_v244_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_126d_v244_signal},
    "f43_payout_momentum_fcf_ewma_slope_252d_v245_signal": {"func": f43_payout_momentum_fcf_ewma_slope_252d_v245_signal},
    "f43_payout_momentum_shareswa_ewma_slope_252d_v246_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_252d_v246_signal},
    "f43_payout_momentum_divyield_ewma_slope_252d_v247_signal": {"func": f43_payout_momentum_divyield_ewma_slope_252d_v247_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_252d_v248_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_252d_v248_signal},
    "f43_payout_momentum_fcf_ewma_slope_504d_v249_signal": {"func": f43_payout_momentum_fcf_ewma_slope_504d_v249_signal},
    "f43_payout_momentum_shareswa_ewma_slope_504d_v250_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_504d_v250_signal},
    "f43_payout_momentum_divyield_ewma_slope_504d_v251_signal": {"func": f43_payout_momentum_divyield_ewma_slope_504d_v251_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_504d_v252_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_504d_v252_signal},
    "f43_payout_momentum_fcf_ewma_slope_756d_v253_signal": {"func": f43_payout_momentum_fcf_ewma_slope_756d_v253_signal},
    "f43_payout_momentum_shareswa_ewma_slope_756d_v254_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_756d_v254_signal},
    "f43_payout_momentum_divyield_ewma_slope_756d_v255_signal": {"func": f43_payout_momentum_divyield_ewma_slope_756d_v255_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_756d_v256_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_756d_v256_signal},
    "f43_payout_momentum_fcf_ewma_slope_1008d_v257_signal": {"func": f43_payout_momentum_fcf_ewma_slope_1008d_v257_signal},
    "f43_payout_momentum_shareswa_ewma_slope_1008d_v258_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_1008d_v258_signal},
    "f43_payout_momentum_divyield_ewma_slope_1008d_v259_signal": {"func": f43_payout_momentum_divyield_ewma_slope_1008d_v259_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_1008d_v260_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_1008d_v260_signal},
    "f43_payout_momentum_fcf_ewma_slope_1260d_v261_signal": {"func": f43_payout_momentum_fcf_ewma_slope_1260d_v261_signal},
    "f43_payout_momentum_shareswa_ewma_slope_1260d_v262_signal": {"func": f43_payout_momentum_shareswa_ewma_slope_1260d_v262_signal},
    "f43_payout_momentum_divyield_ewma_slope_1260d_v263_signal": {"func": f43_payout_momentum_divyield_ewma_slope_1260d_v263_signal},
    "f43_payout_momentum_fcf_yield_proxy_ewma_slope_1260d_v264_signal": {"func": f43_payout_momentum_fcf_yield_proxy_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 43...")
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
