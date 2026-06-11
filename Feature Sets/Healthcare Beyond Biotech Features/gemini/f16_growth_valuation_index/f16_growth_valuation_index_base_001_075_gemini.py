import pandas as pd
import numpy as np
import inspect

# ===== Healthcare High-Performance Alpha Helpers =====
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

def f16_growth_valuation_index_sgna_base_5d_v001_signal(sgna):
    """Moving average of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_5d_v003_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_5d_v004_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 5d window."""
    res = _sma(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_10d_v005_signal(sgna):
    """Moving average of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_10d_v006_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_10d_v007_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_10d_v008_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 10d window."""
    res = _sma(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_21d_v009_signal(sgna):
    """Moving average of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_21d_v010_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_21d_v011_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_21d_v012_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 21d window."""
    res = _sma(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_42d_v013_signal(sgna):
    """Moving average of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_42d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_42d_v015_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_42d_v016_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 42d window."""
    res = _sma(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_63d_v017_signal(sgna):
    """Moving average of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_63d_v018_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_63d_v019_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_63d_v020_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 63d window."""
    res = _sma(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_126d_v021_signal(sgna):
    """Moving average of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_126d_v022_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_126d_v023_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_126d_v024_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 126d window."""
    res = _sma(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_252d_v025_signal(sgna):
    """Moving average of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_252d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_252d_v027_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_252d_v028_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 252d window."""
    res = _sma(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_504d_v029_signal(sgna):
    """Moving average of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_504d_v030_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_504d_v031_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_504d_v032_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 504d window."""
    res = _sma(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_756d_v033_signal(sgna):
    """Moving average of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_756d_v034_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_756d_v035_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_756d_v036_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 756d window."""
    res = _sma(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_1008d_v037_signal(sgna):
    """Moving average of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_1008d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_1008d_v039_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_1008d_v040_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 1008d window."""
    res = _sma(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_base_1260d_v041_signal(sgna):
    """Moving average of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_base_1260d_v042_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_base_1260d_v043_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_base_1260d_v044_signal(revenue, sgna):
    """Moving average of Revenue yield on sales spend over 1260d window."""
    res = _sma(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_5d_v045_signal(sgna):
    """Exponential moving average of Raw level of sgna over 5d window."""
    res = _ewma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_5d_v046_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_5d_v047_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_5d_v048_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 5d window."""
    res = _ewma(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_10d_v049_signal(sgna):
    """Exponential moving average of Raw level of sgna over 10d window."""
    res = _ewma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_10d_v050_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_10d_v051_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_10d_v052_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 10d window."""
    res = _ewma(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_21d_v053_signal(sgna):
    """Exponential moving average of Raw level of sgna over 21d window."""
    res = _ewma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_21d_v054_signal(revenue):
    """Exponential moving average of Raw level of revenue over 21d window."""
    res = _ewma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_21d_v055_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_21d_v056_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 21d window."""
    res = _ewma(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_42d_v057_signal(sgna):
    """Exponential moving average of Raw level of sgna over 42d window."""
    res = _ewma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_42d_v058_signal(revenue):
    """Exponential moving average of Raw level of revenue over 42d window."""
    res = _ewma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_42d_v059_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_42d_v060_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 42d window."""
    res = _ewma(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_63d_v061_signal(sgna):
    """Exponential moving average of Raw level of sgna over 63d window."""
    res = _ewma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_63d_v062_signal(revenue):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_63d_v063_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_63d_v064_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 63d window."""
    res = _ewma(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_126d_v065_signal(sgna):
    """Exponential moving average of Raw level of sgna over 126d window."""
    res = _ewma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_126d_v066_signal(revenue):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_126d_v067_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_126d_v068_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 126d window."""
    res = _ewma(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_252d_v069_signal(sgna):
    """Exponential moving average of Raw level of sgna over 252d window."""
    res = _ewma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_252d_v070_signal(revenue):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_252d_v071_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sales_efficiency_ewma_252d_v072_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 252d window."""
    res = _ewma(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_sgna_ewma_504d_v073_signal(sgna):
    """Exponential moving average of Raw level of sgna over 504d window."""
    res = _ewma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_revenue_ewma_504d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f16_growth_valuation_index_netinc_ewma_504d_v075_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f16_growth_valuation_index_sgna_base_5d_v001_signal": {"func": f16_growth_valuation_index_sgna_base_5d_v001_signal},
    "f16_growth_valuation_index_revenue_base_5d_v002_signal": {"func": f16_growth_valuation_index_revenue_base_5d_v002_signal},
    "f16_growth_valuation_index_netinc_base_5d_v003_signal": {"func": f16_growth_valuation_index_netinc_base_5d_v003_signal},
    "f16_growth_valuation_index_sales_efficiency_base_5d_v004_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_5d_v004_signal},
    "f16_growth_valuation_index_sgna_base_10d_v005_signal": {"func": f16_growth_valuation_index_sgna_base_10d_v005_signal},
    "f16_growth_valuation_index_revenue_base_10d_v006_signal": {"func": f16_growth_valuation_index_revenue_base_10d_v006_signal},
    "f16_growth_valuation_index_netinc_base_10d_v007_signal": {"func": f16_growth_valuation_index_netinc_base_10d_v007_signal},
    "f16_growth_valuation_index_sales_efficiency_base_10d_v008_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_10d_v008_signal},
    "f16_growth_valuation_index_sgna_base_21d_v009_signal": {"func": f16_growth_valuation_index_sgna_base_21d_v009_signal},
    "f16_growth_valuation_index_revenue_base_21d_v010_signal": {"func": f16_growth_valuation_index_revenue_base_21d_v010_signal},
    "f16_growth_valuation_index_netinc_base_21d_v011_signal": {"func": f16_growth_valuation_index_netinc_base_21d_v011_signal},
    "f16_growth_valuation_index_sales_efficiency_base_21d_v012_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_21d_v012_signal},
    "f16_growth_valuation_index_sgna_base_42d_v013_signal": {"func": f16_growth_valuation_index_sgna_base_42d_v013_signal},
    "f16_growth_valuation_index_revenue_base_42d_v014_signal": {"func": f16_growth_valuation_index_revenue_base_42d_v014_signal},
    "f16_growth_valuation_index_netinc_base_42d_v015_signal": {"func": f16_growth_valuation_index_netinc_base_42d_v015_signal},
    "f16_growth_valuation_index_sales_efficiency_base_42d_v016_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_42d_v016_signal},
    "f16_growth_valuation_index_sgna_base_63d_v017_signal": {"func": f16_growth_valuation_index_sgna_base_63d_v017_signal},
    "f16_growth_valuation_index_revenue_base_63d_v018_signal": {"func": f16_growth_valuation_index_revenue_base_63d_v018_signal},
    "f16_growth_valuation_index_netinc_base_63d_v019_signal": {"func": f16_growth_valuation_index_netinc_base_63d_v019_signal},
    "f16_growth_valuation_index_sales_efficiency_base_63d_v020_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_63d_v020_signal},
    "f16_growth_valuation_index_sgna_base_126d_v021_signal": {"func": f16_growth_valuation_index_sgna_base_126d_v021_signal},
    "f16_growth_valuation_index_revenue_base_126d_v022_signal": {"func": f16_growth_valuation_index_revenue_base_126d_v022_signal},
    "f16_growth_valuation_index_netinc_base_126d_v023_signal": {"func": f16_growth_valuation_index_netinc_base_126d_v023_signal},
    "f16_growth_valuation_index_sales_efficiency_base_126d_v024_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_126d_v024_signal},
    "f16_growth_valuation_index_sgna_base_252d_v025_signal": {"func": f16_growth_valuation_index_sgna_base_252d_v025_signal},
    "f16_growth_valuation_index_revenue_base_252d_v026_signal": {"func": f16_growth_valuation_index_revenue_base_252d_v026_signal},
    "f16_growth_valuation_index_netinc_base_252d_v027_signal": {"func": f16_growth_valuation_index_netinc_base_252d_v027_signal},
    "f16_growth_valuation_index_sales_efficiency_base_252d_v028_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_252d_v028_signal},
    "f16_growth_valuation_index_sgna_base_504d_v029_signal": {"func": f16_growth_valuation_index_sgna_base_504d_v029_signal},
    "f16_growth_valuation_index_revenue_base_504d_v030_signal": {"func": f16_growth_valuation_index_revenue_base_504d_v030_signal},
    "f16_growth_valuation_index_netinc_base_504d_v031_signal": {"func": f16_growth_valuation_index_netinc_base_504d_v031_signal},
    "f16_growth_valuation_index_sales_efficiency_base_504d_v032_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_504d_v032_signal},
    "f16_growth_valuation_index_sgna_base_756d_v033_signal": {"func": f16_growth_valuation_index_sgna_base_756d_v033_signal},
    "f16_growth_valuation_index_revenue_base_756d_v034_signal": {"func": f16_growth_valuation_index_revenue_base_756d_v034_signal},
    "f16_growth_valuation_index_netinc_base_756d_v035_signal": {"func": f16_growth_valuation_index_netinc_base_756d_v035_signal},
    "f16_growth_valuation_index_sales_efficiency_base_756d_v036_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_756d_v036_signal},
    "f16_growth_valuation_index_sgna_base_1008d_v037_signal": {"func": f16_growth_valuation_index_sgna_base_1008d_v037_signal},
    "f16_growth_valuation_index_revenue_base_1008d_v038_signal": {"func": f16_growth_valuation_index_revenue_base_1008d_v038_signal},
    "f16_growth_valuation_index_netinc_base_1008d_v039_signal": {"func": f16_growth_valuation_index_netinc_base_1008d_v039_signal},
    "f16_growth_valuation_index_sales_efficiency_base_1008d_v040_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_1008d_v040_signal},
    "f16_growth_valuation_index_sgna_base_1260d_v041_signal": {"func": f16_growth_valuation_index_sgna_base_1260d_v041_signal},
    "f16_growth_valuation_index_revenue_base_1260d_v042_signal": {"func": f16_growth_valuation_index_revenue_base_1260d_v042_signal},
    "f16_growth_valuation_index_netinc_base_1260d_v043_signal": {"func": f16_growth_valuation_index_netinc_base_1260d_v043_signal},
    "f16_growth_valuation_index_sales_efficiency_base_1260d_v044_signal": {"func": f16_growth_valuation_index_sales_efficiency_base_1260d_v044_signal},
    "f16_growth_valuation_index_sgna_ewma_5d_v045_signal": {"func": f16_growth_valuation_index_sgna_ewma_5d_v045_signal},
    "f16_growth_valuation_index_revenue_ewma_5d_v046_signal": {"func": f16_growth_valuation_index_revenue_ewma_5d_v046_signal},
    "f16_growth_valuation_index_netinc_ewma_5d_v047_signal": {"func": f16_growth_valuation_index_netinc_ewma_5d_v047_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_5d_v048_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_5d_v048_signal},
    "f16_growth_valuation_index_sgna_ewma_10d_v049_signal": {"func": f16_growth_valuation_index_sgna_ewma_10d_v049_signal},
    "f16_growth_valuation_index_revenue_ewma_10d_v050_signal": {"func": f16_growth_valuation_index_revenue_ewma_10d_v050_signal},
    "f16_growth_valuation_index_netinc_ewma_10d_v051_signal": {"func": f16_growth_valuation_index_netinc_ewma_10d_v051_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_10d_v052_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_10d_v052_signal},
    "f16_growth_valuation_index_sgna_ewma_21d_v053_signal": {"func": f16_growth_valuation_index_sgna_ewma_21d_v053_signal},
    "f16_growth_valuation_index_revenue_ewma_21d_v054_signal": {"func": f16_growth_valuation_index_revenue_ewma_21d_v054_signal},
    "f16_growth_valuation_index_netinc_ewma_21d_v055_signal": {"func": f16_growth_valuation_index_netinc_ewma_21d_v055_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_21d_v056_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_21d_v056_signal},
    "f16_growth_valuation_index_sgna_ewma_42d_v057_signal": {"func": f16_growth_valuation_index_sgna_ewma_42d_v057_signal},
    "f16_growth_valuation_index_revenue_ewma_42d_v058_signal": {"func": f16_growth_valuation_index_revenue_ewma_42d_v058_signal},
    "f16_growth_valuation_index_netinc_ewma_42d_v059_signal": {"func": f16_growth_valuation_index_netinc_ewma_42d_v059_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_42d_v060_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_42d_v060_signal},
    "f16_growth_valuation_index_sgna_ewma_63d_v061_signal": {"func": f16_growth_valuation_index_sgna_ewma_63d_v061_signal},
    "f16_growth_valuation_index_revenue_ewma_63d_v062_signal": {"func": f16_growth_valuation_index_revenue_ewma_63d_v062_signal},
    "f16_growth_valuation_index_netinc_ewma_63d_v063_signal": {"func": f16_growth_valuation_index_netinc_ewma_63d_v063_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_63d_v064_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_63d_v064_signal},
    "f16_growth_valuation_index_sgna_ewma_126d_v065_signal": {"func": f16_growth_valuation_index_sgna_ewma_126d_v065_signal},
    "f16_growth_valuation_index_revenue_ewma_126d_v066_signal": {"func": f16_growth_valuation_index_revenue_ewma_126d_v066_signal},
    "f16_growth_valuation_index_netinc_ewma_126d_v067_signal": {"func": f16_growth_valuation_index_netinc_ewma_126d_v067_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_126d_v068_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_126d_v068_signal},
    "f16_growth_valuation_index_sgna_ewma_252d_v069_signal": {"func": f16_growth_valuation_index_sgna_ewma_252d_v069_signal},
    "f16_growth_valuation_index_revenue_ewma_252d_v070_signal": {"func": f16_growth_valuation_index_revenue_ewma_252d_v070_signal},
    "f16_growth_valuation_index_netinc_ewma_252d_v071_signal": {"func": f16_growth_valuation_index_netinc_ewma_252d_v071_signal},
    "f16_growth_valuation_index_sales_efficiency_ewma_252d_v072_signal": {"func": f16_growth_valuation_index_sales_efficiency_ewma_252d_v072_signal},
    "f16_growth_valuation_index_sgna_ewma_504d_v073_signal": {"func": f16_growth_valuation_index_sgna_ewma_504d_v073_signal},
    "f16_growth_valuation_index_revenue_ewma_504d_v074_signal": {"func": f16_growth_valuation_index_revenue_ewma_504d_v074_signal},
    "f16_growth_valuation_index_netinc_ewma_504d_v075_signal": {"func": f16_growth_valuation_index_netinc_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "sbcomp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 16...")
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
