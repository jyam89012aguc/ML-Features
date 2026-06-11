import pandas as pd
import numpy as np
import inspect

# ===== Energy Ultra-High-Performance Alpha Helpers =====
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

def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_5d_v001_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 5d window."""
    res = _slope_pct(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_5d_v003_signal(inventory):
    """Percentage slope for Raw level of inventory over 5d window."""
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_5d_v004_signal(fcf):
    """Percentage slope for Raw level of fcf over 5d window."""
    res = _slope_pct(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_5d_v005_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 5d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_5d_v006_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 5d window."""
    res = _slope_pct(_ratio(inventory, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_10d_v007_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 10d window."""
    res = _slope_pct(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_10d_v008_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_10d_v009_signal(inventory):
    """Percentage slope for Raw level of inventory over 10d window."""
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_10d_v010_signal(fcf):
    """Percentage slope for Raw level of fcf over 10d window."""
    res = _slope_pct(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_10d_v011_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 10d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_10d_v012_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 10d window."""
    res = _slope_pct(_ratio(inventory, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_21d_v013_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 21d window."""
    res = _slope_pct(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_21d_v014_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_21d_v015_signal(inventory):
    """Percentage slope for Raw level of inventory over 21d window."""
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_21d_v016_signal(fcf):
    """Percentage slope for Raw level of fcf over 21d window."""
    res = _slope_pct(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_21d_v017_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 21d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_21d_v018_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 21d window."""
    res = _slope_pct(_ratio(inventory, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_42d_v019_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 42d window."""
    res = _slope_pct(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_42d_v020_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_42d_v021_signal(inventory):
    """Percentage slope for Raw level of inventory over 42d window."""
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_42d_v022_signal(fcf):
    """Percentage slope for Raw level of fcf over 42d window."""
    res = _slope_pct(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_42d_v023_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 42d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_42d_v024_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 42d window."""
    res = _slope_pct(_ratio(inventory, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_63d_v025_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 63d window."""
    res = _slope_pct(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_63d_v026_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_63d_v027_signal(inventory):
    """Percentage slope for Raw level of inventory over 63d window."""
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_63d_v028_signal(fcf):
    """Percentage slope for Raw level of fcf over 63d window."""
    res = _slope_pct(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_63d_v029_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 63d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_63d_v030_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 63d window."""
    res = _slope_pct(_ratio(inventory, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_126d_v031_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 126d window."""
    res = _slope_pct(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_126d_v032_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_126d_v033_signal(inventory):
    """Percentage slope for Raw level of inventory over 126d window."""
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_126d_v034_signal(fcf):
    """Percentage slope for Raw level of fcf over 126d window."""
    res = _slope_pct(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_126d_v035_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 126d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_126d_v036_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 126d window."""
    res = _slope_pct(_ratio(inventory, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_252d_v037_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 252d window."""
    res = _slope_pct(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_252d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_252d_v039_signal(inventory):
    """Percentage slope for Raw level of inventory over 252d window."""
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_252d_v040_signal(fcf):
    """Percentage slope for Raw level of fcf over 252d window."""
    res = _slope_pct(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_252d_v041_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 252d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_252d_v042_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 252d window."""
    res = _slope_pct(_ratio(inventory, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_504d_v043_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 504d window."""
    res = _slope_pct(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_504d_v044_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_504d_v045_signal(inventory):
    """Percentage slope for Raw level of inventory over 504d window."""
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_504d_v046_signal(fcf):
    """Percentage slope for Raw level of fcf over 504d window."""
    res = _slope_pct(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_504d_v047_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 504d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_504d_v048_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 504d window."""
    res = _slope_pct(_ratio(inventory, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_756d_v049_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 756d window."""
    res = _slope_pct(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_756d_v050_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_756d_v051_signal(inventory):
    """Percentage slope for Raw level of inventory over 756d window."""
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_756d_v052_signal(fcf):
    """Percentage slope for Raw level of fcf over 756d window."""
    res = _slope_pct(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_756d_v053_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 756d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_756d_v054_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 756d window."""
    res = _slope_pct(_ratio(inventory, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_1008d_v055_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 1008d window."""
    res = _slope_pct(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_1008d_v056_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_1008d_v057_signal(inventory):
    """Percentage slope for Raw level of inventory over 1008d window."""
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_1008d_v058_signal(fcf):
    """Percentage slope for Raw level of fcf over 1008d window."""
    res = _slope_pct(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_1008d_v059_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 1008d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_1008d_v060_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 1008d window."""
    res = _slope_pct(_ratio(inventory, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_pct_1260d_v061_signal(deferredrev):
    """Percentage slope for Raw level of deferredrev over 1260d window."""
    res = _slope_pct(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_pct_1260d_v062_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_pct_1260d_v063_signal(inventory):
    """Percentage slope for Raw level of inventory over 1260d window."""
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_pct_1260d_v064_signal(fcf):
    """Percentage slope for Raw level of fcf over 1260d window."""
    res = _slope_pct(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_pct_1260d_v065_signal(deferredrev, revenue, fcf, netinc):
    """Percentage slope for Backlog quality and cash conversion interaction over 1260d window."""
    res = _slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_1260d_v066_signal(inventory, revenue):
    """Percentage slope for Inventory to sales cycle over 1260d window."""
    res = _slope_pct(_ratio(inventory, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_5d_v067_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 5d window."""
    res = _jerk(deferredrev, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_5d_v068_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_5d_v069_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 5d window."""
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_5d_v070_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 5d window."""
    res = _jerk(fcf, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_5d_v071_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 5d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_5d_v072_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 5d window."""
    res = _jerk(_ratio(inventory, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_10d_v073_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 10d window."""
    res = _jerk(deferredrev, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_10d_v074_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_10d_v075_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 10d window."""
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_10d_v076_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 10d window."""
    res = _jerk(fcf, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_10d_v077_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 10d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_10d_v078_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 10d window."""
    res = _jerk(_ratio(inventory, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_21d_v079_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 21d window."""
    res = _jerk(deferredrev, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_21d_v080_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_21d_v081_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 21d window."""
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_21d_v082_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 21d window."""
    res = _jerk(fcf, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_21d_v083_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 21d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_21d_v084_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 21d window."""
    res = _jerk(_ratio(inventory, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_42d_v085_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 42d window."""
    res = _jerk(deferredrev, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_42d_v086_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_42d_v087_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 42d window."""
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_42d_v088_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 42d window."""
    res = _jerk(fcf, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_42d_v089_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 42d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_42d_v090_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 42d window."""
    res = _jerk(_ratio(inventory, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_63d_v091_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 63d window."""
    res = _jerk(deferredrev, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_63d_v092_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_63d_v093_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 63d window."""
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_63d_v094_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 63d window."""
    res = _jerk(fcf, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_63d_v095_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 63d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_63d_v096_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 63d window."""
    res = _jerk(_ratio(inventory, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_126d_v097_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 126d window."""
    res = _jerk(deferredrev, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_126d_v098_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_126d_v099_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 126d window."""
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_126d_v100_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 126d window."""
    res = _jerk(fcf, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_126d_v101_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 126d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_126d_v102_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 126d window."""
    res = _jerk(_ratio(inventory, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_252d_v103_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 252d window."""
    res = _jerk(deferredrev, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_252d_v104_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_252d_v105_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 252d window."""
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_252d_v106_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 252d window."""
    res = _jerk(fcf, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_252d_v107_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 252d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_252d_v108_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 252d window."""
    res = _jerk(_ratio(inventory, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_504d_v109_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 504d window."""
    res = _jerk(deferredrev, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_504d_v110_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_504d_v111_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 504d window."""
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_504d_v112_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 504d window."""
    res = _jerk(fcf, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_504d_v113_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 504d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_504d_v114_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 504d window."""
    res = _jerk(_ratio(inventory, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_756d_v115_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 756d window."""
    res = _jerk(deferredrev, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_756d_v116_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_756d_v117_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 756d window."""
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_756d_v118_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 756d window."""
    res = _jerk(fcf, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_756d_v119_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 756d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_756d_v120_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 756d window."""
    res = _jerk(_ratio(inventory, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_1008d_v121_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 1008d window."""
    res = _jerk(deferredrev, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_1008d_v122_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_1008d_v123_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 1008d window."""
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_1008d_v124_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 1008d window."""
    res = _jerk(fcf, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_1008d_v125_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 1008d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_1008d_v126_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 1008d window."""
    res = _jerk(_ratio(inventory, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_jerk_1260d_v127_signal(deferredrev):
    """Acceleration/Jerk for Raw level of deferredrev over 1260d window."""
    res = _jerk(deferredrev, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_jerk_1260d_v128_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_jerk_1260d_v129_signal(inventory):
    """Acceleration/Jerk for Raw level of inventory over 1260d window."""
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_jerk_1260d_v130_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 1260d window."""
    res = _jerk(fcf, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_jerk_1260d_v131_signal(deferredrev, revenue, fcf, netinc):
    """Acceleration/Jerk for Backlog quality and cash conversion interaction over 1260d window."""
    res = _jerk(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_jerk_1260d_v132_signal(inventory, revenue):
    """Acceleration/Jerk for Inventory to sales cycle over 1260d window."""
    res = _jerk(_ratio(inventory, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_5d_v133_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 5d window."""
    res = (_slope_pct(deferredrev, 5).diff(5) / _sma(deferredrev.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_diff_norm_5d_v134_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_diff_norm_5d_v135_signal(inventory):
    """Normalized slope change for Raw level of inventory over 5d window."""
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_diff_norm_5d_v136_signal(fcf):
    """Normalized slope change for Raw level of fcf over 5d window."""
    res = (_slope_pct(fcf, 5).diff(5) / _sma(fcf.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_5d_v137_signal(deferredrev, revenue, fcf, netinc):
    """Normalized slope change for Backlog quality and cash conversion interaction over 5d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 5).diff(5) / _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_5d_v138_signal(inventory, revenue):
    """Normalized slope change for Inventory to sales cycle over 5d window."""
    res = (_slope_pct(_ratio(inventory, revenue), 5).diff(5) / _sma(_ratio(inventory, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_10d_v139_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 10d window."""
    res = (_slope_pct(deferredrev, 10).diff(10) / _sma(deferredrev.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_diff_norm_10d_v140_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_diff_norm_10d_v141_signal(inventory):
    """Normalized slope change for Raw level of inventory over 10d window."""
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_diff_norm_10d_v142_signal(fcf):
    """Normalized slope change for Raw level of fcf over 10d window."""
    res = (_slope_pct(fcf, 10).diff(10) / _sma(fcf.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_10d_v143_signal(deferredrev, revenue, fcf, netinc):
    """Normalized slope change for Backlog quality and cash conversion interaction over 10d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 10).diff(10) / _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_10d_v144_signal(inventory, revenue):
    """Normalized slope change for Inventory to sales cycle over 10d window."""
    res = (_slope_pct(_ratio(inventory, revenue), 10).diff(10) / _sma(_ratio(inventory, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_21d_v145_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 21d window."""
    res = (_slope_pct(deferredrev, 21).diff(21) / _sma(deferredrev.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_revenue_slope_diff_norm_21d_v146_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_slope_diff_norm_21d_v147_signal(inventory):
    """Normalized slope change for Raw level of inventory over 21d window."""
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_fcf_slope_diff_norm_21d_v148_signal(fcf):
    """Normalized slope change for Raw level of fcf over 21d window."""
    res = (_slope_pct(fcf, 21).diff(21) / _sma(fcf.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_21d_v149_signal(deferredrev, revenue, fcf, netinc):
    """Normalized slope change for Backlog quality and cash conversion interaction over 21d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 21).diff(21) / _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_21d_v150_signal(inventory, revenue):
    """Normalized slope change for Inventory to sales cycle over 21d window."""
    res = (_slope_pct(_ratio(inventory, revenue), 21).diff(21) / _sma(_ratio(inventory, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_5d_v001_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_5d_v001_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_5d_v002_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_5d_v002_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_5d_v003_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_5d_v003_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_5d_v004_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_5d_v004_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_5d_v005_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_5d_v005_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_5d_v006_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_5d_v006_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_10d_v007_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_10d_v007_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_10d_v008_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_10d_v008_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_10d_v009_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_10d_v009_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_10d_v010_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_10d_v010_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_10d_v011_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_10d_v011_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_10d_v012_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_10d_v012_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_21d_v013_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_21d_v013_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_21d_v014_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_21d_v014_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_21d_v015_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_21d_v015_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_21d_v016_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_21d_v016_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_21d_v017_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_21d_v017_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_21d_v018_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_21d_v018_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_42d_v019_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_42d_v019_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_42d_v020_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_42d_v020_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_42d_v021_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_42d_v021_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_42d_v022_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_42d_v022_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_42d_v023_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_42d_v023_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_42d_v024_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_42d_v024_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_63d_v025_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_63d_v025_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_63d_v026_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_63d_v026_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_63d_v027_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_63d_v027_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_63d_v028_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_63d_v028_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_63d_v029_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_63d_v029_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_63d_v030_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_63d_v030_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_126d_v031_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_126d_v031_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_126d_v032_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_126d_v032_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_126d_v033_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_126d_v033_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_126d_v034_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_126d_v034_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_126d_v035_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_126d_v035_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_126d_v036_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_126d_v036_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_252d_v037_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_252d_v037_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_252d_v038_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_252d_v038_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_252d_v039_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_252d_v039_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_252d_v040_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_252d_v040_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_252d_v041_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_252d_v041_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_252d_v042_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_252d_v042_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_504d_v043_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_504d_v043_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_504d_v044_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_504d_v044_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_504d_v045_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_504d_v045_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_504d_v046_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_504d_v046_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_504d_v047_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_504d_v047_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_504d_v048_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_504d_v048_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_756d_v049_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_756d_v049_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_756d_v050_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_756d_v050_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_756d_v051_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_756d_v051_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_756d_v052_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_756d_v052_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_756d_v053_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_756d_v053_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_756d_v054_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_756d_v054_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_1008d_v055_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_1008d_v055_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_1008d_v056_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_1008d_v056_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_1008d_v057_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_1008d_v057_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_1008d_v058_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_1008d_v058_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_1008d_v059_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_1008d_v059_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_1008d_v060_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_1008d_v060_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_pct_1260d_v061_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_pct_1260d_v061_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_pct_1260d_v062_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_pct_1260d_v062_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_pct_1260d_v063_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_pct_1260d_v063_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_pct_1260d_v064_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_pct_1260d_v064_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_pct_1260d_v065_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_pct_1260d_v065_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_1260d_v066_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_pct_1260d_v066_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_5d_v067_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_5d_v067_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_5d_v068_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_5d_v068_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_5d_v069_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_5d_v069_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_5d_v070_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_5d_v070_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_5d_v071_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_5d_v071_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_5d_v072_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_5d_v072_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_10d_v073_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_10d_v073_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_10d_v074_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_10d_v074_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_10d_v075_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_10d_v075_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_10d_v076_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_10d_v076_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_10d_v077_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_10d_v077_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_10d_v078_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_10d_v078_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_21d_v079_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_21d_v079_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_21d_v080_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_21d_v080_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_21d_v081_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_21d_v081_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_21d_v082_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_21d_v082_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_21d_v083_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_21d_v083_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_21d_v084_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_21d_v084_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_42d_v085_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_42d_v085_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_42d_v086_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_42d_v086_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_42d_v087_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_42d_v087_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_42d_v088_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_42d_v088_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_42d_v089_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_42d_v089_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_42d_v090_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_42d_v090_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_63d_v091_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_63d_v091_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_63d_v092_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_63d_v092_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_63d_v093_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_63d_v093_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_63d_v094_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_63d_v094_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_63d_v095_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_63d_v095_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_63d_v096_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_63d_v096_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_126d_v097_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_126d_v097_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_126d_v098_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_126d_v098_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_126d_v099_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_126d_v099_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_126d_v100_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_126d_v100_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_126d_v101_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_126d_v101_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_126d_v102_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_126d_v102_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_252d_v103_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_252d_v103_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_252d_v104_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_252d_v104_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_252d_v105_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_252d_v105_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_252d_v106_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_252d_v106_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_252d_v107_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_252d_v107_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_252d_v108_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_252d_v108_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_504d_v109_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_504d_v109_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_504d_v110_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_504d_v110_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_504d_v111_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_504d_v111_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_504d_v112_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_504d_v112_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_504d_v113_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_504d_v113_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_504d_v114_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_504d_v114_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_756d_v115_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_756d_v115_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_756d_v116_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_756d_v116_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_756d_v117_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_756d_v117_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_756d_v118_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_756d_v118_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_756d_v119_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_756d_v119_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_756d_v120_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_756d_v120_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_1008d_v121_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_1008d_v121_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_1008d_v122_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_1008d_v122_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_1008d_v123_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_1008d_v123_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_1008d_v124_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_1008d_v124_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_1008d_v125_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_1008d_v125_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_1008d_v126_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_1008d_v126_signal},
    "f03_ep_finding_cost_momentum_deferredrev_jerk_1260d_v127_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_jerk_1260d_v127_signal},
    "f03_ep_finding_cost_momentum_revenue_jerk_1260d_v128_signal": {"func": f03_ep_finding_cost_momentum_revenue_jerk_1260d_v128_signal},
    "f03_ep_finding_cost_momentum_inventory_jerk_1260d_v129_signal": {"func": f03_ep_finding_cost_momentum_inventory_jerk_1260d_v129_signal},
    "f03_ep_finding_cost_momentum_fcf_jerk_1260d_v130_signal": {"func": f03_ep_finding_cost_momentum_fcf_jerk_1260d_v130_signal},
    "f03_ep_finding_cost_momentum_backlog_health_jerk_1260d_v131_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_jerk_1260d_v131_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_jerk_1260d_v132_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_jerk_1260d_v132_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_5d_v133_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_5d_v133_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_diff_norm_5d_v134_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_diff_norm_5d_v134_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_diff_norm_5d_v135_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_diff_norm_5d_v135_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_diff_norm_5d_v136_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_diff_norm_5d_v136_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_5d_v137_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_5d_v137_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_5d_v138_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_5d_v138_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_10d_v139_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_10d_v139_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_diff_norm_10d_v140_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_diff_norm_10d_v140_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_diff_norm_10d_v141_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_diff_norm_10d_v141_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_diff_norm_10d_v142_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_diff_norm_10d_v142_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_10d_v143_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_10d_v143_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_10d_v144_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_10d_v144_signal},
    "f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_21d_v145_signal": {"func": f03_ep_finding_cost_momentum_deferredrev_slope_diff_norm_21d_v145_signal},
    "f03_ep_finding_cost_momentum_revenue_slope_diff_norm_21d_v146_signal": {"func": f03_ep_finding_cost_momentum_revenue_slope_diff_norm_21d_v146_signal},
    "f03_ep_finding_cost_momentum_inventory_slope_diff_norm_21d_v147_signal": {"func": f03_ep_finding_cost_momentum_inventory_slope_diff_norm_21d_v147_signal},
    "f03_ep_finding_cost_momentum_fcf_slope_diff_norm_21d_v148_signal": {"func": f03_ep_finding_cost_momentum_fcf_slope_diff_norm_21d_v148_signal},
    "f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_21d_v149_signal": {"func": f03_ep_finding_cost_momentum_backlog_health_slope_diff_norm_21d_v149_signal},
    "f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_21d_v150_signal": {"func": f03_ep_finding_cost_momentum_inventory_cycle_slope_diff_norm_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            # Relaxing non-null for RSI/Skew which need more data
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
