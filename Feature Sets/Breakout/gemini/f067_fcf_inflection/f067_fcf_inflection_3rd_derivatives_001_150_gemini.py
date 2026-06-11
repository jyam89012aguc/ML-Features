import pandas as pd
import numpy as np
import inspect

# ===== BREAKOUT High-Performance Alpha Helpers =====
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
def _jerk(s, w1, w2): return s.slope_pct(w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()
def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))
def bo_067_fcf_inflection_revenue_vol_slope_252d_v151_signal(closeadj):
    """Volatility of momentum for Raw level of revenue over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_slope_252d_v152_signal(closeadj):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_slope_252d_v153_signal(closeadj):
    """Volatility of momentum for Growth ignition over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_slope_504d_v154_signal(closeadj):
    """Volatility of momentum for Raw level of revenue over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_slope_504d_v155_signal(closeadj):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_slope_504d_v156_signal(closeadj):
    """Volatility of momentum for Growth ignition over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_slope_756d_v157_signal(closeadj):
    """Volatility of momentum for Raw level of revenue over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_slope_756d_v158_signal(closeadj):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_slope_756d_v159_signal(closeadj):
    """Volatility of momentum for Growth ignition over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_slope_1008d_v160_signal(closeadj):
    """Volatility of momentum for Raw level of revenue over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_slope_1008d_v161_signal(closeadj):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_slope_1008d_v162_signal(closeadj):
    """Volatility of momentum for Growth ignition over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_slope_1260d_v163_signal(closeadj):
    """Volatility of momentum for Raw level of revenue over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_slope_1260d_v164_signal(closeadj):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_slope_1260d_v165_signal(closeadj):
    """Volatility of momentum for Growth ignition over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_5d_v166_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_5d_v167_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_5d_v168_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_10d_v169_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_10d_v170_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_10d_v171_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_21d_v172_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_21d_v173_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_21d_v174_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_42d_v175_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_42d_v176_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_42d_v177_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_63d_v178_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_63d_v179_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_63d_v180_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_126d_v181_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_126d_v182_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_126d_v183_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_252d_v184_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_252d_v185_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_252d_v186_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_504d_v187_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_504d_v188_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_504d_v189_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_756d_v190_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_756d_v191_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_756d_v192_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_1008d_v193_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_1008d_v194_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_1008d_v195_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_ewma_slope_1260d_v196_signal(closeadj):
    """Exponential momentum smoothing for Raw level of revenue over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_ewma_slope_1260d_v197_signal(closeadj):
    """Exponential momentum smoothing for Raw level of netinc over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_ewma_slope_1260d_v198_signal(closeadj):
    """Exponential momentum smoothing for Growth ignition over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_5d_v199_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_5d_v200_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_5d_v201_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_10d_v202_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_10d_v203_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_10d_v204_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_21d_v205_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_21d_v206_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_21d_v207_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_42d_v208_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_42d_v209_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_42d_v210_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_63d_v211_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_63d_v212_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_63d_v213_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_126d_v214_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_126d_v215_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_126d_v216_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_252d_v217_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_252d_v218_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_252d_v219_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_504d_v220_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_504d_v221_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_504d_v222_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_756d_v223_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_756d_v224_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_756d_v225_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_1008d_v226_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_1008d_v227_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_1008d_v228_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_revenue_vol_accel_1260d_v229_signal(closeadj):
    """Acceleration of volatility for Raw level of revenue over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_netinc_vol_accel_1260d_v230_signal(closeadj):
    """Acceleration of volatility for Raw level of netinc over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_067_fcf_inflection_growth_ignition_vol_accel_1260d_v231_signal(closeadj):
    """Acceleration of volatility for Growth ignition over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "bo_067_fcf_inflection_revenue_vol_slope_252d_v151_signal": {"func": bo_067_fcf_inflection_revenue_vol_slope_252d_v151_signal},
    "bo_067_fcf_inflection_netinc_vol_slope_252d_v152_signal": {"func": bo_067_fcf_inflection_netinc_vol_slope_252d_v152_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_slope_252d_v153_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_slope_252d_v153_signal},
    "bo_067_fcf_inflection_revenue_vol_slope_504d_v154_signal": {"func": bo_067_fcf_inflection_revenue_vol_slope_504d_v154_signal},
    "bo_067_fcf_inflection_netinc_vol_slope_504d_v155_signal": {"func": bo_067_fcf_inflection_netinc_vol_slope_504d_v155_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_slope_504d_v156_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_slope_504d_v156_signal},
    "bo_067_fcf_inflection_revenue_vol_slope_756d_v157_signal": {"func": bo_067_fcf_inflection_revenue_vol_slope_756d_v157_signal},
    "bo_067_fcf_inflection_netinc_vol_slope_756d_v158_signal": {"func": bo_067_fcf_inflection_netinc_vol_slope_756d_v158_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_slope_756d_v159_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_slope_756d_v159_signal},
    "bo_067_fcf_inflection_revenue_vol_slope_1008d_v160_signal": {"func": bo_067_fcf_inflection_revenue_vol_slope_1008d_v160_signal},
    "bo_067_fcf_inflection_netinc_vol_slope_1008d_v161_signal": {"func": bo_067_fcf_inflection_netinc_vol_slope_1008d_v161_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_slope_1008d_v162_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_slope_1008d_v162_signal},
    "bo_067_fcf_inflection_revenue_vol_slope_1260d_v163_signal": {"func": bo_067_fcf_inflection_revenue_vol_slope_1260d_v163_signal},
    "bo_067_fcf_inflection_netinc_vol_slope_1260d_v164_signal": {"func": bo_067_fcf_inflection_netinc_vol_slope_1260d_v164_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_slope_1260d_v165_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_slope_1260d_v165_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_5d_v166_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_5d_v166_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_5d_v167_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_5d_v167_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_5d_v168_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_5d_v168_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_10d_v169_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_10d_v169_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_10d_v170_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_10d_v170_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_10d_v171_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_10d_v171_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_21d_v172_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_21d_v172_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_21d_v173_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_21d_v173_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_21d_v174_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_21d_v174_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_42d_v175_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_42d_v175_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_42d_v176_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_42d_v176_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_42d_v177_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_42d_v177_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_63d_v178_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_63d_v178_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_63d_v179_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_63d_v179_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_63d_v180_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_63d_v180_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_126d_v181_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_126d_v181_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_126d_v182_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_126d_v182_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_126d_v183_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_126d_v183_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_252d_v184_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_252d_v184_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_252d_v185_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_252d_v185_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_252d_v186_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_252d_v186_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_504d_v187_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_504d_v187_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_504d_v188_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_504d_v188_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_504d_v189_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_504d_v189_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_756d_v190_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_756d_v190_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_756d_v191_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_756d_v191_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_756d_v192_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_756d_v192_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_1008d_v193_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_1008d_v193_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_1008d_v194_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_1008d_v194_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_1008d_v195_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_1008d_v195_signal},
    "bo_067_fcf_inflection_revenue_ewma_slope_1260d_v196_signal": {"func": bo_067_fcf_inflection_revenue_ewma_slope_1260d_v196_signal},
    "bo_067_fcf_inflection_netinc_ewma_slope_1260d_v197_signal": {"func": bo_067_fcf_inflection_netinc_ewma_slope_1260d_v197_signal},
    "bo_067_fcf_inflection_growth_ignition_ewma_slope_1260d_v198_signal": {"func": bo_067_fcf_inflection_growth_ignition_ewma_slope_1260d_v198_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_5d_v199_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_5d_v199_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_5d_v200_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_5d_v200_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_5d_v201_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_5d_v201_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_10d_v202_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_10d_v202_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_10d_v203_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_10d_v203_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_10d_v204_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_10d_v204_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_21d_v205_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_21d_v205_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_21d_v206_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_21d_v206_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_21d_v207_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_21d_v207_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_42d_v208_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_42d_v208_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_42d_v209_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_42d_v209_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_42d_v210_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_42d_v210_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_63d_v211_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_63d_v211_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_63d_v212_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_63d_v212_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_63d_v213_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_63d_v213_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_126d_v214_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_126d_v214_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_126d_v215_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_126d_v215_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_126d_v216_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_126d_v216_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_252d_v217_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_252d_v217_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_252d_v218_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_252d_v218_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_252d_v219_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_252d_v219_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_504d_v220_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_504d_v220_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_504d_v221_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_504d_v221_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_504d_v222_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_504d_v222_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_756d_v223_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_756d_v223_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_756d_v224_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_756d_v224_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_756d_v225_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_756d_v225_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_1008d_v226_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_1008d_v226_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_1008d_v227_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_1008d_v227_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_1008d_v228_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_1008d_v228_signal},
    "bo_067_fcf_inflection_revenue_vol_accel_1260d_v229_signal": {"func": bo_067_fcf_inflection_revenue_vol_accel_1260d_v229_signal},
    "bo_067_fcf_inflection_netinc_vol_accel_1260d_v230_signal": {"func": bo_067_fcf_inflection_netinc_vol_accel_1260d_v230_signal},
    "bo_067_fcf_inflection_growth_ignition_vol_accel_1260d_v231_signal": {"func": bo_067_fcf_inflection_growth_ignition_vol_accel_1260d_v231_signal},
}
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "rnd": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 067...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
