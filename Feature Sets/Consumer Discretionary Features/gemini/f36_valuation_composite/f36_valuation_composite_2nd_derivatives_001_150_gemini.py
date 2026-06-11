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

def f36_valuation_composite_pe_slope_pct_5d_v001_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 5d window."""
    res = _slope_pct(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_5d_v002_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 5d window."""
    res = _slope_pct(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_5d_v003_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 5d window."""
    res = _slope_pct(ps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_5d_v004_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 5d window."""
    res = _slope_pct(pe * ps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_10d_v005_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 10d window."""
    res = _slope_pct(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_10d_v006_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 10d window."""
    res = _slope_pct(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_10d_v007_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 10d window."""
    res = _slope_pct(ps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_10d_v008_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 10d window."""
    res = _slope_pct(pe * ps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_21d_v009_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 21d window."""
    res = _slope_pct(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_21d_v010_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 21d window."""
    res = _slope_pct(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_21d_v011_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 21d window."""
    res = _slope_pct(ps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_21d_v012_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 21d window."""
    res = _slope_pct(pe * ps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_42d_v013_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 42d window."""
    res = _slope_pct(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_42d_v014_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 42d window."""
    res = _slope_pct(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_42d_v015_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 42d window."""
    res = _slope_pct(ps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_42d_v016_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 42d window."""
    res = _slope_pct(pe * ps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_63d_v017_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 63d window."""
    res = _slope_pct(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_63d_v018_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 63d window."""
    res = _slope_pct(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_63d_v019_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 63d window."""
    res = _slope_pct(ps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_63d_v020_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 63d window."""
    res = _slope_pct(pe * ps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_126d_v021_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 126d window."""
    res = _slope_pct(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_126d_v022_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 126d window."""
    res = _slope_pct(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_126d_v023_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 126d window."""
    res = _slope_pct(ps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_126d_v024_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 126d window."""
    res = _slope_pct(pe * ps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_252d_v025_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 252d window."""
    res = _slope_pct(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_252d_v026_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 252d window."""
    res = _slope_pct(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_252d_v027_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 252d window."""
    res = _slope_pct(ps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_252d_v028_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 252d window."""
    res = _slope_pct(pe * ps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_504d_v029_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 504d window."""
    res = _slope_pct(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_504d_v030_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 504d window."""
    res = _slope_pct(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_504d_v031_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 504d window."""
    res = _slope_pct(ps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_504d_v032_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 504d window."""
    res = _slope_pct(pe * ps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_756d_v033_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 756d window."""
    res = _slope_pct(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_756d_v034_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 756d window."""
    res = _slope_pct(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_756d_v035_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 756d window."""
    res = _slope_pct(ps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_756d_v036_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 756d window."""
    res = _slope_pct(pe * ps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_1008d_v037_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 1008d window."""
    res = _slope_pct(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_1008d_v038_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 1008d window."""
    res = _slope_pct(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_1008d_v039_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 1008d window."""
    res = _slope_pct(ps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_1008d_v040_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 1008d window."""
    res = _slope_pct(pe * ps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_pct_1260d_v041_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 1260d window."""
    res = _slope_pct(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_pct_1260d_v042_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 1260d window."""
    res = _slope_pct(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_pct_1260d_v043_signal(ps):
    """Percentage slope for momentum for Raw level of ps over 1260d window."""
    res = _slope_pct(ps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_pct_1260d_v044_signal(pe, ps):
    """Percentage slope for momentum for Combined earnings and sales valuation index over 1260d window."""
    res = _slope_pct(pe * ps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_5d_v045_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 5d window."""
    res = _jerk(pe, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_5d_v046_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 5d window."""
    res = _jerk(pb, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_5d_v047_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 5d window."""
    res = _jerk(ps, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_5d_v048_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 5d window."""
    res = _jerk(pe * ps, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_10d_v049_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 10d window."""
    res = _jerk(pe, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_10d_v050_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 10d window."""
    res = _jerk(pb, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_10d_v051_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 10d window."""
    res = _jerk(ps, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_10d_v052_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 10d window."""
    res = _jerk(pe * ps, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_21d_v053_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 21d window."""
    res = _jerk(pe, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_21d_v054_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 21d window."""
    res = _jerk(pb, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_21d_v055_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 21d window."""
    res = _jerk(ps, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_21d_v056_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 21d window."""
    res = _jerk(pe * ps, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_42d_v057_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 42d window."""
    res = _jerk(pe, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_42d_v058_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 42d window."""
    res = _jerk(pb, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_42d_v059_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 42d window."""
    res = _jerk(ps, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_42d_v060_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 42d window."""
    res = _jerk(pe * ps, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_63d_v061_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 63d window."""
    res = _jerk(pe, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_63d_v062_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 63d window."""
    res = _jerk(pb, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_63d_v063_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 63d window."""
    res = _jerk(ps, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_63d_v064_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 63d window."""
    res = _jerk(pe * ps, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_126d_v065_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 126d window."""
    res = _jerk(pe, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_126d_v066_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 126d window."""
    res = _jerk(pb, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_126d_v067_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 126d window."""
    res = _jerk(ps, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_126d_v068_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 126d window."""
    res = _jerk(pe * ps, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_252d_v069_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 252d window."""
    res = _jerk(pe, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_252d_v070_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 252d window."""
    res = _jerk(pb, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_252d_v071_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 252d window."""
    res = _jerk(ps, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_252d_v072_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 252d window."""
    res = _jerk(pe * ps, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_504d_v073_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 504d window."""
    res = _jerk(pe, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_504d_v074_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 504d window."""
    res = _jerk(pb, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_504d_v075_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 504d window."""
    res = _jerk(ps, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_504d_v076_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 504d window."""
    res = _jerk(pe * ps, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_756d_v077_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 756d window."""
    res = _jerk(pe, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_756d_v078_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 756d window."""
    res = _jerk(pb, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_756d_v079_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 756d window."""
    res = _jerk(ps, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_756d_v080_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 756d window."""
    res = _jerk(pe * ps, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_1008d_v081_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 1008d window."""
    res = _jerk(pe, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_1008d_v082_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 1008d window."""
    res = _jerk(pb, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_1008d_v083_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 1008d window."""
    res = _jerk(ps, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_1008d_v084_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 1008d window."""
    res = _jerk(pe * ps, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_jerk_1260d_v085_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 1260d window."""
    res = _jerk(pe, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_jerk_1260d_v086_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 1260d window."""
    res = _jerk(pb, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_jerk_1260d_v087_signal(ps):
    """Acceleration/Jerk for structural shifts for Raw level of ps over 1260d window."""
    res = _jerk(ps, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_jerk_1260d_v088_signal(pe, ps):
    """Acceleration/Jerk for structural shifts for Combined earnings and sales valuation index over 1260d window."""
    res = _jerk(pe * ps, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_5d_v089_signal(pe):
    """Normalized slope change for Raw level of pe over 5d window."""
    res = (_slope_pct(pe, 5).diff(5) / _sma(pe.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_5d_v090_signal(pb):
    """Normalized slope change for Raw level of pb over 5d window."""
    res = (_slope_pct(pb, 5).diff(5) / _sma(pb.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_5d_v091_signal(ps):
    """Normalized slope change for Raw level of ps over 5d window."""
    res = (_slope_pct(ps, 5).diff(5) / _sma(ps.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_5d_v092_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 5d window."""
    res = (_slope_pct(pe * ps, 5).diff(5) / _sma(pe * ps.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_10d_v093_signal(pe):
    """Normalized slope change for Raw level of pe over 10d window."""
    res = (_slope_pct(pe, 10).diff(10) / _sma(pe.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_10d_v094_signal(pb):
    """Normalized slope change for Raw level of pb over 10d window."""
    res = (_slope_pct(pb, 10).diff(10) / _sma(pb.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_10d_v095_signal(ps):
    """Normalized slope change for Raw level of ps over 10d window."""
    res = (_slope_pct(ps, 10).diff(10) / _sma(ps.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_10d_v096_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 10d window."""
    res = (_slope_pct(pe * ps, 10).diff(10) / _sma(pe * ps.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_21d_v097_signal(pe):
    """Normalized slope change for Raw level of pe over 21d window."""
    res = (_slope_pct(pe, 21).diff(21) / _sma(pe.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_21d_v098_signal(pb):
    """Normalized slope change for Raw level of pb over 21d window."""
    res = (_slope_pct(pb, 21).diff(21) / _sma(pb.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_21d_v099_signal(ps):
    """Normalized slope change for Raw level of ps over 21d window."""
    res = (_slope_pct(ps, 21).diff(21) / _sma(ps.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_21d_v100_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 21d window."""
    res = (_slope_pct(pe * ps, 21).diff(21) / _sma(pe * ps.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_42d_v101_signal(pe):
    """Normalized slope change for Raw level of pe over 42d window."""
    res = (_slope_pct(pe, 42).diff(42) / _sma(pe.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_42d_v102_signal(pb):
    """Normalized slope change for Raw level of pb over 42d window."""
    res = (_slope_pct(pb, 42).diff(42) / _sma(pb.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_42d_v103_signal(ps):
    """Normalized slope change for Raw level of ps over 42d window."""
    res = (_slope_pct(ps, 42).diff(42) / _sma(ps.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_42d_v104_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 42d window."""
    res = (_slope_pct(pe * ps, 42).diff(42) / _sma(pe * ps.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_63d_v105_signal(pe):
    """Normalized slope change for Raw level of pe over 63d window."""
    res = (_slope_pct(pe, 63).diff(63) / _sma(pe.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_63d_v106_signal(pb):
    """Normalized slope change for Raw level of pb over 63d window."""
    res = (_slope_pct(pb, 63).diff(63) / _sma(pb.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_63d_v107_signal(ps):
    """Normalized slope change for Raw level of ps over 63d window."""
    res = (_slope_pct(ps, 63).diff(63) / _sma(ps.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_63d_v108_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 63d window."""
    res = (_slope_pct(pe * ps, 63).diff(63) / _sma(pe * ps.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_126d_v109_signal(pe):
    """Normalized slope change for Raw level of pe over 126d window."""
    res = (_slope_pct(pe, 126).diff(126) / _sma(pe.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_126d_v110_signal(pb):
    """Normalized slope change for Raw level of pb over 126d window."""
    res = (_slope_pct(pb, 126).diff(126) / _sma(pb.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_126d_v111_signal(ps):
    """Normalized slope change for Raw level of ps over 126d window."""
    res = (_slope_pct(ps, 126).diff(126) / _sma(ps.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_126d_v112_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 126d window."""
    res = (_slope_pct(pe * ps, 126).diff(126) / _sma(pe * ps.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_252d_v113_signal(pe):
    """Normalized slope change for Raw level of pe over 252d window."""
    res = (_slope_pct(pe, 252).diff(252) / _sma(pe.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_252d_v114_signal(pb):
    """Normalized slope change for Raw level of pb over 252d window."""
    res = (_slope_pct(pb, 252).diff(252) / _sma(pb.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_252d_v115_signal(ps):
    """Normalized slope change for Raw level of ps over 252d window."""
    res = (_slope_pct(ps, 252).diff(252) / _sma(ps.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_252d_v116_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 252d window."""
    res = (_slope_pct(pe * ps, 252).diff(252) / _sma(pe * ps.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_504d_v117_signal(pe):
    """Normalized slope change for Raw level of pe over 504d window."""
    res = (_slope_pct(pe, 504).diff(504) / _sma(pe.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_504d_v118_signal(pb):
    """Normalized slope change for Raw level of pb over 504d window."""
    res = (_slope_pct(pb, 504).diff(504) / _sma(pb.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_504d_v119_signal(ps):
    """Normalized slope change for Raw level of ps over 504d window."""
    res = (_slope_pct(ps, 504).diff(504) / _sma(ps.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_504d_v120_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 504d window."""
    res = (_slope_pct(pe * ps, 504).diff(504) / _sma(pe * ps.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_756d_v121_signal(pe):
    """Normalized slope change for Raw level of pe over 756d window."""
    res = (_slope_pct(pe, 756).diff(756) / _sma(pe.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_756d_v122_signal(pb):
    """Normalized slope change for Raw level of pb over 756d window."""
    res = (_slope_pct(pb, 756).diff(756) / _sma(pb.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_756d_v123_signal(ps):
    """Normalized slope change for Raw level of ps over 756d window."""
    res = (_slope_pct(ps, 756).diff(756) / _sma(ps.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_756d_v124_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 756d window."""
    res = (_slope_pct(pe * ps, 756).diff(756) / _sma(pe * ps.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_1008d_v125_signal(pe):
    """Normalized slope change for Raw level of pe over 1008d window."""
    res = (_slope_pct(pe, 1008).diff(1008) / _sma(pe.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_1008d_v126_signal(pb):
    """Normalized slope change for Raw level of pb over 1008d window."""
    res = (_slope_pct(pb, 1008).diff(1008) / _sma(pb.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_1008d_v127_signal(ps):
    """Normalized slope change for Raw level of ps over 1008d window."""
    res = (_slope_pct(ps, 1008).diff(1008) / _sma(ps.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_1008d_v128_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 1008d window."""
    res = (_slope_pct(pe * ps, 1008).diff(1008) / _sma(pe * ps.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_slope_diff_norm_1260d_v129_signal(pe):
    """Normalized slope change for Raw level of pe over 1260d window."""
    res = (_slope_pct(pe, 1260).diff(1260) / _sma(pe.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_slope_diff_norm_1260d_v130_signal(pb):
    """Normalized slope change for Raw level of pb over 1260d window."""
    res = (_slope_pct(pb, 1260).diff(1260) / _sma(pb.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_slope_diff_norm_1260d_v131_signal(ps):
    """Normalized slope change for Raw level of ps over 1260d window."""
    res = (_slope_pct(ps, 1260).diff(1260) / _sma(ps.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_slope_diff_norm_1260d_v132_signal(pe, ps):
    """Normalized slope change for Combined earnings and sales valuation index over 1260d window."""
    res = (_slope_pct(pe * ps, 1260).diff(1260) / _sma(pe * ps.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_mom_z_5d_v133_signal(pe):
    """Relative momentum strength for Raw level of pe over 5d window."""
    res = _z(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_mom_z_5d_v134_signal(pb):
    """Relative momentum strength for Raw level of pb over 5d window."""
    res = _z(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_mom_z_5d_v135_signal(ps):
    """Relative momentum strength for Raw level of ps over 5d window."""
    res = _z(_slope_pct(ps, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_mom_z_5d_v136_signal(pe, ps):
    """Relative momentum strength for Combined earnings and sales valuation index over 5d window."""
    res = _z(_slope_pct(pe * ps, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_mom_z_10d_v137_signal(pe):
    """Relative momentum strength for Raw level of pe over 10d window."""
    res = _z(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_mom_z_10d_v138_signal(pb):
    """Relative momentum strength for Raw level of pb over 10d window."""
    res = _z(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_mom_z_10d_v139_signal(ps):
    """Relative momentum strength for Raw level of ps over 10d window."""
    res = _z(_slope_pct(ps, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_mom_z_10d_v140_signal(pe, ps):
    """Relative momentum strength for Combined earnings and sales valuation index over 10d window."""
    res = _z(_slope_pct(pe * ps, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_mom_z_21d_v141_signal(pe):
    """Relative momentum strength for Raw level of pe over 21d window."""
    res = _z(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_mom_z_21d_v142_signal(pb):
    """Relative momentum strength for Raw level of pb over 21d window."""
    res = _z(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_mom_z_21d_v143_signal(ps):
    """Relative momentum strength for Raw level of ps over 21d window."""
    res = _z(_slope_pct(ps, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_mom_z_21d_v144_signal(pe, ps):
    """Relative momentum strength for Combined earnings and sales valuation index over 21d window."""
    res = _z(_slope_pct(pe * ps, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_mom_z_42d_v145_signal(pe):
    """Relative momentum strength for Raw level of pe over 42d window."""
    res = _z(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_mom_z_42d_v146_signal(pb):
    """Relative momentum strength for Raw level of pb over 42d window."""
    res = _z(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_ps_mom_z_42d_v147_signal(ps):
    """Relative momentum strength for Raw level of ps over 42d window."""
    res = _z(_slope_pct(ps, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_value_index_mom_z_42d_v148_signal(pe, ps):
    """Relative momentum strength for Combined earnings and sales valuation index over 42d window."""
    res = _z(_slope_pct(pe * ps, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pe_mom_z_63d_v149_signal(pe):
    """Relative momentum strength for Raw level of pe over 63d window."""
    res = _z(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_valuation_composite_pb_mom_z_63d_v150_signal(pb):
    """Relative momentum strength for Raw level of pb over 63d window."""
    res = _z(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f36_valuation_composite_pe_slope_pct_5d_v001_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_5d_v001_signal},    "f36_valuation_composite_pb_slope_pct_5d_v002_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_5d_v002_signal},    "f36_valuation_composite_ps_slope_pct_5d_v003_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_5d_v003_signal},    "f36_valuation_composite_value_index_slope_pct_5d_v004_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_5d_v004_signal},    "f36_valuation_composite_pe_slope_pct_10d_v005_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_10d_v005_signal},    "f36_valuation_composite_pb_slope_pct_10d_v006_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_10d_v006_signal},    "f36_valuation_composite_ps_slope_pct_10d_v007_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_10d_v007_signal},    "f36_valuation_composite_value_index_slope_pct_10d_v008_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_10d_v008_signal},    "f36_valuation_composite_pe_slope_pct_21d_v009_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_21d_v009_signal},    "f36_valuation_composite_pb_slope_pct_21d_v010_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_21d_v010_signal},    "f36_valuation_composite_ps_slope_pct_21d_v011_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_21d_v011_signal},    "f36_valuation_composite_value_index_slope_pct_21d_v012_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_21d_v012_signal},    "f36_valuation_composite_pe_slope_pct_42d_v013_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_42d_v013_signal},    "f36_valuation_composite_pb_slope_pct_42d_v014_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_42d_v014_signal},    "f36_valuation_composite_ps_slope_pct_42d_v015_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_42d_v015_signal},    "f36_valuation_composite_value_index_slope_pct_42d_v016_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_42d_v016_signal},    "f36_valuation_composite_pe_slope_pct_63d_v017_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_63d_v017_signal},    "f36_valuation_composite_pb_slope_pct_63d_v018_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_63d_v018_signal},    "f36_valuation_composite_ps_slope_pct_63d_v019_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_63d_v019_signal},    "f36_valuation_composite_value_index_slope_pct_63d_v020_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_63d_v020_signal},    "f36_valuation_composite_pe_slope_pct_126d_v021_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_126d_v021_signal},    "f36_valuation_composite_pb_slope_pct_126d_v022_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_126d_v022_signal},    "f36_valuation_composite_ps_slope_pct_126d_v023_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_126d_v023_signal},    "f36_valuation_composite_value_index_slope_pct_126d_v024_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_126d_v024_signal},    "f36_valuation_composite_pe_slope_pct_252d_v025_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_252d_v025_signal},    "f36_valuation_composite_pb_slope_pct_252d_v026_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_252d_v026_signal},    "f36_valuation_composite_ps_slope_pct_252d_v027_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_252d_v027_signal},    "f36_valuation_composite_value_index_slope_pct_252d_v028_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_252d_v028_signal},    "f36_valuation_composite_pe_slope_pct_504d_v029_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_504d_v029_signal},    "f36_valuation_composite_pb_slope_pct_504d_v030_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_504d_v030_signal},    "f36_valuation_composite_ps_slope_pct_504d_v031_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_504d_v031_signal},    "f36_valuation_composite_value_index_slope_pct_504d_v032_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_504d_v032_signal},    "f36_valuation_composite_pe_slope_pct_756d_v033_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_756d_v033_signal},    "f36_valuation_composite_pb_slope_pct_756d_v034_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_756d_v034_signal},    "f36_valuation_composite_ps_slope_pct_756d_v035_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_756d_v035_signal},    "f36_valuation_composite_value_index_slope_pct_756d_v036_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_756d_v036_signal},    "f36_valuation_composite_pe_slope_pct_1008d_v037_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_1008d_v037_signal},    "f36_valuation_composite_pb_slope_pct_1008d_v038_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_1008d_v038_signal},    "f36_valuation_composite_ps_slope_pct_1008d_v039_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_1008d_v039_signal},    "f36_valuation_composite_value_index_slope_pct_1008d_v040_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_1008d_v040_signal},    "f36_valuation_composite_pe_slope_pct_1260d_v041_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_pct_1260d_v041_signal},    "f36_valuation_composite_pb_slope_pct_1260d_v042_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_pct_1260d_v042_signal},    "f36_valuation_composite_ps_slope_pct_1260d_v043_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_pct_1260d_v043_signal},    "f36_valuation_composite_value_index_slope_pct_1260d_v044_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_pct_1260d_v044_signal},    "f36_valuation_composite_pe_jerk_5d_v045_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_5d_v045_signal},    "f36_valuation_composite_pb_jerk_5d_v046_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_5d_v046_signal},    "f36_valuation_composite_ps_jerk_5d_v047_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_5d_v047_signal},    "f36_valuation_composite_value_index_jerk_5d_v048_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_5d_v048_signal},    "f36_valuation_composite_pe_jerk_10d_v049_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_10d_v049_signal},    "f36_valuation_composite_pb_jerk_10d_v050_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_10d_v050_signal},    "f36_valuation_composite_ps_jerk_10d_v051_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_10d_v051_signal},    "f36_valuation_composite_value_index_jerk_10d_v052_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_10d_v052_signal},    "f36_valuation_composite_pe_jerk_21d_v053_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_21d_v053_signal},    "f36_valuation_composite_pb_jerk_21d_v054_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_21d_v054_signal},    "f36_valuation_composite_ps_jerk_21d_v055_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_21d_v055_signal},    "f36_valuation_composite_value_index_jerk_21d_v056_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_21d_v056_signal},    "f36_valuation_composite_pe_jerk_42d_v057_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_42d_v057_signal},    "f36_valuation_composite_pb_jerk_42d_v058_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_42d_v058_signal},    "f36_valuation_composite_ps_jerk_42d_v059_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_42d_v059_signal},    "f36_valuation_composite_value_index_jerk_42d_v060_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_42d_v060_signal},    "f36_valuation_composite_pe_jerk_63d_v061_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_63d_v061_signal},    "f36_valuation_composite_pb_jerk_63d_v062_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_63d_v062_signal},    "f36_valuation_composite_ps_jerk_63d_v063_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_63d_v063_signal},    "f36_valuation_composite_value_index_jerk_63d_v064_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_63d_v064_signal},    "f36_valuation_composite_pe_jerk_126d_v065_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_126d_v065_signal},    "f36_valuation_composite_pb_jerk_126d_v066_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_126d_v066_signal},    "f36_valuation_composite_ps_jerk_126d_v067_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_126d_v067_signal},    "f36_valuation_composite_value_index_jerk_126d_v068_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_126d_v068_signal},    "f36_valuation_composite_pe_jerk_252d_v069_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_252d_v069_signal},    "f36_valuation_composite_pb_jerk_252d_v070_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_252d_v070_signal},    "f36_valuation_composite_ps_jerk_252d_v071_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_252d_v071_signal},    "f36_valuation_composite_value_index_jerk_252d_v072_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_252d_v072_signal},    "f36_valuation_composite_pe_jerk_504d_v073_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_504d_v073_signal},    "f36_valuation_composite_pb_jerk_504d_v074_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_504d_v074_signal},    "f36_valuation_composite_ps_jerk_504d_v075_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_504d_v075_signal},    "f36_valuation_composite_value_index_jerk_504d_v076_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_504d_v076_signal},    "f36_valuation_composite_pe_jerk_756d_v077_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_756d_v077_signal},    "f36_valuation_composite_pb_jerk_756d_v078_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_756d_v078_signal},    "f36_valuation_composite_ps_jerk_756d_v079_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_756d_v079_signal},    "f36_valuation_composite_value_index_jerk_756d_v080_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_756d_v080_signal},    "f36_valuation_composite_pe_jerk_1008d_v081_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_1008d_v081_signal},    "f36_valuation_composite_pb_jerk_1008d_v082_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_1008d_v082_signal},    "f36_valuation_composite_ps_jerk_1008d_v083_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_1008d_v083_signal},    "f36_valuation_composite_value_index_jerk_1008d_v084_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_1008d_v084_signal},    "f36_valuation_composite_pe_jerk_1260d_v085_signal": {"inputs": [], "func": f36_valuation_composite_pe_jerk_1260d_v085_signal},    "f36_valuation_composite_pb_jerk_1260d_v086_signal": {"inputs": [], "func": f36_valuation_composite_pb_jerk_1260d_v086_signal},    "f36_valuation_composite_ps_jerk_1260d_v087_signal": {"inputs": [], "func": f36_valuation_composite_ps_jerk_1260d_v087_signal},    "f36_valuation_composite_value_index_jerk_1260d_v088_signal": {"inputs": [], "func": f36_valuation_composite_value_index_jerk_1260d_v088_signal},    "f36_valuation_composite_pe_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_5d_v089_signal},    "f36_valuation_composite_pb_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_5d_v090_signal},    "f36_valuation_composite_ps_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_5d_v091_signal},    "f36_valuation_composite_value_index_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_5d_v092_signal},    "f36_valuation_composite_pe_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_10d_v093_signal},    "f36_valuation_composite_pb_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_10d_v094_signal},    "f36_valuation_composite_ps_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_10d_v095_signal},    "f36_valuation_composite_value_index_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_10d_v096_signal},    "f36_valuation_composite_pe_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_21d_v097_signal},    "f36_valuation_composite_pb_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_21d_v098_signal},    "f36_valuation_composite_ps_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_21d_v099_signal},    "f36_valuation_composite_value_index_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_21d_v100_signal},    "f36_valuation_composite_pe_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_42d_v101_signal},    "f36_valuation_composite_pb_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_42d_v102_signal},    "f36_valuation_composite_ps_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_42d_v103_signal},    "f36_valuation_composite_value_index_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_42d_v104_signal},    "f36_valuation_composite_pe_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_63d_v105_signal},    "f36_valuation_composite_pb_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_63d_v106_signal},    "f36_valuation_composite_ps_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_63d_v107_signal},    "f36_valuation_composite_value_index_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_63d_v108_signal},    "f36_valuation_composite_pe_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_126d_v109_signal},    "f36_valuation_composite_pb_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_126d_v110_signal},    "f36_valuation_composite_ps_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_126d_v111_signal},    "f36_valuation_composite_value_index_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_126d_v112_signal},    "f36_valuation_composite_pe_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_252d_v113_signal},    "f36_valuation_composite_pb_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_252d_v114_signal},    "f36_valuation_composite_ps_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_252d_v115_signal},    "f36_valuation_composite_value_index_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_252d_v116_signal},    "f36_valuation_composite_pe_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_504d_v117_signal},    "f36_valuation_composite_pb_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_504d_v118_signal},    "f36_valuation_composite_ps_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_504d_v119_signal},    "f36_valuation_composite_value_index_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_504d_v120_signal},    "f36_valuation_composite_pe_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_756d_v121_signal},    "f36_valuation_composite_pb_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_756d_v122_signal},    "f36_valuation_composite_ps_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_756d_v123_signal},    "f36_valuation_composite_value_index_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_756d_v124_signal},    "f36_valuation_composite_pe_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_1008d_v125_signal},    "f36_valuation_composite_pb_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_1008d_v126_signal},    "f36_valuation_composite_ps_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_1008d_v127_signal},    "f36_valuation_composite_value_index_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_1008d_v128_signal},    "f36_valuation_composite_pe_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f36_valuation_composite_pe_slope_diff_norm_1260d_v129_signal},    "f36_valuation_composite_pb_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f36_valuation_composite_pb_slope_diff_norm_1260d_v130_signal},    "f36_valuation_composite_ps_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f36_valuation_composite_ps_slope_diff_norm_1260d_v131_signal},    "f36_valuation_composite_value_index_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f36_valuation_composite_value_index_slope_diff_norm_1260d_v132_signal},    "f36_valuation_composite_pe_mom_z_5d_v133_signal": {"inputs": [], "func": f36_valuation_composite_pe_mom_z_5d_v133_signal},    "f36_valuation_composite_pb_mom_z_5d_v134_signal": {"inputs": [], "func": f36_valuation_composite_pb_mom_z_5d_v134_signal},    "f36_valuation_composite_ps_mom_z_5d_v135_signal": {"inputs": [], "func": f36_valuation_composite_ps_mom_z_5d_v135_signal},    "f36_valuation_composite_value_index_mom_z_5d_v136_signal": {"inputs": [], "func": f36_valuation_composite_value_index_mom_z_5d_v136_signal},    "f36_valuation_composite_pe_mom_z_10d_v137_signal": {"inputs": [], "func": f36_valuation_composite_pe_mom_z_10d_v137_signal},    "f36_valuation_composite_pb_mom_z_10d_v138_signal": {"inputs": [], "func": f36_valuation_composite_pb_mom_z_10d_v138_signal},    "f36_valuation_composite_ps_mom_z_10d_v139_signal": {"inputs": [], "func": f36_valuation_composite_ps_mom_z_10d_v139_signal},    "f36_valuation_composite_value_index_mom_z_10d_v140_signal": {"inputs": [], "func": f36_valuation_composite_value_index_mom_z_10d_v140_signal},    "f36_valuation_composite_pe_mom_z_21d_v141_signal": {"inputs": [], "func": f36_valuation_composite_pe_mom_z_21d_v141_signal},    "f36_valuation_composite_pb_mom_z_21d_v142_signal": {"inputs": [], "func": f36_valuation_composite_pb_mom_z_21d_v142_signal},    "f36_valuation_composite_ps_mom_z_21d_v143_signal": {"inputs": [], "func": f36_valuation_composite_ps_mom_z_21d_v143_signal},    "f36_valuation_composite_value_index_mom_z_21d_v144_signal": {"inputs": [], "func": f36_valuation_composite_value_index_mom_z_21d_v144_signal},    "f36_valuation_composite_pe_mom_z_42d_v145_signal": {"inputs": [], "func": f36_valuation_composite_pe_mom_z_42d_v145_signal},    "f36_valuation_composite_pb_mom_z_42d_v146_signal": {"inputs": [], "func": f36_valuation_composite_pb_mom_z_42d_v146_signal},    "f36_valuation_composite_ps_mom_z_42d_v147_signal": {"inputs": [], "func": f36_valuation_composite_ps_mom_z_42d_v147_signal},    "f36_valuation_composite_value_index_mom_z_42d_v148_signal": {"inputs": [], "func": f36_valuation_composite_value_index_mom_z_42d_v148_signal},    "f36_valuation_composite_pe_mom_z_63d_v149_signal": {"inputs": [], "func": f36_valuation_composite_pe_mom_z_63d_v149_signal},    "f36_valuation_composite_pb_mom_z_63d_v150_signal": {"inputs": [], "func": f36_valuation_composite_pb_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 36...")
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
