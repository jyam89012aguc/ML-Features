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

def f12_labor_productivity_sgna_base_5d_v001_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_5d_v002_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 5d window."""
    res = _sma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_5d_v003_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_5d_v004_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 5d window."""
    res = _sma(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_10d_v005_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_10d_v006_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 10d window."""
    res = _sma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_10d_v007_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_10d_v008_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 10d window."""
    res = _sma(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_21d_v009_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_21d_v010_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 21d window."""
    res = _sma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_21d_v011_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_21d_v012_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 21d window."""
    res = _sma(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_42d_v013_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_42d_v014_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 42d window."""
    res = _sma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_42d_v015_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_42d_v016_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 42d window."""
    res = _sma(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_63d_v017_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_63d_v018_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 63d window."""
    res = _sma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_63d_v019_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_63d_v020_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 63d window."""
    res = _sma(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_126d_v021_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_126d_v022_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 126d window."""
    res = _sma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_126d_v023_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_126d_v024_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 126d window."""
    res = _sma(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_252d_v025_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_252d_v026_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 252d window."""
    res = _sma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_252d_v027_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_252d_v028_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 252d window."""
    res = _sma(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_504d_v029_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_504d_v030_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 504d window."""
    res = _sma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_504d_v031_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_504d_v032_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 504d window."""
    res = _sma(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_756d_v033_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_756d_v034_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 756d window."""
    res = _sma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_756d_v035_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_756d_v036_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 756d window."""
    res = _sma(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_1008d_v037_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_1008d_v038_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 1008d window."""
    res = _sma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_1008d_v039_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_1008d_v040_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 1008d window."""
    res = _sma(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_base_1260d_v041_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_base_1260d_v042_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 1260d window."""
    res = _sma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_base_1260d_v043_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_base_1260d_v044_signal(revenue, sgna):
    """Moving average to smooth noise of Sales productivity of the labor/overhead base over 1260d window."""
    res = _sma(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_5d_v045_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 5d window."""
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_5d_v046_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 5d window."""
    res = _z(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_5d_v047_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_5d_v048_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 5d window."""
    res = _z(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_10d_v049_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 10d window."""
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_10d_v050_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 10d window."""
    res = _z(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_10d_v051_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_10d_v052_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 10d window."""
    res = _z(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_21d_v053_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 21d window."""
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_21d_v054_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 21d window."""
    res = _z(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_21d_v055_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_21d_v056_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 21d window."""
    res = _z(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_42d_v057_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 42d window."""
    res = _z(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_42d_v058_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 42d window."""
    res = _z(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_42d_v059_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_42d_v060_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 42d window."""
    res = _z(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_63d_v061_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 63d window."""
    res = _z(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_63d_v062_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 63d window."""
    res = _z(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_63d_v063_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_63d_v064_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 63d window."""
    res = _z(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_126d_v065_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 126d window."""
    res = _z(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_126d_v066_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 126d window."""
    res = _z(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_126d_v067_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_126d_v068_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 126d window."""
    res = _z(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_252d_v069_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 252d window."""
    res = _z(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_252d_v070_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 252d window."""
    res = _z(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_252d_v071_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_labor_leverage_z_252d_v072_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales productivity of the labor/overhead base over 252d window."""
    res = _z(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_sgna_z_504d_v073_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 504d window."""
    res = _z(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_ebit_z_504d_v074_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 504d window."""
    res = _z(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_labor_productivity_revenue_z_504d_v075_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f12_labor_productivity_sgna_base_5d_v001_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_5d_v001_signal},    "f12_labor_productivity_ebit_base_5d_v002_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_5d_v002_signal},    "f12_labor_productivity_revenue_base_5d_v003_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_5d_v003_signal},    "f12_labor_productivity_labor_leverage_base_5d_v004_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_5d_v004_signal},    "f12_labor_productivity_sgna_base_10d_v005_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_10d_v005_signal},    "f12_labor_productivity_ebit_base_10d_v006_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_10d_v006_signal},    "f12_labor_productivity_revenue_base_10d_v007_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_10d_v007_signal},    "f12_labor_productivity_labor_leverage_base_10d_v008_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_10d_v008_signal},    "f12_labor_productivity_sgna_base_21d_v009_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_21d_v009_signal},    "f12_labor_productivity_ebit_base_21d_v010_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_21d_v010_signal},    "f12_labor_productivity_revenue_base_21d_v011_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_21d_v011_signal},    "f12_labor_productivity_labor_leverage_base_21d_v012_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_21d_v012_signal},    "f12_labor_productivity_sgna_base_42d_v013_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_42d_v013_signal},    "f12_labor_productivity_ebit_base_42d_v014_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_42d_v014_signal},    "f12_labor_productivity_revenue_base_42d_v015_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_42d_v015_signal},    "f12_labor_productivity_labor_leverage_base_42d_v016_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_42d_v016_signal},    "f12_labor_productivity_sgna_base_63d_v017_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_63d_v017_signal},    "f12_labor_productivity_ebit_base_63d_v018_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_63d_v018_signal},    "f12_labor_productivity_revenue_base_63d_v019_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_63d_v019_signal},    "f12_labor_productivity_labor_leverage_base_63d_v020_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_63d_v020_signal},    "f12_labor_productivity_sgna_base_126d_v021_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_126d_v021_signal},    "f12_labor_productivity_ebit_base_126d_v022_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_126d_v022_signal},    "f12_labor_productivity_revenue_base_126d_v023_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_126d_v023_signal},    "f12_labor_productivity_labor_leverage_base_126d_v024_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_126d_v024_signal},    "f12_labor_productivity_sgna_base_252d_v025_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_252d_v025_signal},    "f12_labor_productivity_ebit_base_252d_v026_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_252d_v026_signal},    "f12_labor_productivity_revenue_base_252d_v027_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_252d_v027_signal},    "f12_labor_productivity_labor_leverage_base_252d_v028_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_252d_v028_signal},    "f12_labor_productivity_sgna_base_504d_v029_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_504d_v029_signal},    "f12_labor_productivity_ebit_base_504d_v030_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_504d_v030_signal},    "f12_labor_productivity_revenue_base_504d_v031_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_504d_v031_signal},    "f12_labor_productivity_labor_leverage_base_504d_v032_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_504d_v032_signal},    "f12_labor_productivity_sgna_base_756d_v033_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_756d_v033_signal},    "f12_labor_productivity_ebit_base_756d_v034_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_756d_v034_signal},    "f12_labor_productivity_revenue_base_756d_v035_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_756d_v035_signal},    "f12_labor_productivity_labor_leverage_base_756d_v036_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_756d_v036_signal},    "f12_labor_productivity_sgna_base_1008d_v037_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_1008d_v037_signal},    "f12_labor_productivity_ebit_base_1008d_v038_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_1008d_v038_signal},    "f12_labor_productivity_revenue_base_1008d_v039_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_1008d_v039_signal},    "f12_labor_productivity_labor_leverage_base_1008d_v040_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_1008d_v040_signal},    "f12_labor_productivity_sgna_base_1260d_v041_signal": {"inputs": [], "func": f12_labor_productivity_sgna_base_1260d_v041_signal},    "f12_labor_productivity_ebit_base_1260d_v042_signal": {"inputs": [], "func": f12_labor_productivity_ebit_base_1260d_v042_signal},    "f12_labor_productivity_revenue_base_1260d_v043_signal": {"inputs": [], "func": f12_labor_productivity_revenue_base_1260d_v043_signal},    "f12_labor_productivity_labor_leverage_base_1260d_v044_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_base_1260d_v044_signal},    "f12_labor_productivity_sgna_z_5d_v045_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_5d_v045_signal},    "f12_labor_productivity_ebit_z_5d_v046_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_5d_v046_signal},    "f12_labor_productivity_revenue_z_5d_v047_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_5d_v047_signal},    "f12_labor_productivity_labor_leverage_z_5d_v048_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_5d_v048_signal},    "f12_labor_productivity_sgna_z_10d_v049_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_10d_v049_signal},    "f12_labor_productivity_ebit_z_10d_v050_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_10d_v050_signal},    "f12_labor_productivity_revenue_z_10d_v051_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_10d_v051_signal},    "f12_labor_productivity_labor_leverage_z_10d_v052_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_10d_v052_signal},    "f12_labor_productivity_sgna_z_21d_v053_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_21d_v053_signal},    "f12_labor_productivity_ebit_z_21d_v054_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_21d_v054_signal},    "f12_labor_productivity_revenue_z_21d_v055_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_21d_v055_signal},    "f12_labor_productivity_labor_leverage_z_21d_v056_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_21d_v056_signal},    "f12_labor_productivity_sgna_z_42d_v057_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_42d_v057_signal},    "f12_labor_productivity_ebit_z_42d_v058_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_42d_v058_signal},    "f12_labor_productivity_revenue_z_42d_v059_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_42d_v059_signal},    "f12_labor_productivity_labor_leverage_z_42d_v060_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_42d_v060_signal},    "f12_labor_productivity_sgna_z_63d_v061_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_63d_v061_signal},    "f12_labor_productivity_ebit_z_63d_v062_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_63d_v062_signal},    "f12_labor_productivity_revenue_z_63d_v063_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_63d_v063_signal},    "f12_labor_productivity_labor_leverage_z_63d_v064_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_63d_v064_signal},    "f12_labor_productivity_sgna_z_126d_v065_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_126d_v065_signal},    "f12_labor_productivity_ebit_z_126d_v066_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_126d_v066_signal},    "f12_labor_productivity_revenue_z_126d_v067_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_126d_v067_signal},    "f12_labor_productivity_labor_leverage_z_126d_v068_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_126d_v068_signal},    "f12_labor_productivity_sgna_z_252d_v069_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_252d_v069_signal},    "f12_labor_productivity_ebit_z_252d_v070_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_252d_v070_signal},    "f12_labor_productivity_revenue_z_252d_v071_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_252d_v071_signal},    "f12_labor_productivity_labor_leverage_z_252d_v072_signal": {"inputs": [], "func": f12_labor_productivity_labor_leverage_z_252d_v072_signal},    "f12_labor_productivity_sgna_z_504d_v073_signal": {"inputs": [], "func": f12_labor_productivity_sgna_z_504d_v073_signal},    "f12_labor_productivity_ebit_z_504d_v074_signal": {"inputs": [], "func": f12_labor_productivity_ebit_z_504d_v074_signal},    "f12_labor_productivity_revenue_z_504d_v075_signal": {"inputs": [], "func": f12_labor_productivity_revenue_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 12...")
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
