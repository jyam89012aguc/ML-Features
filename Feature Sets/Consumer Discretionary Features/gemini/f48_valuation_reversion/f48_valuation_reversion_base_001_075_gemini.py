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

def f48_valuation_reversion_pe_base_5d_v001_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 5d window."""
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_5d_v002_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 5d window."""
    res = _sma(ps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_5d_v003_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 5d window."""
    res = _sma(ev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_5d_v004_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 5d window."""
    res = _sma(_z(ps, 1260), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_10d_v005_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 10d window."""
    res = _sma(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_10d_v006_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 10d window."""
    res = _sma(ps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_10d_v007_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 10d window."""
    res = _sma(ev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_10d_v008_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 10d window."""
    res = _sma(_z(ps, 1260), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_21d_v009_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 21d window."""
    res = _sma(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_21d_v010_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 21d window."""
    res = _sma(ps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_21d_v011_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 21d window."""
    res = _sma(ev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_21d_v012_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 21d window."""
    res = _sma(_z(ps, 1260), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_42d_v013_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 42d window."""
    res = _sma(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_42d_v014_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 42d window."""
    res = _sma(ps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_42d_v015_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 42d window."""
    res = _sma(ev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_42d_v016_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 42d window."""
    res = _sma(_z(ps, 1260), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_63d_v017_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 63d window."""
    res = _sma(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_63d_v018_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 63d window."""
    res = _sma(ps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_63d_v019_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 63d window."""
    res = _sma(ev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_63d_v020_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 63d window."""
    res = _sma(_z(ps, 1260), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_126d_v021_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 126d window."""
    res = _sma(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_126d_v022_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 126d window."""
    res = _sma(ps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_126d_v023_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 126d window."""
    res = _sma(ev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_126d_v024_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 126d window."""
    res = _sma(_z(ps, 1260), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_252d_v025_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 252d window."""
    res = _sma(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_252d_v026_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 252d window."""
    res = _sma(ps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_252d_v027_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 252d window."""
    res = _sma(ev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_252d_v028_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 252d window."""
    res = _sma(_z(ps, 1260), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_504d_v029_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 504d window."""
    res = _sma(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_504d_v030_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 504d window."""
    res = _sma(ps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_504d_v031_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 504d window."""
    res = _sma(ev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_504d_v032_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 504d window."""
    res = _sma(_z(ps, 1260), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_756d_v033_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 756d window."""
    res = _sma(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_756d_v034_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 756d window."""
    res = _sma(ps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_756d_v035_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 756d window."""
    res = _sma(ev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_756d_v036_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 756d window."""
    res = _sma(_z(ps, 1260), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_1008d_v037_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 1008d window."""
    res = _sma(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_1008d_v038_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 1008d window."""
    res = _sma(ps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_1008d_v039_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 1008d window."""
    res = _sma(ev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_1008d_v040_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 1008d window."""
    res = _sma(_z(ps, 1260), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_base_1260d_v041_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 1260d window."""
    res = _sma(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_base_1260d_v042_signal(ps):
    """Moving average to smooth noise of Raw level of ps over 1260d window."""
    res = _sma(ps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_base_1260d_v043_signal(ev):
    """Moving average to smooth noise of Raw level of ev over 1260d window."""
    res = _sma(ev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_base_1260d_v044_signal(ps):
    """Moving average to smooth noise of Z-score of Price-to-Sales relative to 5y history over 1260d window."""
    res = _sma(_z(ps, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_5d_v045_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 5d window."""
    res = _z(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_5d_v046_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 5d window."""
    res = _z(ps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_5d_v047_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 5d window."""
    res = _z(ev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_5d_v048_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 5d window."""
    res = _z(_z(ps, 1260), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_10d_v049_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 10d window."""
    res = _z(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_10d_v050_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 10d window."""
    res = _z(ps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_10d_v051_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 10d window."""
    res = _z(ev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_10d_v052_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 10d window."""
    res = _z(_z(ps, 1260), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_21d_v053_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 21d window."""
    res = _z(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_21d_v054_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 21d window."""
    res = _z(ps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_21d_v055_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 21d window."""
    res = _z(ev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_21d_v056_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 21d window."""
    res = _z(_z(ps, 1260), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_42d_v057_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 42d window."""
    res = _z(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_42d_v058_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 42d window."""
    res = _z(ps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_42d_v059_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 42d window."""
    res = _z(ev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_42d_v060_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 42d window."""
    res = _z(_z(ps, 1260), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_63d_v061_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 63d window."""
    res = _z(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_63d_v062_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 63d window."""
    res = _z(ps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_63d_v063_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 63d window."""
    res = _z(ev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_63d_v064_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 63d window."""
    res = _z(_z(ps, 1260), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_126d_v065_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 126d window."""
    res = _z(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_126d_v066_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 126d window."""
    res = _z(ps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_126d_v067_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 126d window."""
    res = _z(ev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_126d_v068_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 126d window."""
    res = _z(_z(ps, 1260), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_252d_v069_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 252d window."""
    res = _z(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_252d_v070_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 252d window."""
    res = _z(ps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_252d_v071_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 252d window."""
    res = _z(ev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_z_252d_v072_signal(ps):
    """Z-score for relative outlier detection of Z-score of Price-to-Sales relative to 5y history over 252d window."""
    res = _z(_z(ps, 1260), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_pe_z_504d_v073_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 504d window."""
    res = _z(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ps_z_504d_v074_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 504d window."""
    res = _z(ps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f48_valuation_reversion_ev_z_504d_v075_signal(ev):
    """Z-score for relative outlier detection of Raw level of ev over 504d window."""
    res = _z(ev, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f48_valuation_reversion_pe_base_5d_v001_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_5d_v001_signal},    "f48_valuation_reversion_ps_base_5d_v002_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_5d_v002_signal},    "f48_valuation_reversion_ev_base_5d_v003_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_5d_v003_signal},    "f48_valuation_reversion_ps_z_base_5d_v004_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_5d_v004_signal},    "f48_valuation_reversion_pe_base_10d_v005_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_10d_v005_signal},    "f48_valuation_reversion_ps_base_10d_v006_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_10d_v006_signal},    "f48_valuation_reversion_ev_base_10d_v007_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_10d_v007_signal},    "f48_valuation_reversion_ps_z_base_10d_v008_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_10d_v008_signal},    "f48_valuation_reversion_pe_base_21d_v009_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_21d_v009_signal},    "f48_valuation_reversion_ps_base_21d_v010_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_21d_v010_signal},    "f48_valuation_reversion_ev_base_21d_v011_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_21d_v011_signal},    "f48_valuation_reversion_ps_z_base_21d_v012_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_21d_v012_signal},    "f48_valuation_reversion_pe_base_42d_v013_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_42d_v013_signal},    "f48_valuation_reversion_ps_base_42d_v014_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_42d_v014_signal},    "f48_valuation_reversion_ev_base_42d_v015_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_42d_v015_signal},    "f48_valuation_reversion_ps_z_base_42d_v016_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_42d_v016_signal},    "f48_valuation_reversion_pe_base_63d_v017_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_63d_v017_signal},    "f48_valuation_reversion_ps_base_63d_v018_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_63d_v018_signal},    "f48_valuation_reversion_ev_base_63d_v019_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_63d_v019_signal},    "f48_valuation_reversion_ps_z_base_63d_v020_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_63d_v020_signal},    "f48_valuation_reversion_pe_base_126d_v021_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_126d_v021_signal},    "f48_valuation_reversion_ps_base_126d_v022_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_126d_v022_signal},    "f48_valuation_reversion_ev_base_126d_v023_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_126d_v023_signal},    "f48_valuation_reversion_ps_z_base_126d_v024_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_126d_v024_signal},    "f48_valuation_reversion_pe_base_252d_v025_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_252d_v025_signal},    "f48_valuation_reversion_ps_base_252d_v026_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_252d_v026_signal},    "f48_valuation_reversion_ev_base_252d_v027_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_252d_v027_signal},    "f48_valuation_reversion_ps_z_base_252d_v028_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_252d_v028_signal},    "f48_valuation_reversion_pe_base_504d_v029_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_504d_v029_signal},    "f48_valuation_reversion_ps_base_504d_v030_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_504d_v030_signal},    "f48_valuation_reversion_ev_base_504d_v031_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_504d_v031_signal},    "f48_valuation_reversion_ps_z_base_504d_v032_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_504d_v032_signal},    "f48_valuation_reversion_pe_base_756d_v033_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_756d_v033_signal},    "f48_valuation_reversion_ps_base_756d_v034_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_756d_v034_signal},    "f48_valuation_reversion_ev_base_756d_v035_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_756d_v035_signal},    "f48_valuation_reversion_ps_z_base_756d_v036_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_756d_v036_signal},    "f48_valuation_reversion_pe_base_1008d_v037_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_1008d_v037_signal},    "f48_valuation_reversion_ps_base_1008d_v038_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_1008d_v038_signal},    "f48_valuation_reversion_ev_base_1008d_v039_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_1008d_v039_signal},    "f48_valuation_reversion_ps_z_base_1008d_v040_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_1008d_v040_signal},    "f48_valuation_reversion_pe_base_1260d_v041_signal": {"inputs": [], "func": f48_valuation_reversion_pe_base_1260d_v041_signal},    "f48_valuation_reversion_ps_base_1260d_v042_signal": {"inputs": [], "func": f48_valuation_reversion_ps_base_1260d_v042_signal},    "f48_valuation_reversion_ev_base_1260d_v043_signal": {"inputs": [], "func": f48_valuation_reversion_ev_base_1260d_v043_signal},    "f48_valuation_reversion_ps_z_base_1260d_v044_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_base_1260d_v044_signal},    "f48_valuation_reversion_pe_z_5d_v045_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_5d_v045_signal},    "f48_valuation_reversion_ps_z_5d_v046_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_5d_v046_signal},    "f48_valuation_reversion_ev_z_5d_v047_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_5d_v047_signal},    "f48_valuation_reversion_ps_z_z_5d_v048_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_5d_v048_signal},    "f48_valuation_reversion_pe_z_10d_v049_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_10d_v049_signal},    "f48_valuation_reversion_ps_z_10d_v050_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_10d_v050_signal},    "f48_valuation_reversion_ev_z_10d_v051_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_10d_v051_signal},    "f48_valuation_reversion_ps_z_z_10d_v052_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_10d_v052_signal},    "f48_valuation_reversion_pe_z_21d_v053_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_21d_v053_signal},    "f48_valuation_reversion_ps_z_21d_v054_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_21d_v054_signal},    "f48_valuation_reversion_ev_z_21d_v055_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_21d_v055_signal},    "f48_valuation_reversion_ps_z_z_21d_v056_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_21d_v056_signal},    "f48_valuation_reversion_pe_z_42d_v057_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_42d_v057_signal},    "f48_valuation_reversion_ps_z_42d_v058_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_42d_v058_signal},    "f48_valuation_reversion_ev_z_42d_v059_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_42d_v059_signal},    "f48_valuation_reversion_ps_z_z_42d_v060_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_42d_v060_signal},    "f48_valuation_reversion_pe_z_63d_v061_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_63d_v061_signal},    "f48_valuation_reversion_ps_z_63d_v062_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_63d_v062_signal},    "f48_valuation_reversion_ev_z_63d_v063_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_63d_v063_signal},    "f48_valuation_reversion_ps_z_z_63d_v064_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_63d_v064_signal},    "f48_valuation_reversion_pe_z_126d_v065_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_126d_v065_signal},    "f48_valuation_reversion_ps_z_126d_v066_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_126d_v066_signal},    "f48_valuation_reversion_ev_z_126d_v067_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_126d_v067_signal},    "f48_valuation_reversion_ps_z_z_126d_v068_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_126d_v068_signal},    "f48_valuation_reversion_pe_z_252d_v069_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_252d_v069_signal},    "f48_valuation_reversion_ps_z_252d_v070_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_252d_v070_signal},    "f48_valuation_reversion_ev_z_252d_v071_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_252d_v071_signal},    "f48_valuation_reversion_ps_z_z_252d_v072_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_z_252d_v072_signal},    "f48_valuation_reversion_pe_z_504d_v073_signal": {"inputs": [], "func": f48_valuation_reversion_pe_z_504d_v073_signal},    "f48_valuation_reversion_ps_z_504d_v074_signal": {"inputs": [], "func": f48_valuation_reversion_ps_z_504d_v074_signal},    "f48_valuation_reversion_ev_z_504d_v075_signal": {"inputs": [], "func": f48_valuation_reversion_ev_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 48...")
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
