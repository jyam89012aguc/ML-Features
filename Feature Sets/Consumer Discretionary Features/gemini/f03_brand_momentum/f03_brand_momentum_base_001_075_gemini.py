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

def f03_brand_momentum_revenue_base_5d_v001_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_5d_v002_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_5d_v003_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 5d window."""
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_5d_v004_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 5d window."""
    res = _sma(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_5d_v005_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 5d window."""
    res = _sma(_ratio(marketcap, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_10d_v006_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_10d_v007_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_10d_v008_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 10d window."""
    res = _sma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_10d_v009_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 10d window."""
    res = _sma(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_10d_v010_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 10d window."""
    res = _sma(_ratio(marketcap, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_21d_v011_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_21d_v012_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_21d_v013_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 21d window."""
    res = _sma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_21d_v014_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 21d window."""
    res = _sma(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_21d_v015_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 21d window."""
    res = _sma(_ratio(marketcap, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_42d_v016_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_42d_v017_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_42d_v018_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 42d window."""
    res = _sma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_42d_v019_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 42d window."""
    res = _sma(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_42d_v020_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 42d window."""
    res = _sma(_ratio(marketcap, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_63d_v021_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_63d_v022_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_63d_v023_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 63d window."""
    res = _sma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_63d_v024_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 63d window."""
    res = _sma(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_63d_v025_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 63d window."""
    res = _sma(_ratio(marketcap, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_126d_v026_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_126d_v027_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_126d_v028_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 126d window."""
    res = _sma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_126d_v029_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 126d window."""
    res = _sma(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_126d_v030_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 126d window."""
    res = _sma(_ratio(marketcap, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_252d_v031_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_252d_v032_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_252d_v033_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 252d window."""
    res = _sma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_252d_v034_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 252d window."""
    res = _sma(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_252d_v035_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 252d window."""
    res = _sma(_ratio(marketcap, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_504d_v036_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_504d_v037_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_504d_v038_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 504d window."""
    res = _sma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_504d_v039_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 504d window."""
    res = _sma(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_504d_v040_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 504d window."""
    res = _sma(_ratio(marketcap, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_756d_v041_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_756d_v042_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_756d_v043_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 756d window."""
    res = _sma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_756d_v044_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 756d window."""
    res = _sma(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_756d_v045_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 756d window."""
    res = _sma(_ratio(marketcap, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_1008d_v046_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_1008d_v047_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_1008d_v048_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 1008d window."""
    res = _sma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_1008d_v049_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 1008d window."""
    res = _sma(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_1008d_v050_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 1008d window."""
    res = _sma(_ratio(marketcap, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_base_1260d_v051_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_base_1260d_v052_signal(sgna):
    """Moving average to smooth noise of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_base_1260d_v053_signal(marketcap):
    """Moving average to smooth noise of Raw level of marketcap over 1260d window."""
    res = _sma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_base_1260d_v054_signal(revenue, sgna):
    """Moving average to smooth noise of Sales generated per dollar of marketing/admin over 1260d window."""
    res = _sma(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_base_1260d_v055_signal(marketcap, revenue):
    """Moving average to smooth noise of Valuation ascribed per unit of sales over 1260d window."""
    res = _sma(_ratio(marketcap, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_5d_v056_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_5d_v057_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 5d window."""
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_5d_v058_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 5d window."""
    res = _z(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_5d_v059_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 5d window."""
    res = _z(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_5d_v060_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 5d window."""
    res = _z(_ratio(marketcap, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_10d_v061_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_10d_v062_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 10d window."""
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_10d_v063_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 10d window."""
    res = _z(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_10d_v064_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 10d window."""
    res = _z(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_10d_v065_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 10d window."""
    res = _z(_ratio(marketcap, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_21d_v066_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_21d_v067_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 21d window."""
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_21d_v068_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 21d window."""
    res = _z(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_21d_v069_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 21d window."""
    res = _z(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_21d_v070_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 21d window."""
    res = _z(_ratio(marketcap, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_42d_v071_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_42d_v072_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 42d window."""
    res = _z(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_42d_v073_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 42d window."""
    res = _z(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_42d_v074_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 42d window."""
    res = _z(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_42d_v075_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 42d window."""
    res = _z(_ratio(marketcap, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_brand_momentum_revenue_base_5d_v001_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_5d_v001_signal},    "f03_brand_momentum_sgna_base_5d_v002_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_5d_v002_signal},    "f03_brand_momentum_marketcap_base_5d_v003_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_5d_v003_signal},    "f03_brand_momentum_brand_leverage_base_5d_v004_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_5d_v004_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_5d_v005_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_5d_v005_signal},    "f03_brand_momentum_revenue_base_10d_v006_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_10d_v006_signal},    "f03_brand_momentum_sgna_base_10d_v007_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_10d_v007_signal},    "f03_brand_momentum_marketcap_base_10d_v008_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_10d_v008_signal},    "f03_brand_momentum_brand_leverage_base_10d_v009_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_10d_v009_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_10d_v010_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_10d_v010_signal},    "f03_brand_momentum_revenue_base_21d_v011_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_21d_v011_signal},    "f03_brand_momentum_sgna_base_21d_v012_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_21d_v012_signal},    "f03_brand_momentum_marketcap_base_21d_v013_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_21d_v013_signal},    "f03_brand_momentum_brand_leverage_base_21d_v014_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_21d_v014_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_21d_v015_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_21d_v015_signal},    "f03_brand_momentum_revenue_base_42d_v016_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_42d_v016_signal},    "f03_brand_momentum_sgna_base_42d_v017_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_42d_v017_signal},    "f03_brand_momentum_marketcap_base_42d_v018_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_42d_v018_signal},    "f03_brand_momentum_brand_leverage_base_42d_v019_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_42d_v019_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_42d_v020_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_42d_v020_signal},    "f03_brand_momentum_revenue_base_63d_v021_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_63d_v021_signal},    "f03_brand_momentum_sgna_base_63d_v022_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_63d_v022_signal},    "f03_brand_momentum_marketcap_base_63d_v023_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_63d_v023_signal},    "f03_brand_momentum_brand_leverage_base_63d_v024_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_63d_v024_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_63d_v025_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_63d_v025_signal},    "f03_brand_momentum_revenue_base_126d_v026_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_126d_v026_signal},    "f03_brand_momentum_sgna_base_126d_v027_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_126d_v027_signal},    "f03_brand_momentum_marketcap_base_126d_v028_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_126d_v028_signal},    "f03_brand_momentum_brand_leverage_base_126d_v029_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_126d_v029_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_126d_v030_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_126d_v030_signal},    "f03_brand_momentum_revenue_base_252d_v031_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_252d_v031_signal},    "f03_brand_momentum_sgna_base_252d_v032_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_252d_v032_signal},    "f03_brand_momentum_marketcap_base_252d_v033_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_252d_v033_signal},    "f03_brand_momentum_brand_leverage_base_252d_v034_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_252d_v034_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_252d_v035_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_252d_v035_signal},    "f03_brand_momentum_revenue_base_504d_v036_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_504d_v036_signal},    "f03_brand_momentum_sgna_base_504d_v037_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_504d_v037_signal},    "f03_brand_momentum_marketcap_base_504d_v038_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_504d_v038_signal},    "f03_brand_momentum_brand_leverage_base_504d_v039_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_504d_v039_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_504d_v040_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_504d_v040_signal},    "f03_brand_momentum_revenue_base_756d_v041_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_756d_v041_signal},    "f03_brand_momentum_sgna_base_756d_v042_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_756d_v042_signal},    "f03_brand_momentum_marketcap_base_756d_v043_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_756d_v043_signal},    "f03_brand_momentum_brand_leverage_base_756d_v044_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_756d_v044_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_756d_v045_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_756d_v045_signal},    "f03_brand_momentum_revenue_base_1008d_v046_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_1008d_v046_signal},    "f03_brand_momentum_sgna_base_1008d_v047_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_1008d_v047_signal},    "f03_brand_momentum_marketcap_base_1008d_v048_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_1008d_v048_signal},    "f03_brand_momentum_brand_leverage_base_1008d_v049_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_1008d_v049_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_1008d_v050_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_1008d_v050_signal},    "f03_brand_momentum_revenue_base_1260d_v051_signal": {"inputs": [], "func": f03_brand_momentum_revenue_base_1260d_v051_signal},    "f03_brand_momentum_sgna_base_1260d_v052_signal": {"inputs": [], "func": f03_brand_momentum_sgna_base_1260d_v052_signal},    "f03_brand_momentum_marketcap_base_1260d_v053_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_base_1260d_v053_signal},    "f03_brand_momentum_brand_leverage_base_1260d_v054_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_base_1260d_v054_signal},    "f03_brand_momentum_mkt_cap_per_rev_base_1260d_v055_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_base_1260d_v055_signal},    "f03_brand_momentum_revenue_z_5d_v056_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_5d_v056_signal},    "f03_brand_momentum_sgna_z_5d_v057_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_5d_v057_signal},    "f03_brand_momentum_marketcap_z_5d_v058_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_5d_v058_signal},    "f03_brand_momentum_brand_leverage_z_5d_v059_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_5d_v059_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_5d_v060_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_5d_v060_signal},    "f03_brand_momentum_revenue_z_10d_v061_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_10d_v061_signal},    "f03_brand_momentum_sgna_z_10d_v062_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_10d_v062_signal},    "f03_brand_momentum_marketcap_z_10d_v063_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_10d_v063_signal},    "f03_brand_momentum_brand_leverage_z_10d_v064_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_10d_v064_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_10d_v065_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_10d_v065_signal},    "f03_brand_momentum_revenue_z_21d_v066_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_21d_v066_signal},    "f03_brand_momentum_sgna_z_21d_v067_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_21d_v067_signal},    "f03_brand_momentum_marketcap_z_21d_v068_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_21d_v068_signal},    "f03_brand_momentum_brand_leverage_z_21d_v069_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_21d_v069_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_21d_v070_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_21d_v070_signal},    "f03_brand_momentum_revenue_z_42d_v071_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_42d_v071_signal},    "f03_brand_momentum_sgna_z_42d_v072_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_42d_v072_signal},    "f03_brand_momentum_marketcap_z_42d_v073_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_42d_v073_signal},    "f03_brand_momentum_brand_leverage_z_42d_v074_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_42d_v074_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_42d_v075_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_42d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
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
