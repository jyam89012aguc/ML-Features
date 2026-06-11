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

def f45_overhead_rational_sgna_base_5d_v001_signal(sgna):
    """Moving average of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_5d_v003_signal(ebit):
    """Moving average of Raw level of ebit over 5d window."""
    res = _sma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_5d_v004_signal(sgna):
    """Moving average of Annual SG&A change momentum over 5d window."""
    res = _sma(_slope_pct(sgna, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_10d_v005_signal(sgna):
    """Moving average of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_10d_v006_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_10d_v007_signal(ebit):
    """Moving average of Raw level of ebit over 10d window."""
    res = _sma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_10d_v008_signal(sgna):
    """Moving average of Annual SG&A change momentum over 10d window."""
    res = _sma(_slope_pct(sgna, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_21d_v009_signal(sgna):
    """Moving average of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_21d_v010_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_21d_v011_signal(ebit):
    """Moving average of Raw level of ebit over 21d window."""
    res = _sma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_21d_v012_signal(sgna):
    """Moving average of Annual SG&A change momentum over 21d window."""
    res = _sma(_slope_pct(sgna, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_42d_v013_signal(sgna):
    """Moving average of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_42d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_42d_v015_signal(ebit):
    """Moving average of Raw level of ebit over 42d window."""
    res = _sma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_42d_v016_signal(sgna):
    """Moving average of Annual SG&A change momentum over 42d window."""
    res = _sma(_slope_pct(sgna, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_63d_v017_signal(sgna):
    """Moving average of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_63d_v018_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_63d_v019_signal(ebit):
    """Moving average of Raw level of ebit over 63d window."""
    res = _sma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_63d_v020_signal(sgna):
    """Moving average of Annual SG&A change momentum over 63d window."""
    res = _sma(_slope_pct(sgna, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_126d_v021_signal(sgna):
    """Moving average of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_126d_v022_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_126d_v023_signal(ebit):
    """Moving average of Raw level of ebit over 126d window."""
    res = _sma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_126d_v024_signal(sgna):
    """Moving average of Annual SG&A change momentum over 126d window."""
    res = _sma(_slope_pct(sgna, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_252d_v025_signal(sgna):
    """Moving average of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_252d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_252d_v027_signal(ebit):
    """Moving average of Raw level of ebit over 252d window."""
    res = _sma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_252d_v028_signal(sgna):
    """Moving average of Annual SG&A change momentum over 252d window."""
    res = _sma(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_504d_v029_signal(sgna):
    """Moving average of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_504d_v030_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_504d_v031_signal(ebit):
    """Moving average of Raw level of ebit over 504d window."""
    res = _sma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_504d_v032_signal(sgna):
    """Moving average of Annual SG&A change momentum over 504d window."""
    res = _sma(_slope_pct(sgna, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_756d_v033_signal(sgna):
    """Moving average of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_756d_v034_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_756d_v035_signal(ebit):
    """Moving average of Raw level of ebit over 756d window."""
    res = _sma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_756d_v036_signal(sgna):
    """Moving average of Annual SG&A change momentum over 756d window."""
    res = _sma(_slope_pct(sgna, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_1008d_v037_signal(sgna):
    """Moving average of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_1008d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_1008d_v039_signal(ebit):
    """Moving average of Raw level of ebit over 1008d window."""
    res = _sma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_1008d_v040_signal(sgna):
    """Moving average of Annual SG&A change momentum over 1008d window."""
    res = _sma(_slope_pct(sgna, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_base_1260d_v041_signal(sgna):
    """Moving average of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_base_1260d_v042_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_base_1260d_v043_signal(ebit):
    """Moving average of Raw level of ebit over 1260d window."""
    res = _sma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_base_1260d_v044_signal(sgna):
    """Moving average of Annual SG&A change momentum over 1260d window."""
    res = _sma(_slope_pct(sgna, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_5d_v045_signal(sgna):
    """Exponential moving average of Raw level of sgna over 5d window."""
    res = _ewma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_5d_v046_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_5d_v047_signal(ebit):
    """Exponential moving average of Raw level of ebit over 5d window."""
    res = _ewma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_5d_v048_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 5d window."""
    res = _ewma(_slope_pct(sgna, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_10d_v049_signal(sgna):
    """Exponential moving average of Raw level of sgna over 10d window."""
    res = _ewma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_10d_v050_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_10d_v051_signal(ebit):
    """Exponential moving average of Raw level of ebit over 10d window."""
    res = _ewma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_10d_v052_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 10d window."""
    res = _ewma(_slope_pct(sgna, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_21d_v053_signal(sgna):
    """Exponential moving average of Raw level of sgna over 21d window."""
    res = _ewma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_21d_v054_signal(revenue):
    """Exponential moving average of Raw level of revenue over 21d window."""
    res = _ewma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_21d_v055_signal(ebit):
    """Exponential moving average of Raw level of ebit over 21d window."""
    res = _ewma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_21d_v056_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 21d window."""
    res = _ewma(_slope_pct(sgna, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_42d_v057_signal(sgna):
    """Exponential moving average of Raw level of sgna over 42d window."""
    res = _ewma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_42d_v058_signal(revenue):
    """Exponential moving average of Raw level of revenue over 42d window."""
    res = _ewma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_42d_v059_signal(ebit):
    """Exponential moving average of Raw level of ebit over 42d window."""
    res = _ewma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_42d_v060_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 42d window."""
    res = _ewma(_slope_pct(sgna, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_63d_v061_signal(sgna):
    """Exponential moving average of Raw level of sgna over 63d window."""
    res = _ewma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_63d_v062_signal(revenue):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_63d_v063_signal(ebit):
    """Exponential moving average of Raw level of ebit over 63d window."""
    res = _ewma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_63d_v064_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 63d window."""
    res = _ewma(_slope_pct(sgna, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_126d_v065_signal(sgna):
    """Exponential moving average of Raw level of sgna over 126d window."""
    res = _ewma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_126d_v066_signal(revenue):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_126d_v067_signal(ebit):
    """Exponential moving average of Raw level of ebit over 126d window."""
    res = _ewma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_126d_v068_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 126d window."""
    res = _ewma(_slope_pct(sgna, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_252d_v069_signal(sgna):
    """Exponential moving average of Raw level of sgna over 252d window."""
    res = _ewma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_252d_v070_signal(revenue):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_252d_v071_signal(ebit):
    """Exponential moving average of Raw level of ebit over 252d window."""
    res = _ewma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_252d_v072_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 252d window."""
    res = _ewma(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_504d_v073_signal(sgna):
    """Exponential moving average of Raw level of sgna over 504d window."""
    res = _ewma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_504d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_504d_v075_signal(ebit):
    """Exponential moving average of Raw level of ebit over 504d window."""
    res = _ewma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f45_overhead_rational_sgna_base_5d_v001_signal": {"func": f45_overhead_rational_sgna_base_5d_v001_signal},
    "f45_overhead_rational_revenue_base_5d_v002_signal": {"func": f45_overhead_rational_revenue_base_5d_v002_signal},
    "f45_overhead_rational_ebit_base_5d_v003_signal": {"func": f45_overhead_rational_ebit_base_5d_v003_signal},
    "f45_overhead_rational_sgna_momentum_base_5d_v004_signal": {"func": f45_overhead_rational_sgna_momentum_base_5d_v004_signal},
    "f45_overhead_rational_sgna_base_10d_v005_signal": {"func": f45_overhead_rational_sgna_base_10d_v005_signal},
    "f45_overhead_rational_revenue_base_10d_v006_signal": {"func": f45_overhead_rational_revenue_base_10d_v006_signal},
    "f45_overhead_rational_ebit_base_10d_v007_signal": {"func": f45_overhead_rational_ebit_base_10d_v007_signal},
    "f45_overhead_rational_sgna_momentum_base_10d_v008_signal": {"func": f45_overhead_rational_sgna_momentum_base_10d_v008_signal},
    "f45_overhead_rational_sgna_base_21d_v009_signal": {"func": f45_overhead_rational_sgna_base_21d_v009_signal},
    "f45_overhead_rational_revenue_base_21d_v010_signal": {"func": f45_overhead_rational_revenue_base_21d_v010_signal},
    "f45_overhead_rational_ebit_base_21d_v011_signal": {"func": f45_overhead_rational_ebit_base_21d_v011_signal},
    "f45_overhead_rational_sgna_momentum_base_21d_v012_signal": {"func": f45_overhead_rational_sgna_momentum_base_21d_v012_signal},
    "f45_overhead_rational_sgna_base_42d_v013_signal": {"func": f45_overhead_rational_sgna_base_42d_v013_signal},
    "f45_overhead_rational_revenue_base_42d_v014_signal": {"func": f45_overhead_rational_revenue_base_42d_v014_signal},
    "f45_overhead_rational_ebit_base_42d_v015_signal": {"func": f45_overhead_rational_ebit_base_42d_v015_signal},
    "f45_overhead_rational_sgna_momentum_base_42d_v016_signal": {"func": f45_overhead_rational_sgna_momentum_base_42d_v016_signal},
    "f45_overhead_rational_sgna_base_63d_v017_signal": {"func": f45_overhead_rational_sgna_base_63d_v017_signal},
    "f45_overhead_rational_revenue_base_63d_v018_signal": {"func": f45_overhead_rational_revenue_base_63d_v018_signal},
    "f45_overhead_rational_ebit_base_63d_v019_signal": {"func": f45_overhead_rational_ebit_base_63d_v019_signal},
    "f45_overhead_rational_sgna_momentum_base_63d_v020_signal": {"func": f45_overhead_rational_sgna_momentum_base_63d_v020_signal},
    "f45_overhead_rational_sgna_base_126d_v021_signal": {"func": f45_overhead_rational_sgna_base_126d_v021_signal},
    "f45_overhead_rational_revenue_base_126d_v022_signal": {"func": f45_overhead_rational_revenue_base_126d_v022_signal},
    "f45_overhead_rational_ebit_base_126d_v023_signal": {"func": f45_overhead_rational_ebit_base_126d_v023_signal},
    "f45_overhead_rational_sgna_momentum_base_126d_v024_signal": {"func": f45_overhead_rational_sgna_momentum_base_126d_v024_signal},
    "f45_overhead_rational_sgna_base_252d_v025_signal": {"func": f45_overhead_rational_sgna_base_252d_v025_signal},
    "f45_overhead_rational_revenue_base_252d_v026_signal": {"func": f45_overhead_rational_revenue_base_252d_v026_signal},
    "f45_overhead_rational_ebit_base_252d_v027_signal": {"func": f45_overhead_rational_ebit_base_252d_v027_signal},
    "f45_overhead_rational_sgna_momentum_base_252d_v028_signal": {"func": f45_overhead_rational_sgna_momentum_base_252d_v028_signal},
    "f45_overhead_rational_sgna_base_504d_v029_signal": {"func": f45_overhead_rational_sgna_base_504d_v029_signal},
    "f45_overhead_rational_revenue_base_504d_v030_signal": {"func": f45_overhead_rational_revenue_base_504d_v030_signal},
    "f45_overhead_rational_ebit_base_504d_v031_signal": {"func": f45_overhead_rational_ebit_base_504d_v031_signal},
    "f45_overhead_rational_sgna_momentum_base_504d_v032_signal": {"func": f45_overhead_rational_sgna_momentum_base_504d_v032_signal},
    "f45_overhead_rational_sgna_base_756d_v033_signal": {"func": f45_overhead_rational_sgna_base_756d_v033_signal},
    "f45_overhead_rational_revenue_base_756d_v034_signal": {"func": f45_overhead_rational_revenue_base_756d_v034_signal},
    "f45_overhead_rational_ebit_base_756d_v035_signal": {"func": f45_overhead_rational_ebit_base_756d_v035_signal},
    "f45_overhead_rational_sgna_momentum_base_756d_v036_signal": {"func": f45_overhead_rational_sgna_momentum_base_756d_v036_signal},
    "f45_overhead_rational_sgna_base_1008d_v037_signal": {"func": f45_overhead_rational_sgna_base_1008d_v037_signal},
    "f45_overhead_rational_revenue_base_1008d_v038_signal": {"func": f45_overhead_rational_revenue_base_1008d_v038_signal},
    "f45_overhead_rational_ebit_base_1008d_v039_signal": {"func": f45_overhead_rational_ebit_base_1008d_v039_signal},
    "f45_overhead_rational_sgna_momentum_base_1008d_v040_signal": {"func": f45_overhead_rational_sgna_momentum_base_1008d_v040_signal},
    "f45_overhead_rational_sgna_base_1260d_v041_signal": {"func": f45_overhead_rational_sgna_base_1260d_v041_signal},
    "f45_overhead_rational_revenue_base_1260d_v042_signal": {"func": f45_overhead_rational_revenue_base_1260d_v042_signal},
    "f45_overhead_rational_ebit_base_1260d_v043_signal": {"func": f45_overhead_rational_ebit_base_1260d_v043_signal},
    "f45_overhead_rational_sgna_momentum_base_1260d_v044_signal": {"func": f45_overhead_rational_sgna_momentum_base_1260d_v044_signal},
    "f45_overhead_rational_sgna_ewma_5d_v045_signal": {"func": f45_overhead_rational_sgna_ewma_5d_v045_signal},
    "f45_overhead_rational_revenue_ewma_5d_v046_signal": {"func": f45_overhead_rational_revenue_ewma_5d_v046_signal},
    "f45_overhead_rational_ebit_ewma_5d_v047_signal": {"func": f45_overhead_rational_ebit_ewma_5d_v047_signal},
    "f45_overhead_rational_sgna_momentum_ewma_5d_v048_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_5d_v048_signal},
    "f45_overhead_rational_sgna_ewma_10d_v049_signal": {"func": f45_overhead_rational_sgna_ewma_10d_v049_signal},
    "f45_overhead_rational_revenue_ewma_10d_v050_signal": {"func": f45_overhead_rational_revenue_ewma_10d_v050_signal},
    "f45_overhead_rational_ebit_ewma_10d_v051_signal": {"func": f45_overhead_rational_ebit_ewma_10d_v051_signal},
    "f45_overhead_rational_sgna_momentum_ewma_10d_v052_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_10d_v052_signal},
    "f45_overhead_rational_sgna_ewma_21d_v053_signal": {"func": f45_overhead_rational_sgna_ewma_21d_v053_signal},
    "f45_overhead_rational_revenue_ewma_21d_v054_signal": {"func": f45_overhead_rational_revenue_ewma_21d_v054_signal},
    "f45_overhead_rational_ebit_ewma_21d_v055_signal": {"func": f45_overhead_rational_ebit_ewma_21d_v055_signal},
    "f45_overhead_rational_sgna_momentum_ewma_21d_v056_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_21d_v056_signal},
    "f45_overhead_rational_sgna_ewma_42d_v057_signal": {"func": f45_overhead_rational_sgna_ewma_42d_v057_signal},
    "f45_overhead_rational_revenue_ewma_42d_v058_signal": {"func": f45_overhead_rational_revenue_ewma_42d_v058_signal},
    "f45_overhead_rational_ebit_ewma_42d_v059_signal": {"func": f45_overhead_rational_ebit_ewma_42d_v059_signal},
    "f45_overhead_rational_sgna_momentum_ewma_42d_v060_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_42d_v060_signal},
    "f45_overhead_rational_sgna_ewma_63d_v061_signal": {"func": f45_overhead_rational_sgna_ewma_63d_v061_signal},
    "f45_overhead_rational_revenue_ewma_63d_v062_signal": {"func": f45_overhead_rational_revenue_ewma_63d_v062_signal},
    "f45_overhead_rational_ebit_ewma_63d_v063_signal": {"func": f45_overhead_rational_ebit_ewma_63d_v063_signal},
    "f45_overhead_rational_sgna_momentum_ewma_63d_v064_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_63d_v064_signal},
    "f45_overhead_rational_sgna_ewma_126d_v065_signal": {"func": f45_overhead_rational_sgna_ewma_126d_v065_signal},
    "f45_overhead_rational_revenue_ewma_126d_v066_signal": {"func": f45_overhead_rational_revenue_ewma_126d_v066_signal},
    "f45_overhead_rational_ebit_ewma_126d_v067_signal": {"func": f45_overhead_rational_ebit_ewma_126d_v067_signal},
    "f45_overhead_rational_sgna_momentum_ewma_126d_v068_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_126d_v068_signal},
    "f45_overhead_rational_sgna_ewma_252d_v069_signal": {"func": f45_overhead_rational_sgna_ewma_252d_v069_signal},
    "f45_overhead_rational_revenue_ewma_252d_v070_signal": {"func": f45_overhead_rational_revenue_ewma_252d_v070_signal},
    "f45_overhead_rational_ebit_ewma_252d_v071_signal": {"func": f45_overhead_rational_ebit_ewma_252d_v071_signal},
    "f45_overhead_rational_sgna_momentum_ewma_252d_v072_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_252d_v072_signal},
    "f45_overhead_rational_sgna_ewma_504d_v073_signal": {"func": f45_overhead_rational_sgna_ewma_504d_v073_signal},
    "f45_overhead_rational_revenue_ewma_504d_v074_signal": {"func": f45_overhead_rational_revenue_ewma_504d_v074_signal},
    "f45_overhead_rational_ebit_ewma_504d_v075_signal": {"func": f45_overhead_rational_ebit_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 45...")
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
