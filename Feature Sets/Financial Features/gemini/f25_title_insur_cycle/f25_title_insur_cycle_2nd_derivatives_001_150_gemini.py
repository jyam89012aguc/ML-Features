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

def f25_title_insur_cycle_revenue_slope_pct_5d_v001_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_5d_v002_signal(inventory):
    """Percentage slope for Raw level of inventory over 5d window."""
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_5d_v003_signal(cor):
    """Percentage slope for Raw level of cor over 5d window."""
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_5d_v004_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 5d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_10d_v005_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_10d_v006_signal(inventory):
    """Percentage slope for Raw level of inventory over 10d window."""
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_10d_v007_signal(cor):
    """Percentage slope for Raw level of cor over 10d window."""
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_10d_v008_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 10d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_21d_v009_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_21d_v010_signal(inventory):
    """Percentage slope for Raw level of inventory over 21d window."""
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_21d_v011_signal(cor):
    """Percentage slope for Raw level of cor over 21d window."""
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_21d_v012_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 21d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_42d_v013_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_42d_v014_signal(inventory):
    """Percentage slope for Raw level of inventory over 42d window."""
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_42d_v015_signal(cor):
    """Percentage slope for Raw level of cor over 42d window."""
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_42d_v016_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 42d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_63d_v017_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_63d_v018_signal(inventory):
    """Percentage slope for Raw level of inventory over 63d window."""
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_63d_v019_signal(cor):
    """Percentage slope for Raw level of cor over 63d window."""
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_63d_v020_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 63d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_126d_v021_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_126d_v022_signal(inventory):
    """Percentage slope for Raw level of inventory over 126d window."""
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_126d_v023_signal(cor):
    """Percentage slope for Raw level of cor over 126d window."""
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_126d_v024_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 126d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_252d_v025_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_252d_v026_signal(inventory):
    """Percentage slope for Raw level of inventory over 252d window."""
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_252d_v027_signal(cor):
    """Percentage slope for Raw level of cor over 252d window."""
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_252d_v028_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 252d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_504d_v029_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_504d_v030_signal(inventory):
    """Percentage slope for Raw level of inventory over 504d window."""
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_504d_v031_signal(cor):
    """Percentage slope for Raw level of cor over 504d window."""
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_504d_v032_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 504d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_756d_v033_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_756d_v034_signal(inventory):
    """Percentage slope for Raw level of inventory over 756d window."""
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_756d_v035_signal(cor):
    """Percentage slope for Raw level of cor over 756d window."""
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_756d_v036_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 756d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_1008d_v037_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_1008d_v038_signal(inventory):
    """Percentage slope for Raw level of inventory over 1008d window."""
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_1008d_v039_signal(cor):
    """Percentage slope for Raw level of cor over 1008d window."""
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_1008d_v040_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 1008d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_pct_1260d_v041_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_pct_1260d_v042_signal(inventory):
    """Percentage slope for Raw level of inventory over 1260d window."""
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_pct_1260d_v043_signal(cor):
    """Percentage slope for Raw level of cor over 1260d window."""
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_pct_1260d_v044_signal(revenue):
    """Percentage slope for Revenue relative to long-term cycle over 1260d window."""
    res = _slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_5d_v045_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_5d_v046_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 5d window."""
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_5d_v047_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 5d window."""
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_5d_v048_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 5d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_10d_v049_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_10d_v050_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 10d window."""
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_10d_v051_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 10d window."""
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_10d_v052_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 10d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_21d_v053_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_21d_v054_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 21d window."""
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_21d_v055_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 21d window."""
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_21d_v056_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 21d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_42d_v057_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_42d_v058_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 42d window."""
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_42d_v059_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 42d window."""
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_42d_v060_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 42d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_63d_v061_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_63d_v062_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 63d window."""
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_63d_v063_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 63d window."""
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_63d_v064_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 63d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_126d_v065_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_126d_v066_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 126d window."""
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_126d_v067_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 126d window."""
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_126d_v068_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 126d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_252d_v069_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_252d_v070_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 252d window."""
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_252d_v071_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 252d window."""
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_252d_v072_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 252d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_504d_v073_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_504d_v074_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 504d window."""
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_504d_v075_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 504d window."""
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_504d_v076_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 504d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_756d_v077_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_756d_v078_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 756d window."""
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_756d_v079_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 756d window."""
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_756d_v080_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 756d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_1008d_v081_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_1008d_v082_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 1008d window."""
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_1008d_v083_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1008d window."""
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_1008d_v084_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 1008d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_jerk_1260d_v085_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_jerk_1260d_v086_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 1260d window."""
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_jerk_1260d_v087_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1260d window."""
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_jerk_1260d_v088_signal(revenue):
    """Acceleration/Jerk for Revenue relative to long-term cycle over 1260d window."""
    res = _jerk(_ratio(revenue, _sma(revenue, 1260)), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_5d_v089_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_5d_v090_signal(inventory):
    """Normalized slope change for Raw level of inventory over 5d window."""
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_5d_v091_signal(cor):
    """Normalized slope change for Raw level of cor over 5d window."""
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_5d_v092_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 5d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 5).diff(5) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_10d_v093_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_10d_v094_signal(inventory):
    """Normalized slope change for Raw level of inventory over 10d window."""
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_10d_v095_signal(cor):
    """Normalized slope change for Raw level of cor over 10d window."""
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_10d_v096_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 10d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 10).diff(10) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_21d_v097_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_21d_v098_signal(inventory):
    """Normalized slope change for Raw level of inventory over 21d window."""
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_21d_v099_signal(cor):
    """Normalized slope change for Raw level of cor over 21d window."""
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_21d_v100_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 21d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 21).diff(21) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_42d_v101_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_42d_v102_signal(inventory):
    """Normalized slope change for Raw level of inventory over 42d window."""
    res = (_slope_pct(inventory, 42).diff(42) / _sma(inventory.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_42d_v103_signal(cor):
    """Normalized slope change for Raw level of cor over 42d window."""
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_42d_v104_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 42d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 42).diff(42) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_63d_v105_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_63d_v106_signal(inventory):
    """Normalized slope change for Raw level of inventory over 63d window."""
    res = (_slope_pct(inventory, 63).diff(63) / _sma(inventory.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_63d_v107_signal(cor):
    """Normalized slope change for Raw level of cor over 63d window."""
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_63d_v108_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 63d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 63).diff(63) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_126d_v109_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_126d_v110_signal(inventory):
    """Normalized slope change for Raw level of inventory over 126d window."""
    res = (_slope_pct(inventory, 126).diff(126) / _sma(inventory.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_126d_v111_signal(cor):
    """Normalized slope change for Raw level of cor over 126d window."""
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_126d_v112_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 126d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 126).diff(126) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_252d_v113_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_252d_v114_signal(inventory):
    """Normalized slope change for Raw level of inventory over 252d window."""
    res = (_slope_pct(inventory, 252).diff(252) / _sma(inventory.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_252d_v115_signal(cor):
    """Normalized slope change for Raw level of cor over 252d window."""
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_252d_v116_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 252d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 252).diff(252) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_504d_v117_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_504d_v118_signal(inventory):
    """Normalized slope change for Raw level of inventory over 504d window."""
    res = (_slope_pct(inventory, 504).diff(504) / _sma(inventory.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_504d_v119_signal(cor):
    """Normalized slope change for Raw level of cor over 504d window."""
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_504d_v120_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 504d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 504).diff(504) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_756d_v121_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_756d_v122_signal(inventory):
    """Normalized slope change for Raw level of inventory over 756d window."""
    res = (_slope_pct(inventory, 756).diff(756) / _sma(inventory.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_756d_v123_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_756d_v124_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 756d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 756).diff(756) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_1008d_v125_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_1008d_v126_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1008d window."""
    res = (_slope_pct(inventory, 1008).diff(1008) / _sma(inventory.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_1008d_v127_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_1008d_v128_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 1008d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1008).diff(1008) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_slope_diff_norm_1260d_v129_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_slope_diff_norm_1260d_v130_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1260d window."""
    res = (_slope_pct(inventory, 1260).diff(1260) / _sma(inventory.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_slope_diff_norm_1260d_v131_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_slope_diff_norm_1260d_v132_signal(revenue):
    """Normalized slope change for Revenue relative to long-term cycle over 1260d window."""
    res = (_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1260).diff(1260) / _sma(_ratio(revenue, _sma(revenue, 1260)).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_5d_v133_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_5d_v134_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 5d window."""
    res = _z(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_5d_v135_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_5d_v136_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 5d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_10d_v137_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_10d_v138_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 10d window."""
    res = _z(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_10d_v139_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_10d_v140_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 10d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_21d_v141_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_21d_v142_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 21d window."""
    res = _z(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_21d_v143_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_21d_v144_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 21d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_42d_v145_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_42d_v146_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 42d window."""
    res = _z(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_42d_v147_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_42d_v148_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 42d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_63d_v149_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_63d_v150_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 63d window."""
    res = _z(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f25_title_insur_cycle_revenue_slope_pct_5d_v001_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_5d_v001_signal},
    "f25_title_insur_cycle_inventory_slope_pct_5d_v002_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_5d_v002_signal},
    "f25_title_insur_cycle_cor_slope_pct_5d_v003_signal": {"func": f25_title_insur_cycle_cor_slope_pct_5d_v003_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_5d_v004_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_5d_v004_signal},
    "f25_title_insur_cycle_revenue_slope_pct_10d_v005_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_10d_v005_signal},
    "f25_title_insur_cycle_inventory_slope_pct_10d_v006_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_10d_v006_signal},
    "f25_title_insur_cycle_cor_slope_pct_10d_v007_signal": {"func": f25_title_insur_cycle_cor_slope_pct_10d_v007_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_10d_v008_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_10d_v008_signal},
    "f25_title_insur_cycle_revenue_slope_pct_21d_v009_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_21d_v009_signal},
    "f25_title_insur_cycle_inventory_slope_pct_21d_v010_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_21d_v010_signal},
    "f25_title_insur_cycle_cor_slope_pct_21d_v011_signal": {"func": f25_title_insur_cycle_cor_slope_pct_21d_v011_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_21d_v012_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_21d_v012_signal},
    "f25_title_insur_cycle_revenue_slope_pct_42d_v013_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_42d_v013_signal},
    "f25_title_insur_cycle_inventory_slope_pct_42d_v014_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_42d_v014_signal},
    "f25_title_insur_cycle_cor_slope_pct_42d_v015_signal": {"func": f25_title_insur_cycle_cor_slope_pct_42d_v015_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_42d_v016_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_42d_v016_signal},
    "f25_title_insur_cycle_revenue_slope_pct_63d_v017_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_63d_v017_signal},
    "f25_title_insur_cycle_inventory_slope_pct_63d_v018_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_63d_v018_signal},
    "f25_title_insur_cycle_cor_slope_pct_63d_v019_signal": {"func": f25_title_insur_cycle_cor_slope_pct_63d_v019_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_63d_v020_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_63d_v020_signal},
    "f25_title_insur_cycle_revenue_slope_pct_126d_v021_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_126d_v021_signal},
    "f25_title_insur_cycle_inventory_slope_pct_126d_v022_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_126d_v022_signal},
    "f25_title_insur_cycle_cor_slope_pct_126d_v023_signal": {"func": f25_title_insur_cycle_cor_slope_pct_126d_v023_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_126d_v024_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_126d_v024_signal},
    "f25_title_insur_cycle_revenue_slope_pct_252d_v025_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_252d_v025_signal},
    "f25_title_insur_cycle_inventory_slope_pct_252d_v026_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_252d_v026_signal},
    "f25_title_insur_cycle_cor_slope_pct_252d_v027_signal": {"func": f25_title_insur_cycle_cor_slope_pct_252d_v027_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_252d_v028_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_252d_v028_signal},
    "f25_title_insur_cycle_revenue_slope_pct_504d_v029_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_504d_v029_signal},
    "f25_title_insur_cycle_inventory_slope_pct_504d_v030_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_504d_v030_signal},
    "f25_title_insur_cycle_cor_slope_pct_504d_v031_signal": {"func": f25_title_insur_cycle_cor_slope_pct_504d_v031_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_504d_v032_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_504d_v032_signal},
    "f25_title_insur_cycle_revenue_slope_pct_756d_v033_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_756d_v033_signal},
    "f25_title_insur_cycle_inventory_slope_pct_756d_v034_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_756d_v034_signal},
    "f25_title_insur_cycle_cor_slope_pct_756d_v035_signal": {"func": f25_title_insur_cycle_cor_slope_pct_756d_v035_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_756d_v036_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_756d_v036_signal},
    "f25_title_insur_cycle_revenue_slope_pct_1008d_v037_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_1008d_v037_signal},
    "f25_title_insur_cycle_inventory_slope_pct_1008d_v038_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_1008d_v038_signal},
    "f25_title_insur_cycle_cor_slope_pct_1008d_v039_signal": {"func": f25_title_insur_cycle_cor_slope_pct_1008d_v039_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_1008d_v040_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_1008d_v040_signal},
    "f25_title_insur_cycle_revenue_slope_pct_1260d_v041_signal": {"func": f25_title_insur_cycle_revenue_slope_pct_1260d_v041_signal},
    "f25_title_insur_cycle_inventory_slope_pct_1260d_v042_signal": {"func": f25_title_insur_cycle_inventory_slope_pct_1260d_v042_signal},
    "f25_title_insur_cycle_cor_slope_pct_1260d_v043_signal": {"func": f25_title_insur_cycle_cor_slope_pct_1260d_v043_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_pct_1260d_v044_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_pct_1260d_v044_signal},
    "f25_title_insur_cycle_revenue_jerk_5d_v045_signal": {"func": f25_title_insur_cycle_revenue_jerk_5d_v045_signal},
    "f25_title_insur_cycle_inventory_jerk_5d_v046_signal": {"func": f25_title_insur_cycle_inventory_jerk_5d_v046_signal},
    "f25_title_insur_cycle_cor_jerk_5d_v047_signal": {"func": f25_title_insur_cycle_cor_jerk_5d_v047_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_5d_v048_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_5d_v048_signal},
    "f25_title_insur_cycle_revenue_jerk_10d_v049_signal": {"func": f25_title_insur_cycle_revenue_jerk_10d_v049_signal},
    "f25_title_insur_cycle_inventory_jerk_10d_v050_signal": {"func": f25_title_insur_cycle_inventory_jerk_10d_v050_signal},
    "f25_title_insur_cycle_cor_jerk_10d_v051_signal": {"func": f25_title_insur_cycle_cor_jerk_10d_v051_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_10d_v052_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_10d_v052_signal},
    "f25_title_insur_cycle_revenue_jerk_21d_v053_signal": {"func": f25_title_insur_cycle_revenue_jerk_21d_v053_signal},
    "f25_title_insur_cycle_inventory_jerk_21d_v054_signal": {"func": f25_title_insur_cycle_inventory_jerk_21d_v054_signal},
    "f25_title_insur_cycle_cor_jerk_21d_v055_signal": {"func": f25_title_insur_cycle_cor_jerk_21d_v055_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_21d_v056_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_21d_v056_signal},
    "f25_title_insur_cycle_revenue_jerk_42d_v057_signal": {"func": f25_title_insur_cycle_revenue_jerk_42d_v057_signal},
    "f25_title_insur_cycle_inventory_jerk_42d_v058_signal": {"func": f25_title_insur_cycle_inventory_jerk_42d_v058_signal},
    "f25_title_insur_cycle_cor_jerk_42d_v059_signal": {"func": f25_title_insur_cycle_cor_jerk_42d_v059_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_42d_v060_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_42d_v060_signal},
    "f25_title_insur_cycle_revenue_jerk_63d_v061_signal": {"func": f25_title_insur_cycle_revenue_jerk_63d_v061_signal},
    "f25_title_insur_cycle_inventory_jerk_63d_v062_signal": {"func": f25_title_insur_cycle_inventory_jerk_63d_v062_signal},
    "f25_title_insur_cycle_cor_jerk_63d_v063_signal": {"func": f25_title_insur_cycle_cor_jerk_63d_v063_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_63d_v064_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_63d_v064_signal},
    "f25_title_insur_cycle_revenue_jerk_126d_v065_signal": {"func": f25_title_insur_cycle_revenue_jerk_126d_v065_signal},
    "f25_title_insur_cycle_inventory_jerk_126d_v066_signal": {"func": f25_title_insur_cycle_inventory_jerk_126d_v066_signal},
    "f25_title_insur_cycle_cor_jerk_126d_v067_signal": {"func": f25_title_insur_cycle_cor_jerk_126d_v067_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_126d_v068_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_126d_v068_signal},
    "f25_title_insur_cycle_revenue_jerk_252d_v069_signal": {"func": f25_title_insur_cycle_revenue_jerk_252d_v069_signal},
    "f25_title_insur_cycle_inventory_jerk_252d_v070_signal": {"func": f25_title_insur_cycle_inventory_jerk_252d_v070_signal},
    "f25_title_insur_cycle_cor_jerk_252d_v071_signal": {"func": f25_title_insur_cycle_cor_jerk_252d_v071_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_252d_v072_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_252d_v072_signal},
    "f25_title_insur_cycle_revenue_jerk_504d_v073_signal": {"func": f25_title_insur_cycle_revenue_jerk_504d_v073_signal},
    "f25_title_insur_cycle_inventory_jerk_504d_v074_signal": {"func": f25_title_insur_cycle_inventory_jerk_504d_v074_signal},
    "f25_title_insur_cycle_cor_jerk_504d_v075_signal": {"func": f25_title_insur_cycle_cor_jerk_504d_v075_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_504d_v076_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_504d_v076_signal},
    "f25_title_insur_cycle_revenue_jerk_756d_v077_signal": {"func": f25_title_insur_cycle_revenue_jerk_756d_v077_signal},
    "f25_title_insur_cycle_inventory_jerk_756d_v078_signal": {"func": f25_title_insur_cycle_inventory_jerk_756d_v078_signal},
    "f25_title_insur_cycle_cor_jerk_756d_v079_signal": {"func": f25_title_insur_cycle_cor_jerk_756d_v079_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_756d_v080_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_756d_v080_signal},
    "f25_title_insur_cycle_revenue_jerk_1008d_v081_signal": {"func": f25_title_insur_cycle_revenue_jerk_1008d_v081_signal},
    "f25_title_insur_cycle_inventory_jerk_1008d_v082_signal": {"func": f25_title_insur_cycle_inventory_jerk_1008d_v082_signal},
    "f25_title_insur_cycle_cor_jerk_1008d_v083_signal": {"func": f25_title_insur_cycle_cor_jerk_1008d_v083_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_1008d_v084_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_1008d_v084_signal},
    "f25_title_insur_cycle_revenue_jerk_1260d_v085_signal": {"func": f25_title_insur_cycle_revenue_jerk_1260d_v085_signal},
    "f25_title_insur_cycle_inventory_jerk_1260d_v086_signal": {"func": f25_title_insur_cycle_inventory_jerk_1260d_v086_signal},
    "f25_title_insur_cycle_cor_jerk_1260d_v087_signal": {"func": f25_title_insur_cycle_cor_jerk_1260d_v087_signal},
    "f25_title_insur_cycle_revenue_cycle_jerk_1260d_v088_signal": {"func": f25_title_insur_cycle_revenue_cycle_jerk_1260d_v088_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_5d_v089_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_5d_v089_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_5d_v090_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_5d_v090_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_5d_v091_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_5d_v091_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_5d_v092_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_5d_v092_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_10d_v093_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_10d_v093_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_10d_v094_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_10d_v094_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_10d_v095_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_10d_v095_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_10d_v096_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_10d_v096_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_21d_v097_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_21d_v097_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_21d_v098_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_21d_v098_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_21d_v099_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_21d_v099_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_21d_v100_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_21d_v100_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_42d_v101_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_42d_v101_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_42d_v102_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_42d_v102_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_42d_v103_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_42d_v103_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_42d_v104_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_42d_v104_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_63d_v105_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_63d_v105_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_63d_v106_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_63d_v106_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_63d_v107_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_63d_v107_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_63d_v108_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_63d_v108_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_126d_v109_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_126d_v109_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_126d_v110_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_126d_v110_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_126d_v111_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_126d_v111_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_126d_v112_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_126d_v112_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_252d_v113_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_252d_v113_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_252d_v114_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_252d_v114_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_252d_v115_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_252d_v115_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_252d_v116_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_252d_v116_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_504d_v117_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_504d_v117_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_504d_v118_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_504d_v118_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_504d_v119_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_504d_v119_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_504d_v120_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_504d_v120_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_756d_v121_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_756d_v121_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_756d_v122_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_756d_v122_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_756d_v123_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_756d_v123_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_756d_v124_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_756d_v124_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_1008d_v125_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_1008d_v125_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_1008d_v126_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_1008d_v126_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_1008d_v127_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_1008d_v127_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_1008d_v128_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_1008d_v128_signal},
    "f25_title_insur_cycle_revenue_slope_diff_norm_1260d_v129_signal": {"func": f25_title_insur_cycle_revenue_slope_diff_norm_1260d_v129_signal},
    "f25_title_insur_cycle_inventory_slope_diff_norm_1260d_v130_signal": {"func": f25_title_insur_cycle_inventory_slope_diff_norm_1260d_v130_signal},
    "f25_title_insur_cycle_cor_slope_diff_norm_1260d_v131_signal": {"func": f25_title_insur_cycle_cor_slope_diff_norm_1260d_v131_signal},
    "f25_title_insur_cycle_revenue_cycle_slope_diff_norm_1260d_v132_signal": {"func": f25_title_insur_cycle_revenue_cycle_slope_diff_norm_1260d_v132_signal},
    "f25_title_insur_cycle_revenue_mom_z_5d_v133_signal": {"func": f25_title_insur_cycle_revenue_mom_z_5d_v133_signal},
    "f25_title_insur_cycle_inventory_mom_z_5d_v134_signal": {"func": f25_title_insur_cycle_inventory_mom_z_5d_v134_signal},
    "f25_title_insur_cycle_cor_mom_z_5d_v135_signal": {"func": f25_title_insur_cycle_cor_mom_z_5d_v135_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_5d_v136_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_5d_v136_signal},
    "f25_title_insur_cycle_revenue_mom_z_10d_v137_signal": {"func": f25_title_insur_cycle_revenue_mom_z_10d_v137_signal},
    "f25_title_insur_cycle_inventory_mom_z_10d_v138_signal": {"func": f25_title_insur_cycle_inventory_mom_z_10d_v138_signal},
    "f25_title_insur_cycle_cor_mom_z_10d_v139_signal": {"func": f25_title_insur_cycle_cor_mom_z_10d_v139_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_10d_v140_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_10d_v140_signal},
    "f25_title_insur_cycle_revenue_mom_z_21d_v141_signal": {"func": f25_title_insur_cycle_revenue_mom_z_21d_v141_signal},
    "f25_title_insur_cycle_inventory_mom_z_21d_v142_signal": {"func": f25_title_insur_cycle_inventory_mom_z_21d_v142_signal},
    "f25_title_insur_cycle_cor_mom_z_21d_v143_signal": {"func": f25_title_insur_cycle_cor_mom_z_21d_v143_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_21d_v144_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_21d_v144_signal},
    "f25_title_insur_cycle_revenue_mom_z_42d_v145_signal": {"func": f25_title_insur_cycle_revenue_mom_z_42d_v145_signal},
    "f25_title_insur_cycle_inventory_mom_z_42d_v146_signal": {"func": f25_title_insur_cycle_inventory_mom_z_42d_v146_signal},
    "f25_title_insur_cycle_cor_mom_z_42d_v147_signal": {"func": f25_title_insur_cycle_cor_mom_z_42d_v147_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_42d_v148_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_42d_v148_signal},
    "f25_title_insur_cycle_revenue_mom_z_63d_v149_signal": {"func": f25_title_insur_cycle_revenue_mom_z_63d_v149_signal},
    "f25_title_insur_cycle_inventory_mom_z_63d_v150_signal": {"func": f25_title_insur_cycle_inventory_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 25...")
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
