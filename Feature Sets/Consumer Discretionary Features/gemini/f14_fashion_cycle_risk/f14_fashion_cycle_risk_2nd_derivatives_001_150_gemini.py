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

def f14_fashion_cycle_risk_inventory_slope_pct_5d_v001_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 5d window."""
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_5d_v002_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 5d window."""
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_5d_v003_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 5d window."""
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_5d_v004_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 5d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_10d_v005_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 10d window."""
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_10d_v006_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 10d window."""
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_10d_v007_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 10d window."""
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_10d_v008_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 10d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_21d_v009_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 21d window."""
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_21d_v010_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 21d window."""
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_21d_v011_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 21d window."""
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_21d_v012_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 21d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_42d_v013_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 42d window."""
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_42d_v014_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 42d window."""
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_42d_v015_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 42d window."""
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_42d_v016_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 42d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_63d_v017_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 63d window."""
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_63d_v018_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 63d window."""
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_63d_v019_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 63d window."""
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_63d_v020_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 63d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_126d_v021_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 126d window."""
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_126d_v022_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 126d window."""
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_126d_v023_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 126d window."""
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_126d_v024_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 126d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_252d_v025_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 252d window."""
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_252d_v026_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 252d window."""
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_252d_v027_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 252d window."""
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_252d_v028_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 252d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_504d_v029_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 504d window."""
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_504d_v030_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 504d window."""
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_504d_v031_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 504d window."""
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_504d_v032_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 504d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_756d_v033_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 756d window."""
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_756d_v034_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 756d window."""
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_756d_v035_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 756d window."""
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_756d_v036_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 756d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_1008d_v037_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 1008d window."""
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_1008d_v038_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 1008d window."""
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_1008d_v039_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 1008d window."""
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_1008d_v040_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 1008d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_pct_1260d_v041_signal(inventory):
    """Percentage slope for momentum for Raw level of inventory over 1260d window."""
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_pct_1260d_v042_signal(cor):
    """Percentage slope for momentum for Raw level of cor over 1260d window."""
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_pct_1260d_v043_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 1260d window."""
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_pct_1260d_v044_signal(inventory, cor, grossmargin):
    """Percentage slope for momentum for Interactive risk of inventory build-up and margin volatility over 1260d window."""
    res = _slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_5d_v045_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 5d window."""
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_5d_v046_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 5d window."""
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_5d_v047_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 5d window."""
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_5d_v048_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 5d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_10d_v049_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 10d window."""
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_10d_v050_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 10d window."""
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_10d_v051_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 10d window."""
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_10d_v052_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 10d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_21d_v053_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 21d window."""
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_21d_v054_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 21d window."""
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_21d_v055_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 21d window."""
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_21d_v056_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 21d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_42d_v057_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 42d window."""
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_42d_v058_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 42d window."""
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_42d_v059_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 42d window."""
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_42d_v060_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 42d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_63d_v061_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 63d window."""
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_63d_v062_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 63d window."""
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_63d_v063_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 63d window."""
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_63d_v064_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 63d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_126d_v065_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 126d window."""
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_126d_v066_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 126d window."""
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_126d_v067_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 126d window."""
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_126d_v068_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 126d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_252d_v069_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 252d window."""
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_252d_v070_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 252d window."""
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_252d_v071_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 252d window."""
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_252d_v072_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 252d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_504d_v073_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 504d window."""
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_504d_v074_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 504d window."""
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_504d_v075_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 504d window."""
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_504d_v076_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 504d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_756d_v077_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 756d window."""
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_756d_v078_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 756d window."""
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_756d_v079_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 756d window."""
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_756d_v080_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 756d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_1008d_v081_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 1008d window."""
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_1008d_v082_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 1008d window."""
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_1008d_v083_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 1008d window."""
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_1008d_v084_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 1008d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_jerk_1260d_v085_signal(inventory):
    """Acceleration/Jerk for structural shifts for Raw level of inventory over 1260d window."""
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_jerk_1260d_v086_signal(cor):
    """Acceleration/Jerk for structural shifts for Raw level of cor over 1260d window."""
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_jerk_1260d_v087_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 1260d window."""
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_jerk_1260d_v088_signal(inventory, cor, grossmargin):
    """Acceleration/Jerk for structural shifts for Interactive risk of inventory build-up and margin volatility over 1260d window."""
    res = _jerk(_ratio(inventory, cor) * _std(grossmargin, 63), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_5d_v089_signal(inventory):
    """Normalized slope change for Raw level of inventory over 5d window."""
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_5d_v090_signal(cor):
    """Normalized slope change for Raw level of cor over 5d window."""
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_5d_v091_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 5d window."""
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_5d_v092_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 5d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 5).diff(5) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_10d_v093_signal(inventory):
    """Normalized slope change for Raw level of inventory over 10d window."""
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_10d_v094_signal(cor):
    """Normalized slope change for Raw level of cor over 10d window."""
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_10d_v095_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 10d window."""
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_10d_v096_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 10d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 10).diff(10) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_21d_v097_signal(inventory):
    """Normalized slope change for Raw level of inventory over 21d window."""
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_21d_v098_signal(cor):
    """Normalized slope change for Raw level of cor over 21d window."""
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_21d_v099_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 21d window."""
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_21d_v100_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 21d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 21).diff(21) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_42d_v101_signal(inventory):
    """Normalized slope change for Raw level of inventory over 42d window."""
    res = (_slope_pct(inventory, 42).diff(42) / _sma(inventory.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_42d_v102_signal(cor):
    """Normalized slope change for Raw level of cor over 42d window."""
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_42d_v103_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 42d window."""
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_42d_v104_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 42d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 42).diff(42) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_63d_v105_signal(inventory):
    """Normalized slope change for Raw level of inventory over 63d window."""
    res = (_slope_pct(inventory, 63).diff(63) / _sma(inventory.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_63d_v106_signal(cor):
    """Normalized slope change for Raw level of cor over 63d window."""
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_63d_v107_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 63d window."""
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_63d_v108_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 63d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 63).diff(63) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_126d_v109_signal(inventory):
    """Normalized slope change for Raw level of inventory over 126d window."""
    res = (_slope_pct(inventory, 126).diff(126) / _sma(inventory.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_126d_v110_signal(cor):
    """Normalized slope change for Raw level of cor over 126d window."""
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_126d_v111_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 126d window."""
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_126d_v112_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 126d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 126).diff(126) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_252d_v113_signal(inventory):
    """Normalized slope change for Raw level of inventory over 252d window."""
    res = (_slope_pct(inventory, 252).diff(252) / _sma(inventory.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_252d_v114_signal(cor):
    """Normalized slope change for Raw level of cor over 252d window."""
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_252d_v115_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 252d window."""
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_252d_v116_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 252d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 252).diff(252) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_504d_v117_signal(inventory):
    """Normalized slope change for Raw level of inventory over 504d window."""
    res = (_slope_pct(inventory, 504).diff(504) / _sma(inventory.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_504d_v118_signal(cor):
    """Normalized slope change for Raw level of cor over 504d window."""
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_504d_v119_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 504d window."""
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_504d_v120_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 504d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 504).diff(504) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_756d_v121_signal(inventory):
    """Normalized slope change for Raw level of inventory over 756d window."""
    res = (_slope_pct(inventory, 756).diff(756) / _sma(inventory.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_756d_v122_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_756d_v123_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 756d window."""
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_756d_v124_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 756d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 756).diff(756) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_1008d_v125_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1008d window."""
    res = (_slope_pct(inventory, 1008).diff(1008) / _sma(inventory.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_1008d_v126_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_1008d_v127_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1008d window."""
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_1008d_v128_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 1008d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 1008).diff(1008) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_slope_diff_norm_1260d_v129_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1260d window."""
    res = (_slope_pct(inventory, 1260).diff(1260) / _sma(inventory.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_slope_diff_norm_1260d_v130_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_slope_diff_norm_1260d_v131_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1260d window."""
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_slope_diff_norm_1260d_v132_signal(inventory, cor, grossmargin):
    """Normalized slope change for Interactive risk of inventory build-up and margin volatility over 1260d window."""
    res = (_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 1260).diff(1260) / _sma(_ratio(inventory, cor) * _std(grossmargin, 63).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_mom_z_5d_v133_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 5d window."""
    res = _z(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_mom_z_5d_v134_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_mom_z_5d_v135_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 5d window."""
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_mom_z_5d_v136_signal(inventory, cor, grossmargin):
    """Relative momentum strength for Interactive risk of inventory build-up and margin volatility over 5d window."""
    res = _z(_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_mom_z_10d_v137_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 10d window."""
    res = _z(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_mom_z_10d_v138_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_mom_z_10d_v139_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 10d window."""
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_mom_z_10d_v140_signal(inventory, cor, grossmargin):
    """Relative momentum strength for Interactive risk of inventory build-up and margin volatility over 10d window."""
    res = _z(_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_mom_z_21d_v141_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 21d window."""
    res = _z(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_mom_z_21d_v142_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_mom_z_21d_v143_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 21d window."""
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_mom_z_21d_v144_signal(inventory, cor, grossmargin):
    """Relative momentum strength for Interactive risk of inventory build-up and margin volatility over 21d window."""
    res = _z(_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_mom_z_42d_v145_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 42d window."""
    res = _z(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_mom_z_42d_v146_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_grossmargin_mom_z_42d_v147_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 42d window."""
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_risk_index_mom_z_42d_v148_signal(inventory, cor, grossmargin):
    """Relative momentum strength for Interactive risk of inventory build-up and margin volatility over 42d window."""
    res = _z(_slope_pct(_ratio(inventory, cor) * _std(grossmargin, 63), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_inventory_mom_z_63d_v149_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 63d window."""
    res = _z(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_fashion_cycle_risk_cor_mom_z_63d_v150_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f14_fashion_cycle_risk_inventory_slope_pct_5d_v001_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_5d_v001_signal},    "f14_fashion_cycle_risk_cor_slope_pct_5d_v002_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_5d_v002_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_5d_v003_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_5d_v003_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_5d_v004_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_5d_v004_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_10d_v005_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_10d_v005_signal},    "f14_fashion_cycle_risk_cor_slope_pct_10d_v006_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_10d_v006_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_10d_v007_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_10d_v007_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_10d_v008_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_10d_v008_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_21d_v009_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_21d_v009_signal},    "f14_fashion_cycle_risk_cor_slope_pct_21d_v010_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_21d_v010_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_21d_v011_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_21d_v011_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_21d_v012_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_21d_v012_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_42d_v013_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_42d_v013_signal},    "f14_fashion_cycle_risk_cor_slope_pct_42d_v014_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_42d_v014_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_42d_v015_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_42d_v015_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_42d_v016_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_42d_v016_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_63d_v017_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_63d_v017_signal},    "f14_fashion_cycle_risk_cor_slope_pct_63d_v018_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_63d_v018_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_63d_v019_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_63d_v019_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_63d_v020_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_63d_v020_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_126d_v021_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_126d_v021_signal},    "f14_fashion_cycle_risk_cor_slope_pct_126d_v022_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_126d_v022_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_126d_v023_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_126d_v023_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_126d_v024_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_126d_v024_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_252d_v025_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_252d_v025_signal},    "f14_fashion_cycle_risk_cor_slope_pct_252d_v026_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_252d_v026_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_252d_v027_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_252d_v027_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_252d_v028_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_252d_v028_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_504d_v029_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_504d_v029_signal},    "f14_fashion_cycle_risk_cor_slope_pct_504d_v030_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_504d_v030_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_504d_v031_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_504d_v031_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_504d_v032_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_504d_v032_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_756d_v033_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_756d_v033_signal},    "f14_fashion_cycle_risk_cor_slope_pct_756d_v034_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_756d_v034_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_756d_v035_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_756d_v035_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_756d_v036_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_756d_v036_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_1008d_v037_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_1008d_v037_signal},    "f14_fashion_cycle_risk_cor_slope_pct_1008d_v038_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_1008d_v038_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_1008d_v039_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_1008d_v039_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_1008d_v040_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_1008d_v040_signal},    "f14_fashion_cycle_risk_inventory_slope_pct_1260d_v041_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_pct_1260d_v041_signal},    "f14_fashion_cycle_risk_cor_slope_pct_1260d_v042_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_pct_1260d_v042_signal},    "f14_fashion_cycle_risk_grossmargin_slope_pct_1260d_v043_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_pct_1260d_v043_signal},    "f14_fashion_cycle_risk_risk_index_slope_pct_1260d_v044_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_pct_1260d_v044_signal},    "f14_fashion_cycle_risk_inventory_jerk_5d_v045_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_5d_v045_signal},    "f14_fashion_cycle_risk_cor_jerk_5d_v046_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_5d_v046_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_5d_v047_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_5d_v047_signal},    "f14_fashion_cycle_risk_risk_index_jerk_5d_v048_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_5d_v048_signal},    "f14_fashion_cycle_risk_inventory_jerk_10d_v049_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_10d_v049_signal},    "f14_fashion_cycle_risk_cor_jerk_10d_v050_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_10d_v050_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_10d_v051_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_10d_v051_signal},    "f14_fashion_cycle_risk_risk_index_jerk_10d_v052_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_10d_v052_signal},    "f14_fashion_cycle_risk_inventory_jerk_21d_v053_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_21d_v053_signal},    "f14_fashion_cycle_risk_cor_jerk_21d_v054_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_21d_v054_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_21d_v055_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_21d_v055_signal},    "f14_fashion_cycle_risk_risk_index_jerk_21d_v056_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_21d_v056_signal},    "f14_fashion_cycle_risk_inventory_jerk_42d_v057_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_42d_v057_signal},    "f14_fashion_cycle_risk_cor_jerk_42d_v058_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_42d_v058_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_42d_v059_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_42d_v059_signal},    "f14_fashion_cycle_risk_risk_index_jerk_42d_v060_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_42d_v060_signal},    "f14_fashion_cycle_risk_inventory_jerk_63d_v061_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_63d_v061_signal},    "f14_fashion_cycle_risk_cor_jerk_63d_v062_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_63d_v062_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_63d_v063_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_63d_v063_signal},    "f14_fashion_cycle_risk_risk_index_jerk_63d_v064_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_63d_v064_signal},    "f14_fashion_cycle_risk_inventory_jerk_126d_v065_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_126d_v065_signal},    "f14_fashion_cycle_risk_cor_jerk_126d_v066_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_126d_v066_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_126d_v067_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_126d_v067_signal},    "f14_fashion_cycle_risk_risk_index_jerk_126d_v068_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_126d_v068_signal},    "f14_fashion_cycle_risk_inventory_jerk_252d_v069_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_252d_v069_signal},    "f14_fashion_cycle_risk_cor_jerk_252d_v070_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_252d_v070_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_252d_v071_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_252d_v071_signal},    "f14_fashion_cycle_risk_risk_index_jerk_252d_v072_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_252d_v072_signal},    "f14_fashion_cycle_risk_inventory_jerk_504d_v073_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_504d_v073_signal},    "f14_fashion_cycle_risk_cor_jerk_504d_v074_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_504d_v074_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_504d_v075_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_504d_v075_signal},    "f14_fashion_cycle_risk_risk_index_jerk_504d_v076_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_504d_v076_signal},    "f14_fashion_cycle_risk_inventory_jerk_756d_v077_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_756d_v077_signal},    "f14_fashion_cycle_risk_cor_jerk_756d_v078_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_756d_v078_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_756d_v079_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_756d_v079_signal},    "f14_fashion_cycle_risk_risk_index_jerk_756d_v080_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_756d_v080_signal},    "f14_fashion_cycle_risk_inventory_jerk_1008d_v081_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_1008d_v081_signal},    "f14_fashion_cycle_risk_cor_jerk_1008d_v082_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_1008d_v082_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_1008d_v083_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_1008d_v083_signal},    "f14_fashion_cycle_risk_risk_index_jerk_1008d_v084_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_1008d_v084_signal},    "f14_fashion_cycle_risk_inventory_jerk_1260d_v085_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_jerk_1260d_v085_signal},    "f14_fashion_cycle_risk_cor_jerk_1260d_v086_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_jerk_1260d_v086_signal},    "f14_fashion_cycle_risk_grossmargin_jerk_1260d_v087_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_jerk_1260d_v087_signal},    "f14_fashion_cycle_risk_risk_index_jerk_1260d_v088_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_jerk_1260d_v088_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_5d_v089_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_5d_v090_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_5d_v091_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_5d_v092_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_10d_v093_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_10d_v094_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_10d_v095_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_10d_v096_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_21d_v097_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_21d_v098_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_21d_v099_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_21d_v100_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_42d_v101_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_42d_v102_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_42d_v103_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_42d_v104_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_63d_v105_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_63d_v106_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_63d_v107_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_63d_v108_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_126d_v109_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_126d_v110_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_126d_v111_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_126d_v112_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_252d_v113_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_252d_v114_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_252d_v115_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_252d_v116_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_504d_v117_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_504d_v118_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_504d_v119_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_504d_v120_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_756d_v121_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_756d_v122_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_756d_v123_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_756d_v124_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_1008d_v125_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_1008d_v126_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_1008d_v127_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_1008d_v128_signal},    "f14_fashion_cycle_risk_inventory_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_slope_diff_norm_1260d_v129_signal},    "f14_fashion_cycle_risk_cor_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_slope_diff_norm_1260d_v130_signal},    "f14_fashion_cycle_risk_grossmargin_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_slope_diff_norm_1260d_v131_signal},    "f14_fashion_cycle_risk_risk_index_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_slope_diff_norm_1260d_v132_signal},    "f14_fashion_cycle_risk_inventory_mom_z_5d_v133_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_mom_z_5d_v133_signal},    "f14_fashion_cycle_risk_cor_mom_z_5d_v134_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_mom_z_5d_v134_signal},    "f14_fashion_cycle_risk_grossmargin_mom_z_5d_v135_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_mom_z_5d_v135_signal},    "f14_fashion_cycle_risk_risk_index_mom_z_5d_v136_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_mom_z_5d_v136_signal},    "f14_fashion_cycle_risk_inventory_mom_z_10d_v137_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_mom_z_10d_v137_signal},    "f14_fashion_cycle_risk_cor_mom_z_10d_v138_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_mom_z_10d_v138_signal},    "f14_fashion_cycle_risk_grossmargin_mom_z_10d_v139_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_mom_z_10d_v139_signal},    "f14_fashion_cycle_risk_risk_index_mom_z_10d_v140_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_mom_z_10d_v140_signal},    "f14_fashion_cycle_risk_inventory_mom_z_21d_v141_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_mom_z_21d_v141_signal},    "f14_fashion_cycle_risk_cor_mom_z_21d_v142_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_mom_z_21d_v142_signal},    "f14_fashion_cycle_risk_grossmargin_mom_z_21d_v143_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_mom_z_21d_v143_signal},    "f14_fashion_cycle_risk_risk_index_mom_z_21d_v144_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_mom_z_21d_v144_signal},    "f14_fashion_cycle_risk_inventory_mom_z_42d_v145_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_mom_z_42d_v145_signal},    "f14_fashion_cycle_risk_cor_mom_z_42d_v146_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_mom_z_42d_v146_signal},    "f14_fashion_cycle_risk_grossmargin_mom_z_42d_v147_signal": {"inputs": [], "func": f14_fashion_cycle_risk_grossmargin_mom_z_42d_v147_signal},    "f14_fashion_cycle_risk_risk_index_mom_z_42d_v148_signal": {"inputs": [], "func": f14_fashion_cycle_risk_risk_index_mom_z_42d_v148_signal},    "f14_fashion_cycle_risk_inventory_mom_z_63d_v149_signal": {"inputs": [], "func": f14_fashion_cycle_risk_inventory_mom_z_63d_v149_signal},    "f14_fashion_cycle_risk_cor_mom_z_63d_v150_signal": {"inputs": [], "func": f14_fashion_cycle_risk_cor_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 14...")
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
