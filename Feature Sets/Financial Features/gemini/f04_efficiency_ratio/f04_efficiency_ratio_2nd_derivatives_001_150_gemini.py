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

def f04_efficiency_ratio_sgna_slope_pct_5d_v001_signal(sgna):
    """Percentage slope for Raw level of sgna over 5d window."""
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_5d_v003_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 5d window."""
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_5d_v004_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 5d window."""
    res = _slope_pct(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_5d_v005_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 5d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_5d_v006_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 5d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_10d_v007_signal(sgna):
    """Percentage slope for Raw level of sgna over 10d window."""
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_10d_v008_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_10d_v009_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 10d window."""
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_10d_v010_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 10d window."""
    res = _slope_pct(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_10d_v011_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 10d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_10d_v012_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 10d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_21d_v013_signal(sgna):
    """Percentage slope for Raw level of sgna over 21d window."""
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_21d_v014_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_21d_v015_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 21d window."""
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_21d_v016_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 21d window."""
    res = _slope_pct(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_21d_v017_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 21d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_21d_v018_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 21d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_42d_v019_signal(sgna):
    """Percentage slope for Raw level of sgna over 42d window."""
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_42d_v020_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_42d_v021_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 42d window."""
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_42d_v022_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 42d window."""
    res = _slope_pct(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_42d_v023_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 42d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_42d_v024_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 42d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_63d_v025_signal(sgna):
    """Percentage slope for Raw level of sgna over 63d window."""
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_63d_v026_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_63d_v027_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 63d window."""
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_63d_v028_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 63d window."""
    res = _slope_pct(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_63d_v029_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 63d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_63d_v030_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 63d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_126d_v031_signal(sgna):
    """Percentage slope for Raw level of sgna over 126d window."""
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_126d_v032_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_126d_v033_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 126d window."""
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_126d_v034_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 126d window."""
    res = _slope_pct(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_126d_v035_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 126d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_126d_v036_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 126d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_252d_v037_signal(sgna):
    """Percentage slope for Raw level of sgna over 252d window."""
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_252d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_252d_v039_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 252d window."""
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_252d_v040_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 252d window."""
    res = _slope_pct(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_252d_v041_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 252d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_252d_v042_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 252d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_504d_v043_signal(sgna):
    """Percentage slope for Raw level of sgna over 504d window."""
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_504d_v044_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_504d_v045_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 504d window."""
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_504d_v046_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 504d window."""
    res = _slope_pct(_ratio(sgna, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_504d_v047_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 504d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_504d_v048_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 504d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_756d_v049_signal(sgna):
    """Percentage slope for Raw level of sgna over 756d window."""
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_756d_v050_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_756d_v051_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 756d window."""
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_756d_v052_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 756d window."""
    res = _slope_pct(_ratio(sgna, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_756d_v053_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 756d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_756d_v054_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 756d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_1008d_v055_signal(sgna):
    """Percentage slope for Raw level of sgna over 1008d window."""
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_1008d_v056_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_1008d_v057_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1008d window."""
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_1008d_v058_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 1008d window."""
    res = _slope_pct(_ratio(sgna, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_1008d_v059_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 1008d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_1008d_v060_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 1008d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_pct_1260d_v061_signal(sgna):
    """Percentage slope for Raw level of sgna over 1260d window."""
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_pct_1260d_v062_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_pct_1260d_v063_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1260d window."""
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_pct_1260d_v064_signal(sgna, revenue):
    """Percentage slope for SG&A efficiency ratio over 1260d window."""
    res = _slope_pct(_ratio(sgna, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_pct_1260d_v065_signal(ebitda, revenue):
    """Percentage slope for EBITDA margin strength over 1260d window."""
    res = _slope_pct(_ratio(ebitda, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_pct_1260d_v066_signal(ebitda, sgna):
    """Percentage slope for Operating income per unit of overhead over 1260d window."""
    res = _slope_pct(_ratio(ebitda, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_5d_v067_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 5d window."""
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_5d_v068_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_5d_v069_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 5d window."""
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_5d_v070_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 5d window."""
    res = _jerk(_ratio(sgna, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_5d_v071_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 5d window."""
    res = _jerk(_ratio(ebitda, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_5d_v072_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 5d window."""
    res = _jerk(_ratio(ebitda, sgna), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_10d_v073_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 10d window."""
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_10d_v074_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_10d_v075_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 10d window."""
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_10d_v076_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 10d window."""
    res = _jerk(_ratio(sgna, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_10d_v077_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 10d window."""
    res = _jerk(_ratio(ebitda, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_10d_v078_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 10d window."""
    res = _jerk(_ratio(ebitda, sgna), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_21d_v079_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 21d window."""
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_21d_v080_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_21d_v081_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 21d window."""
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_21d_v082_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 21d window."""
    res = _jerk(_ratio(sgna, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_21d_v083_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 21d window."""
    res = _jerk(_ratio(ebitda, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_21d_v084_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 21d window."""
    res = _jerk(_ratio(ebitda, sgna), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_42d_v085_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 42d window."""
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_42d_v086_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_42d_v087_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 42d window."""
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_42d_v088_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 42d window."""
    res = _jerk(_ratio(sgna, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_42d_v089_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 42d window."""
    res = _jerk(_ratio(ebitda, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_42d_v090_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 42d window."""
    res = _jerk(_ratio(ebitda, sgna), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_63d_v091_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 63d window."""
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_63d_v092_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_63d_v093_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 63d window."""
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_63d_v094_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 63d window."""
    res = _jerk(_ratio(sgna, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_63d_v095_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 63d window."""
    res = _jerk(_ratio(ebitda, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_63d_v096_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 63d window."""
    res = _jerk(_ratio(ebitda, sgna), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_126d_v097_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 126d window."""
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_126d_v098_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_126d_v099_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 126d window."""
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_126d_v100_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 126d window."""
    res = _jerk(_ratio(sgna, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_126d_v101_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 126d window."""
    res = _jerk(_ratio(ebitda, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_126d_v102_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 126d window."""
    res = _jerk(_ratio(ebitda, sgna), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_252d_v103_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 252d window."""
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_252d_v104_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_252d_v105_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 252d window."""
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_252d_v106_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 252d window."""
    res = _jerk(_ratio(sgna, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_252d_v107_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 252d window."""
    res = _jerk(_ratio(ebitda, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_252d_v108_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 252d window."""
    res = _jerk(_ratio(ebitda, sgna), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_504d_v109_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 504d window."""
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_504d_v110_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_504d_v111_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 504d window."""
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_504d_v112_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 504d window."""
    res = _jerk(_ratio(sgna, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_504d_v113_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 504d window."""
    res = _jerk(_ratio(ebitda, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_504d_v114_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 504d window."""
    res = _jerk(_ratio(ebitda, sgna), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_756d_v115_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 756d window."""
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_756d_v116_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_756d_v117_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 756d window."""
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_756d_v118_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 756d window."""
    res = _jerk(_ratio(sgna, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_756d_v119_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 756d window."""
    res = _jerk(_ratio(ebitda, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_756d_v120_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 756d window."""
    res = _jerk(_ratio(ebitda, sgna), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_1008d_v121_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1008d window."""
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_1008d_v122_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_1008d_v123_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1008d window."""
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_1008d_v124_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 1008d window."""
    res = _jerk(_ratio(sgna, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_1008d_v125_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 1008d window."""
    res = _jerk(_ratio(ebitda, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_1008d_v126_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 1008d window."""
    res = _jerk(_ratio(ebitda, sgna), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_jerk_1260d_v127_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1260d window."""
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_jerk_1260d_v128_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_jerk_1260d_v129_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1260d window."""
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_jerk_1260d_v130_signal(sgna, revenue):
    """Acceleration/Jerk for SG&A efficiency ratio over 1260d window."""
    res = _jerk(_ratio(sgna, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_jerk_1260d_v131_signal(ebitda, revenue):
    """Acceleration/Jerk for EBITDA margin strength over 1260d window."""
    res = _jerk(_ratio(ebitda, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_jerk_1260d_v132_signal(ebitda, sgna):
    """Acceleration/Jerk for Operating income per unit of overhead over 1260d window."""
    res = _jerk(_ratio(ebitda, sgna), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_5d_v133_signal(sgna):
    """Normalized slope change for Raw level of sgna over 5d window."""
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_5d_v134_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_5d_v135_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 5d window."""
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_5d_v136_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 5d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 5).diff(5) / _sma(_ratio(sgna, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_5d_v137_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 5d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 5).diff(5) / _sma(_ratio(ebitda, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_5d_v138_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 5d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 5).diff(5) / _sma(_ratio(ebitda, sgna).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_10d_v139_signal(sgna):
    """Normalized slope change for Raw level of sgna over 10d window."""
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_10d_v140_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_10d_v141_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 10d window."""
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_10d_v142_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 10d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 10).diff(10) / _sma(_ratio(sgna, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_10d_v143_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 10d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 10).diff(10) / _sma(_ratio(ebitda, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_10d_v144_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 10d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 10).diff(10) / _sma(_ratio(ebitda, sgna).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_21d_v145_signal(sgna):
    """Normalized slope change for Raw level of sgna over 21d window."""
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_21d_v146_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_21d_v147_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 21d window."""
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_21d_v148_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 21d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 21).diff(21) / _sma(_ratio(sgna, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_21d_v149_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 21d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 21).diff(21) / _sma(_ratio(ebitda, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_21d_v150_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 21d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 21).diff(21) / _sma(_ratio(ebitda, sgna).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f04_efficiency_ratio_sgna_slope_pct_5d_v001_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_5d_v001_signal},
    "f04_efficiency_ratio_revenue_slope_pct_5d_v002_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_5d_v002_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_5d_v003_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_5d_v003_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_5d_v004_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_5d_v004_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_5d_v005_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_5d_v005_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_5d_v006_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_5d_v006_signal},
    "f04_efficiency_ratio_sgna_slope_pct_10d_v007_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_10d_v007_signal},
    "f04_efficiency_ratio_revenue_slope_pct_10d_v008_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_10d_v008_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_10d_v009_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_10d_v009_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_10d_v010_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_10d_v010_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_10d_v011_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_10d_v011_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_10d_v012_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_10d_v012_signal},
    "f04_efficiency_ratio_sgna_slope_pct_21d_v013_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_21d_v013_signal},
    "f04_efficiency_ratio_revenue_slope_pct_21d_v014_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_21d_v014_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_21d_v015_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_21d_v015_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_21d_v016_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_21d_v016_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_21d_v017_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_21d_v017_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_21d_v018_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_21d_v018_signal},
    "f04_efficiency_ratio_sgna_slope_pct_42d_v019_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_42d_v019_signal},
    "f04_efficiency_ratio_revenue_slope_pct_42d_v020_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_42d_v020_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_42d_v021_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_42d_v021_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_42d_v022_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_42d_v022_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_42d_v023_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_42d_v023_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_42d_v024_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_42d_v024_signal},
    "f04_efficiency_ratio_sgna_slope_pct_63d_v025_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_63d_v025_signal},
    "f04_efficiency_ratio_revenue_slope_pct_63d_v026_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_63d_v026_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_63d_v027_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_63d_v027_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_63d_v028_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_63d_v028_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_63d_v029_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_63d_v029_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_63d_v030_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_63d_v030_signal},
    "f04_efficiency_ratio_sgna_slope_pct_126d_v031_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_126d_v031_signal},
    "f04_efficiency_ratio_revenue_slope_pct_126d_v032_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_126d_v032_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_126d_v033_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_126d_v033_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_126d_v034_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_126d_v034_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_126d_v035_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_126d_v035_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_126d_v036_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_126d_v036_signal},
    "f04_efficiency_ratio_sgna_slope_pct_252d_v037_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_252d_v037_signal},
    "f04_efficiency_ratio_revenue_slope_pct_252d_v038_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_252d_v038_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_252d_v039_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_252d_v039_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_252d_v040_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_252d_v040_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_252d_v041_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_252d_v041_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_252d_v042_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_252d_v042_signal},
    "f04_efficiency_ratio_sgna_slope_pct_504d_v043_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_504d_v043_signal},
    "f04_efficiency_ratio_revenue_slope_pct_504d_v044_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_504d_v044_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_504d_v045_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_504d_v045_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_504d_v046_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_504d_v046_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_504d_v047_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_504d_v047_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_504d_v048_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_504d_v048_signal},
    "f04_efficiency_ratio_sgna_slope_pct_756d_v049_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_756d_v049_signal},
    "f04_efficiency_ratio_revenue_slope_pct_756d_v050_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_756d_v050_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_756d_v051_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_756d_v051_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_756d_v052_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_756d_v052_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_756d_v053_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_756d_v053_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_756d_v054_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_756d_v054_signal},
    "f04_efficiency_ratio_sgna_slope_pct_1008d_v055_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_1008d_v055_signal},
    "f04_efficiency_ratio_revenue_slope_pct_1008d_v056_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_1008d_v056_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_1008d_v057_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_1008d_v057_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_1008d_v058_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_1008d_v058_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_1008d_v059_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_1008d_v059_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_1008d_v060_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_1008d_v060_signal},
    "f04_efficiency_ratio_sgna_slope_pct_1260d_v061_signal": {"func": f04_efficiency_ratio_sgna_slope_pct_1260d_v061_signal},
    "f04_efficiency_ratio_revenue_slope_pct_1260d_v062_signal": {"func": f04_efficiency_ratio_revenue_slope_pct_1260d_v062_signal},
    "f04_efficiency_ratio_ebitda_slope_pct_1260d_v063_signal": {"func": f04_efficiency_ratio_ebitda_slope_pct_1260d_v063_signal},
    "f04_efficiency_ratio_efficiency_score_slope_pct_1260d_v064_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_pct_1260d_v064_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_pct_1260d_v065_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_pct_1260d_v065_signal},
    "f04_efficiency_ratio_overhead_yield_slope_pct_1260d_v066_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_pct_1260d_v066_signal},
    "f04_efficiency_ratio_sgna_jerk_5d_v067_signal": {"func": f04_efficiency_ratio_sgna_jerk_5d_v067_signal},
    "f04_efficiency_ratio_revenue_jerk_5d_v068_signal": {"func": f04_efficiency_ratio_revenue_jerk_5d_v068_signal},
    "f04_efficiency_ratio_ebitda_jerk_5d_v069_signal": {"func": f04_efficiency_ratio_ebitda_jerk_5d_v069_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_5d_v070_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_5d_v070_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_5d_v071_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_5d_v071_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_5d_v072_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_5d_v072_signal},
    "f04_efficiency_ratio_sgna_jerk_10d_v073_signal": {"func": f04_efficiency_ratio_sgna_jerk_10d_v073_signal},
    "f04_efficiency_ratio_revenue_jerk_10d_v074_signal": {"func": f04_efficiency_ratio_revenue_jerk_10d_v074_signal},
    "f04_efficiency_ratio_ebitda_jerk_10d_v075_signal": {"func": f04_efficiency_ratio_ebitda_jerk_10d_v075_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_10d_v076_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_10d_v076_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_10d_v077_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_10d_v077_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_10d_v078_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_10d_v078_signal},
    "f04_efficiency_ratio_sgna_jerk_21d_v079_signal": {"func": f04_efficiency_ratio_sgna_jerk_21d_v079_signal},
    "f04_efficiency_ratio_revenue_jerk_21d_v080_signal": {"func": f04_efficiency_ratio_revenue_jerk_21d_v080_signal},
    "f04_efficiency_ratio_ebitda_jerk_21d_v081_signal": {"func": f04_efficiency_ratio_ebitda_jerk_21d_v081_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_21d_v082_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_21d_v082_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_21d_v083_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_21d_v083_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_21d_v084_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_21d_v084_signal},
    "f04_efficiency_ratio_sgna_jerk_42d_v085_signal": {"func": f04_efficiency_ratio_sgna_jerk_42d_v085_signal},
    "f04_efficiency_ratio_revenue_jerk_42d_v086_signal": {"func": f04_efficiency_ratio_revenue_jerk_42d_v086_signal},
    "f04_efficiency_ratio_ebitda_jerk_42d_v087_signal": {"func": f04_efficiency_ratio_ebitda_jerk_42d_v087_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_42d_v088_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_42d_v088_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_42d_v089_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_42d_v089_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_42d_v090_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_42d_v090_signal},
    "f04_efficiency_ratio_sgna_jerk_63d_v091_signal": {"func": f04_efficiency_ratio_sgna_jerk_63d_v091_signal},
    "f04_efficiency_ratio_revenue_jerk_63d_v092_signal": {"func": f04_efficiency_ratio_revenue_jerk_63d_v092_signal},
    "f04_efficiency_ratio_ebitda_jerk_63d_v093_signal": {"func": f04_efficiency_ratio_ebitda_jerk_63d_v093_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_63d_v094_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_63d_v094_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_63d_v095_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_63d_v095_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_63d_v096_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_63d_v096_signal},
    "f04_efficiency_ratio_sgna_jerk_126d_v097_signal": {"func": f04_efficiency_ratio_sgna_jerk_126d_v097_signal},
    "f04_efficiency_ratio_revenue_jerk_126d_v098_signal": {"func": f04_efficiency_ratio_revenue_jerk_126d_v098_signal},
    "f04_efficiency_ratio_ebitda_jerk_126d_v099_signal": {"func": f04_efficiency_ratio_ebitda_jerk_126d_v099_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_126d_v100_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_126d_v100_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_126d_v101_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_126d_v101_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_126d_v102_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_126d_v102_signal},
    "f04_efficiency_ratio_sgna_jerk_252d_v103_signal": {"func": f04_efficiency_ratio_sgna_jerk_252d_v103_signal},
    "f04_efficiency_ratio_revenue_jerk_252d_v104_signal": {"func": f04_efficiency_ratio_revenue_jerk_252d_v104_signal},
    "f04_efficiency_ratio_ebitda_jerk_252d_v105_signal": {"func": f04_efficiency_ratio_ebitda_jerk_252d_v105_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_252d_v106_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_252d_v106_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_252d_v107_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_252d_v107_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_252d_v108_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_252d_v108_signal},
    "f04_efficiency_ratio_sgna_jerk_504d_v109_signal": {"func": f04_efficiency_ratio_sgna_jerk_504d_v109_signal},
    "f04_efficiency_ratio_revenue_jerk_504d_v110_signal": {"func": f04_efficiency_ratio_revenue_jerk_504d_v110_signal},
    "f04_efficiency_ratio_ebitda_jerk_504d_v111_signal": {"func": f04_efficiency_ratio_ebitda_jerk_504d_v111_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_504d_v112_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_504d_v112_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_504d_v113_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_504d_v113_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_504d_v114_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_504d_v114_signal},
    "f04_efficiency_ratio_sgna_jerk_756d_v115_signal": {"func": f04_efficiency_ratio_sgna_jerk_756d_v115_signal},
    "f04_efficiency_ratio_revenue_jerk_756d_v116_signal": {"func": f04_efficiency_ratio_revenue_jerk_756d_v116_signal},
    "f04_efficiency_ratio_ebitda_jerk_756d_v117_signal": {"func": f04_efficiency_ratio_ebitda_jerk_756d_v117_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_756d_v118_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_756d_v118_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_756d_v119_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_756d_v119_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_756d_v120_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_756d_v120_signal},
    "f04_efficiency_ratio_sgna_jerk_1008d_v121_signal": {"func": f04_efficiency_ratio_sgna_jerk_1008d_v121_signal},
    "f04_efficiency_ratio_revenue_jerk_1008d_v122_signal": {"func": f04_efficiency_ratio_revenue_jerk_1008d_v122_signal},
    "f04_efficiency_ratio_ebitda_jerk_1008d_v123_signal": {"func": f04_efficiency_ratio_ebitda_jerk_1008d_v123_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_1008d_v124_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_1008d_v124_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_1008d_v125_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_1008d_v125_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_1008d_v126_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_1008d_v126_signal},
    "f04_efficiency_ratio_sgna_jerk_1260d_v127_signal": {"func": f04_efficiency_ratio_sgna_jerk_1260d_v127_signal},
    "f04_efficiency_ratio_revenue_jerk_1260d_v128_signal": {"func": f04_efficiency_ratio_revenue_jerk_1260d_v128_signal},
    "f04_efficiency_ratio_ebitda_jerk_1260d_v129_signal": {"func": f04_efficiency_ratio_ebitda_jerk_1260d_v129_signal},
    "f04_efficiency_ratio_efficiency_score_jerk_1260d_v130_signal": {"func": f04_efficiency_ratio_efficiency_score_jerk_1260d_v130_signal},
    "f04_efficiency_ratio_ebitda_margin_jerk_1260d_v131_signal": {"func": f04_efficiency_ratio_ebitda_margin_jerk_1260d_v131_signal},
    "f04_efficiency_ratio_overhead_yield_jerk_1260d_v132_signal": {"func": f04_efficiency_ratio_overhead_yield_jerk_1260d_v132_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_5d_v133_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_5d_v133_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_5d_v134_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_5d_v134_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_5d_v135_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_5d_v135_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_5d_v136_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_5d_v136_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_5d_v137_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_5d_v137_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_5d_v138_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_5d_v138_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_10d_v139_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_10d_v139_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_10d_v140_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_10d_v140_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_10d_v141_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_10d_v141_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_10d_v142_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_10d_v142_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_10d_v143_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_10d_v143_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_10d_v144_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_10d_v144_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_21d_v145_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_21d_v145_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_21d_v146_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_21d_v146_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_21d_v147_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_21d_v147_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_21d_v148_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_21d_v148_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_21d_v149_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_21d_v149_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_21d_v150_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_21d_v150_signal},
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
