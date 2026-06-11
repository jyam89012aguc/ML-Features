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

def f35_combined_slope_cor_base_5d_v001_signal(cor):
    """Moving average of Raw level of cor over 5d window."""
    res = _sma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_5d_v003_signal(sgna):
    """Moving average of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_5d_v004_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 5d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_10d_v005_signal(cor):
    """Moving average of Raw level of cor over 10d window."""
    res = _sma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_10d_v006_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_10d_v007_signal(sgna):
    """Moving average of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_10d_v008_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 10d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_21d_v009_signal(cor):
    """Moving average of Raw level of cor over 21d window."""
    res = _sma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_21d_v010_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_21d_v011_signal(sgna):
    """Moving average of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_21d_v012_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 21d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_42d_v013_signal(cor):
    """Moving average of Raw level of cor over 42d window."""
    res = _sma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_42d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_42d_v015_signal(sgna):
    """Moving average of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_42d_v016_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 42d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_63d_v017_signal(cor):
    """Moving average of Raw level of cor over 63d window."""
    res = _sma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_63d_v018_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_63d_v019_signal(sgna):
    """Moving average of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_63d_v020_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 63d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_126d_v021_signal(cor):
    """Moving average of Raw level of cor over 126d window."""
    res = _sma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_126d_v022_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_126d_v023_signal(sgna):
    """Moving average of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_126d_v024_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 126d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_252d_v025_signal(cor):
    """Moving average of Raw level of cor over 252d window."""
    res = _sma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_252d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_252d_v027_signal(sgna):
    """Moving average of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_252d_v028_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 252d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_504d_v029_signal(cor):
    """Moving average of Raw level of cor over 504d window."""
    res = _sma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_504d_v030_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_504d_v031_signal(sgna):
    """Moving average of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_504d_v032_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 504d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_756d_v033_signal(cor):
    """Moving average of Raw level of cor over 756d window."""
    res = _sma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_756d_v034_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_756d_v035_signal(sgna):
    """Moving average of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_756d_v036_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 756d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_1008d_v037_signal(cor):
    """Moving average of Raw level of cor over 1008d window."""
    res = _sma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_1008d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_1008d_v039_signal(sgna):
    """Moving average of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_1008d_v040_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 1008d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_base_1260d_v041_signal(cor):
    """Moving average of Raw level of cor over 1260d window."""
    res = _sma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_base_1260d_v042_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_base_1260d_v043_signal(sgna):
    """Moving average of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_base_1260d_v044_signal(cor, sgna, revenue):
    """Moving average of Total expense momentum over 1260d window."""
    res = _sma(_slope_pct(_ratio(cor + sgna, revenue), 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_5d_v045_signal(cor):
    """Exponential moving average of Raw level of cor over 5d window."""
    res = _ewma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_5d_v046_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_5d_v047_signal(sgna):
    """Exponential moving average of Raw level of sgna over 5d window."""
    res = _ewma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_5d_v048_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 5d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_10d_v049_signal(cor):
    """Exponential moving average of Raw level of cor over 10d window."""
    res = _ewma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_10d_v050_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_10d_v051_signal(sgna):
    """Exponential moving average of Raw level of sgna over 10d window."""
    res = _ewma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_10d_v052_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 10d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_21d_v053_signal(cor):
    """Exponential moving average of Raw level of cor over 21d window."""
    res = _ewma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_21d_v054_signal(revenue):
    """Exponential moving average of Raw level of revenue over 21d window."""
    res = _ewma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_21d_v055_signal(sgna):
    """Exponential moving average of Raw level of sgna over 21d window."""
    res = _ewma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_21d_v056_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 21d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_42d_v057_signal(cor):
    """Exponential moving average of Raw level of cor over 42d window."""
    res = _ewma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_42d_v058_signal(revenue):
    """Exponential moving average of Raw level of revenue over 42d window."""
    res = _ewma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_42d_v059_signal(sgna):
    """Exponential moving average of Raw level of sgna over 42d window."""
    res = _ewma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_42d_v060_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 42d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_63d_v061_signal(cor):
    """Exponential moving average of Raw level of cor over 63d window."""
    res = _ewma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_63d_v062_signal(revenue):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_63d_v063_signal(sgna):
    """Exponential moving average of Raw level of sgna over 63d window."""
    res = _ewma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_63d_v064_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 63d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_126d_v065_signal(cor):
    """Exponential moving average of Raw level of cor over 126d window."""
    res = _ewma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_126d_v066_signal(revenue):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_126d_v067_signal(sgna):
    """Exponential moving average of Raw level of sgna over 126d window."""
    res = _ewma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_126d_v068_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 126d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_252d_v069_signal(cor):
    """Exponential moving average of Raw level of cor over 252d window."""
    res = _ewma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_252d_v070_signal(revenue):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_252d_v071_signal(sgna):
    """Exponential moving average of Raw level of sgna over 252d window."""
    res = _ewma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_ewma_252d_v072_signal(cor, sgna, revenue):
    """Exponential moving average of Total expense momentum over 252d window."""
    res = _ewma(_slope_pct(_ratio(cor + sgna, revenue), 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_ewma_504d_v073_signal(cor):
    """Exponential moving average of Raw level of cor over 504d window."""
    res = _ewma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_ewma_504d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_ewma_504d_v075_signal(sgna):
    """Exponential moving average of Raw level of sgna over 504d window."""
    res = _ewma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f35_combined_slope_cor_base_5d_v001_signal": {"func": f35_combined_slope_cor_base_5d_v001_signal},
    "f35_combined_slope_revenue_base_5d_v002_signal": {"func": f35_combined_slope_revenue_base_5d_v002_signal},
    "f35_combined_slope_sgna_base_5d_v003_signal": {"func": f35_combined_slope_sgna_base_5d_v003_signal},
    "f35_combined_slope_expense_velocity_base_5d_v004_signal": {"func": f35_combined_slope_expense_velocity_base_5d_v004_signal},
    "f35_combined_slope_cor_base_10d_v005_signal": {"func": f35_combined_slope_cor_base_10d_v005_signal},
    "f35_combined_slope_revenue_base_10d_v006_signal": {"func": f35_combined_slope_revenue_base_10d_v006_signal},
    "f35_combined_slope_sgna_base_10d_v007_signal": {"func": f35_combined_slope_sgna_base_10d_v007_signal},
    "f35_combined_slope_expense_velocity_base_10d_v008_signal": {"func": f35_combined_slope_expense_velocity_base_10d_v008_signal},
    "f35_combined_slope_cor_base_21d_v009_signal": {"func": f35_combined_slope_cor_base_21d_v009_signal},
    "f35_combined_slope_revenue_base_21d_v010_signal": {"func": f35_combined_slope_revenue_base_21d_v010_signal},
    "f35_combined_slope_sgna_base_21d_v011_signal": {"func": f35_combined_slope_sgna_base_21d_v011_signal},
    "f35_combined_slope_expense_velocity_base_21d_v012_signal": {"func": f35_combined_slope_expense_velocity_base_21d_v012_signal},
    "f35_combined_slope_cor_base_42d_v013_signal": {"func": f35_combined_slope_cor_base_42d_v013_signal},
    "f35_combined_slope_revenue_base_42d_v014_signal": {"func": f35_combined_slope_revenue_base_42d_v014_signal},
    "f35_combined_slope_sgna_base_42d_v015_signal": {"func": f35_combined_slope_sgna_base_42d_v015_signal},
    "f35_combined_slope_expense_velocity_base_42d_v016_signal": {"func": f35_combined_slope_expense_velocity_base_42d_v016_signal},
    "f35_combined_slope_cor_base_63d_v017_signal": {"func": f35_combined_slope_cor_base_63d_v017_signal},
    "f35_combined_slope_revenue_base_63d_v018_signal": {"func": f35_combined_slope_revenue_base_63d_v018_signal},
    "f35_combined_slope_sgna_base_63d_v019_signal": {"func": f35_combined_slope_sgna_base_63d_v019_signal},
    "f35_combined_slope_expense_velocity_base_63d_v020_signal": {"func": f35_combined_slope_expense_velocity_base_63d_v020_signal},
    "f35_combined_slope_cor_base_126d_v021_signal": {"func": f35_combined_slope_cor_base_126d_v021_signal},
    "f35_combined_slope_revenue_base_126d_v022_signal": {"func": f35_combined_slope_revenue_base_126d_v022_signal},
    "f35_combined_slope_sgna_base_126d_v023_signal": {"func": f35_combined_slope_sgna_base_126d_v023_signal},
    "f35_combined_slope_expense_velocity_base_126d_v024_signal": {"func": f35_combined_slope_expense_velocity_base_126d_v024_signal},
    "f35_combined_slope_cor_base_252d_v025_signal": {"func": f35_combined_slope_cor_base_252d_v025_signal},
    "f35_combined_slope_revenue_base_252d_v026_signal": {"func": f35_combined_slope_revenue_base_252d_v026_signal},
    "f35_combined_slope_sgna_base_252d_v027_signal": {"func": f35_combined_slope_sgna_base_252d_v027_signal},
    "f35_combined_slope_expense_velocity_base_252d_v028_signal": {"func": f35_combined_slope_expense_velocity_base_252d_v028_signal},
    "f35_combined_slope_cor_base_504d_v029_signal": {"func": f35_combined_slope_cor_base_504d_v029_signal},
    "f35_combined_slope_revenue_base_504d_v030_signal": {"func": f35_combined_slope_revenue_base_504d_v030_signal},
    "f35_combined_slope_sgna_base_504d_v031_signal": {"func": f35_combined_slope_sgna_base_504d_v031_signal},
    "f35_combined_slope_expense_velocity_base_504d_v032_signal": {"func": f35_combined_slope_expense_velocity_base_504d_v032_signal},
    "f35_combined_slope_cor_base_756d_v033_signal": {"func": f35_combined_slope_cor_base_756d_v033_signal},
    "f35_combined_slope_revenue_base_756d_v034_signal": {"func": f35_combined_slope_revenue_base_756d_v034_signal},
    "f35_combined_slope_sgna_base_756d_v035_signal": {"func": f35_combined_slope_sgna_base_756d_v035_signal},
    "f35_combined_slope_expense_velocity_base_756d_v036_signal": {"func": f35_combined_slope_expense_velocity_base_756d_v036_signal},
    "f35_combined_slope_cor_base_1008d_v037_signal": {"func": f35_combined_slope_cor_base_1008d_v037_signal},
    "f35_combined_slope_revenue_base_1008d_v038_signal": {"func": f35_combined_slope_revenue_base_1008d_v038_signal},
    "f35_combined_slope_sgna_base_1008d_v039_signal": {"func": f35_combined_slope_sgna_base_1008d_v039_signal},
    "f35_combined_slope_expense_velocity_base_1008d_v040_signal": {"func": f35_combined_slope_expense_velocity_base_1008d_v040_signal},
    "f35_combined_slope_cor_base_1260d_v041_signal": {"func": f35_combined_slope_cor_base_1260d_v041_signal},
    "f35_combined_slope_revenue_base_1260d_v042_signal": {"func": f35_combined_slope_revenue_base_1260d_v042_signal},
    "f35_combined_slope_sgna_base_1260d_v043_signal": {"func": f35_combined_slope_sgna_base_1260d_v043_signal},
    "f35_combined_slope_expense_velocity_base_1260d_v044_signal": {"func": f35_combined_slope_expense_velocity_base_1260d_v044_signal},
    "f35_combined_slope_cor_ewma_5d_v045_signal": {"func": f35_combined_slope_cor_ewma_5d_v045_signal},
    "f35_combined_slope_revenue_ewma_5d_v046_signal": {"func": f35_combined_slope_revenue_ewma_5d_v046_signal},
    "f35_combined_slope_sgna_ewma_5d_v047_signal": {"func": f35_combined_slope_sgna_ewma_5d_v047_signal},
    "f35_combined_slope_expense_velocity_ewma_5d_v048_signal": {"func": f35_combined_slope_expense_velocity_ewma_5d_v048_signal},
    "f35_combined_slope_cor_ewma_10d_v049_signal": {"func": f35_combined_slope_cor_ewma_10d_v049_signal},
    "f35_combined_slope_revenue_ewma_10d_v050_signal": {"func": f35_combined_slope_revenue_ewma_10d_v050_signal},
    "f35_combined_slope_sgna_ewma_10d_v051_signal": {"func": f35_combined_slope_sgna_ewma_10d_v051_signal},
    "f35_combined_slope_expense_velocity_ewma_10d_v052_signal": {"func": f35_combined_slope_expense_velocity_ewma_10d_v052_signal},
    "f35_combined_slope_cor_ewma_21d_v053_signal": {"func": f35_combined_slope_cor_ewma_21d_v053_signal},
    "f35_combined_slope_revenue_ewma_21d_v054_signal": {"func": f35_combined_slope_revenue_ewma_21d_v054_signal},
    "f35_combined_slope_sgna_ewma_21d_v055_signal": {"func": f35_combined_slope_sgna_ewma_21d_v055_signal},
    "f35_combined_slope_expense_velocity_ewma_21d_v056_signal": {"func": f35_combined_slope_expense_velocity_ewma_21d_v056_signal},
    "f35_combined_slope_cor_ewma_42d_v057_signal": {"func": f35_combined_slope_cor_ewma_42d_v057_signal},
    "f35_combined_slope_revenue_ewma_42d_v058_signal": {"func": f35_combined_slope_revenue_ewma_42d_v058_signal},
    "f35_combined_slope_sgna_ewma_42d_v059_signal": {"func": f35_combined_slope_sgna_ewma_42d_v059_signal},
    "f35_combined_slope_expense_velocity_ewma_42d_v060_signal": {"func": f35_combined_slope_expense_velocity_ewma_42d_v060_signal},
    "f35_combined_slope_cor_ewma_63d_v061_signal": {"func": f35_combined_slope_cor_ewma_63d_v061_signal},
    "f35_combined_slope_revenue_ewma_63d_v062_signal": {"func": f35_combined_slope_revenue_ewma_63d_v062_signal},
    "f35_combined_slope_sgna_ewma_63d_v063_signal": {"func": f35_combined_slope_sgna_ewma_63d_v063_signal},
    "f35_combined_slope_expense_velocity_ewma_63d_v064_signal": {"func": f35_combined_slope_expense_velocity_ewma_63d_v064_signal},
    "f35_combined_slope_cor_ewma_126d_v065_signal": {"func": f35_combined_slope_cor_ewma_126d_v065_signal},
    "f35_combined_slope_revenue_ewma_126d_v066_signal": {"func": f35_combined_slope_revenue_ewma_126d_v066_signal},
    "f35_combined_slope_sgna_ewma_126d_v067_signal": {"func": f35_combined_slope_sgna_ewma_126d_v067_signal},
    "f35_combined_slope_expense_velocity_ewma_126d_v068_signal": {"func": f35_combined_slope_expense_velocity_ewma_126d_v068_signal},
    "f35_combined_slope_cor_ewma_252d_v069_signal": {"func": f35_combined_slope_cor_ewma_252d_v069_signal},
    "f35_combined_slope_revenue_ewma_252d_v070_signal": {"func": f35_combined_slope_revenue_ewma_252d_v070_signal},
    "f35_combined_slope_sgna_ewma_252d_v071_signal": {"func": f35_combined_slope_sgna_ewma_252d_v071_signal},
    "f35_combined_slope_expense_velocity_ewma_252d_v072_signal": {"func": f35_combined_slope_expense_velocity_ewma_252d_v072_signal},
    "f35_combined_slope_cor_ewma_504d_v073_signal": {"func": f35_combined_slope_cor_ewma_504d_v073_signal},
    "f35_combined_slope_revenue_ewma_504d_v074_signal": {"func": f35_combined_slope_revenue_ewma_504d_v074_signal},
    "f35_combined_slope_sgna_ewma_504d_v075_signal": {"func": f35_combined_slope_sgna_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 35...")
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
