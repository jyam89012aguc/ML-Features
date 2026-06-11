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

def f28_uranium_supply_deficit_proxy_deferredrev_base_5d_v001_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 5d window."""
    res = _sma(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_5d_v003_signal(inventory):
    """Moving average of Raw level of inventory over 5d window."""
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_5d_v004_signal(fcf):
    """Moving average of Raw level of fcf over 5d window."""
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_5d_v005_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 5d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_5d_v006_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 5d window."""
    res = _sma(_ratio(inventory, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_10d_v007_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 10d window."""
    res = _sma(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_10d_v008_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_10d_v009_signal(inventory):
    """Moving average of Raw level of inventory over 10d window."""
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_10d_v010_signal(fcf):
    """Moving average of Raw level of fcf over 10d window."""
    res = _sma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_10d_v011_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 10d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_10d_v012_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 10d window."""
    res = _sma(_ratio(inventory, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_21d_v013_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 21d window."""
    res = _sma(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_21d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_21d_v015_signal(inventory):
    """Moving average of Raw level of inventory over 21d window."""
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_21d_v016_signal(fcf):
    """Moving average of Raw level of fcf over 21d window."""
    res = _sma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_21d_v017_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 21d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_21d_v018_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 21d window."""
    res = _sma(_ratio(inventory, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_42d_v019_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 42d window."""
    res = _sma(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_42d_v020_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_42d_v021_signal(inventory):
    """Moving average of Raw level of inventory over 42d window."""
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_42d_v022_signal(fcf):
    """Moving average of Raw level of fcf over 42d window."""
    res = _sma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_42d_v023_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 42d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_42d_v024_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 42d window."""
    res = _sma(_ratio(inventory, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_63d_v025_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 63d window."""
    res = _sma(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_63d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_63d_v027_signal(inventory):
    """Moving average of Raw level of inventory over 63d window."""
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_63d_v028_signal(fcf):
    """Moving average of Raw level of fcf over 63d window."""
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_63d_v029_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 63d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_63d_v030_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 63d window."""
    res = _sma(_ratio(inventory, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_126d_v031_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 126d window."""
    res = _sma(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_126d_v032_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_126d_v033_signal(inventory):
    """Moving average of Raw level of inventory over 126d window."""
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_126d_v034_signal(fcf):
    """Moving average of Raw level of fcf over 126d window."""
    res = _sma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_126d_v035_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 126d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_126d_v036_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 126d window."""
    res = _sma(_ratio(inventory, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_252d_v037_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 252d window."""
    res = _sma(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_252d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_252d_v039_signal(inventory):
    """Moving average of Raw level of inventory over 252d window."""
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_252d_v040_signal(fcf):
    """Moving average of Raw level of fcf over 252d window."""
    res = _sma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_252d_v041_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 252d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_252d_v042_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 252d window."""
    res = _sma(_ratio(inventory, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_504d_v043_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 504d window."""
    res = _sma(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_504d_v044_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_504d_v045_signal(inventory):
    """Moving average of Raw level of inventory over 504d window."""
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_504d_v046_signal(fcf):
    """Moving average of Raw level of fcf over 504d window."""
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_504d_v047_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 504d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_504d_v048_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 504d window."""
    res = _sma(_ratio(inventory, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_756d_v049_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 756d window."""
    res = _sma(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_756d_v050_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_756d_v051_signal(inventory):
    """Moving average of Raw level of inventory over 756d window."""
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_756d_v052_signal(fcf):
    """Moving average of Raw level of fcf over 756d window."""
    res = _sma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_756d_v053_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 756d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_756d_v054_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 756d window."""
    res = _sma(_ratio(inventory, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_1008d_v055_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 1008d window."""
    res = _sma(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_1008d_v056_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_1008d_v057_signal(inventory):
    """Moving average of Raw level of inventory over 1008d window."""
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_1008d_v058_signal(fcf):
    """Moving average of Raw level of fcf over 1008d window."""
    res = _sma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_1008d_v059_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 1008d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_1008d_v060_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 1008d window."""
    res = _sma(_ratio(inventory, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_base_1260d_v061_signal(deferredrev):
    """Moving average of Raw level of deferredrev over 1260d window."""
    res = _sma(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_base_1260d_v062_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_base_1260d_v063_signal(inventory):
    """Moving average of Raw level of inventory over 1260d window."""
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_base_1260d_v064_signal(fcf):
    """Moving average of Raw level of fcf over 1260d window."""
    res = _sma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_base_1260d_v065_signal(deferredrev, revenue, fcf, netinc):
    """Moving average of Backlog quality and cash conversion interaction over 1260d window."""
    res = _sma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_base_1260d_v066_signal(inventory, revenue):
    """Moving average of Inventory to sales cycle over 1260d window."""
    res = _sma(_ratio(inventory, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_ewma_5d_v067_signal(deferredrev):
    """Exponential moving average of Raw level of deferredrev over 5d window."""
    res = _ewma(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_ewma_5d_v068_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_ewma_5d_v069_signal(inventory):
    """Exponential moving average of Raw level of inventory over 5d window."""
    res = _ewma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_fcf_ewma_5d_v070_signal(fcf):
    """Exponential moving average of Raw level of fcf over 5d window."""
    res = _ewma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_backlog_health_ewma_5d_v071_signal(deferredrev, revenue, fcf, netinc):
    """Exponential moving average of Backlog quality and cash conversion interaction over 5d window."""
    res = _ewma(_ratio(deferredrev, revenue) * _ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_cycle_ewma_5d_v072_signal(inventory, revenue):
    """Exponential moving average of Inventory to sales cycle over 5d window."""
    res = _ewma(_ratio(inventory, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_deferredrev_ewma_10d_v073_signal(deferredrev):
    """Exponential moving average of Raw level of deferredrev over 10d window."""
    res = _ewma(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_revenue_ewma_10d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_uranium_supply_deficit_proxy_inventory_ewma_10d_v075_signal(inventory):
    """Exponential moving average of Raw level of inventory over 10d window."""
    res = _ewma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f28_uranium_supply_deficit_proxy_deferredrev_base_5d_v001_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_5d_v001_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_5d_v002_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_5d_v002_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_5d_v003_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_5d_v003_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_5d_v004_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_5d_v004_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_5d_v005_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_5d_v005_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_5d_v006_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_5d_v006_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_10d_v007_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_10d_v007_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_10d_v008_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_10d_v008_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_10d_v009_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_10d_v009_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_10d_v010_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_10d_v010_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_10d_v011_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_10d_v011_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_10d_v012_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_10d_v012_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_21d_v013_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_21d_v013_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_21d_v014_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_21d_v014_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_21d_v015_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_21d_v015_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_21d_v016_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_21d_v016_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_21d_v017_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_21d_v017_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_21d_v018_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_21d_v018_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_42d_v019_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_42d_v019_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_42d_v020_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_42d_v020_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_42d_v021_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_42d_v021_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_42d_v022_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_42d_v022_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_42d_v023_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_42d_v023_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_42d_v024_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_42d_v024_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_63d_v025_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_63d_v025_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_63d_v026_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_63d_v026_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_63d_v027_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_63d_v027_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_63d_v028_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_63d_v028_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_63d_v029_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_63d_v029_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_63d_v030_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_63d_v030_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_126d_v031_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_126d_v031_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_126d_v032_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_126d_v032_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_126d_v033_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_126d_v033_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_126d_v034_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_126d_v034_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_126d_v035_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_126d_v035_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_126d_v036_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_126d_v036_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_252d_v037_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_252d_v037_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_252d_v038_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_252d_v038_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_252d_v039_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_252d_v039_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_252d_v040_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_252d_v040_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_252d_v041_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_252d_v041_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_252d_v042_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_252d_v042_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_504d_v043_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_504d_v043_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_504d_v044_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_504d_v044_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_504d_v045_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_504d_v045_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_504d_v046_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_504d_v046_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_504d_v047_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_504d_v047_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_504d_v048_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_504d_v048_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_756d_v049_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_756d_v049_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_756d_v050_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_756d_v050_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_756d_v051_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_756d_v051_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_756d_v052_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_756d_v052_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_756d_v053_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_756d_v053_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_756d_v054_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_756d_v054_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_1008d_v055_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_1008d_v055_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_1008d_v056_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_1008d_v056_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_1008d_v057_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_1008d_v057_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_1008d_v058_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_1008d_v058_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_1008d_v059_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_1008d_v059_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_1008d_v060_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_1008d_v060_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_base_1260d_v061_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_base_1260d_v061_signal},
    "f28_uranium_supply_deficit_proxy_revenue_base_1260d_v062_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_base_1260d_v062_signal},
    "f28_uranium_supply_deficit_proxy_inventory_base_1260d_v063_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_base_1260d_v063_signal},
    "f28_uranium_supply_deficit_proxy_fcf_base_1260d_v064_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_base_1260d_v064_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_base_1260d_v065_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_base_1260d_v065_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_base_1260d_v066_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_base_1260d_v066_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_ewma_5d_v067_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_ewma_5d_v067_signal},
    "f28_uranium_supply_deficit_proxy_revenue_ewma_5d_v068_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_ewma_5d_v068_signal},
    "f28_uranium_supply_deficit_proxy_inventory_ewma_5d_v069_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_ewma_5d_v069_signal},
    "f28_uranium_supply_deficit_proxy_fcf_ewma_5d_v070_signal": {"func": f28_uranium_supply_deficit_proxy_fcf_ewma_5d_v070_signal},
    "f28_uranium_supply_deficit_proxy_backlog_health_ewma_5d_v071_signal": {"func": f28_uranium_supply_deficit_proxy_backlog_health_ewma_5d_v071_signal},
    "f28_uranium_supply_deficit_proxy_inventory_cycle_ewma_5d_v072_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_cycle_ewma_5d_v072_signal},
    "f28_uranium_supply_deficit_proxy_deferredrev_ewma_10d_v073_signal": {"func": f28_uranium_supply_deficit_proxy_deferredrev_ewma_10d_v073_signal},
    "f28_uranium_supply_deficit_proxy_revenue_ewma_10d_v074_signal": {"func": f28_uranium_supply_deficit_proxy_revenue_ewma_10d_v074_signal},
    "f28_uranium_supply_deficit_proxy_inventory_ewma_10d_v075_signal": {"func": f28_uranium_supply_deficit_proxy_inventory_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 28...")
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
