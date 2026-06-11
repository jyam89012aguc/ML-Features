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

def f50_compounder_index_fin_pb_base_5d_v001_signal(pb):
    """Moving average of Raw level of pb over 5d window."""
    res = _sma(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_5d_v002_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_5d_v003_signal(equity):
    """Moving average of Raw level of equity over 5d window."""
    res = _sma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_5d_v004_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 5d window."""
    res = _sma(_ratio(netinc, equity) / pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_10d_v005_signal(pb):
    """Moving average of Raw level of pb over 10d window."""
    res = _sma(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_10d_v006_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_10d_v007_signal(equity):
    """Moving average of Raw level of equity over 10d window."""
    res = _sma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_10d_v008_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 10d window."""
    res = _sma(_ratio(netinc, equity) / pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_21d_v009_signal(pb):
    """Moving average of Raw level of pb over 21d window."""
    res = _sma(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_21d_v010_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_21d_v011_signal(equity):
    """Moving average of Raw level of equity over 21d window."""
    res = _sma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_21d_v012_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 21d window."""
    res = _sma(_ratio(netinc, equity) / pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_42d_v013_signal(pb):
    """Moving average of Raw level of pb over 42d window."""
    res = _sma(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_42d_v014_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_42d_v015_signal(equity):
    """Moving average of Raw level of equity over 42d window."""
    res = _sma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_42d_v016_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 42d window."""
    res = _sma(_ratio(netinc, equity) / pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_63d_v017_signal(pb):
    """Moving average of Raw level of pb over 63d window."""
    res = _sma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_63d_v018_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_63d_v019_signal(equity):
    """Moving average of Raw level of equity over 63d window."""
    res = _sma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_63d_v020_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 63d window."""
    res = _sma(_ratio(netinc, equity) / pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_126d_v021_signal(pb):
    """Moving average of Raw level of pb over 126d window."""
    res = _sma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_126d_v022_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_126d_v023_signal(equity):
    """Moving average of Raw level of equity over 126d window."""
    res = _sma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_126d_v024_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 126d window."""
    res = _sma(_ratio(netinc, equity) / pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_252d_v025_signal(pb):
    """Moving average of Raw level of pb over 252d window."""
    res = _sma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_252d_v026_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_252d_v027_signal(equity):
    """Moving average of Raw level of equity over 252d window."""
    res = _sma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_252d_v028_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 252d window."""
    res = _sma(_ratio(netinc, equity) / pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_504d_v029_signal(pb):
    """Moving average of Raw level of pb over 504d window."""
    res = _sma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_504d_v030_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_504d_v031_signal(equity):
    """Moving average of Raw level of equity over 504d window."""
    res = _sma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_504d_v032_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 504d window."""
    res = _sma(_ratio(netinc, equity) / pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_756d_v033_signal(pb):
    """Moving average of Raw level of pb over 756d window."""
    res = _sma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_756d_v034_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_756d_v035_signal(equity):
    """Moving average of Raw level of equity over 756d window."""
    res = _sma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_756d_v036_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 756d window."""
    res = _sma(_ratio(netinc, equity) / pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_1008d_v037_signal(pb):
    """Moving average of Raw level of pb over 1008d window."""
    res = _sma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_1008d_v038_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_1008d_v039_signal(equity):
    """Moving average of Raw level of equity over 1008d window."""
    res = _sma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_1008d_v040_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 1008d window."""
    res = _sma(_ratio(netinc, equity) / pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_base_1260d_v041_signal(pb):
    """Moving average of Raw level of pb over 1260d window."""
    res = _sma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_base_1260d_v042_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_base_1260d_v043_signal(equity):
    """Moving average of Raw level of equity over 1260d window."""
    res = _sma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_base_1260d_v044_signal(netinc, equity, pb):
    """Moving average of ROE relative to P/B valuation over 1260d window."""
    res = _sma(_ratio(netinc, equity) / pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_5d_v045_signal(pb):
    """Exponential moving average of Raw level of pb over 5d window."""
    res = _ewma(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_5d_v046_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_5d_v047_signal(equity):
    """Exponential moving average of Raw level of equity over 5d window."""
    res = _ewma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_5d_v048_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 5d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_10d_v049_signal(pb):
    """Exponential moving average of Raw level of pb over 10d window."""
    res = _ewma(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_10d_v050_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_10d_v051_signal(equity):
    """Exponential moving average of Raw level of equity over 10d window."""
    res = _ewma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_10d_v052_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 10d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_21d_v053_signal(pb):
    """Exponential moving average of Raw level of pb over 21d window."""
    res = _ewma(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_21d_v054_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_21d_v055_signal(equity):
    """Exponential moving average of Raw level of equity over 21d window."""
    res = _ewma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_21d_v056_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 21d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_42d_v057_signal(pb):
    """Exponential moving average of Raw level of pb over 42d window."""
    res = _ewma(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_42d_v058_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_42d_v059_signal(equity):
    """Exponential moving average of Raw level of equity over 42d window."""
    res = _ewma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_42d_v060_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 42d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_63d_v061_signal(pb):
    """Exponential moving average of Raw level of pb over 63d window."""
    res = _ewma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_63d_v062_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_63d_v063_signal(equity):
    """Exponential moving average of Raw level of equity over 63d window."""
    res = _ewma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_63d_v064_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 63d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_126d_v065_signal(pb):
    """Exponential moving average of Raw level of pb over 126d window."""
    res = _ewma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_126d_v066_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_126d_v067_signal(equity):
    """Exponential moving average of Raw level of equity over 126d window."""
    res = _ewma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_126d_v068_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 126d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_252d_v069_signal(pb):
    """Exponential moving average of Raw level of pb over 252d window."""
    res = _ewma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_252d_v070_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_252d_v071_signal(equity):
    """Exponential moving average of Raw level of equity over 252d window."""
    res = _ewma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_252d_v072_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 252d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_504d_v073_signal(pb):
    """Exponential moving average of Raw level of pb over 504d window."""
    res = _ewma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_504d_v074_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_504d_v075_signal(equity):
    """Exponential moving average of Raw level of equity over 504d window."""
    res = _ewma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f50_compounder_index_fin_pb_base_5d_v001_signal": {"func": f50_compounder_index_fin_pb_base_5d_v001_signal},
    "f50_compounder_index_fin_netinc_base_5d_v002_signal": {"func": f50_compounder_index_fin_netinc_base_5d_v002_signal},
    "f50_compounder_index_fin_equity_base_5d_v003_signal": {"func": f50_compounder_index_fin_equity_base_5d_v003_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_5d_v004_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_5d_v004_signal},
    "f50_compounder_index_fin_pb_base_10d_v005_signal": {"func": f50_compounder_index_fin_pb_base_10d_v005_signal},
    "f50_compounder_index_fin_netinc_base_10d_v006_signal": {"func": f50_compounder_index_fin_netinc_base_10d_v006_signal},
    "f50_compounder_index_fin_equity_base_10d_v007_signal": {"func": f50_compounder_index_fin_equity_base_10d_v007_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_10d_v008_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_10d_v008_signal},
    "f50_compounder_index_fin_pb_base_21d_v009_signal": {"func": f50_compounder_index_fin_pb_base_21d_v009_signal},
    "f50_compounder_index_fin_netinc_base_21d_v010_signal": {"func": f50_compounder_index_fin_netinc_base_21d_v010_signal},
    "f50_compounder_index_fin_equity_base_21d_v011_signal": {"func": f50_compounder_index_fin_equity_base_21d_v011_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_21d_v012_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_21d_v012_signal},
    "f50_compounder_index_fin_pb_base_42d_v013_signal": {"func": f50_compounder_index_fin_pb_base_42d_v013_signal},
    "f50_compounder_index_fin_netinc_base_42d_v014_signal": {"func": f50_compounder_index_fin_netinc_base_42d_v014_signal},
    "f50_compounder_index_fin_equity_base_42d_v015_signal": {"func": f50_compounder_index_fin_equity_base_42d_v015_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_42d_v016_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_42d_v016_signal},
    "f50_compounder_index_fin_pb_base_63d_v017_signal": {"func": f50_compounder_index_fin_pb_base_63d_v017_signal},
    "f50_compounder_index_fin_netinc_base_63d_v018_signal": {"func": f50_compounder_index_fin_netinc_base_63d_v018_signal},
    "f50_compounder_index_fin_equity_base_63d_v019_signal": {"func": f50_compounder_index_fin_equity_base_63d_v019_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_63d_v020_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_63d_v020_signal},
    "f50_compounder_index_fin_pb_base_126d_v021_signal": {"func": f50_compounder_index_fin_pb_base_126d_v021_signal},
    "f50_compounder_index_fin_netinc_base_126d_v022_signal": {"func": f50_compounder_index_fin_netinc_base_126d_v022_signal},
    "f50_compounder_index_fin_equity_base_126d_v023_signal": {"func": f50_compounder_index_fin_equity_base_126d_v023_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_126d_v024_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_126d_v024_signal},
    "f50_compounder_index_fin_pb_base_252d_v025_signal": {"func": f50_compounder_index_fin_pb_base_252d_v025_signal},
    "f50_compounder_index_fin_netinc_base_252d_v026_signal": {"func": f50_compounder_index_fin_netinc_base_252d_v026_signal},
    "f50_compounder_index_fin_equity_base_252d_v027_signal": {"func": f50_compounder_index_fin_equity_base_252d_v027_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_252d_v028_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_252d_v028_signal},
    "f50_compounder_index_fin_pb_base_504d_v029_signal": {"func": f50_compounder_index_fin_pb_base_504d_v029_signal},
    "f50_compounder_index_fin_netinc_base_504d_v030_signal": {"func": f50_compounder_index_fin_netinc_base_504d_v030_signal},
    "f50_compounder_index_fin_equity_base_504d_v031_signal": {"func": f50_compounder_index_fin_equity_base_504d_v031_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_504d_v032_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_504d_v032_signal},
    "f50_compounder_index_fin_pb_base_756d_v033_signal": {"func": f50_compounder_index_fin_pb_base_756d_v033_signal},
    "f50_compounder_index_fin_netinc_base_756d_v034_signal": {"func": f50_compounder_index_fin_netinc_base_756d_v034_signal},
    "f50_compounder_index_fin_equity_base_756d_v035_signal": {"func": f50_compounder_index_fin_equity_base_756d_v035_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_756d_v036_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_756d_v036_signal},
    "f50_compounder_index_fin_pb_base_1008d_v037_signal": {"func": f50_compounder_index_fin_pb_base_1008d_v037_signal},
    "f50_compounder_index_fin_netinc_base_1008d_v038_signal": {"func": f50_compounder_index_fin_netinc_base_1008d_v038_signal},
    "f50_compounder_index_fin_equity_base_1008d_v039_signal": {"func": f50_compounder_index_fin_equity_base_1008d_v039_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_1008d_v040_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_1008d_v040_signal},
    "f50_compounder_index_fin_pb_base_1260d_v041_signal": {"func": f50_compounder_index_fin_pb_base_1260d_v041_signal},
    "f50_compounder_index_fin_netinc_base_1260d_v042_signal": {"func": f50_compounder_index_fin_netinc_base_1260d_v042_signal},
    "f50_compounder_index_fin_equity_base_1260d_v043_signal": {"func": f50_compounder_index_fin_equity_base_1260d_v043_signal},
    "f50_compounder_index_fin_quality_valuation_index_base_1260d_v044_signal": {"func": f50_compounder_index_fin_quality_valuation_index_base_1260d_v044_signal},
    "f50_compounder_index_fin_pb_ewma_5d_v045_signal": {"func": f50_compounder_index_fin_pb_ewma_5d_v045_signal},
    "f50_compounder_index_fin_netinc_ewma_5d_v046_signal": {"func": f50_compounder_index_fin_netinc_ewma_5d_v046_signal},
    "f50_compounder_index_fin_equity_ewma_5d_v047_signal": {"func": f50_compounder_index_fin_equity_ewma_5d_v047_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_5d_v048_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_5d_v048_signal},
    "f50_compounder_index_fin_pb_ewma_10d_v049_signal": {"func": f50_compounder_index_fin_pb_ewma_10d_v049_signal},
    "f50_compounder_index_fin_netinc_ewma_10d_v050_signal": {"func": f50_compounder_index_fin_netinc_ewma_10d_v050_signal},
    "f50_compounder_index_fin_equity_ewma_10d_v051_signal": {"func": f50_compounder_index_fin_equity_ewma_10d_v051_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_10d_v052_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_10d_v052_signal},
    "f50_compounder_index_fin_pb_ewma_21d_v053_signal": {"func": f50_compounder_index_fin_pb_ewma_21d_v053_signal},
    "f50_compounder_index_fin_netinc_ewma_21d_v054_signal": {"func": f50_compounder_index_fin_netinc_ewma_21d_v054_signal},
    "f50_compounder_index_fin_equity_ewma_21d_v055_signal": {"func": f50_compounder_index_fin_equity_ewma_21d_v055_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_21d_v056_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_21d_v056_signal},
    "f50_compounder_index_fin_pb_ewma_42d_v057_signal": {"func": f50_compounder_index_fin_pb_ewma_42d_v057_signal},
    "f50_compounder_index_fin_netinc_ewma_42d_v058_signal": {"func": f50_compounder_index_fin_netinc_ewma_42d_v058_signal},
    "f50_compounder_index_fin_equity_ewma_42d_v059_signal": {"func": f50_compounder_index_fin_equity_ewma_42d_v059_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_42d_v060_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_42d_v060_signal},
    "f50_compounder_index_fin_pb_ewma_63d_v061_signal": {"func": f50_compounder_index_fin_pb_ewma_63d_v061_signal},
    "f50_compounder_index_fin_netinc_ewma_63d_v062_signal": {"func": f50_compounder_index_fin_netinc_ewma_63d_v062_signal},
    "f50_compounder_index_fin_equity_ewma_63d_v063_signal": {"func": f50_compounder_index_fin_equity_ewma_63d_v063_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_63d_v064_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_63d_v064_signal},
    "f50_compounder_index_fin_pb_ewma_126d_v065_signal": {"func": f50_compounder_index_fin_pb_ewma_126d_v065_signal},
    "f50_compounder_index_fin_netinc_ewma_126d_v066_signal": {"func": f50_compounder_index_fin_netinc_ewma_126d_v066_signal},
    "f50_compounder_index_fin_equity_ewma_126d_v067_signal": {"func": f50_compounder_index_fin_equity_ewma_126d_v067_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_126d_v068_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_126d_v068_signal},
    "f50_compounder_index_fin_pb_ewma_252d_v069_signal": {"func": f50_compounder_index_fin_pb_ewma_252d_v069_signal},
    "f50_compounder_index_fin_netinc_ewma_252d_v070_signal": {"func": f50_compounder_index_fin_netinc_ewma_252d_v070_signal},
    "f50_compounder_index_fin_equity_ewma_252d_v071_signal": {"func": f50_compounder_index_fin_equity_ewma_252d_v071_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_252d_v072_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_252d_v072_signal},
    "f50_compounder_index_fin_pb_ewma_504d_v073_signal": {"func": f50_compounder_index_fin_pb_ewma_504d_v073_signal},
    "f50_compounder_index_fin_netinc_ewma_504d_v074_signal": {"func": f50_compounder_index_fin_netinc_ewma_504d_v074_signal},
    "f50_compounder_index_fin_equity_ewma_504d_v075_signal": {"func": f50_compounder_index_fin_equity_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 50...")
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
