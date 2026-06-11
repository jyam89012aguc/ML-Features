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

def f05_deposit_funding_deposits_slope_diff_norm_42d_v151_signal(deposits):
    """Normalized slope change for Raw level of deposits over 42d window."""
    res = (_slope_pct(deposits, 42).diff(42) / _sma(deposits.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_42d_v152_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_42d_v153_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 42d window."""
    res = (_slope_pct(liabilitiesc, 42).diff(42) / _sma(liabilitiesc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_42d_v154_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 42d window."""
    res = (_slope_pct(_ratio(deposits, assets), 42).diff(42) / _sma(_ratio(deposits, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_42d_v155_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 42d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 42).diff(42) / _sma(_ratio(deposits, liabilitiesc).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_42d_v156_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 42d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 42).diff(42) / _sma(_ratio(deposits, assets - equity).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_63d_v157_signal(deposits):
    """Normalized slope change for Raw level of deposits over 63d window."""
    res = (_slope_pct(deposits, 63).diff(63) / _sma(deposits.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_63d_v158_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_63d_v159_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 63d window."""
    res = (_slope_pct(liabilitiesc, 63).diff(63) / _sma(liabilitiesc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_63d_v160_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 63d window."""
    res = (_slope_pct(_ratio(deposits, assets), 63).diff(63) / _sma(_ratio(deposits, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_63d_v161_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 63d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 63).diff(63) / _sma(_ratio(deposits, liabilitiesc).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_63d_v162_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 63d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 63).diff(63) / _sma(_ratio(deposits, assets - equity).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_126d_v163_signal(deposits):
    """Normalized slope change for Raw level of deposits over 126d window."""
    res = (_slope_pct(deposits, 126).diff(126) / _sma(deposits.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_126d_v164_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_126d_v165_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 126d window."""
    res = (_slope_pct(liabilitiesc, 126).diff(126) / _sma(liabilitiesc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_126d_v166_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 126d window."""
    res = (_slope_pct(_ratio(deposits, assets), 126).diff(126) / _sma(_ratio(deposits, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_126d_v167_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 126d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 126).diff(126) / _sma(_ratio(deposits, liabilitiesc).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_126d_v168_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 126d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 126).diff(126) / _sma(_ratio(deposits, assets - equity).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_252d_v169_signal(deposits):
    """Normalized slope change for Raw level of deposits over 252d window."""
    res = (_slope_pct(deposits, 252).diff(252) / _sma(deposits.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_252d_v170_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_252d_v171_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 252d window."""
    res = (_slope_pct(liabilitiesc, 252).diff(252) / _sma(liabilitiesc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_252d_v172_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 252d window."""
    res = (_slope_pct(_ratio(deposits, assets), 252).diff(252) / _sma(_ratio(deposits, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_252d_v173_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 252d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 252).diff(252) / _sma(_ratio(deposits, liabilitiesc).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_252d_v174_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 252d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 252).diff(252) / _sma(_ratio(deposits, assets - equity).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_504d_v175_signal(deposits):
    """Normalized slope change for Raw level of deposits over 504d window."""
    res = (_slope_pct(deposits, 504).diff(504) / _sma(deposits.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_504d_v176_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_504d_v177_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 504d window."""
    res = (_slope_pct(liabilitiesc, 504).diff(504) / _sma(liabilitiesc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_504d_v178_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 504d window."""
    res = (_slope_pct(_ratio(deposits, assets), 504).diff(504) / _sma(_ratio(deposits, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_504d_v179_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 504d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 504).diff(504) / _sma(_ratio(deposits, liabilitiesc).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_504d_v180_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 504d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 504).diff(504) / _sma(_ratio(deposits, assets - equity).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_756d_v181_signal(deposits):
    """Normalized slope change for Raw level of deposits over 756d window."""
    res = (_slope_pct(deposits, 756).diff(756) / _sma(deposits.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_756d_v182_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_756d_v183_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 756d window."""
    res = (_slope_pct(liabilitiesc, 756).diff(756) / _sma(liabilitiesc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_756d_v184_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 756d window."""
    res = (_slope_pct(_ratio(deposits, assets), 756).diff(756) / _sma(_ratio(deposits, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_756d_v185_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 756d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 756).diff(756) / _sma(_ratio(deposits, liabilitiesc).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_756d_v186_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 756d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 756).diff(756) / _sma(_ratio(deposits, assets - equity).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_1008d_v187_signal(deposits):
    """Normalized slope change for Raw level of deposits over 1008d window."""
    res = (_slope_pct(deposits, 1008).diff(1008) / _sma(deposits.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_1008d_v188_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_1008d_v189_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 1008d window."""
    res = (_slope_pct(liabilitiesc, 1008).diff(1008) / _sma(liabilitiesc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_1008d_v190_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 1008d window."""
    res = (_slope_pct(_ratio(deposits, assets), 1008).diff(1008) / _sma(_ratio(deposits, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_1008d_v191_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 1008d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 1008).diff(1008) / _sma(_ratio(deposits, liabilitiesc).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_1008d_v192_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 1008d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 1008).diff(1008) / _sma(_ratio(deposits, assets - equity).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_1260d_v193_signal(deposits):
    """Normalized slope change for Raw level of deposits over 1260d window."""
    res = (_slope_pct(deposits, 1260).diff(1260) / _sma(deposits.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_1260d_v194_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_1260d_v195_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 1260d window."""
    res = (_slope_pct(liabilitiesc, 1260).diff(1260) / _sma(liabilitiesc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_1260d_v196_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 1260d window."""
    res = (_slope_pct(_ratio(deposits, assets), 1260).diff(1260) / _sma(_ratio(deposits, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_1260d_v197_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 1260d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 1260).diff(1260) / _sma(_ratio(deposits, liabilitiesc).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_1260d_v198_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 1260d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 1260).diff(1260) / _sma(_ratio(deposits, assets - equity).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_5d_v199_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 5d window."""
    res = _z(_slope_pct(deposits, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_5d_v200_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_5d_v201_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 5d window."""
    res = _z(_slope_pct(liabilitiesc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_5d_v202_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 5d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_5d_v203_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 5d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_5d_v204_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 5d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_10d_v205_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 10d window."""
    res = _z(_slope_pct(deposits, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_10d_v206_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_10d_v207_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 10d window."""
    res = _z(_slope_pct(liabilitiesc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_10d_v208_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 10d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_10d_v209_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 10d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_10d_v210_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 10d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_21d_v211_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 21d window."""
    res = _z(_slope_pct(deposits, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_21d_v212_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_21d_v213_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 21d window."""
    res = _z(_slope_pct(liabilitiesc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_21d_v214_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 21d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_21d_v215_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 21d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_21d_v216_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 21d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_42d_v217_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 42d window."""
    res = _z(_slope_pct(deposits, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_42d_v218_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_42d_v219_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 42d window."""
    res = _z(_slope_pct(liabilitiesc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_42d_v220_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 42d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_42d_v221_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 42d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_42d_v222_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 42d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_63d_v223_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 63d window."""
    res = _z(_slope_pct(deposits, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_63d_v224_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_63d_v225_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 63d window."""
    res = _z(_slope_pct(liabilitiesc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_63d_v226_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 63d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_63d_v227_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 63d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_63d_v228_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 63d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_126d_v229_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 126d window."""
    res = _z(_slope_pct(deposits, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_126d_v230_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_126d_v231_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 126d window."""
    res = _z(_slope_pct(liabilitiesc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_126d_v232_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 126d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_126d_v233_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 126d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_126d_v234_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 126d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_252d_v235_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 252d window."""
    res = _z(_slope_pct(deposits, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_252d_v236_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_252d_v237_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 252d window."""
    res = _z(_slope_pct(liabilitiesc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_252d_v238_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 252d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_252d_v239_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 252d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_252d_v240_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 252d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_504d_v241_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 504d window."""
    res = _z(_slope_pct(deposits, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_504d_v242_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_504d_v243_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 504d window."""
    res = _z(_slope_pct(liabilitiesc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_504d_v244_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 504d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_504d_v245_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 504d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_504d_v246_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 504d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_756d_v247_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 756d window."""
    res = _z(_slope_pct(deposits, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_756d_v248_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_756d_v249_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 756d window."""
    res = _z(_slope_pct(liabilitiesc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_756d_v250_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 756d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_756d_v251_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 756d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_756d_v252_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 756d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_1008d_v253_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 1008d window."""
    res = _z(_slope_pct(deposits, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_1008d_v254_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_1008d_v255_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 1008d window."""
    res = _z(_slope_pct(liabilitiesc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_1008d_v256_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 1008d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_1008d_v257_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 1008d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_1008d_v258_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 1008d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_mom_z_1260d_v259_signal(deposits):
    """Relative momentum strength for Raw level of deposits over 1260d window."""
    res = _z(_slope_pct(deposits, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_mom_z_1260d_v260_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_mom_z_1260d_v261_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 1260d window."""
    res = _z(_slope_pct(liabilitiesc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_mom_z_1260d_v262_signal(deposits, assets):
    """Relative momentum strength for Deposits as % of assets over 1260d window."""
    res = _z(_slope_pct(_ratio(deposits, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_mom_z_1260d_v263_signal(deposits, liabilitiesc):
    """Relative momentum strength for Stable deposits relative to short-term liabilities over 1260d window."""
    res = _z(_slope_pct(_ratio(deposits, liabilitiesc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_mom_z_1260d_v264_signal(deposits, assets, equity):
    """Relative momentum strength for Deposits relative to total debt funding over 1260d window."""
    res = _z(_slope_pct(_ratio(deposits, assets - equity), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_vol_slope_5d_v265_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 5d window."""
    res = _std(_slope_pct(deposits, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_vol_slope_5d_v266_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_vol_slope_5d_v267_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 5d window."""
    res = _std(_slope_pct(liabilitiesc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_vol_slope_5d_v268_signal(deposits, assets):
    """Volatility of momentum for Deposits as % of assets over 5d window."""
    res = _std(_slope_pct(_ratio(deposits, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_vol_slope_5d_v269_signal(deposits, liabilitiesc):
    """Volatility of momentum for Stable deposits relative to short-term liabilities over 5d window."""
    res = _std(_slope_pct(_ratio(deposits, liabilitiesc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_vol_slope_5d_v270_signal(deposits, assets, equity):
    """Volatility of momentum for Deposits relative to total debt funding over 5d window."""
    res = _std(_slope_pct(_ratio(deposits, assets - equity), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_vol_slope_10d_v271_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 10d window."""
    res = _std(_slope_pct(deposits, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_vol_slope_10d_v272_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_vol_slope_10d_v273_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 10d window."""
    res = _std(_slope_pct(liabilitiesc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_vol_slope_10d_v274_signal(deposits, assets):
    """Volatility of momentum for Deposits as % of assets over 10d window."""
    res = _std(_slope_pct(_ratio(deposits, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_vol_slope_10d_v275_signal(deposits, liabilitiesc):
    """Volatility of momentum for Stable deposits relative to short-term liabilities over 10d window."""
    res = _std(_slope_pct(_ratio(deposits, liabilitiesc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_vol_slope_10d_v276_signal(deposits, assets, equity):
    """Volatility of momentum for Deposits relative to total debt funding over 10d window."""
    res = _std(_slope_pct(_ratio(deposits, assets - equity), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_vol_slope_21d_v277_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 21d window."""
    res = _std(_slope_pct(deposits, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_vol_slope_21d_v278_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_vol_slope_21d_v279_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 21d window."""
    res = _std(_slope_pct(liabilitiesc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_vol_slope_21d_v280_signal(deposits, assets):
    """Volatility of momentum for Deposits as % of assets over 21d window."""
    res = _std(_slope_pct(_ratio(deposits, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_vol_slope_21d_v281_signal(deposits, liabilitiesc):
    """Volatility of momentum for Stable deposits relative to short-term liabilities over 21d window."""
    res = _std(_slope_pct(_ratio(deposits, liabilitiesc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_vol_slope_21d_v282_signal(deposits, assets, equity):
    """Volatility of momentum for Deposits relative to total debt funding over 21d window."""
    res = _std(_slope_pct(_ratio(deposits, assets - equity), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_vol_slope_42d_v283_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 42d window."""
    res = _std(_slope_pct(deposits, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_vol_slope_42d_v284_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_vol_slope_42d_v285_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 42d window."""
    res = _std(_slope_pct(liabilitiesc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_vol_slope_42d_v286_signal(deposits, assets):
    """Volatility of momentum for Deposits as % of assets over 42d window."""
    res = _std(_slope_pct(_ratio(deposits, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_vol_slope_42d_v287_signal(deposits, liabilitiesc):
    """Volatility of momentum for Stable deposits relative to short-term liabilities over 42d window."""
    res = _std(_slope_pct(_ratio(deposits, liabilitiesc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_vol_slope_42d_v288_signal(deposits, assets, equity):
    """Volatility of momentum for Deposits relative to total debt funding over 42d window."""
    res = _std(_slope_pct(_ratio(deposits, assets - equity), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_vol_slope_63d_v289_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 63d window."""
    res = _std(_slope_pct(deposits, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_vol_slope_63d_v290_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_vol_slope_63d_v291_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 63d window."""
    res = _std(_slope_pct(liabilitiesc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_vol_slope_63d_v292_signal(deposits, assets):
    """Volatility of momentum for Deposits as % of assets over 63d window."""
    res = _std(_slope_pct(_ratio(deposits, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_vol_slope_63d_v293_signal(deposits, liabilitiesc):
    """Volatility of momentum for Stable deposits relative to short-term liabilities over 63d window."""
    res = _std(_slope_pct(_ratio(deposits, liabilitiesc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_vol_slope_63d_v294_signal(deposits, assets, equity):
    """Volatility of momentum for Deposits relative to total debt funding over 63d window."""
    res = _std(_slope_pct(_ratio(deposits, assets - equity), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_vol_slope_126d_v295_signal(deposits):
    """Volatility of momentum for Raw level of deposits over 126d window."""
    res = _std(_slope_pct(deposits, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_vol_slope_126d_v296_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_vol_slope_126d_v297_signal(liabilitiesc):
    """Volatility of momentum for Raw level of liabilitiesc over 126d window."""
    res = _std(_slope_pct(liabilitiesc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_vol_slope_126d_v298_signal(deposits, assets):
    """Volatility of momentum for Deposits as % of assets over 126d window."""
    res = _std(_slope_pct(_ratio(deposits, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_vol_slope_126d_v299_signal(deposits, liabilitiesc):
    """Volatility of momentum for Stable deposits relative to short-term liabilities over 126d window."""
    res = _std(_slope_pct(_ratio(deposits, liabilitiesc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_vol_slope_126d_v300_signal(deposits, assets, equity):
    """Volatility of momentum for Deposits relative to total debt funding over 126d window."""
    res = _std(_slope_pct(_ratio(deposits, assets - equity), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f05_deposit_funding_deposits_slope_diff_norm_42d_v151_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_42d_v151_signal},
    "f05_deposit_funding_assets_slope_diff_norm_42d_v152_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_42d_v152_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_42d_v153_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_42d_v153_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_42d_v154_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_42d_v154_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_42d_v155_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_42d_v155_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_42d_v156_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_42d_v156_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_63d_v157_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_63d_v157_signal},
    "f05_deposit_funding_assets_slope_diff_norm_63d_v158_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_63d_v158_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_63d_v159_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_63d_v159_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_63d_v160_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_63d_v160_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_63d_v161_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_63d_v161_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_63d_v162_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_63d_v162_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_126d_v163_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_126d_v163_signal},
    "f05_deposit_funding_assets_slope_diff_norm_126d_v164_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_126d_v164_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_126d_v165_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_126d_v165_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_126d_v166_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_126d_v166_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_126d_v167_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_126d_v167_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_126d_v168_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_126d_v168_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_252d_v169_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_252d_v169_signal},
    "f05_deposit_funding_assets_slope_diff_norm_252d_v170_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_252d_v170_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_252d_v171_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_252d_v171_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_252d_v172_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_252d_v172_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_252d_v173_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_252d_v173_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_252d_v174_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_252d_v174_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_504d_v175_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_504d_v175_signal},
    "f05_deposit_funding_assets_slope_diff_norm_504d_v176_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_504d_v176_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_504d_v177_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_504d_v177_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_504d_v178_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_504d_v178_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_504d_v179_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_504d_v179_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_504d_v180_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_504d_v180_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_756d_v181_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_756d_v181_signal},
    "f05_deposit_funding_assets_slope_diff_norm_756d_v182_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_756d_v182_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_756d_v183_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_756d_v183_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_756d_v184_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_756d_v184_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_756d_v185_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_756d_v185_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_756d_v186_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_756d_v186_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_1008d_v187_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_1008d_v187_signal},
    "f05_deposit_funding_assets_slope_diff_norm_1008d_v188_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_1008d_v188_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_1008d_v189_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_1008d_v189_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_1008d_v190_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_1008d_v190_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_1008d_v191_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_1008d_v191_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_1008d_v192_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_1008d_v192_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_1260d_v193_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_1260d_v193_signal},
    "f05_deposit_funding_assets_slope_diff_norm_1260d_v194_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_1260d_v194_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_1260d_v195_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_1260d_v195_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_1260d_v196_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_1260d_v196_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_1260d_v197_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_1260d_v197_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_1260d_v198_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_1260d_v198_signal},
    "f05_deposit_funding_deposits_mom_z_5d_v199_signal": {"func": f05_deposit_funding_deposits_mom_z_5d_v199_signal},
    "f05_deposit_funding_assets_mom_z_5d_v200_signal": {"func": f05_deposit_funding_assets_mom_z_5d_v200_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_5d_v201_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_5d_v201_signal},
    "f05_deposit_funding_deposit_density_mom_z_5d_v202_signal": {"func": f05_deposit_funding_deposit_density_mom_z_5d_v202_signal},
    "f05_deposit_funding_funding_quality_mom_z_5d_v203_signal": {"func": f05_deposit_funding_funding_quality_mom_z_5d_v203_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_5d_v204_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_5d_v204_signal},
    "f05_deposit_funding_deposits_mom_z_10d_v205_signal": {"func": f05_deposit_funding_deposits_mom_z_10d_v205_signal},
    "f05_deposit_funding_assets_mom_z_10d_v206_signal": {"func": f05_deposit_funding_assets_mom_z_10d_v206_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_10d_v207_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_10d_v207_signal},
    "f05_deposit_funding_deposit_density_mom_z_10d_v208_signal": {"func": f05_deposit_funding_deposit_density_mom_z_10d_v208_signal},
    "f05_deposit_funding_funding_quality_mom_z_10d_v209_signal": {"func": f05_deposit_funding_funding_quality_mom_z_10d_v209_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_10d_v210_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_10d_v210_signal},
    "f05_deposit_funding_deposits_mom_z_21d_v211_signal": {"func": f05_deposit_funding_deposits_mom_z_21d_v211_signal},
    "f05_deposit_funding_assets_mom_z_21d_v212_signal": {"func": f05_deposit_funding_assets_mom_z_21d_v212_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_21d_v213_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_21d_v213_signal},
    "f05_deposit_funding_deposit_density_mom_z_21d_v214_signal": {"func": f05_deposit_funding_deposit_density_mom_z_21d_v214_signal},
    "f05_deposit_funding_funding_quality_mom_z_21d_v215_signal": {"func": f05_deposit_funding_funding_quality_mom_z_21d_v215_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_21d_v216_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_21d_v216_signal},
    "f05_deposit_funding_deposits_mom_z_42d_v217_signal": {"func": f05_deposit_funding_deposits_mom_z_42d_v217_signal},
    "f05_deposit_funding_assets_mom_z_42d_v218_signal": {"func": f05_deposit_funding_assets_mom_z_42d_v218_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_42d_v219_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_42d_v219_signal},
    "f05_deposit_funding_deposit_density_mom_z_42d_v220_signal": {"func": f05_deposit_funding_deposit_density_mom_z_42d_v220_signal},
    "f05_deposit_funding_funding_quality_mom_z_42d_v221_signal": {"func": f05_deposit_funding_funding_quality_mom_z_42d_v221_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_42d_v222_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_42d_v222_signal},
    "f05_deposit_funding_deposits_mom_z_63d_v223_signal": {"func": f05_deposit_funding_deposits_mom_z_63d_v223_signal},
    "f05_deposit_funding_assets_mom_z_63d_v224_signal": {"func": f05_deposit_funding_assets_mom_z_63d_v224_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_63d_v225_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_63d_v225_signal},
    "f05_deposit_funding_deposit_density_mom_z_63d_v226_signal": {"func": f05_deposit_funding_deposit_density_mom_z_63d_v226_signal},
    "f05_deposit_funding_funding_quality_mom_z_63d_v227_signal": {"func": f05_deposit_funding_funding_quality_mom_z_63d_v227_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_63d_v228_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_63d_v228_signal},
    "f05_deposit_funding_deposits_mom_z_126d_v229_signal": {"func": f05_deposit_funding_deposits_mom_z_126d_v229_signal},
    "f05_deposit_funding_assets_mom_z_126d_v230_signal": {"func": f05_deposit_funding_assets_mom_z_126d_v230_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_126d_v231_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_126d_v231_signal},
    "f05_deposit_funding_deposit_density_mom_z_126d_v232_signal": {"func": f05_deposit_funding_deposit_density_mom_z_126d_v232_signal},
    "f05_deposit_funding_funding_quality_mom_z_126d_v233_signal": {"func": f05_deposit_funding_funding_quality_mom_z_126d_v233_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_126d_v234_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_126d_v234_signal},
    "f05_deposit_funding_deposits_mom_z_252d_v235_signal": {"func": f05_deposit_funding_deposits_mom_z_252d_v235_signal},
    "f05_deposit_funding_assets_mom_z_252d_v236_signal": {"func": f05_deposit_funding_assets_mom_z_252d_v236_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_252d_v237_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_252d_v237_signal},
    "f05_deposit_funding_deposit_density_mom_z_252d_v238_signal": {"func": f05_deposit_funding_deposit_density_mom_z_252d_v238_signal},
    "f05_deposit_funding_funding_quality_mom_z_252d_v239_signal": {"func": f05_deposit_funding_funding_quality_mom_z_252d_v239_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_252d_v240_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_252d_v240_signal},
    "f05_deposit_funding_deposits_mom_z_504d_v241_signal": {"func": f05_deposit_funding_deposits_mom_z_504d_v241_signal},
    "f05_deposit_funding_assets_mom_z_504d_v242_signal": {"func": f05_deposit_funding_assets_mom_z_504d_v242_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_504d_v243_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_504d_v243_signal},
    "f05_deposit_funding_deposit_density_mom_z_504d_v244_signal": {"func": f05_deposit_funding_deposit_density_mom_z_504d_v244_signal},
    "f05_deposit_funding_funding_quality_mom_z_504d_v245_signal": {"func": f05_deposit_funding_funding_quality_mom_z_504d_v245_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_504d_v246_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_504d_v246_signal},
    "f05_deposit_funding_deposits_mom_z_756d_v247_signal": {"func": f05_deposit_funding_deposits_mom_z_756d_v247_signal},
    "f05_deposit_funding_assets_mom_z_756d_v248_signal": {"func": f05_deposit_funding_assets_mom_z_756d_v248_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_756d_v249_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_756d_v249_signal},
    "f05_deposit_funding_deposit_density_mom_z_756d_v250_signal": {"func": f05_deposit_funding_deposit_density_mom_z_756d_v250_signal},
    "f05_deposit_funding_funding_quality_mom_z_756d_v251_signal": {"func": f05_deposit_funding_funding_quality_mom_z_756d_v251_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_756d_v252_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_756d_v252_signal},
    "f05_deposit_funding_deposits_mom_z_1008d_v253_signal": {"func": f05_deposit_funding_deposits_mom_z_1008d_v253_signal},
    "f05_deposit_funding_assets_mom_z_1008d_v254_signal": {"func": f05_deposit_funding_assets_mom_z_1008d_v254_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_1008d_v255_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_1008d_v255_signal},
    "f05_deposit_funding_deposit_density_mom_z_1008d_v256_signal": {"func": f05_deposit_funding_deposit_density_mom_z_1008d_v256_signal},
    "f05_deposit_funding_funding_quality_mom_z_1008d_v257_signal": {"func": f05_deposit_funding_funding_quality_mom_z_1008d_v257_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_1008d_v258_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_1008d_v258_signal},
    "f05_deposit_funding_deposits_mom_z_1260d_v259_signal": {"func": f05_deposit_funding_deposits_mom_z_1260d_v259_signal},
    "f05_deposit_funding_assets_mom_z_1260d_v260_signal": {"func": f05_deposit_funding_assets_mom_z_1260d_v260_signal},
    "f05_deposit_funding_liabilitiesc_mom_z_1260d_v261_signal": {"func": f05_deposit_funding_liabilitiesc_mom_z_1260d_v261_signal},
    "f05_deposit_funding_deposit_density_mom_z_1260d_v262_signal": {"func": f05_deposit_funding_deposit_density_mom_z_1260d_v262_signal},
    "f05_deposit_funding_funding_quality_mom_z_1260d_v263_signal": {"func": f05_deposit_funding_funding_quality_mom_z_1260d_v263_signal},
    "f05_deposit_funding_asset_funding_mix_mom_z_1260d_v264_signal": {"func": f05_deposit_funding_asset_funding_mix_mom_z_1260d_v264_signal},
    "f05_deposit_funding_deposits_vol_slope_5d_v265_signal": {"func": f05_deposit_funding_deposits_vol_slope_5d_v265_signal},
    "f05_deposit_funding_assets_vol_slope_5d_v266_signal": {"func": f05_deposit_funding_assets_vol_slope_5d_v266_signal},
    "f05_deposit_funding_liabilitiesc_vol_slope_5d_v267_signal": {"func": f05_deposit_funding_liabilitiesc_vol_slope_5d_v267_signal},
    "f05_deposit_funding_deposit_density_vol_slope_5d_v268_signal": {"func": f05_deposit_funding_deposit_density_vol_slope_5d_v268_signal},
    "f05_deposit_funding_funding_quality_vol_slope_5d_v269_signal": {"func": f05_deposit_funding_funding_quality_vol_slope_5d_v269_signal},
    "f05_deposit_funding_asset_funding_mix_vol_slope_5d_v270_signal": {"func": f05_deposit_funding_asset_funding_mix_vol_slope_5d_v270_signal},
    "f05_deposit_funding_deposits_vol_slope_10d_v271_signal": {"func": f05_deposit_funding_deposits_vol_slope_10d_v271_signal},
    "f05_deposit_funding_assets_vol_slope_10d_v272_signal": {"func": f05_deposit_funding_assets_vol_slope_10d_v272_signal},
    "f05_deposit_funding_liabilitiesc_vol_slope_10d_v273_signal": {"func": f05_deposit_funding_liabilitiesc_vol_slope_10d_v273_signal},
    "f05_deposit_funding_deposit_density_vol_slope_10d_v274_signal": {"func": f05_deposit_funding_deposit_density_vol_slope_10d_v274_signal},
    "f05_deposit_funding_funding_quality_vol_slope_10d_v275_signal": {"func": f05_deposit_funding_funding_quality_vol_slope_10d_v275_signal},
    "f05_deposit_funding_asset_funding_mix_vol_slope_10d_v276_signal": {"func": f05_deposit_funding_asset_funding_mix_vol_slope_10d_v276_signal},
    "f05_deposit_funding_deposits_vol_slope_21d_v277_signal": {"func": f05_deposit_funding_deposits_vol_slope_21d_v277_signal},
    "f05_deposit_funding_assets_vol_slope_21d_v278_signal": {"func": f05_deposit_funding_assets_vol_slope_21d_v278_signal},
    "f05_deposit_funding_liabilitiesc_vol_slope_21d_v279_signal": {"func": f05_deposit_funding_liabilitiesc_vol_slope_21d_v279_signal},
    "f05_deposit_funding_deposit_density_vol_slope_21d_v280_signal": {"func": f05_deposit_funding_deposit_density_vol_slope_21d_v280_signal},
    "f05_deposit_funding_funding_quality_vol_slope_21d_v281_signal": {"func": f05_deposit_funding_funding_quality_vol_slope_21d_v281_signal},
    "f05_deposit_funding_asset_funding_mix_vol_slope_21d_v282_signal": {"func": f05_deposit_funding_asset_funding_mix_vol_slope_21d_v282_signal},
    "f05_deposit_funding_deposits_vol_slope_42d_v283_signal": {"func": f05_deposit_funding_deposits_vol_slope_42d_v283_signal},
    "f05_deposit_funding_assets_vol_slope_42d_v284_signal": {"func": f05_deposit_funding_assets_vol_slope_42d_v284_signal},
    "f05_deposit_funding_liabilitiesc_vol_slope_42d_v285_signal": {"func": f05_deposit_funding_liabilitiesc_vol_slope_42d_v285_signal},
    "f05_deposit_funding_deposit_density_vol_slope_42d_v286_signal": {"func": f05_deposit_funding_deposit_density_vol_slope_42d_v286_signal},
    "f05_deposit_funding_funding_quality_vol_slope_42d_v287_signal": {"func": f05_deposit_funding_funding_quality_vol_slope_42d_v287_signal},
    "f05_deposit_funding_asset_funding_mix_vol_slope_42d_v288_signal": {"func": f05_deposit_funding_asset_funding_mix_vol_slope_42d_v288_signal},
    "f05_deposit_funding_deposits_vol_slope_63d_v289_signal": {"func": f05_deposit_funding_deposits_vol_slope_63d_v289_signal},
    "f05_deposit_funding_assets_vol_slope_63d_v290_signal": {"func": f05_deposit_funding_assets_vol_slope_63d_v290_signal},
    "f05_deposit_funding_liabilitiesc_vol_slope_63d_v291_signal": {"func": f05_deposit_funding_liabilitiesc_vol_slope_63d_v291_signal},
    "f05_deposit_funding_deposit_density_vol_slope_63d_v292_signal": {"func": f05_deposit_funding_deposit_density_vol_slope_63d_v292_signal},
    "f05_deposit_funding_funding_quality_vol_slope_63d_v293_signal": {"func": f05_deposit_funding_funding_quality_vol_slope_63d_v293_signal},
    "f05_deposit_funding_asset_funding_mix_vol_slope_63d_v294_signal": {"func": f05_deposit_funding_asset_funding_mix_vol_slope_63d_v294_signal},
    "f05_deposit_funding_deposits_vol_slope_126d_v295_signal": {"func": f05_deposit_funding_deposits_vol_slope_126d_v295_signal},
    "f05_deposit_funding_assets_vol_slope_126d_v296_signal": {"func": f05_deposit_funding_assets_vol_slope_126d_v296_signal},
    "f05_deposit_funding_liabilitiesc_vol_slope_126d_v297_signal": {"func": f05_deposit_funding_liabilitiesc_vol_slope_126d_v297_signal},
    "f05_deposit_funding_deposit_density_vol_slope_126d_v298_signal": {"func": f05_deposit_funding_deposit_density_vol_slope_126d_v298_signal},
    "f05_deposit_funding_funding_quality_vol_slope_126d_v299_signal": {"func": f05_deposit_funding_funding_quality_vol_slope_126d_v299_signal},
    "f05_deposit_funding_asset_funding_mix_vol_slope_126d_v300_signal": {"func": f05_deposit_funding_asset_funding_mix_vol_slope_126d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 05...")
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
