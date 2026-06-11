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

def f31_specialty_roe_netinc_base_5d_v001_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_5d_v002_signal(equity):
    """Moving average of Raw level of equity over 5d window."""
    res = _sma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_5d_v003_signal(roic):
    """Moving average of Raw level of roic over 5d window."""
    res = _sma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_5d_v004_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 5d window."""
    res = _sma(_ratio(netinc, equity) * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_10d_v005_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_10d_v006_signal(equity):
    """Moving average of Raw level of equity over 10d window."""
    res = _sma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_10d_v007_signal(roic):
    """Moving average of Raw level of roic over 10d window."""
    res = _sma(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_10d_v008_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 10d window."""
    res = _sma(_ratio(netinc, equity) * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_21d_v009_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_21d_v010_signal(equity):
    """Moving average of Raw level of equity over 21d window."""
    res = _sma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_21d_v011_signal(roic):
    """Moving average of Raw level of roic over 21d window."""
    res = _sma(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_21d_v012_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 21d window."""
    res = _sma(_ratio(netinc, equity) * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_42d_v013_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_42d_v014_signal(equity):
    """Moving average of Raw level of equity over 42d window."""
    res = _sma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_42d_v015_signal(roic):
    """Moving average of Raw level of roic over 42d window."""
    res = _sma(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_42d_v016_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 42d window."""
    res = _sma(_ratio(netinc, equity) * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_63d_v017_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_63d_v018_signal(equity):
    """Moving average of Raw level of equity over 63d window."""
    res = _sma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_63d_v019_signal(roic):
    """Moving average of Raw level of roic over 63d window."""
    res = _sma(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_63d_v020_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 63d window."""
    res = _sma(_ratio(netinc, equity) * roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_126d_v021_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_126d_v022_signal(equity):
    """Moving average of Raw level of equity over 126d window."""
    res = _sma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_126d_v023_signal(roic):
    """Moving average of Raw level of roic over 126d window."""
    res = _sma(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_126d_v024_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 126d window."""
    res = _sma(_ratio(netinc, equity) * roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_252d_v025_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_252d_v026_signal(equity):
    """Moving average of Raw level of equity over 252d window."""
    res = _sma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_252d_v027_signal(roic):
    """Moving average of Raw level of roic over 252d window."""
    res = _sma(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_252d_v028_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 252d window."""
    res = _sma(_ratio(netinc, equity) * roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_504d_v029_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_504d_v030_signal(equity):
    """Moving average of Raw level of equity over 504d window."""
    res = _sma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_504d_v031_signal(roic):
    """Moving average of Raw level of roic over 504d window."""
    res = _sma(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_504d_v032_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 504d window."""
    res = _sma(_ratio(netinc, equity) * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_756d_v033_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_756d_v034_signal(equity):
    """Moving average of Raw level of equity over 756d window."""
    res = _sma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_756d_v035_signal(roic):
    """Moving average of Raw level of roic over 756d window."""
    res = _sma(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_756d_v036_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 756d window."""
    res = _sma(_ratio(netinc, equity) * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_1008d_v037_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_1008d_v038_signal(equity):
    """Moving average of Raw level of equity over 1008d window."""
    res = _sma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_1008d_v039_signal(roic):
    """Moving average of Raw level of roic over 1008d window."""
    res = _sma(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_1008d_v040_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 1008d window."""
    res = _sma(_ratio(netinc, equity) * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_base_1260d_v041_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_base_1260d_v042_signal(equity):
    """Moving average of Raw level of equity over 1260d window."""
    res = _sma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_base_1260d_v043_signal(roic):
    """Moving average of Raw level of roic over 1260d window."""
    res = _sma(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_base_1260d_v044_signal(netinc, equity, roic):
    """Moving average of ROIC-amplified ROE over 1260d window."""
    res = _sma(_ratio(netinc, equity) * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_5d_v045_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_5d_v046_signal(equity):
    """Exponential moving average of Raw level of equity over 5d window."""
    res = _ewma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_5d_v047_signal(roic):
    """Exponential moving average of Raw level of roic over 5d window."""
    res = _ewma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_5d_v048_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 5d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_10d_v049_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_10d_v050_signal(equity):
    """Exponential moving average of Raw level of equity over 10d window."""
    res = _ewma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_10d_v051_signal(roic):
    """Exponential moving average of Raw level of roic over 10d window."""
    res = _ewma(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_10d_v052_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 10d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_21d_v053_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_21d_v054_signal(equity):
    """Exponential moving average of Raw level of equity over 21d window."""
    res = _ewma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_21d_v055_signal(roic):
    """Exponential moving average of Raw level of roic over 21d window."""
    res = _ewma(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_21d_v056_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 21d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_42d_v057_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_42d_v058_signal(equity):
    """Exponential moving average of Raw level of equity over 42d window."""
    res = _ewma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_42d_v059_signal(roic):
    """Exponential moving average of Raw level of roic over 42d window."""
    res = _ewma(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_42d_v060_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 42d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_63d_v061_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_63d_v062_signal(equity):
    """Exponential moving average of Raw level of equity over 63d window."""
    res = _ewma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_63d_v063_signal(roic):
    """Exponential moving average of Raw level of roic over 63d window."""
    res = _ewma(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_63d_v064_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 63d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_126d_v065_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_126d_v066_signal(equity):
    """Exponential moving average of Raw level of equity over 126d window."""
    res = _ewma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_126d_v067_signal(roic):
    """Exponential moving average of Raw level of roic over 126d window."""
    res = _ewma(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_126d_v068_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 126d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_252d_v069_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_252d_v070_signal(equity):
    """Exponential moving average of Raw level of equity over 252d window."""
    res = _ewma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_252d_v071_signal(roic):
    """Exponential moving average of Raw level of roic over 252d window."""
    res = _ewma(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_252d_v072_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 252d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_504d_v073_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_504d_v074_signal(equity):
    """Exponential moving average of Raw level of equity over 504d window."""
    res = _ewma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_504d_v075_signal(roic):
    """Exponential moving average of Raw level of roic over 504d window."""
    res = _ewma(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f31_specialty_roe_netinc_base_5d_v001_signal": {"func": f31_specialty_roe_netinc_base_5d_v001_signal},
    "f31_specialty_roe_equity_base_5d_v002_signal": {"func": f31_specialty_roe_equity_base_5d_v002_signal},
    "f31_specialty_roe_roic_base_5d_v003_signal": {"func": f31_specialty_roe_roic_base_5d_v003_signal},
    "f31_specialty_roe_adjusted_roe_base_5d_v004_signal": {"func": f31_specialty_roe_adjusted_roe_base_5d_v004_signal},
    "f31_specialty_roe_netinc_base_10d_v005_signal": {"func": f31_specialty_roe_netinc_base_10d_v005_signal},
    "f31_specialty_roe_equity_base_10d_v006_signal": {"func": f31_specialty_roe_equity_base_10d_v006_signal},
    "f31_specialty_roe_roic_base_10d_v007_signal": {"func": f31_specialty_roe_roic_base_10d_v007_signal},
    "f31_specialty_roe_adjusted_roe_base_10d_v008_signal": {"func": f31_specialty_roe_adjusted_roe_base_10d_v008_signal},
    "f31_specialty_roe_netinc_base_21d_v009_signal": {"func": f31_specialty_roe_netinc_base_21d_v009_signal},
    "f31_specialty_roe_equity_base_21d_v010_signal": {"func": f31_specialty_roe_equity_base_21d_v010_signal},
    "f31_specialty_roe_roic_base_21d_v011_signal": {"func": f31_specialty_roe_roic_base_21d_v011_signal},
    "f31_specialty_roe_adjusted_roe_base_21d_v012_signal": {"func": f31_specialty_roe_adjusted_roe_base_21d_v012_signal},
    "f31_specialty_roe_netinc_base_42d_v013_signal": {"func": f31_specialty_roe_netinc_base_42d_v013_signal},
    "f31_specialty_roe_equity_base_42d_v014_signal": {"func": f31_specialty_roe_equity_base_42d_v014_signal},
    "f31_specialty_roe_roic_base_42d_v015_signal": {"func": f31_specialty_roe_roic_base_42d_v015_signal},
    "f31_specialty_roe_adjusted_roe_base_42d_v016_signal": {"func": f31_specialty_roe_adjusted_roe_base_42d_v016_signal},
    "f31_specialty_roe_netinc_base_63d_v017_signal": {"func": f31_specialty_roe_netinc_base_63d_v017_signal},
    "f31_specialty_roe_equity_base_63d_v018_signal": {"func": f31_specialty_roe_equity_base_63d_v018_signal},
    "f31_specialty_roe_roic_base_63d_v019_signal": {"func": f31_specialty_roe_roic_base_63d_v019_signal},
    "f31_specialty_roe_adjusted_roe_base_63d_v020_signal": {"func": f31_specialty_roe_adjusted_roe_base_63d_v020_signal},
    "f31_specialty_roe_netinc_base_126d_v021_signal": {"func": f31_specialty_roe_netinc_base_126d_v021_signal},
    "f31_specialty_roe_equity_base_126d_v022_signal": {"func": f31_specialty_roe_equity_base_126d_v022_signal},
    "f31_specialty_roe_roic_base_126d_v023_signal": {"func": f31_specialty_roe_roic_base_126d_v023_signal},
    "f31_specialty_roe_adjusted_roe_base_126d_v024_signal": {"func": f31_specialty_roe_adjusted_roe_base_126d_v024_signal},
    "f31_specialty_roe_netinc_base_252d_v025_signal": {"func": f31_specialty_roe_netinc_base_252d_v025_signal},
    "f31_specialty_roe_equity_base_252d_v026_signal": {"func": f31_specialty_roe_equity_base_252d_v026_signal},
    "f31_specialty_roe_roic_base_252d_v027_signal": {"func": f31_specialty_roe_roic_base_252d_v027_signal},
    "f31_specialty_roe_adjusted_roe_base_252d_v028_signal": {"func": f31_specialty_roe_adjusted_roe_base_252d_v028_signal},
    "f31_specialty_roe_netinc_base_504d_v029_signal": {"func": f31_specialty_roe_netinc_base_504d_v029_signal},
    "f31_specialty_roe_equity_base_504d_v030_signal": {"func": f31_specialty_roe_equity_base_504d_v030_signal},
    "f31_specialty_roe_roic_base_504d_v031_signal": {"func": f31_specialty_roe_roic_base_504d_v031_signal},
    "f31_specialty_roe_adjusted_roe_base_504d_v032_signal": {"func": f31_specialty_roe_adjusted_roe_base_504d_v032_signal},
    "f31_specialty_roe_netinc_base_756d_v033_signal": {"func": f31_specialty_roe_netinc_base_756d_v033_signal},
    "f31_specialty_roe_equity_base_756d_v034_signal": {"func": f31_specialty_roe_equity_base_756d_v034_signal},
    "f31_specialty_roe_roic_base_756d_v035_signal": {"func": f31_specialty_roe_roic_base_756d_v035_signal},
    "f31_specialty_roe_adjusted_roe_base_756d_v036_signal": {"func": f31_specialty_roe_adjusted_roe_base_756d_v036_signal},
    "f31_specialty_roe_netinc_base_1008d_v037_signal": {"func": f31_specialty_roe_netinc_base_1008d_v037_signal},
    "f31_specialty_roe_equity_base_1008d_v038_signal": {"func": f31_specialty_roe_equity_base_1008d_v038_signal},
    "f31_specialty_roe_roic_base_1008d_v039_signal": {"func": f31_specialty_roe_roic_base_1008d_v039_signal},
    "f31_specialty_roe_adjusted_roe_base_1008d_v040_signal": {"func": f31_specialty_roe_adjusted_roe_base_1008d_v040_signal},
    "f31_specialty_roe_netinc_base_1260d_v041_signal": {"func": f31_specialty_roe_netinc_base_1260d_v041_signal},
    "f31_specialty_roe_equity_base_1260d_v042_signal": {"func": f31_specialty_roe_equity_base_1260d_v042_signal},
    "f31_specialty_roe_roic_base_1260d_v043_signal": {"func": f31_specialty_roe_roic_base_1260d_v043_signal},
    "f31_specialty_roe_adjusted_roe_base_1260d_v044_signal": {"func": f31_specialty_roe_adjusted_roe_base_1260d_v044_signal},
    "f31_specialty_roe_netinc_ewma_5d_v045_signal": {"func": f31_specialty_roe_netinc_ewma_5d_v045_signal},
    "f31_specialty_roe_equity_ewma_5d_v046_signal": {"func": f31_specialty_roe_equity_ewma_5d_v046_signal},
    "f31_specialty_roe_roic_ewma_5d_v047_signal": {"func": f31_specialty_roe_roic_ewma_5d_v047_signal},
    "f31_specialty_roe_adjusted_roe_ewma_5d_v048_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_5d_v048_signal},
    "f31_specialty_roe_netinc_ewma_10d_v049_signal": {"func": f31_specialty_roe_netinc_ewma_10d_v049_signal},
    "f31_specialty_roe_equity_ewma_10d_v050_signal": {"func": f31_specialty_roe_equity_ewma_10d_v050_signal},
    "f31_specialty_roe_roic_ewma_10d_v051_signal": {"func": f31_specialty_roe_roic_ewma_10d_v051_signal},
    "f31_specialty_roe_adjusted_roe_ewma_10d_v052_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_10d_v052_signal},
    "f31_specialty_roe_netinc_ewma_21d_v053_signal": {"func": f31_specialty_roe_netinc_ewma_21d_v053_signal},
    "f31_specialty_roe_equity_ewma_21d_v054_signal": {"func": f31_specialty_roe_equity_ewma_21d_v054_signal},
    "f31_specialty_roe_roic_ewma_21d_v055_signal": {"func": f31_specialty_roe_roic_ewma_21d_v055_signal},
    "f31_specialty_roe_adjusted_roe_ewma_21d_v056_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_21d_v056_signal},
    "f31_specialty_roe_netinc_ewma_42d_v057_signal": {"func": f31_specialty_roe_netinc_ewma_42d_v057_signal},
    "f31_specialty_roe_equity_ewma_42d_v058_signal": {"func": f31_specialty_roe_equity_ewma_42d_v058_signal},
    "f31_specialty_roe_roic_ewma_42d_v059_signal": {"func": f31_specialty_roe_roic_ewma_42d_v059_signal},
    "f31_specialty_roe_adjusted_roe_ewma_42d_v060_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_42d_v060_signal},
    "f31_specialty_roe_netinc_ewma_63d_v061_signal": {"func": f31_specialty_roe_netinc_ewma_63d_v061_signal},
    "f31_specialty_roe_equity_ewma_63d_v062_signal": {"func": f31_specialty_roe_equity_ewma_63d_v062_signal},
    "f31_specialty_roe_roic_ewma_63d_v063_signal": {"func": f31_specialty_roe_roic_ewma_63d_v063_signal},
    "f31_specialty_roe_adjusted_roe_ewma_63d_v064_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_63d_v064_signal},
    "f31_specialty_roe_netinc_ewma_126d_v065_signal": {"func": f31_specialty_roe_netinc_ewma_126d_v065_signal},
    "f31_specialty_roe_equity_ewma_126d_v066_signal": {"func": f31_specialty_roe_equity_ewma_126d_v066_signal},
    "f31_specialty_roe_roic_ewma_126d_v067_signal": {"func": f31_specialty_roe_roic_ewma_126d_v067_signal},
    "f31_specialty_roe_adjusted_roe_ewma_126d_v068_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_126d_v068_signal},
    "f31_specialty_roe_netinc_ewma_252d_v069_signal": {"func": f31_specialty_roe_netinc_ewma_252d_v069_signal},
    "f31_specialty_roe_equity_ewma_252d_v070_signal": {"func": f31_specialty_roe_equity_ewma_252d_v070_signal},
    "f31_specialty_roe_roic_ewma_252d_v071_signal": {"func": f31_specialty_roe_roic_ewma_252d_v071_signal},
    "f31_specialty_roe_adjusted_roe_ewma_252d_v072_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_252d_v072_signal},
    "f31_specialty_roe_netinc_ewma_504d_v073_signal": {"func": f31_specialty_roe_netinc_ewma_504d_v073_signal},
    "f31_specialty_roe_equity_ewma_504d_v074_signal": {"func": f31_specialty_roe_equity_ewma_504d_v074_signal},
    "f31_specialty_roe_roic_ewma_504d_v075_signal": {"func": f31_specialty_roe_roic_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 31...")
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
