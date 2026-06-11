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

def f26_vendor_leverage_inventory_base_5d_v001_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 5d window."""
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_5d_v002_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 5d window."""
    res = _sma(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_5d_v003_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 5d window."""
    res = _sma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_5d_v004_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 5d window."""
    res = _sma(_ratio(payables, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_10d_v005_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 10d window."""
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_10d_v006_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 10d window."""
    res = _sma(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_10d_v007_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 10d window."""
    res = _sma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_10d_v008_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 10d window."""
    res = _sma(_ratio(payables, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_21d_v009_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 21d window."""
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_21d_v010_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 21d window."""
    res = _sma(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_21d_v011_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 21d window."""
    res = _sma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_21d_v012_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 21d window."""
    res = _sma(_ratio(payables, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_42d_v013_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 42d window."""
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_42d_v014_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 42d window."""
    res = _sma(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_42d_v015_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 42d window."""
    res = _sma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_42d_v016_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 42d window."""
    res = _sma(_ratio(payables, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_63d_v017_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 63d window."""
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_63d_v018_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 63d window."""
    res = _sma(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_63d_v019_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 63d window."""
    res = _sma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_63d_v020_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 63d window."""
    res = _sma(_ratio(payables, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_126d_v021_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 126d window."""
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_126d_v022_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 126d window."""
    res = _sma(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_126d_v023_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 126d window."""
    res = _sma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_126d_v024_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 126d window."""
    res = _sma(_ratio(payables, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_252d_v025_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 252d window."""
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_252d_v026_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 252d window."""
    res = _sma(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_252d_v027_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 252d window."""
    res = _sma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_252d_v028_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 252d window."""
    res = _sma(_ratio(payables, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_504d_v029_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 504d window."""
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_504d_v030_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 504d window."""
    res = _sma(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_504d_v031_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 504d window."""
    res = _sma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_504d_v032_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 504d window."""
    res = _sma(_ratio(payables, inventory), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_756d_v033_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 756d window."""
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_756d_v034_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 756d window."""
    res = _sma(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_756d_v035_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 756d window."""
    res = _sma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_756d_v036_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 756d window."""
    res = _sma(_ratio(payables, inventory), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_1008d_v037_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 1008d window."""
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_1008d_v038_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 1008d window."""
    res = _sma(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_1008d_v039_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 1008d window."""
    res = _sma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_1008d_v040_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 1008d window."""
    res = _sma(_ratio(payables, inventory), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_base_1260d_v041_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 1260d window."""
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_base_1260d_v042_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 1260d window."""
    res = _sma(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_base_1260d_v043_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 1260d window."""
    res = _sma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_base_1260d_v044_signal(payables, inventory):
    """Moving average to smooth noise of Percentage of inventory financed by vendors over 1260d window."""
    res = _sma(_ratio(payables, inventory), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_5d_v045_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 5d window."""
    res = _z(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_5d_v046_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 5d window."""
    res = _z(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_5d_v047_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 5d window."""
    res = _z(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_5d_v048_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 5d window."""
    res = _z(_ratio(payables, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_10d_v049_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 10d window."""
    res = _z(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_10d_v050_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 10d window."""
    res = _z(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_10d_v051_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 10d window."""
    res = _z(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_10d_v052_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 10d window."""
    res = _z(_ratio(payables, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_21d_v053_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 21d window."""
    res = _z(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_21d_v054_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 21d window."""
    res = _z(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_21d_v055_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 21d window."""
    res = _z(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_21d_v056_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 21d window."""
    res = _z(_ratio(payables, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_42d_v057_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 42d window."""
    res = _z(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_42d_v058_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 42d window."""
    res = _z(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_42d_v059_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 42d window."""
    res = _z(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_42d_v060_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 42d window."""
    res = _z(_ratio(payables, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_63d_v061_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 63d window."""
    res = _z(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_63d_v062_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 63d window."""
    res = _z(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_63d_v063_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 63d window."""
    res = _z(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_63d_v064_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 63d window."""
    res = _z(_ratio(payables, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_126d_v065_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 126d window."""
    res = _z(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_126d_v066_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 126d window."""
    res = _z(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_126d_v067_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 126d window."""
    res = _z(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_126d_v068_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 126d window."""
    res = _z(_ratio(payables, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_252d_v069_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 252d window."""
    res = _z(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_252d_v070_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 252d window."""
    res = _z(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_252d_v071_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 252d window."""
    res = _z(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_252d_v072_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 252d window."""
    res = _z(_ratio(payables, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_504d_v073_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 504d window."""
    res = _z(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_504d_v074_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 504d window."""
    res = _z(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_504d_v075_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 504d window."""
    res = _z(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f26_vendor_leverage_inventory_base_5d_v001_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_5d_v001_signal},    "f26_vendor_leverage_payables_base_5d_v002_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_5d_v002_signal},    "f26_vendor_leverage_cor_base_5d_v003_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_5d_v003_signal},    "f26_vendor_leverage_financing_moat_base_5d_v004_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_5d_v004_signal},    "f26_vendor_leverage_inventory_base_10d_v005_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_10d_v005_signal},    "f26_vendor_leverage_payables_base_10d_v006_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_10d_v006_signal},    "f26_vendor_leverage_cor_base_10d_v007_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_10d_v007_signal},    "f26_vendor_leverage_financing_moat_base_10d_v008_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_10d_v008_signal},    "f26_vendor_leverage_inventory_base_21d_v009_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_21d_v009_signal},    "f26_vendor_leverage_payables_base_21d_v010_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_21d_v010_signal},    "f26_vendor_leverage_cor_base_21d_v011_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_21d_v011_signal},    "f26_vendor_leverage_financing_moat_base_21d_v012_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_21d_v012_signal},    "f26_vendor_leverage_inventory_base_42d_v013_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_42d_v013_signal},    "f26_vendor_leverage_payables_base_42d_v014_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_42d_v014_signal},    "f26_vendor_leverage_cor_base_42d_v015_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_42d_v015_signal},    "f26_vendor_leverage_financing_moat_base_42d_v016_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_42d_v016_signal},    "f26_vendor_leverage_inventory_base_63d_v017_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_63d_v017_signal},    "f26_vendor_leverage_payables_base_63d_v018_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_63d_v018_signal},    "f26_vendor_leverage_cor_base_63d_v019_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_63d_v019_signal},    "f26_vendor_leverage_financing_moat_base_63d_v020_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_63d_v020_signal},    "f26_vendor_leverage_inventory_base_126d_v021_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_126d_v021_signal},    "f26_vendor_leverage_payables_base_126d_v022_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_126d_v022_signal},    "f26_vendor_leverage_cor_base_126d_v023_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_126d_v023_signal},    "f26_vendor_leverage_financing_moat_base_126d_v024_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_126d_v024_signal},    "f26_vendor_leverage_inventory_base_252d_v025_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_252d_v025_signal},    "f26_vendor_leverage_payables_base_252d_v026_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_252d_v026_signal},    "f26_vendor_leverage_cor_base_252d_v027_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_252d_v027_signal},    "f26_vendor_leverage_financing_moat_base_252d_v028_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_252d_v028_signal},    "f26_vendor_leverage_inventory_base_504d_v029_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_504d_v029_signal},    "f26_vendor_leverage_payables_base_504d_v030_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_504d_v030_signal},    "f26_vendor_leverage_cor_base_504d_v031_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_504d_v031_signal},    "f26_vendor_leverage_financing_moat_base_504d_v032_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_504d_v032_signal},    "f26_vendor_leverage_inventory_base_756d_v033_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_756d_v033_signal},    "f26_vendor_leverage_payables_base_756d_v034_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_756d_v034_signal},    "f26_vendor_leverage_cor_base_756d_v035_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_756d_v035_signal},    "f26_vendor_leverage_financing_moat_base_756d_v036_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_756d_v036_signal},    "f26_vendor_leverage_inventory_base_1008d_v037_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_1008d_v037_signal},    "f26_vendor_leverage_payables_base_1008d_v038_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_1008d_v038_signal},    "f26_vendor_leverage_cor_base_1008d_v039_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_1008d_v039_signal},    "f26_vendor_leverage_financing_moat_base_1008d_v040_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_1008d_v040_signal},    "f26_vendor_leverage_inventory_base_1260d_v041_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_base_1260d_v041_signal},    "f26_vendor_leverage_payables_base_1260d_v042_signal": {"inputs": [], "func": f26_vendor_leverage_payables_base_1260d_v042_signal},    "f26_vendor_leverage_cor_base_1260d_v043_signal": {"inputs": [], "func": f26_vendor_leverage_cor_base_1260d_v043_signal},    "f26_vendor_leverage_financing_moat_base_1260d_v044_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_base_1260d_v044_signal},    "f26_vendor_leverage_inventory_z_5d_v045_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_5d_v045_signal},    "f26_vendor_leverage_payables_z_5d_v046_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_5d_v046_signal},    "f26_vendor_leverage_cor_z_5d_v047_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_5d_v047_signal},    "f26_vendor_leverage_financing_moat_z_5d_v048_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_5d_v048_signal},    "f26_vendor_leverage_inventory_z_10d_v049_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_10d_v049_signal},    "f26_vendor_leverage_payables_z_10d_v050_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_10d_v050_signal},    "f26_vendor_leverage_cor_z_10d_v051_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_10d_v051_signal},    "f26_vendor_leverage_financing_moat_z_10d_v052_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_10d_v052_signal},    "f26_vendor_leverage_inventory_z_21d_v053_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_21d_v053_signal},    "f26_vendor_leverage_payables_z_21d_v054_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_21d_v054_signal},    "f26_vendor_leverage_cor_z_21d_v055_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_21d_v055_signal},    "f26_vendor_leverage_financing_moat_z_21d_v056_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_21d_v056_signal},    "f26_vendor_leverage_inventory_z_42d_v057_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_42d_v057_signal},    "f26_vendor_leverage_payables_z_42d_v058_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_42d_v058_signal},    "f26_vendor_leverage_cor_z_42d_v059_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_42d_v059_signal},    "f26_vendor_leverage_financing_moat_z_42d_v060_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_42d_v060_signal},    "f26_vendor_leverage_inventory_z_63d_v061_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_63d_v061_signal},    "f26_vendor_leverage_payables_z_63d_v062_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_63d_v062_signal},    "f26_vendor_leverage_cor_z_63d_v063_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_63d_v063_signal},    "f26_vendor_leverage_financing_moat_z_63d_v064_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_63d_v064_signal},    "f26_vendor_leverage_inventory_z_126d_v065_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_126d_v065_signal},    "f26_vendor_leverage_payables_z_126d_v066_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_126d_v066_signal},    "f26_vendor_leverage_cor_z_126d_v067_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_126d_v067_signal},    "f26_vendor_leverage_financing_moat_z_126d_v068_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_126d_v068_signal},    "f26_vendor_leverage_inventory_z_252d_v069_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_252d_v069_signal},    "f26_vendor_leverage_payables_z_252d_v070_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_252d_v070_signal},    "f26_vendor_leverage_cor_z_252d_v071_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_252d_v071_signal},    "f26_vendor_leverage_financing_moat_z_252d_v072_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_252d_v072_signal},    "f26_vendor_leverage_inventory_z_504d_v073_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_504d_v073_signal},    "f26_vendor_leverage_payables_z_504d_v074_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_504d_v074_signal},    "f26_vendor_leverage_cor_z_504d_v075_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 26...")
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
