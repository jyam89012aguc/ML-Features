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

def f25_brand_equity_grossmargin_base_5d_v001_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 5d window."""
    res = _sma(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_5d_v002_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 5d window."""
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_5d_v003_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 5d window."""
    res = _sma(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_5d_v004_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 5d window."""
    res = _sma(grossmargin * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_10d_v005_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 10d window."""
    res = _sma(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_10d_v006_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 10d window."""
    res = _sma(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_10d_v007_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 10d window."""
    res = _sma(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_10d_v008_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 10d window."""
    res = _sma(grossmargin * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_21d_v009_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 21d window."""
    res = _sma(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_21d_v010_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 21d window."""
    res = _sma(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_21d_v011_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 21d window."""
    res = _sma(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_21d_v012_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 21d window."""
    res = _sma(grossmargin * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_42d_v013_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 42d window."""
    res = _sma(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_42d_v014_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 42d window."""
    res = _sma(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_42d_v015_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 42d window."""
    res = _sma(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_42d_v016_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 42d window."""
    res = _sma(grossmargin * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_63d_v017_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 63d window."""
    res = _sma(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_63d_v018_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 63d window."""
    res = _sma(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_63d_v019_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 63d window."""
    res = _sma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_63d_v020_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 63d window."""
    res = _sma(grossmargin * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_126d_v021_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 126d window."""
    res = _sma(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_126d_v022_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 126d window."""
    res = _sma(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_126d_v023_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 126d window."""
    res = _sma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_126d_v024_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 126d window."""
    res = _sma(grossmargin * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_252d_v025_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 252d window."""
    res = _sma(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_252d_v026_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 252d window."""
    res = _sma(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_252d_v027_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 252d window."""
    res = _sma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_252d_v028_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 252d window."""
    res = _sma(grossmargin * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_504d_v029_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 504d window."""
    res = _sma(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_504d_v030_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 504d window."""
    res = _sma(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_504d_v031_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 504d window."""
    res = _sma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_504d_v032_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 504d window."""
    res = _sma(grossmargin * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_756d_v033_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 756d window."""
    res = _sma(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_756d_v034_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 756d window."""
    res = _sma(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_756d_v035_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 756d window."""
    res = _sma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_756d_v036_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 756d window."""
    res = _sma(grossmargin * pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_1008d_v037_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 1008d window."""
    res = _sma(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_1008d_v038_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 1008d window."""
    res = _sma(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_1008d_v039_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 1008d window."""
    res = _sma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_1008d_v040_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 1008d window."""
    res = _sma(grossmargin * pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_base_1260d_v041_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 1260d window."""
    res = _sma(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_base_1260d_v042_signal(pe):
    """Moving average to smooth noise of Raw level of pe over 1260d window."""
    res = _sma(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_base_1260d_v043_signal(pb):
    """Moving average to smooth noise of Raw level of pb over 1260d window."""
    res = _sma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_base_1260d_v044_signal(grossmargin, pe):
    """Moving average to smooth noise of Brand margin amplified by market valuation multiples over 1260d window."""
    res = _sma(grossmargin * pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_5d_v045_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 5d window."""
    res = _z(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_5d_v046_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 5d window."""
    res = _z(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_5d_v047_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 5d window."""
    res = _z(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_5d_v048_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 5d window."""
    res = _z(grossmargin * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_10d_v049_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 10d window."""
    res = _z(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_10d_v050_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 10d window."""
    res = _z(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_10d_v051_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 10d window."""
    res = _z(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_10d_v052_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 10d window."""
    res = _z(grossmargin * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_21d_v053_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 21d window."""
    res = _z(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_21d_v054_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 21d window."""
    res = _z(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_21d_v055_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 21d window."""
    res = _z(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_21d_v056_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 21d window."""
    res = _z(grossmargin * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_42d_v057_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 42d window."""
    res = _z(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_42d_v058_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 42d window."""
    res = _z(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_42d_v059_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 42d window."""
    res = _z(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_42d_v060_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 42d window."""
    res = _z(grossmargin * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_63d_v061_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 63d window."""
    res = _z(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_63d_v062_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 63d window."""
    res = _z(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_63d_v063_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 63d window."""
    res = _z(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_63d_v064_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 63d window."""
    res = _z(grossmargin * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_126d_v065_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 126d window."""
    res = _z(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_126d_v066_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 126d window."""
    res = _z(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_126d_v067_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 126d window."""
    res = _z(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_126d_v068_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 126d window."""
    res = _z(grossmargin * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_252d_v069_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 252d window."""
    res = _z(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_252d_v070_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 252d window."""
    res = _z(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_252d_v071_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 252d window."""
    res = _z(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_252d_v072_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 252d window."""
    res = _z(grossmargin * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_504d_v073_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 504d window."""
    res = _z(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_504d_v074_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 504d window."""
    res = _z(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_504d_v075_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 504d window."""
    res = _z(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f25_brand_equity_grossmargin_base_5d_v001_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_5d_v001_signal},    "f25_brand_equity_pe_base_5d_v002_signal": {"inputs": [], "func": f25_brand_equity_pe_base_5d_v002_signal},    "f25_brand_equity_pb_base_5d_v003_signal": {"inputs": [], "func": f25_brand_equity_pb_base_5d_v003_signal},    "f25_brand_equity_equity_moat_base_5d_v004_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_5d_v004_signal},    "f25_brand_equity_grossmargin_base_10d_v005_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_10d_v005_signal},    "f25_brand_equity_pe_base_10d_v006_signal": {"inputs": [], "func": f25_brand_equity_pe_base_10d_v006_signal},    "f25_brand_equity_pb_base_10d_v007_signal": {"inputs": [], "func": f25_brand_equity_pb_base_10d_v007_signal},    "f25_brand_equity_equity_moat_base_10d_v008_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_10d_v008_signal},    "f25_brand_equity_grossmargin_base_21d_v009_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_21d_v009_signal},    "f25_brand_equity_pe_base_21d_v010_signal": {"inputs": [], "func": f25_brand_equity_pe_base_21d_v010_signal},    "f25_brand_equity_pb_base_21d_v011_signal": {"inputs": [], "func": f25_brand_equity_pb_base_21d_v011_signal},    "f25_brand_equity_equity_moat_base_21d_v012_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_21d_v012_signal},    "f25_brand_equity_grossmargin_base_42d_v013_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_42d_v013_signal},    "f25_brand_equity_pe_base_42d_v014_signal": {"inputs": [], "func": f25_brand_equity_pe_base_42d_v014_signal},    "f25_brand_equity_pb_base_42d_v015_signal": {"inputs": [], "func": f25_brand_equity_pb_base_42d_v015_signal},    "f25_brand_equity_equity_moat_base_42d_v016_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_42d_v016_signal},    "f25_brand_equity_grossmargin_base_63d_v017_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_63d_v017_signal},    "f25_brand_equity_pe_base_63d_v018_signal": {"inputs": [], "func": f25_brand_equity_pe_base_63d_v018_signal},    "f25_brand_equity_pb_base_63d_v019_signal": {"inputs": [], "func": f25_brand_equity_pb_base_63d_v019_signal},    "f25_brand_equity_equity_moat_base_63d_v020_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_63d_v020_signal},    "f25_brand_equity_grossmargin_base_126d_v021_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_126d_v021_signal},    "f25_brand_equity_pe_base_126d_v022_signal": {"inputs": [], "func": f25_brand_equity_pe_base_126d_v022_signal},    "f25_brand_equity_pb_base_126d_v023_signal": {"inputs": [], "func": f25_brand_equity_pb_base_126d_v023_signal},    "f25_brand_equity_equity_moat_base_126d_v024_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_126d_v024_signal},    "f25_brand_equity_grossmargin_base_252d_v025_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_252d_v025_signal},    "f25_brand_equity_pe_base_252d_v026_signal": {"inputs": [], "func": f25_brand_equity_pe_base_252d_v026_signal},    "f25_brand_equity_pb_base_252d_v027_signal": {"inputs": [], "func": f25_brand_equity_pb_base_252d_v027_signal},    "f25_brand_equity_equity_moat_base_252d_v028_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_252d_v028_signal},    "f25_brand_equity_grossmargin_base_504d_v029_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_504d_v029_signal},    "f25_brand_equity_pe_base_504d_v030_signal": {"inputs": [], "func": f25_brand_equity_pe_base_504d_v030_signal},    "f25_brand_equity_pb_base_504d_v031_signal": {"inputs": [], "func": f25_brand_equity_pb_base_504d_v031_signal},    "f25_brand_equity_equity_moat_base_504d_v032_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_504d_v032_signal},    "f25_brand_equity_grossmargin_base_756d_v033_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_756d_v033_signal},    "f25_brand_equity_pe_base_756d_v034_signal": {"inputs": [], "func": f25_brand_equity_pe_base_756d_v034_signal},    "f25_brand_equity_pb_base_756d_v035_signal": {"inputs": [], "func": f25_brand_equity_pb_base_756d_v035_signal},    "f25_brand_equity_equity_moat_base_756d_v036_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_756d_v036_signal},    "f25_brand_equity_grossmargin_base_1008d_v037_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_1008d_v037_signal},    "f25_brand_equity_pe_base_1008d_v038_signal": {"inputs": [], "func": f25_brand_equity_pe_base_1008d_v038_signal},    "f25_brand_equity_pb_base_1008d_v039_signal": {"inputs": [], "func": f25_brand_equity_pb_base_1008d_v039_signal},    "f25_brand_equity_equity_moat_base_1008d_v040_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_1008d_v040_signal},    "f25_brand_equity_grossmargin_base_1260d_v041_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_base_1260d_v041_signal},    "f25_brand_equity_pe_base_1260d_v042_signal": {"inputs": [], "func": f25_brand_equity_pe_base_1260d_v042_signal},    "f25_brand_equity_pb_base_1260d_v043_signal": {"inputs": [], "func": f25_brand_equity_pb_base_1260d_v043_signal},    "f25_brand_equity_equity_moat_base_1260d_v044_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_base_1260d_v044_signal},    "f25_brand_equity_grossmargin_z_5d_v045_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_5d_v045_signal},    "f25_brand_equity_pe_z_5d_v046_signal": {"inputs": [], "func": f25_brand_equity_pe_z_5d_v046_signal},    "f25_brand_equity_pb_z_5d_v047_signal": {"inputs": [], "func": f25_brand_equity_pb_z_5d_v047_signal},    "f25_brand_equity_equity_moat_z_5d_v048_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_5d_v048_signal},    "f25_brand_equity_grossmargin_z_10d_v049_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_10d_v049_signal},    "f25_brand_equity_pe_z_10d_v050_signal": {"inputs": [], "func": f25_brand_equity_pe_z_10d_v050_signal},    "f25_brand_equity_pb_z_10d_v051_signal": {"inputs": [], "func": f25_brand_equity_pb_z_10d_v051_signal},    "f25_brand_equity_equity_moat_z_10d_v052_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_10d_v052_signal},    "f25_brand_equity_grossmargin_z_21d_v053_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_21d_v053_signal},    "f25_brand_equity_pe_z_21d_v054_signal": {"inputs": [], "func": f25_brand_equity_pe_z_21d_v054_signal},    "f25_brand_equity_pb_z_21d_v055_signal": {"inputs": [], "func": f25_brand_equity_pb_z_21d_v055_signal},    "f25_brand_equity_equity_moat_z_21d_v056_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_21d_v056_signal},    "f25_brand_equity_grossmargin_z_42d_v057_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_42d_v057_signal},    "f25_brand_equity_pe_z_42d_v058_signal": {"inputs": [], "func": f25_brand_equity_pe_z_42d_v058_signal},    "f25_brand_equity_pb_z_42d_v059_signal": {"inputs": [], "func": f25_brand_equity_pb_z_42d_v059_signal},    "f25_brand_equity_equity_moat_z_42d_v060_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_42d_v060_signal},    "f25_brand_equity_grossmargin_z_63d_v061_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_63d_v061_signal},    "f25_brand_equity_pe_z_63d_v062_signal": {"inputs": [], "func": f25_brand_equity_pe_z_63d_v062_signal},    "f25_brand_equity_pb_z_63d_v063_signal": {"inputs": [], "func": f25_brand_equity_pb_z_63d_v063_signal},    "f25_brand_equity_equity_moat_z_63d_v064_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_63d_v064_signal},    "f25_brand_equity_grossmargin_z_126d_v065_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_126d_v065_signal},    "f25_brand_equity_pe_z_126d_v066_signal": {"inputs": [], "func": f25_brand_equity_pe_z_126d_v066_signal},    "f25_brand_equity_pb_z_126d_v067_signal": {"inputs": [], "func": f25_brand_equity_pb_z_126d_v067_signal},    "f25_brand_equity_equity_moat_z_126d_v068_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_126d_v068_signal},    "f25_brand_equity_grossmargin_z_252d_v069_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_252d_v069_signal},    "f25_brand_equity_pe_z_252d_v070_signal": {"inputs": [], "func": f25_brand_equity_pe_z_252d_v070_signal},    "f25_brand_equity_pb_z_252d_v071_signal": {"inputs": [], "func": f25_brand_equity_pb_z_252d_v071_signal},    "f25_brand_equity_equity_moat_z_252d_v072_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_252d_v072_signal},    "f25_brand_equity_grossmargin_z_504d_v073_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_504d_v073_signal},    "f25_brand_equity_pe_z_504d_v074_signal": {"inputs": [], "func": f25_brand_equity_pe_z_504d_v074_signal},    "f25_brand_equity_pb_z_504d_v075_signal": {"inputs": [], "func": f25_brand_equity_pb_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 25...")
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
