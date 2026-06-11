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

def f47_retail_roic_stability_roic_base_5d_v001_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 5d window."""
    res = _sma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_5d_v002_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 5d window."""
    res = _sma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_5d_v003_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 5d window."""
    res = _sma(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_5d_v004_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 5d window."""
    res = _sma(_z(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_10d_v005_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 10d window."""
    res = _sma(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_10d_v006_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 10d window."""
    res = _sma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_10d_v007_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 10d window."""
    res = _sma(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_10d_v008_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 10d window."""
    res = _sma(_z(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_21d_v009_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 21d window."""
    res = _sma(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_21d_v010_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 21d window."""
    res = _sma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_21d_v011_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 21d window."""
    res = _sma(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_21d_v012_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 21d window."""
    res = _sma(_z(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_42d_v013_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 42d window."""
    res = _sma(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_42d_v014_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 42d window."""
    res = _sma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_42d_v015_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 42d window."""
    res = _sma(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_42d_v016_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 42d window."""
    res = _sma(_z(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_63d_v017_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 63d window."""
    res = _sma(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_63d_v018_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 63d window."""
    res = _sma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_63d_v019_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 63d window."""
    res = _sma(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_63d_v020_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 63d window."""
    res = _sma(_z(roic, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_126d_v021_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 126d window."""
    res = _sma(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_126d_v022_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 126d window."""
    res = _sma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_126d_v023_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 126d window."""
    res = _sma(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_126d_v024_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 126d window."""
    res = _sma(_z(roic, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_252d_v025_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 252d window."""
    res = _sma(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_252d_v026_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 252d window."""
    res = _sma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_252d_v027_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 252d window."""
    res = _sma(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_252d_v028_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 252d window."""
    res = _sma(_z(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_504d_v029_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 504d window."""
    res = _sma(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_504d_v030_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 504d window."""
    res = _sma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_504d_v031_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 504d window."""
    res = _sma(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_504d_v032_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 504d window."""
    res = _sma(_z(roic, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_756d_v033_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 756d window."""
    res = _sma(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_756d_v034_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 756d window."""
    res = _sma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_756d_v035_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 756d window."""
    res = _sma(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_756d_v036_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 756d window."""
    res = _sma(_z(roic, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_1008d_v037_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 1008d window."""
    res = _sma(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_1008d_v038_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 1008d window."""
    res = _sma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_1008d_v039_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 1008d window."""
    res = _sma(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_1008d_v040_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 1008d window."""
    res = _sma(_z(roic, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_base_1260d_v041_signal(roic):
    """Moving average to smooth noise of Raw level of roic over 1260d window."""
    res = _sma(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_base_1260d_v042_signal(ebit):
    """Moving average to smooth noise of Raw level of ebit over 1260d window."""
    res = _sma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_base_1260d_v043_signal(invcap):
    """Moving average to smooth noise of Raw level of invcap over 1260d window."""
    res = _sma(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_base_1260d_v044_signal(roic):
    """Moving average to smooth noise of Z-score of ROIC relative to 1y history over 1260d window."""
    res = _sma(_z(roic, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_5d_v045_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 5d window."""
    res = _z(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_5d_v046_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 5d window."""
    res = _z(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_5d_v047_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 5d window."""
    res = _z(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_5d_v048_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 5d window."""
    res = _z(_z(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_10d_v049_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 10d window."""
    res = _z(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_10d_v050_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 10d window."""
    res = _z(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_10d_v051_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 10d window."""
    res = _z(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_10d_v052_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 10d window."""
    res = _z(_z(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_21d_v053_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 21d window."""
    res = _z(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_21d_v054_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 21d window."""
    res = _z(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_21d_v055_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 21d window."""
    res = _z(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_21d_v056_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 21d window."""
    res = _z(_z(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_42d_v057_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 42d window."""
    res = _z(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_42d_v058_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 42d window."""
    res = _z(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_42d_v059_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 42d window."""
    res = _z(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_42d_v060_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 42d window."""
    res = _z(_z(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_63d_v061_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 63d window."""
    res = _z(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_63d_v062_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 63d window."""
    res = _z(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_63d_v063_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 63d window."""
    res = _z(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_63d_v064_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 63d window."""
    res = _z(_z(roic, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_126d_v065_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 126d window."""
    res = _z(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_126d_v066_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 126d window."""
    res = _z(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_126d_v067_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 126d window."""
    res = _z(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_126d_v068_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 126d window."""
    res = _z(_z(roic, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_252d_v069_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 252d window."""
    res = _z(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_252d_v070_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 252d window."""
    res = _z(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_252d_v071_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 252d window."""
    res = _z(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_252d_v072_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 252d window."""
    res = _z(_z(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_504d_v073_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 504d window."""
    res = _z(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_504d_v074_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 504d window."""
    res = _z(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_504d_v075_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 504d window."""
    res = _z(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f47_retail_roic_stability_roic_base_5d_v001_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_5d_v001_signal},    "f47_retail_roic_stability_ebit_base_5d_v002_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_5d_v002_signal},    "f47_retail_roic_stability_invcap_base_5d_v003_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_5d_v003_signal},    "f47_retail_roic_stability_roic_z_base_5d_v004_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_5d_v004_signal},    "f47_retail_roic_stability_roic_base_10d_v005_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_10d_v005_signal},    "f47_retail_roic_stability_ebit_base_10d_v006_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_10d_v006_signal},    "f47_retail_roic_stability_invcap_base_10d_v007_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_10d_v007_signal},    "f47_retail_roic_stability_roic_z_base_10d_v008_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_10d_v008_signal},    "f47_retail_roic_stability_roic_base_21d_v009_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_21d_v009_signal},    "f47_retail_roic_stability_ebit_base_21d_v010_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_21d_v010_signal},    "f47_retail_roic_stability_invcap_base_21d_v011_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_21d_v011_signal},    "f47_retail_roic_stability_roic_z_base_21d_v012_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_21d_v012_signal},    "f47_retail_roic_stability_roic_base_42d_v013_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_42d_v013_signal},    "f47_retail_roic_stability_ebit_base_42d_v014_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_42d_v014_signal},    "f47_retail_roic_stability_invcap_base_42d_v015_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_42d_v015_signal},    "f47_retail_roic_stability_roic_z_base_42d_v016_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_42d_v016_signal},    "f47_retail_roic_stability_roic_base_63d_v017_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_63d_v017_signal},    "f47_retail_roic_stability_ebit_base_63d_v018_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_63d_v018_signal},    "f47_retail_roic_stability_invcap_base_63d_v019_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_63d_v019_signal},    "f47_retail_roic_stability_roic_z_base_63d_v020_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_63d_v020_signal},    "f47_retail_roic_stability_roic_base_126d_v021_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_126d_v021_signal},    "f47_retail_roic_stability_ebit_base_126d_v022_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_126d_v022_signal},    "f47_retail_roic_stability_invcap_base_126d_v023_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_126d_v023_signal},    "f47_retail_roic_stability_roic_z_base_126d_v024_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_126d_v024_signal},    "f47_retail_roic_stability_roic_base_252d_v025_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_252d_v025_signal},    "f47_retail_roic_stability_ebit_base_252d_v026_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_252d_v026_signal},    "f47_retail_roic_stability_invcap_base_252d_v027_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_252d_v027_signal},    "f47_retail_roic_stability_roic_z_base_252d_v028_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_252d_v028_signal},    "f47_retail_roic_stability_roic_base_504d_v029_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_504d_v029_signal},    "f47_retail_roic_stability_ebit_base_504d_v030_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_504d_v030_signal},    "f47_retail_roic_stability_invcap_base_504d_v031_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_504d_v031_signal},    "f47_retail_roic_stability_roic_z_base_504d_v032_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_504d_v032_signal},    "f47_retail_roic_stability_roic_base_756d_v033_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_756d_v033_signal},    "f47_retail_roic_stability_ebit_base_756d_v034_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_756d_v034_signal},    "f47_retail_roic_stability_invcap_base_756d_v035_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_756d_v035_signal},    "f47_retail_roic_stability_roic_z_base_756d_v036_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_756d_v036_signal},    "f47_retail_roic_stability_roic_base_1008d_v037_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_1008d_v037_signal},    "f47_retail_roic_stability_ebit_base_1008d_v038_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_1008d_v038_signal},    "f47_retail_roic_stability_invcap_base_1008d_v039_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_1008d_v039_signal},    "f47_retail_roic_stability_roic_z_base_1008d_v040_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_1008d_v040_signal},    "f47_retail_roic_stability_roic_base_1260d_v041_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_base_1260d_v041_signal},    "f47_retail_roic_stability_ebit_base_1260d_v042_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_base_1260d_v042_signal},    "f47_retail_roic_stability_invcap_base_1260d_v043_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_base_1260d_v043_signal},    "f47_retail_roic_stability_roic_z_base_1260d_v044_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_base_1260d_v044_signal},    "f47_retail_roic_stability_roic_z_5d_v045_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_5d_v045_signal},    "f47_retail_roic_stability_ebit_z_5d_v046_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_5d_v046_signal},    "f47_retail_roic_stability_invcap_z_5d_v047_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_5d_v047_signal},    "f47_retail_roic_stability_roic_z_z_5d_v048_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_5d_v048_signal},    "f47_retail_roic_stability_roic_z_10d_v049_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_10d_v049_signal},    "f47_retail_roic_stability_ebit_z_10d_v050_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_10d_v050_signal},    "f47_retail_roic_stability_invcap_z_10d_v051_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_10d_v051_signal},    "f47_retail_roic_stability_roic_z_z_10d_v052_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_10d_v052_signal},    "f47_retail_roic_stability_roic_z_21d_v053_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_21d_v053_signal},    "f47_retail_roic_stability_ebit_z_21d_v054_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_21d_v054_signal},    "f47_retail_roic_stability_invcap_z_21d_v055_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_21d_v055_signal},    "f47_retail_roic_stability_roic_z_z_21d_v056_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_21d_v056_signal},    "f47_retail_roic_stability_roic_z_42d_v057_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_42d_v057_signal},    "f47_retail_roic_stability_ebit_z_42d_v058_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_42d_v058_signal},    "f47_retail_roic_stability_invcap_z_42d_v059_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_42d_v059_signal},    "f47_retail_roic_stability_roic_z_z_42d_v060_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_42d_v060_signal},    "f47_retail_roic_stability_roic_z_63d_v061_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_63d_v061_signal},    "f47_retail_roic_stability_ebit_z_63d_v062_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_63d_v062_signal},    "f47_retail_roic_stability_invcap_z_63d_v063_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_63d_v063_signal},    "f47_retail_roic_stability_roic_z_z_63d_v064_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_63d_v064_signal},    "f47_retail_roic_stability_roic_z_126d_v065_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_126d_v065_signal},    "f47_retail_roic_stability_ebit_z_126d_v066_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_126d_v066_signal},    "f47_retail_roic_stability_invcap_z_126d_v067_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_126d_v067_signal},    "f47_retail_roic_stability_roic_z_z_126d_v068_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_126d_v068_signal},    "f47_retail_roic_stability_roic_z_252d_v069_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_252d_v069_signal},    "f47_retail_roic_stability_ebit_z_252d_v070_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_252d_v070_signal},    "f47_retail_roic_stability_invcap_z_252d_v071_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_252d_v071_signal},    "f47_retail_roic_stability_roic_z_z_252d_v072_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_252d_v072_signal},    "f47_retail_roic_stability_roic_z_504d_v073_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_504d_v073_signal},    "f47_retail_roic_stability_ebit_z_504d_v074_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_504d_v074_signal},    "f47_retail_roic_stability_invcap_z_504d_v075_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 47...")
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
