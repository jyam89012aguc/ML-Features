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

def f09_markdown_risk_grossmargin_base_5d_v001_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 5d window."""
    res = _sma(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_5d_v002_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_5d_v003_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 5d window."""
    res = _sma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_5d_v004_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 5d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_10d_v005_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 10d window."""
    res = _sma(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_10d_v006_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_10d_v007_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 10d window."""
    res = _sma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_10d_v008_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 10d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_21d_v009_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 21d window."""
    res = _sma(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_21d_v010_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_21d_v011_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 21d window."""
    res = _sma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_21d_v012_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 21d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_42d_v013_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 42d window."""
    res = _sma(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_42d_v014_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_42d_v015_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 42d window."""
    res = _sma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_42d_v016_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 42d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_63d_v017_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 63d window."""
    res = _sma(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_63d_v018_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_63d_v019_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 63d window."""
    res = _sma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_63d_v020_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 63d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_126d_v021_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 126d window."""
    res = _sma(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_126d_v022_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_126d_v023_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 126d window."""
    res = _sma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_126d_v024_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 126d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_252d_v025_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 252d window."""
    res = _sma(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_252d_v026_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_252d_v027_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 252d window."""
    res = _sma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_252d_v028_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 252d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_504d_v029_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 504d window."""
    res = _sma(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_504d_v030_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_504d_v031_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 504d window."""
    res = _sma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_504d_v032_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 504d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_756d_v033_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 756d window."""
    res = _sma(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_756d_v034_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_756d_v035_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 756d window."""
    res = _sma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_756d_v036_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 756d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_1008d_v037_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 1008d window."""
    res = _sma(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_1008d_v038_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_1008d_v039_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 1008d window."""
    res = _sma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_1008d_v040_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 1008d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_base_1260d_v041_signal(grossmargin):
    """Moving average to smooth noise of Raw level of grossmargin over 1260d window."""
    res = _sma(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_base_1260d_v042_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_base_1260d_v043_signal(cor):
    """Moving average to smooth noise of Raw level of cor over 1260d window."""
    res = _sma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_base_1260d_v044_signal(grossmargin):
    """Moving average to smooth noise of Erosion of gross margin vs 1y average over 1260d window."""
    res = _sma(grossmargin - _sma(grossmargin, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_5d_v045_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 5d window."""
    res = _z(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_5d_v046_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_5d_v047_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 5d window."""
    res = _z(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_5d_v048_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 5d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_10d_v049_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 10d window."""
    res = _z(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_10d_v050_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_10d_v051_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 10d window."""
    res = _z(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_10d_v052_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 10d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_21d_v053_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 21d window."""
    res = _z(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_21d_v054_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_21d_v055_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 21d window."""
    res = _z(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_21d_v056_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 21d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_42d_v057_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 42d window."""
    res = _z(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_42d_v058_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_42d_v059_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 42d window."""
    res = _z(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_42d_v060_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 42d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_63d_v061_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 63d window."""
    res = _z(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_63d_v062_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_63d_v063_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 63d window."""
    res = _z(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_63d_v064_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 63d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_126d_v065_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 126d window."""
    res = _z(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_126d_v066_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_126d_v067_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 126d window."""
    res = _z(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_126d_v068_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 126d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_252d_v069_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 252d window."""
    res = _z(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_252d_v070_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_252d_v071_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 252d window."""
    res = _z(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_margin_erosion_z_252d_v072_signal(grossmargin):
    """Z-score for relative outlier detection of Erosion of gross margin vs 1y average over 252d window."""
    res = _z(grossmargin - _sma(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_grossmargin_z_504d_v073_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 504d window."""
    res = _z(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_revenue_z_504d_v074_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_markdown_risk_cor_z_504d_v075_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 504d window."""
    res = _z(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f09_markdown_risk_grossmargin_base_5d_v001_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_5d_v001_signal},    "f09_markdown_risk_revenue_base_5d_v002_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_5d_v002_signal},    "f09_markdown_risk_cor_base_5d_v003_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_5d_v003_signal},    "f09_markdown_risk_margin_erosion_base_5d_v004_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_5d_v004_signal},    "f09_markdown_risk_grossmargin_base_10d_v005_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_10d_v005_signal},    "f09_markdown_risk_revenue_base_10d_v006_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_10d_v006_signal},    "f09_markdown_risk_cor_base_10d_v007_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_10d_v007_signal},    "f09_markdown_risk_margin_erosion_base_10d_v008_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_10d_v008_signal},    "f09_markdown_risk_grossmargin_base_21d_v009_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_21d_v009_signal},    "f09_markdown_risk_revenue_base_21d_v010_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_21d_v010_signal},    "f09_markdown_risk_cor_base_21d_v011_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_21d_v011_signal},    "f09_markdown_risk_margin_erosion_base_21d_v012_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_21d_v012_signal},    "f09_markdown_risk_grossmargin_base_42d_v013_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_42d_v013_signal},    "f09_markdown_risk_revenue_base_42d_v014_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_42d_v014_signal},    "f09_markdown_risk_cor_base_42d_v015_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_42d_v015_signal},    "f09_markdown_risk_margin_erosion_base_42d_v016_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_42d_v016_signal},    "f09_markdown_risk_grossmargin_base_63d_v017_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_63d_v017_signal},    "f09_markdown_risk_revenue_base_63d_v018_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_63d_v018_signal},    "f09_markdown_risk_cor_base_63d_v019_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_63d_v019_signal},    "f09_markdown_risk_margin_erosion_base_63d_v020_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_63d_v020_signal},    "f09_markdown_risk_grossmargin_base_126d_v021_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_126d_v021_signal},    "f09_markdown_risk_revenue_base_126d_v022_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_126d_v022_signal},    "f09_markdown_risk_cor_base_126d_v023_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_126d_v023_signal},    "f09_markdown_risk_margin_erosion_base_126d_v024_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_126d_v024_signal},    "f09_markdown_risk_grossmargin_base_252d_v025_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_252d_v025_signal},    "f09_markdown_risk_revenue_base_252d_v026_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_252d_v026_signal},    "f09_markdown_risk_cor_base_252d_v027_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_252d_v027_signal},    "f09_markdown_risk_margin_erosion_base_252d_v028_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_252d_v028_signal},    "f09_markdown_risk_grossmargin_base_504d_v029_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_504d_v029_signal},    "f09_markdown_risk_revenue_base_504d_v030_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_504d_v030_signal},    "f09_markdown_risk_cor_base_504d_v031_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_504d_v031_signal},    "f09_markdown_risk_margin_erosion_base_504d_v032_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_504d_v032_signal},    "f09_markdown_risk_grossmargin_base_756d_v033_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_756d_v033_signal},    "f09_markdown_risk_revenue_base_756d_v034_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_756d_v034_signal},    "f09_markdown_risk_cor_base_756d_v035_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_756d_v035_signal},    "f09_markdown_risk_margin_erosion_base_756d_v036_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_756d_v036_signal},    "f09_markdown_risk_grossmargin_base_1008d_v037_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_1008d_v037_signal},    "f09_markdown_risk_revenue_base_1008d_v038_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_1008d_v038_signal},    "f09_markdown_risk_cor_base_1008d_v039_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_1008d_v039_signal},    "f09_markdown_risk_margin_erosion_base_1008d_v040_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_1008d_v040_signal},    "f09_markdown_risk_grossmargin_base_1260d_v041_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_base_1260d_v041_signal},    "f09_markdown_risk_revenue_base_1260d_v042_signal": {"inputs": [], "func": f09_markdown_risk_revenue_base_1260d_v042_signal},    "f09_markdown_risk_cor_base_1260d_v043_signal": {"inputs": [], "func": f09_markdown_risk_cor_base_1260d_v043_signal},    "f09_markdown_risk_margin_erosion_base_1260d_v044_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_base_1260d_v044_signal},    "f09_markdown_risk_grossmargin_z_5d_v045_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_5d_v045_signal},    "f09_markdown_risk_revenue_z_5d_v046_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_5d_v046_signal},    "f09_markdown_risk_cor_z_5d_v047_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_5d_v047_signal},    "f09_markdown_risk_margin_erosion_z_5d_v048_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_5d_v048_signal},    "f09_markdown_risk_grossmargin_z_10d_v049_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_10d_v049_signal},    "f09_markdown_risk_revenue_z_10d_v050_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_10d_v050_signal},    "f09_markdown_risk_cor_z_10d_v051_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_10d_v051_signal},    "f09_markdown_risk_margin_erosion_z_10d_v052_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_10d_v052_signal},    "f09_markdown_risk_grossmargin_z_21d_v053_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_21d_v053_signal},    "f09_markdown_risk_revenue_z_21d_v054_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_21d_v054_signal},    "f09_markdown_risk_cor_z_21d_v055_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_21d_v055_signal},    "f09_markdown_risk_margin_erosion_z_21d_v056_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_21d_v056_signal},    "f09_markdown_risk_grossmargin_z_42d_v057_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_42d_v057_signal},    "f09_markdown_risk_revenue_z_42d_v058_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_42d_v058_signal},    "f09_markdown_risk_cor_z_42d_v059_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_42d_v059_signal},    "f09_markdown_risk_margin_erosion_z_42d_v060_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_42d_v060_signal},    "f09_markdown_risk_grossmargin_z_63d_v061_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_63d_v061_signal},    "f09_markdown_risk_revenue_z_63d_v062_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_63d_v062_signal},    "f09_markdown_risk_cor_z_63d_v063_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_63d_v063_signal},    "f09_markdown_risk_margin_erosion_z_63d_v064_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_63d_v064_signal},    "f09_markdown_risk_grossmargin_z_126d_v065_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_126d_v065_signal},    "f09_markdown_risk_revenue_z_126d_v066_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_126d_v066_signal},    "f09_markdown_risk_cor_z_126d_v067_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_126d_v067_signal},    "f09_markdown_risk_margin_erosion_z_126d_v068_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_126d_v068_signal},    "f09_markdown_risk_grossmargin_z_252d_v069_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_252d_v069_signal},    "f09_markdown_risk_revenue_z_252d_v070_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_252d_v070_signal},    "f09_markdown_risk_cor_z_252d_v071_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_252d_v071_signal},    "f09_markdown_risk_margin_erosion_z_252d_v072_signal": {"inputs": [], "func": f09_markdown_risk_margin_erosion_z_252d_v072_signal},    "f09_markdown_risk_grossmargin_z_504d_v073_signal": {"inputs": [], "func": f09_markdown_risk_grossmargin_z_504d_v073_signal},    "f09_markdown_risk_revenue_z_504d_v074_signal": {"inputs": [], "func": f09_markdown_risk_revenue_z_504d_v074_signal},    "f09_markdown_risk_cor_z_504d_v075_signal": {"inputs": [], "func": f09_markdown_risk_cor_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 09...")
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
