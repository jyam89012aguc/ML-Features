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

def f34_earnings_quality_fcf_slope_pct_5d_v001_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 5d window."""
    res = _slope_pct(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_5d_v002_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_5d_v003_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 5d window."""
    res = _slope_pct(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_5d_v004_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 5d window."""
    res = _slope_pct(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_10d_v005_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 10d window."""
    res = _slope_pct(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_10d_v006_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_10d_v007_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 10d window."""
    res = _slope_pct(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_10d_v008_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 10d window."""
    res = _slope_pct(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_21d_v009_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 21d window."""
    res = _slope_pct(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_21d_v010_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_21d_v011_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 21d window."""
    res = _slope_pct(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_21d_v012_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 21d window."""
    res = _slope_pct(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_42d_v013_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 42d window."""
    res = _slope_pct(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_42d_v014_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_42d_v015_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 42d window."""
    res = _slope_pct(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_42d_v016_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 42d window."""
    res = _slope_pct(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_63d_v017_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 63d window."""
    res = _slope_pct(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_63d_v018_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_63d_v019_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 63d window."""
    res = _slope_pct(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_63d_v020_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 63d window."""
    res = _slope_pct(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_126d_v021_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 126d window."""
    res = _slope_pct(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_126d_v022_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_126d_v023_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 126d window."""
    res = _slope_pct(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_126d_v024_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 126d window."""
    res = _slope_pct(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_252d_v025_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 252d window."""
    res = _slope_pct(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_252d_v026_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_252d_v027_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 252d window."""
    res = _slope_pct(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_252d_v028_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 252d window."""
    res = _slope_pct(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_504d_v029_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 504d window."""
    res = _slope_pct(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_504d_v030_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_504d_v031_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 504d window."""
    res = _slope_pct(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_504d_v032_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 504d window."""
    res = _slope_pct(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_756d_v033_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 756d window."""
    res = _slope_pct(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_756d_v034_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_756d_v035_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 756d window."""
    res = _slope_pct(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_756d_v036_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 756d window."""
    res = _slope_pct(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_1008d_v037_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 1008d window."""
    res = _slope_pct(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_1008d_v038_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_1008d_v039_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 1008d window."""
    res = _slope_pct(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_1008d_v040_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 1008d window."""
    res = _slope_pct(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_pct_1260d_v041_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 1260d window."""
    res = _slope_pct(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_pct_1260d_v042_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_pct_1260d_v043_signal(receivables):
    """Percentage slope for momentum for Raw level of receivables over 1260d window."""
    res = _slope_pct(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_pct_1260d_v044_signal(fcf, netinc):
    """Percentage slope for momentum for Free cash flow conversion of net income over 1260d window."""
    res = _slope_pct(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_5d_v045_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 5d window."""
    res = _jerk(fcf, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_5d_v046_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_5d_v047_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 5d window."""
    res = _jerk(receivables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_5d_v048_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 5d window."""
    res = _jerk(_ratio(fcf, netinc), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_10d_v049_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 10d window."""
    res = _jerk(fcf, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_10d_v050_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_10d_v051_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 10d window."""
    res = _jerk(receivables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_10d_v052_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 10d window."""
    res = _jerk(_ratio(fcf, netinc), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_21d_v053_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 21d window."""
    res = _jerk(fcf, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_21d_v054_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_21d_v055_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 21d window."""
    res = _jerk(receivables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_21d_v056_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 21d window."""
    res = _jerk(_ratio(fcf, netinc), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_42d_v057_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 42d window."""
    res = _jerk(fcf, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_42d_v058_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_42d_v059_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 42d window."""
    res = _jerk(receivables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_42d_v060_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 42d window."""
    res = _jerk(_ratio(fcf, netinc), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_63d_v061_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 63d window."""
    res = _jerk(fcf, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_63d_v062_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_63d_v063_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 63d window."""
    res = _jerk(receivables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_63d_v064_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 63d window."""
    res = _jerk(_ratio(fcf, netinc), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_126d_v065_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 126d window."""
    res = _jerk(fcf, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_126d_v066_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_126d_v067_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 126d window."""
    res = _jerk(receivables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_126d_v068_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 126d window."""
    res = _jerk(_ratio(fcf, netinc), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_252d_v069_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 252d window."""
    res = _jerk(fcf, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_252d_v070_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_252d_v071_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 252d window."""
    res = _jerk(receivables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_252d_v072_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 252d window."""
    res = _jerk(_ratio(fcf, netinc), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_504d_v073_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 504d window."""
    res = _jerk(fcf, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_504d_v074_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_504d_v075_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 504d window."""
    res = _jerk(receivables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_504d_v076_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 504d window."""
    res = _jerk(_ratio(fcf, netinc), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_756d_v077_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 756d window."""
    res = _jerk(fcf, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_756d_v078_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_756d_v079_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 756d window."""
    res = _jerk(receivables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_756d_v080_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 756d window."""
    res = _jerk(_ratio(fcf, netinc), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_1008d_v081_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 1008d window."""
    res = _jerk(fcf, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_1008d_v082_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_1008d_v083_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 1008d window."""
    res = _jerk(receivables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_1008d_v084_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 1008d window."""
    res = _jerk(_ratio(fcf, netinc), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_jerk_1260d_v085_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 1260d window."""
    res = _jerk(fcf, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_jerk_1260d_v086_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_jerk_1260d_v087_signal(receivables):
    """Acceleration/Jerk for structural shifts for Raw level of receivables over 1260d window."""
    res = _jerk(receivables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_jerk_1260d_v088_signal(fcf, netinc):
    """Acceleration/Jerk for structural shifts for Free cash flow conversion of net income over 1260d window."""
    res = _jerk(_ratio(fcf, netinc), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_5d_v089_signal(fcf):
    """Normalized slope change for Raw level of fcf over 5d window."""
    res = (_slope_pct(fcf, 5).diff(5) / _sma(fcf.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_5d_v090_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_5d_v091_signal(receivables):
    """Normalized slope change for Raw level of receivables over 5d window."""
    res = (_slope_pct(receivables, 5).diff(5) / _sma(receivables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_5d_v092_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 5d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 5).diff(5) / _sma(_ratio(fcf, netinc).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_10d_v093_signal(fcf):
    """Normalized slope change for Raw level of fcf over 10d window."""
    res = (_slope_pct(fcf, 10).diff(10) / _sma(fcf.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_10d_v094_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_10d_v095_signal(receivables):
    """Normalized slope change for Raw level of receivables over 10d window."""
    res = (_slope_pct(receivables, 10).diff(10) / _sma(receivables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_10d_v096_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 10d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 10).diff(10) / _sma(_ratio(fcf, netinc).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_21d_v097_signal(fcf):
    """Normalized slope change for Raw level of fcf over 21d window."""
    res = (_slope_pct(fcf, 21).diff(21) / _sma(fcf.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_21d_v098_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_21d_v099_signal(receivables):
    """Normalized slope change for Raw level of receivables over 21d window."""
    res = (_slope_pct(receivables, 21).diff(21) / _sma(receivables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_21d_v100_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 21d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 21).diff(21) / _sma(_ratio(fcf, netinc).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_42d_v101_signal(fcf):
    """Normalized slope change for Raw level of fcf over 42d window."""
    res = (_slope_pct(fcf, 42).diff(42) / _sma(fcf.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_42d_v102_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_42d_v103_signal(receivables):
    """Normalized slope change for Raw level of receivables over 42d window."""
    res = (_slope_pct(receivables, 42).diff(42) / _sma(receivables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_42d_v104_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 42d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 42).diff(42) / _sma(_ratio(fcf, netinc).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_63d_v105_signal(fcf):
    """Normalized slope change for Raw level of fcf over 63d window."""
    res = (_slope_pct(fcf, 63).diff(63) / _sma(fcf.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_63d_v106_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_63d_v107_signal(receivables):
    """Normalized slope change for Raw level of receivables over 63d window."""
    res = (_slope_pct(receivables, 63).diff(63) / _sma(receivables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_63d_v108_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 63d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 63).diff(63) / _sma(_ratio(fcf, netinc).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_126d_v109_signal(fcf):
    """Normalized slope change for Raw level of fcf over 126d window."""
    res = (_slope_pct(fcf, 126).diff(126) / _sma(fcf.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_126d_v110_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_126d_v111_signal(receivables):
    """Normalized slope change for Raw level of receivables over 126d window."""
    res = (_slope_pct(receivables, 126).diff(126) / _sma(receivables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_126d_v112_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 126d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 126).diff(126) / _sma(_ratio(fcf, netinc).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_252d_v113_signal(fcf):
    """Normalized slope change for Raw level of fcf over 252d window."""
    res = (_slope_pct(fcf, 252).diff(252) / _sma(fcf.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_252d_v114_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_252d_v115_signal(receivables):
    """Normalized slope change for Raw level of receivables over 252d window."""
    res = (_slope_pct(receivables, 252).diff(252) / _sma(receivables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_252d_v116_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 252d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 252).diff(252) / _sma(_ratio(fcf, netinc).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_504d_v117_signal(fcf):
    """Normalized slope change for Raw level of fcf over 504d window."""
    res = (_slope_pct(fcf, 504).diff(504) / _sma(fcf.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_504d_v118_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_504d_v119_signal(receivables):
    """Normalized slope change for Raw level of receivables over 504d window."""
    res = (_slope_pct(receivables, 504).diff(504) / _sma(receivables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_504d_v120_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 504d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 504).diff(504) / _sma(_ratio(fcf, netinc).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_756d_v121_signal(fcf):
    """Normalized slope change for Raw level of fcf over 756d window."""
    res = (_slope_pct(fcf, 756).diff(756) / _sma(fcf.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_756d_v122_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_756d_v123_signal(receivables):
    """Normalized slope change for Raw level of receivables over 756d window."""
    res = (_slope_pct(receivables, 756).diff(756) / _sma(receivables.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_756d_v124_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 756d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 756).diff(756) / _sma(_ratio(fcf, netinc).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_1008d_v125_signal(fcf):
    """Normalized slope change for Raw level of fcf over 1008d window."""
    res = (_slope_pct(fcf, 1008).diff(1008) / _sma(fcf.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_1008d_v126_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_1008d_v127_signal(receivables):
    """Normalized slope change for Raw level of receivables over 1008d window."""
    res = (_slope_pct(receivables, 1008).diff(1008) / _sma(receivables.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_1008d_v128_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 1008d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 1008).diff(1008) / _sma(_ratio(fcf, netinc).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_slope_diff_norm_1260d_v129_signal(fcf):
    """Normalized slope change for Raw level of fcf over 1260d window."""
    res = (_slope_pct(fcf, 1260).diff(1260) / _sma(fcf.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_slope_diff_norm_1260d_v130_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_slope_diff_norm_1260d_v131_signal(receivables):
    """Normalized slope change for Raw level of receivables over 1260d window."""
    res = (_slope_pct(receivables, 1260).diff(1260) / _sma(receivables.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_slope_diff_norm_1260d_v132_signal(fcf, netinc):
    """Normalized slope change for Free cash flow conversion of net income over 1260d window."""
    res = (_slope_pct(_ratio(fcf, netinc), 1260).diff(1260) / _sma(_ratio(fcf, netinc).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_mom_z_5d_v133_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 5d window."""
    res = _z(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_mom_z_5d_v134_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_mom_z_5d_v135_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 5d window."""
    res = _z(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_mom_z_5d_v136_signal(fcf, netinc):
    """Relative momentum strength for Free cash flow conversion of net income over 5d window."""
    res = _z(_slope_pct(_ratio(fcf, netinc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_mom_z_10d_v137_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 10d window."""
    res = _z(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_mom_z_10d_v138_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_mom_z_10d_v139_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 10d window."""
    res = _z(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_mom_z_10d_v140_signal(fcf, netinc):
    """Relative momentum strength for Free cash flow conversion of net income over 10d window."""
    res = _z(_slope_pct(_ratio(fcf, netinc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_mom_z_21d_v141_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 21d window."""
    res = _z(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_mom_z_21d_v142_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_mom_z_21d_v143_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 21d window."""
    res = _z(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_mom_z_21d_v144_signal(fcf, netinc):
    """Relative momentum strength for Free cash flow conversion of net income over 21d window."""
    res = _z(_slope_pct(_ratio(fcf, netinc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_mom_z_42d_v145_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 42d window."""
    res = _z(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_mom_z_42d_v146_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_mom_z_42d_v147_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 42d window."""
    res = _z(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_mom_z_42d_v148_signal(fcf, netinc):
    """Relative momentum strength for Free cash flow conversion of net income over 42d window."""
    res = _z(_slope_pct(_ratio(fcf, netinc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_mom_z_63d_v149_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 63d window."""
    res = _z(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_mom_z_63d_v150_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f34_earnings_quality_fcf_slope_pct_5d_v001_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_5d_v001_signal},    "f34_earnings_quality_netinc_slope_pct_5d_v002_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_5d_v002_signal},    "f34_earnings_quality_receivables_slope_pct_5d_v003_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_5d_v003_signal},    "f34_earnings_quality_cash_quality_slope_pct_5d_v004_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_5d_v004_signal},    "f34_earnings_quality_fcf_slope_pct_10d_v005_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_10d_v005_signal},    "f34_earnings_quality_netinc_slope_pct_10d_v006_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_10d_v006_signal},    "f34_earnings_quality_receivables_slope_pct_10d_v007_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_10d_v007_signal},    "f34_earnings_quality_cash_quality_slope_pct_10d_v008_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_10d_v008_signal},    "f34_earnings_quality_fcf_slope_pct_21d_v009_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_21d_v009_signal},    "f34_earnings_quality_netinc_slope_pct_21d_v010_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_21d_v010_signal},    "f34_earnings_quality_receivables_slope_pct_21d_v011_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_21d_v011_signal},    "f34_earnings_quality_cash_quality_slope_pct_21d_v012_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_21d_v012_signal},    "f34_earnings_quality_fcf_slope_pct_42d_v013_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_42d_v013_signal},    "f34_earnings_quality_netinc_slope_pct_42d_v014_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_42d_v014_signal},    "f34_earnings_quality_receivables_slope_pct_42d_v015_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_42d_v015_signal},    "f34_earnings_quality_cash_quality_slope_pct_42d_v016_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_42d_v016_signal},    "f34_earnings_quality_fcf_slope_pct_63d_v017_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_63d_v017_signal},    "f34_earnings_quality_netinc_slope_pct_63d_v018_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_63d_v018_signal},    "f34_earnings_quality_receivables_slope_pct_63d_v019_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_63d_v019_signal},    "f34_earnings_quality_cash_quality_slope_pct_63d_v020_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_63d_v020_signal},    "f34_earnings_quality_fcf_slope_pct_126d_v021_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_126d_v021_signal},    "f34_earnings_quality_netinc_slope_pct_126d_v022_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_126d_v022_signal},    "f34_earnings_quality_receivables_slope_pct_126d_v023_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_126d_v023_signal},    "f34_earnings_quality_cash_quality_slope_pct_126d_v024_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_126d_v024_signal},    "f34_earnings_quality_fcf_slope_pct_252d_v025_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_252d_v025_signal},    "f34_earnings_quality_netinc_slope_pct_252d_v026_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_252d_v026_signal},    "f34_earnings_quality_receivables_slope_pct_252d_v027_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_252d_v027_signal},    "f34_earnings_quality_cash_quality_slope_pct_252d_v028_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_252d_v028_signal},    "f34_earnings_quality_fcf_slope_pct_504d_v029_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_504d_v029_signal},    "f34_earnings_quality_netinc_slope_pct_504d_v030_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_504d_v030_signal},    "f34_earnings_quality_receivables_slope_pct_504d_v031_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_504d_v031_signal},    "f34_earnings_quality_cash_quality_slope_pct_504d_v032_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_504d_v032_signal},    "f34_earnings_quality_fcf_slope_pct_756d_v033_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_756d_v033_signal},    "f34_earnings_quality_netinc_slope_pct_756d_v034_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_756d_v034_signal},    "f34_earnings_quality_receivables_slope_pct_756d_v035_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_756d_v035_signal},    "f34_earnings_quality_cash_quality_slope_pct_756d_v036_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_756d_v036_signal},    "f34_earnings_quality_fcf_slope_pct_1008d_v037_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_1008d_v037_signal},    "f34_earnings_quality_netinc_slope_pct_1008d_v038_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_1008d_v038_signal},    "f34_earnings_quality_receivables_slope_pct_1008d_v039_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_1008d_v039_signal},    "f34_earnings_quality_cash_quality_slope_pct_1008d_v040_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_1008d_v040_signal},    "f34_earnings_quality_fcf_slope_pct_1260d_v041_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_pct_1260d_v041_signal},    "f34_earnings_quality_netinc_slope_pct_1260d_v042_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_pct_1260d_v042_signal},    "f34_earnings_quality_receivables_slope_pct_1260d_v043_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_pct_1260d_v043_signal},    "f34_earnings_quality_cash_quality_slope_pct_1260d_v044_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_pct_1260d_v044_signal},    "f34_earnings_quality_fcf_jerk_5d_v045_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_5d_v045_signal},    "f34_earnings_quality_netinc_jerk_5d_v046_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_5d_v046_signal},    "f34_earnings_quality_receivables_jerk_5d_v047_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_5d_v047_signal},    "f34_earnings_quality_cash_quality_jerk_5d_v048_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_5d_v048_signal},    "f34_earnings_quality_fcf_jerk_10d_v049_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_10d_v049_signal},    "f34_earnings_quality_netinc_jerk_10d_v050_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_10d_v050_signal},    "f34_earnings_quality_receivables_jerk_10d_v051_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_10d_v051_signal},    "f34_earnings_quality_cash_quality_jerk_10d_v052_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_10d_v052_signal},    "f34_earnings_quality_fcf_jerk_21d_v053_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_21d_v053_signal},    "f34_earnings_quality_netinc_jerk_21d_v054_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_21d_v054_signal},    "f34_earnings_quality_receivables_jerk_21d_v055_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_21d_v055_signal},    "f34_earnings_quality_cash_quality_jerk_21d_v056_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_21d_v056_signal},    "f34_earnings_quality_fcf_jerk_42d_v057_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_42d_v057_signal},    "f34_earnings_quality_netinc_jerk_42d_v058_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_42d_v058_signal},    "f34_earnings_quality_receivables_jerk_42d_v059_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_42d_v059_signal},    "f34_earnings_quality_cash_quality_jerk_42d_v060_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_42d_v060_signal},    "f34_earnings_quality_fcf_jerk_63d_v061_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_63d_v061_signal},    "f34_earnings_quality_netinc_jerk_63d_v062_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_63d_v062_signal},    "f34_earnings_quality_receivables_jerk_63d_v063_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_63d_v063_signal},    "f34_earnings_quality_cash_quality_jerk_63d_v064_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_63d_v064_signal},    "f34_earnings_quality_fcf_jerk_126d_v065_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_126d_v065_signal},    "f34_earnings_quality_netinc_jerk_126d_v066_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_126d_v066_signal},    "f34_earnings_quality_receivables_jerk_126d_v067_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_126d_v067_signal},    "f34_earnings_quality_cash_quality_jerk_126d_v068_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_126d_v068_signal},    "f34_earnings_quality_fcf_jerk_252d_v069_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_252d_v069_signal},    "f34_earnings_quality_netinc_jerk_252d_v070_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_252d_v070_signal},    "f34_earnings_quality_receivables_jerk_252d_v071_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_252d_v071_signal},    "f34_earnings_quality_cash_quality_jerk_252d_v072_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_252d_v072_signal},    "f34_earnings_quality_fcf_jerk_504d_v073_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_504d_v073_signal},    "f34_earnings_quality_netinc_jerk_504d_v074_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_504d_v074_signal},    "f34_earnings_quality_receivables_jerk_504d_v075_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_504d_v075_signal},    "f34_earnings_quality_cash_quality_jerk_504d_v076_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_504d_v076_signal},    "f34_earnings_quality_fcf_jerk_756d_v077_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_756d_v077_signal},    "f34_earnings_quality_netinc_jerk_756d_v078_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_756d_v078_signal},    "f34_earnings_quality_receivables_jerk_756d_v079_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_756d_v079_signal},    "f34_earnings_quality_cash_quality_jerk_756d_v080_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_756d_v080_signal},    "f34_earnings_quality_fcf_jerk_1008d_v081_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_1008d_v081_signal},    "f34_earnings_quality_netinc_jerk_1008d_v082_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_1008d_v082_signal},    "f34_earnings_quality_receivables_jerk_1008d_v083_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_1008d_v083_signal},    "f34_earnings_quality_cash_quality_jerk_1008d_v084_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_1008d_v084_signal},    "f34_earnings_quality_fcf_jerk_1260d_v085_signal": {"inputs": [], "func": f34_earnings_quality_fcf_jerk_1260d_v085_signal},    "f34_earnings_quality_netinc_jerk_1260d_v086_signal": {"inputs": [], "func": f34_earnings_quality_netinc_jerk_1260d_v086_signal},    "f34_earnings_quality_receivables_jerk_1260d_v087_signal": {"inputs": [], "func": f34_earnings_quality_receivables_jerk_1260d_v087_signal},    "f34_earnings_quality_cash_quality_jerk_1260d_v088_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_jerk_1260d_v088_signal},    "f34_earnings_quality_fcf_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_5d_v089_signal},    "f34_earnings_quality_netinc_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_5d_v090_signal},    "f34_earnings_quality_receivables_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_5d_v091_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_5d_v092_signal},    "f34_earnings_quality_fcf_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_10d_v093_signal},    "f34_earnings_quality_netinc_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_10d_v094_signal},    "f34_earnings_quality_receivables_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_10d_v095_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_10d_v096_signal},    "f34_earnings_quality_fcf_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_21d_v097_signal},    "f34_earnings_quality_netinc_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_21d_v098_signal},    "f34_earnings_quality_receivables_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_21d_v099_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_21d_v100_signal},    "f34_earnings_quality_fcf_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_42d_v101_signal},    "f34_earnings_quality_netinc_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_42d_v102_signal},    "f34_earnings_quality_receivables_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_42d_v103_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_42d_v104_signal},    "f34_earnings_quality_fcf_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_63d_v105_signal},    "f34_earnings_quality_netinc_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_63d_v106_signal},    "f34_earnings_quality_receivables_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_63d_v107_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_63d_v108_signal},    "f34_earnings_quality_fcf_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_126d_v109_signal},    "f34_earnings_quality_netinc_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_126d_v110_signal},    "f34_earnings_quality_receivables_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_126d_v111_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_126d_v112_signal},    "f34_earnings_quality_fcf_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_252d_v113_signal},    "f34_earnings_quality_netinc_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_252d_v114_signal},    "f34_earnings_quality_receivables_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_252d_v115_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_252d_v116_signal},    "f34_earnings_quality_fcf_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_504d_v117_signal},    "f34_earnings_quality_netinc_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_504d_v118_signal},    "f34_earnings_quality_receivables_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_504d_v119_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_504d_v120_signal},    "f34_earnings_quality_fcf_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_756d_v121_signal},    "f34_earnings_quality_netinc_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_756d_v122_signal},    "f34_earnings_quality_receivables_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_756d_v123_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_756d_v124_signal},    "f34_earnings_quality_fcf_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_1008d_v125_signal},    "f34_earnings_quality_netinc_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_1008d_v126_signal},    "f34_earnings_quality_receivables_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_1008d_v127_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_1008d_v128_signal},    "f34_earnings_quality_fcf_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f34_earnings_quality_fcf_slope_diff_norm_1260d_v129_signal},    "f34_earnings_quality_netinc_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f34_earnings_quality_netinc_slope_diff_norm_1260d_v130_signal},    "f34_earnings_quality_receivables_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f34_earnings_quality_receivables_slope_diff_norm_1260d_v131_signal},    "f34_earnings_quality_cash_quality_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_slope_diff_norm_1260d_v132_signal},    "f34_earnings_quality_fcf_mom_z_5d_v133_signal": {"inputs": [], "func": f34_earnings_quality_fcf_mom_z_5d_v133_signal},    "f34_earnings_quality_netinc_mom_z_5d_v134_signal": {"inputs": [], "func": f34_earnings_quality_netinc_mom_z_5d_v134_signal},    "f34_earnings_quality_receivables_mom_z_5d_v135_signal": {"inputs": [], "func": f34_earnings_quality_receivables_mom_z_5d_v135_signal},    "f34_earnings_quality_cash_quality_mom_z_5d_v136_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_mom_z_5d_v136_signal},    "f34_earnings_quality_fcf_mom_z_10d_v137_signal": {"inputs": [], "func": f34_earnings_quality_fcf_mom_z_10d_v137_signal},    "f34_earnings_quality_netinc_mom_z_10d_v138_signal": {"inputs": [], "func": f34_earnings_quality_netinc_mom_z_10d_v138_signal},    "f34_earnings_quality_receivables_mom_z_10d_v139_signal": {"inputs": [], "func": f34_earnings_quality_receivables_mom_z_10d_v139_signal},    "f34_earnings_quality_cash_quality_mom_z_10d_v140_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_mom_z_10d_v140_signal},    "f34_earnings_quality_fcf_mom_z_21d_v141_signal": {"inputs": [], "func": f34_earnings_quality_fcf_mom_z_21d_v141_signal},    "f34_earnings_quality_netinc_mom_z_21d_v142_signal": {"inputs": [], "func": f34_earnings_quality_netinc_mom_z_21d_v142_signal},    "f34_earnings_quality_receivables_mom_z_21d_v143_signal": {"inputs": [], "func": f34_earnings_quality_receivables_mom_z_21d_v143_signal},    "f34_earnings_quality_cash_quality_mom_z_21d_v144_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_mom_z_21d_v144_signal},    "f34_earnings_quality_fcf_mom_z_42d_v145_signal": {"inputs": [], "func": f34_earnings_quality_fcf_mom_z_42d_v145_signal},    "f34_earnings_quality_netinc_mom_z_42d_v146_signal": {"inputs": [], "func": f34_earnings_quality_netinc_mom_z_42d_v146_signal},    "f34_earnings_quality_receivables_mom_z_42d_v147_signal": {"inputs": [], "func": f34_earnings_quality_receivables_mom_z_42d_v147_signal},    "f34_earnings_quality_cash_quality_mom_z_42d_v148_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_mom_z_42d_v148_signal},    "f34_earnings_quality_fcf_mom_z_63d_v149_signal": {"inputs": [], "func": f34_earnings_quality_fcf_mom_z_63d_v149_signal},    "f34_earnings_quality_netinc_mom_z_63d_v150_signal": {"inputs": [], "func": f34_earnings_quality_netinc_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 34...")
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
