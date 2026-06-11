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

def f15_franchise_yield_revenue_slope_pct_5d_v001_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_5d_v002_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_5d_v003_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_5d_v004_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 5d window."""
    res = _slope_pct(_ratio(netinc, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_10d_v005_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_10d_v006_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_10d_v007_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_10d_v008_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 10d window."""
    res = _slope_pct(_ratio(netinc, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_21d_v009_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_21d_v010_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_21d_v011_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_21d_v012_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 21d window."""
    res = _slope_pct(_ratio(netinc, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_42d_v013_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_42d_v014_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_42d_v015_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_42d_v016_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 42d window."""
    res = _slope_pct(_ratio(netinc, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_63d_v017_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_63d_v018_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_63d_v019_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_63d_v020_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 63d window."""
    res = _slope_pct(_ratio(netinc, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_126d_v021_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_126d_v022_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_126d_v023_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_126d_v024_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 126d window."""
    res = _slope_pct(_ratio(netinc, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_252d_v025_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_252d_v026_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_252d_v027_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_252d_v028_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 252d window."""
    res = _slope_pct(_ratio(netinc, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_504d_v029_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_504d_v030_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_504d_v031_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_504d_v032_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 504d window."""
    res = _slope_pct(_ratio(netinc, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_756d_v033_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_756d_v034_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_756d_v035_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_756d_v036_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 756d window."""
    res = _slope_pct(_ratio(netinc, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_1008d_v037_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_1008d_v038_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_1008d_v039_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_1008d_v040_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 1008d window."""
    res = _slope_pct(_ratio(netinc, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_pct_1260d_v041_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_pct_1260d_v042_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_pct_1260d_v043_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_pct_1260d_v044_signal(netinc, assets):
    """Percentage slope for momentum for Net income return on total asset base over 1260d window."""
    res = _slope_pct(_ratio(netinc, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_5d_v045_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_5d_v046_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_5d_v047_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_5d_v048_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 5d window."""
    res = _jerk(_ratio(netinc, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_10d_v049_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_10d_v050_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_10d_v051_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_10d_v052_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 10d window."""
    res = _jerk(_ratio(netinc, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_21d_v053_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_21d_v054_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_21d_v055_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_21d_v056_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 21d window."""
    res = _jerk(_ratio(netinc, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_42d_v057_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_42d_v058_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_42d_v059_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_42d_v060_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 42d window."""
    res = _jerk(_ratio(netinc, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_63d_v061_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_63d_v062_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_63d_v063_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_63d_v064_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 63d window."""
    res = _jerk(_ratio(netinc, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_126d_v065_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_126d_v066_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_126d_v067_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_126d_v068_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 126d window."""
    res = _jerk(_ratio(netinc, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_252d_v069_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_252d_v070_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_252d_v071_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_252d_v072_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 252d window."""
    res = _jerk(_ratio(netinc, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_504d_v073_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_504d_v074_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_504d_v075_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_504d_v076_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 504d window."""
    res = _jerk(_ratio(netinc, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_756d_v077_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_756d_v078_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_756d_v079_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_756d_v080_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 756d window."""
    res = _jerk(_ratio(netinc, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_1008d_v081_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_1008d_v082_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_1008d_v083_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_1008d_v084_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 1008d window."""
    res = _jerk(_ratio(netinc, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_jerk_1260d_v085_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_jerk_1260d_v086_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_jerk_1260d_v087_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_jerk_1260d_v088_signal(netinc, assets):
    """Acceleration/Jerk for structural shifts for Net income return on total asset base over 1260d window."""
    res = _jerk(_ratio(netinc, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_5d_v089_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_5d_v090_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_5d_v091_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_5d_v092_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 5d window."""
    res = (_slope_pct(_ratio(netinc, assets), 5).diff(5) / _sma(_ratio(netinc, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_10d_v093_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_10d_v094_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_10d_v095_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_10d_v096_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 10d window."""
    res = (_slope_pct(_ratio(netinc, assets), 10).diff(10) / _sma(_ratio(netinc, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_21d_v097_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_21d_v098_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_21d_v099_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_21d_v100_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 21d window."""
    res = (_slope_pct(_ratio(netinc, assets), 21).diff(21) / _sma(_ratio(netinc, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_42d_v101_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_42d_v102_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_42d_v103_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_42d_v104_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 42d window."""
    res = (_slope_pct(_ratio(netinc, assets), 42).diff(42) / _sma(_ratio(netinc, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_63d_v105_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_63d_v106_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_63d_v107_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_63d_v108_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 63d window."""
    res = (_slope_pct(_ratio(netinc, assets), 63).diff(63) / _sma(_ratio(netinc, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_126d_v109_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_126d_v110_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_126d_v111_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_126d_v112_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 126d window."""
    res = (_slope_pct(_ratio(netinc, assets), 126).diff(126) / _sma(_ratio(netinc, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_252d_v113_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_252d_v114_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_252d_v115_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_252d_v116_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 252d window."""
    res = (_slope_pct(_ratio(netinc, assets), 252).diff(252) / _sma(_ratio(netinc, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_504d_v117_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_504d_v118_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_504d_v119_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_504d_v120_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 504d window."""
    res = (_slope_pct(_ratio(netinc, assets), 504).diff(504) / _sma(_ratio(netinc, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_756d_v121_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_756d_v122_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_756d_v123_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_756d_v124_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 756d window."""
    res = (_slope_pct(_ratio(netinc, assets), 756).diff(756) / _sma(_ratio(netinc, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_1008d_v125_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_1008d_v126_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_1008d_v127_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_1008d_v128_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 1008d window."""
    res = (_slope_pct(_ratio(netinc, assets), 1008).diff(1008) / _sma(_ratio(netinc, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_slope_diff_norm_1260d_v129_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_slope_diff_norm_1260d_v130_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_slope_diff_norm_1260d_v131_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_slope_diff_norm_1260d_v132_signal(netinc, assets):
    """Normalized slope change for Net income return on total asset base over 1260d window."""
    res = (_slope_pct(_ratio(netinc, assets), 1260).diff(1260) / _sma(_ratio(netinc, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_mom_z_5d_v133_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_mom_z_5d_v134_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_mom_z_5d_v135_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_mom_z_5d_v136_signal(netinc, assets):
    """Relative momentum strength for Net income return on total asset base over 5d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_mom_z_10d_v137_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_mom_z_10d_v138_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_mom_z_10d_v139_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_mom_z_10d_v140_signal(netinc, assets):
    """Relative momentum strength for Net income return on total asset base over 10d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_mom_z_21d_v141_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_mom_z_21d_v142_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_mom_z_21d_v143_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_mom_z_21d_v144_signal(netinc, assets):
    """Relative momentum strength for Net income return on total asset base over 21d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_mom_z_42d_v145_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_mom_z_42d_v146_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_assets_mom_z_42d_v147_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_asset_light_roi_mom_z_42d_v148_signal(netinc, assets):
    """Relative momentum strength for Net income return on total asset base over 42d window."""
    res = _z(_slope_pct(_ratio(netinc, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_revenue_mom_z_63d_v149_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_franchise_yield_netinc_mom_z_63d_v150_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f15_franchise_yield_revenue_slope_pct_5d_v001_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_5d_v001_signal},    "f15_franchise_yield_netinc_slope_pct_5d_v002_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_5d_v002_signal},    "f15_franchise_yield_assets_slope_pct_5d_v003_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_5d_v003_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_5d_v004_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_5d_v004_signal},    "f15_franchise_yield_revenue_slope_pct_10d_v005_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_10d_v005_signal},    "f15_franchise_yield_netinc_slope_pct_10d_v006_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_10d_v006_signal},    "f15_franchise_yield_assets_slope_pct_10d_v007_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_10d_v007_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_10d_v008_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_10d_v008_signal},    "f15_franchise_yield_revenue_slope_pct_21d_v009_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_21d_v009_signal},    "f15_franchise_yield_netinc_slope_pct_21d_v010_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_21d_v010_signal},    "f15_franchise_yield_assets_slope_pct_21d_v011_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_21d_v011_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_21d_v012_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_21d_v012_signal},    "f15_franchise_yield_revenue_slope_pct_42d_v013_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_42d_v013_signal},    "f15_franchise_yield_netinc_slope_pct_42d_v014_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_42d_v014_signal},    "f15_franchise_yield_assets_slope_pct_42d_v015_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_42d_v015_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_42d_v016_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_42d_v016_signal},    "f15_franchise_yield_revenue_slope_pct_63d_v017_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_63d_v017_signal},    "f15_franchise_yield_netinc_slope_pct_63d_v018_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_63d_v018_signal},    "f15_franchise_yield_assets_slope_pct_63d_v019_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_63d_v019_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_63d_v020_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_63d_v020_signal},    "f15_franchise_yield_revenue_slope_pct_126d_v021_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_126d_v021_signal},    "f15_franchise_yield_netinc_slope_pct_126d_v022_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_126d_v022_signal},    "f15_franchise_yield_assets_slope_pct_126d_v023_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_126d_v023_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_126d_v024_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_126d_v024_signal},    "f15_franchise_yield_revenue_slope_pct_252d_v025_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_252d_v025_signal},    "f15_franchise_yield_netinc_slope_pct_252d_v026_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_252d_v026_signal},    "f15_franchise_yield_assets_slope_pct_252d_v027_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_252d_v027_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_252d_v028_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_252d_v028_signal},    "f15_franchise_yield_revenue_slope_pct_504d_v029_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_504d_v029_signal},    "f15_franchise_yield_netinc_slope_pct_504d_v030_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_504d_v030_signal},    "f15_franchise_yield_assets_slope_pct_504d_v031_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_504d_v031_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_504d_v032_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_504d_v032_signal},    "f15_franchise_yield_revenue_slope_pct_756d_v033_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_756d_v033_signal},    "f15_franchise_yield_netinc_slope_pct_756d_v034_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_756d_v034_signal},    "f15_franchise_yield_assets_slope_pct_756d_v035_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_756d_v035_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_756d_v036_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_756d_v036_signal},    "f15_franchise_yield_revenue_slope_pct_1008d_v037_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_1008d_v037_signal},    "f15_franchise_yield_netinc_slope_pct_1008d_v038_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_1008d_v038_signal},    "f15_franchise_yield_assets_slope_pct_1008d_v039_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_1008d_v039_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_1008d_v040_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_1008d_v040_signal},    "f15_franchise_yield_revenue_slope_pct_1260d_v041_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_pct_1260d_v041_signal},    "f15_franchise_yield_netinc_slope_pct_1260d_v042_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_pct_1260d_v042_signal},    "f15_franchise_yield_assets_slope_pct_1260d_v043_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_pct_1260d_v043_signal},    "f15_franchise_yield_asset_light_roi_slope_pct_1260d_v044_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_pct_1260d_v044_signal},    "f15_franchise_yield_revenue_jerk_5d_v045_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_5d_v045_signal},    "f15_franchise_yield_netinc_jerk_5d_v046_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_5d_v046_signal},    "f15_franchise_yield_assets_jerk_5d_v047_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_5d_v047_signal},    "f15_franchise_yield_asset_light_roi_jerk_5d_v048_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_5d_v048_signal},    "f15_franchise_yield_revenue_jerk_10d_v049_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_10d_v049_signal},    "f15_franchise_yield_netinc_jerk_10d_v050_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_10d_v050_signal},    "f15_franchise_yield_assets_jerk_10d_v051_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_10d_v051_signal},    "f15_franchise_yield_asset_light_roi_jerk_10d_v052_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_10d_v052_signal},    "f15_franchise_yield_revenue_jerk_21d_v053_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_21d_v053_signal},    "f15_franchise_yield_netinc_jerk_21d_v054_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_21d_v054_signal},    "f15_franchise_yield_assets_jerk_21d_v055_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_21d_v055_signal},    "f15_franchise_yield_asset_light_roi_jerk_21d_v056_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_21d_v056_signal},    "f15_franchise_yield_revenue_jerk_42d_v057_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_42d_v057_signal},    "f15_franchise_yield_netinc_jerk_42d_v058_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_42d_v058_signal},    "f15_franchise_yield_assets_jerk_42d_v059_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_42d_v059_signal},    "f15_franchise_yield_asset_light_roi_jerk_42d_v060_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_42d_v060_signal},    "f15_franchise_yield_revenue_jerk_63d_v061_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_63d_v061_signal},    "f15_franchise_yield_netinc_jerk_63d_v062_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_63d_v062_signal},    "f15_franchise_yield_assets_jerk_63d_v063_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_63d_v063_signal},    "f15_franchise_yield_asset_light_roi_jerk_63d_v064_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_63d_v064_signal},    "f15_franchise_yield_revenue_jerk_126d_v065_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_126d_v065_signal},    "f15_franchise_yield_netinc_jerk_126d_v066_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_126d_v066_signal},    "f15_franchise_yield_assets_jerk_126d_v067_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_126d_v067_signal},    "f15_franchise_yield_asset_light_roi_jerk_126d_v068_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_126d_v068_signal},    "f15_franchise_yield_revenue_jerk_252d_v069_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_252d_v069_signal},    "f15_franchise_yield_netinc_jerk_252d_v070_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_252d_v070_signal},    "f15_franchise_yield_assets_jerk_252d_v071_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_252d_v071_signal},    "f15_franchise_yield_asset_light_roi_jerk_252d_v072_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_252d_v072_signal},    "f15_franchise_yield_revenue_jerk_504d_v073_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_504d_v073_signal},    "f15_franchise_yield_netinc_jerk_504d_v074_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_504d_v074_signal},    "f15_franchise_yield_assets_jerk_504d_v075_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_504d_v075_signal},    "f15_franchise_yield_asset_light_roi_jerk_504d_v076_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_504d_v076_signal},    "f15_franchise_yield_revenue_jerk_756d_v077_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_756d_v077_signal},    "f15_franchise_yield_netinc_jerk_756d_v078_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_756d_v078_signal},    "f15_franchise_yield_assets_jerk_756d_v079_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_756d_v079_signal},    "f15_franchise_yield_asset_light_roi_jerk_756d_v080_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_756d_v080_signal},    "f15_franchise_yield_revenue_jerk_1008d_v081_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_1008d_v081_signal},    "f15_franchise_yield_netinc_jerk_1008d_v082_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_1008d_v082_signal},    "f15_franchise_yield_assets_jerk_1008d_v083_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_1008d_v083_signal},    "f15_franchise_yield_asset_light_roi_jerk_1008d_v084_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_1008d_v084_signal},    "f15_franchise_yield_revenue_jerk_1260d_v085_signal": {"inputs": [], "func": f15_franchise_yield_revenue_jerk_1260d_v085_signal},    "f15_franchise_yield_netinc_jerk_1260d_v086_signal": {"inputs": [], "func": f15_franchise_yield_netinc_jerk_1260d_v086_signal},    "f15_franchise_yield_assets_jerk_1260d_v087_signal": {"inputs": [], "func": f15_franchise_yield_assets_jerk_1260d_v087_signal},    "f15_franchise_yield_asset_light_roi_jerk_1260d_v088_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_jerk_1260d_v088_signal},    "f15_franchise_yield_revenue_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_5d_v089_signal},    "f15_franchise_yield_netinc_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_5d_v090_signal},    "f15_franchise_yield_assets_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_5d_v091_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_5d_v092_signal},    "f15_franchise_yield_revenue_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_10d_v093_signal},    "f15_franchise_yield_netinc_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_10d_v094_signal},    "f15_franchise_yield_assets_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_10d_v095_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_10d_v096_signal},    "f15_franchise_yield_revenue_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_21d_v097_signal},    "f15_franchise_yield_netinc_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_21d_v098_signal},    "f15_franchise_yield_assets_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_21d_v099_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_21d_v100_signal},    "f15_franchise_yield_revenue_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_42d_v101_signal},    "f15_franchise_yield_netinc_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_42d_v102_signal},    "f15_franchise_yield_assets_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_42d_v103_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_42d_v104_signal},    "f15_franchise_yield_revenue_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_63d_v105_signal},    "f15_franchise_yield_netinc_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_63d_v106_signal},    "f15_franchise_yield_assets_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_63d_v107_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_63d_v108_signal},    "f15_franchise_yield_revenue_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_126d_v109_signal},    "f15_franchise_yield_netinc_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_126d_v110_signal},    "f15_franchise_yield_assets_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_126d_v111_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_126d_v112_signal},    "f15_franchise_yield_revenue_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_252d_v113_signal},    "f15_franchise_yield_netinc_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_252d_v114_signal},    "f15_franchise_yield_assets_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_252d_v115_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_252d_v116_signal},    "f15_franchise_yield_revenue_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_504d_v117_signal},    "f15_franchise_yield_netinc_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_504d_v118_signal},    "f15_franchise_yield_assets_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_504d_v119_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_504d_v120_signal},    "f15_franchise_yield_revenue_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_756d_v121_signal},    "f15_franchise_yield_netinc_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_756d_v122_signal},    "f15_franchise_yield_assets_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_756d_v123_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_756d_v124_signal},    "f15_franchise_yield_revenue_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_1008d_v125_signal},    "f15_franchise_yield_netinc_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_1008d_v126_signal},    "f15_franchise_yield_assets_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_1008d_v127_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_1008d_v128_signal},    "f15_franchise_yield_revenue_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f15_franchise_yield_revenue_slope_diff_norm_1260d_v129_signal},    "f15_franchise_yield_netinc_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f15_franchise_yield_netinc_slope_diff_norm_1260d_v130_signal},    "f15_franchise_yield_assets_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f15_franchise_yield_assets_slope_diff_norm_1260d_v131_signal},    "f15_franchise_yield_asset_light_roi_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_slope_diff_norm_1260d_v132_signal},    "f15_franchise_yield_revenue_mom_z_5d_v133_signal": {"inputs": [], "func": f15_franchise_yield_revenue_mom_z_5d_v133_signal},    "f15_franchise_yield_netinc_mom_z_5d_v134_signal": {"inputs": [], "func": f15_franchise_yield_netinc_mom_z_5d_v134_signal},    "f15_franchise_yield_assets_mom_z_5d_v135_signal": {"inputs": [], "func": f15_franchise_yield_assets_mom_z_5d_v135_signal},    "f15_franchise_yield_asset_light_roi_mom_z_5d_v136_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_mom_z_5d_v136_signal},    "f15_franchise_yield_revenue_mom_z_10d_v137_signal": {"inputs": [], "func": f15_franchise_yield_revenue_mom_z_10d_v137_signal},    "f15_franchise_yield_netinc_mom_z_10d_v138_signal": {"inputs": [], "func": f15_franchise_yield_netinc_mom_z_10d_v138_signal},    "f15_franchise_yield_assets_mom_z_10d_v139_signal": {"inputs": [], "func": f15_franchise_yield_assets_mom_z_10d_v139_signal},    "f15_franchise_yield_asset_light_roi_mom_z_10d_v140_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_mom_z_10d_v140_signal},    "f15_franchise_yield_revenue_mom_z_21d_v141_signal": {"inputs": [], "func": f15_franchise_yield_revenue_mom_z_21d_v141_signal},    "f15_franchise_yield_netinc_mom_z_21d_v142_signal": {"inputs": [], "func": f15_franchise_yield_netinc_mom_z_21d_v142_signal},    "f15_franchise_yield_assets_mom_z_21d_v143_signal": {"inputs": [], "func": f15_franchise_yield_assets_mom_z_21d_v143_signal},    "f15_franchise_yield_asset_light_roi_mom_z_21d_v144_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_mom_z_21d_v144_signal},    "f15_franchise_yield_revenue_mom_z_42d_v145_signal": {"inputs": [], "func": f15_franchise_yield_revenue_mom_z_42d_v145_signal},    "f15_franchise_yield_netinc_mom_z_42d_v146_signal": {"inputs": [], "func": f15_franchise_yield_netinc_mom_z_42d_v146_signal},    "f15_franchise_yield_assets_mom_z_42d_v147_signal": {"inputs": [], "func": f15_franchise_yield_assets_mom_z_42d_v147_signal},    "f15_franchise_yield_asset_light_roi_mom_z_42d_v148_signal": {"inputs": [], "func": f15_franchise_yield_asset_light_roi_mom_z_42d_v148_signal},    "f15_franchise_yield_revenue_mom_z_63d_v149_signal": {"inputs": [], "func": f15_franchise_yield_revenue_mom_z_63d_v149_signal},    "f15_franchise_yield_netinc_mom_z_63d_v150_signal": {"inputs": [], "func": f15_franchise_yield_netinc_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 15...")
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
