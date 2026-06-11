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

def f10_retail_working_capital_inventory_base_5d_v001_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 5d window."""
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_5d_v002_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 5d window."""
    res = _sma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_5d_v003_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 5d window."""
    res = _sma(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_5d_v004_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_5d_v005_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 5d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_10d_v006_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 10d window."""
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_10d_v007_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 10d window."""
    res = _sma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_10d_v008_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 10d window."""
    res = _sma(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_10d_v009_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_10d_v010_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 10d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_21d_v011_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 21d window."""
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_21d_v012_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 21d window."""
    res = _sma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_21d_v013_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 21d window."""
    res = _sma(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_21d_v014_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_21d_v015_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 21d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_42d_v016_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 42d window."""
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_42d_v017_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 42d window."""
    res = _sma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_42d_v018_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 42d window."""
    res = _sma(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_42d_v019_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_42d_v020_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 42d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_63d_v021_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 63d window."""
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_63d_v022_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 63d window."""
    res = _sma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_63d_v023_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 63d window."""
    res = _sma(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_63d_v024_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_63d_v025_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 63d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_126d_v026_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 126d window."""
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_126d_v027_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 126d window."""
    res = _sma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_126d_v028_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 126d window."""
    res = _sma(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_126d_v029_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_126d_v030_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 126d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_252d_v031_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 252d window."""
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_252d_v032_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 252d window."""
    res = _sma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_252d_v033_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 252d window."""
    res = _sma(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_252d_v034_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_252d_v035_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 252d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_504d_v036_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 504d window."""
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_504d_v037_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 504d window."""
    res = _sma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_504d_v038_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 504d window."""
    res = _sma(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_504d_v039_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_504d_v040_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 504d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_756d_v041_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 756d window."""
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_756d_v042_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 756d window."""
    res = _sma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_756d_v043_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 756d window."""
    res = _sma(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_756d_v044_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_756d_v045_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 756d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_1008d_v046_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 1008d window."""
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_1008d_v047_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 1008d window."""
    res = _sma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_1008d_v048_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 1008d window."""
    res = _sma(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_1008d_v049_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_1008d_v050_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 1008d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_base_1260d_v051_signal(inventory):
    """Moving average to smooth noise of Raw level of inventory over 1260d window."""
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_base_1260d_v052_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 1260d window."""
    res = _sma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_base_1260d_v053_signal(payables):
    """Moving average to smooth noise of Raw level of payables over 1260d window."""
    res = _sma(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_base_1260d_v054_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_base_1260d_v055_signal(inventory, receivables, payables, revenue):
    """Moving average to smooth noise of Working capital load per dollar of sales over 1260d window."""
    res = _sma(_ratio(inventory + receivables - payables, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_5d_v056_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 5d window."""
    res = _z(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_5d_v057_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 5d window."""
    res = _z(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_5d_v058_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 5d window."""
    res = _z(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_5d_v059_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_5d_v060_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 5d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_10d_v061_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 10d window."""
    res = _z(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_10d_v062_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 10d window."""
    res = _z(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_10d_v063_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 10d window."""
    res = _z(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_10d_v064_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_10d_v065_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 10d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_21d_v066_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 21d window."""
    res = _z(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_21d_v067_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 21d window."""
    res = _z(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_21d_v068_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 21d window."""
    res = _z(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_21d_v069_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_21d_v070_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 21d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_42d_v071_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 42d window."""
    res = _z(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_42d_v072_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 42d window."""
    res = _z(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_42d_v073_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 42d window."""
    res = _z(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_42d_v074_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_42d_v075_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 42d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_retail_working_capital_inventory_base_5d_v001_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_5d_v001_signal},    "f10_retail_working_capital_receivables_base_5d_v002_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_5d_v002_signal},    "f10_retail_working_capital_payables_base_5d_v003_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_5d_v003_signal},    "f10_retail_working_capital_revenue_base_5d_v004_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_5d_v004_signal},    "f10_retail_working_capital_wc_drag_base_5d_v005_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_5d_v005_signal},    "f10_retail_working_capital_inventory_base_10d_v006_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_10d_v006_signal},    "f10_retail_working_capital_receivables_base_10d_v007_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_10d_v007_signal},    "f10_retail_working_capital_payables_base_10d_v008_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_10d_v008_signal},    "f10_retail_working_capital_revenue_base_10d_v009_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_10d_v009_signal},    "f10_retail_working_capital_wc_drag_base_10d_v010_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_10d_v010_signal},    "f10_retail_working_capital_inventory_base_21d_v011_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_21d_v011_signal},    "f10_retail_working_capital_receivables_base_21d_v012_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_21d_v012_signal},    "f10_retail_working_capital_payables_base_21d_v013_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_21d_v013_signal},    "f10_retail_working_capital_revenue_base_21d_v014_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_21d_v014_signal},    "f10_retail_working_capital_wc_drag_base_21d_v015_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_21d_v015_signal},    "f10_retail_working_capital_inventory_base_42d_v016_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_42d_v016_signal},    "f10_retail_working_capital_receivables_base_42d_v017_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_42d_v017_signal},    "f10_retail_working_capital_payables_base_42d_v018_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_42d_v018_signal},    "f10_retail_working_capital_revenue_base_42d_v019_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_42d_v019_signal},    "f10_retail_working_capital_wc_drag_base_42d_v020_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_42d_v020_signal},    "f10_retail_working_capital_inventory_base_63d_v021_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_63d_v021_signal},    "f10_retail_working_capital_receivables_base_63d_v022_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_63d_v022_signal},    "f10_retail_working_capital_payables_base_63d_v023_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_63d_v023_signal},    "f10_retail_working_capital_revenue_base_63d_v024_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_63d_v024_signal},    "f10_retail_working_capital_wc_drag_base_63d_v025_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_63d_v025_signal},    "f10_retail_working_capital_inventory_base_126d_v026_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_126d_v026_signal},    "f10_retail_working_capital_receivables_base_126d_v027_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_126d_v027_signal},    "f10_retail_working_capital_payables_base_126d_v028_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_126d_v028_signal},    "f10_retail_working_capital_revenue_base_126d_v029_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_126d_v029_signal},    "f10_retail_working_capital_wc_drag_base_126d_v030_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_126d_v030_signal},    "f10_retail_working_capital_inventory_base_252d_v031_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_252d_v031_signal},    "f10_retail_working_capital_receivables_base_252d_v032_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_252d_v032_signal},    "f10_retail_working_capital_payables_base_252d_v033_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_252d_v033_signal},    "f10_retail_working_capital_revenue_base_252d_v034_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_252d_v034_signal},    "f10_retail_working_capital_wc_drag_base_252d_v035_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_252d_v035_signal},    "f10_retail_working_capital_inventory_base_504d_v036_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_504d_v036_signal},    "f10_retail_working_capital_receivables_base_504d_v037_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_504d_v037_signal},    "f10_retail_working_capital_payables_base_504d_v038_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_504d_v038_signal},    "f10_retail_working_capital_revenue_base_504d_v039_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_504d_v039_signal},    "f10_retail_working_capital_wc_drag_base_504d_v040_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_504d_v040_signal},    "f10_retail_working_capital_inventory_base_756d_v041_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_756d_v041_signal},    "f10_retail_working_capital_receivables_base_756d_v042_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_756d_v042_signal},    "f10_retail_working_capital_payables_base_756d_v043_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_756d_v043_signal},    "f10_retail_working_capital_revenue_base_756d_v044_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_756d_v044_signal},    "f10_retail_working_capital_wc_drag_base_756d_v045_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_756d_v045_signal},    "f10_retail_working_capital_inventory_base_1008d_v046_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_1008d_v046_signal},    "f10_retail_working_capital_receivables_base_1008d_v047_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_1008d_v047_signal},    "f10_retail_working_capital_payables_base_1008d_v048_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_1008d_v048_signal},    "f10_retail_working_capital_revenue_base_1008d_v049_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_1008d_v049_signal},    "f10_retail_working_capital_wc_drag_base_1008d_v050_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_1008d_v050_signal},    "f10_retail_working_capital_inventory_base_1260d_v051_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_base_1260d_v051_signal},    "f10_retail_working_capital_receivables_base_1260d_v052_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_base_1260d_v052_signal},    "f10_retail_working_capital_payables_base_1260d_v053_signal": {"inputs": [], "func": f10_retail_working_capital_payables_base_1260d_v053_signal},    "f10_retail_working_capital_revenue_base_1260d_v054_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_base_1260d_v054_signal},    "f10_retail_working_capital_wc_drag_base_1260d_v055_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_base_1260d_v055_signal},    "f10_retail_working_capital_inventory_z_5d_v056_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_5d_v056_signal},    "f10_retail_working_capital_receivables_z_5d_v057_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_5d_v057_signal},    "f10_retail_working_capital_payables_z_5d_v058_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_5d_v058_signal},    "f10_retail_working_capital_revenue_z_5d_v059_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_5d_v059_signal},    "f10_retail_working_capital_wc_drag_z_5d_v060_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_5d_v060_signal},    "f10_retail_working_capital_inventory_z_10d_v061_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_10d_v061_signal},    "f10_retail_working_capital_receivables_z_10d_v062_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_10d_v062_signal},    "f10_retail_working_capital_payables_z_10d_v063_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_10d_v063_signal},    "f10_retail_working_capital_revenue_z_10d_v064_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_10d_v064_signal},    "f10_retail_working_capital_wc_drag_z_10d_v065_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_10d_v065_signal},    "f10_retail_working_capital_inventory_z_21d_v066_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_21d_v066_signal},    "f10_retail_working_capital_receivables_z_21d_v067_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_21d_v067_signal},    "f10_retail_working_capital_payables_z_21d_v068_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_21d_v068_signal},    "f10_retail_working_capital_revenue_z_21d_v069_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_21d_v069_signal},    "f10_retail_working_capital_wc_drag_z_21d_v070_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_21d_v070_signal},    "f10_retail_working_capital_inventory_z_42d_v071_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_42d_v071_signal},    "f10_retail_working_capital_receivables_z_42d_v072_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_42d_v072_signal},    "f10_retail_working_capital_payables_z_42d_v073_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_42d_v073_signal},    "f10_retail_working_capital_revenue_z_42d_v074_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_42d_v074_signal},    "f10_retail_working_capital_wc_drag_z_42d_v075_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_42d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 10...")
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
