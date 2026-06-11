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

def f47_roic_compounder_fin_roic_base_5d_v001_signal(roic):
    """Moving average of Raw level of roic over 5d window."""
    res = _sma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_5d_v002_signal(invcap):
    """Moving average of Raw level of invcap over 5d window."""
    res = _sma(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_5d_v003_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_5d_v004_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 5d window."""
    res = _sma(_std(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_10d_v005_signal(roic):
    """Moving average of Raw level of roic over 10d window."""
    res = _sma(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_10d_v006_signal(invcap):
    """Moving average of Raw level of invcap over 10d window."""
    res = _sma(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_10d_v007_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_10d_v008_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 10d window."""
    res = _sma(_std(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_21d_v009_signal(roic):
    """Moving average of Raw level of roic over 21d window."""
    res = _sma(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_21d_v010_signal(invcap):
    """Moving average of Raw level of invcap over 21d window."""
    res = _sma(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_21d_v011_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_21d_v012_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 21d window."""
    res = _sma(_std(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_42d_v013_signal(roic):
    """Moving average of Raw level of roic over 42d window."""
    res = _sma(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_42d_v014_signal(invcap):
    """Moving average of Raw level of invcap over 42d window."""
    res = _sma(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_42d_v015_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_42d_v016_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 42d window."""
    res = _sma(_std(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_63d_v017_signal(roic):
    """Moving average of Raw level of roic over 63d window."""
    res = _sma(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_63d_v018_signal(invcap):
    """Moving average of Raw level of invcap over 63d window."""
    res = _sma(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_63d_v019_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_63d_v020_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 63d window."""
    res = _sma(_std(roic, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_126d_v021_signal(roic):
    """Moving average of Raw level of roic over 126d window."""
    res = _sma(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_126d_v022_signal(invcap):
    """Moving average of Raw level of invcap over 126d window."""
    res = _sma(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_126d_v023_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_126d_v024_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 126d window."""
    res = _sma(_std(roic, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_252d_v025_signal(roic):
    """Moving average of Raw level of roic over 252d window."""
    res = _sma(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_252d_v026_signal(invcap):
    """Moving average of Raw level of invcap over 252d window."""
    res = _sma(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_252d_v027_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_252d_v028_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 252d window."""
    res = _sma(_std(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_504d_v029_signal(roic):
    """Moving average of Raw level of roic over 504d window."""
    res = _sma(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_504d_v030_signal(invcap):
    """Moving average of Raw level of invcap over 504d window."""
    res = _sma(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_504d_v031_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_504d_v032_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 504d window."""
    res = _sma(_std(roic, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_756d_v033_signal(roic):
    """Moving average of Raw level of roic over 756d window."""
    res = _sma(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_756d_v034_signal(invcap):
    """Moving average of Raw level of invcap over 756d window."""
    res = _sma(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_756d_v035_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_756d_v036_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 756d window."""
    res = _sma(_std(roic, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_1008d_v037_signal(roic):
    """Moving average of Raw level of roic over 1008d window."""
    res = _sma(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_1008d_v038_signal(invcap):
    """Moving average of Raw level of invcap over 1008d window."""
    res = _sma(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_1008d_v039_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_1008d_v040_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 1008d window."""
    res = _sma(_std(roic, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_base_1260d_v041_signal(roic):
    """Moving average of Raw level of roic over 1260d window."""
    res = _sma(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_base_1260d_v042_signal(invcap):
    """Moving average of Raw level of invcap over 1260d window."""
    res = _sma(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_base_1260d_v043_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_base_1260d_v044_signal(roic):
    """Moving average of ROIC stability (standard deviation) over 1260d window."""
    res = _sma(_std(roic, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_5d_v045_signal(roic):
    """Exponential moving average of Raw level of roic over 5d window."""
    res = _ewma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_5d_v046_signal(invcap):
    """Exponential moving average of Raw level of invcap over 5d window."""
    res = _ewma(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_5d_v047_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_5d_v048_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 5d window."""
    res = _ewma(_std(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_10d_v049_signal(roic):
    """Exponential moving average of Raw level of roic over 10d window."""
    res = _ewma(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_10d_v050_signal(invcap):
    """Exponential moving average of Raw level of invcap over 10d window."""
    res = _ewma(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_10d_v051_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_10d_v052_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 10d window."""
    res = _ewma(_std(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_21d_v053_signal(roic):
    """Exponential moving average of Raw level of roic over 21d window."""
    res = _ewma(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_21d_v054_signal(invcap):
    """Exponential moving average of Raw level of invcap over 21d window."""
    res = _ewma(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_21d_v055_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_21d_v056_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 21d window."""
    res = _ewma(_std(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_42d_v057_signal(roic):
    """Exponential moving average of Raw level of roic over 42d window."""
    res = _ewma(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_42d_v058_signal(invcap):
    """Exponential moving average of Raw level of invcap over 42d window."""
    res = _ewma(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_42d_v059_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_42d_v060_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 42d window."""
    res = _ewma(_std(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_63d_v061_signal(roic):
    """Exponential moving average of Raw level of roic over 63d window."""
    res = _ewma(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_63d_v062_signal(invcap):
    """Exponential moving average of Raw level of invcap over 63d window."""
    res = _ewma(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_63d_v063_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_63d_v064_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 63d window."""
    res = _ewma(_std(roic, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_126d_v065_signal(roic):
    """Exponential moving average of Raw level of roic over 126d window."""
    res = _ewma(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_126d_v066_signal(invcap):
    """Exponential moving average of Raw level of invcap over 126d window."""
    res = _ewma(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_126d_v067_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_126d_v068_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 126d window."""
    res = _ewma(_std(roic, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_252d_v069_signal(roic):
    """Exponential moving average of Raw level of roic over 252d window."""
    res = _ewma(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_252d_v070_signal(invcap):
    """Exponential moving average of Raw level of invcap over 252d window."""
    res = _ewma(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_252d_v071_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_vol_ewma_252d_v072_signal(roic):
    """Exponential moving average of ROIC stability (standard deviation) over 252d window."""
    res = _ewma(_std(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_roic_ewma_504d_v073_signal(roic):
    """Exponential moving average of Raw level of roic over 504d window."""
    res = _ewma(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_invcap_ewma_504d_v074_signal(invcap):
    """Exponential moving average of Raw level of invcap over 504d window."""
    res = _ewma(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_roic_compounder_fin_netinc_ewma_504d_v075_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f47_roic_compounder_fin_roic_base_5d_v001_signal": {"func": f47_roic_compounder_fin_roic_base_5d_v001_signal},
    "f47_roic_compounder_fin_invcap_base_5d_v002_signal": {"func": f47_roic_compounder_fin_invcap_base_5d_v002_signal},
    "f47_roic_compounder_fin_netinc_base_5d_v003_signal": {"func": f47_roic_compounder_fin_netinc_base_5d_v003_signal},
    "f47_roic_compounder_fin_roic_vol_base_5d_v004_signal": {"func": f47_roic_compounder_fin_roic_vol_base_5d_v004_signal},
    "f47_roic_compounder_fin_roic_base_10d_v005_signal": {"func": f47_roic_compounder_fin_roic_base_10d_v005_signal},
    "f47_roic_compounder_fin_invcap_base_10d_v006_signal": {"func": f47_roic_compounder_fin_invcap_base_10d_v006_signal},
    "f47_roic_compounder_fin_netinc_base_10d_v007_signal": {"func": f47_roic_compounder_fin_netinc_base_10d_v007_signal},
    "f47_roic_compounder_fin_roic_vol_base_10d_v008_signal": {"func": f47_roic_compounder_fin_roic_vol_base_10d_v008_signal},
    "f47_roic_compounder_fin_roic_base_21d_v009_signal": {"func": f47_roic_compounder_fin_roic_base_21d_v009_signal},
    "f47_roic_compounder_fin_invcap_base_21d_v010_signal": {"func": f47_roic_compounder_fin_invcap_base_21d_v010_signal},
    "f47_roic_compounder_fin_netinc_base_21d_v011_signal": {"func": f47_roic_compounder_fin_netinc_base_21d_v011_signal},
    "f47_roic_compounder_fin_roic_vol_base_21d_v012_signal": {"func": f47_roic_compounder_fin_roic_vol_base_21d_v012_signal},
    "f47_roic_compounder_fin_roic_base_42d_v013_signal": {"func": f47_roic_compounder_fin_roic_base_42d_v013_signal},
    "f47_roic_compounder_fin_invcap_base_42d_v014_signal": {"func": f47_roic_compounder_fin_invcap_base_42d_v014_signal},
    "f47_roic_compounder_fin_netinc_base_42d_v015_signal": {"func": f47_roic_compounder_fin_netinc_base_42d_v015_signal},
    "f47_roic_compounder_fin_roic_vol_base_42d_v016_signal": {"func": f47_roic_compounder_fin_roic_vol_base_42d_v016_signal},
    "f47_roic_compounder_fin_roic_base_63d_v017_signal": {"func": f47_roic_compounder_fin_roic_base_63d_v017_signal},
    "f47_roic_compounder_fin_invcap_base_63d_v018_signal": {"func": f47_roic_compounder_fin_invcap_base_63d_v018_signal},
    "f47_roic_compounder_fin_netinc_base_63d_v019_signal": {"func": f47_roic_compounder_fin_netinc_base_63d_v019_signal},
    "f47_roic_compounder_fin_roic_vol_base_63d_v020_signal": {"func": f47_roic_compounder_fin_roic_vol_base_63d_v020_signal},
    "f47_roic_compounder_fin_roic_base_126d_v021_signal": {"func": f47_roic_compounder_fin_roic_base_126d_v021_signal},
    "f47_roic_compounder_fin_invcap_base_126d_v022_signal": {"func": f47_roic_compounder_fin_invcap_base_126d_v022_signal},
    "f47_roic_compounder_fin_netinc_base_126d_v023_signal": {"func": f47_roic_compounder_fin_netinc_base_126d_v023_signal},
    "f47_roic_compounder_fin_roic_vol_base_126d_v024_signal": {"func": f47_roic_compounder_fin_roic_vol_base_126d_v024_signal},
    "f47_roic_compounder_fin_roic_base_252d_v025_signal": {"func": f47_roic_compounder_fin_roic_base_252d_v025_signal},
    "f47_roic_compounder_fin_invcap_base_252d_v026_signal": {"func": f47_roic_compounder_fin_invcap_base_252d_v026_signal},
    "f47_roic_compounder_fin_netinc_base_252d_v027_signal": {"func": f47_roic_compounder_fin_netinc_base_252d_v027_signal},
    "f47_roic_compounder_fin_roic_vol_base_252d_v028_signal": {"func": f47_roic_compounder_fin_roic_vol_base_252d_v028_signal},
    "f47_roic_compounder_fin_roic_base_504d_v029_signal": {"func": f47_roic_compounder_fin_roic_base_504d_v029_signal},
    "f47_roic_compounder_fin_invcap_base_504d_v030_signal": {"func": f47_roic_compounder_fin_invcap_base_504d_v030_signal},
    "f47_roic_compounder_fin_netinc_base_504d_v031_signal": {"func": f47_roic_compounder_fin_netinc_base_504d_v031_signal},
    "f47_roic_compounder_fin_roic_vol_base_504d_v032_signal": {"func": f47_roic_compounder_fin_roic_vol_base_504d_v032_signal},
    "f47_roic_compounder_fin_roic_base_756d_v033_signal": {"func": f47_roic_compounder_fin_roic_base_756d_v033_signal},
    "f47_roic_compounder_fin_invcap_base_756d_v034_signal": {"func": f47_roic_compounder_fin_invcap_base_756d_v034_signal},
    "f47_roic_compounder_fin_netinc_base_756d_v035_signal": {"func": f47_roic_compounder_fin_netinc_base_756d_v035_signal},
    "f47_roic_compounder_fin_roic_vol_base_756d_v036_signal": {"func": f47_roic_compounder_fin_roic_vol_base_756d_v036_signal},
    "f47_roic_compounder_fin_roic_base_1008d_v037_signal": {"func": f47_roic_compounder_fin_roic_base_1008d_v037_signal},
    "f47_roic_compounder_fin_invcap_base_1008d_v038_signal": {"func": f47_roic_compounder_fin_invcap_base_1008d_v038_signal},
    "f47_roic_compounder_fin_netinc_base_1008d_v039_signal": {"func": f47_roic_compounder_fin_netinc_base_1008d_v039_signal},
    "f47_roic_compounder_fin_roic_vol_base_1008d_v040_signal": {"func": f47_roic_compounder_fin_roic_vol_base_1008d_v040_signal},
    "f47_roic_compounder_fin_roic_base_1260d_v041_signal": {"func": f47_roic_compounder_fin_roic_base_1260d_v041_signal},
    "f47_roic_compounder_fin_invcap_base_1260d_v042_signal": {"func": f47_roic_compounder_fin_invcap_base_1260d_v042_signal},
    "f47_roic_compounder_fin_netinc_base_1260d_v043_signal": {"func": f47_roic_compounder_fin_netinc_base_1260d_v043_signal},
    "f47_roic_compounder_fin_roic_vol_base_1260d_v044_signal": {"func": f47_roic_compounder_fin_roic_vol_base_1260d_v044_signal},
    "f47_roic_compounder_fin_roic_ewma_5d_v045_signal": {"func": f47_roic_compounder_fin_roic_ewma_5d_v045_signal},
    "f47_roic_compounder_fin_invcap_ewma_5d_v046_signal": {"func": f47_roic_compounder_fin_invcap_ewma_5d_v046_signal},
    "f47_roic_compounder_fin_netinc_ewma_5d_v047_signal": {"func": f47_roic_compounder_fin_netinc_ewma_5d_v047_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_5d_v048_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_5d_v048_signal},
    "f47_roic_compounder_fin_roic_ewma_10d_v049_signal": {"func": f47_roic_compounder_fin_roic_ewma_10d_v049_signal},
    "f47_roic_compounder_fin_invcap_ewma_10d_v050_signal": {"func": f47_roic_compounder_fin_invcap_ewma_10d_v050_signal},
    "f47_roic_compounder_fin_netinc_ewma_10d_v051_signal": {"func": f47_roic_compounder_fin_netinc_ewma_10d_v051_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_10d_v052_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_10d_v052_signal},
    "f47_roic_compounder_fin_roic_ewma_21d_v053_signal": {"func": f47_roic_compounder_fin_roic_ewma_21d_v053_signal},
    "f47_roic_compounder_fin_invcap_ewma_21d_v054_signal": {"func": f47_roic_compounder_fin_invcap_ewma_21d_v054_signal},
    "f47_roic_compounder_fin_netinc_ewma_21d_v055_signal": {"func": f47_roic_compounder_fin_netinc_ewma_21d_v055_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_21d_v056_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_21d_v056_signal},
    "f47_roic_compounder_fin_roic_ewma_42d_v057_signal": {"func": f47_roic_compounder_fin_roic_ewma_42d_v057_signal},
    "f47_roic_compounder_fin_invcap_ewma_42d_v058_signal": {"func": f47_roic_compounder_fin_invcap_ewma_42d_v058_signal},
    "f47_roic_compounder_fin_netinc_ewma_42d_v059_signal": {"func": f47_roic_compounder_fin_netinc_ewma_42d_v059_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_42d_v060_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_42d_v060_signal},
    "f47_roic_compounder_fin_roic_ewma_63d_v061_signal": {"func": f47_roic_compounder_fin_roic_ewma_63d_v061_signal},
    "f47_roic_compounder_fin_invcap_ewma_63d_v062_signal": {"func": f47_roic_compounder_fin_invcap_ewma_63d_v062_signal},
    "f47_roic_compounder_fin_netinc_ewma_63d_v063_signal": {"func": f47_roic_compounder_fin_netinc_ewma_63d_v063_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_63d_v064_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_63d_v064_signal},
    "f47_roic_compounder_fin_roic_ewma_126d_v065_signal": {"func": f47_roic_compounder_fin_roic_ewma_126d_v065_signal},
    "f47_roic_compounder_fin_invcap_ewma_126d_v066_signal": {"func": f47_roic_compounder_fin_invcap_ewma_126d_v066_signal},
    "f47_roic_compounder_fin_netinc_ewma_126d_v067_signal": {"func": f47_roic_compounder_fin_netinc_ewma_126d_v067_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_126d_v068_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_126d_v068_signal},
    "f47_roic_compounder_fin_roic_ewma_252d_v069_signal": {"func": f47_roic_compounder_fin_roic_ewma_252d_v069_signal},
    "f47_roic_compounder_fin_invcap_ewma_252d_v070_signal": {"func": f47_roic_compounder_fin_invcap_ewma_252d_v070_signal},
    "f47_roic_compounder_fin_netinc_ewma_252d_v071_signal": {"func": f47_roic_compounder_fin_netinc_ewma_252d_v071_signal},
    "f47_roic_compounder_fin_roic_vol_ewma_252d_v072_signal": {"func": f47_roic_compounder_fin_roic_vol_ewma_252d_v072_signal},
    "f47_roic_compounder_fin_roic_ewma_504d_v073_signal": {"func": f47_roic_compounder_fin_roic_ewma_504d_v073_signal},
    "f47_roic_compounder_fin_invcap_ewma_504d_v074_signal": {"func": f47_roic_compounder_fin_invcap_ewma_504d_v074_signal},
    "f47_roic_compounder_fin_netinc_ewma_504d_v075_signal": {"func": f47_roic_compounder_fin_netinc_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
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
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
