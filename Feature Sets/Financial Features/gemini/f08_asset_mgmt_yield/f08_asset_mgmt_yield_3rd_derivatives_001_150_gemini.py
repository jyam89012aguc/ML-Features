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

def f08_asset_mgmt_yield_netinc_slope_diff_norm_756d_v151_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_756d_v152_signal(invcap):
    """Normalized slope change for Raw level of invcap over 756d window."""
    res = (_slope_pct(invcap, 756).diff(756) / _sma(invcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_756d_v153_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_756d_v154_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 756d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 756).diff(756) / _sma(_ratio(netinc, invcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_756d_v155_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 756d window."""
    res = (_slope_pct(_ratio(revenue, assets), 756).diff(756) / _sma(_ratio(revenue, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_1008d_v156_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_1008d_v157_signal(invcap):
    """Normalized slope change for Raw level of invcap over 1008d window."""
    res = (_slope_pct(invcap, 1008).diff(1008) / _sma(invcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_1008d_v158_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_1008d_v159_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 1008d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 1008).diff(1008) / _sma(_ratio(netinc, invcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_1008d_v160_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 1008d window."""
    res = (_slope_pct(_ratio(revenue, assets), 1008).diff(1008) / _sma(_ratio(revenue, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_1260d_v161_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_1260d_v162_signal(invcap):
    """Normalized slope change for Raw level of invcap over 1260d window."""
    res = (_slope_pct(invcap, 1260).diff(1260) / _sma(invcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_1260d_v163_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_1260d_v164_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 1260d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 1260).diff(1260) / _sma(_ratio(netinc, invcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_1260d_v165_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 1260d window."""
    res = (_slope_pct(_ratio(revenue, assets), 1260).diff(1260) / _sma(_ratio(revenue, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_5d_v166_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_5d_v167_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 5d window."""
    res = _z(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_5d_v168_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_5d_v169_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 5d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_5d_v170_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 5d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_10d_v171_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_10d_v172_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 10d window."""
    res = _z(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_10d_v173_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_10d_v174_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 10d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_10d_v175_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 10d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_21d_v176_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_21d_v177_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 21d window."""
    res = _z(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_21d_v178_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_21d_v179_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 21d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_21d_v180_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 21d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_42d_v181_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_42d_v182_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 42d window."""
    res = _z(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_42d_v183_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_42d_v184_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 42d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_42d_v185_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 42d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_63d_v186_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_63d_v187_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 63d window."""
    res = _z(_slope_pct(invcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_63d_v188_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_63d_v189_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 63d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_63d_v190_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_126d_v191_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_126d_v192_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 126d window."""
    res = _z(_slope_pct(invcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_126d_v193_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_126d_v194_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 126d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_126d_v195_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_252d_v196_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_252d_v197_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 252d window."""
    res = _z(_slope_pct(invcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_252d_v198_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_252d_v199_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 252d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_252d_v200_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_504d_v201_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_504d_v202_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 504d window."""
    res = _z(_slope_pct(invcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_504d_v203_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_504d_v204_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 504d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_504d_v205_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_756d_v206_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_756d_v207_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 756d window."""
    res = _z(_slope_pct(invcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_756d_v208_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_756d_v209_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 756d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_756d_v210_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_1008d_v211_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_1008d_v212_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 1008d window."""
    res = _z(_slope_pct(invcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_1008d_v213_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_1008d_v214_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 1008d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_1008d_v215_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_mom_z_1260d_v216_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_mom_z_1260d_v217_signal(invcap):
    """Relative momentum strength for Raw level of invcap over 1260d window."""
    res = _z(_slope_pct(invcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_mom_z_1260d_v218_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_mom_z_1260d_v219_signal(netinc, invcap):
    """Relative momentum strength for Return on invested capital over 1260d window."""
    res = _z(_slope_pct(_ratio(netinc, invcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_mom_z_1260d_v220_signal(revenue, assets):
    """Relative momentum strength for Total asset utilization over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_5d_v221_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_5d_v222_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 5d window."""
    res = _std(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_5d_v223_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_5d_v224_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 5d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_5d_v225_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_10d_v226_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_10d_v227_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 10d window."""
    res = _std(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_10d_v228_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_10d_v229_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 10d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_10d_v230_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_21d_v231_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_21d_v232_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 21d window."""
    res = _std(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_21d_v233_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_21d_v234_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 21d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_21d_v235_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_42d_v236_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_42d_v237_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 42d window."""
    res = _std(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_42d_v238_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_42d_v239_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 42d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_42d_v240_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_63d_v241_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_63d_v242_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 63d window."""
    res = _std(_slope_pct(invcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_63d_v243_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_63d_v244_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 63d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_63d_v245_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_126d_v246_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_126d_v247_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 126d window."""
    res = _std(_slope_pct(invcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_126d_v248_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_126d_v249_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 126d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_126d_v250_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_252d_v251_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_252d_v252_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 252d window."""
    res = _std(_slope_pct(invcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_252d_v253_signal(assets):
    """Volatility of momentum for Raw level of assets over 252d window."""
    res = _std(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_252d_v254_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 252d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_252d_v255_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_504d_v256_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_504d_v257_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 504d window."""
    res = _std(_slope_pct(invcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_504d_v258_signal(assets):
    """Volatility of momentum for Raw level of assets over 504d window."""
    res = _std(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_504d_v259_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 504d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_504d_v260_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_756d_v261_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_756d_v262_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 756d window."""
    res = _std(_slope_pct(invcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_756d_v263_signal(assets):
    """Volatility of momentum for Raw level of assets over 756d window."""
    res = _std(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_756d_v264_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 756d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_756d_v265_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_1008d_v266_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_1008d_v267_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 1008d window."""
    res = _std(_slope_pct(invcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_1008d_v268_signal(assets):
    """Volatility of momentum for Raw level of assets over 1008d window."""
    res = _std(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_1008d_v269_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 1008d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_1008d_v270_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_vol_slope_1260d_v271_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_vol_slope_1260d_v272_signal(invcap):
    """Volatility of momentum for Raw level of invcap over 1260d window."""
    res = _std(_slope_pct(invcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_vol_slope_1260d_v273_signal(assets):
    """Volatility of momentum for Raw level of assets over 1260d window."""
    res = _std(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_vol_slope_1260d_v274_signal(netinc, invcap):
    """Volatility of momentum for Return on invested capital over 1260d window."""
    res = _std(_slope_pct(_ratio(netinc, invcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_vol_slope_1260d_v275_signal(revenue, assets):
    """Volatility of momentum for Total asset utilization over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_slope_5d_v276_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _ewma(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_slope_5d_v277_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 5d window."""
    res = _ewma(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_slope_5d_v278_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 5d window."""
    res = _ewma(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_slope_5d_v279_signal(netinc, invcap):
    """Exponential momentum smoothing for Return on invested capital over 5d window."""
    res = _ewma(_slope_pct(_ratio(netinc, invcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_slope_5d_v280_signal(revenue, assets):
    """Exponential momentum smoothing for Total asset utilization over 5d window."""
    res = _ewma(_slope_pct(_ratio(revenue, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_slope_10d_v281_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _ewma(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_slope_10d_v282_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 10d window."""
    res = _ewma(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_slope_10d_v283_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 10d window."""
    res = _ewma(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_slope_10d_v284_signal(netinc, invcap):
    """Exponential momentum smoothing for Return on invested capital over 10d window."""
    res = _ewma(_slope_pct(_ratio(netinc, invcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_slope_10d_v285_signal(revenue, assets):
    """Exponential momentum smoothing for Total asset utilization over 10d window."""
    res = _ewma(_slope_pct(_ratio(revenue, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_slope_21d_v286_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _ewma(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_slope_21d_v287_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 21d window."""
    res = _ewma(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_slope_21d_v288_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 21d window."""
    res = _ewma(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_slope_21d_v289_signal(netinc, invcap):
    """Exponential momentum smoothing for Return on invested capital over 21d window."""
    res = _ewma(_slope_pct(_ratio(netinc, invcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_slope_21d_v290_signal(revenue, assets):
    """Exponential momentum smoothing for Total asset utilization over 21d window."""
    res = _ewma(_slope_pct(_ratio(revenue, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_slope_42d_v291_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _ewma(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_slope_42d_v292_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 42d window."""
    res = _ewma(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_slope_42d_v293_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 42d window."""
    res = _ewma(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_slope_42d_v294_signal(netinc, invcap):
    """Exponential momentum smoothing for Return on invested capital over 42d window."""
    res = _ewma(_slope_pct(_ratio(netinc, invcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_slope_42d_v295_signal(revenue, assets):
    """Exponential momentum smoothing for Total asset utilization over 42d window."""
    res = _ewma(_slope_pct(_ratio(revenue, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_slope_63d_v296_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _ewma(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_slope_63d_v297_signal(invcap):
    """Exponential momentum smoothing for Raw level of invcap over 63d window."""
    res = _ewma(_slope_pct(invcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_slope_63d_v298_signal(assets):
    """Exponential momentum smoothing for Raw level of assets over 63d window."""
    res = _ewma(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_slope_63d_v299_signal(netinc, invcap):
    """Exponential momentum smoothing for Return on invested capital over 63d window."""
    res = _ewma(_slope_pct(_ratio(netinc, invcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_slope_63d_v300_signal(revenue, assets):
    """Exponential momentum smoothing for Total asset utilization over 63d window."""
    res = _ewma(_slope_pct(_ratio(revenue, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_756d_v151_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_756d_v151_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_756d_v152_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_756d_v152_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_756d_v153_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_756d_v153_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_756d_v154_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_756d_v154_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_756d_v155_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_756d_v155_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_1008d_v156_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_1008d_v156_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_1008d_v157_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_1008d_v157_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_1008d_v158_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_1008d_v158_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_1008d_v159_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_1008d_v159_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_1008d_v160_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_1008d_v160_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_1260d_v161_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_1260d_v161_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_1260d_v162_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_1260d_v162_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_1260d_v163_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_1260d_v163_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_1260d_v164_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_1260d_v164_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_1260d_v165_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_1260d_v165_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_5d_v166_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_5d_v166_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_5d_v167_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_5d_v167_signal},
    "f08_asset_mgmt_yield_assets_mom_z_5d_v168_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_5d_v168_signal},
    "f08_asset_mgmt_yield_roic_mom_z_5d_v169_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_5d_v169_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_5d_v170_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_5d_v170_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_10d_v171_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_10d_v171_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_10d_v172_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_10d_v172_signal},
    "f08_asset_mgmt_yield_assets_mom_z_10d_v173_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_10d_v173_signal},
    "f08_asset_mgmt_yield_roic_mom_z_10d_v174_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_10d_v174_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_10d_v175_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_10d_v175_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_21d_v176_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_21d_v176_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_21d_v177_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_21d_v177_signal},
    "f08_asset_mgmt_yield_assets_mom_z_21d_v178_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_21d_v178_signal},
    "f08_asset_mgmt_yield_roic_mom_z_21d_v179_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_21d_v179_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_21d_v180_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_21d_v180_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_42d_v181_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_42d_v181_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_42d_v182_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_42d_v182_signal},
    "f08_asset_mgmt_yield_assets_mom_z_42d_v183_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_42d_v183_signal},
    "f08_asset_mgmt_yield_roic_mom_z_42d_v184_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_42d_v184_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_42d_v185_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_42d_v185_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_63d_v186_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_63d_v186_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_63d_v187_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_63d_v187_signal},
    "f08_asset_mgmt_yield_assets_mom_z_63d_v188_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_63d_v188_signal},
    "f08_asset_mgmt_yield_roic_mom_z_63d_v189_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_63d_v189_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_63d_v190_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_63d_v190_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_126d_v191_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_126d_v191_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_126d_v192_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_126d_v192_signal},
    "f08_asset_mgmt_yield_assets_mom_z_126d_v193_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_126d_v193_signal},
    "f08_asset_mgmt_yield_roic_mom_z_126d_v194_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_126d_v194_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_126d_v195_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_126d_v195_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_252d_v196_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_252d_v196_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_252d_v197_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_252d_v197_signal},
    "f08_asset_mgmt_yield_assets_mom_z_252d_v198_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_252d_v198_signal},
    "f08_asset_mgmt_yield_roic_mom_z_252d_v199_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_252d_v199_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_252d_v200_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_252d_v200_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_504d_v201_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_504d_v201_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_504d_v202_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_504d_v202_signal},
    "f08_asset_mgmt_yield_assets_mom_z_504d_v203_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_504d_v203_signal},
    "f08_asset_mgmt_yield_roic_mom_z_504d_v204_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_504d_v204_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_504d_v205_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_504d_v205_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_756d_v206_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_756d_v206_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_756d_v207_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_756d_v207_signal},
    "f08_asset_mgmt_yield_assets_mom_z_756d_v208_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_756d_v208_signal},
    "f08_asset_mgmt_yield_roic_mom_z_756d_v209_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_756d_v209_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_756d_v210_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_756d_v210_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_1008d_v211_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_1008d_v211_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_1008d_v212_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_1008d_v212_signal},
    "f08_asset_mgmt_yield_assets_mom_z_1008d_v213_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_1008d_v213_signal},
    "f08_asset_mgmt_yield_roic_mom_z_1008d_v214_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_1008d_v214_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_1008d_v215_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_1008d_v215_signal},
    "f08_asset_mgmt_yield_netinc_mom_z_1260d_v216_signal": {"func": f08_asset_mgmt_yield_netinc_mom_z_1260d_v216_signal},
    "f08_asset_mgmt_yield_invcap_mom_z_1260d_v217_signal": {"func": f08_asset_mgmt_yield_invcap_mom_z_1260d_v217_signal},
    "f08_asset_mgmt_yield_assets_mom_z_1260d_v218_signal": {"func": f08_asset_mgmt_yield_assets_mom_z_1260d_v218_signal},
    "f08_asset_mgmt_yield_roic_mom_z_1260d_v219_signal": {"func": f08_asset_mgmt_yield_roic_mom_z_1260d_v219_signal},
    "f08_asset_mgmt_yield_asset_turnover_mom_z_1260d_v220_signal": {"func": f08_asset_mgmt_yield_asset_turnover_mom_z_1260d_v220_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_5d_v221_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_5d_v221_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_5d_v222_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_5d_v222_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_5d_v223_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_5d_v223_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_5d_v224_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_5d_v224_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_5d_v225_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_5d_v225_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_10d_v226_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_10d_v226_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_10d_v227_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_10d_v227_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_10d_v228_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_10d_v228_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_10d_v229_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_10d_v229_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_10d_v230_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_10d_v230_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_21d_v231_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_21d_v231_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_21d_v232_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_21d_v232_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_21d_v233_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_21d_v233_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_21d_v234_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_21d_v234_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_21d_v235_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_21d_v235_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_42d_v236_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_42d_v236_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_42d_v237_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_42d_v237_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_42d_v238_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_42d_v238_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_42d_v239_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_42d_v239_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_42d_v240_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_42d_v240_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_63d_v241_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_63d_v241_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_63d_v242_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_63d_v242_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_63d_v243_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_63d_v243_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_63d_v244_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_63d_v244_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_63d_v245_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_63d_v245_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_126d_v246_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_126d_v246_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_126d_v247_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_126d_v247_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_126d_v248_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_126d_v248_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_126d_v249_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_126d_v249_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_126d_v250_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_126d_v250_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_252d_v251_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_252d_v251_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_252d_v252_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_252d_v252_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_252d_v253_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_252d_v253_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_252d_v254_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_252d_v254_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_252d_v255_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_252d_v255_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_504d_v256_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_504d_v256_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_504d_v257_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_504d_v257_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_504d_v258_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_504d_v258_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_504d_v259_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_504d_v259_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_504d_v260_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_504d_v260_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_756d_v261_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_756d_v261_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_756d_v262_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_756d_v262_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_756d_v263_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_756d_v263_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_756d_v264_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_756d_v264_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_756d_v265_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_756d_v265_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_1008d_v266_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_1008d_v266_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_1008d_v267_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_1008d_v267_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_1008d_v268_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_1008d_v268_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_1008d_v269_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_1008d_v269_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_1008d_v270_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_1008d_v270_signal},
    "f08_asset_mgmt_yield_netinc_vol_slope_1260d_v271_signal": {"func": f08_asset_mgmt_yield_netinc_vol_slope_1260d_v271_signal},
    "f08_asset_mgmt_yield_invcap_vol_slope_1260d_v272_signal": {"func": f08_asset_mgmt_yield_invcap_vol_slope_1260d_v272_signal},
    "f08_asset_mgmt_yield_assets_vol_slope_1260d_v273_signal": {"func": f08_asset_mgmt_yield_assets_vol_slope_1260d_v273_signal},
    "f08_asset_mgmt_yield_roic_vol_slope_1260d_v274_signal": {"func": f08_asset_mgmt_yield_roic_vol_slope_1260d_v274_signal},
    "f08_asset_mgmt_yield_asset_turnover_vol_slope_1260d_v275_signal": {"func": f08_asset_mgmt_yield_asset_turnover_vol_slope_1260d_v275_signal},
    "f08_asset_mgmt_yield_netinc_ewma_slope_5d_v276_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_slope_5d_v276_signal},
    "f08_asset_mgmt_yield_invcap_ewma_slope_5d_v277_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_slope_5d_v277_signal},
    "f08_asset_mgmt_yield_assets_ewma_slope_5d_v278_signal": {"func": f08_asset_mgmt_yield_assets_ewma_slope_5d_v278_signal},
    "f08_asset_mgmt_yield_roic_ewma_slope_5d_v279_signal": {"func": f08_asset_mgmt_yield_roic_ewma_slope_5d_v279_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_slope_5d_v280_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_slope_5d_v280_signal},
    "f08_asset_mgmt_yield_netinc_ewma_slope_10d_v281_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_slope_10d_v281_signal},
    "f08_asset_mgmt_yield_invcap_ewma_slope_10d_v282_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_slope_10d_v282_signal},
    "f08_asset_mgmt_yield_assets_ewma_slope_10d_v283_signal": {"func": f08_asset_mgmt_yield_assets_ewma_slope_10d_v283_signal},
    "f08_asset_mgmt_yield_roic_ewma_slope_10d_v284_signal": {"func": f08_asset_mgmt_yield_roic_ewma_slope_10d_v284_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_slope_10d_v285_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_slope_10d_v285_signal},
    "f08_asset_mgmt_yield_netinc_ewma_slope_21d_v286_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_slope_21d_v286_signal},
    "f08_asset_mgmt_yield_invcap_ewma_slope_21d_v287_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_slope_21d_v287_signal},
    "f08_asset_mgmt_yield_assets_ewma_slope_21d_v288_signal": {"func": f08_asset_mgmt_yield_assets_ewma_slope_21d_v288_signal},
    "f08_asset_mgmt_yield_roic_ewma_slope_21d_v289_signal": {"func": f08_asset_mgmt_yield_roic_ewma_slope_21d_v289_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_slope_21d_v290_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_slope_21d_v290_signal},
    "f08_asset_mgmt_yield_netinc_ewma_slope_42d_v291_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_slope_42d_v291_signal},
    "f08_asset_mgmt_yield_invcap_ewma_slope_42d_v292_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_slope_42d_v292_signal},
    "f08_asset_mgmt_yield_assets_ewma_slope_42d_v293_signal": {"func": f08_asset_mgmt_yield_assets_ewma_slope_42d_v293_signal},
    "f08_asset_mgmt_yield_roic_ewma_slope_42d_v294_signal": {"func": f08_asset_mgmt_yield_roic_ewma_slope_42d_v294_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_slope_42d_v295_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_slope_42d_v295_signal},
    "f08_asset_mgmt_yield_netinc_ewma_slope_63d_v296_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_slope_63d_v296_signal},
    "f08_asset_mgmt_yield_invcap_ewma_slope_63d_v297_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_slope_63d_v297_signal},
    "f08_asset_mgmt_yield_assets_ewma_slope_63d_v298_signal": {"func": f08_asset_mgmt_yield_assets_ewma_slope_63d_v298_signal},
    "f08_asset_mgmt_yield_roic_ewma_slope_63d_v299_signal": {"func": f08_asset_mgmt_yield_roic_ewma_slope_63d_v299_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_slope_63d_v300_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_slope_63d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 08...")
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
