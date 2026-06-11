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

def f08_asset_mgmt_yield_netinc_slope_pct_5d_v001_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_5d_v002_signal(invcap):
    """Percentage slope for Raw level of invcap over 5d window."""
    res = _slope_pct(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_5d_v003_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_5d_v004_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 5d window."""
    res = _slope_pct(_ratio(netinc, invcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_5d_v005_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 5d window."""
    res = _slope_pct(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_10d_v006_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_10d_v007_signal(invcap):
    """Percentage slope for Raw level of invcap over 10d window."""
    res = _slope_pct(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_10d_v008_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_10d_v009_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 10d window."""
    res = _slope_pct(_ratio(netinc, invcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_10d_v010_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 10d window."""
    res = _slope_pct(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_21d_v011_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_21d_v012_signal(invcap):
    """Percentage slope for Raw level of invcap over 21d window."""
    res = _slope_pct(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_21d_v013_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_21d_v014_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 21d window."""
    res = _slope_pct(_ratio(netinc, invcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_21d_v015_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 21d window."""
    res = _slope_pct(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_42d_v016_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_42d_v017_signal(invcap):
    """Percentage slope for Raw level of invcap over 42d window."""
    res = _slope_pct(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_42d_v018_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_42d_v019_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 42d window."""
    res = _slope_pct(_ratio(netinc, invcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_42d_v020_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 42d window."""
    res = _slope_pct(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_63d_v021_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_63d_v022_signal(invcap):
    """Percentage slope for Raw level of invcap over 63d window."""
    res = _slope_pct(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_63d_v023_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_63d_v024_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 63d window."""
    res = _slope_pct(_ratio(netinc, invcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_63d_v025_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 63d window."""
    res = _slope_pct(_ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_126d_v026_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_126d_v027_signal(invcap):
    """Percentage slope for Raw level of invcap over 126d window."""
    res = _slope_pct(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_126d_v028_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_126d_v029_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 126d window."""
    res = _slope_pct(_ratio(netinc, invcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_126d_v030_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 126d window."""
    res = _slope_pct(_ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_252d_v031_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_252d_v032_signal(invcap):
    """Percentage slope for Raw level of invcap over 252d window."""
    res = _slope_pct(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_252d_v033_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_252d_v034_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 252d window."""
    res = _slope_pct(_ratio(netinc, invcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_252d_v035_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 252d window."""
    res = _slope_pct(_ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_504d_v036_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_504d_v037_signal(invcap):
    """Percentage slope for Raw level of invcap over 504d window."""
    res = _slope_pct(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_504d_v038_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_504d_v039_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 504d window."""
    res = _slope_pct(_ratio(netinc, invcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_504d_v040_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 504d window."""
    res = _slope_pct(_ratio(revenue, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_756d_v041_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_756d_v042_signal(invcap):
    """Percentage slope for Raw level of invcap over 756d window."""
    res = _slope_pct(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_756d_v043_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_756d_v044_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 756d window."""
    res = _slope_pct(_ratio(netinc, invcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_756d_v045_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 756d window."""
    res = _slope_pct(_ratio(revenue, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_1008d_v046_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_1008d_v047_signal(invcap):
    """Percentage slope for Raw level of invcap over 1008d window."""
    res = _slope_pct(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_1008d_v048_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_1008d_v049_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 1008d window."""
    res = _slope_pct(_ratio(netinc, invcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_1008d_v050_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 1008d window."""
    res = _slope_pct(_ratio(revenue, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_pct_1260d_v051_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_pct_1260d_v052_signal(invcap):
    """Percentage slope for Raw level of invcap over 1260d window."""
    res = _slope_pct(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_pct_1260d_v053_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_pct_1260d_v054_signal(netinc, invcap):
    """Percentage slope for Return on invested capital over 1260d window."""
    res = _slope_pct(_ratio(netinc, invcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_pct_1260d_v055_signal(revenue, assets):
    """Percentage slope for Total asset utilization over 1260d window."""
    res = _slope_pct(_ratio(revenue, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_5d_v056_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_5d_v057_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 5d window."""
    res = _jerk(invcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_5d_v058_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_5d_v059_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 5d window."""
    res = _jerk(_ratio(netinc, invcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_5d_v060_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 5d window."""
    res = _jerk(_ratio(revenue, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_10d_v061_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_10d_v062_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 10d window."""
    res = _jerk(invcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_10d_v063_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_10d_v064_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 10d window."""
    res = _jerk(_ratio(netinc, invcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_10d_v065_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 10d window."""
    res = _jerk(_ratio(revenue, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_21d_v066_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_21d_v067_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 21d window."""
    res = _jerk(invcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_21d_v068_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_21d_v069_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 21d window."""
    res = _jerk(_ratio(netinc, invcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_21d_v070_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 21d window."""
    res = _jerk(_ratio(revenue, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_42d_v071_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_42d_v072_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 42d window."""
    res = _jerk(invcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_42d_v073_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_42d_v074_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 42d window."""
    res = _jerk(_ratio(netinc, invcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_42d_v075_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 42d window."""
    res = _jerk(_ratio(revenue, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_63d_v076_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_63d_v077_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 63d window."""
    res = _jerk(invcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_63d_v078_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_63d_v079_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 63d window."""
    res = _jerk(_ratio(netinc, invcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_63d_v080_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 63d window."""
    res = _jerk(_ratio(revenue, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_126d_v081_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_126d_v082_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 126d window."""
    res = _jerk(invcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_126d_v083_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_126d_v084_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 126d window."""
    res = _jerk(_ratio(netinc, invcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_126d_v085_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 126d window."""
    res = _jerk(_ratio(revenue, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_252d_v086_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_252d_v087_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 252d window."""
    res = _jerk(invcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_252d_v088_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_252d_v089_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 252d window."""
    res = _jerk(_ratio(netinc, invcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_252d_v090_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 252d window."""
    res = _jerk(_ratio(revenue, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_504d_v091_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_504d_v092_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 504d window."""
    res = _jerk(invcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_504d_v093_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_504d_v094_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 504d window."""
    res = _jerk(_ratio(netinc, invcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_504d_v095_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 504d window."""
    res = _jerk(_ratio(revenue, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_756d_v096_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_756d_v097_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 756d window."""
    res = _jerk(invcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_756d_v098_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_756d_v099_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 756d window."""
    res = _jerk(_ratio(netinc, invcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_756d_v100_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 756d window."""
    res = _jerk(_ratio(revenue, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_1008d_v101_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_1008d_v102_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 1008d window."""
    res = _jerk(invcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_1008d_v103_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_1008d_v104_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 1008d window."""
    res = _jerk(_ratio(netinc, invcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_1008d_v105_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 1008d window."""
    res = _jerk(_ratio(revenue, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_jerk_1260d_v106_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_jerk_1260d_v107_signal(invcap):
    """Acceleration/Jerk for Raw level of invcap over 1260d window."""
    res = _jerk(invcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_jerk_1260d_v108_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_jerk_1260d_v109_signal(netinc, invcap):
    """Acceleration/Jerk for Return on invested capital over 1260d window."""
    res = _jerk(_ratio(netinc, invcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_jerk_1260d_v110_signal(revenue, assets):
    """Acceleration/Jerk for Total asset utilization over 1260d window."""
    res = _jerk(_ratio(revenue, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_5d_v111_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_5d_v112_signal(invcap):
    """Normalized slope change for Raw level of invcap over 5d window."""
    res = (_slope_pct(invcap, 5).diff(5) / _sma(invcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_5d_v113_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_5d_v114_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 5d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 5).diff(5) / _sma(_ratio(netinc, invcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_5d_v115_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 5d window."""
    res = (_slope_pct(_ratio(revenue, assets), 5).diff(5) / _sma(_ratio(revenue, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_10d_v116_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_10d_v117_signal(invcap):
    """Normalized slope change for Raw level of invcap over 10d window."""
    res = (_slope_pct(invcap, 10).diff(10) / _sma(invcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_10d_v118_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_10d_v119_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 10d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 10).diff(10) / _sma(_ratio(netinc, invcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_10d_v120_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 10d window."""
    res = (_slope_pct(_ratio(revenue, assets), 10).diff(10) / _sma(_ratio(revenue, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_21d_v121_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_21d_v122_signal(invcap):
    """Normalized slope change for Raw level of invcap over 21d window."""
    res = (_slope_pct(invcap, 21).diff(21) / _sma(invcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_21d_v123_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_21d_v124_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 21d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 21).diff(21) / _sma(_ratio(netinc, invcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_21d_v125_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 21d window."""
    res = (_slope_pct(_ratio(revenue, assets), 21).diff(21) / _sma(_ratio(revenue, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_42d_v126_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_42d_v127_signal(invcap):
    """Normalized slope change for Raw level of invcap over 42d window."""
    res = (_slope_pct(invcap, 42).diff(42) / _sma(invcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_42d_v128_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_42d_v129_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 42d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 42).diff(42) / _sma(_ratio(netinc, invcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_42d_v130_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 42d window."""
    res = (_slope_pct(_ratio(revenue, assets), 42).diff(42) / _sma(_ratio(revenue, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_63d_v131_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_63d_v132_signal(invcap):
    """Normalized slope change for Raw level of invcap over 63d window."""
    res = (_slope_pct(invcap, 63).diff(63) / _sma(invcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_63d_v133_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_63d_v134_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 63d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 63).diff(63) / _sma(_ratio(netinc, invcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_63d_v135_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 63d window."""
    res = (_slope_pct(_ratio(revenue, assets), 63).diff(63) / _sma(_ratio(revenue, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_126d_v136_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_126d_v137_signal(invcap):
    """Normalized slope change for Raw level of invcap over 126d window."""
    res = (_slope_pct(invcap, 126).diff(126) / _sma(invcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_126d_v138_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_126d_v139_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 126d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 126).diff(126) / _sma(_ratio(netinc, invcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_126d_v140_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 126d window."""
    res = (_slope_pct(_ratio(revenue, assets), 126).diff(126) / _sma(_ratio(revenue, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_252d_v141_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_252d_v142_signal(invcap):
    """Normalized slope change for Raw level of invcap over 252d window."""
    res = (_slope_pct(invcap, 252).diff(252) / _sma(invcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_252d_v143_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_252d_v144_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 252d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 252).diff(252) / _sma(_ratio(netinc, invcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_252d_v145_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 252d window."""
    res = (_slope_pct(_ratio(revenue, assets), 252).diff(252) / _sma(_ratio(revenue, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_slope_diff_norm_504d_v146_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_slope_diff_norm_504d_v147_signal(invcap):
    """Normalized slope change for Raw level of invcap over 504d window."""
    res = (_slope_pct(invcap, 504).diff(504) / _sma(invcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_slope_diff_norm_504d_v148_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_slope_diff_norm_504d_v149_signal(netinc, invcap):
    """Normalized slope change for Return on invested capital over 504d window."""
    res = (_slope_pct(_ratio(netinc, invcap), 504).diff(504) / _sma(_ratio(netinc, invcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_504d_v150_signal(revenue, assets):
    """Normalized slope change for Total asset utilization over 504d window."""
    res = (_slope_pct(_ratio(revenue, assets), 504).diff(504) / _sma(_ratio(revenue, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f08_asset_mgmt_yield_netinc_slope_pct_5d_v001_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_5d_v001_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_5d_v002_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_5d_v002_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_5d_v003_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_5d_v003_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_5d_v004_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_5d_v004_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_5d_v005_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_5d_v005_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_10d_v006_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_10d_v006_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_10d_v007_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_10d_v007_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_10d_v008_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_10d_v008_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_10d_v009_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_10d_v009_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_10d_v010_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_10d_v010_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_21d_v011_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_21d_v011_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_21d_v012_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_21d_v012_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_21d_v013_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_21d_v013_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_21d_v014_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_21d_v014_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_21d_v015_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_21d_v015_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_42d_v016_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_42d_v016_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_42d_v017_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_42d_v017_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_42d_v018_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_42d_v018_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_42d_v019_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_42d_v019_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_42d_v020_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_42d_v020_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_63d_v021_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_63d_v021_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_63d_v022_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_63d_v022_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_63d_v023_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_63d_v023_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_63d_v024_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_63d_v024_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_63d_v025_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_63d_v025_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_126d_v026_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_126d_v026_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_126d_v027_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_126d_v027_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_126d_v028_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_126d_v028_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_126d_v029_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_126d_v029_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_126d_v030_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_126d_v030_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_252d_v031_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_252d_v031_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_252d_v032_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_252d_v032_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_252d_v033_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_252d_v033_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_252d_v034_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_252d_v034_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_252d_v035_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_252d_v035_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_504d_v036_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_504d_v036_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_504d_v037_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_504d_v037_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_504d_v038_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_504d_v038_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_504d_v039_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_504d_v039_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_504d_v040_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_504d_v040_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_756d_v041_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_756d_v041_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_756d_v042_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_756d_v042_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_756d_v043_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_756d_v043_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_756d_v044_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_756d_v044_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_756d_v045_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_756d_v045_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_1008d_v046_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_1008d_v046_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_1008d_v047_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_1008d_v047_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_1008d_v048_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_1008d_v048_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_1008d_v049_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_1008d_v049_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_1008d_v050_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_1008d_v050_signal},
    "f08_asset_mgmt_yield_netinc_slope_pct_1260d_v051_signal": {"func": f08_asset_mgmt_yield_netinc_slope_pct_1260d_v051_signal},
    "f08_asset_mgmt_yield_invcap_slope_pct_1260d_v052_signal": {"func": f08_asset_mgmt_yield_invcap_slope_pct_1260d_v052_signal},
    "f08_asset_mgmt_yield_assets_slope_pct_1260d_v053_signal": {"func": f08_asset_mgmt_yield_assets_slope_pct_1260d_v053_signal},
    "f08_asset_mgmt_yield_roic_slope_pct_1260d_v054_signal": {"func": f08_asset_mgmt_yield_roic_slope_pct_1260d_v054_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_pct_1260d_v055_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_pct_1260d_v055_signal},
    "f08_asset_mgmt_yield_netinc_jerk_5d_v056_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_5d_v056_signal},
    "f08_asset_mgmt_yield_invcap_jerk_5d_v057_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_5d_v057_signal},
    "f08_asset_mgmt_yield_assets_jerk_5d_v058_signal": {"func": f08_asset_mgmt_yield_assets_jerk_5d_v058_signal},
    "f08_asset_mgmt_yield_roic_jerk_5d_v059_signal": {"func": f08_asset_mgmt_yield_roic_jerk_5d_v059_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_5d_v060_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_5d_v060_signal},
    "f08_asset_mgmt_yield_netinc_jerk_10d_v061_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_10d_v061_signal},
    "f08_asset_mgmt_yield_invcap_jerk_10d_v062_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_10d_v062_signal},
    "f08_asset_mgmt_yield_assets_jerk_10d_v063_signal": {"func": f08_asset_mgmt_yield_assets_jerk_10d_v063_signal},
    "f08_asset_mgmt_yield_roic_jerk_10d_v064_signal": {"func": f08_asset_mgmt_yield_roic_jerk_10d_v064_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_10d_v065_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_10d_v065_signal},
    "f08_asset_mgmt_yield_netinc_jerk_21d_v066_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_21d_v066_signal},
    "f08_asset_mgmt_yield_invcap_jerk_21d_v067_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_21d_v067_signal},
    "f08_asset_mgmt_yield_assets_jerk_21d_v068_signal": {"func": f08_asset_mgmt_yield_assets_jerk_21d_v068_signal},
    "f08_asset_mgmt_yield_roic_jerk_21d_v069_signal": {"func": f08_asset_mgmt_yield_roic_jerk_21d_v069_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_21d_v070_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_21d_v070_signal},
    "f08_asset_mgmt_yield_netinc_jerk_42d_v071_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_42d_v071_signal},
    "f08_asset_mgmt_yield_invcap_jerk_42d_v072_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_42d_v072_signal},
    "f08_asset_mgmt_yield_assets_jerk_42d_v073_signal": {"func": f08_asset_mgmt_yield_assets_jerk_42d_v073_signal},
    "f08_asset_mgmt_yield_roic_jerk_42d_v074_signal": {"func": f08_asset_mgmt_yield_roic_jerk_42d_v074_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_42d_v075_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_42d_v075_signal},
    "f08_asset_mgmt_yield_netinc_jerk_63d_v076_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_63d_v076_signal},
    "f08_asset_mgmt_yield_invcap_jerk_63d_v077_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_63d_v077_signal},
    "f08_asset_mgmt_yield_assets_jerk_63d_v078_signal": {"func": f08_asset_mgmt_yield_assets_jerk_63d_v078_signal},
    "f08_asset_mgmt_yield_roic_jerk_63d_v079_signal": {"func": f08_asset_mgmt_yield_roic_jerk_63d_v079_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_63d_v080_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_63d_v080_signal},
    "f08_asset_mgmt_yield_netinc_jerk_126d_v081_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_126d_v081_signal},
    "f08_asset_mgmt_yield_invcap_jerk_126d_v082_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_126d_v082_signal},
    "f08_asset_mgmt_yield_assets_jerk_126d_v083_signal": {"func": f08_asset_mgmt_yield_assets_jerk_126d_v083_signal},
    "f08_asset_mgmt_yield_roic_jerk_126d_v084_signal": {"func": f08_asset_mgmt_yield_roic_jerk_126d_v084_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_126d_v085_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_126d_v085_signal},
    "f08_asset_mgmt_yield_netinc_jerk_252d_v086_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_252d_v086_signal},
    "f08_asset_mgmt_yield_invcap_jerk_252d_v087_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_252d_v087_signal},
    "f08_asset_mgmt_yield_assets_jerk_252d_v088_signal": {"func": f08_asset_mgmt_yield_assets_jerk_252d_v088_signal},
    "f08_asset_mgmt_yield_roic_jerk_252d_v089_signal": {"func": f08_asset_mgmt_yield_roic_jerk_252d_v089_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_252d_v090_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_252d_v090_signal},
    "f08_asset_mgmt_yield_netinc_jerk_504d_v091_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_504d_v091_signal},
    "f08_asset_mgmt_yield_invcap_jerk_504d_v092_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_504d_v092_signal},
    "f08_asset_mgmt_yield_assets_jerk_504d_v093_signal": {"func": f08_asset_mgmt_yield_assets_jerk_504d_v093_signal},
    "f08_asset_mgmt_yield_roic_jerk_504d_v094_signal": {"func": f08_asset_mgmt_yield_roic_jerk_504d_v094_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_504d_v095_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_504d_v095_signal},
    "f08_asset_mgmt_yield_netinc_jerk_756d_v096_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_756d_v096_signal},
    "f08_asset_mgmt_yield_invcap_jerk_756d_v097_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_756d_v097_signal},
    "f08_asset_mgmt_yield_assets_jerk_756d_v098_signal": {"func": f08_asset_mgmt_yield_assets_jerk_756d_v098_signal},
    "f08_asset_mgmt_yield_roic_jerk_756d_v099_signal": {"func": f08_asset_mgmt_yield_roic_jerk_756d_v099_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_756d_v100_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_756d_v100_signal},
    "f08_asset_mgmt_yield_netinc_jerk_1008d_v101_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_1008d_v101_signal},
    "f08_asset_mgmt_yield_invcap_jerk_1008d_v102_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_1008d_v102_signal},
    "f08_asset_mgmt_yield_assets_jerk_1008d_v103_signal": {"func": f08_asset_mgmt_yield_assets_jerk_1008d_v103_signal},
    "f08_asset_mgmt_yield_roic_jerk_1008d_v104_signal": {"func": f08_asset_mgmt_yield_roic_jerk_1008d_v104_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_1008d_v105_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_1008d_v105_signal},
    "f08_asset_mgmt_yield_netinc_jerk_1260d_v106_signal": {"func": f08_asset_mgmt_yield_netinc_jerk_1260d_v106_signal},
    "f08_asset_mgmt_yield_invcap_jerk_1260d_v107_signal": {"func": f08_asset_mgmt_yield_invcap_jerk_1260d_v107_signal},
    "f08_asset_mgmt_yield_assets_jerk_1260d_v108_signal": {"func": f08_asset_mgmt_yield_assets_jerk_1260d_v108_signal},
    "f08_asset_mgmt_yield_roic_jerk_1260d_v109_signal": {"func": f08_asset_mgmt_yield_roic_jerk_1260d_v109_signal},
    "f08_asset_mgmt_yield_asset_turnover_jerk_1260d_v110_signal": {"func": f08_asset_mgmt_yield_asset_turnover_jerk_1260d_v110_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_5d_v111_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_5d_v111_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_5d_v112_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_5d_v112_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_5d_v113_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_5d_v113_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_5d_v114_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_5d_v114_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_5d_v115_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_5d_v115_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_10d_v116_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_10d_v116_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_10d_v117_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_10d_v117_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_10d_v118_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_10d_v118_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_10d_v119_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_10d_v119_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_10d_v120_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_10d_v120_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_21d_v121_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_21d_v121_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_21d_v122_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_21d_v122_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_21d_v123_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_21d_v123_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_21d_v124_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_21d_v124_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_21d_v125_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_21d_v125_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_42d_v126_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_42d_v126_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_42d_v127_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_42d_v127_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_42d_v128_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_42d_v128_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_42d_v129_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_42d_v129_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_42d_v130_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_42d_v130_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_63d_v131_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_63d_v131_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_63d_v132_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_63d_v132_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_63d_v133_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_63d_v133_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_63d_v134_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_63d_v134_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_63d_v135_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_63d_v135_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_126d_v136_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_126d_v136_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_126d_v137_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_126d_v137_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_126d_v138_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_126d_v138_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_126d_v139_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_126d_v139_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_126d_v140_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_126d_v140_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_252d_v141_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_252d_v141_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_252d_v142_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_252d_v142_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_252d_v143_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_252d_v143_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_252d_v144_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_252d_v144_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_252d_v145_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_252d_v145_signal},
    "f08_asset_mgmt_yield_netinc_slope_diff_norm_504d_v146_signal": {"func": f08_asset_mgmt_yield_netinc_slope_diff_norm_504d_v146_signal},
    "f08_asset_mgmt_yield_invcap_slope_diff_norm_504d_v147_signal": {"func": f08_asset_mgmt_yield_invcap_slope_diff_norm_504d_v147_signal},
    "f08_asset_mgmt_yield_assets_slope_diff_norm_504d_v148_signal": {"func": f08_asset_mgmt_yield_assets_slope_diff_norm_504d_v148_signal},
    "f08_asset_mgmt_yield_roic_slope_diff_norm_504d_v149_signal": {"func": f08_asset_mgmt_yield_roic_slope_diff_norm_504d_v149_signal},
    "f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_504d_v150_signal": {"func": f08_asset_mgmt_yield_asset_turnover_slope_diff_norm_504d_v150_signal},
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
