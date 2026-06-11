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

def f24_distressed_alpha_liabilitiesc_mom_z_63d_v151_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 63d window."""
    res = _z(_slope_pct(liabilitiesc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_63d_v152_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 63d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_mom_z_126d_v153_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_mom_z_126d_v154_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_mom_z_126d_v155_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 126d window."""
    res = _z(_slope_pct(liabilitiesc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_126d_v156_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 126d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_mom_z_252d_v157_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_mom_z_252d_v158_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_mom_z_252d_v159_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 252d window."""
    res = _z(_slope_pct(liabilitiesc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_252d_v160_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 252d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_mom_z_504d_v161_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_mom_z_504d_v162_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_mom_z_504d_v163_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 504d window."""
    res = _z(_slope_pct(liabilitiesc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_504d_v164_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 504d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_mom_z_756d_v165_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_mom_z_756d_v166_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_mom_z_756d_v167_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 756d window."""
    res = _z(_slope_pct(liabilitiesc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_756d_v168_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 756d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_mom_z_1008d_v169_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_mom_z_1008d_v170_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_mom_z_1008d_v171_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 1008d window."""
    res = _z(_slope_pct(liabilitiesc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_1008d_v172_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 1008d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_mom_z_1260d_v173_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_mom_z_1260d_v174_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_mom_z_1260d_v175_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 1260d window."""
    res = _z(_slope_pct(liabilitiesc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_mom_z_1260d_v176_signal(netinc, liabilitiesc):
    """Relative momentum strength for Net income relative to short-term liabilities over 1260d window."""
    res = _z(_slope_pct(_ratio(netinc, liabilitiesc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_5d_v177_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_5d_v178_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_5d_v179_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 5d window."""
    res = _std(_slope_pct(liabilitiesc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_5d_v180_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 5d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_10d_v181_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_10d_v182_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_10d_v183_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 10d window."""
    res = _std(_slope_pct(liabilitiesc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_10d_v184_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 10d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_21d_v185_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_21d_v186_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_21d_v187_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 21d window."""
    res = _std(_slope_pct(liabilitiesc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_21d_v188_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 21d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_42d_v189_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_42d_v190_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_42d_v191_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 42d window."""
    res = _std(_slope_pct(liabilitiesc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_42d_v192_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 42d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_63d_v193_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_63d_v194_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_63d_v195_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 63d window."""
    res = _std(_slope_pct(liabilitiesc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_63d_v196_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 63d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_126d_v197_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_126d_v198_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_126d_v199_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 126d window."""
    res = _std(_slope_pct(liabilitiesc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_126d_v200_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 126d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_252d_v201_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_252d_v202_signal(assets):
    """Volatility of momentum for Raw level of assets over 252d window."""
    res = _std(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_252d_v203_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 252d window."""
    res = _std(_slope_pct(liabilitiesc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_252d_v204_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 252d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_504d_v205_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_504d_v206_signal(assets):
    """Volatility of momentum for Raw level of assets over 504d window."""
    res = _std(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_504d_v207_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 504d window."""
    res = _std(_slope_pct(liabilitiesc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_504d_v208_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 504d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_756d_v209_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_756d_v210_signal(assets):
    """Volatility of momentum for Raw level of assets over 756d window."""
    res = _std(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_756d_v211_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 756d window."""
    res = _std(_slope_pct(liabilitiesc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_756d_v212_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 756d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_1008d_v213_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_1008d_v214_signal(assets):
    """Volatility of momentum for Raw level of assets over 1008d window."""
    res = _std(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_1008d_v215_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 1008d window."""
    res = _std(_slope_pct(liabilitiesc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_1008d_v216_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 1008d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_vol_slope_1260d_v217_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_vol_slope_1260d_v218_signal(assets):
    """Volatility of momentum for Raw level of assets over 1260d window."""
    res = _std(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_vol_slope_1260d_v219_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 1260d window."""
    res = _std(_slope_pct(liabilitiesc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_vol_slope_1260d_v220_signal(netinc, liabilitiesc):
    """Volatility of momentum for Net income relative to short-term liabilities over 1260d window."""
    res = _std(_slope_pct(_ratio(netinc, liabilitiesc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_5d_v221_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _ewma(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_5d_v222_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 5d window."""
    res = _ewma(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_5d_v223_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 5d window."""
    res = _ewma(_slope_pct(liabilitiesc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_5d_v224_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 5d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_10d_v225_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _ewma(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_10d_v226_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 10d window."""
    res = _ewma(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_10d_v227_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 10d window."""
    res = _ewma(_slope_pct(liabilitiesc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_10d_v228_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 10d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_21d_v229_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _ewma(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_21d_v230_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 21d window."""
    res = _ewma(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_21d_v231_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 21d window."""
    res = _ewma(_slope_pct(liabilitiesc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_21d_v232_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 21d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_42d_v233_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _ewma(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_42d_v234_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 42d window."""
    res = _ewma(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_42d_v235_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 42d window."""
    res = _ewma(_slope_pct(liabilitiesc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_42d_v236_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 42d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_63d_v237_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _ewma(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_63d_v238_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 63d window."""
    res = _ewma(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_63d_v239_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 63d window."""
    res = _ewma(_slope_pct(liabilitiesc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_63d_v240_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 63d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_126d_v241_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 126d window."""
    res = _ewma(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_126d_v242_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 126d window."""
    res = _ewma(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_126d_v243_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 126d window."""
    res = _ewma(_slope_pct(liabilitiesc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_126d_v244_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 126d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_252d_v245_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 252d window."""
    res = _ewma(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_252d_v246_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 252d window."""
    res = _ewma(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_252d_v247_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 252d window."""
    res = _ewma(_slope_pct(liabilitiesc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_252d_v248_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 252d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_504d_v249_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 504d window."""
    res = _ewma(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_504d_v250_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 504d window."""
    res = _ewma(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_504d_v251_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 504d window."""
    res = _ewma(_slope_pct(liabilitiesc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_504d_v252_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 504d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_756d_v253_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 756d window."""
    res = _ewma(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_756d_v254_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 756d window."""
    res = _ewma(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_756d_v255_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 756d window."""
    res = _ewma(_slope_pct(liabilitiesc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_756d_v256_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 756d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_1008d_v257_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1008d window."""
    res = _ewma(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_1008d_v258_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 1008d window."""
    res = _ewma(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_1008d_v259_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 1008d window."""
    res = _ewma(_slope_pct(liabilitiesc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_1008d_v260_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 1008d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_netinc_ewma_slope_1260d_v261_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 1260d window."""
    res = _ewma(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_assets_ewma_slope_1260d_v262_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 1260d window."""
    res = _ewma(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_liabilitiesc_ewma_slope_1260d_v263_signal(liabilitiesc):
    """Exponential momentum smoothing for Raw level of liabilitiesc over 1260d window."""
    res = _ewma(_slope_pct(liabilitiesc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_distressed_alpha_recovery_score_ewma_slope_1260d_v264_signal(netinc, liabilitiesc):
    """Exponential momentum smoothing for Net income relative to short-term liabilities over 1260d window."""
    res = _ewma(_slope_pct(_ratio(netinc, liabilitiesc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f24_distressed_alpha_liabilitiesc_mom_z_63d_v151_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_63d_v151_signal},
    "f24_distressed_alpha_recovery_score_mom_z_63d_v152_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_63d_v152_signal},
    "f24_distressed_alpha_netinc_mom_z_126d_v153_signal": {"func": f24_distressed_alpha_netinc_mom_z_126d_v153_signal},
    "f24_distressed_alpha_assets_mom_z_126d_v154_signal": {"func": f24_distressed_alpha_assets_mom_z_126d_v154_signal},
    "f24_distressed_alpha_liabilitiesc_mom_z_126d_v155_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_126d_v155_signal},
    "f24_distressed_alpha_recovery_score_mom_z_126d_v156_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_126d_v156_signal},
    "f24_distressed_alpha_netinc_mom_z_252d_v157_signal": {"func": f24_distressed_alpha_netinc_mom_z_252d_v157_signal},
    "f24_distressed_alpha_assets_mom_z_252d_v158_signal": {"func": f24_distressed_alpha_assets_mom_z_252d_v158_signal},
    "f24_distressed_alpha_liabilitiesc_mom_z_252d_v159_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_252d_v159_signal},
    "f24_distressed_alpha_recovery_score_mom_z_252d_v160_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_252d_v160_signal},
    "f24_distressed_alpha_netinc_mom_z_504d_v161_signal": {"func": f24_distressed_alpha_netinc_mom_z_504d_v161_signal},
    "f24_distressed_alpha_assets_mom_z_504d_v162_signal": {"func": f24_distressed_alpha_assets_mom_z_504d_v162_signal},
    "f24_distressed_alpha_liabilitiesc_mom_z_504d_v163_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_504d_v163_signal},
    "f24_distressed_alpha_recovery_score_mom_z_504d_v164_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_504d_v164_signal},
    "f24_distressed_alpha_netinc_mom_z_756d_v165_signal": {"func": f24_distressed_alpha_netinc_mom_z_756d_v165_signal},
    "f24_distressed_alpha_assets_mom_z_756d_v166_signal": {"func": f24_distressed_alpha_assets_mom_z_756d_v166_signal},
    "f24_distressed_alpha_liabilitiesc_mom_z_756d_v167_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_756d_v167_signal},
    "f24_distressed_alpha_recovery_score_mom_z_756d_v168_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_756d_v168_signal},
    "f24_distressed_alpha_netinc_mom_z_1008d_v169_signal": {"func": f24_distressed_alpha_netinc_mom_z_1008d_v169_signal},
    "f24_distressed_alpha_assets_mom_z_1008d_v170_signal": {"func": f24_distressed_alpha_assets_mom_z_1008d_v170_signal},
    "f24_distressed_alpha_liabilitiesc_mom_z_1008d_v171_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_1008d_v171_signal},
    "f24_distressed_alpha_recovery_score_mom_z_1008d_v172_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_1008d_v172_signal},
    "f24_distressed_alpha_netinc_mom_z_1260d_v173_signal": {"func": f24_distressed_alpha_netinc_mom_z_1260d_v173_signal},
    "f24_distressed_alpha_assets_mom_z_1260d_v174_signal": {"func": f24_distressed_alpha_assets_mom_z_1260d_v174_signal},
    "f24_distressed_alpha_liabilitiesc_mom_z_1260d_v175_signal": {"func": f24_distressed_alpha_liabilitiesc_mom_z_1260d_v175_signal},
    "f24_distressed_alpha_recovery_score_mom_z_1260d_v176_signal": {"func": f24_distressed_alpha_recovery_score_mom_z_1260d_v176_signal},
    "f24_distressed_alpha_netinc_vol_slope_5d_v177_signal": {"func": f24_distressed_alpha_netinc_vol_slope_5d_v177_signal},
    "f24_distressed_alpha_assets_vol_slope_5d_v178_signal": {"func": f24_distressed_alpha_assets_vol_slope_5d_v178_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_5d_v179_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_5d_v179_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_5d_v180_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_5d_v180_signal},
    "f24_distressed_alpha_netinc_vol_slope_10d_v181_signal": {"func": f24_distressed_alpha_netinc_vol_slope_10d_v181_signal},
    "f24_distressed_alpha_assets_vol_slope_10d_v182_signal": {"func": f24_distressed_alpha_assets_vol_slope_10d_v182_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_10d_v183_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_10d_v183_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_10d_v184_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_10d_v184_signal},
    "f24_distressed_alpha_netinc_vol_slope_21d_v185_signal": {"func": f24_distressed_alpha_netinc_vol_slope_21d_v185_signal},
    "f24_distressed_alpha_assets_vol_slope_21d_v186_signal": {"func": f24_distressed_alpha_assets_vol_slope_21d_v186_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_21d_v187_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_21d_v187_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_21d_v188_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_21d_v188_signal},
    "f24_distressed_alpha_netinc_vol_slope_42d_v189_signal": {"func": f24_distressed_alpha_netinc_vol_slope_42d_v189_signal},
    "f24_distressed_alpha_assets_vol_slope_42d_v190_signal": {"func": f24_distressed_alpha_assets_vol_slope_42d_v190_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_42d_v191_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_42d_v191_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_42d_v192_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_42d_v192_signal},
    "f24_distressed_alpha_netinc_vol_slope_63d_v193_signal": {"func": f24_distressed_alpha_netinc_vol_slope_63d_v193_signal},
    "f24_distressed_alpha_assets_vol_slope_63d_v194_signal": {"func": f24_distressed_alpha_assets_vol_slope_63d_v194_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_63d_v195_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_63d_v195_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_63d_v196_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_63d_v196_signal},
    "f24_distressed_alpha_netinc_vol_slope_126d_v197_signal": {"func": f24_distressed_alpha_netinc_vol_slope_126d_v197_signal},
    "f24_distressed_alpha_assets_vol_slope_126d_v198_signal": {"func": f24_distressed_alpha_assets_vol_slope_126d_v198_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_126d_v199_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_126d_v199_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_126d_v200_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_126d_v200_signal},
    "f24_distressed_alpha_netinc_vol_slope_252d_v201_signal": {"func": f24_distressed_alpha_netinc_vol_slope_252d_v201_signal},
    "f24_distressed_alpha_assets_vol_slope_252d_v202_signal": {"func": f24_distressed_alpha_assets_vol_slope_252d_v202_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_252d_v203_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_252d_v203_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_252d_v204_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_252d_v204_signal},
    "f24_distressed_alpha_netinc_vol_slope_504d_v205_signal": {"func": f24_distressed_alpha_netinc_vol_slope_504d_v205_signal},
    "f24_distressed_alpha_assets_vol_slope_504d_v206_signal": {"func": f24_distressed_alpha_assets_vol_slope_504d_v206_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_504d_v207_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_504d_v207_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_504d_v208_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_504d_v208_signal},
    "f24_distressed_alpha_netinc_vol_slope_756d_v209_signal": {"func": f24_distressed_alpha_netinc_vol_slope_756d_v209_signal},
    "f24_distressed_alpha_assets_vol_slope_756d_v210_signal": {"func": f24_distressed_alpha_assets_vol_slope_756d_v210_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_756d_v211_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_756d_v211_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_756d_v212_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_756d_v212_signal},
    "f24_distressed_alpha_netinc_vol_slope_1008d_v213_signal": {"func": f24_distressed_alpha_netinc_vol_slope_1008d_v213_signal},
    "f24_distressed_alpha_assets_vol_slope_1008d_v214_signal": {"func": f24_distressed_alpha_assets_vol_slope_1008d_v214_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_1008d_v215_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_1008d_v215_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_1008d_v216_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_1008d_v216_signal},
    "f24_distressed_alpha_netinc_vol_slope_1260d_v217_signal": {"func": f24_distressed_alpha_netinc_vol_slope_1260d_v217_signal},
    "f24_distressed_alpha_assets_vol_slope_1260d_v218_signal": {"func": f24_distressed_alpha_assets_vol_slope_1260d_v218_signal},
    "f24_distressed_alpha_liabilitiesc_vol_slope_1260d_v219_signal": {"func": f24_distressed_alpha_liabilitiesc_vol_slope_1260d_v219_signal},
    "f24_distressed_alpha_recovery_score_vol_slope_1260d_v220_signal": {"func": f24_distressed_alpha_recovery_score_vol_slope_1260d_v220_signal},
    "f24_distressed_alpha_netinc_ewma_slope_5d_v221_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_5d_v221_signal},
    "f24_distressed_alpha_assets_ewma_slope_5d_v222_signal": {"func": f24_distressed_alpha_assets_ewma_slope_5d_v222_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_5d_v223_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_5d_v223_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_5d_v224_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_5d_v224_signal},
    "f24_distressed_alpha_netinc_ewma_slope_10d_v225_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_10d_v225_signal},
    "f24_distressed_alpha_assets_ewma_slope_10d_v226_signal": {"func": f24_distressed_alpha_assets_ewma_slope_10d_v226_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_10d_v227_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_10d_v227_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_10d_v228_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_10d_v228_signal},
    "f24_distressed_alpha_netinc_ewma_slope_21d_v229_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_21d_v229_signal},
    "f24_distressed_alpha_assets_ewma_slope_21d_v230_signal": {"func": f24_distressed_alpha_assets_ewma_slope_21d_v230_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_21d_v231_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_21d_v231_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_21d_v232_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_21d_v232_signal},
    "f24_distressed_alpha_netinc_ewma_slope_42d_v233_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_42d_v233_signal},
    "f24_distressed_alpha_assets_ewma_slope_42d_v234_signal": {"func": f24_distressed_alpha_assets_ewma_slope_42d_v234_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_42d_v235_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_42d_v235_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_42d_v236_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_42d_v236_signal},
    "f24_distressed_alpha_netinc_ewma_slope_63d_v237_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_63d_v237_signal},
    "f24_distressed_alpha_assets_ewma_slope_63d_v238_signal": {"func": f24_distressed_alpha_assets_ewma_slope_63d_v238_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_63d_v239_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_63d_v239_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_63d_v240_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_63d_v240_signal},
    "f24_distressed_alpha_netinc_ewma_slope_126d_v241_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_126d_v241_signal},
    "f24_distressed_alpha_assets_ewma_slope_126d_v242_signal": {"func": f24_distressed_alpha_assets_ewma_slope_126d_v242_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_126d_v243_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_126d_v243_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_126d_v244_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_126d_v244_signal},
    "f24_distressed_alpha_netinc_ewma_slope_252d_v245_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_252d_v245_signal},
    "f24_distressed_alpha_assets_ewma_slope_252d_v246_signal": {"func": f24_distressed_alpha_assets_ewma_slope_252d_v246_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_252d_v247_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_252d_v247_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_252d_v248_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_252d_v248_signal},
    "f24_distressed_alpha_netinc_ewma_slope_504d_v249_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_504d_v249_signal},
    "f24_distressed_alpha_assets_ewma_slope_504d_v250_signal": {"func": f24_distressed_alpha_assets_ewma_slope_504d_v250_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_504d_v251_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_504d_v251_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_504d_v252_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_504d_v252_signal},
    "f24_distressed_alpha_netinc_ewma_slope_756d_v253_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_756d_v253_signal},
    "f24_distressed_alpha_assets_ewma_slope_756d_v254_signal": {"func": f24_distressed_alpha_assets_ewma_slope_756d_v254_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_756d_v255_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_756d_v255_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_756d_v256_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_756d_v256_signal},
    "f24_distressed_alpha_netinc_ewma_slope_1008d_v257_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_1008d_v257_signal},
    "f24_distressed_alpha_assets_ewma_slope_1008d_v258_signal": {"func": f24_distressed_alpha_assets_ewma_slope_1008d_v258_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_1008d_v259_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_1008d_v259_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_1008d_v260_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_1008d_v260_signal},
    "f24_distressed_alpha_netinc_ewma_slope_1260d_v261_signal": {"func": f24_distressed_alpha_netinc_ewma_slope_1260d_v261_signal},
    "f24_distressed_alpha_assets_ewma_slope_1260d_v262_signal": {"func": f24_distressed_alpha_assets_ewma_slope_1260d_v262_signal},
    "f24_distressed_alpha_liabilitiesc_ewma_slope_1260d_v263_signal": {"func": f24_distressed_alpha_liabilitiesc_ewma_slope_1260d_v263_signal},
    "f24_distressed_alpha_recovery_score_ewma_slope_1260d_v264_signal": {"func": f24_distressed_alpha_recovery_score_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 24...")
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
