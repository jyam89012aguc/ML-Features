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

def f01_unit_economics_revenue_slope_pct_5d_v001_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_5d_v002_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 5d window."""
    res = _slope_pct(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_5d_v003_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_5d_v004_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 5d window."""
    res = _slope_pct(_ratio(revenue, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_5d_v005_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 5d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_10d_v006_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_10d_v007_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 10d window."""
    res = _slope_pct(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_10d_v008_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_10d_v009_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 10d window."""
    res = _slope_pct(_ratio(revenue, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_10d_v010_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 10d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_21d_v011_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_21d_v012_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 21d window."""
    res = _slope_pct(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_21d_v013_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_21d_v014_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 21d window."""
    res = _slope_pct(_ratio(revenue, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_21d_v015_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 21d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_42d_v016_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_42d_v017_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 42d window."""
    res = _slope_pct(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_42d_v018_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_42d_v019_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 42d window."""
    res = _slope_pct(_ratio(revenue, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_42d_v020_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 42d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_63d_v021_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_63d_v022_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 63d window."""
    res = _slope_pct(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_63d_v023_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_63d_v024_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 63d window."""
    res = _slope_pct(_ratio(revenue, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_63d_v025_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 63d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_126d_v026_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_126d_v027_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 126d window."""
    res = _slope_pct(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_126d_v028_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_126d_v029_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 126d window."""
    res = _slope_pct(_ratio(revenue, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_126d_v030_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 126d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_252d_v031_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_252d_v032_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 252d window."""
    res = _slope_pct(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_252d_v033_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_252d_v034_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 252d window."""
    res = _slope_pct(_ratio(revenue, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_252d_v035_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 252d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_504d_v036_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_504d_v037_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 504d window."""
    res = _slope_pct(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_504d_v038_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_504d_v039_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 504d window."""
    res = _slope_pct(_ratio(revenue, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_504d_v040_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 504d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_756d_v041_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_756d_v042_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 756d window."""
    res = _slope_pct(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_756d_v043_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_756d_v044_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 756d window."""
    res = _slope_pct(_ratio(revenue, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_756d_v045_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 756d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_1008d_v046_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_1008d_v047_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 1008d window."""
    res = _slope_pct(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_1008d_v048_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_1008d_v049_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 1008d window."""
    res = _slope_pct(_ratio(revenue, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_1008d_v050_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 1008d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_pct_1260d_v051_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_pct_1260d_v052_signal(capex):
    """Percentage slope for momentum for Raw level of capex over 1260d window."""
    res = _slope_pct(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_pct_1260d_v053_signal(assets):
    """Percentage slope for momentum for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_pct_1260d_v054_signal(revenue, capex):
    """Percentage slope for momentum for Revenue per unit of capital expenditure over 1260d window."""
    res = _slope_pct(_ratio(revenue, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_pct_1260d_v055_signal(revenue, capex, assets):
    """Percentage slope for momentum for Net unit productivity relative to assets over 1260d window."""
    res = _slope_pct(_ratio(revenue - capex, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_5d_v056_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_5d_v057_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 5d window."""
    res = _jerk(capex, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_5d_v058_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_5d_v059_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 5d window."""
    res = _jerk(_ratio(revenue, capex), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_5d_v060_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 5d window."""
    res = _jerk(_ratio(revenue - capex, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_10d_v061_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_10d_v062_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 10d window."""
    res = _jerk(capex, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_10d_v063_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_10d_v064_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 10d window."""
    res = _jerk(_ratio(revenue, capex), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_10d_v065_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 10d window."""
    res = _jerk(_ratio(revenue - capex, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_21d_v066_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_21d_v067_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 21d window."""
    res = _jerk(capex, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_21d_v068_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_21d_v069_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 21d window."""
    res = _jerk(_ratio(revenue, capex), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_21d_v070_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 21d window."""
    res = _jerk(_ratio(revenue - capex, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_42d_v071_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_42d_v072_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 42d window."""
    res = _jerk(capex, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_42d_v073_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_42d_v074_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 42d window."""
    res = _jerk(_ratio(revenue, capex), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_42d_v075_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 42d window."""
    res = _jerk(_ratio(revenue - capex, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_63d_v076_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_63d_v077_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 63d window."""
    res = _jerk(capex, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_63d_v078_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_63d_v079_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 63d window."""
    res = _jerk(_ratio(revenue, capex), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_63d_v080_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 63d window."""
    res = _jerk(_ratio(revenue - capex, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_126d_v081_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_126d_v082_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 126d window."""
    res = _jerk(capex, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_126d_v083_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_126d_v084_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 126d window."""
    res = _jerk(_ratio(revenue, capex), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_126d_v085_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 126d window."""
    res = _jerk(_ratio(revenue - capex, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_252d_v086_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_252d_v087_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 252d window."""
    res = _jerk(capex, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_252d_v088_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_252d_v089_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 252d window."""
    res = _jerk(_ratio(revenue, capex), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_252d_v090_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 252d window."""
    res = _jerk(_ratio(revenue - capex, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_504d_v091_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_504d_v092_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 504d window."""
    res = _jerk(capex, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_504d_v093_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_504d_v094_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 504d window."""
    res = _jerk(_ratio(revenue, capex), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_504d_v095_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 504d window."""
    res = _jerk(_ratio(revenue - capex, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_756d_v096_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_756d_v097_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 756d window."""
    res = _jerk(capex, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_756d_v098_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_756d_v099_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 756d window."""
    res = _jerk(_ratio(revenue, capex), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_756d_v100_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 756d window."""
    res = _jerk(_ratio(revenue - capex, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_1008d_v101_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_1008d_v102_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 1008d window."""
    res = _jerk(capex, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_1008d_v103_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_1008d_v104_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 1008d window."""
    res = _jerk(_ratio(revenue, capex), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_1008d_v105_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 1008d window."""
    res = _jerk(_ratio(revenue - capex, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_jerk_1260d_v106_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_jerk_1260d_v107_signal(capex):
    """Acceleration/Jerk for structural shifts for Raw level of capex over 1260d window."""
    res = _jerk(capex, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_jerk_1260d_v108_signal(assets):
    """Acceleration/Jerk for structural shifts for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_jerk_1260d_v109_signal(revenue, capex):
    """Acceleration/Jerk for structural shifts for Revenue per unit of capital expenditure over 1260d window."""
    res = _jerk(_ratio(revenue, capex), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_jerk_1260d_v110_signal(revenue, capex, assets):
    """Acceleration/Jerk for structural shifts for Net unit productivity relative to assets over 1260d window."""
    res = _jerk(_ratio(revenue - capex, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_5d_v111_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_5d_v112_signal(capex):
    """Normalized slope change for Raw level of capex over 5d window."""
    res = (_slope_pct(capex, 5).diff(5) / _sma(capex.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_5d_v113_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_5d_v114_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 5d window."""
    res = (_slope_pct(_ratio(revenue, capex), 5).diff(5) / _sma(_ratio(revenue, capex).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_5d_v115_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 5d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 5).diff(5) / _sma(_ratio(revenue - capex, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_10d_v116_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_10d_v117_signal(capex):
    """Normalized slope change for Raw level of capex over 10d window."""
    res = (_slope_pct(capex, 10).diff(10) / _sma(capex.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_10d_v118_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_10d_v119_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 10d window."""
    res = (_slope_pct(_ratio(revenue, capex), 10).diff(10) / _sma(_ratio(revenue, capex).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_10d_v120_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 10d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 10).diff(10) / _sma(_ratio(revenue - capex, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_21d_v121_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_21d_v122_signal(capex):
    """Normalized slope change for Raw level of capex over 21d window."""
    res = (_slope_pct(capex, 21).diff(21) / _sma(capex.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_21d_v123_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_21d_v124_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 21d window."""
    res = (_slope_pct(_ratio(revenue, capex), 21).diff(21) / _sma(_ratio(revenue, capex).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_21d_v125_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 21d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 21).diff(21) / _sma(_ratio(revenue - capex, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_42d_v126_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_42d_v127_signal(capex):
    """Normalized slope change for Raw level of capex over 42d window."""
    res = (_slope_pct(capex, 42).diff(42) / _sma(capex.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_42d_v128_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_42d_v129_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 42d window."""
    res = (_slope_pct(_ratio(revenue, capex), 42).diff(42) / _sma(_ratio(revenue, capex).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_42d_v130_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 42d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 42).diff(42) / _sma(_ratio(revenue - capex, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_63d_v131_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_63d_v132_signal(capex):
    """Normalized slope change for Raw level of capex over 63d window."""
    res = (_slope_pct(capex, 63).diff(63) / _sma(capex.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_63d_v133_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_63d_v134_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 63d window."""
    res = (_slope_pct(_ratio(revenue, capex), 63).diff(63) / _sma(_ratio(revenue, capex).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_63d_v135_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 63d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 63).diff(63) / _sma(_ratio(revenue - capex, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_126d_v136_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_126d_v137_signal(capex):
    """Normalized slope change for Raw level of capex over 126d window."""
    res = (_slope_pct(capex, 126).diff(126) / _sma(capex.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_126d_v138_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_126d_v139_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 126d window."""
    res = (_slope_pct(_ratio(revenue, capex), 126).diff(126) / _sma(_ratio(revenue, capex).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_126d_v140_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 126d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 126).diff(126) / _sma(_ratio(revenue - capex, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_252d_v141_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_252d_v142_signal(capex):
    """Normalized slope change for Raw level of capex over 252d window."""
    res = (_slope_pct(capex, 252).diff(252) / _sma(capex.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_252d_v143_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_252d_v144_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 252d window."""
    res = (_slope_pct(_ratio(revenue, capex), 252).diff(252) / _sma(_ratio(revenue, capex).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_252d_v145_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 252d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 252).diff(252) / _sma(_ratio(revenue - capex, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_slope_diff_norm_504d_v146_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_slope_diff_norm_504d_v147_signal(capex):
    """Normalized slope change for Raw level of capex over 504d window."""
    res = (_slope_pct(capex, 504).diff(504) / _sma(capex.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_slope_diff_norm_504d_v148_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_slope_diff_norm_504d_v149_signal(revenue, capex):
    """Normalized slope change for Revenue per unit of capital expenditure over 504d window."""
    res = (_slope_pct(_ratio(revenue, capex), 504).diff(504) / _sma(_ratio(revenue, capex).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_slope_diff_norm_504d_v150_signal(revenue, capex, assets):
    """Normalized slope change for Net unit productivity relative to assets over 504d window."""
    res = (_slope_pct(_ratio(revenue - capex, assets), 504).diff(504) / _sma(_ratio(revenue - capex, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f01_unit_economics_revenue_slope_pct_5d_v001_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_5d_v001_signal},    "f01_unit_economics_capex_slope_pct_5d_v002_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_5d_v002_signal},    "f01_unit_economics_assets_slope_pct_5d_v003_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_5d_v003_signal},    "f01_unit_economics_rev_per_capex_slope_pct_5d_v004_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_5d_v004_signal},    "f01_unit_economics_asset_efficiency_slope_pct_5d_v005_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_5d_v005_signal},    "f01_unit_economics_revenue_slope_pct_10d_v006_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_10d_v006_signal},    "f01_unit_economics_capex_slope_pct_10d_v007_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_10d_v007_signal},    "f01_unit_economics_assets_slope_pct_10d_v008_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_10d_v008_signal},    "f01_unit_economics_rev_per_capex_slope_pct_10d_v009_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_10d_v009_signal},    "f01_unit_economics_asset_efficiency_slope_pct_10d_v010_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_10d_v010_signal},    "f01_unit_economics_revenue_slope_pct_21d_v011_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_21d_v011_signal},    "f01_unit_economics_capex_slope_pct_21d_v012_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_21d_v012_signal},    "f01_unit_economics_assets_slope_pct_21d_v013_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_21d_v013_signal},    "f01_unit_economics_rev_per_capex_slope_pct_21d_v014_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_21d_v014_signal},    "f01_unit_economics_asset_efficiency_slope_pct_21d_v015_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_21d_v015_signal},    "f01_unit_economics_revenue_slope_pct_42d_v016_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_42d_v016_signal},    "f01_unit_economics_capex_slope_pct_42d_v017_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_42d_v017_signal},    "f01_unit_economics_assets_slope_pct_42d_v018_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_42d_v018_signal},    "f01_unit_economics_rev_per_capex_slope_pct_42d_v019_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_42d_v019_signal},    "f01_unit_economics_asset_efficiency_slope_pct_42d_v020_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_42d_v020_signal},    "f01_unit_economics_revenue_slope_pct_63d_v021_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_63d_v021_signal},    "f01_unit_economics_capex_slope_pct_63d_v022_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_63d_v022_signal},    "f01_unit_economics_assets_slope_pct_63d_v023_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_63d_v023_signal},    "f01_unit_economics_rev_per_capex_slope_pct_63d_v024_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_63d_v024_signal},    "f01_unit_economics_asset_efficiency_slope_pct_63d_v025_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_63d_v025_signal},    "f01_unit_economics_revenue_slope_pct_126d_v026_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_126d_v026_signal},    "f01_unit_economics_capex_slope_pct_126d_v027_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_126d_v027_signal},    "f01_unit_economics_assets_slope_pct_126d_v028_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_126d_v028_signal},    "f01_unit_economics_rev_per_capex_slope_pct_126d_v029_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_126d_v029_signal},    "f01_unit_economics_asset_efficiency_slope_pct_126d_v030_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_126d_v030_signal},    "f01_unit_economics_revenue_slope_pct_252d_v031_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_252d_v031_signal},    "f01_unit_economics_capex_slope_pct_252d_v032_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_252d_v032_signal},    "f01_unit_economics_assets_slope_pct_252d_v033_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_252d_v033_signal},    "f01_unit_economics_rev_per_capex_slope_pct_252d_v034_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_252d_v034_signal},    "f01_unit_economics_asset_efficiency_slope_pct_252d_v035_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_252d_v035_signal},    "f01_unit_economics_revenue_slope_pct_504d_v036_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_504d_v036_signal},    "f01_unit_economics_capex_slope_pct_504d_v037_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_504d_v037_signal},    "f01_unit_economics_assets_slope_pct_504d_v038_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_504d_v038_signal},    "f01_unit_economics_rev_per_capex_slope_pct_504d_v039_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_504d_v039_signal},    "f01_unit_economics_asset_efficiency_slope_pct_504d_v040_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_504d_v040_signal},    "f01_unit_economics_revenue_slope_pct_756d_v041_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_756d_v041_signal},    "f01_unit_economics_capex_slope_pct_756d_v042_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_756d_v042_signal},    "f01_unit_economics_assets_slope_pct_756d_v043_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_756d_v043_signal},    "f01_unit_economics_rev_per_capex_slope_pct_756d_v044_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_756d_v044_signal},    "f01_unit_economics_asset_efficiency_slope_pct_756d_v045_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_756d_v045_signal},    "f01_unit_economics_revenue_slope_pct_1008d_v046_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_1008d_v046_signal},    "f01_unit_economics_capex_slope_pct_1008d_v047_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_1008d_v047_signal},    "f01_unit_economics_assets_slope_pct_1008d_v048_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_1008d_v048_signal},    "f01_unit_economics_rev_per_capex_slope_pct_1008d_v049_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_1008d_v049_signal},    "f01_unit_economics_asset_efficiency_slope_pct_1008d_v050_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_1008d_v050_signal},    "f01_unit_economics_revenue_slope_pct_1260d_v051_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_pct_1260d_v051_signal},    "f01_unit_economics_capex_slope_pct_1260d_v052_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_pct_1260d_v052_signal},    "f01_unit_economics_assets_slope_pct_1260d_v053_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_pct_1260d_v053_signal},    "f01_unit_economics_rev_per_capex_slope_pct_1260d_v054_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_pct_1260d_v054_signal},    "f01_unit_economics_asset_efficiency_slope_pct_1260d_v055_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_pct_1260d_v055_signal},    "f01_unit_economics_revenue_jerk_5d_v056_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_5d_v056_signal},    "f01_unit_economics_capex_jerk_5d_v057_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_5d_v057_signal},    "f01_unit_economics_assets_jerk_5d_v058_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_5d_v058_signal},    "f01_unit_economics_rev_per_capex_jerk_5d_v059_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_5d_v059_signal},    "f01_unit_economics_asset_efficiency_jerk_5d_v060_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_5d_v060_signal},    "f01_unit_economics_revenue_jerk_10d_v061_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_10d_v061_signal},    "f01_unit_economics_capex_jerk_10d_v062_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_10d_v062_signal},    "f01_unit_economics_assets_jerk_10d_v063_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_10d_v063_signal},    "f01_unit_economics_rev_per_capex_jerk_10d_v064_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_10d_v064_signal},    "f01_unit_economics_asset_efficiency_jerk_10d_v065_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_10d_v065_signal},    "f01_unit_economics_revenue_jerk_21d_v066_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_21d_v066_signal},    "f01_unit_economics_capex_jerk_21d_v067_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_21d_v067_signal},    "f01_unit_economics_assets_jerk_21d_v068_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_21d_v068_signal},    "f01_unit_economics_rev_per_capex_jerk_21d_v069_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_21d_v069_signal},    "f01_unit_economics_asset_efficiency_jerk_21d_v070_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_21d_v070_signal},    "f01_unit_economics_revenue_jerk_42d_v071_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_42d_v071_signal},    "f01_unit_economics_capex_jerk_42d_v072_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_42d_v072_signal},    "f01_unit_economics_assets_jerk_42d_v073_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_42d_v073_signal},    "f01_unit_economics_rev_per_capex_jerk_42d_v074_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_42d_v074_signal},    "f01_unit_economics_asset_efficiency_jerk_42d_v075_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_42d_v075_signal},    "f01_unit_economics_revenue_jerk_63d_v076_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_63d_v076_signal},    "f01_unit_economics_capex_jerk_63d_v077_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_63d_v077_signal},    "f01_unit_economics_assets_jerk_63d_v078_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_63d_v078_signal},    "f01_unit_economics_rev_per_capex_jerk_63d_v079_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_63d_v079_signal},    "f01_unit_economics_asset_efficiency_jerk_63d_v080_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_63d_v080_signal},    "f01_unit_economics_revenue_jerk_126d_v081_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_126d_v081_signal},    "f01_unit_economics_capex_jerk_126d_v082_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_126d_v082_signal},    "f01_unit_economics_assets_jerk_126d_v083_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_126d_v083_signal},    "f01_unit_economics_rev_per_capex_jerk_126d_v084_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_126d_v084_signal},    "f01_unit_economics_asset_efficiency_jerk_126d_v085_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_126d_v085_signal},    "f01_unit_economics_revenue_jerk_252d_v086_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_252d_v086_signal},    "f01_unit_economics_capex_jerk_252d_v087_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_252d_v087_signal},    "f01_unit_economics_assets_jerk_252d_v088_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_252d_v088_signal},    "f01_unit_economics_rev_per_capex_jerk_252d_v089_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_252d_v089_signal},    "f01_unit_economics_asset_efficiency_jerk_252d_v090_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_252d_v090_signal},    "f01_unit_economics_revenue_jerk_504d_v091_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_504d_v091_signal},    "f01_unit_economics_capex_jerk_504d_v092_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_504d_v092_signal},    "f01_unit_economics_assets_jerk_504d_v093_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_504d_v093_signal},    "f01_unit_economics_rev_per_capex_jerk_504d_v094_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_504d_v094_signal},    "f01_unit_economics_asset_efficiency_jerk_504d_v095_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_504d_v095_signal},    "f01_unit_economics_revenue_jerk_756d_v096_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_756d_v096_signal},    "f01_unit_economics_capex_jerk_756d_v097_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_756d_v097_signal},    "f01_unit_economics_assets_jerk_756d_v098_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_756d_v098_signal},    "f01_unit_economics_rev_per_capex_jerk_756d_v099_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_756d_v099_signal},    "f01_unit_economics_asset_efficiency_jerk_756d_v100_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_756d_v100_signal},    "f01_unit_economics_revenue_jerk_1008d_v101_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_1008d_v101_signal},    "f01_unit_economics_capex_jerk_1008d_v102_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_1008d_v102_signal},    "f01_unit_economics_assets_jerk_1008d_v103_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_1008d_v103_signal},    "f01_unit_economics_rev_per_capex_jerk_1008d_v104_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_1008d_v104_signal},    "f01_unit_economics_asset_efficiency_jerk_1008d_v105_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_1008d_v105_signal},    "f01_unit_economics_revenue_jerk_1260d_v106_signal": {"inputs": [], "func": f01_unit_economics_revenue_jerk_1260d_v106_signal},    "f01_unit_economics_capex_jerk_1260d_v107_signal": {"inputs": [], "func": f01_unit_economics_capex_jerk_1260d_v107_signal},    "f01_unit_economics_assets_jerk_1260d_v108_signal": {"inputs": [], "func": f01_unit_economics_assets_jerk_1260d_v108_signal},    "f01_unit_economics_rev_per_capex_jerk_1260d_v109_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_jerk_1260d_v109_signal},    "f01_unit_economics_asset_efficiency_jerk_1260d_v110_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_jerk_1260d_v110_signal},    "f01_unit_economics_revenue_slope_diff_norm_5d_v111_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_5d_v111_signal},    "f01_unit_economics_capex_slope_diff_norm_5d_v112_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_5d_v112_signal},    "f01_unit_economics_assets_slope_diff_norm_5d_v113_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_5d_v113_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_5d_v114_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_5d_v114_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_5d_v115_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_5d_v115_signal},    "f01_unit_economics_revenue_slope_diff_norm_10d_v116_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_10d_v116_signal},    "f01_unit_economics_capex_slope_diff_norm_10d_v117_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_10d_v117_signal},    "f01_unit_economics_assets_slope_diff_norm_10d_v118_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_10d_v118_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_10d_v119_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_10d_v119_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_10d_v120_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_10d_v120_signal},    "f01_unit_economics_revenue_slope_diff_norm_21d_v121_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_21d_v121_signal},    "f01_unit_economics_capex_slope_diff_norm_21d_v122_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_21d_v122_signal},    "f01_unit_economics_assets_slope_diff_norm_21d_v123_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_21d_v123_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_21d_v124_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_21d_v124_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_21d_v125_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_21d_v125_signal},    "f01_unit_economics_revenue_slope_diff_norm_42d_v126_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_42d_v126_signal},    "f01_unit_economics_capex_slope_diff_norm_42d_v127_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_42d_v127_signal},    "f01_unit_economics_assets_slope_diff_norm_42d_v128_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_42d_v128_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_42d_v129_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_42d_v129_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_42d_v130_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_42d_v130_signal},    "f01_unit_economics_revenue_slope_diff_norm_63d_v131_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_63d_v131_signal},    "f01_unit_economics_capex_slope_diff_norm_63d_v132_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_63d_v132_signal},    "f01_unit_economics_assets_slope_diff_norm_63d_v133_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_63d_v133_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_63d_v134_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_63d_v134_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_63d_v135_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_63d_v135_signal},    "f01_unit_economics_revenue_slope_diff_norm_126d_v136_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_126d_v136_signal},    "f01_unit_economics_capex_slope_diff_norm_126d_v137_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_126d_v137_signal},    "f01_unit_economics_assets_slope_diff_norm_126d_v138_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_126d_v138_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_126d_v139_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_126d_v139_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_126d_v140_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_126d_v140_signal},    "f01_unit_economics_revenue_slope_diff_norm_252d_v141_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_252d_v141_signal},    "f01_unit_economics_capex_slope_diff_norm_252d_v142_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_252d_v142_signal},    "f01_unit_economics_assets_slope_diff_norm_252d_v143_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_252d_v143_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_252d_v144_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_252d_v144_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_252d_v145_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_252d_v145_signal},    "f01_unit_economics_revenue_slope_diff_norm_504d_v146_signal": {"inputs": [], "func": f01_unit_economics_revenue_slope_diff_norm_504d_v146_signal},    "f01_unit_economics_capex_slope_diff_norm_504d_v147_signal": {"inputs": [], "func": f01_unit_economics_capex_slope_diff_norm_504d_v147_signal},    "f01_unit_economics_assets_slope_diff_norm_504d_v148_signal": {"inputs": [], "func": f01_unit_economics_assets_slope_diff_norm_504d_v148_signal},    "f01_unit_economics_rev_per_capex_slope_diff_norm_504d_v149_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_slope_diff_norm_504d_v149_signal},    "f01_unit_economics_asset_efficiency_slope_diff_norm_504d_v150_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_slope_diff_norm_504d_v150_signal},
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
