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

def f14_bank_payout_fcf_base_5d_v001_signal(fcf):
    """Moving average of Raw level of fcf over 5d window."""
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_5d_v002_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_5d_v003_signal(divyield):
    """Moving average of Raw level of divyield over 5d window."""
    res = _sma(divyield, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_5d_v004_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 5d window."""
    res = _sma(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_10d_v005_signal(fcf):
    """Moving average of Raw level of fcf over 10d window."""
    res = _sma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_10d_v006_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_10d_v007_signal(divyield):
    """Moving average of Raw level of divyield over 10d window."""
    res = _sma(divyield, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_10d_v008_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 10d window."""
    res = _sma(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_21d_v009_signal(fcf):
    """Moving average of Raw level of fcf over 21d window."""
    res = _sma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_21d_v010_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_21d_v011_signal(divyield):
    """Moving average of Raw level of divyield over 21d window."""
    res = _sma(divyield, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_21d_v012_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 21d window."""
    res = _sma(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_42d_v013_signal(fcf):
    """Moving average of Raw level of fcf over 42d window."""
    res = _sma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_42d_v014_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_42d_v015_signal(divyield):
    """Moving average of Raw level of divyield over 42d window."""
    res = _sma(divyield, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_42d_v016_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 42d window."""
    res = _sma(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_63d_v017_signal(fcf):
    """Moving average of Raw level of fcf over 63d window."""
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_63d_v018_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_63d_v019_signal(divyield):
    """Moving average of Raw level of divyield over 63d window."""
    res = _sma(divyield, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_63d_v020_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 63d window."""
    res = _sma(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_126d_v021_signal(fcf):
    """Moving average of Raw level of fcf over 126d window."""
    res = _sma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_126d_v022_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_126d_v023_signal(divyield):
    """Moving average of Raw level of divyield over 126d window."""
    res = _sma(divyield, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_126d_v024_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 126d window."""
    res = _sma(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_252d_v025_signal(fcf):
    """Moving average of Raw level of fcf over 252d window."""
    res = _sma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_252d_v026_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_252d_v027_signal(divyield):
    """Moving average of Raw level of divyield over 252d window."""
    res = _sma(divyield, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_252d_v028_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 252d window."""
    res = _sma(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_504d_v029_signal(fcf):
    """Moving average of Raw level of fcf over 504d window."""
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_504d_v030_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_504d_v031_signal(divyield):
    """Moving average of Raw level of divyield over 504d window."""
    res = _sma(divyield, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_504d_v032_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 504d window."""
    res = _sma(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_756d_v033_signal(fcf):
    """Moving average of Raw level of fcf over 756d window."""
    res = _sma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_756d_v034_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_756d_v035_signal(divyield):
    """Moving average of Raw level of divyield over 756d window."""
    res = _sma(divyield, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_756d_v036_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 756d window."""
    res = _sma(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_1008d_v037_signal(fcf):
    """Moving average of Raw level of fcf over 1008d window."""
    res = _sma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_1008d_v038_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_1008d_v039_signal(divyield):
    """Moving average of Raw level of divyield over 1008d window."""
    res = _sma(divyield, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_1008d_v040_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 1008d window."""
    res = _sma(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_base_1260d_v041_signal(fcf):
    """Moving average of Raw level of fcf over 1260d window."""
    res = _sma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_base_1260d_v042_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_base_1260d_v043_signal(divyield):
    """Moving average of Raw level of divyield over 1260d window."""
    res = _sma(divyield, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_base_1260d_v044_signal(fcf, netinc):
    """Moving average of Cash flow conversion safety over 1260d window."""
    res = _sma(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_5d_v045_signal(fcf):
    """Exponential moving average of Raw level of fcf over 5d window."""
    res = _ewma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_5d_v046_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_5d_v047_signal(divyield):
    """Exponential moving average of Raw level of divyield over 5d window."""
    res = _ewma(divyield, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_5d_v048_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 5d window."""
    res = _ewma(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_10d_v049_signal(fcf):
    """Exponential moving average of Raw level of fcf over 10d window."""
    res = _ewma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_10d_v050_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_10d_v051_signal(divyield):
    """Exponential moving average of Raw level of divyield over 10d window."""
    res = _ewma(divyield, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_10d_v052_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 10d window."""
    res = _ewma(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_21d_v053_signal(fcf):
    """Exponential moving average of Raw level of fcf over 21d window."""
    res = _ewma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_21d_v054_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_21d_v055_signal(divyield):
    """Exponential moving average of Raw level of divyield over 21d window."""
    res = _ewma(divyield, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_21d_v056_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 21d window."""
    res = _ewma(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_42d_v057_signal(fcf):
    """Exponential moving average of Raw level of fcf over 42d window."""
    res = _ewma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_42d_v058_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_42d_v059_signal(divyield):
    """Exponential moving average of Raw level of divyield over 42d window."""
    res = _ewma(divyield, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_42d_v060_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 42d window."""
    res = _ewma(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_63d_v061_signal(fcf):
    """Exponential moving average of Raw level of fcf over 63d window."""
    res = _ewma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_63d_v062_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_63d_v063_signal(divyield):
    """Exponential moving average of Raw level of divyield over 63d window."""
    res = _ewma(divyield, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_63d_v064_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 63d window."""
    res = _ewma(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_126d_v065_signal(fcf):
    """Exponential moving average of Raw level of fcf over 126d window."""
    res = _ewma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_126d_v066_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_126d_v067_signal(divyield):
    """Exponential moving average of Raw level of divyield over 126d window."""
    res = _ewma(divyield, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_126d_v068_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 126d window."""
    res = _ewma(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_252d_v069_signal(fcf):
    """Exponential moving average of Raw level of fcf over 252d window."""
    res = _ewma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_252d_v070_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_252d_v071_signal(divyield):
    """Exponential moving average of Raw level of divyield over 252d window."""
    res = _ewma(divyield, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_252d_v072_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 252d window."""
    res = _ewma(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_504d_v073_signal(fcf):
    """Exponential moving average of Raw level of fcf over 504d window."""
    res = _ewma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_504d_v074_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_504d_v075_signal(divyield):
    """Exponential moving average of Raw level of divyield over 504d window."""
    res = _ewma(divyield, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f14_bank_payout_fcf_base_5d_v001_signal": {"func": f14_bank_payout_fcf_base_5d_v001_signal},
    "f14_bank_payout_netinc_base_5d_v002_signal": {"func": f14_bank_payout_netinc_base_5d_v002_signal},
    "f14_bank_payout_divyield_base_5d_v003_signal": {"func": f14_bank_payout_divyield_base_5d_v003_signal},
    "f14_bank_payout_cash_payout_safety_base_5d_v004_signal": {"func": f14_bank_payout_cash_payout_safety_base_5d_v004_signal},
    "f14_bank_payout_fcf_base_10d_v005_signal": {"func": f14_bank_payout_fcf_base_10d_v005_signal},
    "f14_bank_payout_netinc_base_10d_v006_signal": {"func": f14_bank_payout_netinc_base_10d_v006_signal},
    "f14_bank_payout_divyield_base_10d_v007_signal": {"func": f14_bank_payout_divyield_base_10d_v007_signal},
    "f14_bank_payout_cash_payout_safety_base_10d_v008_signal": {"func": f14_bank_payout_cash_payout_safety_base_10d_v008_signal},
    "f14_bank_payout_fcf_base_21d_v009_signal": {"func": f14_bank_payout_fcf_base_21d_v009_signal},
    "f14_bank_payout_netinc_base_21d_v010_signal": {"func": f14_bank_payout_netinc_base_21d_v010_signal},
    "f14_bank_payout_divyield_base_21d_v011_signal": {"func": f14_bank_payout_divyield_base_21d_v011_signal},
    "f14_bank_payout_cash_payout_safety_base_21d_v012_signal": {"func": f14_bank_payout_cash_payout_safety_base_21d_v012_signal},
    "f14_bank_payout_fcf_base_42d_v013_signal": {"func": f14_bank_payout_fcf_base_42d_v013_signal},
    "f14_bank_payout_netinc_base_42d_v014_signal": {"func": f14_bank_payout_netinc_base_42d_v014_signal},
    "f14_bank_payout_divyield_base_42d_v015_signal": {"func": f14_bank_payout_divyield_base_42d_v015_signal},
    "f14_bank_payout_cash_payout_safety_base_42d_v016_signal": {"func": f14_bank_payout_cash_payout_safety_base_42d_v016_signal},
    "f14_bank_payout_fcf_base_63d_v017_signal": {"func": f14_bank_payout_fcf_base_63d_v017_signal},
    "f14_bank_payout_netinc_base_63d_v018_signal": {"func": f14_bank_payout_netinc_base_63d_v018_signal},
    "f14_bank_payout_divyield_base_63d_v019_signal": {"func": f14_bank_payout_divyield_base_63d_v019_signal},
    "f14_bank_payout_cash_payout_safety_base_63d_v020_signal": {"func": f14_bank_payout_cash_payout_safety_base_63d_v020_signal},
    "f14_bank_payout_fcf_base_126d_v021_signal": {"func": f14_bank_payout_fcf_base_126d_v021_signal},
    "f14_bank_payout_netinc_base_126d_v022_signal": {"func": f14_bank_payout_netinc_base_126d_v022_signal},
    "f14_bank_payout_divyield_base_126d_v023_signal": {"func": f14_bank_payout_divyield_base_126d_v023_signal},
    "f14_bank_payout_cash_payout_safety_base_126d_v024_signal": {"func": f14_bank_payout_cash_payout_safety_base_126d_v024_signal},
    "f14_bank_payout_fcf_base_252d_v025_signal": {"func": f14_bank_payout_fcf_base_252d_v025_signal},
    "f14_bank_payout_netinc_base_252d_v026_signal": {"func": f14_bank_payout_netinc_base_252d_v026_signal},
    "f14_bank_payout_divyield_base_252d_v027_signal": {"func": f14_bank_payout_divyield_base_252d_v027_signal},
    "f14_bank_payout_cash_payout_safety_base_252d_v028_signal": {"func": f14_bank_payout_cash_payout_safety_base_252d_v028_signal},
    "f14_bank_payout_fcf_base_504d_v029_signal": {"func": f14_bank_payout_fcf_base_504d_v029_signal},
    "f14_bank_payout_netinc_base_504d_v030_signal": {"func": f14_bank_payout_netinc_base_504d_v030_signal},
    "f14_bank_payout_divyield_base_504d_v031_signal": {"func": f14_bank_payout_divyield_base_504d_v031_signal},
    "f14_bank_payout_cash_payout_safety_base_504d_v032_signal": {"func": f14_bank_payout_cash_payout_safety_base_504d_v032_signal},
    "f14_bank_payout_fcf_base_756d_v033_signal": {"func": f14_bank_payout_fcf_base_756d_v033_signal},
    "f14_bank_payout_netinc_base_756d_v034_signal": {"func": f14_bank_payout_netinc_base_756d_v034_signal},
    "f14_bank_payout_divyield_base_756d_v035_signal": {"func": f14_bank_payout_divyield_base_756d_v035_signal},
    "f14_bank_payout_cash_payout_safety_base_756d_v036_signal": {"func": f14_bank_payout_cash_payout_safety_base_756d_v036_signal},
    "f14_bank_payout_fcf_base_1008d_v037_signal": {"func": f14_bank_payout_fcf_base_1008d_v037_signal},
    "f14_bank_payout_netinc_base_1008d_v038_signal": {"func": f14_bank_payout_netinc_base_1008d_v038_signal},
    "f14_bank_payout_divyield_base_1008d_v039_signal": {"func": f14_bank_payout_divyield_base_1008d_v039_signal},
    "f14_bank_payout_cash_payout_safety_base_1008d_v040_signal": {"func": f14_bank_payout_cash_payout_safety_base_1008d_v040_signal},
    "f14_bank_payout_fcf_base_1260d_v041_signal": {"func": f14_bank_payout_fcf_base_1260d_v041_signal},
    "f14_bank_payout_netinc_base_1260d_v042_signal": {"func": f14_bank_payout_netinc_base_1260d_v042_signal},
    "f14_bank_payout_divyield_base_1260d_v043_signal": {"func": f14_bank_payout_divyield_base_1260d_v043_signal},
    "f14_bank_payout_cash_payout_safety_base_1260d_v044_signal": {"func": f14_bank_payout_cash_payout_safety_base_1260d_v044_signal},
    "f14_bank_payout_fcf_ewma_5d_v045_signal": {"func": f14_bank_payout_fcf_ewma_5d_v045_signal},
    "f14_bank_payout_netinc_ewma_5d_v046_signal": {"func": f14_bank_payout_netinc_ewma_5d_v046_signal},
    "f14_bank_payout_divyield_ewma_5d_v047_signal": {"func": f14_bank_payout_divyield_ewma_5d_v047_signal},
    "f14_bank_payout_cash_payout_safety_ewma_5d_v048_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_5d_v048_signal},
    "f14_bank_payout_fcf_ewma_10d_v049_signal": {"func": f14_bank_payout_fcf_ewma_10d_v049_signal},
    "f14_bank_payout_netinc_ewma_10d_v050_signal": {"func": f14_bank_payout_netinc_ewma_10d_v050_signal},
    "f14_bank_payout_divyield_ewma_10d_v051_signal": {"func": f14_bank_payout_divyield_ewma_10d_v051_signal},
    "f14_bank_payout_cash_payout_safety_ewma_10d_v052_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_10d_v052_signal},
    "f14_bank_payout_fcf_ewma_21d_v053_signal": {"func": f14_bank_payout_fcf_ewma_21d_v053_signal},
    "f14_bank_payout_netinc_ewma_21d_v054_signal": {"func": f14_bank_payout_netinc_ewma_21d_v054_signal},
    "f14_bank_payout_divyield_ewma_21d_v055_signal": {"func": f14_bank_payout_divyield_ewma_21d_v055_signal},
    "f14_bank_payout_cash_payout_safety_ewma_21d_v056_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_21d_v056_signal},
    "f14_bank_payout_fcf_ewma_42d_v057_signal": {"func": f14_bank_payout_fcf_ewma_42d_v057_signal},
    "f14_bank_payout_netinc_ewma_42d_v058_signal": {"func": f14_bank_payout_netinc_ewma_42d_v058_signal},
    "f14_bank_payout_divyield_ewma_42d_v059_signal": {"func": f14_bank_payout_divyield_ewma_42d_v059_signal},
    "f14_bank_payout_cash_payout_safety_ewma_42d_v060_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_42d_v060_signal},
    "f14_bank_payout_fcf_ewma_63d_v061_signal": {"func": f14_bank_payout_fcf_ewma_63d_v061_signal},
    "f14_bank_payout_netinc_ewma_63d_v062_signal": {"func": f14_bank_payout_netinc_ewma_63d_v062_signal},
    "f14_bank_payout_divyield_ewma_63d_v063_signal": {"func": f14_bank_payout_divyield_ewma_63d_v063_signal},
    "f14_bank_payout_cash_payout_safety_ewma_63d_v064_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_63d_v064_signal},
    "f14_bank_payout_fcf_ewma_126d_v065_signal": {"func": f14_bank_payout_fcf_ewma_126d_v065_signal},
    "f14_bank_payout_netinc_ewma_126d_v066_signal": {"func": f14_bank_payout_netinc_ewma_126d_v066_signal},
    "f14_bank_payout_divyield_ewma_126d_v067_signal": {"func": f14_bank_payout_divyield_ewma_126d_v067_signal},
    "f14_bank_payout_cash_payout_safety_ewma_126d_v068_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_126d_v068_signal},
    "f14_bank_payout_fcf_ewma_252d_v069_signal": {"func": f14_bank_payout_fcf_ewma_252d_v069_signal},
    "f14_bank_payout_netinc_ewma_252d_v070_signal": {"func": f14_bank_payout_netinc_ewma_252d_v070_signal},
    "f14_bank_payout_divyield_ewma_252d_v071_signal": {"func": f14_bank_payout_divyield_ewma_252d_v071_signal},
    "f14_bank_payout_cash_payout_safety_ewma_252d_v072_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_252d_v072_signal},
    "f14_bank_payout_fcf_ewma_504d_v073_signal": {"func": f14_bank_payout_fcf_ewma_504d_v073_signal},
    "f14_bank_payout_netinc_ewma_504d_v074_signal": {"func": f14_bank_payout_netinc_ewma_504d_v074_signal},
    "f14_bank_payout_divyield_ewma_504d_v075_signal": {"func": f14_bank_payout_divyield_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 14...")
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
