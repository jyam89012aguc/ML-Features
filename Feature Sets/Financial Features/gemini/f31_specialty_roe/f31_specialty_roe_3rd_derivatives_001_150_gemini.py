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

def f31_specialty_roe_roic_mom_z_63d_v151_signal(roic):
    """Relative momentum strength for Raw level of roic over 63d window."""
    res = _z(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_63d_v152_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 63d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_mom_z_126d_v153_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_mom_z_126d_v154_signal(equity):
    """Relative momentum strength for Raw level of equity over 126d window."""
    res = _z(_slope_pct(equity, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_mom_z_126d_v155_signal(roic):
    """Relative momentum strength for Raw level of roic over 126d window."""
    res = _z(_slope_pct(roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_126d_v156_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 126d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_mom_z_252d_v157_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_mom_z_252d_v158_signal(equity):
    """Relative momentum strength for Raw level of equity over 252d window."""
    res = _z(_slope_pct(equity, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_mom_z_252d_v159_signal(roic):
    """Relative momentum strength for Raw level of roic over 252d window."""
    res = _z(_slope_pct(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_252d_v160_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 252d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_mom_z_504d_v161_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_mom_z_504d_v162_signal(equity):
    """Relative momentum strength for Raw level of equity over 504d window."""
    res = _z(_slope_pct(equity, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_mom_z_504d_v163_signal(roic):
    """Relative momentum strength for Raw level of roic over 504d window."""
    res = _z(_slope_pct(roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_504d_v164_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 504d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_mom_z_756d_v165_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_mom_z_756d_v166_signal(equity):
    """Relative momentum strength for Raw level of equity over 756d window."""
    res = _z(_slope_pct(equity, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_mom_z_756d_v167_signal(roic):
    """Relative momentum strength for Raw level of roic over 756d window."""
    res = _z(_slope_pct(roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_756d_v168_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 756d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_mom_z_1008d_v169_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_mom_z_1008d_v170_signal(equity):
    """Relative momentum strength for Raw level of equity over 1008d window."""
    res = _z(_slope_pct(equity, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_mom_z_1008d_v171_signal(roic):
    """Relative momentum strength for Raw level of roic over 1008d window."""
    res = _z(_slope_pct(roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_1008d_v172_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 1008d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_mom_z_1260d_v173_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_mom_z_1260d_v174_signal(equity):
    """Relative momentum strength for Raw level of equity over 1260d window."""
    res = _z(_slope_pct(equity, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_mom_z_1260d_v175_signal(roic):
    """Relative momentum strength for Raw level of roic over 1260d window."""
    res = _z(_slope_pct(roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_mom_z_1260d_v176_signal(netinc, equity, roic):
    """Relative momentum strength for ROIC-amplified ROE over 1260d window."""
    res = _z(_slope_pct(_ratio(netinc, equity) * roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_5d_v177_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_5d_v178_signal(equity):
    """Volatility of momentum for Raw level of equity over 5d window."""
    res = _std(_slope_pct(equity, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_5d_v179_signal(roic):
    """Volatility of momentum for Raw level of roic over 5d window."""
    res = _std(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_5d_v180_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 5d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_10d_v181_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_10d_v182_signal(equity):
    """Volatility of momentum for Raw level of equity over 10d window."""
    res = _std(_slope_pct(equity, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_10d_v183_signal(roic):
    """Volatility of momentum for Raw level of roic over 10d window."""
    res = _std(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_10d_v184_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 10d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_21d_v185_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_21d_v186_signal(equity):
    """Volatility of momentum for Raw level of equity over 21d window."""
    res = _std(_slope_pct(equity, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_21d_v187_signal(roic):
    """Volatility of momentum for Raw level of roic over 21d window."""
    res = _std(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_21d_v188_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 21d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_42d_v189_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_42d_v190_signal(equity):
    """Volatility of momentum for Raw level of equity over 42d window."""
    res = _std(_slope_pct(equity, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_42d_v191_signal(roic):
    """Volatility of momentum for Raw level of roic over 42d window."""
    res = _std(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_42d_v192_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 42d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_63d_v193_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_63d_v194_signal(equity):
    """Volatility of momentum for Raw level of equity over 63d window."""
    res = _std(_slope_pct(equity, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_63d_v195_signal(roic):
    """Volatility of momentum for Raw level of roic over 63d window."""
    res = _std(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_63d_v196_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 63d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_126d_v197_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_126d_v198_signal(equity):
    """Volatility of momentum for Raw level of equity over 126d window."""
    res = _std(_slope_pct(equity, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_126d_v199_signal(roic):
    """Volatility of momentum for Raw level of roic over 126d window."""
    res = _std(_slope_pct(roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_126d_v200_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 126d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_252d_v201_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_252d_v202_signal(equity):
    """Volatility of momentum for Raw level of equity over 252d window."""
    res = _std(_slope_pct(equity, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_252d_v203_signal(roic):
    """Volatility of momentum for Raw level of roic over 252d window."""
    res = _std(_slope_pct(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_252d_v204_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 252d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_504d_v205_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_504d_v206_signal(equity):
    """Volatility of momentum for Raw level of equity over 504d window."""
    res = _std(_slope_pct(equity, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_504d_v207_signal(roic):
    """Volatility of momentum for Raw level of roic over 504d window."""
    res = _std(_slope_pct(roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_504d_v208_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 504d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_756d_v209_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_756d_v210_signal(equity):
    """Volatility of momentum for Raw level of equity over 756d window."""
    res = _std(_slope_pct(equity, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_756d_v211_signal(roic):
    """Volatility of momentum for Raw level of roic over 756d window."""
    res = _std(_slope_pct(roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_756d_v212_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 756d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_1008d_v213_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_1008d_v214_signal(equity):
    """Volatility of momentum for Raw level of equity over 1008d window."""
    res = _std(_slope_pct(equity, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_1008d_v215_signal(roic):
    """Volatility of momentum for Raw level of roic over 1008d window."""
    res = _std(_slope_pct(roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_1008d_v216_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 1008d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_vol_slope_1260d_v217_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_vol_slope_1260d_v218_signal(equity):
    """Volatility of momentum for Raw level of equity over 1260d window."""
    res = _std(_slope_pct(equity, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_vol_slope_1260d_v219_signal(roic):
    """Volatility of momentum for Raw level of roic over 1260d window."""
    res = _std(_slope_pct(roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_vol_slope_1260d_v220_signal(netinc, equity, roic):
    """Volatility of momentum for ROIC-amplified ROE over 1260d window."""
    res = _std(_slope_pct(_ratio(netinc, equity) * roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_5d_v221_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _ewma(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_5d_v222_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 5d window."""
    res = _ewma(_slope_pct(equity, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_5d_v223_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 5d window."""
    res = _ewma(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_5d_v224_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 5d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_10d_v225_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _ewma(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_10d_v226_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 10d window."""
    res = _ewma(_slope_pct(equity, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_10d_v227_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 10d window."""
    res = _ewma(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_10d_v228_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 10d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_21d_v229_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _ewma(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_21d_v230_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 21d window."""
    res = _ewma(_slope_pct(equity, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_21d_v231_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 21d window."""
    res = _ewma(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_21d_v232_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 21d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_42d_v233_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _ewma(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_42d_v234_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 42d window."""
    res = _ewma(_slope_pct(equity, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_42d_v235_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 42d window."""
    res = _ewma(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_42d_v236_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 42d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_63d_v237_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _ewma(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_63d_v238_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 63d window."""
    res = _ewma(_slope_pct(equity, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_63d_v239_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 63d window."""
    res = _ewma(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_63d_v240_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 63d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_126d_v241_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 126d window."""
    res = _ewma(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_126d_v242_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 126d window."""
    res = _ewma(_slope_pct(equity, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_126d_v243_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 126d window."""
    res = _ewma(_slope_pct(roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_126d_v244_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 126d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_252d_v245_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 252d window."""
    res = _ewma(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_252d_v246_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 252d window."""
    res = _ewma(_slope_pct(equity, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_252d_v247_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 252d window."""
    res = _ewma(_slope_pct(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_252d_v248_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 252d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_504d_v249_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 504d window."""
    res = _ewma(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_504d_v250_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 504d window."""
    res = _ewma(_slope_pct(equity, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_504d_v251_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 504d window."""
    res = _ewma(_slope_pct(roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_504d_v252_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 504d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_756d_v253_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 756d window."""
    res = _ewma(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_756d_v254_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 756d window."""
    res = _ewma(_slope_pct(equity, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_756d_v255_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 756d window."""
    res = _ewma(_slope_pct(roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_756d_v256_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 756d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_1008d_v257_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1008d window."""
    res = _ewma(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_1008d_v258_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 1008d window."""
    res = _ewma(_slope_pct(equity, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_1008d_v259_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 1008d window."""
    res = _ewma(_slope_pct(roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_1008d_v260_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 1008d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_slope_1260d_v261_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1260d window."""
    res = _ewma(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_slope_1260d_v262_signal(equity):
    """Exponential momentum smoothing for Raw level of equity over 1260d window."""
    res = _ewma(_slope_pct(equity, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_slope_1260d_v263_signal(roic):
    """Exponential momentum smoothing for Raw level of roic over 1260d window."""
    res = _ewma(_slope_pct(roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_slope_1260d_v264_signal(netinc, equity, roic):
    """Exponential momentum smoothing for ROIC-amplified ROE over 1260d window."""
    res = _ewma(_slope_pct(_ratio(netinc, equity) * roic, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f31_specialty_roe_roic_mom_z_63d_v151_signal": {"func": f31_specialty_roe_roic_mom_z_63d_v151_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_63d_v152_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_63d_v152_signal},
    "f31_specialty_roe_netinc_mom_z_126d_v153_signal": {"func": f31_specialty_roe_netinc_mom_z_126d_v153_signal},
    "f31_specialty_roe_equity_mom_z_126d_v154_signal": {"func": f31_specialty_roe_equity_mom_z_126d_v154_signal},
    "f31_specialty_roe_roic_mom_z_126d_v155_signal": {"func": f31_specialty_roe_roic_mom_z_126d_v155_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_126d_v156_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_126d_v156_signal},
    "f31_specialty_roe_netinc_mom_z_252d_v157_signal": {"func": f31_specialty_roe_netinc_mom_z_252d_v157_signal},
    "f31_specialty_roe_equity_mom_z_252d_v158_signal": {"func": f31_specialty_roe_equity_mom_z_252d_v158_signal},
    "f31_specialty_roe_roic_mom_z_252d_v159_signal": {"func": f31_specialty_roe_roic_mom_z_252d_v159_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_252d_v160_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_252d_v160_signal},
    "f31_specialty_roe_netinc_mom_z_504d_v161_signal": {"func": f31_specialty_roe_netinc_mom_z_504d_v161_signal},
    "f31_specialty_roe_equity_mom_z_504d_v162_signal": {"func": f31_specialty_roe_equity_mom_z_504d_v162_signal},
    "f31_specialty_roe_roic_mom_z_504d_v163_signal": {"func": f31_specialty_roe_roic_mom_z_504d_v163_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_504d_v164_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_504d_v164_signal},
    "f31_specialty_roe_netinc_mom_z_756d_v165_signal": {"func": f31_specialty_roe_netinc_mom_z_756d_v165_signal},
    "f31_specialty_roe_equity_mom_z_756d_v166_signal": {"func": f31_specialty_roe_equity_mom_z_756d_v166_signal},
    "f31_specialty_roe_roic_mom_z_756d_v167_signal": {"func": f31_specialty_roe_roic_mom_z_756d_v167_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_756d_v168_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_756d_v168_signal},
    "f31_specialty_roe_netinc_mom_z_1008d_v169_signal": {"func": f31_specialty_roe_netinc_mom_z_1008d_v169_signal},
    "f31_specialty_roe_equity_mom_z_1008d_v170_signal": {"func": f31_specialty_roe_equity_mom_z_1008d_v170_signal},
    "f31_specialty_roe_roic_mom_z_1008d_v171_signal": {"func": f31_specialty_roe_roic_mom_z_1008d_v171_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_1008d_v172_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_1008d_v172_signal},
    "f31_specialty_roe_netinc_mom_z_1260d_v173_signal": {"func": f31_specialty_roe_netinc_mom_z_1260d_v173_signal},
    "f31_specialty_roe_equity_mom_z_1260d_v174_signal": {"func": f31_specialty_roe_equity_mom_z_1260d_v174_signal},
    "f31_specialty_roe_roic_mom_z_1260d_v175_signal": {"func": f31_specialty_roe_roic_mom_z_1260d_v175_signal},
    "f31_specialty_roe_adjusted_roe_mom_z_1260d_v176_signal": {"func": f31_specialty_roe_adjusted_roe_mom_z_1260d_v176_signal},
    "f31_specialty_roe_netinc_vol_slope_5d_v177_signal": {"func": f31_specialty_roe_netinc_vol_slope_5d_v177_signal},
    "f31_specialty_roe_equity_vol_slope_5d_v178_signal": {"func": f31_specialty_roe_equity_vol_slope_5d_v178_signal},
    "f31_specialty_roe_roic_vol_slope_5d_v179_signal": {"func": f31_specialty_roe_roic_vol_slope_5d_v179_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_5d_v180_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_5d_v180_signal},
    "f31_specialty_roe_netinc_vol_slope_10d_v181_signal": {"func": f31_specialty_roe_netinc_vol_slope_10d_v181_signal},
    "f31_specialty_roe_equity_vol_slope_10d_v182_signal": {"func": f31_specialty_roe_equity_vol_slope_10d_v182_signal},
    "f31_specialty_roe_roic_vol_slope_10d_v183_signal": {"func": f31_specialty_roe_roic_vol_slope_10d_v183_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_10d_v184_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_10d_v184_signal},
    "f31_specialty_roe_netinc_vol_slope_21d_v185_signal": {"func": f31_specialty_roe_netinc_vol_slope_21d_v185_signal},
    "f31_specialty_roe_equity_vol_slope_21d_v186_signal": {"func": f31_specialty_roe_equity_vol_slope_21d_v186_signal},
    "f31_specialty_roe_roic_vol_slope_21d_v187_signal": {"func": f31_specialty_roe_roic_vol_slope_21d_v187_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_21d_v188_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_21d_v188_signal},
    "f31_specialty_roe_netinc_vol_slope_42d_v189_signal": {"func": f31_specialty_roe_netinc_vol_slope_42d_v189_signal},
    "f31_specialty_roe_equity_vol_slope_42d_v190_signal": {"func": f31_specialty_roe_equity_vol_slope_42d_v190_signal},
    "f31_specialty_roe_roic_vol_slope_42d_v191_signal": {"func": f31_specialty_roe_roic_vol_slope_42d_v191_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_42d_v192_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_42d_v192_signal},
    "f31_specialty_roe_netinc_vol_slope_63d_v193_signal": {"func": f31_specialty_roe_netinc_vol_slope_63d_v193_signal},
    "f31_specialty_roe_equity_vol_slope_63d_v194_signal": {"func": f31_specialty_roe_equity_vol_slope_63d_v194_signal},
    "f31_specialty_roe_roic_vol_slope_63d_v195_signal": {"func": f31_specialty_roe_roic_vol_slope_63d_v195_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_63d_v196_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_63d_v196_signal},
    "f31_specialty_roe_netinc_vol_slope_126d_v197_signal": {"func": f31_specialty_roe_netinc_vol_slope_126d_v197_signal},
    "f31_specialty_roe_equity_vol_slope_126d_v198_signal": {"func": f31_specialty_roe_equity_vol_slope_126d_v198_signal},
    "f31_specialty_roe_roic_vol_slope_126d_v199_signal": {"func": f31_specialty_roe_roic_vol_slope_126d_v199_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_126d_v200_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_126d_v200_signal},
    "f31_specialty_roe_netinc_vol_slope_252d_v201_signal": {"func": f31_specialty_roe_netinc_vol_slope_252d_v201_signal},
    "f31_specialty_roe_equity_vol_slope_252d_v202_signal": {"func": f31_specialty_roe_equity_vol_slope_252d_v202_signal},
    "f31_specialty_roe_roic_vol_slope_252d_v203_signal": {"func": f31_specialty_roe_roic_vol_slope_252d_v203_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_252d_v204_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_252d_v204_signal},
    "f31_specialty_roe_netinc_vol_slope_504d_v205_signal": {"func": f31_specialty_roe_netinc_vol_slope_504d_v205_signal},
    "f31_specialty_roe_equity_vol_slope_504d_v206_signal": {"func": f31_specialty_roe_equity_vol_slope_504d_v206_signal},
    "f31_specialty_roe_roic_vol_slope_504d_v207_signal": {"func": f31_specialty_roe_roic_vol_slope_504d_v207_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_504d_v208_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_504d_v208_signal},
    "f31_specialty_roe_netinc_vol_slope_756d_v209_signal": {"func": f31_specialty_roe_netinc_vol_slope_756d_v209_signal},
    "f31_specialty_roe_equity_vol_slope_756d_v210_signal": {"func": f31_specialty_roe_equity_vol_slope_756d_v210_signal},
    "f31_specialty_roe_roic_vol_slope_756d_v211_signal": {"func": f31_specialty_roe_roic_vol_slope_756d_v211_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_756d_v212_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_756d_v212_signal},
    "f31_specialty_roe_netinc_vol_slope_1008d_v213_signal": {"func": f31_specialty_roe_netinc_vol_slope_1008d_v213_signal},
    "f31_specialty_roe_equity_vol_slope_1008d_v214_signal": {"func": f31_specialty_roe_equity_vol_slope_1008d_v214_signal},
    "f31_specialty_roe_roic_vol_slope_1008d_v215_signal": {"func": f31_specialty_roe_roic_vol_slope_1008d_v215_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_1008d_v216_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_1008d_v216_signal},
    "f31_specialty_roe_netinc_vol_slope_1260d_v217_signal": {"func": f31_specialty_roe_netinc_vol_slope_1260d_v217_signal},
    "f31_specialty_roe_equity_vol_slope_1260d_v218_signal": {"func": f31_specialty_roe_equity_vol_slope_1260d_v218_signal},
    "f31_specialty_roe_roic_vol_slope_1260d_v219_signal": {"func": f31_specialty_roe_roic_vol_slope_1260d_v219_signal},
    "f31_specialty_roe_adjusted_roe_vol_slope_1260d_v220_signal": {"func": f31_specialty_roe_adjusted_roe_vol_slope_1260d_v220_signal},
    "f31_specialty_roe_netinc_ewma_slope_5d_v221_signal": {"func": f31_specialty_roe_netinc_ewma_slope_5d_v221_signal},
    "f31_specialty_roe_equity_ewma_slope_5d_v222_signal": {"func": f31_specialty_roe_equity_ewma_slope_5d_v222_signal},
    "f31_specialty_roe_roic_ewma_slope_5d_v223_signal": {"func": f31_specialty_roe_roic_ewma_slope_5d_v223_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_5d_v224_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_5d_v224_signal},
    "f31_specialty_roe_netinc_ewma_slope_10d_v225_signal": {"func": f31_specialty_roe_netinc_ewma_slope_10d_v225_signal},
    "f31_specialty_roe_equity_ewma_slope_10d_v226_signal": {"func": f31_specialty_roe_equity_ewma_slope_10d_v226_signal},
    "f31_specialty_roe_roic_ewma_slope_10d_v227_signal": {"func": f31_specialty_roe_roic_ewma_slope_10d_v227_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_10d_v228_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_10d_v228_signal},
    "f31_specialty_roe_netinc_ewma_slope_21d_v229_signal": {"func": f31_specialty_roe_netinc_ewma_slope_21d_v229_signal},
    "f31_specialty_roe_equity_ewma_slope_21d_v230_signal": {"func": f31_specialty_roe_equity_ewma_slope_21d_v230_signal},
    "f31_specialty_roe_roic_ewma_slope_21d_v231_signal": {"func": f31_specialty_roe_roic_ewma_slope_21d_v231_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_21d_v232_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_21d_v232_signal},
    "f31_specialty_roe_netinc_ewma_slope_42d_v233_signal": {"func": f31_specialty_roe_netinc_ewma_slope_42d_v233_signal},
    "f31_specialty_roe_equity_ewma_slope_42d_v234_signal": {"func": f31_specialty_roe_equity_ewma_slope_42d_v234_signal},
    "f31_specialty_roe_roic_ewma_slope_42d_v235_signal": {"func": f31_specialty_roe_roic_ewma_slope_42d_v235_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_42d_v236_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_42d_v236_signal},
    "f31_specialty_roe_netinc_ewma_slope_63d_v237_signal": {"func": f31_specialty_roe_netinc_ewma_slope_63d_v237_signal},
    "f31_specialty_roe_equity_ewma_slope_63d_v238_signal": {"func": f31_specialty_roe_equity_ewma_slope_63d_v238_signal},
    "f31_specialty_roe_roic_ewma_slope_63d_v239_signal": {"func": f31_specialty_roe_roic_ewma_slope_63d_v239_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_63d_v240_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_63d_v240_signal},
    "f31_specialty_roe_netinc_ewma_slope_126d_v241_signal": {"func": f31_specialty_roe_netinc_ewma_slope_126d_v241_signal},
    "f31_specialty_roe_equity_ewma_slope_126d_v242_signal": {"func": f31_specialty_roe_equity_ewma_slope_126d_v242_signal},
    "f31_specialty_roe_roic_ewma_slope_126d_v243_signal": {"func": f31_specialty_roe_roic_ewma_slope_126d_v243_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_126d_v244_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_126d_v244_signal},
    "f31_specialty_roe_netinc_ewma_slope_252d_v245_signal": {"func": f31_specialty_roe_netinc_ewma_slope_252d_v245_signal},
    "f31_specialty_roe_equity_ewma_slope_252d_v246_signal": {"func": f31_specialty_roe_equity_ewma_slope_252d_v246_signal},
    "f31_specialty_roe_roic_ewma_slope_252d_v247_signal": {"func": f31_specialty_roe_roic_ewma_slope_252d_v247_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_252d_v248_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_252d_v248_signal},
    "f31_specialty_roe_netinc_ewma_slope_504d_v249_signal": {"func": f31_specialty_roe_netinc_ewma_slope_504d_v249_signal},
    "f31_specialty_roe_equity_ewma_slope_504d_v250_signal": {"func": f31_specialty_roe_equity_ewma_slope_504d_v250_signal},
    "f31_specialty_roe_roic_ewma_slope_504d_v251_signal": {"func": f31_specialty_roe_roic_ewma_slope_504d_v251_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_504d_v252_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_504d_v252_signal},
    "f31_specialty_roe_netinc_ewma_slope_756d_v253_signal": {"func": f31_specialty_roe_netinc_ewma_slope_756d_v253_signal},
    "f31_specialty_roe_equity_ewma_slope_756d_v254_signal": {"func": f31_specialty_roe_equity_ewma_slope_756d_v254_signal},
    "f31_specialty_roe_roic_ewma_slope_756d_v255_signal": {"func": f31_specialty_roe_roic_ewma_slope_756d_v255_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_756d_v256_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_756d_v256_signal},
    "f31_specialty_roe_netinc_ewma_slope_1008d_v257_signal": {"func": f31_specialty_roe_netinc_ewma_slope_1008d_v257_signal},
    "f31_specialty_roe_equity_ewma_slope_1008d_v258_signal": {"func": f31_specialty_roe_equity_ewma_slope_1008d_v258_signal},
    "f31_specialty_roe_roic_ewma_slope_1008d_v259_signal": {"func": f31_specialty_roe_roic_ewma_slope_1008d_v259_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_1008d_v260_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_1008d_v260_signal},
    "f31_specialty_roe_netinc_ewma_slope_1260d_v261_signal": {"func": f31_specialty_roe_netinc_ewma_slope_1260d_v261_signal},
    "f31_specialty_roe_equity_ewma_slope_1260d_v262_signal": {"func": f31_specialty_roe_equity_ewma_slope_1260d_v262_signal},
    "f31_specialty_roe_roic_ewma_slope_1260d_v263_signal": {"func": f31_specialty_roe_roic_ewma_slope_1260d_v263_signal},
    "f31_specialty_roe_adjusted_roe_ewma_slope_1260d_v264_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 31...")
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
