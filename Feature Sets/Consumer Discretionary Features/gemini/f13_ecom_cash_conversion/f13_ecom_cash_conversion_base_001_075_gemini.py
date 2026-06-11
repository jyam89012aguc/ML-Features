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

def f13_ecom_cash_conversion_revenue_base_5d_v001_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_5d_v002_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 5d window."""
    res = _sma(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_5d_v003_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 5d window."""
    res = _sma(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_5d_v004_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 5d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_10d_v005_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_10d_v006_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 10d window."""
    res = _sma(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_10d_v007_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 10d window."""
    res = _sma(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_10d_v008_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 10d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_21d_v009_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_21d_v010_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 21d window."""
    res = _sma(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_21d_v011_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 21d window."""
    res = _sma(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_21d_v012_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 21d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_42d_v013_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_42d_v014_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 42d window."""
    res = _sma(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_42d_v015_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 42d window."""
    res = _sma(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_42d_v016_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 42d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_63d_v017_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_63d_v018_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 63d window."""
    res = _sma(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_63d_v019_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 63d window."""
    res = _sma(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_63d_v020_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 63d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_126d_v021_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_126d_v022_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 126d window."""
    res = _sma(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_126d_v023_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 126d window."""
    res = _sma(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_126d_v024_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 126d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_252d_v025_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_252d_v026_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 252d window."""
    res = _sma(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_252d_v027_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 252d window."""
    res = _sma(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_252d_v028_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 252d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_504d_v029_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_504d_v030_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 504d window."""
    res = _sma(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_504d_v031_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 504d window."""
    res = _sma(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_504d_v032_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 504d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_756d_v033_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_756d_v034_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 756d window."""
    res = _sma(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_756d_v035_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 756d window."""
    res = _sma(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_756d_v036_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 756d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_1008d_v037_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_1008d_v038_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 1008d window."""
    res = _sma(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_1008d_v039_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 1008d window."""
    res = _sma(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_1008d_v040_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 1008d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_base_1260d_v041_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_base_1260d_v042_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 1260d window."""
    res = _sma(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_base_1260d_v043_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 1260d window."""
    res = _sma(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_base_1260d_v044_signal(cashneq, deferredrev, revenue):
    """Moving average to smooth noise of Digital liquidity and upfront payment strength over 1260d window."""
    res = _sma(_ratio(cashneq + deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_5d_v045_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_5d_v046_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 5d window."""
    res = _z(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_5d_v047_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 5d window."""
    res = _z(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_5d_v048_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 5d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_10d_v049_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_10d_v050_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 10d window."""
    res = _z(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_10d_v051_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 10d window."""
    res = _z(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_10d_v052_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 10d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_21d_v053_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_21d_v054_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 21d window."""
    res = _z(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_21d_v055_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 21d window."""
    res = _z(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_21d_v056_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 21d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_42d_v057_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_42d_v058_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 42d window."""
    res = _z(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_42d_v059_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 42d window."""
    res = _z(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_42d_v060_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 42d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_63d_v061_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_63d_v062_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 63d window."""
    res = _z(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_63d_v063_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 63d window."""
    res = _z(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_63d_v064_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 63d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_126d_v065_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_126d_v066_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 126d window."""
    res = _z(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_126d_v067_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 126d window."""
    res = _z(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_126d_v068_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 126d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_252d_v069_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_252d_v070_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 252d window."""
    res = _z(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_252d_v071_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 252d window."""
    res = _z(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_252d_v072_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 252d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_504d_v073_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_504d_v074_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 504d window."""
    res = _z(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_504d_v075_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 504d window."""
    res = _z(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f13_ecom_cash_conversion_revenue_base_5d_v001_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_5d_v001_signal},    "f13_ecom_cash_conversion_deferredrev_base_5d_v002_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_5d_v002_signal},    "f13_ecom_cash_conversion_cashneq_base_5d_v003_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_5d_v003_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_5d_v004_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_5d_v004_signal},    "f13_ecom_cash_conversion_revenue_base_10d_v005_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_10d_v005_signal},    "f13_ecom_cash_conversion_deferredrev_base_10d_v006_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_10d_v006_signal},    "f13_ecom_cash_conversion_cashneq_base_10d_v007_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_10d_v007_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_10d_v008_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_10d_v008_signal},    "f13_ecom_cash_conversion_revenue_base_21d_v009_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_21d_v009_signal},    "f13_ecom_cash_conversion_deferredrev_base_21d_v010_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_21d_v010_signal},    "f13_ecom_cash_conversion_cashneq_base_21d_v011_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_21d_v011_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_21d_v012_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_21d_v012_signal},    "f13_ecom_cash_conversion_revenue_base_42d_v013_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_42d_v013_signal},    "f13_ecom_cash_conversion_deferredrev_base_42d_v014_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_42d_v014_signal},    "f13_ecom_cash_conversion_cashneq_base_42d_v015_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_42d_v015_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_42d_v016_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_42d_v016_signal},    "f13_ecom_cash_conversion_revenue_base_63d_v017_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_63d_v017_signal},    "f13_ecom_cash_conversion_deferredrev_base_63d_v018_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_63d_v018_signal},    "f13_ecom_cash_conversion_cashneq_base_63d_v019_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_63d_v019_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_63d_v020_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_63d_v020_signal},    "f13_ecom_cash_conversion_revenue_base_126d_v021_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_126d_v021_signal},    "f13_ecom_cash_conversion_deferredrev_base_126d_v022_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_126d_v022_signal},    "f13_ecom_cash_conversion_cashneq_base_126d_v023_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_126d_v023_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_126d_v024_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_126d_v024_signal},    "f13_ecom_cash_conversion_revenue_base_252d_v025_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_252d_v025_signal},    "f13_ecom_cash_conversion_deferredrev_base_252d_v026_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_252d_v026_signal},    "f13_ecom_cash_conversion_cashneq_base_252d_v027_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_252d_v027_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_252d_v028_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_252d_v028_signal},    "f13_ecom_cash_conversion_revenue_base_504d_v029_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_504d_v029_signal},    "f13_ecom_cash_conversion_deferredrev_base_504d_v030_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_504d_v030_signal},    "f13_ecom_cash_conversion_cashneq_base_504d_v031_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_504d_v031_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_504d_v032_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_504d_v032_signal},    "f13_ecom_cash_conversion_revenue_base_756d_v033_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_756d_v033_signal},    "f13_ecom_cash_conversion_deferredrev_base_756d_v034_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_756d_v034_signal},    "f13_ecom_cash_conversion_cashneq_base_756d_v035_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_756d_v035_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_756d_v036_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_756d_v036_signal},    "f13_ecom_cash_conversion_revenue_base_1008d_v037_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_1008d_v037_signal},    "f13_ecom_cash_conversion_deferredrev_base_1008d_v038_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_1008d_v038_signal},    "f13_ecom_cash_conversion_cashneq_base_1008d_v039_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_1008d_v039_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_1008d_v040_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_1008d_v040_signal},    "f13_ecom_cash_conversion_revenue_base_1260d_v041_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_base_1260d_v041_signal},    "f13_ecom_cash_conversion_deferredrev_base_1260d_v042_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_base_1260d_v042_signal},    "f13_ecom_cash_conversion_cashneq_base_1260d_v043_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_base_1260d_v043_signal},    "f13_ecom_cash_conversion_ecom_liquidity_base_1260d_v044_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_base_1260d_v044_signal},    "f13_ecom_cash_conversion_revenue_z_5d_v045_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_5d_v045_signal},    "f13_ecom_cash_conversion_deferredrev_z_5d_v046_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_5d_v046_signal},    "f13_ecom_cash_conversion_cashneq_z_5d_v047_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_5d_v047_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_5d_v048_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_5d_v048_signal},    "f13_ecom_cash_conversion_revenue_z_10d_v049_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_10d_v049_signal},    "f13_ecom_cash_conversion_deferredrev_z_10d_v050_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_10d_v050_signal},    "f13_ecom_cash_conversion_cashneq_z_10d_v051_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_10d_v051_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_10d_v052_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_10d_v052_signal},    "f13_ecom_cash_conversion_revenue_z_21d_v053_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_21d_v053_signal},    "f13_ecom_cash_conversion_deferredrev_z_21d_v054_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_21d_v054_signal},    "f13_ecom_cash_conversion_cashneq_z_21d_v055_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_21d_v055_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_21d_v056_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_21d_v056_signal},    "f13_ecom_cash_conversion_revenue_z_42d_v057_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_42d_v057_signal},    "f13_ecom_cash_conversion_deferredrev_z_42d_v058_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_42d_v058_signal},    "f13_ecom_cash_conversion_cashneq_z_42d_v059_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_42d_v059_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_42d_v060_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_42d_v060_signal},    "f13_ecom_cash_conversion_revenue_z_63d_v061_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_63d_v061_signal},    "f13_ecom_cash_conversion_deferredrev_z_63d_v062_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_63d_v062_signal},    "f13_ecom_cash_conversion_cashneq_z_63d_v063_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_63d_v063_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_63d_v064_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_63d_v064_signal},    "f13_ecom_cash_conversion_revenue_z_126d_v065_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_126d_v065_signal},    "f13_ecom_cash_conversion_deferredrev_z_126d_v066_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_126d_v066_signal},    "f13_ecom_cash_conversion_cashneq_z_126d_v067_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_126d_v067_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_126d_v068_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_126d_v068_signal},    "f13_ecom_cash_conversion_revenue_z_252d_v069_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_252d_v069_signal},    "f13_ecom_cash_conversion_deferredrev_z_252d_v070_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_252d_v070_signal},    "f13_ecom_cash_conversion_cashneq_z_252d_v071_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_252d_v071_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_252d_v072_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_252d_v072_signal},    "f13_ecom_cash_conversion_revenue_z_504d_v073_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_504d_v073_signal},    "f13_ecom_cash_conversion_deferredrev_z_504d_v074_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_504d_v074_signal},    "f13_ecom_cash_conversion_cashneq_z_504d_v075_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 13...")
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
