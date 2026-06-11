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

def f39_working_cap_liquidity_inventory_slope_pct_5d_v001_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 5d window."""
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_5d_v002_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 5d window."""
    res = _slope_pct(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_5d_v003_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 5d window."""
    res = _slope_pct(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_5d_v004_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 5d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_10d_v005_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 10d window."""
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_10d_v006_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 10d window."""
    res = _slope_pct(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_10d_v007_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 10d window."""
    res = _slope_pct(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_10d_v008_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 10d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_21d_v009_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 21d window."""
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_21d_v010_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 21d window."""
    res = _slope_pct(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_21d_v011_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 21d window."""
    res = _slope_pct(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_21d_v012_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 21d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_42d_v013_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 42d window."""
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_42d_v014_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 42d window."""
    res = _slope_pct(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_42d_v015_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 42d window."""
    res = _slope_pct(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_42d_v016_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 42d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_63d_v017_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 63d window."""
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_63d_v018_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 63d window."""
    res = _slope_pct(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_63d_v019_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 63d window."""
    res = _slope_pct(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_63d_v020_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 63d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_126d_v021_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 126d window."""
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_126d_v022_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 126d window."""
    res = _slope_pct(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_126d_v023_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 126d window."""
    res = _slope_pct(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_126d_v024_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 126d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_252d_v025_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 252d window."""
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_252d_v026_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 252d window."""
    res = _slope_pct(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_252d_v027_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 252d window."""
    res = _slope_pct(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_252d_v028_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 252d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_504d_v029_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 504d window."""
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_504d_v030_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 504d window."""
    res = _slope_pct(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_504d_v031_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 504d window."""
    res = _slope_pct(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_504d_v032_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 504d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_756d_v033_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 756d window."""
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_756d_v034_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 756d window."""
    res = _slope_pct(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_756d_v035_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 756d window."""
    res = _slope_pct(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_756d_v036_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 756d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_1008d_v037_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 1008d window."""
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_1008d_v038_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 1008d window."""
    res = _slope_pct(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_1008d_v039_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 1008d window."""
    res = _slope_pct(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_1008d_v040_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 1008d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_pct_1260d_v041_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 1260d window."""
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_pct_1260d_v042_signal(cashneq):
    """Percentage slope for momentum for Raw level of cashneq over 1260d window."""
    res = _slope_pct(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_pct_1260d_v043_signal(liabilitiesc):
    """Percentage slope for momentum for Raw level of liabilitiesc over 1260d window."""
    res = _slope_pct(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_pct_1260d_v044_signal(cashneq, liabilitiesc):
    """Percentage slope for momentum for Current liquidity coverage of short-term liabilities over 1260d window."""
    res = _slope_pct(_ratio(cashneq, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_5d_v045_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 5d window."""
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_5d_v046_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 5d window."""
    res = _jerk(cashneq, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_5d_v047_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 5d window."""
    res = _jerk(liabilitiesc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_5d_v048_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 5d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_10d_v049_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 10d window."""
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_10d_v050_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 10d window."""
    res = _jerk(cashneq, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_10d_v051_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 10d window."""
    res = _jerk(liabilitiesc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_10d_v052_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 10d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_21d_v053_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 21d window."""
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_21d_v054_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 21d window."""
    res = _jerk(cashneq, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_21d_v055_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 21d window."""
    res = _jerk(liabilitiesc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_21d_v056_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 21d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_42d_v057_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 42d window."""
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_42d_v058_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 42d window."""
    res = _jerk(cashneq, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_42d_v059_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 42d window."""
    res = _jerk(liabilitiesc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_42d_v060_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 42d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_63d_v061_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 63d window."""
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_63d_v062_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 63d window."""
    res = _jerk(cashneq, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_63d_v063_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 63d window."""
    res = _jerk(liabilitiesc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_63d_v064_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 63d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_126d_v065_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 126d window."""
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_126d_v066_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 126d window."""
    res = _jerk(cashneq, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_126d_v067_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 126d window."""
    res = _jerk(liabilitiesc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_126d_v068_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 126d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_252d_v069_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 252d window."""
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_252d_v070_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 252d window."""
    res = _jerk(cashneq, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_252d_v071_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 252d window."""
    res = _jerk(liabilitiesc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_252d_v072_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 252d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_504d_v073_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 504d window."""
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_504d_v074_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 504d window."""
    res = _jerk(cashneq, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_504d_v075_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 504d window."""
    res = _jerk(liabilitiesc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_504d_v076_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 504d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_756d_v077_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 756d window."""
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_756d_v078_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 756d window."""
    res = _jerk(cashneq, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_756d_v079_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 756d window."""
    res = _jerk(liabilitiesc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_756d_v080_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 756d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_1008d_v081_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 1008d window."""
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_1008d_v082_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 1008d window."""
    res = _jerk(cashneq, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_1008d_v083_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 1008d window."""
    res = _jerk(liabilitiesc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_1008d_v084_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 1008d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_jerk_1260d_v085_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 1260d window."""
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_jerk_1260d_v086_signal(cashneq):
    """Acceleration/Jerk for structural shifts for Raw level of cashneq over 1260d window."""
    res = _jerk(cashneq, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_jerk_1260d_v087_signal(liabilitiesc):
    """Acceleration/Jerk for structural shifts for Raw level of liabilitiesc over 1260d window."""
    res = _jerk(liabilitiesc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_jerk_1260d_v088_signal(cashneq, liabilitiesc):
    """Acceleration/Jerk for structural shifts for Current liquidity coverage of short-term liabilities over 1260d window."""
    res = _jerk(_ratio(cashneq, liabilitiesc), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_5d_v089_signal(inventory):
    """Normalized slope change for Raw level of inventory over 5d window."""
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_5d_v090_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 5d window."""
    res = (_slope_pct(cashneq, 5).diff(5) / _sma(cashneq.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_5d_v091_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 5d window."""
    res = (_slope_pct(liabilitiesc, 5).diff(5) / _sma(liabilitiesc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_5d_v092_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 5d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 5).diff(5) / _sma(_ratio(cashneq, liabilitiesc).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_10d_v093_signal(inventory):
    """Normalized slope change for Raw level of inventory over 10d window."""
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_10d_v094_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 10d window."""
    res = (_slope_pct(cashneq, 10).diff(10) / _sma(cashneq.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_10d_v095_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 10d window."""
    res = (_slope_pct(liabilitiesc, 10).diff(10) / _sma(liabilitiesc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_10d_v096_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 10d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 10).diff(10) / _sma(_ratio(cashneq, liabilitiesc).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_21d_v097_signal(inventory):
    """Normalized slope change for Raw level of inventory over 21d window."""
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_21d_v098_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 21d window."""
    res = (_slope_pct(cashneq, 21).diff(21) / _sma(cashneq.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_21d_v099_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 21d window."""
    res = (_slope_pct(liabilitiesc, 21).diff(21) / _sma(liabilitiesc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_21d_v100_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 21d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 21).diff(21) / _sma(_ratio(cashneq, liabilitiesc).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_42d_v101_signal(inventory):
    """Normalized slope change for Raw level of inventory over 42d window."""
    res = (_slope_pct(inventory, 42).diff(42) / _sma(inventory.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_42d_v102_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 42d window."""
    res = (_slope_pct(cashneq, 42).diff(42) / _sma(cashneq.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_42d_v103_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 42d window."""
    res = (_slope_pct(liabilitiesc, 42).diff(42) / _sma(liabilitiesc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_42d_v104_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 42d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 42).diff(42) / _sma(_ratio(cashneq, liabilitiesc).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_63d_v105_signal(inventory):
    """Normalized slope change for Raw level of inventory over 63d window."""
    res = (_slope_pct(inventory, 63).diff(63) / _sma(inventory.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_63d_v106_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 63d window."""
    res = (_slope_pct(cashneq, 63).diff(63) / _sma(cashneq.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_63d_v107_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 63d window."""
    res = (_slope_pct(liabilitiesc, 63).diff(63) / _sma(liabilitiesc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_63d_v108_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 63d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 63).diff(63) / _sma(_ratio(cashneq, liabilitiesc).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_126d_v109_signal(inventory):
    """Normalized slope change for Raw level of inventory over 126d window."""
    res = (_slope_pct(inventory, 126).diff(126) / _sma(inventory.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_126d_v110_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 126d window."""
    res = (_slope_pct(cashneq, 126).diff(126) / _sma(cashneq.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_126d_v111_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 126d window."""
    res = (_slope_pct(liabilitiesc, 126).diff(126) / _sma(liabilitiesc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_126d_v112_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 126d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 126).diff(126) / _sma(_ratio(cashneq, liabilitiesc).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_252d_v113_signal(inventory):
    """Normalized slope change for Raw level of inventory over 252d window."""
    res = (_slope_pct(inventory, 252).diff(252) / _sma(inventory.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_252d_v114_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 252d window."""
    res = (_slope_pct(cashneq, 252).diff(252) / _sma(cashneq.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_252d_v115_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 252d window."""
    res = (_slope_pct(liabilitiesc, 252).diff(252) / _sma(liabilitiesc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_252d_v116_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 252d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 252).diff(252) / _sma(_ratio(cashneq, liabilitiesc).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_504d_v117_signal(inventory):
    """Normalized slope change for Raw level of inventory over 504d window."""
    res = (_slope_pct(inventory, 504).diff(504) / _sma(inventory.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_504d_v118_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 504d window."""
    res = (_slope_pct(cashneq, 504).diff(504) / _sma(cashneq.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_504d_v119_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 504d window."""
    res = (_slope_pct(liabilitiesc, 504).diff(504) / _sma(liabilitiesc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_504d_v120_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 504d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 504).diff(504) / _sma(_ratio(cashneq, liabilitiesc).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_756d_v121_signal(inventory):
    """Normalized slope change for Raw level of inventory over 756d window."""
    res = (_slope_pct(inventory, 756).diff(756) / _sma(inventory.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_756d_v122_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 756d window."""
    res = (_slope_pct(cashneq, 756).diff(756) / _sma(cashneq.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_756d_v123_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 756d window."""
    res = (_slope_pct(liabilitiesc, 756).diff(756) / _sma(liabilitiesc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_756d_v124_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 756d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 756).diff(756) / _sma(_ratio(cashneq, liabilitiesc).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_1008d_v125_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1008d window."""
    res = (_slope_pct(inventory, 1008).diff(1008) / _sma(inventory.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_1008d_v126_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 1008d window."""
    res = (_slope_pct(cashneq, 1008).diff(1008) / _sma(cashneq.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_1008d_v127_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 1008d window."""
    res = (_slope_pct(liabilitiesc, 1008).diff(1008) / _sma(liabilitiesc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_1008d_v128_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 1008d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 1008).diff(1008) / _sma(_ratio(cashneq, liabilitiesc).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_slope_diff_norm_1260d_v129_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1260d window."""
    res = (_slope_pct(inventory, 1260).diff(1260) / _sma(inventory.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_slope_diff_norm_1260d_v130_signal(cashneq):
    """Normalized slope change for Raw level of cashneq over 1260d window."""
    res = (_slope_pct(cashneq, 1260).diff(1260) / _sma(cashneq.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_1260d_v131_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 1260d window."""
    res = (_slope_pct(liabilitiesc, 1260).diff(1260) / _sma(liabilitiesc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_slope_diff_norm_1260d_v132_signal(cashneq, liabilitiesc):
    """Normalized slope change for Current liquidity coverage of short-term liabilities over 1260d window."""
    res = (_slope_pct(_ratio(cashneq, liabilitiesc), 1260).diff(1260) / _sma(_ratio(cashneq, liabilitiesc).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_mom_z_5d_v133_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 5d window."""
    res = _z(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_mom_z_5d_v134_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 5d window."""
    res = _z(_slope_pct(cashneq, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_mom_z_5d_v135_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 5d window."""
    res = _z(_slope_pct(liabilitiesc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_mom_z_5d_v136_signal(cashneq, liabilitiesc):
    """Relative momentum strength for Current liquidity coverage of short-term liabilities over 5d window."""
    res = _z(_slope_pct(_ratio(cashneq, liabilitiesc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_mom_z_10d_v137_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 10d window."""
    res = _z(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_mom_z_10d_v138_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 10d window."""
    res = _z(_slope_pct(cashneq, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_mom_z_10d_v139_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 10d window."""
    res = _z(_slope_pct(liabilitiesc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_mom_z_10d_v140_signal(cashneq, liabilitiesc):
    """Relative momentum strength for Current liquidity coverage of short-term liabilities over 10d window."""
    res = _z(_slope_pct(_ratio(cashneq, liabilitiesc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_mom_z_21d_v141_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 21d window."""
    res = _z(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_mom_z_21d_v142_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 21d window."""
    res = _z(_slope_pct(cashneq, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_mom_z_21d_v143_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 21d window."""
    res = _z(_slope_pct(liabilitiesc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_mom_z_21d_v144_signal(cashneq, liabilitiesc):
    """Relative momentum strength for Current liquidity coverage of short-term liabilities over 21d window."""
    res = _z(_slope_pct(_ratio(cashneq, liabilitiesc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_mom_z_42d_v145_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 42d window."""
    res = _z(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_mom_z_42d_v146_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 42d window."""
    res = _z(_slope_pct(cashneq, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_mom_z_42d_v147_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 42d window."""
    res = _z(_slope_pct(liabilitiesc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_mom_z_42d_v148_signal(cashneq, liabilitiesc):
    """Relative momentum strength for Current liquidity coverage of short-term liabilities over 42d window."""
    res = _z(_slope_pct(_ratio(cashneq, liabilitiesc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_mom_z_63d_v149_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 63d window."""
    res = _z(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_mom_z_63d_v150_signal(cashneq):
    """Relative momentum strength for Raw level of cashneq over 63d window."""
    res = _z(_slope_pct(cashneq, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f39_working_cap_liquidity_inventory_slope_pct_5d_v001_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_5d_v001_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_5d_v002_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_5d_v002_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_5d_v003_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_5d_v003_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_5d_v004_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_5d_v004_signal},    "f39_working_cap_liquidity_inventory_slope_pct_10d_v005_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_10d_v005_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_10d_v006_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_10d_v006_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_10d_v007_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_10d_v007_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_10d_v008_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_10d_v008_signal},    "f39_working_cap_liquidity_inventory_slope_pct_21d_v009_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_21d_v009_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_21d_v010_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_21d_v010_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_21d_v011_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_21d_v011_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_21d_v012_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_21d_v012_signal},    "f39_working_cap_liquidity_inventory_slope_pct_42d_v013_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_42d_v013_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_42d_v014_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_42d_v014_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_42d_v015_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_42d_v015_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_42d_v016_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_42d_v016_signal},    "f39_working_cap_liquidity_inventory_slope_pct_63d_v017_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_63d_v017_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_63d_v018_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_63d_v018_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_63d_v019_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_63d_v019_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_63d_v020_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_63d_v020_signal},    "f39_working_cap_liquidity_inventory_slope_pct_126d_v021_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_126d_v021_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_126d_v022_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_126d_v022_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_126d_v023_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_126d_v023_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_126d_v024_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_126d_v024_signal},    "f39_working_cap_liquidity_inventory_slope_pct_252d_v025_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_252d_v025_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_252d_v026_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_252d_v026_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_252d_v027_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_252d_v027_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_252d_v028_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_252d_v028_signal},    "f39_working_cap_liquidity_inventory_slope_pct_504d_v029_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_504d_v029_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_504d_v030_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_504d_v030_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_504d_v031_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_504d_v031_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_504d_v032_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_504d_v032_signal},    "f39_working_cap_liquidity_inventory_slope_pct_756d_v033_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_756d_v033_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_756d_v034_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_756d_v034_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_756d_v035_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_756d_v035_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_756d_v036_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_756d_v036_signal},    "f39_working_cap_liquidity_inventory_slope_pct_1008d_v037_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_1008d_v037_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_1008d_v038_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_1008d_v038_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_1008d_v039_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_1008d_v039_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_1008d_v040_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_1008d_v040_signal},    "f39_working_cap_liquidity_inventory_slope_pct_1260d_v041_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_pct_1260d_v041_signal},    "f39_working_cap_liquidity_cashneq_slope_pct_1260d_v042_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_pct_1260d_v042_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_pct_1260d_v043_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_pct_1260d_v043_signal},    "f39_working_cap_liquidity_liquidity_index_slope_pct_1260d_v044_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_pct_1260d_v044_signal},    "f39_working_cap_liquidity_inventory_jerk_5d_v045_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_5d_v045_signal},    "f39_working_cap_liquidity_cashneq_jerk_5d_v046_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_5d_v046_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_5d_v047_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_5d_v047_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_5d_v048_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_5d_v048_signal},    "f39_working_cap_liquidity_inventory_jerk_10d_v049_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_10d_v049_signal},    "f39_working_cap_liquidity_cashneq_jerk_10d_v050_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_10d_v050_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_10d_v051_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_10d_v051_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_10d_v052_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_10d_v052_signal},    "f39_working_cap_liquidity_inventory_jerk_21d_v053_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_21d_v053_signal},    "f39_working_cap_liquidity_cashneq_jerk_21d_v054_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_21d_v054_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_21d_v055_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_21d_v055_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_21d_v056_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_21d_v056_signal},    "f39_working_cap_liquidity_inventory_jerk_42d_v057_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_42d_v057_signal},    "f39_working_cap_liquidity_cashneq_jerk_42d_v058_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_42d_v058_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_42d_v059_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_42d_v059_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_42d_v060_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_42d_v060_signal},    "f39_working_cap_liquidity_inventory_jerk_63d_v061_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_63d_v061_signal},    "f39_working_cap_liquidity_cashneq_jerk_63d_v062_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_63d_v062_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_63d_v063_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_63d_v063_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_63d_v064_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_63d_v064_signal},    "f39_working_cap_liquidity_inventory_jerk_126d_v065_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_126d_v065_signal},    "f39_working_cap_liquidity_cashneq_jerk_126d_v066_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_126d_v066_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_126d_v067_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_126d_v067_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_126d_v068_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_126d_v068_signal},    "f39_working_cap_liquidity_inventory_jerk_252d_v069_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_252d_v069_signal},    "f39_working_cap_liquidity_cashneq_jerk_252d_v070_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_252d_v070_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_252d_v071_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_252d_v071_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_252d_v072_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_252d_v072_signal},    "f39_working_cap_liquidity_inventory_jerk_504d_v073_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_504d_v073_signal},    "f39_working_cap_liquidity_cashneq_jerk_504d_v074_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_504d_v074_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_504d_v075_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_504d_v075_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_504d_v076_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_504d_v076_signal},    "f39_working_cap_liquidity_inventory_jerk_756d_v077_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_756d_v077_signal},    "f39_working_cap_liquidity_cashneq_jerk_756d_v078_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_756d_v078_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_756d_v079_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_756d_v079_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_756d_v080_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_756d_v080_signal},    "f39_working_cap_liquidity_inventory_jerk_1008d_v081_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_1008d_v081_signal},    "f39_working_cap_liquidity_cashneq_jerk_1008d_v082_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_1008d_v082_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_1008d_v083_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_1008d_v083_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_1008d_v084_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_1008d_v084_signal},    "f39_working_cap_liquidity_inventory_jerk_1260d_v085_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_jerk_1260d_v085_signal},    "f39_working_cap_liquidity_cashneq_jerk_1260d_v086_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_jerk_1260d_v086_signal},    "f39_working_cap_liquidity_liabilitiesc_jerk_1260d_v087_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_jerk_1260d_v087_signal},    "f39_working_cap_liquidity_liquidity_index_jerk_1260d_v088_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_jerk_1260d_v088_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_5d_v089_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_5d_v090_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_5d_v091_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_5d_v092_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_10d_v093_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_10d_v094_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_10d_v095_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_10d_v096_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_21d_v097_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_21d_v098_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_21d_v099_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_21d_v100_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_42d_v101_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_42d_v102_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_42d_v103_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_42d_v104_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_63d_v105_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_63d_v106_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_63d_v107_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_63d_v108_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_126d_v109_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_126d_v110_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_126d_v111_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_126d_v112_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_252d_v113_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_252d_v114_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_252d_v115_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_252d_v116_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_504d_v117_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_504d_v118_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_504d_v119_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_504d_v120_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_756d_v121_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_756d_v122_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_756d_v123_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_756d_v124_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_1008d_v125_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_1008d_v126_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_1008d_v127_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_1008d_v128_signal},    "f39_working_cap_liquidity_inventory_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_slope_diff_norm_1260d_v129_signal},    "f39_working_cap_liquidity_cashneq_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_slope_diff_norm_1260d_v130_signal},    "f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_slope_diff_norm_1260d_v131_signal},    "f39_working_cap_liquidity_liquidity_index_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_slope_diff_norm_1260d_v132_signal},    "f39_working_cap_liquidity_inventory_mom_z_5d_v133_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_mom_z_5d_v133_signal},    "f39_working_cap_liquidity_cashneq_mom_z_5d_v134_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_mom_z_5d_v134_signal},    "f39_working_cap_liquidity_liabilitiesc_mom_z_5d_v135_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_mom_z_5d_v135_signal},    "f39_working_cap_liquidity_liquidity_index_mom_z_5d_v136_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_mom_z_5d_v136_signal},    "f39_working_cap_liquidity_inventory_mom_z_10d_v137_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_mom_z_10d_v137_signal},    "f39_working_cap_liquidity_cashneq_mom_z_10d_v138_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_mom_z_10d_v138_signal},    "f39_working_cap_liquidity_liabilitiesc_mom_z_10d_v139_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_mom_z_10d_v139_signal},    "f39_working_cap_liquidity_liquidity_index_mom_z_10d_v140_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_mom_z_10d_v140_signal},    "f39_working_cap_liquidity_inventory_mom_z_21d_v141_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_mom_z_21d_v141_signal},    "f39_working_cap_liquidity_cashneq_mom_z_21d_v142_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_mom_z_21d_v142_signal},    "f39_working_cap_liquidity_liabilitiesc_mom_z_21d_v143_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_mom_z_21d_v143_signal},    "f39_working_cap_liquidity_liquidity_index_mom_z_21d_v144_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_mom_z_21d_v144_signal},    "f39_working_cap_liquidity_inventory_mom_z_42d_v145_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_mom_z_42d_v145_signal},    "f39_working_cap_liquidity_cashneq_mom_z_42d_v146_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_mom_z_42d_v146_signal},    "f39_working_cap_liquidity_liabilitiesc_mom_z_42d_v147_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_mom_z_42d_v147_signal},    "f39_working_cap_liquidity_liquidity_index_mom_z_42d_v148_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_mom_z_42d_v148_signal},    "f39_working_cap_liquidity_inventory_mom_z_63d_v149_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_mom_z_63d_v149_signal},    "f39_working_cap_liquidity_cashneq_mom_z_63d_v150_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 39...")
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
