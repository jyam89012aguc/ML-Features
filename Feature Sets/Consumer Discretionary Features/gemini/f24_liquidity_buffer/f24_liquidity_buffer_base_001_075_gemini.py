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

def f24_liquidity_buffer_cashneq_base_5d_v001_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 5d window."""
    res = _sma(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_5d_v002_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_5d_v003_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 5d window."""
    res = _sma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_5d_v004_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 5d window."""
    res = _sma(_ratio(cashneq, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_10d_v005_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 10d window."""
    res = _sma(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_10d_v006_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_10d_v007_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 10d window."""
    res = _sma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_10d_v008_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 10d window."""
    res = _sma(_ratio(cashneq, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_21d_v009_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 21d window."""
    res = _sma(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_21d_v010_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_21d_v011_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 21d window."""
    res = _sma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_21d_v012_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 21d window."""
    res = _sma(_ratio(cashneq, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_42d_v013_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 42d window."""
    res = _sma(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_42d_v014_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_42d_v015_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 42d window."""
    res = _sma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_42d_v016_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 42d window."""
    res = _sma(_ratio(cashneq, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_63d_v017_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 63d window."""
    res = _sma(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_63d_v018_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_63d_v019_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 63d window."""
    res = _sma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_63d_v020_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 63d window."""
    res = _sma(_ratio(cashneq, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_126d_v021_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 126d window."""
    res = _sma(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_126d_v022_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_126d_v023_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 126d window."""
    res = _sma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_126d_v024_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 126d window."""
    res = _sma(_ratio(cashneq, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_252d_v025_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 252d window."""
    res = _sma(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_252d_v026_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_252d_v027_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 252d window."""
    res = _sma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_252d_v028_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 252d window."""
    res = _sma(_ratio(cashneq, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_504d_v029_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 504d window."""
    res = _sma(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_504d_v030_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_504d_v031_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 504d window."""
    res = _sma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_504d_v032_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 504d window."""
    res = _sma(_ratio(cashneq, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_756d_v033_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 756d window."""
    res = _sma(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_756d_v034_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_756d_v035_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 756d window."""
    res = _sma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_756d_v036_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 756d window."""
    res = _sma(_ratio(cashneq, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_1008d_v037_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 1008d window."""
    res = _sma(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_1008d_v038_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_1008d_v039_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 1008d window."""
    res = _sma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_1008d_v040_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 1008d window."""
    res = _sma(_ratio(cashneq, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_base_1260d_v041_signal(cashneq):
    """Moving average to smooth noise of Raw level of cashneq over 1260d window."""
    res = _sma(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_base_1260d_v042_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_base_1260d_v043_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 1260d window."""
    res = _sma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_base_1260d_v044_signal(cashneq, sgna):
    """Moving average to smooth noise of Cash coverage of SG&A burn over 1260d window."""
    res = _sma(_ratio(cashneq, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_5d_v045_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 5d window."""
    res = _z(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_5d_v046_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 5d window."""
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_5d_v047_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 5d window."""
    res = _z(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_5d_v048_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 5d window."""
    res = _z(_ratio(cashneq, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_10d_v049_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 10d window."""
    res = _z(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_10d_v050_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 10d window."""
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_10d_v051_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 10d window."""
    res = _z(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_10d_v052_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 10d window."""
    res = _z(_ratio(cashneq, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_21d_v053_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 21d window."""
    res = _z(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_21d_v054_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 21d window."""
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_21d_v055_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 21d window."""
    res = _z(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_21d_v056_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 21d window."""
    res = _z(_ratio(cashneq, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_42d_v057_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 42d window."""
    res = _z(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_42d_v058_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 42d window."""
    res = _z(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_42d_v059_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 42d window."""
    res = _z(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_42d_v060_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 42d window."""
    res = _z(_ratio(cashneq, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_63d_v061_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 63d window."""
    res = _z(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_63d_v062_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 63d window."""
    res = _z(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_63d_v063_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 63d window."""
    res = _z(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_63d_v064_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 63d window."""
    res = _z(_ratio(cashneq, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_126d_v065_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 126d window."""
    res = _z(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_126d_v066_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 126d window."""
    res = _z(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_126d_v067_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 126d window."""
    res = _z(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_126d_v068_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 126d window."""
    res = _z(_ratio(cashneq, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_252d_v069_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 252d window."""
    res = _z(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_252d_v070_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 252d window."""
    res = _z(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_252d_v071_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 252d window."""
    res = _z(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_252d_v072_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 252d window."""
    res = _z(_ratio(cashneq, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_504d_v073_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 504d window."""
    res = _z(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_504d_v074_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 504d window."""
    res = _z(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_504d_v075_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 504d window."""
    res = _z(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f24_liquidity_buffer_cashneq_base_5d_v001_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_5d_v001_signal},    "f24_liquidity_buffer_sgna_base_5d_v002_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_5d_v002_signal},    "f24_liquidity_buffer_cor_base_5d_v003_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_5d_v003_signal},    "f24_liquidity_buffer_runway_proxy_base_5d_v004_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_5d_v004_signal},    "f24_liquidity_buffer_cashneq_base_10d_v005_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_10d_v005_signal},    "f24_liquidity_buffer_sgna_base_10d_v006_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_10d_v006_signal},    "f24_liquidity_buffer_cor_base_10d_v007_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_10d_v007_signal},    "f24_liquidity_buffer_runway_proxy_base_10d_v008_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_10d_v008_signal},    "f24_liquidity_buffer_cashneq_base_21d_v009_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_21d_v009_signal},    "f24_liquidity_buffer_sgna_base_21d_v010_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_21d_v010_signal},    "f24_liquidity_buffer_cor_base_21d_v011_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_21d_v011_signal},    "f24_liquidity_buffer_runway_proxy_base_21d_v012_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_21d_v012_signal},    "f24_liquidity_buffer_cashneq_base_42d_v013_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_42d_v013_signal},    "f24_liquidity_buffer_sgna_base_42d_v014_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_42d_v014_signal},    "f24_liquidity_buffer_cor_base_42d_v015_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_42d_v015_signal},    "f24_liquidity_buffer_runway_proxy_base_42d_v016_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_42d_v016_signal},    "f24_liquidity_buffer_cashneq_base_63d_v017_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_63d_v017_signal},    "f24_liquidity_buffer_sgna_base_63d_v018_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_63d_v018_signal},    "f24_liquidity_buffer_cor_base_63d_v019_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_63d_v019_signal},    "f24_liquidity_buffer_runway_proxy_base_63d_v020_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_63d_v020_signal},    "f24_liquidity_buffer_cashneq_base_126d_v021_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_126d_v021_signal},    "f24_liquidity_buffer_sgna_base_126d_v022_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_126d_v022_signal},    "f24_liquidity_buffer_cor_base_126d_v023_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_126d_v023_signal},    "f24_liquidity_buffer_runway_proxy_base_126d_v024_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_126d_v024_signal},    "f24_liquidity_buffer_cashneq_base_252d_v025_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_252d_v025_signal},    "f24_liquidity_buffer_sgna_base_252d_v026_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_252d_v026_signal},    "f24_liquidity_buffer_cor_base_252d_v027_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_252d_v027_signal},    "f24_liquidity_buffer_runway_proxy_base_252d_v028_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_252d_v028_signal},    "f24_liquidity_buffer_cashneq_base_504d_v029_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_504d_v029_signal},    "f24_liquidity_buffer_sgna_base_504d_v030_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_504d_v030_signal},    "f24_liquidity_buffer_cor_base_504d_v031_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_504d_v031_signal},    "f24_liquidity_buffer_runway_proxy_base_504d_v032_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_504d_v032_signal},    "f24_liquidity_buffer_cashneq_base_756d_v033_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_756d_v033_signal},    "f24_liquidity_buffer_sgna_base_756d_v034_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_756d_v034_signal},    "f24_liquidity_buffer_cor_base_756d_v035_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_756d_v035_signal},    "f24_liquidity_buffer_runway_proxy_base_756d_v036_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_756d_v036_signal},    "f24_liquidity_buffer_cashneq_base_1008d_v037_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_1008d_v037_signal},    "f24_liquidity_buffer_sgna_base_1008d_v038_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_1008d_v038_signal},    "f24_liquidity_buffer_cor_base_1008d_v039_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_1008d_v039_signal},    "f24_liquidity_buffer_runway_proxy_base_1008d_v040_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_1008d_v040_signal},    "f24_liquidity_buffer_cashneq_base_1260d_v041_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_base_1260d_v041_signal},    "f24_liquidity_buffer_sgna_base_1260d_v042_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_base_1260d_v042_signal},    "f24_liquidity_buffer_cor_base_1260d_v043_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_base_1260d_v043_signal},    "f24_liquidity_buffer_runway_proxy_base_1260d_v044_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_base_1260d_v044_signal},    "f24_liquidity_buffer_cashneq_z_5d_v045_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_5d_v045_signal},    "f24_liquidity_buffer_sgna_z_5d_v046_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_5d_v046_signal},    "f24_liquidity_buffer_cor_z_5d_v047_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_5d_v047_signal},    "f24_liquidity_buffer_runway_proxy_z_5d_v048_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_5d_v048_signal},    "f24_liquidity_buffer_cashneq_z_10d_v049_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_10d_v049_signal},    "f24_liquidity_buffer_sgna_z_10d_v050_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_10d_v050_signal},    "f24_liquidity_buffer_cor_z_10d_v051_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_10d_v051_signal},    "f24_liquidity_buffer_runway_proxy_z_10d_v052_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_10d_v052_signal},    "f24_liquidity_buffer_cashneq_z_21d_v053_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_21d_v053_signal},    "f24_liquidity_buffer_sgna_z_21d_v054_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_21d_v054_signal},    "f24_liquidity_buffer_cor_z_21d_v055_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_21d_v055_signal},    "f24_liquidity_buffer_runway_proxy_z_21d_v056_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_21d_v056_signal},    "f24_liquidity_buffer_cashneq_z_42d_v057_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_42d_v057_signal},    "f24_liquidity_buffer_sgna_z_42d_v058_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_42d_v058_signal},    "f24_liquidity_buffer_cor_z_42d_v059_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_42d_v059_signal},    "f24_liquidity_buffer_runway_proxy_z_42d_v060_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_42d_v060_signal},    "f24_liquidity_buffer_cashneq_z_63d_v061_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_63d_v061_signal},    "f24_liquidity_buffer_sgna_z_63d_v062_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_63d_v062_signal},    "f24_liquidity_buffer_cor_z_63d_v063_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_63d_v063_signal},    "f24_liquidity_buffer_runway_proxy_z_63d_v064_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_63d_v064_signal},    "f24_liquidity_buffer_cashneq_z_126d_v065_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_126d_v065_signal},    "f24_liquidity_buffer_sgna_z_126d_v066_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_126d_v066_signal},    "f24_liquidity_buffer_cor_z_126d_v067_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_126d_v067_signal},    "f24_liquidity_buffer_runway_proxy_z_126d_v068_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_126d_v068_signal},    "f24_liquidity_buffer_cashneq_z_252d_v069_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_252d_v069_signal},    "f24_liquidity_buffer_sgna_z_252d_v070_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_252d_v070_signal},    "f24_liquidity_buffer_cor_z_252d_v071_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_252d_v071_signal},    "f24_liquidity_buffer_runway_proxy_z_252d_v072_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_252d_v072_signal},    "f24_liquidity_buffer_cashneq_z_504d_v073_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_504d_v073_signal},    "f24_liquidity_buffer_sgna_z_504d_v074_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_504d_v074_signal},    "f24_liquidity_buffer_cor_z_504d_v075_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 24...")
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
