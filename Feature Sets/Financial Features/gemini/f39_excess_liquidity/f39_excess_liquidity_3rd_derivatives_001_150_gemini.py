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

def f39_excess_liquidity_deposits_mom_z_63d_v151_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 63d window."""
    res = _z(_slope_pct(deposits, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_63d_v152_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 63d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_126d_v153_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 126d window."""
    res = _z(_slope_pct(cashneq, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_126d_v154_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_126d_v155_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 126d window."""
    res = _z(_slope_pct(deposits, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_126d_v156_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 126d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_252d_v157_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 252d window."""
    res = _z(_slope_pct(cashneq, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_252d_v158_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_252d_v159_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 252d window."""
    res = _z(_slope_pct(deposits, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_252d_v160_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 252d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_504d_v161_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 504d window."""
    res = _z(_slope_pct(cashneq, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_504d_v162_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_504d_v163_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 504d window."""
    res = _z(_slope_pct(deposits, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_504d_v164_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 504d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_756d_v165_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 756d window."""
    res = _z(_slope_pct(cashneq, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_756d_v166_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_756d_v167_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 756d window."""
    res = _z(_slope_pct(deposits, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_756d_v168_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 756d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_1008d_v169_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 1008d window."""
    res = _z(_slope_pct(cashneq, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_1008d_v170_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_1008d_v171_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 1008d window."""
    res = _z(_slope_pct(deposits, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_1008d_v172_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 1008d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_mom_z_1260d_v173_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 1260d window."""
    res = _z(_slope_pct(cashneq, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_mom_z_1260d_v174_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_mom_z_1260d_v175_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 1260d window."""
    res = _z(_slope_pct(deposits, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_mom_z_1260d_v176_signal(cashneq, assets):
    """Relative momentum strength for Cash as % of assets over 1260d window."""
    res = _z(_slope_pct(_ratio(cashneq, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_5d_v177_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 5d window."""
    res = _std(_slope_pct(cashneq, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_5d_v178_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_5d_v179_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 5d window."""
    res = _std(_slope_pct(deposits, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_5d_v180_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 5d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_10d_v181_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 10d window."""
    res = _std(_slope_pct(cashneq, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_10d_v182_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_10d_v183_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 10d window."""
    res = _std(_slope_pct(deposits, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_10d_v184_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 10d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_21d_v185_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 21d window."""
    res = _std(_slope_pct(cashneq, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_21d_v186_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_21d_v187_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 21d window."""
    res = _std(_slope_pct(deposits, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_21d_v188_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 21d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_42d_v189_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 42d window."""
    res = _std(_slope_pct(cashneq, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_42d_v190_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_42d_v191_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 42d window."""
    res = _std(_slope_pct(deposits, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_42d_v192_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 42d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_63d_v193_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 63d window."""
    res = _std(_slope_pct(cashneq, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_63d_v194_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_63d_v195_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 63d window."""
    res = _std(_slope_pct(deposits, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_63d_v196_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 63d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_126d_v197_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 126d window."""
    res = _std(_slope_pct(cashneq, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_126d_v198_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_126d_v199_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 126d window."""
    res = _std(_slope_pct(deposits, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_126d_v200_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 126d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_252d_v201_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 252d window."""
    res = _std(_slope_pct(cashneq, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_252d_v202_signal(assets):
    """Volatility of momentum for Raw level of assets over 252d window."""
    res = _std(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_252d_v203_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 252d window."""
    res = _std(_slope_pct(deposits, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_252d_v204_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 252d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_504d_v205_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 504d window."""
    res = _std(_slope_pct(cashneq, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_504d_v206_signal(assets):
    """Volatility of momentum for Raw level of assets over 504d window."""
    res = _std(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_504d_v207_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 504d window."""
    res = _std(_slope_pct(deposits, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_504d_v208_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 504d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_756d_v209_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 756d window."""
    res = _std(_slope_pct(cashneq, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_756d_v210_signal(assets):
    """Volatility of momentum for Raw level of assets over 756d window."""
    res = _std(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_756d_v211_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 756d window."""
    res = _std(_slope_pct(deposits, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_756d_v212_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 756d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_1008d_v213_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 1008d window."""
    res = _std(_slope_pct(cashneq, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_1008d_v214_signal(assets):
    """Volatility of momentum for Raw level of assets over 1008d window."""
    res = _std(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_1008d_v215_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 1008d window."""
    res = _std(_slope_pct(deposits, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_1008d_v216_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 1008d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_vol_slope_1260d_v217_signal(cashneq):
    """Volatility of momentum for Raw level of cashneq over 1260d window."""
    res = _std(_slope_pct(cashneq, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_vol_slope_1260d_v218_signal(assets):
    """Volatility of momentum for Raw level of assets over 1260d window."""
    res = _std(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_vol_slope_1260d_v219_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 1260d window."""
    res = _std(_slope_pct(deposits, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_vol_slope_1260d_v220_signal(cashneq, assets):
    """Volatility of momentum for Cash as % of assets over 1260d window."""
    res = _std(_slope_pct(_ratio(cashneq, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_5d_v221_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 5d window."""
    res = _ewma(_slope_pct(cashneq, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_5d_v222_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 5d window."""
    res = _ewma(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_5d_v223_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 5d window."""
    res = _ewma(_slope_pct(deposits, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_5d_v224_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 5d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_10d_v225_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 10d window."""
    res = _ewma(_slope_pct(cashneq, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_10d_v226_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 10d window."""
    res = _ewma(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_10d_v227_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 10d window."""
    res = _ewma(_slope_pct(deposits, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_10d_v228_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 10d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_21d_v229_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 21d window."""
    res = _ewma(_slope_pct(cashneq, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_21d_v230_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 21d window."""
    res = _ewma(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_21d_v231_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 21d window."""
    res = _ewma(_slope_pct(deposits, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_21d_v232_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 21d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_42d_v233_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 42d window."""
    res = _ewma(_slope_pct(cashneq, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_42d_v234_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 42d window."""
    res = _ewma(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_42d_v235_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 42d window."""
    res = _ewma(_slope_pct(deposits, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_42d_v236_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 42d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_63d_v237_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 63d window."""
    res = _ewma(_slope_pct(cashneq, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_63d_v238_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 63d window."""
    res = _ewma(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_63d_v239_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 63d window."""
    res = _ewma(_slope_pct(deposits, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_63d_v240_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 63d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_126d_v241_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 126d window."""
    res = _ewma(_slope_pct(cashneq, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_126d_v242_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 126d window."""
    res = _ewma(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_126d_v243_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 126d window."""
    res = _ewma(_slope_pct(deposits, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_126d_v244_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 126d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_252d_v245_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 252d window."""
    res = _ewma(_slope_pct(cashneq, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_252d_v246_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 252d window."""
    res = _ewma(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_252d_v247_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 252d window."""
    res = _ewma(_slope_pct(deposits, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_252d_v248_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 252d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_504d_v249_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 504d window."""
    res = _ewma(_slope_pct(cashneq, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_504d_v250_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 504d window."""
    res = _ewma(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_504d_v251_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 504d window."""
    res = _ewma(_slope_pct(deposits, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_504d_v252_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 504d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_756d_v253_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 756d window."""
    res = _ewma(_slope_pct(cashneq, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_756d_v254_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 756d window."""
    res = _ewma(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_756d_v255_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 756d window."""
    res = _ewma(_slope_pct(deposits, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_756d_v256_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 756d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_1008d_v257_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 1008d window."""
    res = _ewma(_slope_pct(cashneq, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_1008d_v258_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 1008d window."""
    res = _ewma(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_1008d_v259_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 1008d window."""
    res = _ewma(_slope_pct(deposits, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_1008d_v260_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 1008d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cashneq_ewma_slope_1260d_v261_signal(cashneq):
    """Exponential momentum smoothing for Raw level of cashneq over 1260d window."""
    res = _ewma(_slope_pct(cashneq, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_assets_ewma_slope_1260d_v262_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 1260d window."""
    res = _ewma(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_deposits_ewma_slope_1260d_v263_signal(deposits):
    """Exponential momentum smoothing for Raw level of deposits over 1260d window."""
    res = _ewma(_slope_pct(deposits, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_excess_liquidity_cash_density_ewma_slope_1260d_v264_signal(cashneq, assets):
    """Exponential momentum smoothing for Cash as % of assets over 1260d window."""
    res = _ewma(_slope_pct(_ratio(cashneq, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f39_excess_liquidity_deposits_mom_z_63d_v151_signal": {"func": f39_excess_liquidity_deposits_mom_z_63d_v151_signal},
    "f39_excess_liquidity_cash_density_mom_z_63d_v152_signal": {"func": f39_excess_liquidity_cash_density_mom_z_63d_v152_signal},
    "f39_excess_liquidity_cashneq_mom_z_126d_v153_signal": {"func": f39_excess_liquidity_cashneq_mom_z_126d_v153_signal},
    "f39_excess_liquidity_assets_mom_z_126d_v154_signal": {"func": f39_excess_liquidity_assets_mom_z_126d_v154_signal},
    "f39_excess_liquidity_deposits_mom_z_126d_v155_signal": {"func": f39_excess_liquidity_deposits_mom_z_126d_v155_signal},
    "f39_excess_liquidity_cash_density_mom_z_126d_v156_signal": {"func": f39_excess_liquidity_cash_density_mom_z_126d_v156_signal},
    "f39_excess_liquidity_cashneq_mom_z_252d_v157_signal": {"func": f39_excess_liquidity_cashneq_mom_z_252d_v157_signal},
    "f39_excess_liquidity_assets_mom_z_252d_v158_signal": {"func": f39_excess_liquidity_assets_mom_z_252d_v158_signal},
    "f39_excess_liquidity_deposits_mom_z_252d_v159_signal": {"func": f39_excess_liquidity_deposits_mom_z_252d_v159_signal},
    "f39_excess_liquidity_cash_density_mom_z_252d_v160_signal": {"func": f39_excess_liquidity_cash_density_mom_z_252d_v160_signal},
    "f39_excess_liquidity_cashneq_mom_z_504d_v161_signal": {"func": f39_excess_liquidity_cashneq_mom_z_504d_v161_signal},
    "f39_excess_liquidity_assets_mom_z_504d_v162_signal": {"func": f39_excess_liquidity_assets_mom_z_504d_v162_signal},
    "f39_excess_liquidity_deposits_mom_z_504d_v163_signal": {"func": f39_excess_liquidity_deposits_mom_z_504d_v163_signal},
    "f39_excess_liquidity_cash_density_mom_z_504d_v164_signal": {"func": f39_excess_liquidity_cash_density_mom_z_504d_v164_signal},
    "f39_excess_liquidity_cashneq_mom_z_756d_v165_signal": {"func": f39_excess_liquidity_cashneq_mom_z_756d_v165_signal},
    "f39_excess_liquidity_assets_mom_z_756d_v166_signal": {"func": f39_excess_liquidity_assets_mom_z_756d_v166_signal},
    "f39_excess_liquidity_deposits_mom_z_756d_v167_signal": {"func": f39_excess_liquidity_deposits_mom_z_756d_v167_signal},
    "f39_excess_liquidity_cash_density_mom_z_756d_v168_signal": {"func": f39_excess_liquidity_cash_density_mom_z_756d_v168_signal},
    "f39_excess_liquidity_cashneq_mom_z_1008d_v169_signal": {"func": f39_excess_liquidity_cashneq_mom_z_1008d_v169_signal},
    "f39_excess_liquidity_assets_mom_z_1008d_v170_signal": {"func": f39_excess_liquidity_assets_mom_z_1008d_v170_signal},
    "f39_excess_liquidity_deposits_mom_z_1008d_v171_signal": {"func": f39_excess_liquidity_deposits_mom_z_1008d_v171_signal},
    "f39_excess_liquidity_cash_density_mom_z_1008d_v172_signal": {"func": f39_excess_liquidity_cash_density_mom_z_1008d_v172_signal},
    "f39_excess_liquidity_cashneq_mom_z_1260d_v173_signal": {"func": f39_excess_liquidity_cashneq_mom_z_1260d_v173_signal},
    "f39_excess_liquidity_assets_mom_z_1260d_v174_signal": {"func": f39_excess_liquidity_assets_mom_z_1260d_v174_signal},
    "f39_excess_liquidity_deposits_mom_z_1260d_v175_signal": {"func": f39_excess_liquidity_deposits_mom_z_1260d_v175_signal},
    "f39_excess_liquidity_cash_density_mom_z_1260d_v176_signal": {"func": f39_excess_liquidity_cash_density_mom_z_1260d_v176_signal},
    "f39_excess_liquidity_cashneq_vol_slope_5d_v177_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_5d_v177_signal},
    "f39_excess_liquidity_assets_vol_slope_5d_v178_signal": {"func": f39_excess_liquidity_assets_vol_slope_5d_v178_signal},
    "f39_excess_liquidity_deposits_vol_slope_5d_v179_signal": {"func": f39_excess_liquidity_deposits_vol_slope_5d_v179_signal},
    "f39_excess_liquidity_cash_density_vol_slope_5d_v180_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_5d_v180_signal},
    "f39_excess_liquidity_cashneq_vol_slope_10d_v181_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_10d_v181_signal},
    "f39_excess_liquidity_assets_vol_slope_10d_v182_signal": {"func": f39_excess_liquidity_assets_vol_slope_10d_v182_signal},
    "f39_excess_liquidity_deposits_vol_slope_10d_v183_signal": {"func": f39_excess_liquidity_deposits_vol_slope_10d_v183_signal},
    "f39_excess_liquidity_cash_density_vol_slope_10d_v184_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_10d_v184_signal},
    "f39_excess_liquidity_cashneq_vol_slope_21d_v185_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_21d_v185_signal},
    "f39_excess_liquidity_assets_vol_slope_21d_v186_signal": {"func": f39_excess_liquidity_assets_vol_slope_21d_v186_signal},
    "f39_excess_liquidity_deposits_vol_slope_21d_v187_signal": {"func": f39_excess_liquidity_deposits_vol_slope_21d_v187_signal},
    "f39_excess_liquidity_cash_density_vol_slope_21d_v188_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_21d_v188_signal},
    "f39_excess_liquidity_cashneq_vol_slope_42d_v189_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_42d_v189_signal},
    "f39_excess_liquidity_assets_vol_slope_42d_v190_signal": {"func": f39_excess_liquidity_assets_vol_slope_42d_v190_signal},
    "f39_excess_liquidity_deposits_vol_slope_42d_v191_signal": {"func": f39_excess_liquidity_deposits_vol_slope_42d_v191_signal},
    "f39_excess_liquidity_cash_density_vol_slope_42d_v192_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_42d_v192_signal},
    "f39_excess_liquidity_cashneq_vol_slope_63d_v193_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_63d_v193_signal},
    "f39_excess_liquidity_assets_vol_slope_63d_v194_signal": {"func": f39_excess_liquidity_assets_vol_slope_63d_v194_signal},
    "f39_excess_liquidity_deposits_vol_slope_63d_v195_signal": {"func": f39_excess_liquidity_deposits_vol_slope_63d_v195_signal},
    "f39_excess_liquidity_cash_density_vol_slope_63d_v196_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_63d_v196_signal},
    "f39_excess_liquidity_cashneq_vol_slope_126d_v197_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_126d_v197_signal},
    "f39_excess_liquidity_assets_vol_slope_126d_v198_signal": {"func": f39_excess_liquidity_assets_vol_slope_126d_v198_signal},
    "f39_excess_liquidity_deposits_vol_slope_126d_v199_signal": {"func": f39_excess_liquidity_deposits_vol_slope_126d_v199_signal},
    "f39_excess_liquidity_cash_density_vol_slope_126d_v200_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_126d_v200_signal},
    "f39_excess_liquidity_cashneq_vol_slope_252d_v201_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_252d_v201_signal},
    "f39_excess_liquidity_assets_vol_slope_252d_v202_signal": {"func": f39_excess_liquidity_assets_vol_slope_252d_v202_signal},
    "f39_excess_liquidity_deposits_vol_slope_252d_v203_signal": {"func": f39_excess_liquidity_deposits_vol_slope_252d_v203_signal},
    "f39_excess_liquidity_cash_density_vol_slope_252d_v204_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_252d_v204_signal},
    "f39_excess_liquidity_cashneq_vol_slope_504d_v205_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_504d_v205_signal},
    "f39_excess_liquidity_assets_vol_slope_504d_v206_signal": {"func": f39_excess_liquidity_assets_vol_slope_504d_v206_signal},
    "f39_excess_liquidity_deposits_vol_slope_504d_v207_signal": {"func": f39_excess_liquidity_deposits_vol_slope_504d_v207_signal},
    "f39_excess_liquidity_cash_density_vol_slope_504d_v208_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_504d_v208_signal},
    "f39_excess_liquidity_cashneq_vol_slope_756d_v209_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_756d_v209_signal},
    "f39_excess_liquidity_assets_vol_slope_756d_v210_signal": {"func": f39_excess_liquidity_assets_vol_slope_756d_v210_signal},
    "f39_excess_liquidity_deposits_vol_slope_756d_v211_signal": {"func": f39_excess_liquidity_deposits_vol_slope_756d_v211_signal},
    "f39_excess_liquidity_cash_density_vol_slope_756d_v212_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_756d_v212_signal},
    "f39_excess_liquidity_cashneq_vol_slope_1008d_v213_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_1008d_v213_signal},
    "f39_excess_liquidity_assets_vol_slope_1008d_v214_signal": {"func": f39_excess_liquidity_assets_vol_slope_1008d_v214_signal},
    "f39_excess_liquidity_deposits_vol_slope_1008d_v215_signal": {"func": f39_excess_liquidity_deposits_vol_slope_1008d_v215_signal},
    "f39_excess_liquidity_cash_density_vol_slope_1008d_v216_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_1008d_v216_signal},
    "f39_excess_liquidity_cashneq_vol_slope_1260d_v217_signal": {"func": f39_excess_liquidity_cashneq_vol_slope_1260d_v217_signal},
    "f39_excess_liquidity_assets_vol_slope_1260d_v218_signal": {"func": f39_excess_liquidity_assets_vol_slope_1260d_v218_signal},
    "f39_excess_liquidity_deposits_vol_slope_1260d_v219_signal": {"func": f39_excess_liquidity_deposits_vol_slope_1260d_v219_signal},
    "f39_excess_liquidity_cash_density_vol_slope_1260d_v220_signal": {"func": f39_excess_liquidity_cash_density_vol_slope_1260d_v220_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_5d_v221_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_5d_v221_signal},
    "f39_excess_liquidity_assets_ewma_slope_5d_v222_signal": {"func": f39_excess_liquidity_assets_ewma_slope_5d_v222_signal},
    "f39_excess_liquidity_deposits_ewma_slope_5d_v223_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_5d_v223_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_5d_v224_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_5d_v224_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_10d_v225_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_10d_v225_signal},
    "f39_excess_liquidity_assets_ewma_slope_10d_v226_signal": {"func": f39_excess_liquidity_assets_ewma_slope_10d_v226_signal},
    "f39_excess_liquidity_deposits_ewma_slope_10d_v227_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_10d_v227_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_10d_v228_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_10d_v228_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_21d_v229_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_21d_v229_signal},
    "f39_excess_liquidity_assets_ewma_slope_21d_v230_signal": {"func": f39_excess_liquidity_assets_ewma_slope_21d_v230_signal},
    "f39_excess_liquidity_deposits_ewma_slope_21d_v231_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_21d_v231_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_21d_v232_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_21d_v232_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_42d_v233_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_42d_v233_signal},
    "f39_excess_liquidity_assets_ewma_slope_42d_v234_signal": {"func": f39_excess_liquidity_assets_ewma_slope_42d_v234_signal},
    "f39_excess_liquidity_deposits_ewma_slope_42d_v235_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_42d_v235_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_42d_v236_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_42d_v236_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_63d_v237_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_63d_v237_signal},
    "f39_excess_liquidity_assets_ewma_slope_63d_v238_signal": {"func": f39_excess_liquidity_assets_ewma_slope_63d_v238_signal},
    "f39_excess_liquidity_deposits_ewma_slope_63d_v239_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_63d_v239_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_63d_v240_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_63d_v240_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_126d_v241_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_126d_v241_signal},
    "f39_excess_liquidity_assets_ewma_slope_126d_v242_signal": {"func": f39_excess_liquidity_assets_ewma_slope_126d_v242_signal},
    "f39_excess_liquidity_deposits_ewma_slope_126d_v243_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_126d_v243_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_126d_v244_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_126d_v244_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_252d_v245_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_252d_v245_signal},
    "f39_excess_liquidity_assets_ewma_slope_252d_v246_signal": {"func": f39_excess_liquidity_assets_ewma_slope_252d_v246_signal},
    "f39_excess_liquidity_deposits_ewma_slope_252d_v247_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_252d_v247_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_252d_v248_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_252d_v248_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_504d_v249_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_504d_v249_signal},
    "f39_excess_liquidity_assets_ewma_slope_504d_v250_signal": {"func": f39_excess_liquidity_assets_ewma_slope_504d_v250_signal},
    "f39_excess_liquidity_deposits_ewma_slope_504d_v251_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_504d_v251_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_504d_v252_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_504d_v252_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_756d_v253_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_756d_v253_signal},
    "f39_excess_liquidity_assets_ewma_slope_756d_v254_signal": {"func": f39_excess_liquidity_assets_ewma_slope_756d_v254_signal},
    "f39_excess_liquidity_deposits_ewma_slope_756d_v255_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_756d_v255_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_756d_v256_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_756d_v256_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_1008d_v257_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_1008d_v257_signal},
    "f39_excess_liquidity_assets_ewma_slope_1008d_v258_signal": {"func": f39_excess_liquidity_assets_ewma_slope_1008d_v258_signal},
    "f39_excess_liquidity_deposits_ewma_slope_1008d_v259_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_1008d_v259_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_1008d_v260_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_1008d_v260_signal},
    "f39_excess_liquidity_cashneq_ewma_slope_1260d_v261_signal": {"func": f39_excess_liquidity_cashneq_ewma_slope_1260d_v261_signal},
    "f39_excess_liquidity_assets_ewma_slope_1260d_v262_signal": {"func": f39_excess_liquidity_assets_ewma_slope_1260d_v262_signal},
    "f39_excess_liquidity_deposits_ewma_slope_1260d_v263_signal": {"func": f39_excess_liquidity_deposits_ewma_slope_1260d_v263_signal},
    "f39_excess_liquidity_cash_density_ewma_slope_1260d_v264_signal": {"func": f39_excess_liquidity_cash_density_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 39...")
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
