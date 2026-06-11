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

def f47_roic_compounder_fin_netinc_mom_z_63d_v151_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_63d_v152_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 63d window."""
    res = _z(_slope_pct(_std(roic, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_126d_v153_signal(roic):
    """Relative momentum strength for Raw level of roic over 126d window."""
    res = _z(_slope_pct(roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_126d_v154_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 126d window."""
    res = _z(_slope_pct(invcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_126d_v155_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_126d_v156_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 126d window."""
    res = _z(_slope_pct(_std(roic, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_252d_v157_signal(roic):
    """Relative momentum strength for Raw level of roic over 252d window."""
    res = _z(_slope_pct(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_252d_v158_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 252d window."""
    res = _z(_slope_pct(invcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_252d_v159_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_252d_v160_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 252d window."""
    res = _z(_slope_pct(_std(roic, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_504d_v161_signal(roic):
    """Relative momentum strength for Raw level of roic over 504d window."""
    res = _z(_slope_pct(roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_504d_v162_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 504d window."""
    res = _z(_slope_pct(invcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_504d_v163_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_504d_v164_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 504d window."""
    res = _z(_slope_pct(_std(roic, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_756d_v165_signal(roic):
    """Relative momentum strength for Raw level of roic over 756d window."""
    res = _z(_slope_pct(roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_756d_v166_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 756d window."""
    res = _z(_slope_pct(invcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_756d_v167_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_756d_v168_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 756d window."""
    res = _z(_slope_pct(_std(roic, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_1008d_v169_signal(roic):
    """Relative momentum strength for Raw level of roic over 1008d window."""
    res = _z(_slope_pct(roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_1008d_v170_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 1008d window."""
    res = _z(_slope_pct(invcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_1008d_v171_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_1008d_v172_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 1008d window."""
    res = _z(_slope_pct(_std(roic, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_mom_z_1260d_v173_signal(roic):
    """Relative momentum strength for Raw level of roic over 1260d window."""
    res = _z(_slope_pct(roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_mom_z_1260d_v174_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 1260d window."""
    res = _z(_slope_pct(invcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_mom_z_1260d_v175_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_mom_z_1260d_v176_signal(roic):
    """Relative momentum strength for ROIC stability (standard deviation) over 1260d window."""
    res = _z(_slope_pct(_std(roic, 252), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_5d_v177_signal(roic):
    """Volatility of momentum for Raw level of roic over 5d window."""
    res = _std(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_5d_v178_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 5d window."""
    res = _std(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_5d_v179_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_5d_v180_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 5d window."""
    res = _std(_slope_pct(_std(roic, 252), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_10d_v181_signal(roic):
    """Volatility of momentum for Raw level of roic over 10d window."""
    res = _std(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_10d_v182_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 10d window."""
    res = _std(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_10d_v183_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_10d_v184_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 10d window."""
    res = _std(_slope_pct(_std(roic, 252), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_21d_v185_signal(roic):
    """Volatility of momentum for Raw level of roic over 21d window."""
    res = _std(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_21d_v186_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 21d window."""
    res = _std(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_21d_v187_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_21d_v188_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 21d window."""
    res = _std(_slope_pct(_std(roic, 252), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_42d_v189_signal(roic):
    """Volatility of momentum for Raw level of roic over 42d window."""
    res = _std(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_42d_v190_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 42d window."""
    res = _std(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_42d_v191_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_42d_v192_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 42d window."""
    res = _std(_slope_pct(_std(roic, 252), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_63d_v193_signal(roic):
    """Volatility of momentum for Raw level of roic over 63d window."""
    res = _std(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_63d_v194_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 63d window."""
    res = _std(_slope_pct(invcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_63d_v195_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_63d_v196_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 63d window."""
    res = _std(_slope_pct(_std(roic, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_126d_v197_signal(roic):
    """Volatility of momentum for Raw level of roic over 126d window."""
    res = _std(_slope_pct(roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_126d_v198_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 126d window."""
    res = _std(_slope_pct(invcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_126d_v199_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_126d_v200_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 126d window."""
    res = _std(_slope_pct(_std(roic, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_252d_v201_signal(roic):
    """Volatility of momentum for Raw level of roic over 252d window."""
    res = _std(_slope_pct(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_252d_v202_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 252d window."""
    res = _std(_slope_pct(invcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_252d_v203_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_252d_v204_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 252d window."""
    res = _std(_slope_pct(_std(roic, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_504d_v205_signal(roic):
    """Volatility of momentum for Raw level of roic over 504d window."""
    res = _std(_slope_pct(roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_504d_v206_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 504d window."""
    res = _std(_slope_pct(invcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_504d_v207_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_504d_v208_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 504d window."""
    res = _std(_slope_pct(_std(roic, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_756d_v209_signal(roic):
    """Volatility of momentum for Raw level of roic over 756d window."""
    res = _std(_slope_pct(roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_756d_v210_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 756d window."""
    res = _std(_slope_pct(invcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_756d_v211_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_756d_v212_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 756d window."""
    res = _std(_slope_pct(_std(roic, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_1008d_v213_signal(roic):
    """Volatility of momentum for Raw level of roic over 1008d window."""
    res = _std(_slope_pct(roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_1008d_v214_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 1008d window."""
    res = _std(_slope_pct(invcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_1008d_v215_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_1008d_v216_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 1008d window."""
    res = _std(_slope_pct(_std(roic, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_slope_1260d_v217_signal(roic):
    """Volatility of momentum for Raw level of roic over 1260d window."""
    res = _std(_slope_pct(roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_vol_slope_1260d_v218_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 1260d window."""
    res = _std(_slope_pct(invcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_vol_slope_1260d_v219_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_vol_slope_1260d_v220_signal(roic):
    """Volatility of momentum for ROIC stability (standard deviation) over 1260d window."""
    res = _std(_slope_pct(_std(roic, 252), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_5d_v221_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 5d window."""
    res = _ewma(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_5d_v222_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 5d window."""
    res = _ewma(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_5d_v223_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _ewma(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_5d_v224_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 5d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_10d_v225_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 10d window."""
    res = _ewma(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_10d_v226_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 10d window."""
    res = _ewma(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_10d_v227_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _ewma(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_10d_v228_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 10d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_21d_v229_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 21d window."""
    res = _ewma(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_21d_v230_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 21d window."""
    res = _ewma(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_21d_v231_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _ewma(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_21d_v232_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 21d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_42d_v233_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 42d window."""
    res = _ewma(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_42d_v234_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 42d window."""
    res = _ewma(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_42d_v235_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _ewma(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_42d_v236_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 42d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_63d_v237_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 63d window."""
    res = _ewma(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_63d_v238_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 63d window."""
    res = _ewma(_slope_pct(invcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_63d_v239_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _ewma(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_63d_v240_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 63d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_126d_v241_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 126d window."""
    res = _ewma(_slope_pct(roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_126d_v242_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 126d window."""
    res = _ewma(_slope_pct(invcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_126d_v243_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 126d window."""
    res = _ewma(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_126d_v244_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 126d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_252d_v245_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 252d window."""
    res = _ewma(_slope_pct(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_252d_v246_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 252d window."""
    res = _ewma(_slope_pct(invcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_252d_v247_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 252d window."""
    res = _ewma(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_252d_v248_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 252d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_504d_v249_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 504d window."""
    res = _ewma(_slope_pct(roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_504d_v250_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 504d window."""
    res = _ewma(_slope_pct(invcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_504d_v251_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 504d window."""
    res = _ewma(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_504d_v252_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 504d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_756d_v253_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 756d window."""
    res = _ewma(_slope_pct(roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_756d_v254_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 756d window."""
    res = _ewma(_slope_pct(invcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_756d_v255_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 756d window."""
    res = _ewma(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_756d_v256_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 756d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_1008d_v257_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 1008d window."""
    res = _ewma(_slope_pct(roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_1008d_v258_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 1008d window."""
    res = _ewma(_slope_pct(invcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_1008d_v259_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1008d window."""
    res = _ewma(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_1008d_v260_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 1008d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_slope_1260d_v261_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 1260d window."""
    res = _ewma(_slope_pct(roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_slope_1260d_v262_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 1260d window."""
    res = _ewma(_slope_pct(invcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_slope_1260d_v263_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1260d window."""
    res = _ewma(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_slope_1260d_v264_signal(roic):
    """Exponential momentum smoothing for ROIC stability (standard deviation) over 1260d window."""
    res = _ewma(_slope_pct(_std(roic, 252), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f47_roic_compounder_fin_netinc_mom_z_63d_v151_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_63d_v151_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_63d_v152_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_63d_v152_signal},
    "f47_roic_compounder_fin_roic_mom_z_126d_v153_signal": {"func": f47_roic_compounder_fin_roic_mom_z_126d_v153_signal},
    "f47_roic_compounder_fin_invcap_mom_z_126d_v154_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_126d_v154_signal},
    "f47_roic_compounder_fin_netinc_mom_z_126d_v155_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_126d_v155_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_126d_v156_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_126d_v156_signal},
    "f47_roic_compounder_fin_roic_mom_z_252d_v157_signal": {"func": f47_roic_compounder_fin_roic_mom_z_252d_v157_signal},
    "f47_roic_compounder_fin_invcap_mom_z_252d_v158_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_252d_v158_signal},
    "f47_roic_compounder_fin_netinc_mom_z_252d_v159_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_252d_v159_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_252d_v160_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_252d_v160_signal},
    "f47_roic_compounder_fin_roic_mom_z_504d_v161_signal": {"func": f47_roic_compounder_fin_roic_mom_z_504d_v161_signal},
    "f47_roic_compounder_fin_invcap_mom_z_504d_v162_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_504d_v162_signal},
    "f47_roic_compounder_fin_netinc_mom_z_504d_v163_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_504d_v163_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_504d_v164_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_504d_v164_signal},
    "f47_roic_compounder_fin_roic_mom_z_756d_v165_signal": {"func": f47_roic_compounder_fin_roic_mom_z_756d_v165_signal},
    "f47_roic_compounder_fin_invcap_mom_z_756d_v166_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_756d_v166_signal},
    "f47_roic_compounder_fin_netinc_mom_z_756d_v167_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_756d_v167_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_756d_v168_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_756d_v168_signal},
    "f47_roic_compounder_fin_roic_mom_z_1008d_v169_signal": {"func": f47_roic_compounder_fin_roic_mom_z_1008d_v169_signal},
    "f47_roic_compounder_fin_invcap_mom_z_1008d_v170_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_1008d_v170_signal},
    "f47_roic_compounder_fin_netinc_mom_z_1008d_v171_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_1008d_v171_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_1008d_v172_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_1008d_v172_signal},
    "f47_roic_compounder_fin_roic_mom_z_1260d_v173_signal": {"func": f47_roic_compounder_fin_roic_mom_z_1260d_v173_signal},
    "f47_roic_compounder_fin_invcap_mom_z_1260d_v174_signal": {"func": f47_roic_compounder_fin_invcap_mom_z_1260d_v174_signal},
    "f47_roic_compounder_fin_netinc_mom_z_1260d_v175_signal": {"func": f47_roic_compounder_fin_netinc_mom_z_1260d_v175_signal},
    "f47_roic_compounder_fin_roic_vol_mom_z_1260d_v176_signal": {"func": f47_roic_compounder_fin_roic_vol_mom_z_1260d_v176_signal},
    "f47_roic_compounder_fin_roic_vol_slope_5d_v177_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_5d_v177_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_5d_v178_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_5d_v178_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_5d_v179_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_5d_v179_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_5d_v180_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_5d_v180_signal},
    "f47_roic_compounder_fin_roic_vol_slope_10d_v181_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_10d_v181_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_10d_v182_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_10d_v182_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_10d_v183_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_10d_v183_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_10d_v184_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_10d_v184_signal},
    "f47_roic_compounder_fin_roic_vol_slope_21d_v185_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_21d_v185_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_21d_v186_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_21d_v186_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_21d_v187_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_21d_v187_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_21d_v188_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_21d_v188_signal},
    "f47_roic_compounder_fin_roic_vol_slope_42d_v189_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_42d_v189_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_42d_v190_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_42d_v190_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_42d_v191_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_42d_v191_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_42d_v192_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_42d_v192_signal},
    "f47_roic_compounder_fin_roic_vol_slope_63d_v193_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_63d_v193_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_63d_v194_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_63d_v194_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_63d_v195_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_63d_v195_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_63d_v196_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_63d_v196_signal},
    "f47_roic_compounder_fin_roic_vol_slope_126d_v197_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_126d_v197_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_126d_v198_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_126d_v198_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_126d_v199_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_126d_v199_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_126d_v200_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_126d_v200_signal},
    "f47_roic_compounder_fin_roic_vol_slope_252d_v201_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_252d_v201_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_252d_v202_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_252d_v202_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_252d_v203_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_252d_v203_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_252d_v204_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_252d_v204_signal},
    "f47_roic_compounder_fin_roic_vol_slope_504d_v205_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_504d_v205_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_504d_v206_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_504d_v206_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_504d_v207_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_504d_v207_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_504d_v208_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_504d_v208_signal},
    "f47_roic_compounder_fin_roic_vol_slope_756d_v209_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_756d_v209_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_756d_v210_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_756d_v210_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_756d_v211_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_756d_v211_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_756d_v212_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_756d_v212_signal},
    "f47_roic_compounder_fin_roic_vol_slope_1008d_v213_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_1008d_v213_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_1008d_v214_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_1008d_v214_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_1008d_v215_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_1008d_v215_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_1008d_v216_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_1008d_v216_signal},
    "f47_roic_compounder_fin_roic_vol_slope_1260d_v217_signal": {"func": f47_roic_compounder_fin_roic_vol_slope_1260d_v217_signal},
    "f47_roic_compounder_fin_invcap_vol_slope_1260d_v218_signal": {"func": f47_roic_compounder_fin_invcap_vol_slope_1260d_v218_signal},
    "f47_roic_compounder_fin_netinc_vol_slope_1260d_v219_signal": {"func": f47_roic_compounder_fin_netinc_vol_slope_1260d_v219_signal},
    "f47_roic_compounder_fin_roic_vol_vol_slope_1260d_v220_signal": {"func": f47_roic_compounder_fin_roic_vol_vol_slope_1260d_v220_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_5d_v221_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_5d_v221_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_5d_v222_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_5d_v222_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_5d_v223_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_5d_v223_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_5d_v224_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_5d_v224_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_10d_v225_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_10d_v225_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_10d_v226_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_10d_v226_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_10d_v227_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_10d_v227_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_10d_v228_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_10d_v228_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_21d_v229_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_21d_v229_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_21d_v230_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_21d_v230_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_21d_v231_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_21d_v231_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_21d_v232_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_21d_v232_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_42d_v233_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_42d_v233_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_42d_v234_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_42d_v234_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_42d_v235_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_42d_v235_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_42d_v236_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_42d_v236_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_63d_v237_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_63d_v237_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_63d_v238_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_63d_v238_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_63d_v239_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_63d_v239_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_63d_v240_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_63d_v240_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_126d_v241_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_126d_v241_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_126d_v242_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_126d_v242_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_126d_v243_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_126d_v243_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_126d_v244_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_126d_v244_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_252d_v245_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_252d_v245_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_252d_v246_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_252d_v246_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_252d_v247_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_252d_v247_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_252d_v248_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_252d_v248_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_504d_v249_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_504d_v249_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_504d_v250_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_504d_v250_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_504d_v251_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_504d_v251_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_504d_v252_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_504d_v252_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_756d_v253_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_756d_v253_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_756d_v254_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_756d_v254_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_756d_v255_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_756d_v255_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_756d_v256_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_756d_v256_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_1008d_v257_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_1008d_v257_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_1008d_v258_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_1008d_v258_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_1008d_v259_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_1008d_v259_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_1008d_v260_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_1008d_v260_signal},
    "f47_roic_compounder_fin_roic_ewma_slope_1260d_v261_signal": {"func": f47_roic_compounder_fin_roic_ewma_slope_1260d_v261_signal},
    "f47_roic_compounder_fin_invcap_ewma_slope_1260d_v262_signal": {"func": f47_roic_compounder_fin_invcap_ewma_slope_1260d_v262_signal},
    "f47_roic_compounder_fin_netinc_ewma_slope_1260d_v263_signal": {"func": f47_roic_compounder_fin_netinc_ewma_slope_1260d_v263_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_slope_1260d_v264_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 47...")
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
