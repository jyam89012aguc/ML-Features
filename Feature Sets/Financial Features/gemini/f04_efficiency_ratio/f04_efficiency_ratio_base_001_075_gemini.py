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

def f04_efficiency_ratio_sgna_base_5d_v001_signal(sgna):
    """Moving average of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_5d_v003_signal(ebitda):
    """Moving average of Raw level of ebitda over 5d window."""
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_5d_v004_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 5d window."""
    res = _sma(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_5d_v005_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 5d window."""
    res = _sma(_ratio(ebitda, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_5d_v006_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 5d window."""
    res = _sma(_ratio(ebitda, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_10d_v007_signal(sgna):
    """Moving average of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_10d_v008_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_10d_v009_signal(ebitda):
    """Moving average of Raw level of ebitda over 10d window."""
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_10d_v010_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 10d window."""
    res = _sma(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_10d_v011_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 10d window."""
    res = _sma(_ratio(ebitda, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_10d_v012_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 10d window."""
    res = _sma(_ratio(ebitda, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_21d_v013_signal(sgna):
    """Moving average of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_21d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_21d_v015_signal(ebitda):
    """Moving average of Raw level of ebitda over 21d window."""
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_21d_v016_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 21d window."""
    res = _sma(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_21d_v017_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 21d window."""
    res = _sma(_ratio(ebitda, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_21d_v018_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 21d window."""
    res = _sma(_ratio(ebitda, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_42d_v019_signal(sgna):
    """Moving average of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_42d_v020_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_42d_v021_signal(ebitda):
    """Moving average of Raw level of ebitda over 42d window."""
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_42d_v022_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 42d window."""
    res = _sma(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_42d_v023_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 42d window."""
    res = _sma(_ratio(ebitda, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_42d_v024_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 42d window."""
    res = _sma(_ratio(ebitda, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_63d_v025_signal(sgna):
    """Moving average of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_63d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_63d_v027_signal(ebitda):
    """Moving average of Raw level of ebitda over 63d window."""
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_63d_v028_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 63d window."""
    res = _sma(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_63d_v029_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 63d window."""
    res = _sma(_ratio(ebitda, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_63d_v030_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 63d window."""
    res = _sma(_ratio(ebitda, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_126d_v031_signal(sgna):
    """Moving average of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_126d_v032_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_126d_v033_signal(ebitda):
    """Moving average of Raw level of ebitda over 126d window."""
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_126d_v034_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 126d window."""
    res = _sma(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_126d_v035_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 126d window."""
    res = _sma(_ratio(ebitda, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_126d_v036_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 126d window."""
    res = _sma(_ratio(ebitda, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_252d_v037_signal(sgna):
    """Moving average of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_252d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_252d_v039_signal(ebitda):
    """Moving average of Raw level of ebitda over 252d window."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_252d_v040_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 252d window."""
    res = _sma(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_252d_v041_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 252d window."""
    res = _sma(_ratio(ebitda, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_252d_v042_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 252d window."""
    res = _sma(_ratio(ebitda, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_504d_v043_signal(sgna):
    """Moving average of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_504d_v044_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_504d_v045_signal(ebitda):
    """Moving average of Raw level of ebitda over 504d window."""
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_504d_v046_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 504d window."""
    res = _sma(_ratio(sgna, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_504d_v047_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 504d window."""
    res = _sma(_ratio(ebitda, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_504d_v048_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 504d window."""
    res = _sma(_ratio(ebitda, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_756d_v049_signal(sgna):
    """Moving average of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_756d_v050_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_756d_v051_signal(ebitda):
    """Moving average of Raw level of ebitda over 756d window."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_756d_v052_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 756d window."""
    res = _sma(_ratio(sgna, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_756d_v053_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 756d window."""
    res = _sma(_ratio(ebitda, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_756d_v054_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 756d window."""
    res = _sma(_ratio(ebitda, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_1008d_v055_signal(sgna):
    """Moving average of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_1008d_v056_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_1008d_v057_signal(ebitda):
    """Moving average of Raw level of ebitda over 1008d window."""
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_1008d_v058_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 1008d window."""
    res = _sma(_ratio(sgna, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_1008d_v059_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 1008d window."""
    res = _sma(_ratio(ebitda, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_1008d_v060_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 1008d window."""
    res = _sma(_ratio(ebitda, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_base_1260d_v061_signal(sgna):
    """Moving average of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_base_1260d_v062_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_base_1260d_v063_signal(ebitda):
    """Moving average of Raw level of ebitda over 1260d window."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_base_1260d_v064_signal(sgna, revenue):
    """Moving average of SG&A efficiency ratio over 1260d window."""
    res = _sma(_ratio(sgna, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_base_1260d_v065_signal(ebitda, revenue):
    """Moving average of EBITDA margin strength over 1260d window."""
    res = _sma(_ratio(ebitda, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_base_1260d_v066_signal(ebitda, sgna):
    """Moving average of Operating income per unit of overhead over 1260d window."""
    res = _sma(_ratio(ebitda, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_5d_v067_signal(sgna):
    """Exponential moving average of Raw level of sgna over 5d window."""
    res = _ewma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_5d_v068_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_5d_v069_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 5d window."""
    res = _ewma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_5d_v070_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 5d window."""
    res = _ewma(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_5d_v071_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 5d window."""
    res = _ewma(_ratio(ebitda, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_5d_v072_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 5d window."""
    res = _ewma(_ratio(ebitda, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_10d_v073_signal(sgna):
    """Exponential moving average of Raw level of sgna over 10d window."""
    res = _ewma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_10d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_10d_v075_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 10d window."""
    res = _ewma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f04_efficiency_ratio_sgna_base_5d_v001_signal": {"func": f04_efficiency_ratio_sgna_base_5d_v001_signal},
    "f04_efficiency_ratio_revenue_base_5d_v002_signal": {"func": f04_efficiency_ratio_revenue_base_5d_v002_signal},
    "f04_efficiency_ratio_ebitda_base_5d_v003_signal": {"func": f04_efficiency_ratio_ebitda_base_5d_v003_signal},
    "f04_efficiency_ratio_efficiency_score_base_5d_v004_signal": {"func": f04_efficiency_ratio_efficiency_score_base_5d_v004_signal},
    "f04_efficiency_ratio_ebitda_margin_base_5d_v005_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_5d_v005_signal},
    "f04_efficiency_ratio_overhead_yield_base_5d_v006_signal": {"func": f04_efficiency_ratio_overhead_yield_base_5d_v006_signal},
    "f04_efficiency_ratio_sgna_base_10d_v007_signal": {"func": f04_efficiency_ratio_sgna_base_10d_v007_signal},
    "f04_efficiency_ratio_revenue_base_10d_v008_signal": {"func": f04_efficiency_ratio_revenue_base_10d_v008_signal},
    "f04_efficiency_ratio_ebitda_base_10d_v009_signal": {"func": f04_efficiency_ratio_ebitda_base_10d_v009_signal},
    "f04_efficiency_ratio_efficiency_score_base_10d_v010_signal": {"func": f04_efficiency_ratio_efficiency_score_base_10d_v010_signal},
    "f04_efficiency_ratio_ebitda_margin_base_10d_v011_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_10d_v011_signal},
    "f04_efficiency_ratio_overhead_yield_base_10d_v012_signal": {"func": f04_efficiency_ratio_overhead_yield_base_10d_v012_signal},
    "f04_efficiency_ratio_sgna_base_21d_v013_signal": {"func": f04_efficiency_ratio_sgna_base_21d_v013_signal},
    "f04_efficiency_ratio_revenue_base_21d_v014_signal": {"func": f04_efficiency_ratio_revenue_base_21d_v014_signal},
    "f04_efficiency_ratio_ebitda_base_21d_v015_signal": {"func": f04_efficiency_ratio_ebitda_base_21d_v015_signal},
    "f04_efficiency_ratio_efficiency_score_base_21d_v016_signal": {"func": f04_efficiency_ratio_efficiency_score_base_21d_v016_signal},
    "f04_efficiency_ratio_ebitda_margin_base_21d_v017_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_21d_v017_signal},
    "f04_efficiency_ratio_overhead_yield_base_21d_v018_signal": {"func": f04_efficiency_ratio_overhead_yield_base_21d_v018_signal},
    "f04_efficiency_ratio_sgna_base_42d_v019_signal": {"func": f04_efficiency_ratio_sgna_base_42d_v019_signal},
    "f04_efficiency_ratio_revenue_base_42d_v020_signal": {"func": f04_efficiency_ratio_revenue_base_42d_v020_signal},
    "f04_efficiency_ratio_ebitda_base_42d_v021_signal": {"func": f04_efficiency_ratio_ebitda_base_42d_v021_signal},
    "f04_efficiency_ratio_efficiency_score_base_42d_v022_signal": {"func": f04_efficiency_ratio_efficiency_score_base_42d_v022_signal},
    "f04_efficiency_ratio_ebitda_margin_base_42d_v023_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_42d_v023_signal},
    "f04_efficiency_ratio_overhead_yield_base_42d_v024_signal": {"func": f04_efficiency_ratio_overhead_yield_base_42d_v024_signal},
    "f04_efficiency_ratio_sgna_base_63d_v025_signal": {"func": f04_efficiency_ratio_sgna_base_63d_v025_signal},
    "f04_efficiency_ratio_revenue_base_63d_v026_signal": {"func": f04_efficiency_ratio_revenue_base_63d_v026_signal},
    "f04_efficiency_ratio_ebitda_base_63d_v027_signal": {"func": f04_efficiency_ratio_ebitda_base_63d_v027_signal},
    "f04_efficiency_ratio_efficiency_score_base_63d_v028_signal": {"func": f04_efficiency_ratio_efficiency_score_base_63d_v028_signal},
    "f04_efficiency_ratio_ebitda_margin_base_63d_v029_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_63d_v029_signal},
    "f04_efficiency_ratio_overhead_yield_base_63d_v030_signal": {"func": f04_efficiency_ratio_overhead_yield_base_63d_v030_signal},
    "f04_efficiency_ratio_sgna_base_126d_v031_signal": {"func": f04_efficiency_ratio_sgna_base_126d_v031_signal},
    "f04_efficiency_ratio_revenue_base_126d_v032_signal": {"func": f04_efficiency_ratio_revenue_base_126d_v032_signal},
    "f04_efficiency_ratio_ebitda_base_126d_v033_signal": {"func": f04_efficiency_ratio_ebitda_base_126d_v033_signal},
    "f04_efficiency_ratio_efficiency_score_base_126d_v034_signal": {"func": f04_efficiency_ratio_efficiency_score_base_126d_v034_signal},
    "f04_efficiency_ratio_ebitda_margin_base_126d_v035_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_126d_v035_signal},
    "f04_efficiency_ratio_overhead_yield_base_126d_v036_signal": {"func": f04_efficiency_ratio_overhead_yield_base_126d_v036_signal},
    "f04_efficiency_ratio_sgna_base_252d_v037_signal": {"func": f04_efficiency_ratio_sgna_base_252d_v037_signal},
    "f04_efficiency_ratio_revenue_base_252d_v038_signal": {"func": f04_efficiency_ratio_revenue_base_252d_v038_signal},
    "f04_efficiency_ratio_ebitda_base_252d_v039_signal": {"func": f04_efficiency_ratio_ebitda_base_252d_v039_signal},
    "f04_efficiency_ratio_efficiency_score_base_252d_v040_signal": {"func": f04_efficiency_ratio_efficiency_score_base_252d_v040_signal},
    "f04_efficiency_ratio_ebitda_margin_base_252d_v041_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_252d_v041_signal},
    "f04_efficiency_ratio_overhead_yield_base_252d_v042_signal": {"func": f04_efficiency_ratio_overhead_yield_base_252d_v042_signal},
    "f04_efficiency_ratio_sgna_base_504d_v043_signal": {"func": f04_efficiency_ratio_sgna_base_504d_v043_signal},
    "f04_efficiency_ratio_revenue_base_504d_v044_signal": {"func": f04_efficiency_ratio_revenue_base_504d_v044_signal},
    "f04_efficiency_ratio_ebitda_base_504d_v045_signal": {"func": f04_efficiency_ratio_ebitda_base_504d_v045_signal},
    "f04_efficiency_ratio_efficiency_score_base_504d_v046_signal": {"func": f04_efficiency_ratio_efficiency_score_base_504d_v046_signal},
    "f04_efficiency_ratio_ebitda_margin_base_504d_v047_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_504d_v047_signal},
    "f04_efficiency_ratio_overhead_yield_base_504d_v048_signal": {"func": f04_efficiency_ratio_overhead_yield_base_504d_v048_signal},
    "f04_efficiency_ratio_sgna_base_756d_v049_signal": {"func": f04_efficiency_ratio_sgna_base_756d_v049_signal},
    "f04_efficiency_ratio_revenue_base_756d_v050_signal": {"func": f04_efficiency_ratio_revenue_base_756d_v050_signal},
    "f04_efficiency_ratio_ebitda_base_756d_v051_signal": {"func": f04_efficiency_ratio_ebitda_base_756d_v051_signal},
    "f04_efficiency_ratio_efficiency_score_base_756d_v052_signal": {"func": f04_efficiency_ratio_efficiency_score_base_756d_v052_signal},
    "f04_efficiency_ratio_ebitda_margin_base_756d_v053_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_756d_v053_signal},
    "f04_efficiency_ratio_overhead_yield_base_756d_v054_signal": {"func": f04_efficiency_ratio_overhead_yield_base_756d_v054_signal},
    "f04_efficiency_ratio_sgna_base_1008d_v055_signal": {"func": f04_efficiency_ratio_sgna_base_1008d_v055_signal},
    "f04_efficiency_ratio_revenue_base_1008d_v056_signal": {"func": f04_efficiency_ratio_revenue_base_1008d_v056_signal},
    "f04_efficiency_ratio_ebitda_base_1008d_v057_signal": {"func": f04_efficiency_ratio_ebitda_base_1008d_v057_signal},
    "f04_efficiency_ratio_efficiency_score_base_1008d_v058_signal": {"func": f04_efficiency_ratio_efficiency_score_base_1008d_v058_signal},
    "f04_efficiency_ratio_ebitda_margin_base_1008d_v059_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_1008d_v059_signal},
    "f04_efficiency_ratio_overhead_yield_base_1008d_v060_signal": {"func": f04_efficiency_ratio_overhead_yield_base_1008d_v060_signal},
    "f04_efficiency_ratio_sgna_base_1260d_v061_signal": {"func": f04_efficiency_ratio_sgna_base_1260d_v061_signal},
    "f04_efficiency_ratio_revenue_base_1260d_v062_signal": {"func": f04_efficiency_ratio_revenue_base_1260d_v062_signal},
    "f04_efficiency_ratio_ebitda_base_1260d_v063_signal": {"func": f04_efficiency_ratio_ebitda_base_1260d_v063_signal},
    "f04_efficiency_ratio_efficiency_score_base_1260d_v064_signal": {"func": f04_efficiency_ratio_efficiency_score_base_1260d_v064_signal},
    "f04_efficiency_ratio_ebitda_margin_base_1260d_v065_signal": {"func": f04_efficiency_ratio_ebitda_margin_base_1260d_v065_signal},
    "f04_efficiency_ratio_overhead_yield_base_1260d_v066_signal": {"func": f04_efficiency_ratio_overhead_yield_base_1260d_v066_signal},
    "f04_efficiency_ratio_sgna_ewma_5d_v067_signal": {"func": f04_efficiency_ratio_sgna_ewma_5d_v067_signal},
    "f04_efficiency_ratio_revenue_ewma_5d_v068_signal": {"func": f04_efficiency_ratio_revenue_ewma_5d_v068_signal},
    "f04_efficiency_ratio_ebitda_ewma_5d_v069_signal": {"func": f04_efficiency_ratio_ebitda_ewma_5d_v069_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_5d_v070_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_5d_v070_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_5d_v071_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_5d_v071_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_5d_v072_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_5d_v072_signal},
    "f04_efficiency_ratio_sgna_ewma_10d_v073_signal": {"func": f04_efficiency_ratio_sgna_ewma_10d_v073_signal},
    "f04_efficiency_ratio_revenue_ewma_10d_v074_signal": {"func": f04_efficiency_ratio_revenue_ewma_10d_v074_signal},
    "f04_efficiency_ratio_ebitda_ewma_10d_v075_signal": {"func": f04_efficiency_ratio_ebitda_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 04...")
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
