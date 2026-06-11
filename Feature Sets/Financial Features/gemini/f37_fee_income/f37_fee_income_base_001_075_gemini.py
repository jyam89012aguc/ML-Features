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

def f37_fee_income_revenue_base_5d_v001_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_5d_v002_signal(ebit):
    """Moving average of Raw level of ebit over 5d window."""
    res = _sma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_5d_v003_signal(ebitda):
    """Moving average of Raw level of ebitda over 5d window."""
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_5d_v004_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 5d window."""
    res = _sma(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_10d_v005_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_10d_v006_signal(ebit):
    """Moving average of Raw level of ebit over 10d window."""
    res = _sma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_10d_v007_signal(ebitda):
    """Moving average of Raw level of ebitda over 10d window."""
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_10d_v008_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 10d window."""
    res = _sma(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_21d_v009_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_21d_v010_signal(ebit):
    """Moving average of Raw level of ebit over 21d window."""
    res = _sma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_21d_v011_signal(ebitda):
    """Moving average of Raw level of ebitda over 21d window."""
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_21d_v012_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 21d window."""
    res = _sma(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_42d_v013_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_42d_v014_signal(ebit):
    """Moving average of Raw level of ebit over 42d window."""
    res = _sma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_42d_v015_signal(ebitda):
    """Moving average of Raw level of ebitda over 42d window."""
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_42d_v016_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 42d window."""
    res = _sma(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_63d_v017_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_63d_v018_signal(ebit):
    """Moving average of Raw level of ebit over 63d window."""
    res = _sma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_63d_v019_signal(ebitda):
    """Moving average of Raw level of ebitda over 63d window."""
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_63d_v020_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 63d window."""
    res = _sma(_ratio(ebit, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_126d_v021_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_126d_v022_signal(ebit):
    """Moving average of Raw level of ebit over 126d window."""
    res = _sma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_126d_v023_signal(ebitda):
    """Moving average of Raw level of ebitda over 126d window."""
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_126d_v024_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 126d window."""
    res = _sma(_ratio(ebit, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_252d_v025_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_252d_v026_signal(ebit):
    """Moving average of Raw level of ebit over 252d window."""
    res = _sma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_252d_v027_signal(ebitda):
    """Moving average of Raw level of ebitda over 252d window."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_252d_v028_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 252d window."""
    res = _sma(_ratio(ebit, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_504d_v029_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_504d_v030_signal(ebit):
    """Moving average of Raw level of ebit over 504d window."""
    res = _sma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_504d_v031_signal(ebitda):
    """Moving average of Raw level of ebitda over 504d window."""
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_504d_v032_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 504d window."""
    res = _sma(_ratio(ebit, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_756d_v033_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_756d_v034_signal(ebit):
    """Moving average of Raw level of ebit over 756d window."""
    res = _sma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_756d_v035_signal(ebitda):
    """Moving average of Raw level of ebitda over 756d window."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_756d_v036_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 756d window."""
    res = _sma(_ratio(ebit, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_1008d_v037_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_1008d_v038_signal(ebit):
    """Moving average of Raw level of ebit over 1008d window."""
    res = _sma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_1008d_v039_signal(ebitda):
    """Moving average of Raw level of ebitda over 1008d window."""
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_1008d_v040_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 1008d window."""
    res = _sma(_ratio(ebit, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_base_1260d_v041_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_base_1260d_v042_signal(ebit):
    """Moving average of Raw level of ebit over 1260d window."""
    res = _sma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_base_1260d_v043_signal(ebitda):
    """Moving average of Raw level of ebitda over 1260d window."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_base_1260d_v044_signal(ebit, ebitda):
    """Moving average of Operating-to-EBITDA conversion over 1260d window."""
    res = _sma(_ratio(ebit, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_5d_v045_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_5d_v046_signal(ebit):
    """Exponential moving average of Raw level of ebit over 5d window."""
    res = _ewma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_5d_v047_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 5d window."""
    res = _ewma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_5d_v048_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 5d window."""
    res = _ewma(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_10d_v049_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_10d_v050_signal(ebit):
    """Exponential moving average of Raw level of ebit over 10d window."""
    res = _ewma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_10d_v051_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 10d window."""
    res = _ewma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_10d_v052_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 10d window."""
    res = _ewma(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_21d_v053_signal(revenue):
    """Exponential moving average of Raw level of revenue over 21d window."""
    res = _ewma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_21d_v054_signal(ebit):
    """Exponential moving average of Raw level of ebit over 21d window."""
    res = _ewma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_21d_v055_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 21d window."""
    res = _ewma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_21d_v056_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 21d window."""
    res = _ewma(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_42d_v057_signal(revenue):
    """Exponential moving average of Raw level of revenue over 42d window."""
    res = _ewma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_42d_v058_signal(ebit):
    """Exponential moving average of Raw level of ebit over 42d window."""
    res = _ewma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_42d_v059_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 42d window."""
    res = _ewma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_42d_v060_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 42d window."""
    res = _ewma(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_63d_v061_signal(revenue):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_63d_v062_signal(ebit):
    """Exponential moving average of Raw level of ebit over 63d window."""
    res = _ewma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_63d_v063_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 63d window."""
    res = _ewma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_63d_v064_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 63d window."""
    res = _ewma(_ratio(ebit, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_126d_v065_signal(revenue):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_126d_v066_signal(ebit):
    """Exponential moving average of Raw level of ebit over 126d window."""
    res = _ewma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_126d_v067_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 126d window."""
    res = _ewma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_126d_v068_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 126d window."""
    res = _ewma(_ratio(ebit, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_252d_v069_signal(revenue):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_252d_v070_signal(ebit):
    """Exponential moving average of Raw level of ebit over 252d window."""
    res = _ewma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_252d_v071_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 252d window."""
    res = _ewma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_operating_conversion_ewma_252d_v072_signal(ebit, ebitda):
    """Exponential moving average of Operating-to-EBITDA conversion over 252d window."""
    res = _ewma(_ratio(ebit, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_revenue_ewma_504d_v073_signal(revenue):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebit_ewma_504d_v074_signal(ebit):
    """Exponential moving average of Raw level of ebit over 504d window."""
    res = _ewma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f37_fee_income_ebitda_ewma_504d_v075_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 504d window."""
    res = _ewma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f37_fee_income_revenue_base_5d_v001_signal": {"func": f37_fee_income_revenue_base_5d_v001_signal},
    "f37_fee_income_ebit_base_5d_v002_signal": {"func": f37_fee_income_ebit_base_5d_v002_signal},
    "f37_fee_income_ebitda_base_5d_v003_signal": {"func": f37_fee_income_ebitda_base_5d_v003_signal},
    "f37_fee_income_operating_conversion_base_5d_v004_signal": {"func": f37_fee_income_operating_conversion_base_5d_v004_signal},
    "f37_fee_income_revenue_base_10d_v005_signal": {"func": f37_fee_income_revenue_base_10d_v005_signal},
    "f37_fee_income_ebit_base_10d_v006_signal": {"func": f37_fee_income_ebit_base_10d_v006_signal},
    "f37_fee_income_ebitda_base_10d_v007_signal": {"func": f37_fee_income_ebitda_base_10d_v007_signal},
    "f37_fee_income_operating_conversion_base_10d_v008_signal": {"func": f37_fee_income_operating_conversion_base_10d_v008_signal},
    "f37_fee_income_revenue_base_21d_v009_signal": {"func": f37_fee_income_revenue_base_21d_v009_signal},
    "f37_fee_income_ebit_base_21d_v010_signal": {"func": f37_fee_income_ebit_base_21d_v010_signal},
    "f37_fee_income_ebitda_base_21d_v011_signal": {"func": f37_fee_income_ebitda_base_21d_v011_signal},
    "f37_fee_income_operating_conversion_base_21d_v012_signal": {"func": f37_fee_income_operating_conversion_base_21d_v012_signal},
    "f37_fee_income_revenue_base_42d_v013_signal": {"func": f37_fee_income_revenue_base_42d_v013_signal},
    "f37_fee_income_ebit_base_42d_v014_signal": {"func": f37_fee_income_ebit_base_42d_v014_signal},
    "f37_fee_income_ebitda_base_42d_v015_signal": {"func": f37_fee_income_ebitda_base_42d_v015_signal},
    "f37_fee_income_operating_conversion_base_42d_v016_signal": {"func": f37_fee_income_operating_conversion_base_42d_v016_signal},
    "f37_fee_income_revenue_base_63d_v017_signal": {"func": f37_fee_income_revenue_base_63d_v017_signal},
    "f37_fee_income_ebit_base_63d_v018_signal": {"func": f37_fee_income_ebit_base_63d_v018_signal},
    "f37_fee_income_ebitda_base_63d_v019_signal": {"func": f37_fee_income_ebitda_base_63d_v019_signal},
    "f37_fee_income_operating_conversion_base_63d_v020_signal": {"func": f37_fee_income_operating_conversion_base_63d_v020_signal},
    "f37_fee_income_revenue_base_126d_v021_signal": {"func": f37_fee_income_revenue_base_126d_v021_signal},
    "f37_fee_income_ebit_base_126d_v022_signal": {"func": f37_fee_income_ebit_base_126d_v022_signal},
    "f37_fee_income_ebitda_base_126d_v023_signal": {"func": f37_fee_income_ebitda_base_126d_v023_signal},
    "f37_fee_income_operating_conversion_base_126d_v024_signal": {"func": f37_fee_income_operating_conversion_base_126d_v024_signal},
    "f37_fee_income_revenue_base_252d_v025_signal": {"func": f37_fee_income_revenue_base_252d_v025_signal},
    "f37_fee_income_ebit_base_252d_v026_signal": {"func": f37_fee_income_ebit_base_252d_v026_signal},
    "f37_fee_income_ebitda_base_252d_v027_signal": {"func": f37_fee_income_ebitda_base_252d_v027_signal},
    "f37_fee_income_operating_conversion_base_252d_v028_signal": {"func": f37_fee_income_operating_conversion_base_252d_v028_signal},
    "f37_fee_income_revenue_base_504d_v029_signal": {"func": f37_fee_income_revenue_base_504d_v029_signal},
    "f37_fee_income_ebit_base_504d_v030_signal": {"func": f37_fee_income_ebit_base_504d_v030_signal},
    "f37_fee_income_ebitda_base_504d_v031_signal": {"func": f37_fee_income_ebitda_base_504d_v031_signal},
    "f37_fee_income_operating_conversion_base_504d_v032_signal": {"func": f37_fee_income_operating_conversion_base_504d_v032_signal},
    "f37_fee_income_revenue_base_756d_v033_signal": {"func": f37_fee_income_revenue_base_756d_v033_signal},
    "f37_fee_income_ebit_base_756d_v034_signal": {"func": f37_fee_income_ebit_base_756d_v034_signal},
    "f37_fee_income_ebitda_base_756d_v035_signal": {"func": f37_fee_income_ebitda_base_756d_v035_signal},
    "f37_fee_income_operating_conversion_base_756d_v036_signal": {"func": f37_fee_income_operating_conversion_base_756d_v036_signal},
    "f37_fee_income_revenue_base_1008d_v037_signal": {"func": f37_fee_income_revenue_base_1008d_v037_signal},
    "f37_fee_income_ebit_base_1008d_v038_signal": {"func": f37_fee_income_ebit_base_1008d_v038_signal},
    "f37_fee_income_ebitda_base_1008d_v039_signal": {"func": f37_fee_income_ebitda_base_1008d_v039_signal},
    "f37_fee_income_operating_conversion_base_1008d_v040_signal": {"func": f37_fee_income_operating_conversion_base_1008d_v040_signal},
    "f37_fee_income_revenue_base_1260d_v041_signal": {"func": f37_fee_income_revenue_base_1260d_v041_signal},
    "f37_fee_income_ebit_base_1260d_v042_signal": {"func": f37_fee_income_ebit_base_1260d_v042_signal},
    "f37_fee_income_ebitda_base_1260d_v043_signal": {"func": f37_fee_income_ebitda_base_1260d_v043_signal},
    "f37_fee_income_operating_conversion_base_1260d_v044_signal": {"func": f37_fee_income_operating_conversion_base_1260d_v044_signal},
    "f37_fee_income_revenue_ewma_5d_v045_signal": {"func": f37_fee_income_revenue_ewma_5d_v045_signal},
    "f37_fee_income_ebit_ewma_5d_v046_signal": {"func": f37_fee_income_ebit_ewma_5d_v046_signal},
    "f37_fee_income_ebitda_ewma_5d_v047_signal": {"func": f37_fee_income_ebitda_ewma_5d_v047_signal},
    "f37_fee_income_operating_conversion_ewma_5d_v048_signal": {"func": f37_fee_income_operating_conversion_ewma_5d_v048_signal},
    "f37_fee_income_revenue_ewma_10d_v049_signal": {"func": f37_fee_income_revenue_ewma_10d_v049_signal},
    "f37_fee_income_ebit_ewma_10d_v050_signal": {"func": f37_fee_income_ebit_ewma_10d_v050_signal},
    "f37_fee_income_ebitda_ewma_10d_v051_signal": {"func": f37_fee_income_ebitda_ewma_10d_v051_signal},
    "f37_fee_income_operating_conversion_ewma_10d_v052_signal": {"func": f37_fee_income_operating_conversion_ewma_10d_v052_signal},
    "f37_fee_income_revenue_ewma_21d_v053_signal": {"func": f37_fee_income_revenue_ewma_21d_v053_signal},
    "f37_fee_income_ebit_ewma_21d_v054_signal": {"func": f37_fee_income_ebit_ewma_21d_v054_signal},
    "f37_fee_income_ebitda_ewma_21d_v055_signal": {"func": f37_fee_income_ebitda_ewma_21d_v055_signal},
    "f37_fee_income_operating_conversion_ewma_21d_v056_signal": {"func": f37_fee_income_operating_conversion_ewma_21d_v056_signal},
    "f37_fee_income_revenue_ewma_42d_v057_signal": {"func": f37_fee_income_revenue_ewma_42d_v057_signal},
    "f37_fee_income_ebit_ewma_42d_v058_signal": {"func": f37_fee_income_ebit_ewma_42d_v058_signal},
    "f37_fee_income_ebitda_ewma_42d_v059_signal": {"func": f37_fee_income_ebitda_ewma_42d_v059_signal},
    "f37_fee_income_operating_conversion_ewma_42d_v060_signal": {"func": f37_fee_income_operating_conversion_ewma_42d_v060_signal},
    "f37_fee_income_revenue_ewma_63d_v061_signal": {"func": f37_fee_income_revenue_ewma_63d_v061_signal},
    "f37_fee_income_ebit_ewma_63d_v062_signal": {"func": f37_fee_income_ebit_ewma_63d_v062_signal},
    "f37_fee_income_ebitda_ewma_63d_v063_signal": {"func": f37_fee_income_ebitda_ewma_63d_v063_signal},
    "f37_fee_income_operating_conversion_ewma_63d_v064_signal": {"func": f37_fee_income_operating_conversion_ewma_63d_v064_signal},
    "f37_fee_income_revenue_ewma_126d_v065_signal": {"func": f37_fee_income_revenue_ewma_126d_v065_signal},
    "f37_fee_income_ebit_ewma_126d_v066_signal": {"func": f37_fee_income_ebit_ewma_126d_v066_signal},
    "f37_fee_income_ebitda_ewma_126d_v067_signal": {"func": f37_fee_income_ebitda_ewma_126d_v067_signal},
    "f37_fee_income_operating_conversion_ewma_126d_v068_signal": {"func": f37_fee_income_operating_conversion_ewma_126d_v068_signal},
    "f37_fee_income_revenue_ewma_252d_v069_signal": {"func": f37_fee_income_revenue_ewma_252d_v069_signal},
    "f37_fee_income_ebit_ewma_252d_v070_signal": {"func": f37_fee_income_ebit_ewma_252d_v070_signal},
    "f37_fee_income_ebitda_ewma_252d_v071_signal": {"func": f37_fee_income_ebitda_ewma_252d_v071_signal},
    "f37_fee_income_operating_conversion_ewma_252d_v072_signal": {"func": f37_fee_income_operating_conversion_ewma_252d_v072_signal},
    "f37_fee_income_revenue_ewma_504d_v073_signal": {"func": f37_fee_income_revenue_ewma_504d_v073_signal},
    "f37_fee_income_ebit_ewma_504d_v074_signal": {"func": f37_fee_income_ebit_ewma_504d_v074_signal},
    "f37_fee_income_ebitda_ewma_504d_v075_signal": {"func": f37_fee_income_ebitda_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 37...")
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
