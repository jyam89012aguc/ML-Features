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

def f29_innovation_roi_rnd_base_5d_v001_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 5d window."""
    res = _sma(rnd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_5d_v002_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_5d_v003_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 5d window."""
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_5d_v004_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 5d window."""
    res = _sma(_ratio(revenue, rnd), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_10d_v005_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 10d window."""
    res = _sma(rnd, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_10d_v006_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_10d_v007_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 10d window."""
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_10d_v008_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 10d window."""
    res = _sma(_ratio(revenue, rnd), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_21d_v009_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 21d window."""
    res = _sma(rnd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_21d_v010_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_21d_v011_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 21d window."""
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_21d_v012_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 21d window."""
    res = _sma(_ratio(revenue, rnd), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_42d_v013_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 42d window."""
    res = _sma(rnd, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_42d_v014_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_42d_v015_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 42d window."""
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_42d_v016_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 42d window."""
    res = _sma(_ratio(revenue, rnd), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_63d_v017_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 63d window."""
    res = _sma(rnd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_63d_v018_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_63d_v019_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 63d window."""
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_63d_v020_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 63d window."""
    res = _sma(_ratio(revenue, rnd), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_126d_v021_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 126d window."""
    res = _sma(rnd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_126d_v022_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_126d_v023_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 126d window."""
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_126d_v024_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 126d window."""
    res = _sma(_ratio(revenue, rnd), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_252d_v025_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 252d window."""
    res = _sma(rnd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_252d_v026_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_252d_v027_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 252d window."""
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_252d_v028_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 252d window."""
    res = _sma(_ratio(revenue, rnd), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_504d_v029_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 504d window."""
    res = _sma(rnd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_504d_v030_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_504d_v031_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 504d window."""
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_504d_v032_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 504d window."""
    res = _sma(_ratio(revenue, rnd), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_756d_v033_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 756d window."""
    res = _sma(rnd, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_756d_v034_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_756d_v035_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 756d window."""
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_756d_v036_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 756d window."""
    res = _sma(_ratio(revenue, rnd), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_1008d_v037_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 1008d window."""
    res = _sma(rnd, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_1008d_v038_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_1008d_v039_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 1008d window."""
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_1008d_v040_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 1008d window."""
    res = _sma(_ratio(revenue, rnd), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_base_1260d_v041_signal(rnd):
    """Moving average to smooth noise of Raw level of rnd over 1260d window."""
    res = _sma(rnd, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_base_1260d_v042_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_base_1260d_v043_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 1260d window."""
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_base_1260d_v044_signal(revenue, rnd):
    """Moving average to smooth noise of Sales productivity of R&D investment over 1260d window."""
    res = _sma(_ratio(revenue, rnd), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_5d_v045_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 5d window."""
    res = _z(rnd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_5d_v046_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_5d_v047_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 5d window."""
    res = _z(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_5d_v048_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 5d window."""
    res = _z(_ratio(revenue, rnd), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_10d_v049_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 10d window."""
    res = _z(rnd, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_10d_v050_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_10d_v051_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 10d window."""
    res = _z(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_10d_v052_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 10d window."""
    res = _z(_ratio(revenue, rnd), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_21d_v053_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 21d window."""
    res = _z(rnd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_21d_v054_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_21d_v055_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 21d window."""
    res = _z(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_21d_v056_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 21d window."""
    res = _z(_ratio(revenue, rnd), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_42d_v057_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 42d window."""
    res = _z(rnd, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_42d_v058_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_42d_v059_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 42d window."""
    res = _z(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_42d_v060_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 42d window."""
    res = _z(_ratio(revenue, rnd), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_63d_v061_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 63d window."""
    res = _z(rnd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_63d_v062_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_63d_v063_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 63d window."""
    res = _z(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_63d_v064_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 63d window."""
    res = _z(_ratio(revenue, rnd), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_126d_v065_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 126d window."""
    res = _z(rnd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_126d_v066_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_126d_v067_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 126d window."""
    res = _z(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_126d_v068_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 126d window."""
    res = _z(_ratio(revenue, rnd), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_252d_v069_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 252d window."""
    res = _z(rnd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_252d_v070_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_252d_v071_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 252d window."""
    res = _z(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_leverage_z_252d_v072_signal(revenue, rnd):
    """Z-score for relative outlier detection of Sales productivity of R&D investment over 252d window."""
    res = _z(_ratio(revenue, rnd), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_rnd_z_504d_v073_signal(rnd):
    """Z-score for relative outlier detection of Raw level of rnd over 504d window."""
    res = _z(rnd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_revenue_z_504d_v074_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_innovation_roi_inventory_z_504d_v075_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 504d window."""
    res = _z(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f29_innovation_roi_rnd_base_5d_v001_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_5d_v001_signal},    "f29_innovation_roi_revenue_base_5d_v002_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_5d_v002_signal},    "f29_innovation_roi_inventory_base_5d_v003_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_5d_v003_signal},    "f29_innovation_roi_rnd_leverage_base_5d_v004_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_5d_v004_signal},    "f29_innovation_roi_rnd_base_10d_v005_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_10d_v005_signal},    "f29_innovation_roi_revenue_base_10d_v006_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_10d_v006_signal},    "f29_innovation_roi_inventory_base_10d_v007_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_10d_v007_signal},    "f29_innovation_roi_rnd_leverage_base_10d_v008_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_10d_v008_signal},    "f29_innovation_roi_rnd_base_21d_v009_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_21d_v009_signal},    "f29_innovation_roi_revenue_base_21d_v010_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_21d_v010_signal},    "f29_innovation_roi_inventory_base_21d_v011_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_21d_v011_signal},    "f29_innovation_roi_rnd_leverage_base_21d_v012_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_21d_v012_signal},    "f29_innovation_roi_rnd_base_42d_v013_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_42d_v013_signal},    "f29_innovation_roi_revenue_base_42d_v014_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_42d_v014_signal},    "f29_innovation_roi_inventory_base_42d_v015_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_42d_v015_signal},    "f29_innovation_roi_rnd_leverage_base_42d_v016_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_42d_v016_signal},    "f29_innovation_roi_rnd_base_63d_v017_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_63d_v017_signal},    "f29_innovation_roi_revenue_base_63d_v018_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_63d_v018_signal},    "f29_innovation_roi_inventory_base_63d_v019_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_63d_v019_signal},    "f29_innovation_roi_rnd_leverage_base_63d_v020_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_63d_v020_signal},    "f29_innovation_roi_rnd_base_126d_v021_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_126d_v021_signal},    "f29_innovation_roi_revenue_base_126d_v022_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_126d_v022_signal},    "f29_innovation_roi_inventory_base_126d_v023_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_126d_v023_signal},    "f29_innovation_roi_rnd_leverage_base_126d_v024_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_126d_v024_signal},    "f29_innovation_roi_rnd_base_252d_v025_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_252d_v025_signal},    "f29_innovation_roi_revenue_base_252d_v026_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_252d_v026_signal},    "f29_innovation_roi_inventory_base_252d_v027_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_252d_v027_signal},    "f29_innovation_roi_rnd_leverage_base_252d_v028_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_252d_v028_signal},    "f29_innovation_roi_rnd_base_504d_v029_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_504d_v029_signal},    "f29_innovation_roi_revenue_base_504d_v030_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_504d_v030_signal},    "f29_innovation_roi_inventory_base_504d_v031_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_504d_v031_signal},    "f29_innovation_roi_rnd_leverage_base_504d_v032_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_504d_v032_signal},    "f29_innovation_roi_rnd_base_756d_v033_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_756d_v033_signal},    "f29_innovation_roi_revenue_base_756d_v034_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_756d_v034_signal},    "f29_innovation_roi_inventory_base_756d_v035_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_756d_v035_signal},    "f29_innovation_roi_rnd_leverage_base_756d_v036_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_756d_v036_signal},    "f29_innovation_roi_rnd_base_1008d_v037_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_1008d_v037_signal},    "f29_innovation_roi_revenue_base_1008d_v038_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_1008d_v038_signal},    "f29_innovation_roi_inventory_base_1008d_v039_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_1008d_v039_signal},    "f29_innovation_roi_rnd_leverage_base_1008d_v040_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_1008d_v040_signal},    "f29_innovation_roi_rnd_base_1260d_v041_signal": {"inputs": [], "func": f29_innovation_roi_rnd_base_1260d_v041_signal},    "f29_innovation_roi_revenue_base_1260d_v042_signal": {"inputs": [], "func": f29_innovation_roi_revenue_base_1260d_v042_signal},    "f29_innovation_roi_inventory_base_1260d_v043_signal": {"inputs": [], "func": f29_innovation_roi_inventory_base_1260d_v043_signal},    "f29_innovation_roi_rnd_leverage_base_1260d_v044_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_base_1260d_v044_signal},    "f29_innovation_roi_rnd_z_5d_v045_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_5d_v045_signal},    "f29_innovation_roi_revenue_z_5d_v046_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_5d_v046_signal},    "f29_innovation_roi_inventory_z_5d_v047_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_5d_v047_signal},    "f29_innovation_roi_rnd_leverage_z_5d_v048_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_5d_v048_signal},    "f29_innovation_roi_rnd_z_10d_v049_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_10d_v049_signal},    "f29_innovation_roi_revenue_z_10d_v050_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_10d_v050_signal},    "f29_innovation_roi_inventory_z_10d_v051_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_10d_v051_signal},    "f29_innovation_roi_rnd_leverage_z_10d_v052_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_10d_v052_signal},    "f29_innovation_roi_rnd_z_21d_v053_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_21d_v053_signal},    "f29_innovation_roi_revenue_z_21d_v054_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_21d_v054_signal},    "f29_innovation_roi_inventory_z_21d_v055_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_21d_v055_signal},    "f29_innovation_roi_rnd_leverage_z_21d_v056_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_21d_v056_signal},    "f29_innovation_roi_rnd_z_42d_v057_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_42d_v057_signal},    "f29_innovation_roi_revenue_z_42d_v058_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_42d_v058_signal},    "f29_innovation_roi_inventory_z_42d_v059_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_42d_v059_signal},    "f29_innovation_roi_rnd_leverage_z_42d_v060_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_42d_v060_signal},    "f29_innovation_roi_rnd_z_63d_v061_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_63d_v061_signal},    "f29_innovation_roi_revenue_z_63d_v062_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_63d_v062_signal},    "f29_innovation_roi_inventory_z_63d_v063_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_63d_v063_signal},    "f29_innovation_roi_rnd_leverage_z_63d_v064_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_63d_v064_signal},    "f29_innovation_roi_rnd_z_126d_v065_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_126d_v065_signal},    "f29_innovation_roi_revenue_z_126d_v066_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_126d_v066_signal},    "f29_innovation_roi_inventory_z_126d_v067_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_126d_v067_signal},    "f29_innovation_roi_rnd_leverage_z_126d_v068_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_126d_v068_signal},    "f29_innovation_roi_rnd_z_252d_v069_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_252d_v069_signal},    "f29_innovation_roi_revenue_z_252d_v070_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_252d_v070_signal},    "f29_innovation_roi_inventory_z_252d_v071_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_252d_v071_signal},    "f29_innovation_roi_rnd_leverage_z_252d_v072_signal": {"inputs": [], "func": f29_innovation_roi_rnd_leverage_z_252d_v072_signal},    "f29_innovation_roi_rnd_z_504d_v073_signal": {"inputs": [], "func": f29_innovation_roi_rnd_z_504d_v073_signal},    "f29_innovation_roi_revenue_z_504d_v074_signal": {"inputs": [], "func": f29_innovation_roi_revenue_z_504d_v074_signal},    "f29_innovation_roi_inventory_z_504d_v075_signal": {"inputs": [], "func": f29_innovation_roi_inventory_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 29...")
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
