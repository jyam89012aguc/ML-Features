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

def f43_payout_resilience_fcf_slope_pct_5d_v001_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 5d window."""
    res = _slope_pct(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_5d_v002_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_5d_v003_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 5d window."""
    res = _slope_pct(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_5d_v004_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 5d window."""
    res = _slope_pct(_ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_10d_v005_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 10d window."""
    res = _slope_pct(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_10d_v006_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_10d_v007_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 10d window."""
    res = _slope_pct(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_10d_v008_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 10d window."""
    res = _slope_pct(_ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_21d_v009_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 21d window."""
    res = _slope_pct(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_21d_v010_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_21d_v011_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 21d window."""
    res = _slope_pct(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_21d_v012_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 21d window."""
    res = _slope_pct(_ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_42d_v013_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 42d window."""
    res = _slope_pct(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_42d_v014_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_42d_v015_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 42d window."""
    res = _slope_pct(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_42d_v016_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 42d window."""
    res = _slope_pct(_ratio(fcf, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_63d_v017_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 63d window."""
    res = _slope_pct(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_63d_v018_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_63d_v019_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 63d window."""
    res = _slope_pct(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_63d_v020_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 63d window."""
    res = _slope_pct(_ratio(fcf, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_126d_v021_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 126d window."""
    res = _slope_pct(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_126d_v022_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_126d_v023_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 126d window."""
    res = _slope_pct(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_126d_v024_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 126d window."""
    res = _slope_pct(_ratio(fcf, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_252d_v025_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 252d window."""
    res = _slope_pct(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_252d_v026_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_252d_v027_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 252d window."""
    res = _slope_pct(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_252d_v028_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 252d window."""
    res = _slope_pct(_ratio(fcf, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_504d_v029_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 504d window."""
    res = _slope_pct(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_504d_v030_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_504d_v031_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 504d window."""
    res = _slope_pct(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_504d_v032_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 504d window."""
    res = _slope_pct(_ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_756d_v033_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 756d window."""
    res = _slope_pct(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_756d_v034_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_756d_v035_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 756d window."""
    res = _slope_pct(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_756d_v036_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 756d window."""
    res = _slope_pct(_ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_1008d_v037_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 1008d window."""
    res = _slope_pct(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_1008d_v038_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_1008d_v039_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 1008d window."""
    res = _slope_pct(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_1008d_v040_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 1008d window."""
    res = _slope_pct(_ratio(fcf, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_pct_1260d_v041_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 1260d window."""
    res = _slope_pct(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_pct_1260d_v042_signal(netinc):
    """Percentage slope for momentum for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_pct_1260d_v043_signal(debt):
    """Percentage slope for momentum for Raw level of debt over 1260d window."""
    res = _slope_pct(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_pct_1260d_v044_signal(fcf, debt):
    """Percentage slope for momentum for Cash flow coverage of total debt over 1260d window."""
    res = _slope_pct(_ratio(fcf, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_5d_v045_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 5d window."""
    res = _jerk(fcf, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_5d_v046_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_5d_v047_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 5d window."""
    res = _jerk(debt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_5d_v048_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 5d window."""
    res = _jerk(_ratio(fcf, debt), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_10d_v049_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 10d window."""
    res = _jerk(fcf, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_10d_v050_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_10d_v051_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 10d window."""
    res = _jerk(debt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_10d_v052_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 10d window."""
    res = _jerk(_ratio(fcf, debt), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_21d_v053_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 21d window."""
    res = _jerk(fcf, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_21d_v054_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_21d_v055_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 21d window."""
    res = _jerk(debt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_21d_v056_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 21d window."""
    res = _jerk(_ratio(fcf, debt), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_42d_v057_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 42d window."""
    res = _jerk(fcf, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_42d_v058_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_42d_v059_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 42d window."""
    res = _jerk(debt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_42d_v060_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 42d window."""
    res = _jerk(_ratio(fcf, debt), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_63d_v061_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 63d window."""
    res = _jerk(fcf, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_63d_v062_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_63d_v063_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 63d window."""
    res = _jerk(debt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_63d_v064_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 63d window."""
    res = _jerk(_ratio(fcf, debt), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_126d_v065_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 126d window."""
    res = _jerk(fcf, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_126d_v066_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_126d_v067_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 126d window."""
    res = _jerk(debt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_126d_v068_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 126d window."""
    res = _jerk(_ratio(fcf, debt), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_252d_v069_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 252d window."""
    res = _jerk(fcf, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_252d_v070_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_252d_v071_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 252d window."""
    res = _jerk(debt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_252d_v072_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 252d window."""
    res = _jerk(_ratio(fcf, debt), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_504d_v073_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 504d window."""
    res = _jerk(fcf, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_504d_v074_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_504d_v075_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 504d window."""
    res = _jerk(debt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_504d_v076_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 504d window."""
    res = _jerk(_ratio(fcf, debt), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_756d_v077_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 756d window."""
    res = _jerk(fcf, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_756d_v078_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_756d_v079_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 756d window."""
    res = _jerk(debt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_756d_v080_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 756d window."""
    res = _jerk(_ratio(fcf, debt), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_1008d_v081_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 1008d window."""
    res = _jerk(fcf, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_1008d_v082_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_1008d_v083_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 1008d window."""
    res = _jerk(debt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_1008d_v084_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 1008d window."""
    res = _jerk(_ratio(fcf, debt), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_jerk_1260d_v085_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 1260d window."""
    res = _jerk(fcf, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_jerk_1260d_v086_signal(netinc):
    """Acceleration/Jerk for structural shifts for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_jerk_1260d_v087_signal(debt):
    """Acceleration/Jerk for structural shifts for Raw level of debt over 1260d window."""
    res = _jerk(debt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_jerk_1260d_v088_signal(fcf, debt):
    """Acceleration/Jerk for structural shifts for Cash flow coverage of total debt over 1260d window."""
    res = _jerk(_ratio(fcf, debt), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_5d_v089_signal(fcf):
    """Normalized slope change for Raw level of fcf over 5d window."""
    res = (_slope_pct(fcf, 5).diff(5) / _sma(fcf.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_5d_v090_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_5d_v091_signal(debt):
    """Normalized slope change for Raw level of debt over 5d window."""
    res = (_slope_pct(debt, 5).diff(5) / _sma(debt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_5d_v092_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 5d window."""
    res = (_slope_pct(_ratio(fcf, debt), 5).diff(5) / _sma(_ratio(fcf, debt).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_10d_v093_signal(fcf):
    """Normalized slope change for Raw level of fcf over 10d window."""
    res = (_slope_pct(fcf, 10).diff(10) / _sma(fcf.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_10d_v094_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_10d_v095_signal(debt):
    """Normalized slope change for Raw level of debt over 10d window."""
    res = (_slope_pct(debt, 10).diff(10) / _sma(debt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_10d_v096_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 10d window."""
    res = (_slope_pct(_ratio(fcf, debt), 10).diff(10) / _sma(_ratio(fcf, debt).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_21d_v097_signal(fcf):
    """Normalized slope change for Raw level of fcf over 21d window."""
    res = (_slope_pct(fcf, 21).diff(21) / _sma(fcf.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_21d_v098_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_21d_v099_signal(debt):
    """Normalized slope change for Raw level of debt over 21d window."""
    res = (_slope_pct(debt, 21).diff(21) / _sma(debt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_21d_v100_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 21d window."""
    res = (_slope_pct(_ratio(fcf, debt), 21).diff(21) / _sma(_ratio(fcf, debt).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_42d_v101_signal(fcf):
    """Normalized slope change for Raw level of fcf over 42d window."""
    res = (_slope_pct(fcf, 42).diff(42) / _sma(fcf.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_42d_v102_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_42d_v103_signal(debt):
    """Normalized slope change for Raw level of debt over 42d window."""
    res = (_slope_pct(debt, 42).diff(42) / _sma(debt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_42d_v104_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 42d window."""
    res = (_slope_pct(_ratio(fcf, debt), 42).diff(42) / _sma(_ratio(fcf, debt).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_63d_v105_signal(fcf):
    """Normalized slope change for Raw level of fcf over 63d window."""
    res = (_slope_pct(fcf, 63).diff(63) / _sma(fcf.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_63d_v106_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_63d_v107_signal(debt):
    """Normalized slope change for Raw level of debt over 63d window."""
    res = (_slope_pct(debt, 63).diff(63) / _sma(debt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_63d_v108_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 63d window."""
    res = (_slope_pct(_ratio(fcf, debt), 63).diff(63) / _sma(_ratio(fcf, debt).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_126d_v109_signal(fcf):
    """Normalized slope change for Raw level of fcf over 126d window."""
    res = (_slope_pct(fcf, 126).diff(126) / _sma(fcf.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_126d_v110_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_126d_v111_signal(debt):
    """Normalized slope change for Raw level of debt over 126d window."""
    res = (_slope_pct(debt, 126).diff(126) / _sma(debt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_126d_v112_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 126d window."""
    res = (_slope_pct(_ratio(fcf, debt), 126).diff(126) / _sma(_ratio(fcf, debt).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_252d_v113_signal(fcf):
    """Normalized slope change for Raw level of fcf over 252d window."""
    res = (_slope_pct(fcf, 252).diff(252) / _sma(fcf.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_252d_v114_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_252d_v115_signal(debt):
    """Normalized slope change for Raw level of debt over 252d window."""
    res = (_slope_pct(debt, 252).diff(252) / _sma(debt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_252d_v116_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 252d window."""
    res = (_slope_pct(_ratio(fcf, debt), 252).diff(252) / _sma(_ratio(fcf, debt).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_504d_v117_signal(fcf):
    """Normalized slope change for Raw level of fcf over 504d window."""
    res = (_slope_pct(fcf, 504).diff(504) / _sma(fcf.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_504d_v118_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_504d_v119_signal(debt):
    """Normalized slope change for Raw level of debt over 504d window."""
    res = (_slope_pct(debt, 504).diff(504) / _sma(debt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_504d_v120_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 504d window."""
    res = (_slope_pct(_ratio(fcf, debt), 504).diff(504) / _sma(_ratio(fcf, debt).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_756d_v121_signal(fcf):
    """Normalized slope change for Raw level of fcf over 756d window."""
    res = (_slope_pct(fcf, 756).diff(756) / _sma(fcf.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_756d_v122_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_756d_v123_signal(debt):
    """Normalized slope change for Raw level of debt over 756d window."""
    res = (_slope_pct(debt, 756).diff(756) / _sma(debt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_756d_v124_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 756d window."""
    res = (_slope_pct(_ratio(fcf, debt), 756).diff(756) / _sma(_ratio(fcf, debt).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_1008d_v125_signal(fcf):
    """Normalized slope change for Raw level of fcf over 1008d window."""
    res = (_slope_pct(fcf, 1008).diff(1008) / _sma(fcf.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_1008d_v126_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_1008d_v127_signal(debt):
    """Normalized slope change for Raw level of debt over 1008d window."""
    res = (_slope_pct(debt, 1008).diff(1008) / _sma(debt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_1008d_v128_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 1008d window."""
    res = (_slope_pct(_ratio(fcf, debt), 1008).diff(1008) / _sma(_ratio(fcf, debt).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_slope_diff_norm_1260d_v129_signal(fcf):
    """Normalized slope change for Raw level of fcf over 1260d window."""
    res = (_slope_pct(fcf, 1260).diff(1260) / _sma(fcf.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_slope_diff_norm_1260d_v130_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_slope_diff_norm_1260d_v131_signal(debt):
    """Normalized slope change for Raw level of debt over 1260d window."""
    res = (_slope_pct(debt, 1260).diff(1260) / _sma(debt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_slope_diff_norm_1260d_v132_signal(fcf, debt):
    """Normalized slope change for Cash flow coverage of total debt over 1260d window."""
    res = (_slope_pct(_ratio(fcf, debt), 1260).diff(1260) / _sma(_ratio(fcf, debt).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_mom_z_5d_v133_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 5d window."""
    res = _z(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_mom_z_5d_v134_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_mom_z_5d_v135_signal(debt):
    """Relative momentum strength for Raw level of debt over 5d window."""
    res = _z(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_mom_z_5d_v136_signal(fcf, debt):
    """Relative momentum strength for Cash flow coverage of total debt over 5d window."""
    res = _z(_slope_pct(_ratio(fcf, debt), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_mom_z_10d_v137_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 10d window."""
    res = _z(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_mom_z_10d_v138_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_mom_z_10d_v139_signal(debt):
    """Relative momentum strength for Raw level of debt over 10d window."""
    res = _z(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_mom_z_10d_v140_signal(fcf, debt):
    """Relative momentum strength for Cash flow coverage of total debt over 10d window."""
    res = _z(_slope_pct(_ratio(fcf, debt), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_mom_z_21d_v141_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 21d window."""
    res = _z(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_mom_z_21d_v142_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_mom_z_21d_v143_signal(debt):
    """Relative momentum strength for Raw level of debt over 21d window."""
    res = _z(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_mom_z_21d_v144_signal(fcf, debt):
    """Relative momentum strength for Cash flow coverage of total debt over 21d window."""
    res = _z(_slope_pct(_ratio(fcf, debt), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_mom_z_42d_v145_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 42d window."""
    res = _z(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_mom_z_42d_v146_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_mom_z_42d_v147_signal(debt):
    """Relative momentum strength for Raw level of debt over 42d window."""
    res = _z(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_mom_z_42d_v148_signal(fcf, debt):
    """Relative momentum strength for Cash flow coverage of total debt over 42d window."""
    res = _z(_slope_pct(_ratio(fcf, debt), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_mom_z_63d_v149_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 63d window."""
    res = _z(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_mom_z_63d_v150_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f43_payout_resilience_fcf_slope_pct_5d_v001_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_5d_v001_signal},    "f43_payout_resilience_netinc_slope_pct_5d_v002_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_5d_v002_signal},    "f43_payout_resilience_debt_slope_pct_5d_v003_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_5d_v003_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_5d_v004_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_5d_v004_signal},    "f43_payout_resilience_fcf_slope_pct_10d_v005_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_10d_v005_signal},    "f43_payout_resilience_netinc_slope_pct_10d_v006_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_10d_v006_signal},    "f43_payout_resilience_debt_slope_pct_10d_v007_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_10d_v007_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_10d_v008_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_10d_v008_signal},    "f43_payout_resilience_fcf_slope_pct_21d_v009_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_21d_v009_signal},    "f43_payout_resilience_netinc_slope_pct_21d_v010_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_21d_v010_signal},    "f43_payout_resilience_debt_slope_pct_21d_v011_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_21d_v011_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_21d_v012_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_21d_v012_signal},    "f43_payout_resilience_fcf_slope_pct_42d_v013_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_42d_v013_signal},    "f43_payout_resilience_netinc_slope_pct_42d_v014_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_42d_v014_signal},    "f43_payout_resilience_debt_slope_pct_42d_v015_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_42d_v015_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_42d_v016_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_42d_v016_signal},    "f43_payout_resilience_fcf_slope_pct_63d_v017_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_63d_v017_signal},    "f43_payout_resilience_netinc_slope_pct_63d_v018_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_63d_v018_signal},    "f43_payout_resilience_debt_slope_pct_63d_v019_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_63d_v019_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_63d_v020_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_63d_v020_signal},    "f43_payout_resilience_fcf_slope_pct_126d_v021_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_126d_v021_signal},    "f43_payout_resilience_netinc_slope_pct_126d_v022_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_126d_v022_signal},    "f43_payout_resilience_debt_slope_pct_126d_v023_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_126d_v023_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_126d_v024_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_126d_v024_signal},    "f43_payout_resilience_fcf_slope_pct_252d_v025_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_252d_v025_signal},    "f43_payout_resilience_netinc_slope_pct_252d_v026_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_252d_v026_signal},    "f43_payout_resilience_debt_slope_pct_252d_v027_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_252d_v027_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_252d_v028_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_252d_v028_signal},    "f43_payout_resilience_fcf_slope_pct_504d_v029_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_504d_v029_signal},    "f43_payout_resilience_netinc_slope_pct_504d_v030_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_504d_v030_signal},    "f43_payout_resilience_debt_slope_pct_504d_v031_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_504d_v031_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_504d_v032_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_504d_v032_signal},    "f43_payout_resilience_fcf_slope_pct_756d_v033_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_756d_v033_signal},    "f43_payout_resilience_netinc_slope_pct_756d_v034_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_756d_v034_signal},    "f43_payout_resilience_debt_slope_pct_756d_v035_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_756d_v035_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_756d_v036_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_756d_v036_signal},    "f43_payout_resilience_fcf_slope_pct_1008d_v037_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_1008d_v037_signal},    "f43_payout_resilience_netinc_slope_pct_1008d_v038_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_1008d_v038_signal},    "f43_payout_resilience_debt_slope_pct_1008d_v039_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_1008d_v039_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_1008d_v040_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_1008d_v040_signal},    "f43_payout_resilience_fcf_slope_pct_1260d_v041_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_pct_1260d_v041_signal},    "f43_payout_resilience_netinc_slope_pct_1260d_v042_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_pct_1260d_v042_signal},    "f43_payout_resilience_debt_slope_pct_1260d_v043_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_pct_1260d_v043_signal},    "f43_payout_resilience_fcf_to_debt_slope_pct_1260d_v044_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_pct_1260d_v044_signal},    "f43_payout_resilience_fcf_jerk_5d_v045_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_5d_v045_signal},    "f43_payout_resilience_netinc_jerk_5d_v046_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_5d_v046_signal},    "f43_payout_resilience_debt_jerk_5d_v047_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_5d_v047_signal},    "f43_payout_resilience_fcf_to_debt_jerk_5d_v048_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_5d_v048_signal},    "f43_payout_resilience_fcf_jerk_10d_v049_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_10d_v049_signal},    "f43_payout_resilience_netinc_jerk_10d_v050_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_10d_v050_signal},    "f43_payout_resilience_debt_jerk_10d_v051_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_10d_v051_signal},    "f43_payout_resilience_fcf_to_debt_jerk_10d_v052_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_10d_v052_signal},    "f43_payout_resilience_fcf_jerk_21d_v053_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_21d_v053_signal},    "f43_payout_resilience_netinc_jerk_21d_v054_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_21d_v054_signal},    "f43_payout_resilience_debt_jerk_21d_v055_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_21d_v055_signal},    "f43_payout_resilience_fcf_to_debt_jerk_21d_v056_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_21d_v056_signal},    "f43_payout_resilience_fcf_jerk_42d_v057_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_42d_v057_signal},    "f43_payout_resilience_netinc_jerk_42d_v058_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_42d_v058_signal},    "f43_payout_resilience_debt_jerk_42d_v059_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_42d_v059_signal},    "f43_payout_resilience_fcf_to_debt_jerk_42d_v060_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_42d_v060_signal},    "f43_payout_resilience_fcf_jerk_63d_v061_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_63d_v061_signal},    "f43_payout_resilience_netinc_jerk_63d_v062_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_63d_v062_signal},    "f43_payout_resilience_debt_jerk_63d_v063_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_63d_v063_signal},    "f43_payout_resilience_fcf_to_debt_jerk_63d_v064_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_63d_v064_signal},    "f43_payout_resilience_fcf_jerk_126d_v065_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_126d_v065_signal},    "f43_payout_resilience_netinc_jerk_126d_v066_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_126d_v066_signal},    "f43_payout_resilience_debt_jerk_126d_v067_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_126d_v067_signal},    "f43_payout_resilience_fcf_to_debt_jerk_126d_v068_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_126d_v068_signal},    "f43_payout_resilience_fcf_jerk_252d_v069_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_252d_v069_signal},    "f43_payout_resilience_netinc_jerk_252d_v070_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_252d_v070_signal},    "f43_payout_resilience_debt_jerk_252d_v071_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_252d_v071_signal},    "f43_payout_resilience_fcf_to_debt_jerk_252d_v072_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_252d_v072_signal},    "f43_payout_resilience_fcf_jerk_504d_v073_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_504d_v073_signal},    "f43_payout_resilience_netinc_jerk_504d_v074_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_504d_v074_signal},    "f43_payout_resilience_debt_jerk_504d_v075_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_504d_v075_signal},    "f43_payout_resilience_fcf_to_debt_jerk_504d_v076_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_504d_v076_signal},    "f43_payout_resilience_fcf_jerk_756d_v077_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_756d_v077_signal},    "f43_payout_resilience_netinc_jerk_756d_v078_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_756d_v078_signal},    "f43_payout_resilience_debt_jerk_756d_v079_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_756d_v079_signal},    "f43_payout_resilience_fcf_to_debt_jerk_756d_v080_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_756d_v080_signal},    "f43_payout_resilience_fcf_jerk_1008d_v081_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_1008d_v081_signal},    "f43_payout_resilience_netinc_jerk_1008d_v082_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_1008d_v082_signal},    "f43_payout_resilience_debt_jerk_1008d_v083_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_1008d_v083_signal},    "f43_payout_resilience_fcf_to_debt_jerk_1008d_v084_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_1008d_v084_signal},    "f43_payout_resilience_fcf_jerk_1260d_v085_signal": {"inputs": [], "func": f43_payout_resilience_fcf_jerk_1260d_v085_signal},    "f43_payout_resilience_netinc_jerk_1260d_v086_signal": {"inputs": [], "func": f43_payout_resilience_netinc_jerk_1260d_v086_signal},    "f43_payout_resilience_debt_jerk_1260d_v087_signal": {"inputs": [], "func": f43_payout_resilience_debt_jerk_1260d_v087_signal},    "f43_payout_resilience_fcf_to_debt_jerk_1260d_v088_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_jerk_1260d_v088_signal},    "f43_payout_resilience_fcf_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_5d_v089_signal},    "f43_payout_resilience_netinc_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_5d_v090_signal},    "f43_payout_resilience_debt_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_5d_v091_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_5d_v092_signal},    "f43_payout_resilience_fcf_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_10d_v093_signal},    "f43_payout_resilience_netinc_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_10d_v094_signal},    "f43_payout_resilience_debt_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_10d_v095_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_10d_v096_signal},    "f43_payout_resilience_fcf_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_21d_v097_signal},    "f43_payout_resilience_netinc_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_21d_v098_signal},    "f43_payout_resilience_debt_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_21d_v099_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_21d_v100_signal},    "f43_payout_resilience_fcf_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_42d_v101_signal},    "f43_payout_resilience_netinc_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_42d_v102_signal},    "f43_payout_resilience_debt_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_42d_v103_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_42d_v104_signal},    "f43_payout_resilience_fcf_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_63d_v105_signal},    "f43_payout_resilience_netinc_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_63d_v106_signal},    "f43_payout_resilience_debt_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_63d_v107_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_63d_v108_signal},    "f43_payout_resilience_fcf_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_126d_v109_signal},    "f43_payout_resilience_netinc_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_126d_v110_signal},    "f43_payout_resilience_debt_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_126d_v111_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_126d_v112_signal},    "f43_payout_resilience_fcf_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_252d_v113_signal},    "f43_payout_resilience_netinc_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_252d_v114_signal},    "f43_payout_resilience_debt_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_252d_v115_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_252d_v116_signal},    "f43_payout_resilience_fcf_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_504d_v117_signal},    "f43_payout_resilience_netinc_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_504d_v118_signal},    "f43_payout_resilience_debt_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_504d_v119_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_504d_v120_signal},    "f43_payout_resilience_fcf_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_756d_v121_signal},    "f43_payout_resilience_netinc_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_756d_v122_signal},    "f43_payout_resilience_debt_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_756d_v123_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_756d_v124_signal},    "f43_payout_resilience_fcf_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_1008d_v125_signal},    "f43_payout_resilience_netinc_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_1008d_v126_signal},    "f43_payout_resilience_debt_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_1008d_v127_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_1008d_v128_signal},    "f43_payout_resilience_fcf_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f43_payout_resilience_fcf_slope_diff_norm_1260d_v129_signal},    "f43_payout_resilience_netinc_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f43_payout_resilience_netinc_slope_diff_norm_1260d_v130_signal},    "f43_payout_resilience_debt_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f43_payout_resilience_debt_slope_diff_norm_1260d_v131_signal},    "f43_payout_resilience_fcf_to_debt_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_slope_diff_norm_1260d_v132_signal},    "f43_payout_resilience_fcf_mom_z_5d_v133_signal": {"inputs": [], "func": f43_payout_resilience_fcf_mom_z_5d_v133_signal},    "f43_payout_resilience_netinc_mom_z_5d_v134_signal": {"inputs": [], "func": f43_payout_resilience_netinc_mom_z_5d_v134_signal},    "f43_payout_resilience_debt_mom_z_5d_v135_signal": {"inputs": [], "func": f43_payout_resilience_debt_mom_z_5d_v135_signal},    "f43_payout_resilience_fcf_to_debt_mom_z_5d_v136_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_mom_z_5d_v136_signal},    "f43_payout_resilience_fcf_mom_z_10d_v137_signal": {"inputs": [], "func": f43_payout_resilience_fcf_mom_z_10d_v137_signal},    "f43_payout_resilience_netinc_mom_z_10d_v138_signal": {"inputs": [], "func": f43_payout_resilience_netinc_mom_z_10d_v138_signal},    "f43_payout_resilience_debt_mom_z_10d_v139_signal": {"inputs": [], "func": f43_payout_resilience_debt_mom_z_10d_v139_signal},    "f43_payout_resilience_fcf_to_debt_mom_z_10d_v140_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_mom_z_10d_v140_signal},    "f43_payout_resilience_fcf_mom_z_21d_v141_signal": {"inputs": [], "func": f43_payout_resilience_fcf_mom_z_21d_v141_signal},    "f43_payout_resilience_netinc_mom_z_21d_v142_signal": {"inputs": [], "func": f43_payout_resilience_netinc_mom_z_21d_v142_signal},    "f43_payout_resilience_debt_mom_z_21d_v143_signal": {"inputs": [], "func": f43_payout_resilience_debt_mom_z_21d_v143_signal},    "f43_payout_resilience_fcf_to_debt_mom_z_21d_v144_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_mom_z_21d_v144_signal},    "f43_payout_resilience_fcf_mom_z_42d_v145_signal": {"inputs": [], "func": f43_payout_resilience_fcf_mom_z_42d_v145_signal},    "f43_payout_resilience_netinc_mom_z_42d_v146_signal": {"inputs": [], "func": f43_payout_resilience_netinc_mom_z_42d_v146_signal},    "f43_payout_resilience_debt_mom_z_42d_v147_signal": {"inputs": [], "func": f43_payout_resilience_debt_mom_z_42d_v147_signal},    "f43_payout_resilience_fcf_to_debt_mom_z_42d_v148_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_mom_z_42d_v148_signal},    "f43_payout_resilience_fcf_mom_z_63d_v149_signal": {"inputs": [], "func": f43_payout_resilience_fcf_mom_z_63d_v149_signal},    "f43_payout_resilience_netinc_mom_z_63d_v150_signal": {"inputs": [], "func": f43_payout_resilience_netinc_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "debt": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 43...")
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
