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

def f10_retail_working_capital_inventory_slope_pct_5d_v001_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 5d window."""
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_5d_v002_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 5d window."""
    res = _slope_pct(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_5d_v003_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 5d window."""
    res = _slope_pct(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_5d_v004_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_5d_v005_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 5d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_10d_v006_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 10d window."""
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_10d_v007_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 10d window."""
    res = _slope_pct(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_10d_v008_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 10d window."""
    res = _slope_pct(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_10d_v009_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_10d_v010_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 10d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_21d_v011_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 21d window."""
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_21d_v012_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 21d window."""
    res = _slope_pct(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_21d_v013_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 21d window."""
    res = _slope_pct(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_21d_v014_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_21d_v015_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 21d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_42d_v016_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 42d window."""
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_42d_v017_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 42d window."""
    res = _slope_pct(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_42d_v018_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 42d window."""
    res = _slope_pct(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_42d_v019_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_42d_v020_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 42d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_63d_v021_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 63d window."""
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_63d_v022_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 63d window."""
    res = _slope_pct(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_63d_v023_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 63d window."""
    res = _slope_pct(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_63d_v024_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_63d_v025_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 63d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_126d_v026_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 126d window."""
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_126d_v027_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 126d window."""
    res = _slope_pct(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_126d_v028_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 126d window."""
    res = _slope_pct(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_126d_v029_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_126d_v030_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 126d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_252d_v031_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 252d window."""
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_252d_v032_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 252d window."""
    res = _slope_pct(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_252d_v033_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 252d window."""
    res = _slope_pct(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_252d_v034_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_252d_v035_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 252d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_504d_v036_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 504d window."""
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_504d_v037_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 504d window."""
    res = _slope_pct(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_504d_v038_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 504d window."""
    res = _slope_pct(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_504d_v039_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_504d_v040_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 504d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_756d_v041_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 756d window."""
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_756d_v042_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 756d window."""
    res = _slope_pct(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_756d_v043_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 756d window."""
    res = _slope_pct(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_756d_v044_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_756d_v045_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 756d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_1008d_v046_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 1008d window."""
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_1008d_v047_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 1008d window."""
    res = _slope_pct(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_1008d_v048_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 1008d window."""
    res = _slope_pct(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_1008d_v049_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_1008d_v050_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 1008d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_pct_1260d_v051_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 1260d window."""
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_pct_1260d_v052_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 1260d window."""
    res = _slope_pct(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_pct_1260d_v053_signal(payables):
    """Percentage slope for momentum for Raw level of payables over 1260d window."""
    res = _slope_pct(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_pct_1260d_v054_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_pct_1260d_v055_signal(inventory, receivables, payables, revenue):
    """Percentage slope for momentum for Working capital load per dollar of sales over 1260d window."""
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_5d_v056_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 5d window."""
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_5d_v057_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 5d window."""
    res = _jerk(receivables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_5d_v058_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 5d window."""
    res = _jerk(payables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_5d_v059_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_5d_v060_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 5d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_10d_v061_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 10d window."""
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_10d_v062_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 10d window."""
    res = _jerk(receivables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_10d_v063_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 10d window."""
    res = _jerk(payables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_10d_v064_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_10d_v065_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 10d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_21d_v066_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 21d window."""
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_21d_v067_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 21d window."""
    res = _jerk(receivables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_21d_v068_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 21d window."""
    res = _jerk(payables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_21d_v069_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_21d_v070_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 21d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_42d_v071_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 42d window."""
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_42d_v072_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 42d window."""
    res = _jerk(receivables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_42d_v073_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 42d window."""
    res = _jerk(payables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_42d_v074_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_42d_v075_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 42d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_63d_v076_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 63d window."""
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_63d_v077_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 63d window."""
    res = _jerk(receivables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_63d_v078_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 63d window."""
    res = _jerk(payables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_63d_v079_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_63d_v080_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 63d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_126d_v081_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 126d window."""
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_126d_v082_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 126d window."""
    res = _jerk(receivables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_126d_v083_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 126d window."""
    res = _jerk(payables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_126d_v084_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_126d_v085_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 126d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_252d_v086_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 252d window."""
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_252d_v087_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 252d window."""
    res = _jerk(receivables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_252d_v088_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 252d window."""
    res = _jerk(payables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_252d_v089_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_252d_v090_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 252d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_504d_v091_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 504d window."""
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_504d_v092_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 504d window."""
    res = _jerk(receivables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_504d_v093_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 504d window."""
    res = _jerk(payables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_504d_v094_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_504d_v095_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 504d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_756d_v096_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 756d window."""
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_756d_v097_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 756d window."""
    res = _jerk(receivables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_756d_v098_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 756d window."""
    res = _jerk(payables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_756d_v099_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_756d_v100_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 756d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_1008d_v101_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 1008d window."""
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_1008d_v102_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 1008d window."""
    res = _jerk(receivables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_1008d_v103_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 1008d window."""
    res = _jerk(payables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_1008d_v104_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_1008d_v105_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 1008d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_jerk_1260d_v106_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 1260d window."""
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_jerk_1260d_v107_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 1260d window."""
    res = _jerk(receivables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_jerk_1260d_v108_signal(payables):
    """Acceleration/Jerk for structural shifts for Raw level of payables over 1260d window."""
    res = _jerk(payables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_jerk_1260d_v109_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_jerk_1260d_v110_signal(inventory, receivables, payables, revenue):
    """Acceleration/Jerk for structural shifts for Working capital load per dollar of sales over 1260d window."""
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_5d_v111_signal(inventory):
    """Normalized slope change for Raw level of inventory over 5d window."""
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_5d_v112_signal(receivables):
    """Normalized slope change for Raw level of receivables over 5d window."""
    res = (_slope_pct(receivables, 5).diff(5) / _sma(receivables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_5d_v113_signal(payables):
    """Normalized slope change for Raw level of payables over 5d window."""
    res = (_slope_pct(payables, 5).diff(5) / _sma(payables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_5d_v114_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_5d_v115_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 5d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 5).diff(5) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_10d_v116_signal(inventory):
    """Normalized slope change for Raw level of inventory over 10d window."""
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_10d_v117_signal(receivables):
    """Normalized slope change for Raw level of receivables over 10d window."""
    res = (_slope_pct(receivables, 10).diff(10) / _sma(receivables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_10d_v118_signal(payables):
    """Normalized slope change for Raw level of payables over 10d window."""
    res = (_slope_pct(payables, 10).diff(10) / _sma(payables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_10d_v119_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_10d_v120_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 10d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 10).diff(10) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_21d_v121_signal(inventory):
    """Normalized slope change for Raw level of inventory over 21d window."""
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_21d_v122_signal(receivables):
    """Normalized slope change for Raw level of receivables over 21d window."""
    res = (_slope_pct(receivables, 21).diff(21) / _sma(receivables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_21d_v123_signal(payables):
    """Normalized slope change for Raw level of payables over 21d window."""
    res = (_slope_pct(payables, 21).diff(21) / _sma(payables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_21d_v124_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_21d_v125_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 21d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 21).diff(21) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_42d_v126_signal(inventory):
    """Normalized slope change for Raw level of inventory over 42d window."""
    res = (_slope_pct(inventory, 42).diff(42) / _sma(inventory.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_42d_v127_signal(receivables):
    """Normalized slope change for Raw level of receivables over 42d window."""
    res = (_slope_pct(receivables, 42).diff(42) / _sma(receivables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_42d_v128_signal(payables):
    """Normalized slope change for Raw level of payables over 42d window."""
    res = (_slope_pct(payables, 42).diff(42) / _sma(payables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_42d_v129_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_42d_v130_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 42d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 42).diff(42) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_63d_v131_signal(inventory):
    """Normalized slope change for Raw level of inventory over 63d window."""
    res = (_slope_pct(inventory, 63).diff(63) / _sma(inventory.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_63d_v132_signal(receivables):
    """Normalized slope change for Raw level of receivables over 63d window."""
    res = (_slope_pct(receivables, 63).diff(63) / _sma(receivables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_63d_v133_signal(payables):
    """Normalized slope change for Raw level of payables over 63d window."""
    res = (_slope_pct(payables, 63).diff(63) / _sma(payables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_63d_v134_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_63d_v135_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 63d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 63).diff(63) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_126d_v136_signal(inventory):
    """Normalized slope change for Raw level of inventory over 126d window."""
    res = (_slope_pct(inventory, 126).diff(126) / _sma(inventory.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_126d_v137_signal(receivables):
    """Normalized slope change for Raw level of receivables over 126d window."""
    res = (_slope_pct(receivables, 126).diff(126) / _sma(receivables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_126d_v138_signal(payables):
    """Normalized slope change for Raw level of payables over 126d window."""
    res = (_slope_pct(payables, 126).diff(126) / _sma(payables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_126d_v139_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_126d_v140_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 126d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 126).diff(126) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_252d_v141_signal(inventory):
    """Normalized slope change for Raw level of inventory over 252d window."""
    res = (_slope_pct(inventory, 252).diff(252) / _sma(inventory.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_252d_v142_signal(receivables):
    """Normalized slope change for Raw level of receivables over 252d window."""
    res = (_slope_pct(receivables, 252).diff(252) / _sma(receivables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_252d_v143_signal(payables):
    """Normalized slope change for Raw level of payables over 252d window."""
    res = (_slope_pct(payables, 252).diff(252) / _sma(payables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_252d_v144_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_252d_v145_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 252d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 252).diff(252) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_slope_diff_norm_504d_v146_signal(inventory):
    """Normalized slope change for Raw level of inventory over 504d window."""
    res = (_slope_pct(inventory, 504).diff(504) / _sma(inventory.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_slope_diff_norm_504d_v147_signal(receivables):
    """Normalized slope change for Raw level of receivables over 504d window."""
    res = (_slope_pct(receivables, 504).diff(504) / _sma(receivables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_slope_diff_norm_504d_v148_signal(payables):
    """Normalized slope change for Raw level of payables over 504d window."""
    res = (_slope_pct(payables, 504).diff(504) / _sma(payables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_slope_diff_norm_504d_v149_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_slope_diff_norm_504d_v150_signal(inventory, receivables, payables, revenue):
    """Normalized slope change for Working capital load per dollar of sales over 504d window."""
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 504).diff(504) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_retail_working_capital_inventory_slope_pct_5d_v001_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_5d_v001_signal},    "f10_retail_working_capital_receivables_slope_pct_5d_v002_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_5d_v002_signal},    "f10_retail_working_capital_payables_slope_pct_5d_v003_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_5d_v003_signal},    "f10_retail_working_capital_revenue_slope_pct_5d_v004_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_5d_v004_signal},    "f10_retail_working_capital_wc_drag_slope_pct_5d_v005_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_5d_v005_signal},    "f10_retail_working_capital_inventory_slope_pct_10d_v006_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_10d_v006_signal},    "f10_retail_working_capital_receivables_slope_pct_10d_v007_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_10d_v007_signal},    "f10_retail_working_capital_payables_slope_pct_10d_v008_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_10d_v008_signal},    "f10_retail_working_capital_revenue_slope_pct_10d_v009_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_10d_v009_signal},    "f10_retail_working_capital_wc_drag_slope_pct_10d_v010_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_10d_v010_signal},    "f10_retail_working_capital_inventory_slope_pct_21d_v011_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_21d_v011_signal},    "f10_retail_working_capital_receivables_slope_pct_21d_v012_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_21d_v012_signal},    "f10_retail_working_capital_payables_slope_pct_21d_v013_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_21d_v013_signal},    "f10_retail_working_capital_revenue_slope_pct_21d_v014_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_21d_v014_signal},    "f10_retail_working_capital_wc_drag_slope_pct_21d_v015_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_21d_v015_signal},    "f10_retail_working_capital_inventory_slope_pct_42d_v016_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_42d_v016_signal},    "f10_retail_working_capital_receivables_slope_pct_42d_v017_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_42d_v017_signal},    "f10_retail_working_capital_payables_slope_pct_42d_v018_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_42d_v018_signal},    "f10_retail_working_capital_revenue_slope_pct_42d_v019_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_42d_v019_signal},    "f10_retail_working_capital_wc_drag_slope_pct_42d_v020_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_42d_v020_signal},    "f10_retail_working_capital_inventory_slope_pct_63d_v021_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_63d_v021_signal},    "f10_retail_working_capital_receivables_slope_pct_63d_v022_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_63d_v022_signal},    "f10_retail_working_capital_payables_slope_pct_63d_v023_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_63d_v023_signal},    "f10_retail_working_capital_revenue_slope_pct_63d_v024_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_63d_v024_signal},    "f10_retail_working_capital_wc_drag_slope_pct_63d_v025_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_63d_v025_signal},    "f10_retail_working_capital_inventory_slope_pct_126d_v026_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_126d_v026_signal},    "f10_retail_working_capital_receivables_slope_pct_126d_v027_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_126d_v027_signal},    "f10_retail_working_capital_payables_slope_pct_126d_v028_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_126d_v028_signal},    "f10_retail_working_capital_revenue_slope_pct_126d_v029_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_126d_v029_signal},    "f10_retail_working_capital_wc_drag_slope_pct_126d_v030_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_126d_v030_signal},    "f10_retail_working_capital_inventory_slope_pct_252d_v031_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_252d_v031_signal},    "f10_retail_working_capital_receivables_slope_pct_252d_v032_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_252d_v032_signal},    "f10_retail_working_capital_payables_slope_pct_252d_v033_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_252d_v033_signal},    "f10_retail_working_capital_revenue_slope_pct_252d_v034_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_252d_v034_signal},    "f10_retail_working_capital_wc_drag_slope_pct_252d_v035_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_252d_v035_signal},    "f10_retail_working_capital_inventory_slope_pct_504d_v036_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_504d_v036_signal},    "f10_retail_working_capital_receivables_slope_pct_504d_v037_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_504d_v037_signal},    "f10_retail_working_capital_payables_slope_pct_504d_v038_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_504d_v038_signal},    "f10_retail_working_capital_revenue_slope_pct_504d_v039_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_504d_v039_signal},    "f10_retail_working_capital_wc_drag_slope_pct_504d_v040_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_504d_v040_signal},    "f10_retail_working_capital_inventory_slope_pct_756d_v041_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_756d_v041_signal},    "f10_retail_working_capital_receivables_slope_pct_756d_v042_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_756d_v042_signal},    "f10_retail_working_capital_payables_slope_pct_756d_v043_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_756d_v043_signal},    "f10_retail_working_capital_revenue_slope_pct_756d_v044_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_756d_v044_signal},    "f10_retail_working_capital_wc_drag_slope_pct_756d_v045_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_756d_v045_signal},    "f10_retail_working_capital_inventory_slope_pct_1008d_v046_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_1008d_v046_signal},    "f10_retail_working_capital_receivables_slope_pct_1008d_v047_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_1008d_v047_signal},    "f10_retail_working_capital_payables_slope_pct_1008d_v048_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_1008d_v048_signal},    "f10_retail_working_capital_revenue_slope_pct_1008d_v049_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_1008d_v049_signal},    "f10_retail_working_capital_wc_drag_slope_pct_1008d_v050_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_1008d_v050_signal},    "f10_retail_working_capital_inventory_slope_pct_1260d_v051_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_pct_1260d_v051_signal},    "f10_retail_working_capital_receivables_slope_pct_1260d_v052_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_pct_1260d_v052_signal},    "f10_retail_working_capital_payables_slope_pct_1260d_v053_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_pct_1260d_v053_signal},    "f10_retail_working_capital_revenue_slope_pct_1260d_v054_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_pct_1260d_v054_signal},    "f10_retail_working_capital_wc_drag_slope_pct_1260d_v055_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_pct_1260d_v055_signal},    "f10_retail_working_capital_inventory_jerk_5d_v056_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_5d_v056_signal},    "f10_retail_working_capital_receivables_jerk_5d_v057_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_5d_v057_signal},    "f10_retail_working_capital_payables_jerk_5d_v058_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_5d_v058_signal},    "f10_retail_working_capital_revenue_jerk_5d_v059_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_5d_v059_signal},    "f10_retail_working_capital_wc_drag_jerk_5d_v060_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_5d_v060_signal},    "f10_retail_working_capital_inventory_jerk_10d_v061_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_10d_v061_signal},    "f10_retail_working_capital_receivables_jerk_10d_v062_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_10d_v062_signal},    "f10_retail_working_capital_payables_jerk_10d_v063_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_10d_v063_signal},    "f10_retail_working_capital_revenue_jerk_10d_v064_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_10d_v064_signal},    "f10_retail_working_capital_wc_drag_jerk_10d_v065_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_10d_v065_signal},    "f10_retail_working_capital_inventory_jerk_21d_v066_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_21d_v066_signal},    "f10_retail_working_capital_receivables_jerk_21d_v067_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_21d_v067_signal},    "f10_retail_working_capital_payables_jerk_21d_v068_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_21d_v068_signal},    "f10_retail_working_capital_revenue_jerk_21d_v069_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_21d_v069_signal},    "f10_retail_working_capital_wc_drag_jerk_21d_v070_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_21d_v070_signal},    "f10_retail_working_capital_inventory_jerk_42d_v071_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_42d_v071_signal},    "f10_retail_working_capital_receivables_jerk_42d_v072_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_42d_v072_signal},    "f10_retail_working_capital_payables_jerk_42d_v073_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_42d_v073_signal},    "f10_retail_working_capital_revenue_jerk_42d_v074_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_42d_v074_signal},    "f10_retail_working_capital_wc_drag_jerk_42d_v075_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_42d_v075_signal},    "f10_retail_working_capital_inventory_jerk_63d_v076_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_63d_v076_signal},    "f10_retail_working_capital_receivables_jerk_63d_v077_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_63d_v077_signal},    "f10_retail_working_capital_payables_jerk_63d_v078_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_63d_v078_signal},    "f10_retail_working_capital_revenue_jerk_63d_v079_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_63d_v079_signal},    "f10_retail_working_capital_wc_drag_jerk_63d_v080_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_63d_v080_signal},    "f10_retail_working_capital_inventory_jerk_126d_v081_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_126d_v081_signal},    "f10_retail_working_capital_receivables_jerk_126d_v082_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_126d_v082_signal},    "f10_retail_working_capital_payables_jerk_126d_v083_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_126d_v083_signal},    "f10_retail_working_capital_revenue_jerk_126d_v084_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_126d_v084_signal},    "f10_retail_working_capital_wc_drag_jerk_126d_v085_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_126d_v085_signal},    "f10_retail_working_capital_inventory_jerk_252d_v086_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_252d_v086_signal},    "f10_retail_working_capital_receivables_jerk_252d_v087_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_252d_v087_signal},    "f10_retail_working_capital_payables_jerk_252d_v088_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_252d_v088_signal},    "f10_retail_working_capital_revenue_jerk_252d_v089_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_252d_v089_signal},    "f10_retail_working_capital_wc_drag_jerk_252d_v090_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_252d_v090_signal},    "f10_retail_working_capital_inventory_jerk_504d_v091_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_504d_v091_signal},    "f10_retail_working_capital_receivables_jerk_504d_v092_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_504d_v092_signal},    "f10_retail_working_capital_payables_jerk_504d_v093_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_504d_v093_signal},    "f10_retail_working_capital_revenue_jerk_504d_v094_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_504d_v094_signal},    "f10_retail_working_capital_wc_drag_jerk_504d_v095_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_504d_v095_signal},    "f10_retail_working_capital_inventory_jerk_756d_v096_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_756d_v096_signal},    "f10_retail_working_capital_receivables_jerk_756d_v097_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_756d_v097_signal},    "f10_retail_working_capital_payables_jerk_756d_v098_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_756d_v098_signal},    "f10_retail_working_capital_revenue_jerk_756d_v099_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_756d_v099_signal},    "f10_retail_working_capital_wc_drag_jerk_756d_v100_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_756d_v100_signal},    "f10_retail_working_capital_inventory_jerk_1008d_v101_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_1008d_v101_signal},    "f10_retail_working_capital_receivables_jerk_1008d_v102_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_1008d_v102_signal},    "f10_retail_working_capital_payables_jerk_1008d_v103_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_1008d_v103_signal},    "f10_retail_working_capital_revenue_jerk_1008d_v104_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_1008d_v104_signal},    "f10_retail_working_capital_wc_drag_jerk_1008d_v105_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_1008d_v105_signal},    "f10_retail_working_capital_inventory_jerk_1260d_v106_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_jerk_1260d_v106_signal},    "f10_retail_working_capital_receivables_jerk_1260d_v107_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_jerk_1260d_v107_signal},    "f10_retail_working_capital_payables_jerk_1260d_v108_signal": {"inputs": [], "func": f10_retail_working_capital_payables_jerk_1260d_v108_signal},    "f10_retail_working_capital_revenue_jerk_1260d_v109_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_jerk_1260d_v109_signal},    "f10_retail_working_capital_wc_drag_jerk_1260d_v110_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_jerk_1260d_v110_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_5d_v111_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_5d_v111_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_5d_v112_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_5d_v112_signal},    "f10_retail_working_capital_payables_slope_diff_norm_5d_v113_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_5d_v113_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_5d_v114_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_5d_v114_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_5d_v115_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_5d_v115_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_10d_v116_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_10d_v116_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_10d_v117_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_10d_v117_signal},    "f10_retail_working_capital_payables_slope_diff_norm_10d_v118_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_10d_v118_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_10d_v119_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_10d_v119_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_10d_v120_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_10d_v120_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_21d_v121_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_21d_v121_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_21d_v122_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_21d_v122_signal},    "f10_retail_working_capital_payables_slope_diff_norm_21d_v123_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_21d_v123_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_21d_v124_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_21d_v124_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_21d_v125_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_21d_v125_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_42d_v126_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_42d_v126_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_42d_v127_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_42d_v127_signal},    "f10_retail_working_capital_payables_slope_diff_norm_42d_v128_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_42d_v128_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_42d_v129_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_42d_v129_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_42d_v130_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_42d_v130_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_63d_v131_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_63d_v131_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_63d_v132_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_63d_v132_signal},    "f10_retail_working_capital_payables_slope_diff_norm_63d_v133_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_63d_v133_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_63d_v134_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_63d_v134_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_63d_v135_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_63d_v135_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_126d_v136_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_126d_v136_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_126d_v137_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_126d_v137_signal},    "f10_retail_working_capital_payables_slope_diff_norm_126d_v138_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_126d_v138_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_126d_v139_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_126d_v139_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_126d_v140_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_126d_v140_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_252d_v141_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_252d_v141_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_252d_v142_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_252d_v142_signal},    "f10_retail_working_capital_payables_slope_diff_norm_252d_v143_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_252d_v143_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_252d_v144_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_252d_v144_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_252d_v145_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_252d_v145_signal},    "f10_retail_working_capital_inventory_slope_diff_norm_504d_v146_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_slope_diff_norm_504d_v146_signal},    "f10_retail_working_capital_receivables_slope_diff_norm_504d_v147_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_slope_diff_norm_504d_v147_signal},    "f10_retail_working_capital_payables_slope_diff_norm_504d_v148_signal": {"inputs": [], "func": f10_retail_working_capital_payables_slope_diff_norm_504d_v148_signal},    "f10_retail_working_capital_revenue_slope_diff_norm_504d_v149_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_slope_diff_norm_504d_v149_signal},    "f10_retail_working_capital_wc_drag_slope_diff_norm_504d_v150_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_slope_diff_norm_504d_v150_signal},
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
