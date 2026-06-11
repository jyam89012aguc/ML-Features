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

def f03_nim_proxy_netinc_slope_pct_5d_v001_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_5d_v003_signal(ebt):
    """Percentage slope for Raw level of ebt over 5d window."""
    res = _slope_pct(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_5d_v004_signal(netinc, assets):
    """Percentage slope for Net return on assets over 5d window."""
    res = _slope_pct(_ratio(netinc, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_5d_v005_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 5d window."""
    res = _slope_pct(_ratio(ebt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_5d_v006_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 5d window."""
    res = _slope_pct(_ratio(netinc, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_10d_v007_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_10d_v008_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_10d_v009_signal(ebt):
    """Percentage slope for Raw level of ebt over 10d window."""
    res = _slope_pct(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_10d_v010_signal(netinc, assets):
    """Percentage slope for Net return on assets over 10d window."""
    res = _slope_pct(_ratio(netinc, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_10d_v011_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 10d window."""
    res = _slope_pct(_ratio(ebt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_10d_v012_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 10d window."""
    res = _slope_pct(_ratio(netinc, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_21d_v013_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_21d_v014_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_21d_v015_signal(ebt):
    """Percentage slope for Raw level of ebt over 21d window."""
    res = _slope_pct(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_21d_v016_signal(netinc, assets):
    """Percentage slope for Net return on assets over 21d window."""
    res = _slope_pct(_ratio(netinc, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_21d_v017_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 21d window."""
    res = _slope_pct(_ratio(ebt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_21d_v018_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 21d window."""
    res = _slope_pct(_ratio(netinc, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_42d_v019_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_42d_v020_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_42d_v021_signal(ebt):
    """Percentage slope for Raw level of ebt over 42d window."""
    res = _slope_pct(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_42d_v022_signal(netinc, assets):
    """Percentage slope for Net return on assets over 42d window."""
    res = _slope_pct(_ratio(netinc, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_42d_v023_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 42d window."""
    res = _slope_pct(_ratio(ebt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_42d_v024_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 42d window."""
    res = _slope_pct(_ratio(netinc, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_63d_v025_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_63d_v026_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_63d_v027_signal(ebt):
    """Percentage slope for Raw level of ebt over 63d window."""
    res = _slope_pct(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_63d_v028_signal(netinc, assets):
    """Percentage slope for Net return on assets over 63d window."""
    res = _slope_pct(_ratio(netinc, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_63d_v029_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 63d window."""
    res = _slope_pct(_ratio(ebt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_63d_v030_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 63d window."""
    res = _slope_pct(_ratio(netinc, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_126d_v031_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_126d_v032_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_126d_v033_signal(ebt):
    """Percentage slope for Raw level of ebt over 126d window."""
    res = _slope_pct(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_126d_v034_signal(netinc, assets):
    """Percentage slope for Net return on assets over 126d window."""
    res = _slope_pct(_ratio(netinc, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_126d_v035_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 126d window."""
    res = _slope_pct(_ratio(ebt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_126d_v036_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 126d window."""
    res = _slope_pct(_ratio(netinc, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_252d_v037_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_252d_v038_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_252d_v039_signal(ebt):
    """Percentage slope for Raw level of ebt over 252d window."""
    res = _slope_pct(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_252d_v040_signal(netinc, assets):
    """Percentage slope for Net return on assets over 252d window."""
    res = _slope_pct(_ratio(netinc, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_252d_v041_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 252d window."""
    res = _slope_pct(_ratio(ebt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_252d_v042_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 252d window."""
    res = _slope_pct(_ratio(netinc, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_504d_v043_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_504d_v044_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_504d_v045_signal(ebt):
    """Percentage slope for Raw level of ebt over 504d window."""
    res = _slope_pct(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_504d_v046_signal(netinc, assets):
    """Percentage slope for Net return on assets over 504d window."""
    res = _slope_pct(_ratio(netinc, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_504d_v047_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 504d window."""
    res = _slope_pct(_ratio(ebt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_504d_v048_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 504d window."""
    res = _slope_pct(_ratio(netinc, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_756d_v049_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_756d_v050_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_756d_v051_signal(ebt):
    """Percentage slope for Raw level of ebt over 756d window."""
    res = _slope_pct(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_756d_v052_signal(netinc, assets):
    """Percentage slope for Net return on assets over 756d window."""
    res = _slope_pct(_ratio(netinc, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_756d_v053_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 756d window."""
    res = _slope_pct(_ratio(ebt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_756d_v054_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 756d window."""
    res = _slope_pct(_ratio(netinc, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_1008d_v055_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_1008d_v056_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_1008d_v057_signal(ebt):
    """Percentage slope for Raw level of ebt over 1008d window."""
    res = _slope_pct(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_1008d_v058_signal(netinc, assets):
    """Percentage slope for Net return on assets over 1008d window."""
    res = _slope_pct(_ratio(netinc, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_1008d_v059_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 1008d window."""
    res = _slope_pct(_ratio(ebt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_1008d_v060_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 1008d window."""
    res = _slope_pct(_ratio(netinc, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_pct_1260d_v061_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_pct_1260d_v062_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_pct_1260d_v063_signal(ebt):
    """Percentage slope for Raw level of ebt over 1260d window."""
    res = _slope_pct(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_pct_1260d_v064_signal(netinc, assets):
    """Percentage slope for Net return on assets over 1260d window."""
    res = _slope_pct(_ratio(netinc, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_pct_1260d_v065_signal(ebt, assets):
    """Percentage slope for Pre-tax return on assets over 1260d window."""
    res = _slope_pct(_ratio(ebt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_pct_1260d_v066_signal(netinc, ebt):
    """Percentage slope for Tax efficiency proxy over 1260d window."""
    res = _slope_pct(_ratio(netinc, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_5d_v067_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_5d_v068_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_5d_v069_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 5d window."""
    res = _jerk(ebt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_5d_v070_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 5d window."""
    res = _jerk(_ratio(netinc, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_5d_v071_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 5d window."""
    res = _jerk(_ratio(ebt, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_5d_v072_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 5d window."""
    res = _jerk(_ratio(netinc, ebt), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_10d_v073_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_10d_v074_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_10d_v075_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 10d window."""
    res = _jerk(ebt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_10d_v076_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 10d window."""
    res = _jerk(_ratio(netinc, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_10d_v077_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 10d window."""
    res = _jerk(_ratio(ebt, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_10d_v078_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 10d window."""
    res = _jerk(_ratio(netinc, ebt), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_21d_v079_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_21d_v080_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_21d_v081_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 21d window."""
    res = _jerk(ebt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_21d_v082_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 21d window."""
    res = _jerk(_ratio(netinc, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_21d_v083_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 21d window."""
    res = _jerk(_ratio(ebt, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_21d_v084_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 21d window."""
    res = _jerk(_ratio(netinc, ebt), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_42d_v085_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_42d_v086_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_42d_v087_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 42d window."""
    res = _jerk(ebt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_42d_v088_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 42d window."""
    res = _jerk(_ratio(netinc, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_42d_v089_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 42d window."""
    res = _jerk(_ratio(ebt, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_42d_v090_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 42d window."""
    res = _jerk(_ratio(netinc, ebt), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_63d_v091_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_63d_v092_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_63d_v093_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 63d window."""
    res = _jerk(ebt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_63d_v094_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 63d window."""
    res = _jerk(_ratio(netinc, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_63d_v095_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 63d window."""
    res = _jerk(_ratio(ebt, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_63d_v096_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 63d window."""
    res = _jerk(_ratio(netinc, ebt), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_126d_v097_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_126d_v098_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_126d_v099_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 126d window."""
    res = _jerk(ebt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_126d_v100_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 126d window."""
    res = _jerk(_ratio(netinc, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_126d_v101_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 126d window."""
    res = _jerk(_ratio(ebt, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_126d_v102_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 126d window."""
    res = _jerk(_ratio(netinc, ebt), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_252d_v103_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_252d_v104_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_252d_v105_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 252d window."""
    res = _jerk(ebt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_252d_v106_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 252d window."""
    res = _jerk(_ratio(netinc, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_252d_v107_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 252d window."""
    res = _jerk(_ratio(ebt, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_252d_v108_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 252d window."""
    res = _jerk(_ratio(netinc, ebt), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_504d_v109_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_504d_v110_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_504d_v111_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 504d window."""
    res = _jerk(ebt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_504d_v112_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 504d window."""
    res = _jerk(_ratio(netinc, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_504d_v113_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 504d window."""
    res = _jerk(_ratio(ebt, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_504d_v114_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 504d window."""
    res = _jerk(_ratio(netinc, ebt), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_756d_v115_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_756d_v116_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_756d_v117_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 756d window."""
    res = _jerk(ebt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_756d_v118_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 756d window."""
    res = _jerk(_ratio(netinc, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_756d_v119_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 756d window."""
    res = _jerk(_ratio(ebt, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_756d_v120_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 756d window."""
    res = _jerk(_ratio(netinc, ebt), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_1008d_v121_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_1008d_v122_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_1008d_v123_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 1008d window."""
    res = _jerk(ebt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_1008d_v124_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 1008d window."""
    res = _jerk(_ratio(netinc, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_1008d_v125_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 1008d window."""
    res = _jerk(_ratio(ebt, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_1008d_v126_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 1008d window."""
    res = _jerk(_ratio(netinc, ebt), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_jerk_1260d_v127_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_jerk_1260d_v128_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_jerk_1260d_v129_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 1260d window."""
    res = _jerk(ebt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_jerk_1260d_v130_signal(netinc, assets):
    """Acceleration/Jerk for Net return on assets over 1260d window."""
    res = _jerk(_ratio(netinc, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_jerk_1260d_v131_signal(ebt, assets):
    """Acceleration/Jerk for Pre-tax return on assets over 1260d window."""
    res = _jerk(_ratio(ebt, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_jerk_1260d_v132_signal(netinc, ebt):
    """Acceleration/Jerk for Tax efficiency proxy over 1260d window."""
    res = _jerk(_ratio(netinc, ebt), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_5d_v133_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_5d_v134_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_5d_v135_signal(ebt):
    """Normalized slope change for Raw level of ebt over 5d window."""
    res = (_slope_pct(ebt, 5).diff(5) / _sma(ebt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_5d_v136_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 5d window."""
    res = (_slope_pct(_ratio(netinc, assets), 5).diff(5) / _sma(_ratio(netinc, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_5d_v137_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 5d window."""
    res = (_slope_pct(_ratio(ebt, assets), 5).diff(5) / _sma(_ratio(ebt, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_5d_v138_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 5d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 5).diff(5) / _sma(_ratio(netinc, ebt).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_10d_v139_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_10d_v140_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_10d_v141_signal(ebt):
    """Normalized slope change for Raw level of ebt over 10d window."""
    res = (_slope_pct(ebt, 10).diff(10) / _sma(ebt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_10d_v142_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 10d window."""
    res = (_slope_pct(_ratio(netinc, assets), 10).diff(10) / _sma(_ratio(netinc, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_10d_v143_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 10d window."""
    res = (_slope_pct(_ratio(ebt, assets), 10).diff(10) / _sma(_ratio(ebt, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_10d_v144_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 10d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 10).diff(10) / _sma(_ratio(netinc, ebt).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_slope_diff_norm_21d_v145_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_slope_diff_norm_21d_v146_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_slope_diff_norm_21d_v147_signal(ebt):
    """Normalized slope change for Raw level of ebt over 21d window."""
    res = (_slope_pct(ebt, 21).diff(21) / _sma(ebt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_slope_diff_norm_21d_v148_signal(netinc, assets):
    """Normalized slope change for Net return on assets over 21d window."""
    res = (_slope_pct(_ratio(netinc, assets), 21).diff(21) / _sma(_ratio(netinc, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_slope_diff_norm_21d_v149_signal(ebt, assets):
    """Normalized slope change for Pre-tax return on assets over 21d window."""
    res = (_slope_pct(_ratio(ebt, assets), 21).diff(21) / _sma(_ratio(ebt, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_slope_diff_norm_21d_v150_signal(netinc, ebt):
    """Normalized slope change for Tax efficiency proxy over 21d window."""
    res = (_slope_pct(_ratio(netinc, ebt), 21).diff(21) / _sma(_ratio(netinc, ebt).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_nim_proxy_netinc_slope_pct_5d_v001_signal": {"func": f03_nim_proxy_netinc_slope_pct_5d_v001_signal},
    "f03_nim_proxy_assets_slope_pct_5d_v002_signal": {"func": f03_nim_proxy_assets_slope_pct_5d_v002_signal},
    "f03_nim_proxy_ebt_slope_pct_5d_v003_signal": {"func": f03_nim_proxy_ebt_slope_pct_5d_v003_signal},
    "f03_nim_proxy_roa_net_slope_pct_5d_v004_signal": {"func": f03_nim_proxy_roa_net_slope_pct_5d_v004_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_5d_v005_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_5d_v005_signal},
    "f03_nim_proxy_tax_shield_slope_pct_5d_v006_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_5d_v006_signal},
    "f03_nim_proxy_netinc_slope_pct_10d_v007_signal": {"func": f03_nim_proxy_netinc_slope_pct_10d_v007_signal},
    "f03_nim_proxy_assets_slope_pct_10d_v008_signal": {"func": f03_nim_proxy_assets_slope_pct_10d_v008_signal},
    "f03_nim_proxy_ebt_slope_pct_10d_v009_signal": {"func": f03_nim_proxy_ebt_slope_pct_10d_v009_signal},
    "f03_nim_proxy_roa_net_slope_pct_10d_v010_signal": {"func": f03_nim_proxy_roa_net_slope_pct_10d_v010_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_10d_v011_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_10d_v011_signal},
    "f03_nim_proxy_tax_shield_slope_pct_10d_v012_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_10d_v012_signal},
    "f03_nim_proxy_netinc_slope_pct_21d_v013_signal": {"func": f03_nim_proxy_netinc_slope_pct_21d_v013_signal},
    "f03_nim_proxy_assets_slope_pct_21d_v014_signal": {"func": f03_nim_proxy_assets_slope_pct_21d_v014_signal},
    "f03_nim_proxy_ebt_slope_pct_21d_v015_signal": {"func": f03_nim_proxy_ebt_slope_pct_21d_v015_signal},
    "f03_nim_proxy_roa_net_slope_pct_21d_v016_signal": {"func": f03_nim_proxy_roa_net_slope_pct_21d_v016_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_21d_v017_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_21d_v017_signal},
    "f03_nim_proxy_tax_shield_slope_pct_21d_v018_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_21d_v018_signal},
    "f03_nim_proxy_netinc_slope_pct_42d_v019_signal": {"func": f03_nim_proxy_netinc_slope_pct_42d_v019_signal},
    "f03_nim_proxy_assets_slope_pct_42d_v020_signal": {"func": f03_nim_proxy_assets_slope_pct_42d_v020_signal},
    "f03_nim_proxy_ebt_slope_pct_42d_v021_signal": {"func": f03_nim_proxy_ebt_slope_pct_42d_v021_signal},
    "f03_nim_proxy_roa_net_slope_pct_42d_v022_signal": {"func": f03_nim_proxy_roa_net_slope_pct_42d_v022_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_42d_v023_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_42d_v023_signal},
    "f03_nim_proxy_tax_shield_slope_pct_42d_v024_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_42d_v024_signal},
    "f03_nim_proxy_netinc_slope_pct_63d_v025_signal": {"func": f03_nim_proxy_netinc_slope_pct_63d_v025_signal},
    "f03_nim_proxy_assets_slope_pct_63d_v026_signal": {"func": f03_nim_proxy_assets_slope_pct_63d_v026_signal},
    "f03_nim_proxy_ebt_slope_pct_63d_v027_signal": {"func": f03_nim_proxy_ebt_slope_pct_63d_v027_signal},
    "f03_nim_proxy_roa_net_slope_pct_63d_v028_signal": {"func": f03_nim_proxy_roa_net_slope_pct_63d_v028_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_63d_v029_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_63d_v029_signal},
    "f03_nim_proxy_tax_shield_slope_pct_63d_v030_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_63d_v030_signal},
    "f03_nim_proxy_netinc_slope_pct_126d_v031_signal": {"func": f03_nim_proxy_netinc_slope_pct_126d_v031_signal},
    "f03_nim_proxy_assets_slope_pct_126d_v032_signal": {"func": f03_nim_proxy_assets_slope_pct_126d_v032_signal},
    "f03_nim_proxy_ebt_slope_pct_126d_v033_signal": {"func": f03_nim_proxy_ebt_slope_pct_126d_v033_signal},
    "f03_nim_proxy_roa_net_slope_pct_126d_v034_signal": {"func": f03_nim_proxy_roa_net_slope_pct_126d_v034_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_126d_v035_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_126d_v035_signal},
    "f03_nim_proxy_tax_shield_slope_pct_126d_v036_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_126d_v036_signal},
    "f03_nim_proxy_netinc_slope_pct_252d_v037_signal": {"func": f03_nim_proxy_netinc_slope_pct_252d_v037_signal},
    "f03_nim_proxy_assets_slope_pct_252d_v038_signal": {"func": f03_nim_proxy_assets_slope_pct_252d_v038_signal},
    "f03_nim_proxy_ebt_slope_pct_252d_v039_signal": {"func": f03_nim_proxy_ebt_slope_pct_252d_v039_signal},
    "f03_nim_proxy_roa_net_slope_pct_252d_v040_signal": {"func": f03_nim_proxy_roa_net_slope_pct_252d_v040_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_252d_v041_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_252d_v041_signal},
    "f03_nim_proxy_tax_shield_slope_pct_252d_v042_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_252d_v042_signal},
    "f03_nim_proxy_netinc_slope_pct_504d_v043_signal": {"func": f03_nim_proxy_netinc_slope_pct_504d_v043_signal},
    "f03_nim_proxy_assets_slope_pct_504d_v044_signal": {"func": f03_nim_proxy_assets_slope_pct_504d_v044_signal},
    "f03_nim_proxy_ebt_slope_pct_504d_v045_signal": {"func": f03_nim_proxy_ebt_slope_pct_504d_v045_signal},
    "f03_nim_proxy_roa_net_slope_pct_504d_v046_signal": {"func": f03_nim_proxy_roa_net_slope_pct_504d_v046_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_504d_v047_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_504d_v047_signal},
    "f03_nim_proxy_tax_shield_slope_pct_504d_v048_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_504d_v048_signal},
    "f03_nim_proxy_netinc_slope_pct_756d_v049_signal": {"func": f03_nim_proxy_netinc_slope_pct_756d_v049_signal},
    "f03_nim_proxy_assets_slope_pct_756d_v050_signal": {"func": f03_nim_proxy_assets_slope_pct_756d_v050_signal},
    "f03_nim_proxy_ebt_slope_pct_756d_v051_signal": {"func": f03_nim_proxy_ebt_slope_pct_756d_v051_signal},
    "f03_nim_proxy_roa_net_slope_pct_756d_v052_signal": {"func": f03_nim_proxy_roa_net_slope_pct_756d_v052_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_756d_v053_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_756d_v053_signal},
    "f03_nim_proxy_tax_shield_slope_pct_756d_v054_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_756d_v054_signal},
    "f03_nim_proxy_netinc_slope_pct_1008d_v055_signal": {"func": f03_nim_proxy_netinc_slope_pct_1008d_v055_signal},
    "f03_nim_proxy_assets_slope_pct_1008d_v056_signal": {"func": f03_nim_proxy_assets_slope_pct_1008d_v056_signal},
    "f03_nim_proxy_ebt_slope_pct_1008d_v057_signal": {"func": f03_nim_proxy_ebt_slope_pct_1008d_v057_signal},
    "f03_nim_proxy_roa_net_slope_pct_1008d_v058_signal": {"func": f03_nim_proxy_roa_net_slope_pct_1008d_v058_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_1008d_v059_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_1008d_v059_signal},
    "f03_nim_proxy_tax_shield_slope_pct_1008d_v060_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_1008d_v060_signal},
    "f03_nim_proxy_netinc_slope_pct_1260d_v061_signal": {"func": f03_nim_proxy_netinc_slope_pct_1260d_v061_signal},
    "f03_nim_proxy_assets_slope_pct_1260d_v062_signal": {"func": f03_nim_proxy_assets_slope_pct_1260d_v062_signal},
    "f03_nim_proxy_ebt_slope_pct_1260d_v063_signal": {"func": f03_nim_proxy_ebt_slope_pct_1260d_v063_signal},
    "f03_nim_proxy_roa_net_slope_pct_1260d_v064_signal": {"func": f03_nim_proxy_roa_net_slope_pct_1260d_v064_signal},
    "f03_nim_proxy_roa_pretax_slope_pct_1260d_v065_signal": {"func": f03_nim_proxy_roa_pretax_slope_pct_1260d_v065_signal},
    "f03_nim_proxy_tax_shield_slope_pct_1260d_v066_signal": {"func": f03_nim_proxy_tax_shield_slope_pct_1260d_v066_signal},
    "f03_nim_proxy_netinc_jerk_5d_v067_signal": {"func": f03_nim_proxy_netinc_jerk_5d_v067_signal},
    "f03_nim_proxy_assets_jerk_5d_v068_signal": {"func": f03_nim_proxy_assets_jerk_5d_v068_signal},
    "f03_nim_proxy_ebt_jerk_5d_v069_signal": {"func": f03_nim_proxy_ebt_jerk_5d_v069_signal},
    "f03_nim_proxy_roa_net_jerk_5d_v070_signal": {"func": f03_nim_proxy_roa_net_jerk_5d_v070_signal},
    "f03_nim_proxy_roa_pretax_jerk_5d_v071_signal": {"func": f03_nim_proxy_roa_pretax_jerk_5d_v071_signal},
    "f03_nim_proxy_tax_shield_jerk_5d_v072_signal": {"func": f03_nim_proxy_tax_shield_jerk_5d_v072_signal},
    "f03_nim_proxy_netinc_jerk_10d_v073_signal": {"func": f03_nim_proxy_netinc_jerk_10d_v073_signal},
    "f03_nim_proxy_assets_jerk_10d_v074_signal": {"func": f03_nim_proxy_assets_jerk_10d_v074_signal},
    "f03_nim_proxy_ebt_jerk_10d_v075_signal": {"func": f03_nim_proxy_ebt_jerk_10d_v075_signal},
    "f03_nim_proxy_roa_net_jerk_10d_v076_signal": {"func": f03_nim_proxy_roa_net_jerk_10d_v076_signal},
    "f03_nim_proxy_roa_pretax_jerk_10d_v077_signal": {"func": f03_nim_proxy_roa_pretax_jerk_10d_v077_signal},
    "f03_nim_proxy_tax_shield_jerk_10d_v078_signal": {"func": f03_nim_proxy_tax_shield_jerk_10d_v078_signal},
    "f03_nim_proxy_netinc_jerk_21d_v079_signal": {"func": f03_nim_proxy_netinc_jerk_21d_v079_signal},
    "f03_nim_proxy_assets_jerk_21d_v080_signal": {"func": f03_nim_proxy_assets_jerk_21d_v080_signal},
    "f03_nim_proxy_ebt_jerk_21d_v081_signal": {"func": f03_nim_proxy_ebt_jerk_21d_v081_signal},
    "f03_nim_proxy_roa_net_jerk_21d_v082_signal": {"func": f03_nim_proxy_roa_net_jerk_21d_v082_signal},
    "f03_nim_proxy_roa_pretax_jerk_21d_v083_signal": {"func": f03_nim_proxy_roa_pretax_jerk_21d_v083_signal},
    "f03_nim_proxy_tax_shield_jerk_21d_v084_signal": {"func": f03_nim_proxy_tax_shield_jerk_21d_v084_signal},
    "f03_nim_proxy_netinc_jerk_42d_v085_signal": {"func": f03_nim_proxy_netinc_jerk_42d_v085_signal},
    "f03_nim_proxy_assets_jerk_42d_v086_signal": {"func": f03_nim_proxy_assets_jerk_42d_v086_signal},
    "f03_nim_proxy_ebt_jerk_42d_v087_signal": {"func": f03_nim_proxy_ebt_jerk_42d_v087_signal},
    "f03_nim_proxy_roa_net_jerk_42d_v088_signal": {"func": f03_nim_proxy_roa_net_jerk_42d_v088_signal},
    "f03_nim_proxy_roa_pretax_jerk_42d_v089_signal": {"func": f03_nim_proxy_roa_pretax_jerk_42d_v089_signal},
    "f03_nim_proxy_tax_shield_jerk_42d_v090_signal": {"func": f03_nim_proxy_tax_shield_jerk_42d_v090_signal},
    "f03_nim_proxy_netinc_jerk_63d_v091_signal": {"func": f03_nim_proxy_netinc_jerk_63d_v091_signal},
    "f03_nim_proxy_assets_jerk_63d_v092_signal": {"func": f03_nim_proxy_assets_jerk_63d_v092_signal},
    "f03_nim_proxy_ebt_jerk_63d_v093_signal": {"func": f03_nim_proxy_ebt_jerk_63d_v093_signal},
    "f03_nim_proxy_roa_net_jerk_63d_v094_signal": {"func": f03_nim_proxy_roa_net_jerk_63d_v094_signal},
    "f03_nim_proxy_roa_pretax_jerk_63d_v095_signal": {"func": f03_nim_proxy_roa_pretax_jerk_63d_v095_signal},
    "f03_nim_proxy_tax_shield_jerk_63d_v096_signal": {"func": f03_nim_proxy_tax_shield_jerk_63d_v096_signal},
    "f03_nim_proxy_netinc_jerk_126d_v097_signal": {"func": f03_nim_proxy_netinc_jerk_126d_v097_signal},
    "f03_nim_proxy_assets_jerk_126d_v098_signal": {"func": f03_nim_proxy_assets_jerk_126d_v098_signal},
    "f03_nim_proxy_ebt_jerk_126d_v099_signal": {"func": f03_nim_proxy_ebt_jerk_126d_v099_signal},
    "f03_nim_proxy_roa_net_jerk_126d_v100_signal": {"func": f03_nim_proxy_roa_net_jerk_126d_v100_signal},
    "f03_nim_proxy_roa_pretax_jerk_126d_v101_signal": {"func": f03_nim_proxy_roa_pretax_jerk_126d_v101_signal},
    "f03_nim_proxy_tax_shield_jerk_126d_v102_signal": {"func": f03_nim_proxy_tax_shield_jerk_126d_v102_signal},
    "f03_nim_proxy_netinc_jerk_252d_v103_signal": {"func": f03_nim_proxy_netinc_jerk_252d_v103_signal},
    "f03_nim_proxy_assets_jerk_252d_v104_signal": {"func": f03_nim_proxy_assets_jerk_252d_v104_signal},
    "f03_nim_proxy_ebt_jerk_252d_v105_signal": {"func": f03_nim_proxy_ebt_jerk_252d_v105_signal},
    "f03_nim_proxy_roa_net_jerk_252d_v106_signal": {"func": f03_nim_proxy_roa_net_jerk_252d_v106_signal},
    "f03_nim_proxy_roa_pretax_jerk_252d_v107_signal": {"func": f03_nim_proxy_roa_pretax_jerk_252d_v107_signal},
    "f03_nim_proxy_tax_shield_jerk_252d_v108_signal": {"func": f03_nim_proxy_tax_shield_jerk_252d_v108_signal},
    "f03_nim_proxy_netinc_jerk_504d_v109_signal": {"func": f03_nim_proxy_netinc_jerk_504d_v109_signal},
    "f03_nim_proxy_assets_jerk_504d_v110_signal": {"func": f03_nim_proxy_assets_jerk_504d_v110_signal},
    "f03_nim_proxy_ebt_jerk_504d_v111_signal": {"func": f03_nim_proxy_ebt_jerk_504d_v111_signal},
    "f03_nim_proxy_roa_net_jerk_504d_v112_signal": {"func": f03_nim_proxy_roa_net_jerk_504d_v112_signal},
    "f03_nim_proxy_roa_pretax_jerk_504d_v113_signal": {"func": f03_nim_proxy_roa_pretax_jerk_504d_v113_signal},
    "f03_nim_proxy_tax_shield_jerk_504d_v114_signal": {"func": f03_nim_proxy_tax_shield_jerk_504d_v114_signal},
    "f03_nim_proxy_netinc_jerk_756d_v115_signal": {"func": f03_nim_proxy_netinc_jerk_756d_v115_signal},
    "f03_nim_proxy_assets_jerk_756d_v116_signal": {"func": f03_nim_proxy_assets_jerk_756d_v116_signal},
    "f03_nim_proxy_ebt_jerk_756d_v117_signal": {"func": f03_nim_proxy_ebt_jerk_756d_v117_signal},
    "f03_nim_proxy_roa_net_jerk_756d_v118_signal": {"func": f03_nim_proxy_roa_net_jerk_756d_v118_signal},
    "f03_nim_proxy_roa_pretax_jerk_756d_v119_signal": {"func": f03_nim_proxy_roa_pretax_jerk_756d_v119_signal},
    "f03_nim_proxy_tax_shield_jerk_756d_v120_signal": {"func": f03_nim_proxy_tax_shield_jerk_756d_v120_signal},
    "f03_nim_proxy_netinc_jerk_1008d_v121_signal": {"func": f03_nim_proxy_netinc_jerk_1008d_v121_signal},
    "f03_nim_proxy_assets_jerk_1008d_v122_signal": {"func": f03_nim_proxy_assets_jerk_1008d_v122_signal},
    "f03_nim_proxy_ebt_jerk_1008d_v123_signal": {"func": f03_nim_proxy_ebt_jerk_1008d_v123_signal},
    "f03_nim_proxy_roa_net_jerk_1008d_v124_signal": {"func": f03_nim_proxy_roa_net_jerk_1008d_v124_signal},
    "f03_nim_proxy_roa_pretax_jerk_1008d_v125_signal": {"func": f03_nim_proxy_roa_pretax_jerk_1008d_v125_signal},
    "f03_nim_proxy_tax_shield_jerk_1008d_v126_signal": {"func": f03_nim_proxy_tax_shield_jerk_1008d_v126_signal},
    "f03_nim_proxy_netinc_jerk_1260d_v127_signal": {"func": f03_nim_proxy_netinc_jerk_1260d_v127_signal},
    "f03_nim_proxy_assets_jerk_1260d_v128_signal": {"func": f03_nim_proxy_assets_jerk_1260d_v128_signal},
    "f03_nim_proxy_ebt_jerk_1260d_v129_signal": {"func": f03_nim_proxy_ebt_jerk_1260d_v129_signal},
    "f03_nim_proxy_roa_net_jerk_1260d_v130_signal": {"func": f03_nim_proxy_roa_net_jerk_1260d_v130_signal},
    "f03_nim_proxy_roa_pretax_jerk_1260d_v131_signal": {"func": f03_nim_proxy_roa_pretax_jerk_1260d_v131_signal},
    "f03_nim_proxy_tax_shield_jerk_1260d_v132_signal": {"func": f03_nim_proxy_tax_shield_jerk_1260d_v132_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_5d_v133_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_5d_v133_signal},
    "f03_nim_proxy_assets_slope_diff_norm_5d_v134_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_5d_v134_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_5d_v135_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_5d_v135_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_5d_v136_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_5d_v136_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_5d_v137_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_5d_v137_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_5d_v138_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_5d_v138_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_10d_v139_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_10d_v139_signal},
    "f03_nim_proxy_assets_slope_diff_norm_10d_v140_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_10d_v140_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_10d_v141_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_10d_v141_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_10d_v142_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_10d_v142_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_10d_v143_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_10d_v143_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_10d_v144_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_10d_v144_signal},
    "f03_nim_proxy_netinc_slope_diff_norm_21d_v145_signal": {"func": f03_nim_proxy_netinc_slope_diff_norm_21d_v145_signal},
    "f03_nim_proxy_assets_slope_diff_norm_21d_v146_signal": {"func": f03_nim_proxy_assets_slope_diff_norm_21d_v146_signal},
    "f03_nim_proxy_ebt_slope_diff_norm_21d_v147_signal": {"func": f03_nim_proxy_ebt_slope_diff_norm_21d_v147_signal},
    "f03_nim_proxy_roa_net_slope_diff_norm_21d_v148_signal": {"func": f03_nim_proxy_roa_net_slope_diff_norm_21d_v148_signal},
    "f03_nim_proxy_roa_pretax_slope_diff_norm_21d_v149_signal": {"func": f03_nim_proxy_roa_pretax_slope_diff_norm_21d_v149_signal},
    "f03_nim_proxy_tax_shield_slope_diff_norm_21d_v150_signal": {"func": f03_nim_proxy_tax_shield_slope_diff_norm_21d_v150_signal},
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
