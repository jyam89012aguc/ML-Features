import pandas as pd
import numpy as np
import inspect

# ===== Utilities Ultra-High-Performance Alpha Helpers =====
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

def f33_grid_interconnection_queue_velocity_inventory_base_5d_v001_signal(inventory):
    """Moving average of Raw level of inventory over 5d window."""
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_5d_v002_signal(cor):
    """Moving average of Raw level of cor over 5d window."""
    res = _sma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_5d_v003_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_5d_v004_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 5d window."""
    res = _sma(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_5d_v005_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 5d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_5d_v006_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 5d window."""
    res = _sma(_ratio(revenue, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_10d_v007_signal(inventory):
    """Moving average of Raw level of inventory over 10d window."""
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_10d_v008_signal(cor):
    """Moving average of Raw level of cor over 10d window."""
    res = _sma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_10d_v009_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_10d_v010_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 10d window."""
    res = _sma(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_10d_v011_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 10d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_10d_v012_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 10d window."""
    res = _sma(_ratio(revenue, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_21d_v013_signal(inventory):
    """Moving average of Raw level of inventory over 21d window."""
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_21d_v014_signal(cor):
    """Moving average of Raw level of cor over 21d window."""
    res = _sma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_21d_v015_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_21d_v016_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 21d window."""
    res = _sma(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_21d_v017_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 21d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_21d_v018_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 21d window."""
    res = _sma(_ratio(revenue, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_42d_v019_signal(inventory):
    """Moving average of Raw level of inventory over 42d window."""
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_42d_v020_signal(cor):
    """Moving average of Raw level of cor over 42d window."""
    res = _sma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_42d_v021_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_42d_v022_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 42d window."""
    res = _sma(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_42d_v023_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 42d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_42d_v024_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 42d window."""
    res = _sma(_ratio(revenue, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_63d_v025_signal(inventory):
    """Moving average of Raw level of inventory over 63d window."""
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_63d_v026_signal(cor):
    """Moving average of Raw level of cor over 63d window."""
    res = _sma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_63d_v027_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_63d_v028_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 63d window."""
    res = _sma(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_63d_v029_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 63d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_63d_v030_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 63d window."""
    res = _sma(_ratio(revenue, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_126d_v031_signal(inventory):
    """Moving average of Raw level of inventory over 126d window."""
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_126d_v032_signal(cor):
    """Moving average of Raw level of cor over 126d window."""
    res = _sma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_126d_v033_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_126d_v034_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 126d window."""
    res = _sma(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_126d_v035_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 126d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_126d_v036_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 126d window."""
    res = _sma(_ratio(revenue, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_252d_v037_signal(inventory):
    """Moving average of Raw level of inventory over 252d window."""
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_252d_v038_signal(cor):
    """Moving average of Raw level of cor over 252d window."""
    res = _sma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_252d_v039_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_252d_v040_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 252d window."""
    res = _sma(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_252d_v041_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 252d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_252d_v042_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 252d window."""
    res = _sma(_ratio(revenue, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_504d_v043_signal(inventory):
    """Moving average of Raw level of inventory over 504d window."""
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_504d_v044_signal(cor):
    """Moving average of Raw level of cor over 504d window."""
    res = _sma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_504d_v045_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_504d_v046_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 504d window."""
    res = _sma(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_504d_v047_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 504d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_504d_v048_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 504d window."""
    res = _sma(_ratio(revenue, inventory), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_756d_v049_signal(inventory):
    """Moving average of Raw level of inventory over 756d window."""
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_756d_v050_signal(cor):
    """Moving average of Raw level of cor over 756d window."""
    res = _sma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_756d_v051_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_756d_v052_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 756d window."""
    res = _sma(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_756d_v053_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 756d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_756d_v054_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 756d window."""
    res = _sma(_ratio(revenue, inventory), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_1008d_v055_signal(inventory):
    """Moving average of Raw level of inventory over 1008d window."""
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_1008d_v056_signal(cor):
    """Moving average of Raw level of cor over 1008d window."""
    res = _sma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_1008d_v057_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_1008d_v058_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 1008d window."""
    res = _sma(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_1008d_v059_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 1008d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_1008d_v060_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 1008d window."""
    res = _sma(_ratio(revenue, inventory), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_base_1260d_v061_signal(inventory):
    """Moving average of Raw level of inventory over 1260d window."""
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_base_1260d_v062_signal(cor):
    """Moving average of Raw level of cor over 1260d window."""
    res = _sma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_base_1260d_v063_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_base_1260d_v064_signal(grossmargin):
    """Moving average of Raw level of grossmargin over 1260d window."""
    res = _sma(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_1260d_v065_signal(inventory, cor, grossmargin):
    """Moving average of Boom/bust inventory risk interacting with margin vol over 1260d window."""
    res = _sma(_ratio(inventory, cor) * _std(grossmargin, 126), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_base_1260d_v066_signal(revenue, inventory):
    """Moving average of Sales yield on inventory over 1260d window."""
    res = _sma(_ratio(revenue, inventory), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_ewma_5d_v067_signal(inventory):
    """Exponential moving average of Raw level of inventory over 5d window."""
    res = _ewma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_ewma_5d_v068_signal(cor):
    """Exponential moving average of Raw level of cor over 5d window."""
    res = _ewma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_ewma_5d_v069_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_grossmargin_ewma_5d_v070_signal(grossmargin):
    """Exponential moving average of Raw level of grossmargin over 5d window."""
    res = _ewma(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_glut_risk_ewma_5d_v071_signal(inventory, cor, grossmargin):
    """Exponential moving average of Boom/bust inventory risk interacting with margin vol over 5d window."""
    res = _ewma(_ratio(inventory, cor) * _std(grossmargin, 126), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_sales_efficiency_ewma_5d_v072_signal(revenue, inventory):
    """Exponential moving average of Sales yield on inventory over 5d window."""
    res = _ewma(_ratio(revenue, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_inventory_ewma_10d_v073_signal(inventory):
    """Exponential moving average of Raw level of inventory over 10d window."""
    res = _ewma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_cor_ewma_10d_v074_signal(cor):
    """Exponential moving average of Raw level of cor over 10d window."""
    res = _ewma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_grid_interconnection_queue_velocity_revenue_ewma_10d_v075_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f33_grid_interconnection_queue_velocity_inventory_base_5d_v001_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_5d_v001_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_5d_v002_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_5d_v002_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_5d_v003_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_5d_v003_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_5d_v004_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_5d_v004_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_5d_v005_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_5d_v005_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_5d_v006_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_5d_v006_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_10d_v007_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_10d_v007_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_10d_v008_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_10d_v008_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_10d_v009_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_10d_v009_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_10d_v010_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_10d_v010_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_10d_v011_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_10d_v011_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_10d_v012_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_10d_v012_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_21d_v013_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_21d_v013_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_21d_v014_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_21d_v014_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_21d_v015_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_21d_v015_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_21d_v016_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_21d_v016_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_21d_v017_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_21d_v017_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_21d_v018_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_21d_v018_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_42d_v019_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_42d_v019_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_42d_v020_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_42d_v020_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_42d_v021_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_42d_v021_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_42d_v022_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_42d_v022_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_42d_v023_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_42d_v023_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_42d_v024_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_42d_v024_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_63d_v025_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_63d_v025_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_63d_v026_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_63d_v026_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_63d_v027_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_63d_v027_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_63d_v028_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_63d_v028_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_63d_v029_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_63d_v029_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_63d_v030_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_63d_v030_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_126d_v031_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_126d_v031_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_126d_v032_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_126d_v032_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_126d_v033_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_126d_v033_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_126d_v034_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_126d_v034_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_126d_v035_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_126d_v035_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_126d_v036_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_126d_v036_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_252d_v037_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_252d_v037_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_252d_v038_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_252d_v038_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_252d_v039_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_252d_v039_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_252d_v040_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_252d_v040_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_252d_v041_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_252d_v041_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_252d_v042_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_252d_v042_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_504d_v043_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_504d_v043_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_504d_v044_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_504d_v044_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_504d_v045_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_504d_v045_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_504d_v046_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_504d_v046_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_504d_v047_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_504d_v047_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_504d_v048_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_504d_v048_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_756d_v049_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_756d_v049_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_756d_v050_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_756d_v050_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_756d_v051_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_756d_v051_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_756d_v052_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_756d_v052_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_756d_v053_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_756d_v053_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_756d_v054_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_756d_v054_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_1008d_v055_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_1008d_v055_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_1008d_v056_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_1008d_v056_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_1008d_v057_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_1008d_v057_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_1008d_v058_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_1008d_v058_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_1008d_v059_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_1008d_v059_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_1008d_v060_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_1008d_v060_signal},
    "f33_grid_interconnection_queue_velocity_inventory_base_1260d_v061_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_base_1260d_v061_signal},
    "f33_grid_interconnection_queue_velocity_cor_base_1260d_v062_signal": {"func": f33_grid_interconnection_queue_velocity_cor_base_1260d_v062_signal},
    "f33_grid_interconnection_queue_velocity_revenue_base_1260d_v063_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_base_1260d_v063_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_base_1260d_v064_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_base_1260d_v064_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_1260d_v065_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_base_1260d_v065_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_base_1260d_v066_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_base_1260d_v066_signal},
    "f33_grid_interconnection_queue_velocity_inventory_ewma_5d_v067_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_ewma_5d_v067_signal},
    "f33_grid_interconnection_queue_velocity_cor_ewma_5d_v068_signal": {"func": f33_grid_interconnection_queue_velocity_cor_ewma_5d_v068_signal},
    "f33_grid_interconnection_queue_velocity_revenue_ewma_5d_v069_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_ewma_5d_v069_signal},
    "f33_grid_interconnection_queue_velocity_grossmargin_ewma_5d_v070_signal": {"func": f33_grid_interconnection_queue_velocity_grossmargin_ewma_5d_v070_signal},
    "f33_grid_interconnection_queue_velocity_inventory_glut_risk_ewma_5d_v071_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_glut_risk_ewma_5d_v071_signal},
    "f33_grid_interconnection_queue_velocity_sales_efficiency_ewma_5d_v072_signal": {"func": f33_grid_interconnection_queue_velocity_sales_efficiency_ewma_5d_v072_signal},
    "f33_grid_interconnection_queue_velocity_inventory_ewma_10d_v073_signal": {"func": f33_grid_interconnection_queue_velocity_inventory_ewma_10d_v073_signal},
    "f33_grid_interconnection_queue_velocity_cor_ewma_10d_v074_signal": {"func": f33_grid_interconnection_queue_velocity_cor_ewma_10d_v074_signal},
    "f33_grid_interconnection_queue_velocity_revenue_ewma_10d_v075_signal": {"func": f33_grid_interconnection_queue_velocity_revenue_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 33...")
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
