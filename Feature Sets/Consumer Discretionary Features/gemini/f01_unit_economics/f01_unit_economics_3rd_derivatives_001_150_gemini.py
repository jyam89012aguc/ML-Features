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

def f01_unit_economics_revenue_slope_diff_norm_756d_v151_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_756d_v152_signal(capex):
    """Normalized slope change for Raw level of capex over 756d window."""
    res = (_slope_pct(capex, 756).diff(756) / _sma(capex.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_756d_v153_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_756d_v154_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 756d window."""
    res = (_slope_pct(_ratio(revenue, capex), 756).diff(756) / _sma(_ratio(revenue, capex).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_756d_v155_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 756d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 756).diff(756) / _sma(_ratio(revenue - capex, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_1008d_v156_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_1008d_v157_signal(capex):
    """Normalized slope change for Raw level of capex over 1008d window."""
    res = (_slope_pct(capex, 1008).diff(1008) / _sma(capex.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_1008d_v158_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_1008d_v159_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 1008d window."""
    res = (_slope_pct(_ratio(revenue, capex), 1008).diff(1008) / _sma(_ratio(revenue, capex).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_1008d_v160_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 1008d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 1008).diff(1008) / _sma(_ratio(revenue - capex, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_1260d_v161_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_1260d_v162_signal(capex):
    """Normalized slope change for Raw level of capex over 1260d window."""
    res = (_slope_pct(capex, 1260).diff(1260) / _sma(capex.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_1260d_v163_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_1260d_v164_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 1260d window."""
    res = (_slope_pct(_ratio(revenue, capex), 1260).diff(1260) / _sma(_ratio(revenue, capex).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_1260d_v165_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 1260d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 1260).diff(1260) / _sma(_ratio(revenue - capex, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_5d_v166_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_5d_v167_signal(capex):
    """Relative momentum strength for Raw level of capex over 5d window."""
    res = _z(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_5d_v168_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_5d_v169_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 5d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_5d_v170_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 5d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_10d_v171_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_10d_v172_signal(capex):
    """Relative momentum strength for Raw level of capex over 10d window."""
    res = _z(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_10d_v173_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_10d_v174_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 10d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_10d_v175_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 10d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_21d_v176_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_21d_v177_signal(capex):
    """Relative momentum strength for Raw level of capex over 21d window."""
    res = _z(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_21d_v178_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_21d_v179_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 21d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_21d_v180_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 21d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_42d_v181_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_42d_v182_signal(capex):
    """Relative momentum strength for Raw level of capex over 42d window."""
    res = _z(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_42d_v183_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_42d_v184_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 42d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_42d_v185_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 42d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_63d_v186_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_63d_v187_signal(capex):
    """Relative momentum strength for Raw level of capex over 63d window."""
    res = _z(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_63d_v188_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_63d_v189_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_63d_v190_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 63d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_126d_v191_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_126d_v192_signal(capex):
    """Relative momentum strength for Raw level of capex over 126d window."""
    res = _z(_slope_pct(capex, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_126d_v193_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_126d_v194_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_126d_v195_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 126d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_252d_v196_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_252d_v197_signal(capex):
    """Relative momentum strength for Raw level of capex over 252d window."""
    res = _z(_slope_pct(capex, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_252d_v198_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_252d_v199_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_252d_v200_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 252d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_504d_v201_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_504d_v202_signal(capex):
    """Relative momentum strength for Raw level of capex over 504d window."""
    res = _z(_slope_pct(capex, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_504d_v203_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_504d_v204_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_504d_v205_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 504d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_756d_v206_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_756d_v207_signal(capex):
    """Relative momentum strength for Raw level of capex over 756d window."""
    res = _z(_slope_pct(capex, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_756d_v208_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_756d_v209_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_756d_v210_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 756d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_1008d_v211_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_1008d_v212_signal(capex):
    """Relative momentum strength for Raw level of capex over 1008d window."""
    res = _z(_slope_pct(capex, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_1008d_v213_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_1008d_v214_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_1008d_v215_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_mom_z_1260d_v216_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_mom_z_1260d_v217_signal(capex):
    """Relative momentum strength for Raw level of capex over 1260d window."""
    res = _z(_slope_pct(capex, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_mom_z_1260d_v218_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_mom_z_1260d_v219_signal(revenue, capex):
    """Relative momentum strength for Revenue per unit of capital expenditure over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, capex), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_mom_z_1260d_v220_signal(revenue, capex, assets):
    """Relative momentum strength for Net unit productivity relative to assets over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue - capex, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_5d_v221_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_5d_v222_signal(capex):
    """Volatility of the momentum for Raw level of capex over 5d window."""
    res = _std(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_5d_v223_signal(assets):
    """Volatility of the momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_5d_v224_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_5d_v225_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 5d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_10d_v226_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_10d_v227_signal(capex):
    """Volatility of the momentum for Raw level of capex over 10d window."""
    res = _std(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_10d_v228_signal(assets):
    """Volatility of the momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_10d_v229_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_10d_v230_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 10d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_21d_v231_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_21d_v232_signal(capex):
    """Volatility of the momentum for Raw level of capex over 21d window."""
    res = _std(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_21d_v233_signal(assets):
    """Volatility of the momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_21d_v234_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_21d_v235_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 21d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_42d_v236_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_42d_v237_signal(capex):
    """Volatility of the momentum for Raw level of capex over 42d window."""
    res = _std(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_42d_v238_signal(assets):
    """Volatility of the momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_42d_v239_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_42d_v240_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 42d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_63d_v241_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_63d_v242_signal(capex):
    """Volatility of the momentum for Raw level of capex over 63d window."""
    res = _std(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_63d_v243_signal(assets):
    """Volatility of the momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_63d_v244_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_63d_v245_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 63d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_126d_v246_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_126d_v247_signal(capex):
    """Volatility of the momentum for Raw level of capex over 126d window."""
    res = _std(_slope_pct(capex, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_126d_v248_signal(assets):
    """Volatility of the momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_126d_v249_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_126d_v250_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 126d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_252d_v251_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_252d_v252_signal(capex):
    """Volatility of the momentum for Raw level of capex over 252d window."""
    res = _std(_slope_pct(capex, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_252d_v253_signal(assets):
    """Volatility of the momentum for Raw level of assets over 252d window."""
    res = _std(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_252d_v254_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_252d_v255_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 252d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_504d_v256_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_504d_v257_signal(capex):
    """Volatility of the momentum for Raw level of capex over 504d window."""
    res = _std(_slope_pct(capex, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_504d_v258_signal(assets):
    """Volatility of the momentum for Raw level of assets over 504d window."""
    res = _std(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_504d_v259_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_504d_v260_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 504d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_756d_v261_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_756d_v262_signal(capex):
    """Volatility of the momentum for Raw level of capex over 756d window."""
    res = _std(_slope_pct(capex, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_756d_v263_signal(assets):
    """Volatility of the momentum for Raw level of assets over 756d window."""
    res = _std(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_756d_v264_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_756d_v265_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 756d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_1008d_v266_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_1008d_v267_signal(capex):
    """Volatility of the momentum for Raw level of capex over 1008d window."""
    res = _std(_slope_pct(capex, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_1008d_v268_signal(assets):
    """Volatility of the momentum for Raw level of assets over 1008d window."""
    res = _std(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_1008d_v269_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_1008d_v270_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_vol_slope_1260d_v271_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_vol_slope_1260d_v272_signal(capex):
    """Volatility of the momentum for Raw level of capex over 1260d window."""
    res = _std(_slope_pct(capex, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_vol_slope_1260d_v273_signal(assets):
    """Volatility of the momentum for Raw level of assets over 1260d window."""
    res = _std(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_vol_slope_1260d_v274_signal(revenue, capex):
    """Volatility of the momentum for Revenue per unit of capital expenditure over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, capex), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_vol_slope_1260d_v275_signal(revenue, capex, assets):
    """Volatility of the momentum for Net unit productivity relative to assets over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue - capex, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f01_unit_economics_revenue_slope_diff_norm_756d_v151_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_756d_v151_signal},    "f01_unit_economics_capex_slope_diff_norm_756d_v152_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_756d_v152_signal},    "f01_unit_economics_assets_slope_diff_norm_756d_v153_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_756d_v153_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_756d_v154_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_756d_v154_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_756d_v155_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_756d_v155_signal},    "f01_unit_economics_revenue_slope_diff_norm_1008d_v156_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_1008d_v156_signal},    "f01_unit_economics_capex_slope_diff_norm_1008d_v157_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_1008d_v157_signal},    "f01_unit_economics_assets_slope_diff_norm_1008d_v158_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_1008d_v158_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_1008d_v159_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_1008d_v159_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_1008d_v160_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_1008d_v160_signal},    "f01_unit_economics_revenue_slope_diff_norm_1260d_v161_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_1260d_v161_signal},    "f01_unit_economics_capex_slope_diff_norm_1260d_v162_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_1260d_v162_signal},    "f01_unit_economics_assets_slope_diff_norm_1260d_v163_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_1260d_v163_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_1260d_v164_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_1260d_v164_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_1260d_v165_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_1260d_v165_signal},    "f01_unit_economics_revenue_mom_z_5d_v166_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_5d_v166_signal},    "f01_unit_economics_capex_mom_z_5d_v167_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_5d_v167_signal},    "f01_unit_economics_assets_mom_z_5d_v168_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_5d_v168_signal},    "f01_unit_economics_rev_per_capex_mom_z_5d_v169_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_5d_v169_signal},    "f01_unit_economics_asset_efficiency_mom_z_5d_v170_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_5d_v170_signal},    "f01_unit_economics_revenue_mom_z_10d_v171_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_10d_v171_signal},    "f01_unit_economics_capex_mom_z_10d_v172_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_10d_v172_signal},    "f01_unit_economics_assets_mom_z_10d_v173_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_10d_v173_signal},    "f01_unit_economics_rev_per_capex_mom_z_10d_v174_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_10d_v174_signal},    "f01_unit_economics_asset_efficiency_mom_z_10d_v175_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_10d_v175_signal},    "f01_unit_economics_revenue_mom_z_21d_v176_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_21d_v176_signal},    "f01_unit_economics_capex_mom_z_21d_v177_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_21d_v177_signal},    "f01_unit_economics_assets_mom_z_21d_v178_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_21d_v178_signal},    "f01_unit_economics_rev_per_capex_mom_z_21d_v179_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_21d_v179_signal},    "f01_unit_economics_asset_efficiency_mom_z_21d_v180_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_21d_v180_signal},    "f01_unit_economics_revenue_mom_z_42d_v181_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_42d_v181_signal},    "f01_unit_economics_capex_mom_z_42d_v182_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_42d_v182_signal},    "f01_unit_economics_assets_mom_z_42d_v183_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_42d_v183_signal},    "f01_unit_economics_rev_per_capex_mom_z_42d_v184_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_42d_v184_signal},    "f01_unit_economics_asset_efficiency_mom_z_42d_v185_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_42d_v185_signal},    "f01_unit_economics_revenue_mom_z_63d_v186_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_63d_v186_signal},    "f01_unit_economics_capex_mom_z_63d_v187_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_63d_v187_signal},    "f01_unit_economics_assets_mom_z_63d_v188_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_63d_v188_signal},    "f01_unit_economics_rev_per_capex_mom_z_63d_v189_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_63d_v189_signal},    "f01_unit_economics_asset_efficiency_mom_z_63d_v190_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_63d_v190_signal},    "f01_unit_economics_revenue_mom_z_126d_v191_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_126d_v191_signal},    "f01_unit_economics_capex_mom_z_126d_v192_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_126d_v192_signal},    "f01_unit_economics_assets_mom_z_126d_v193_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_126d_v193_signal},    "f01_unit_economics_rev_per_capex_mom_z_126d_v194_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_126d_v194_signal},    "f01_unit_economics_asset_efficiency_mom_z_126d_v195_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_126d_v195_signal},    "f01_unit_economics_revenue_mom_z_252d_v196_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_252d_v196_signal},    "f01_unit_economics_capex_mom_z_252d_v197_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_252d_v197_signal},    "f01_unit_economics_assets_mom_z_252d_v198_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_252d_v198_signal},    "f01_unit_economics_rev_per_capex_mom_z_252d_v199_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_252d_v199_signal},    "f01_unit_economics_asset_efficiency_mom_z_252d_v200_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_252d_v200_signal},    "f01_unit_economics_revenue_mom_z_504d_v201_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_504d_v201_signal},    "f01_unit_economics_capex_mom_z_504d_v202_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_504d_v202_signal},    "f01_unit_economics_assets_mom_z_504d_v203_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_504d_v203_signal},    "f01_unit_economics_rev_per_capex_mom_z_504d_v204_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_504d_v204_signal},    "f01_unit_economics_asset_efficiency_mom_z_504d_v205_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_504d_v205_signal},    "f01_unit_economics_revenue_mom_z_756d_v206_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_756d_v206_signal},    "f01_unit_economics_capex_mom_z_756d_v207_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_756d_v207_signal},    "f01_unit_economics_assets_mom_z_756d_v208_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_756d_v208_signal},    "f01_unit_economics_rev_per_capex_mom_z_756d_v209_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_756d_v209_signal},    "f01_unit_economics_asset_efficiency_mom_z_756d_v210_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_756d_v210_signal},    "f01_unit_economics_revenue_mom_z_1008d_v211_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_1008d_v211_signal},    "f01_unit_economics_capex_mom_z_1008d_v212_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_1008d_v212_signal},    "f01_unit_economics_assets_mom_z_1008d_v213_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_1008d_v213_signal},    "f01_unit_economics_rev_per_capex_mom_z_1008d_v214_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_1008d_v214_signal},    "f01_unit_economics_asset_efficiency_mom_z_1008d_v215_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_1008d_v215_signal},    "f01_unit_economics_revenue_mom_z_1260d_v216_signal": {"inputs": [], "func": f01_unit_economics_revenue_mom_z_1260d_v216_signal},    "f01_unit_economics_capex_mom_z_1260d_v217_signal": {"inputs": [], "func": f01_unit_economics_capex_mom_z_1260d_v217_signal},    "f01_unit_economics_assets_mom_z_1260d_v218_signal": {"inputs": [], "func": f01_unit_economics_assets_mom_z_1260d_v218_signal},    "f01_unit_economics_rev_per_capex_mom_z_1260d_v219_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_mom_z_1260d_v219_signal},    "f01_unit_economics_asset_efficiency_mom_z_1260d_v220_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_mom_z_1260d_v220_signal},    "f01_unit_economics_revenue_vol_slope_5d_v221_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_5d_v221_signal},    "f01_unit_economics_capex_vol_slope_5d_v222_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_5d_v222_signal},    "f01_unit_economics_assets_vol_slope_5d_v223_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_5d_v223_signal},    "f01_unit_economics_rev_per_capex_vol_slope_5d_v224_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_5d_v224_signal},    "f01_unit_economics_asset_efficiency_vol_slope_5d_v225_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_5d_v225_signal},    "f01_unit_economics_revenue_vol_slope_10d_v226_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_10d_v226_signal},    "f01_unit_economics_capex_vol_slope_10d_v227_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_10d_v227_signal},    "f01_unit_economics_assets_vol_slope_10d_v228_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_10d_v228_signal},    "f01_unit_economics_rev_per_capex_vol_slope_10d_v229_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_10d_v229_signal},    "f01_unit_economics_asset_efficiency_vol_slope_10d_v230_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_10d_v230_signal},    "f01_unit_economics_revenue_vol_slope_21d_v231_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_21d_v231_signal},    "f01_unit_economics_capex_vol_slope_21d_v232_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_21d_v232_signal},    "f01_unit_economics_assets_vol_slope_21d_v233_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_21d_v233_signal},    "f01_unit_economics_rev_per_capex_vol_slope_21d_v234_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_21d_v234_signal},    "f01_unit_economics_asset_efficiency_vol_slope_21d_v235_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_21d_v235_signal},    "f01_unit_economics_revenue_vol_slope_42d_v236_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_42d_v236_signal},    "f01_unit_economics_capex_vol_slope_42d_v237_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_42d_v237_signal},    "f01_unit_economics_assets_vol_slope_42d_v238_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_42d_v238_signal},    "f01_unit_economics_rev_per_capex_vol_slope_42d_v239_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_42d_v239_signal},    "f01_unit_economics_asset_efficiency_vol_slope_42d_v240_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_42d_v240_signal},    "f01_unit_economics_revenue_vol_slope_63d_v241_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_63d_v241_signal},    "f01_unit_economics_capex_vol_slope_63d_v242_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_63d_v242_signal},    "f01_unit_economics_assets_vol_slope_63d_v243_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_63d_v243_signal},    "f01_unit_economics_rev_per_capex_vol_slope_63d_v244_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_63d_v244_signal},    "f01_unit_economics_asset_efficiency_vol_slope_63d_v245_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_63d_v245_signal},    "f01_unit_economics_revenue_vol_slope_126d_v246_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_126d_v246_signal},    "f01_unit_economics_capex_vol_slope_126d_v247_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_126d_v247_signal},    "f01_unit_economics_assets_vol_slope_126d_v248_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_126d_v248_signal},    "f01_unit_economics_rev_per_capex_vol_slope_126d_v249_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_126d_v249_signal},    "f01_unit_economics_asset_efficiency_vol_slope_126d_v250_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_126d_v250_signal},    "f01_unit_economics_revenue_vol_slope_252d_v251_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_252d_v251_signal},    "f01_unit_economics_capex_vol_slope_252d_v252_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_252d_v252_signal},    "f01_unit_economics_assets_vol_slope_252d_v253_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_252d_v253_signal},    "f01_unit_economics_rev_per_capex_vol_slope_252d_v254_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_252d_v254_signal},    "f01_unit_economics_asset_efficiency_vol_slope_252d_v255_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_252d_v255_signal},    "f01_unit_economics_revenue_vol_slope_504d_v256_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_504d_v256_signal},    "f01_unit_economics_capex_vol_slope_504d_v257_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_504d_v257_signal},    "f01_unit_economics_assets_vol_slope_504d_v258_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_504d_v258_signal},    "f01_unit_economics_rev_per_capex_vol_slope_504d_v259_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_504d_v259_signal},    "f01_unit_economics_asset_efficiency_vol_slope_504d_v260_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_504d_v260_signal},    "f01_unit_economics_revenue_vol_slope_756d_v261_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_756d_v261_signal},    "f01_unit_economics_capex_vol_slope_756d_v262_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_756d_v262_signal},    "f01_unit_economics_assets_vol_slope_756d_v263_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_756d_v263_signal},    "f01_unit_economics_rev_per_capex_vol_slope_756d_v264_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_756d_v264_signal},    "f01_unit_economics_asset_efficiency_vol_slope_756d_v265_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_756d_v265_signal},    "f01_unit_economics_revenue_vol_slope_1008d_v266_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_1008d_v266_signal},    "f01_unit_economics_capex_vol_slope_1008d_v267_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_1008d_v267_signal},    "f01_unit_economics_assets_vol_slope_1008d_v268_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_1008d_v268_signal},    "f01_unit_economics_rev_per_capex_vol_slope_1008d_v269_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_1008d_v269_signal},    "f01_unit_economics_asset_efficiency_vol_slope_1008d_v270_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_1008d_v270_signal},    "f01_unit_economics_revenue_vol_slope_1260d_v271_signal": {"inputs": [], "func": f01_unit_economics_revenue_vol_slope_1260d_v271_signal},    "f01_unit_economics_capex_vol_slope_1260d_v272_signal": {"inputs": [], "func": f01_unit_economics_capex_vol_slope_1260d_v272_signal},    "f01_unit_economics_assets_vol_slope_1260d_v273_signal": {"inputs": [], "func": f01_unit_economics_assets_vol_slope_1260d_v273_signal},    "f01_unit_economics_rev_per_capex_vol_slope_1260d_v274_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_vol_slope_1260d_v274_signal},    "f01_unit_economics_asset_efficiency_vol_slope_1260d_v275_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_vol_slope_1260d_v275_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 01...")
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
