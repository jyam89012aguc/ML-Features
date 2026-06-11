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

def f03_nim_proxy_netinc_slope_diff_norm_42d_v151_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_42d_v152_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_42d_v153_signal(ebt):
    """Normalized slope change for Raw level of ebt over 42d window."""
    res = (_slope_pct(ebt, 42).diff(42) / _sma(ebt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_42d_v154_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 42d window."""
    res = (_slope_pct(_ratio(netinc, assets), 42).diff(42) / _sma(_ratio(netinc, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_42d_v155_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 42d window."""
    res = (_slope_pct(_ratio(ebt, assets), 42).diff(42) / _sma(_ratio(ebt, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_42d_v156_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 42d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 42).diff(42) / _sma(_ratio(netinc, ebt).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_63d_v157_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_63d_v158_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_63d_v159_signal(ebt):
    """Normalized slope change for Raw level of ebt over 63d window."""
    res = (_slope_pct(ebt, 63).diff(63) / _sma(ebt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_63d_v160_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 63d window."""
    res = (_slope_pct(_ratio(netinc, assets), 63).diff(63) / _sma(_ratio(netinc, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_63d_v161_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 63d window."""
    res = (_slope_pct(_ratio(ebt, assets), 63).diff(63) / _sma(_ratio(ebt, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_63d_v162_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 63d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 63).diff(63) / _sma(_ratio(netinc, ebt).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_126d_v163_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_126d_v164_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_126d_v165_signal(ebt):
    """Normalized slope change for Raw level of ebt over 126d window."""
    res = (_slope_pct(ebt, 126).diff(126) / _sma(ebt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_126d_v166_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 126d window."""
    res = (_slope_pct(_ratio(netinc, assets), 126).diff(126) / _sma(_ratio(netinc, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_126d_v167_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 126d window."""
    res = (_slope_pct(_ratio(ebt, assets), 126).diff(126) / _sma(_ratio(ebt, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_126d_v168_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 126d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 126).diff(126) / _sma(_ratio(netinc, ebt).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_252d_v169_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_252d_v170_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_252d_v171_signal(ebt):
    """Normalized slope change for Raw level of ebt over 252d window."""
    res = (_slope_pct(ebt, 252).diff(252) / _sma(ebt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_252d_v172_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 252d window."""
    res = (_slope_pct(_ratio(netinc, assets), 252).diff(252) / _sma(_ratio(netinc, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_252d_v173_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 252d window."""
    res = (_slope_pct(_ratio(ebt, assets), 252).diff(252) / _sma(_ratio(ebt, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_252d_v174_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 252d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 252).diff(252) / _sma(_ratio(netinc, ebt).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_504d_v175_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_504d_v176_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_504d_v177_signal(ebt):
    """Normalized slope change for Raw level of ebt over 504d window."""
    res = (_slope_pct(ebt, 504).diff(504) / _sma(ebt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_504d_v178_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 504d window."""
    res = (_slope_pct(_ratio(netinc, assets), 504).diff(504) / _sma(_ratio(netinc, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_504d_v179_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 504d window."""
    res = (_slope_pct(_ratio(ebt, assets), 504).diff(504) / _sma(_ratio(ebt, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_504d_v180_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 504d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 504).diff(504) / _sma(_ratio(netinc, ebt).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_756d_v181_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_756d_v182_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_756d_v183_signal(ebt):
    """Normalized slope change for Raw level of ebt over 756d window."""
    res = (_slope_pct(ebt, 756).diff(756) / _sma(ebt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_756d_v184_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 756d window."""
    res = (_slope_pct(_ratio(netinc, assets), 756).diff(756) / _sma(_ratio(netinc, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_756d_v185_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 756d window."""
    res = (_slope_pct(_ratio(ebt, assets), 756).diff(756) / _sma(_ratio(ebt, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_756d_v186_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 756d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 756).diff(756) / _sma(_ratio(netinc, ebt).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_1008d_v187_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_1008d_v188_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_1008d_v189_signal(ebt):
    """Normalized slope change for Raw level of ebt over 1008d window."""
    res = (_slope_pct(ebt, 1008).diff(1008) / _sma(ebt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_1008d_v190_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 1008d window."""
    res = (_slope_pct(_ratio(netinc, assets), 1008).diff(1008) / _sma(_ratio(netinc, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_1008d_v191_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 1008d window."""
    res = (_slope_pct(_ratio(ebt, assets), 1008).diff(1008) / _sma(_ratio(ebt, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_1008d_v192_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 1008d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 1008).diff(1008) / _sma(_ratio(netinc, ebt).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_1260d_v193_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_1260d_v194_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_1260d_v195_signal(ebt):
    """Normalized slope change for Raw level of ebt over 1260d window."""
    res = (_slope_pct(ebt, 1260).diff(1260) / _sma(ebt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_1260d_v196_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 1260d window."""
    res = (_slope_pct(_ratio(netinc, assets), 1260).diff(1260) / _sma(_ratio(netinc, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_1260d_v197_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 1260d window."""
    res = (_slope_pct(_ratio(ebt, assets), 1260).diff(1260) / _sma(_ratio(ebt, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_1260d_v198_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 1260d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 1260).diff(1260) / _sma(_ratio(netinc, ebt).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_5d_v199_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_5d_v200_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_5d_v201_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 5d window."""
    res = _z(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_5d_v202_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 5d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_5d_v203_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 5d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_5d_v204_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 5d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_10d_v205_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_10d_v206_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_10d_v207_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 10d window."""
    res = _z(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_10d_v208_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 10d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_10d_v209_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 10d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_10d_v210_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 10d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_21d_v211_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_21d_v212_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_21d_v213_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 21d window."""
    res = _z(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_21d_v214_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 21d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_21d_v215_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 21d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_21d_v216_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 21d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_42d_v217_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_42d_v218_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_42d_v219_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 42d window."""
    res = _z(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_42d_v220_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 42d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_42d_v221_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 42d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_42d_v222_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 42d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_63d_v223_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_63d_v224_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_63d_v225_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 63d window."""
    res = _z(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_63d_v226_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 63d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_63d_v227_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 63d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_63d_v228_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 63d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_126d_v229_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_126d_v230_signal(assets):
    """Relative momentum strength for Raw level of assets over 126d window."""
    res = _z(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_126d_v231_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 126d window."""
    res = _z(_slope_pct(ebt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_126d_v232_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 126d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_126d_v233_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 126d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_126d_v234_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 126d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_252d_v235_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_252d_v236_signal(assets):
    """Relative momentum strength for Raw level of assets over 252d window."""
    res = _z(_slope_pct(assets, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_252d_v237_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 252d window."""
    res = _z(_slope_pct(ebt, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_252d_v238_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 252d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_252d_v239_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 252d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_252d_v240_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 252d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_504d_v241_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_504d_v242_signal(assets):
    """Relative momentum strength for Raw level of assets over 504d window."""
    res = _z(_slope_pct(assets, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_504d_v243_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 504d window."""
    res = _z(_slope_pct(ebt, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_504d_v244_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 504d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_504d_v245_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 504d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_504d_v246_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 504d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_756d_v247_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_756d_v248_signal(assets):
    """Relative momentum strength for Raw level of assets over 756d window."""
    res = _z(_slope_pct(assets, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_756d_v249_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 756d window."""
    res = _z(_slope_pct(ebt, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_756d_v250_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 756d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_756d_v251_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 756d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_756d_v252_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 756d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_1008d_v253_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_1008d_v254_signal(assets):
    """Relative momentum strength for Raw level of assets over 1008d window."""
    res = _z(_slope_pct(assets, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_1008d_v255_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 1008d window."""
    res = _z(_slope_pct(ebt, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_1008d_v256_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 1008d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_1008d_v257_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 1008d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_1008d_v258_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 1008d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_mom_z_1260d_v259_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_mom_z_1260d_v260_signal(assets):
    """Relative momentum strength for Raw level of assets over 1260d window."""
    res = _z(_slope_pct(assets, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_mom_z_1260d_v261_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 1260d window."""
    res = _z(_slope_pct(ebt, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_mom_z_1260d_v262_signal(netinc, assets):
    """Relative momentum strength for Net return on assets over 1260d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_mom_z_1260d_v263_signal(ebt, assets):
    """Relative momentum strength for Pre-tax return on assets over 1260d window."""
    res = _z(_slope_pct(_ratio(ebt, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_mom_z_1260d_v264_signal(netinc, ebt):
    """Relative momentum strength for Tax efficiency proxy over 1260d window."""
    res = _z(_slope_pct(_ratio(netinc, ebt), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_vol_slope_5d_v265_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_vol_slope_5d_v266_signal(assets):
    """Volatility of momentum for Raw level of assets over 5d window."""
    res = _std(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_vol_slope_5d_v267_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 5d window."""
    res = _std(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_vol_slope_5d_v268_signal(netinc, assets):
    """Volatility of momentum for Net return on assets over 5d window."""
    res = _std(_slope_pct(_ratio(netinc, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_vol_slope_5d_v269_signal(ebt, assets):
    """Volatility of momentum for Pre-tax return on assets over 5d window."""
    res = _std(_slope_pct(_ratio(ebt, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_vol_slope_5d_v270_signal(netinc, ebt):
    """Volatility of momentum for Tax efficiency proxy over 5d window."""
    res = _std(_slope_pct(_ratio(netinc, ebt), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_vol_slope_10d_v271_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_vol_slope_10d_v272_signal(assets):
    """Volatility of momentum for Raw level of assets over 10d window."""
    res = _std(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_vol_slope_10d_v273_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 10d window."""
    res = _std(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_vol_slope_10d_v274_signal(netinc, assets):
    """Volatility of momentum for Net return on assets over 10d window."""
    res = _std(_slope_pct(_ratio(netinc, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_vol_slope_10d_v275_signal(ebt, assets):
    """Volatility of momentum for Pre-tax return on assets over 10d window."""
    res = _std(_slope_pct(_ratio(ebt, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_vol_slope_10d_v276_signal(netinc, ebt):
    """Volatility of momentum for Tax efficiency proxy over 10d window."""
    res = _std(_slope_pct(_ratio(netinc, ebt), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_vol_slope_21d_v277_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_vol_slope_21d_v278_signal(assets):
    """Volatility of momentum for Raw level of assets over 21d window."""
    res = _std(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_vol_slope_21d_v279_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 21d window."""
    res = _std(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_vol_slope_21d_v280_signal(netinc, assets):
    """Volatility of momentum for Net return on assets over 21d window."""
    res = _std(_slope_pct(_ratio(netinc, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_vol_slope_21d_v281_signal(ebt, assets):
    """Volatility of momentum for Pre-tax return on assets over 21d window."""
    res = _std(_slope_pct(_ratio(ebt, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_vol_slope_21d_v282_signal(netinc, ebt):
    """Volatility of momentum for Tax efficiency proxy over 21d window."""
    res = _std(_slope_pct(_ratio(netinc, ebt), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_vol_slope_42d_v283_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_vol_slope_42d_v284_signal(assets):
    """Volatility of momentum for Raw level of assets over 42d window."""
    res = _std(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_vol_slope_42d_v285_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 42d window."""
    res = _std(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_vol_slope_42d_v286_signal(netinc, assets):
    """Volatility of momentum for Net return on assets over 42d window."""
    res = _std(_slope_pct(_ratio(netinc, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_vol_slope_42d_v287_signal(ebt, assets):
    """Volatility of momentum for Pre-tax return on assets over 42d window."""
    res = _std(_slope_pct(_ratio(ebt, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_vol_slope_42d_v288_signal(netinc, ebt):
    """Volatility of momentum for Tax efficiency proxy over 42d window."""
    res = _std(_slope_pct(_ratio(netinc, ebt), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_vol_slope_63d_v289_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_vol_slope_63d_v290_signal(assets):
    """Volatility of momentum for Raw level of assets over 63d window."""
    res = _std(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_vol_slope_63d_v291_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 63d window."""
    res = _std(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_vol_slope_63d_v292_signal(netinc, assets):
    """Volatility of momentum for Net return on assets over 63d window."""
    res = _std(_slope_pct(_ratio(netinc, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_vol_slope_63d_v293_signal(ebt, assets):
    """Volatility of momentum for Pre-tax return on assets over 63d window."""
    res = _std(_slope_pct(_ratio(ebt, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_vol_slope_63d_v294_signal(netinc, ebt):
    """Volatility of momentum for Tax efficiency proxy over 63d window."""
    res = _std(_slope_pct(_ratio(netinc, ebt), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_vol_slope_126d_v295_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_vol_slope_126d_v296_signal(assets):
    """Volatility of momentum for Raw level of assets over 126d window."""
    res = _std(_slope_pct(assets, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_vol_slope_126d_v297_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 126d window."""
    res = _std(_slope_pct(ebt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_vol_slope_126d_v298_signal(netinc, assets):
    """Volatility of momentum for Net return on assets over 126d window."""
    res = _std(_slope_pct(_ratio(netinc, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_vol_slope_126d_v299_signal(ebt, assets):
    """Volatility of momentum for Pre-tax return on assets over 126d window."""
    res = _std(_slope_pct(_ratio(ebt, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_vol_slope_126d_v300_signal(netinc, ebt):
    """Volatility of momentum for Tax efficiency proxy over 126d window."""
    res = _std(_slope_pct(_ratio(netinc, ebt), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_nim_proxy_netinc_slope_diff_norm_42d_v151_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_42d_v151_signal},
    "f03_nim_proxy_assets_slope_diff_norm_42d_v152_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_42d_v152_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_42d_v153_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_42d_v153_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_42d_v154_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_42d_v154_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_42d_v155_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_42d_v155_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_42d_v156_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_42d_v156_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_63d_v157_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_63d_v157_signal},
    "f03_nim_proxy_assets_slope_diff_norm_63d_v158_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_63d_v158_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_63d_v159_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_63d_v159_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_63d_v160_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_63d_v160_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_63d_v161_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_63d_v161_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_63d_v162_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_63d_v162_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_126d_v163_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_126d_v163_signal},
    "f03_nim_proxy_assets_slope_diff_norm_126d_v164_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_126d_v164_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_126d_v165_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_126d_v165_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_126d_v166_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_126d_v166_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_126d_v167_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_126d_v167_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_126d_v168_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_126d_v168_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_252d_v169_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_252d_v169_signal},
    "f03_nim_proxy_assets_slope_diff_norm_252d_v170_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_252d_v170_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_252d_v171_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_252d_v171_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_252d_v172_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_252d_v172_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_252d_v173_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_252d_v173_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_252d_v174_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_252d_v174_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_504d_v175_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_504d_v175_signal},
    "f03_nim_proxy_assets_slope_diff_norm_504d_v176_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_504d_v176_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_504d_v177_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_504d_v177_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_504d_v178_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_504d_v178_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_504d_v179_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_504d_v179_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_504d_v180_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_504d_v180_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_756d_v181_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_756d_v181_signal},
    "f03_nim_proxy_assets_slope_diff_norm_756d_v182_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_756d_v182_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_756d_v183_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_756d_v183_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_756d_v184_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_756d_v184_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_756d_v185_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_756d_v185_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_756d_v186_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_756d_v186_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_1008d_v187_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_1008d_v187_signal},
    "f03_nim_proxy_assets_slope_diff_norm_1008d_v188_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_1008d_v188_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_1008d_v189_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_1008d_v189_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_1008d_v190_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_1008d_v190_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_1008d_v191_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_1008d_v191_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_1008d_v192_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_1008d_v192_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_1260d_v193_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_1260d_v193_signal},
    "f03_nim_proxy_assets_slope_diff_norm_1260d_v194_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_1260d_v194_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_1260d_v195_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_1260d_v195_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_1260d_v196_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_1260d_v196_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_1260d_v197_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_1260d_v197_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_1260d_v198_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_1260d_v198_signal},
    "f03_nim_proxy_netinc_mom_z_5d_v199_signal": {"func": f03_nim_proxy_netinc_mom_z_5d_v199_signal},
    "f03_nim_proxy_assets_mom_z_5d_v200_signal": {"func": f03_nim_proxy_assets_mom_z_5d_v200_signal},
    "f03_nim_proxy_ebt_mom_z_5d_v201_signal": {"func": f03_nim_proxy_ebt_mom_z_5d_v201_signal},
    "f03_nim_proxy_roa_net_mom_z_5d_v202_signal": {"func": f03_nim_proxy_roa_net_mom_z_5d_v202_signal},
    "f03_nim_proxy_roa_pretax_mom_z_5d_v203_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_5d_v203_signal},
    "f03_nim_proxy_tax_shield_mom_z_5d_v204_signal": {"func": f03_nim_proxy_tax_shield_mom_z_5d_v204_signal},
    "f03_nim_proxy_netinc_mom_z_10d_v205_signal": {"func": f03_nim_proxy_netinc_mom_z_10d_v205_signal},
    "f03_nim_proxy_assets_mom_z_10d_v206_signal": {"func": f03_nim_proxy_assets_mom_z_10d_v206_signal},
    "f03_nim_proxy_ebt_mom_z_10d_v207_signal": {"func": f03_nim_proxy_ebt_mom_z_10d_v207_signal},
    "f03_nim_proxy_roa_net_mom_z_10d_v208_signal": {"func": f03_nim_proxy_roa_net_mom_z_10d_v208_signal},
    "f03_nim_proxy_roa_pretax_mom_z_10d_v209_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_10d_v209_signal},
    "f03_nim_proxy_tax_shield_mom_z_10d_v210_signal": {"func": f03_nim_proxy_tax_shield_mom_z_10d_v210_signal},
    "f03_nim_proxy_netinc_mom_z_21d_v211_signal": {"func": f03_nim_proxy_netinc_mom_z_21d_v211_signal},
    "f03_nim_proxy_assets_mom_z_21d_v212_signal": {"func": f03_nim_proxy_assets_mom_z_21d_v212_signal},
    "f03_nim_proxy_ebt_mom_z_21d_v213_signal": {"func": f03_nim_proxy_ebt_mom_z_21d_v213_signal},
    "f03_nim_proxy_roa_net_mom_z_21d_v214_signal": {"func": f03_nim_proxy_roa_net_mom_z_21d_v214_signal},
    "f03_nim_proxy_roa_pretax_mom_z_21d_v215_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_21d_v215_signal},
    "f03_nim_proxy_tax_shield_mom_z_21d_v216_signal": {"func": f03_nim_proxy_tax_shield_mom_z_21d_v216_signal},
    "f03_nim_proxy_netinc_mom_z_42d_v217_signal": {"func": f03_nim_proxy_netinc_mom_z_42d_v217_signal},
    "f03_nim_proxy_assets_mom_z_42d_v218_signal": {"func": f03_nim_proxy_assets_mom_z_42d_v218_signal},
    "f03_nim_proxy_ebt_mom_z_42d_v219_signal": {"func": f03_nim_proxy_ebt_mom_z_42d_v219_signal},
    "f03_nim_proxy_roa_net_mom_z_42d_v220_signal": {"func": f03_nim_proxy_roa_net_mom_z_42d_v220_signal},
    "f03_nim_proxy_roa_pretax_mom_z_42d_v221_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_42d_v221_signal},
    "f03_nim_proxy_tax_shield_mom_z_42d_v222_signal": {"func": f03_nim_proxy_tax_shield_mom_z_42d_v222_signal},
    "f03_nim_proxy_netinc_mom_z_63d_v223_signal": {"func": f03_nim_proxy_netinc_mom_z_63d_v223_signal},
    "f03_nim_proxy_assets_mom_z_63d_v224_signal": {"func": f03_nim_proxy_assets_mom_z_63d_v224_signal},
    "f03_nim_proxy_ebt_mom_z_63d_v225_signal": {"func": f03_nim_proxy_ebt_mom_z_63d_v225_signal},
    "f03_nim_proxy_roa_net_mom_z_63d_v226_signal": {"func": f03_nim_proxy_roa_net_mom_z_63d_v226_signal},
    "f03_nim_proxy_roa_pretax_mom_z_63d_v227_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_63d_v227_signal},
    "f03_nim_proxy_tax_shield_mom_z_63d_v228_signal": {"func": f03_nim_proxy_tax_shield_mom_z_63d_v228_signal},
    "f03_nim_proxy_netinc_mom_z_126d_v229_signal": {"func": f03_nim_proxy_netinc_mom_z_126d_v229_signal},
    "f03_nim_proxy_assets_mom_z_126d_v230_signal": {"func": f03_nim_proxy_assets_mom_z_126d_v230_signal},
    "f03_nim_proxy_ebt_mom_z_126d_v231_signal": {"func": f03_nim_proxy_ebt_mom_z_126d_v231_signal},
    "f03_nim_proxy_roa_net_mom_z_126d_v232_signal": {"func": f03_nim_proxy_roa_net_mom_z_126d_v232_signal},
    "f03_nim_proxy_roa_pretax_mom_z_126d_v233_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_126d_v233_signal},
    "f03_nim_proxy_tax_shield_mom_z_126d_v234_signal": {"func": f03_nim_proxy_tax_shield_mom_z_126d_v234_signal},
    "f03_nim_proxy_netinc_mom_z_252d_v235_signal": {"func": f03_nim_proxy_netinc_mom_z_252d_v235_signal},
    "f03_nim_proxy_assets_mom_z_252d_v236_signal": {"func": f03_nim_proxy_assets_mom_z_252d_v236_signal},
    "f03_nim_proxy_ebt_mom_z_252d_v237_signal": {"func": f03_nim_proxy_ebt_mom_z_252d_v237_signal},
    "f03_nim_proxy_roa_net_mom_z_252d_v238_signal": {"func": f03_nim_proxy_roa_net_mom_z_252d_v238_signal},
    "f03_nim_proxy_roa_pretax_mom_z_252d_v239_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_252d_v239_signal},
    "f03_nim_proxy_tax_shield_mom_z_252d_v240_signal": {"func": f03_nim_proxy_tax_shield_mom_z_252d_v240_signal},
    "f03_nim_proxy_netinc_mom_z_504d_v241_signal": {"func": f03_nim_proxy_netinc_mom_z_504d_v241_signal},
    "f03_nim_proxy_assets_mom_z_504d_v242_signal": {"func": f03_nim_proxy_assets_mom_z_504d_v242_signal},
    "f03_nim_proxy_ebt_mom_z_504d_v243_signal": {"func": f03_nim_proxy_ebt_mom_z_504d_v243_signal},
    "f03_nim_proxy_roa_net_mom_z_504d_v244_signal": {"func": f03_nim_proxy_roa_net_mom_z_504d_v244_signal},
    "f03_nim_proxy_roa_pretax_mom_z_504d_v245_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_504d_v245_signal},
    "f03_nim_proxy_tax_shield_mom_z_504d_v246_signal": {"func": f03_nim_proxy_tax_shield_mom_z_504d_v246_signal},
    "f03_nim_proxy_netinc_mom_z_756d_v247_signal": {"func": f03_nim_proxy_netinc_mom_z_756d_v247_signal},
    "f03_nim_proxy_assets_mom_z_756d_v248_signal": {"func": f03_nim_proxy_assets_mom_z_756d_v248_signal},
    "f03_nim_proxy_ebt_mom_z_756d_v249_signal": {"func": f03_nim_proxy_ebt_mom_z_756d_v249_signal},
    "f03_nim_proxy_roa_net_mom_z_756d_v250_signal": {"func": f03_nim_proxy_roa_net_mom_z_756d_v250_signal},
    "f03_nim_proxy_roa_pretax_mom_z_756d_v251_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_756d_v251_signal},
    "f03_nim_proxy_tax_shield_mom_z_756d_v252_signal": {"func": f03_nim_proxy_tax_shield_mom_z_756d_v252_signal},
    "f03_nim_proxy_netinc_mom_z_1008d_v253_signal": {"func": f03_nim_proxy_netinc_mom_z_1008d_v253_signal},
    "f03_nim_proxy_assets_mom_z_1008d_v254_signal": {"func": f03_nim_proxy_assets_mom_z_1008d_v254_signal},
    "f03_nim_proxy_ebt_mom_z_1008d_v255_signal": {"func": f03_nim_proxy_ebt_mom_z_1008d_v255_signal},
    "f03_nim_proxy_roa_net_mom_z_1008d_v256_signal": {"func": f03_nim_proxy_roa_net_mom_z_1008d_v256_signal},
    "f03_nim_proxy_roa_pretax_mom_z_1008d_v257_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_1008d_v257_signal},
    "f03_nim_proxy_tax_shield_mom_z_1008d_v258_signal": {"func": f03_nim_proxy_tax_shield_mom_z_1008d_v258_signal},
    "f03_nim_proxy_netinc_mom_z_1260d_v259_signal": {"func": f03_nim_proxy_netinc_mom_z_1260d_v259_signal},
    "f03_nim_proxy_assets_mom_z_1260d_v260_signal": {"func": f03_nim_proxy_assets_mom_z_1260d_v260_signal},
    "f03_nim_proxy_ebt_mom_z_1260d_v261_signal": {"func": f03_nim_proxy_ebt_mom_z_1260d_v261_signal},
    "f03_nim_proxy_roa_net_mom_z_1260d_v262_signal": {"func": f03_nim_proxy_roa_net_mom_z_1260d_v262_signal},
    "f03_nim_proxy_roa_pretax_mom_z_1260d_v263_signal": {"func": f03_nim_proxy_roa_pretax_mom_z_1260d_v263_signal},
    "f03_nim_proxy_tax_shield_mom_z_1260d_v264_signal": {"func": f03_nim_proxy_tax_shield_mom_z_1260d_v264_signal},
    "f03_nim_proxy_netinc_vol_slope_5d_v265_signal": {"func": f03_nim_proxy_netinc_vol_slope_5d_v265_signal},
    "f03_nim_proxy_assets_vol_slope_5d_v266_signal": {"func": f03_nim_proxy_assets_vol_slope_5d_v266_signal},
    "f03_nim_proxy_ebt_vol_slope_5d_v267_signal": {"func": f03_nim_proxy_ebt_vol_slope_5d_v267_signal},
    "f03_nim_proxy_roa_net_vol_slope_5d_v268_signal": {"func": f03_nim_proxy_roa_net_vol_slope_5d_v268_signal},
    "f03_nim_proxy_roa_pretax_vol_slope_5d_v269_signal": {"func": f03_nim_proxy_roa_pretax_vol_slope_5d_v269_signal},
    "f03_nim_proxy_tax_shield_vol_slope_5d_v270_signal": {"func": f03_nim_proxy_tax_shield_vol_slope_5d_v270_signal},
    "f03_nim_proxy_netinc_vol_slope_10d_v271_signal": {"func": f03_nim_proxy_netinc_vol_slope_10d_v271_signal},
    "f03_nim_proxy_assets_vol_slope_10d_v272_signal": {"func": f03_nim_proxy_assets_vol_slope_10d_v272_signal},
    "f03_nim_proxy_ebt_vol_slope_10d_v273_signal": {"func": f03_nim_proxy_ebt_vol_slope_10d_v273_signal},
    "f03_nim_proxy_roa_net_vol_slope_10d_v274_signal": {"func": f03_nim_proxy_roa_net_vol_slope_10d_v274_signal},
    "f03_nim_proxy_roa_pretax_vol_slope_10d_v275_signal": {"func": f03_nim_proxy_roa_pretax_vol_slope_10d_v275_signal},
    "f03_nim_proxy_tax_shield_vol_slope_10d_v276_signal": {"func": f03_nim_proxy_tax_shield_vol_slope_10d_v276_signal},
    "f03_nim_proxy_netinc_vol_slope_21d_v277_signal": {"func": f03_nim_proxy_netinc_vol_slope_21d_v277_signal},
    "f03_nim_proxy_assets_vol_slope_21d_v278_signal": {"func": f03_nim_proxy_assets_vol_slope_21d_v278_signal},
    "f03_nim_proxy_ebt_vol_slope_21d_v279_signal": {"func": f03_nim_proxy_ebt_vol_slope_21d_v279_signal},
    "f03_nim_proxy_roa_net_vol_slope_21d_v280_signal": {"func": f03_nim_proxy_roa_net_vol_slope_21d_v280_signal},
    "f03_nim_proxy_roa_pretax_vol_slope_21d_v281_signal": {"func": f03_nim_proxy_roa_pretax_vol_slope_21d_v281_signal},
    "f03_nim_proxy_tax_shield_vol_slope_21d_v282_signal": {"func": f03_nim_proxy_tax_shield_vol_slope_21d_v282_signal},
    "f03_nim_proxy_netinc_vol_slope_42d_v283_signal": {"func": f03_nim_proxy_netinc_vol_slope_42d_v283_signal},
    "f03_nim_proxy_assets_vol_slope_42d_v284_signal": {"func": f03_nim_proxy_assets_vol_slope_42d_v284_signal},
    "f03_nim_proxy_ebt_vol_slope_42d_v285_signal": {"func": f03_nim_proxy_ebt_vol_slope_42d_v285_signal},
    "f03_nim_proxy_roa_net_vol_slope_42d_v286_signal": {"func": f03_nim_proxy_roa_net_vol_slope_42d_v286_signal},
    "f03_nim_proxy_roa_pretax_vol_slope_42d_v287_signal": {"func": f03_nim_proxy_roa_pretax_vol_slope_42d_v287_signal},
    "f03_nim_proxy_tax_shield_vol_slope_42d_v288_signal": {"func": f03_nim_proxy_tax_shield_vol_slope_42d_v288_signal},
    "f03_nim_proxy_netinc_vol_slope_63d_v289_signal": {"func": f03_nim_proxy_netinc_vol_slope_63d_v289_signal},
    "f03_nim_proxy_assets_vol_slope_63d_v290_signal": {"func": f03_nim_proxy_assets_vol_slope_63d_v290_signal},
    "f03_nim_proxy_ebt_vol_slope_63d_v291_signal": {"func": f03_nim_proxy_ebt_vol_slope_63d_v291_signal},
    "f03_nim_proxy_roa_net_vol_slope_63d_v292_signal": {"func": f03_nim_proxy_roa_net_vol_slope_63d_v292_signal},
    "f03_nim_proxy_roa_pretax_vol_slope_63d_v293_signal": {"func": f03_nim_proxy_roa_pretax_vol_slope_63d_v293_signal},
    "f03_nim_proxy_tax_shield_vol_slope_63d_v294_signal": {"func": f03_nim_proxy_tax_shield_vol_slope_63d_v294_signal},
    "f03_nim_proxy_netinc_vol_slope_126d_v295_signal": {"func": f03_nim_proxy_netinc_vol_slope_126d_v295_signal},
    "f03_nim_proxy_assets_vol_slope_126d_v296_signal": {"func": f03_nim_proxy_assets_vol_slope_126d_v296_signal},
    "f03_nim_proxy_ebt_vol_slope_126d_v297_signal": {"func": f03_nim_proxy_ebt_vol_slope_126d_v297_signal},
    "f03_nim_proxy_roa_net_vol_slope_126d_v298_signal": {"func": f03_nim_proxy_roa_net_vol_slope_126d_v298_signal},
    "f03_nim_proxy_roa_pretax_vol_slope_126d_v299_signal": {"func": f03_nim_proxy_roa_pretax_vol_slope_126d_v299_signal},
    "f03_nim_proxy_tax_shield_vol_slope_126d_v300_signal": {"func": f03_nim_proxy_tax_shield_vol_slope_126d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
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
