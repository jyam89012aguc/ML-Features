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

def f46_valuation_reversion_fin_pb_slope_pct_5d_v001_signal(pb):
    """Percentage slope for Raw level of pb over 5d window."""
    res = _slope_pct(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_5d_v002_signal(pe):
    """Percentage slope for Raw level of pe over 5d window."""
    res = _slope_pct(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_5d_v003_signal(ev):
    """Percentage slope for Raw level of ev over 5d window."""
    res = _slope_pct(ev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_5d_v004_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 5d window."""
    res = _slope_pct(_z(pb, 1260), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_10d_v005_signal(pb):
    """Percentage slope for Raw level of pb over 10d window."""
    res = _slope_pct(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_10d_v006_signal(pe):
    """Percentage slope for Raw level of pe over 10d window."""
    res = _slope_pct(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_10d_v007_signal(ev):
    """Percentage slope for Raw level of ev over 10d window."""
    res = _slope_pct(ev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_10d_v008_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 10d window."""
    res = _slope_pct(_z(pb, 1260), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_21d_v009_signal(pb):
    """Percentage slope for Raw level of pb over 21d window."""
    res = _slope_pct(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_21d_v010_signal(pe):
    """Percentage slope for Raw level of pe over 21d window."""
    res = _slope_pct(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_21d_v011_signal(ev):
    """Percentage slope for Raw level of ev over 21d window."""
    res = _slope_pct(ev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_21d_v012_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 21d window."""
    res = _slope_pct(_z(pb, 1260), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_42d_v013_signal(pb):
    """Percentage slope for Raw level of pb over 42d window."""
    res = _slope_pct(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_42d_v014_signal(pe):
    """Percentage slope for Raw level of pe over 42d window."""
    res = _slope_pct(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_42d_v015_signal(ev):
    """Percentage slope for Raw level of ev over 42d window."""
    res = _slope_pct(ev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_42d_v016_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 42d window."""
    res = _slope_pct(_z(pb, 1260), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_63d_v017_signal(pb):
    """Percentage slope for Raw level of pb over 63d window."""
    res = _slope_pct(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_63d_v018_signal(pe):
    """Percentage slope for Raw level of pe over 63d window."""
    res = _slope_pct(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_63d_v019_signal(ev):
    """Percentage slope for Raw level of ev over 63d window."""
    res = _slope_pct(ev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_63d_v020_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 63d window."""
    res = _slope_pct(_z(pb, 1260), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_126d_v021_signal(pb):
    """Percentage slope for Raw level of pb over 126d window."""
    res = _slope_pct(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_126d_v022_signal(pe):
    """Percentage slope for Raw level of pe over 126d window."""
    res = _slope_pct(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_126d_v023_signal(ev):
    """Percentage slope for Raw level of ev over 126d window."""
    res = _slope_pct(ev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_126d_v024_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 126d window."""
    res = _slope_pct(_z(pb, 1260), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_252d_v025_signal(pb):
    """Percentage slope for Raw level of pb over 252d window."""
    res = _slope_pct(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_252d_v026_signal(pe):
    """Percentage slope for Raw level of pe over 252d window."""
    res = _slope_pct(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_252d_v027_signal(ev):
    """Percentage slope for Raw level of ev over 252d window."""
    res = _slope_pct(ev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_252d_v028_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 252d window."""
    res = _slope_pct(_z(pb, 1260), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_504d_v029_signal(pb):
    """Percentage slope for Raw level of pb over 504d window."""
    res = _slope_pct(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_504d_v030_signal(pe):
    """Percentage slope for Raw level of pe over 504d window."""
    res = _slope_pct(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_504d_v031_signal(ev):
    """Percentage slope for Raw level of ev over 504d window."""
    res = _slope_pct(ev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_504d_v032_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 504d window."""
    res = _slope_pct(_z(pb, 1260), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_756d_v033_signal(pb):
    """Percentage slope for Raw level of pb over 756d window."""
    res = _slope_pct(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_756d_v034_signal(pe):
    """Percentage slope for Raw level of pe over 756d window."""
    res = _slope_pct(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_756d_v035_signal(ev):
    """Percentage slope for Raw level of ev over 756d window."""
    res = _slope_pct(ev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_756d_v036_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 756d window."""
    res = _slope_pct(_z(pb, 1260), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_1008d_v037_signal(pb):
    """Percentage slope for Raw level of pb over 1008d window."""
    res = _slope_pct(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_1008d_v038_signal(pe):
    """Percentage slope for Raw level of pe over 1008d window."""
    res = _slope_pct(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_1008d_v039_signal(ev):
    """Percentage slope for Raw level of ev over 1008d window."""
    res = _slope_pct(ev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_1008d_v040_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 1008d window."""
    res = _slope_pct(_z(pb, 1260), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_pct_1260d_v041_signal(pb):
    """Percentage slope for Raw level of pb over 1260d window."""
    res = _slope_pct(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_pct_1260d_v042_signal(pe):
    """Percentage slope for Raw level of pe over 1260d window."""
    res = _slope_pct(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_pct_1260d_v043_signal(ev):
    """Percentage slope for Raw level of ev over 1260d window."""
    res = _slope_pct(ev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_pct_1260d_v044_signal(pb):
    """Percentage slope for Long-term valuation cycle Z-score over 1260d window."""
    res = _slope_pct(_z(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_5d_v045_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 5d window."""
    res = _jerk(pb, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_5d_v046_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 5d window."""
    res = _jerk(pe, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_5d_v047_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 5d window."""
    res = _jerk(ev, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_5d_v048_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 5d window."""
    res = _jerk(_z(pb, 1260), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_10d_v049_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 10d window."""
    res = _jerk(pb, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_10d_v050_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 10d window."""
    res = _jerk(pe, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_10d_v051_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 10d window."""
    res = _jerk(ev, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_10d_v052_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 10d window."""
    res = _jerk(_z(pb, 1260), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_21d_v053_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 21d window."""
    res = _jerk(pb, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_21d_v054_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 21d window."""
    res = _jerk(pe, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_21d_v055_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 21d window."""
    res = _jerk(ev, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_21d_v056_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 21d window."""
    res = _jerk(_z(pb, 1260), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_42d_v057_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 42d window."""
    res = _jerk(pb, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_42d_v058_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 42d window."""
    res = _jerk(pe, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_42d_v059_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 42d window."""
    res = _jerk(ev, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_42d_v060_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 42d window."""
    res = _jerk(_z(pb, 1260), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_63d_v061_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 63d window."""
    res = _jerk(pb, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_63d_v062_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 63d window."""
    res = _jerk(pe, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_63d_v063_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 63d window."""
    res = _jerk(ev, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_63d_v064_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 63d window."""
    res = _jerk(_z(pb, 1260), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_126d_v065_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 126d window."""
    res = _jerk(pb, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_126d_v066_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 126d window."""
    res = _jerk(pe, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_126d_v067_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 126d window."""
    res = _jerk(ev, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_126d_v068_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 126d window."""
    res = _jerk(_z(pb, 1260), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_252d_v069_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 252d window."""
    res = _jerk(pb, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_252d_v070_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 252d window."""
    res = _jerk(pe, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_252d_v071_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 252d window."""
    res = _jerk(ev, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_252d_v072_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 252d window."""
    res = _jerk(_z(pb, 1260), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_504d_v073_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 504d window."""
    res = _jerk(pb, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_504d_v074_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 504d window."""
    res = _jerk(pe, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_504d_v075_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 504d window."""
    res = _jerk(ev, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_504d_v076_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 504d window."""
    res = _jerk(_z(pb, 1260), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_756d_v077_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 756d window."""
    res = _jerk(pb, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_756d_v078_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 756d window."""
    res = _jerk(pe, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_756d_v079_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 756d window."""
    res = _jerk(ev, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_756d_v080_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 756d window."""
    res = _jerk(_z(pb, 1260), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_1008d_v081_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1008d window."""
    res = _jerk(pb, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_1008d_v082_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 1008d window."""
    res = _jerk(pe, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_1008d_v083_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 1008d window."""
    res = _jerk(ev, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_1008d_v084_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 1008d window."""
    res = _jerk(_z(pb, 1260), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_jerk_1260d_v085_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1260d window."""
    res = _jerk(pb, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_jerk_1260d_v086_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 1260d window."""
    res = _jerk(pe, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_jerk_1260d_v087_signal(ev):
    """Acceleration/Jerk for Raw level of ev over 1260d window."""
    res = _jerk(ev, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_jerk_1260d_v088_signal(pb):
    """Acceleration/Jerk for Long-term valuation cycle Z-score over 1260d window."""
    res = _jerk(_z(pb, 1260), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_5d_v089_signal(pb):
    """Normalized slope change for Raw level of pb over 5d window."""
    res = (_slope_pct(pb, 5).diff(5) / _sma(pb.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_5d_v090_signal(pe):
    """Normalized slope change for Raw level of pe over 5d window."""
    res = (_slope_pct(pe, 5).diff(5) / _sma(pe.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_5d_v091_signal(ev):
    """Normalized slope change for Raw level of ev over 5d window."""
    res = (_slope_pct(ev, 5).diff(5) / _sma(ev.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_5d_v092_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 5d window."""
    res = (_slope_pct(_z(pb, 1260), 5).diff(5) / _sma(_z(pb, 1260).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_10d_v093_signal(pb):
    """Normalized slope change for Raw level of pb over 10d window."""
    res = (_slope_pct(pb, 10).diff(10) / _sma(pb.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_10d_v094_signal(pe):
    """Normalized slope change for Raw level of pe over 10d window."""
    res = (_slope_pct(pe, 10).diff(10) / _sma(pe.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_10d_v095_signal(ev):
    """Normalized slope change for Raw level of ev over 10d window."""
    res = (_slope_pct(ev, 10).diff(10) / _sma(ev.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_10d_v096_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 10d window."""
    res = (_slope_pct(_z(pb, 1260), 10).diff(10) / _sma(_z(pb, 1260).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_21d_v097_signal(pb):
    """Normalized slope change for Raw level of pb over 21d window."""
    res = (_slope_pct(pb, 21).diff(21) / _sma(pb.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_21d_v098_signal(pe):
    """Normalized slope change for Raw level of pe over 21d window."""
    res = (_slope_pct(pe, 21).diff(21) / _sma(pe.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_21d_v099_signal(ev):
    """Normalized slope change for Raw level of ev over 21d window."""
    res = (_slope_pct(ev, 21).diff(21) / _sma(ev.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_21d_v100_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 21d window."""
    res = (_slope_pct(_z(pb, 1260), 21).diff(21) / _sma(_z(pb, 1260).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_42d_v101_signal(pb):
    """Normalized slope change for Raw level of pb over 42d window."""
    res = (_slope_pct(pb, 42).diff(42) / _sma(pb.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_42d_v102_signal(pe):
    """Normalized slope change for Raw level of pe over 42d window."""
    res = (_slope_pct(pe, 42).diff(42) / _sma(pe.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_42d_v103_signal(ev):
    """Normalized slope change for Raw level of ev over 42d window."""
    res = (_slope_pct(ev, 42).diff(42) / _sma(ev.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_42d_v104_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 42d window."""
    res = (_slope_pct(_z(pb, 1260), 42).diff(42) / _sma(_z(pb, 1260).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_63d_v105_signal(pb):
    """Normalized slope change for Raw level of pb over 63d window."""
    res = (_slope_pct(pb, 63).diff(63) / _sma(pb.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_63d_v106_signal(pe):
    """Normalized slope change for Raw level of pe over 63d window."""
    res = (_slope_pct(pe, 63).diff(63) / _sma(pe.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_63d_v107_signal(ev):
    """Normalized slope change for Raw level of ev over 63d window."""
    res = (_slope_pct(ev, 63).diff(63) / _sma(ev.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_63d_v108_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 63d window."""
    res = (_slope_pct(_z(pb, 1260), 63).diff(63) / _sma(_z(pb, 1260).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_126d_v109_signal(pb):
    """Normalized slope change for Raw level of pb over 126d window."""
    res = (_slope_pct(pb, 126).diff(126) / _sma(pb.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_126d_v110_signal(pe):
    """Normalized slope change for Raw level of pe over 126d window."""
    res = (_slope_pct(pe, 126).diff(126) / _sma(pe.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_126d_v111_signal(ev):
    """Normalized slope change for Raw level of ev over 126d window."""
    res = (_slope_pct(ev, 126).diff(126) / _sma(ev.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_126d_v112_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 126d window."""
    res = (_slope_pct(_z(pb, 1260), 126).diff(126) / _sma(_z(pb, 1260).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_252d_v113_signal(pb):
    """Normalized slope change for Raw level of pb over 252d window."""
    res = (_slope_pct(pb, 252).diff(252) / _sma(pb.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_252d_v114_signal(pe):
    """Normalized slope change for Raw level of pe over 252d window."""
    res = (_slope_pct(pe, 252).diff(252) / _sma(pe.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_252d_v115_signal(ev):
    """Normalized slope change for Raw level of ev over 252d window."""
    res = (_slope_pct(ev, 252).diff(252) / _sma(ev.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_252d_v116_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 252d window."""
    res = (_slope_pct(_z(pb, 1260), 252).diff(252) / _sma(_z(pb, 1260).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_504d_v117_signal(pb):
    """Normalized slope change for Raw level of pb over 504d window."""
    res = (_slope_pct(pb, 504).diff(504) / _sma(pb.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_504d_v118_signal(pe):
    """Normalized slope change for Raw level of pe over 504d window."""
    res = (_slope_pct(pe, 504).diff(504) / _sma(pe.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_504d_v119_signal(ev):
    """Normalized slope change for Raw level of ev over 504d window."""
    res = (_slope_pct(ev, 504).diff(504) / _sma(ev.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_504d_v120_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 504d window."""
    res = (_slope_pct(_z(pb, 1260), 504).diff(504) / _sma(_z(pb, 1260).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_756d_v121_signal(pb):
    """Normalized slope change for Raw level of pb over 756d window."""
    res = (_slope_pct(pb, 756).diff(756) / _sma(pb.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_756d_v122_signal(pe):
    """Normalized slope change for Raw level of pe over 756d window."""
    res = (_slope_pct(pe, 756).diff(756) / _sma(pe.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_756d_v123_signal(ev):
    """Normalized slope change for Raw level of ev over 756d window."""
    res = (_slope_pct(ev, 756).diff(756) / _sma(ev.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_756d_v124_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 756d window."""
    res = (_slope_pct(_z(pb, 1260), 756).diff(756) / _sma(_z(pb, 1260).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_1008d_v125_signal(pb):
    """Normalized slope change for Raw level of pb over 1008d window."""
    res = (_slope_pct(pb, 1008).diff(1008) / _sma(pb.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_1008d_v126_signal(pe):
    """Normalized slope change for Raw level of pe over 1008d window."""
    res = (_slope_pct(pe, 1008).diff(1008) / _sma(pe.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_1008d_v127_signal(ev):
    """Normalized slope change for Raw level of ev over 1008d window."""
    res = (_slope_pct(ev, 1008).diff(1008) / _sma(ev.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_1008d_v128_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 1008d window."""
    res = (_slope_pct(_z(pb, 1260), 1008).diff(1008) / _sma(_z(pb, 1260).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_slope_diff_norm_1260d_v129_signal(pb):
    """Normalized slope change for Raw level of pb over 1260d window."""
    res = (_slope_pct(pb, 1260).diff(1260) / _sma(pb.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_slope_diff_norm_1260d_v130_signal(pe):
    """Normalized slope change for Raw level of pe over 1260d window."""
    res = (_slope_pct(pe, 1260).diff(1260) / _sma(pe.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_slope_diff_norm_1260d_v131_signal(ev):
    """Normalized slope change for Raw level of ev over 1260d window."""
    res = (_slope_pct(ev, 1260).diff(1260) / _sma(ev.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_1260d_v132_signal(pb):
    """Normalized slope change for Long-term valuation cycle Z-score over 1260d window."""
    res = (_slope_pct(_z(pb, 1260), 1260).diff(1260) / _sma(_z(pb, 1260).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_mom_z_5d_v133_signal(pb):
    """Relative momentum strength for Raw level of pb over 5d window."""
    res = _z(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_mom_z_5d_v134_signal(pe):
    """Relative momentum strength for Raw level of pe over 5d window."""
    res = _z(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_mom_z_5d_v135_signal(ev):
    """Relative momentum strength for Raw level of ev over 5d window."""
    res = _z(_slope_pct(ev, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_mom_z_5d_v136_signal(pb):
    """Relative momentum strength for Long-term valuation cycle Z-score over 5d window."""
    res = _z(_slope_pct(_z(pb, 1260), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_mom_z_10d_v137_signal(pb):
    """Relative momentum strength for Raw level of pb over 10d window."""
    res = _z(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_mom_z_10d_v138_signal(pe):
    """Relative momentum strength for Raw level of pe over 10d window."""
    res = _z(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_mom_z_10d_v139_signal(ev):
    """Relative momentum strength for Raw level of ev over 10d window."""
    res = _z(_slope_pct(ev, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_mom_z_10d_v140_signal(pb):
    """Relative momentum strength for Long-term valuation cycle Z-score over 10d window."""
    res = _z(_slope_pct(_z(pb, 1260), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_mom_z_21d_v141_signal(pb):
    """Relative momentum strength for Raw level of pb over 21d window."""
    res = _z(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_mom_z_21d_v142_signal(pe):
    """Relative momentum strength for Raw level of pe over 21d window."""
    res = _z(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_mom_z_21d_v143_signal(ev):
    """Relative momentum strength for Raw level of ev over 21d window."""
    res = _z(_slope_pct(ev, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_mom_z_21d_v144_signal(pb):
    """Relative momentum strength for Long-term valuation cycle Z-score over 21d window."""
    res = _z(_slope_pct(_z(pb, 1260), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_mom_z_42d_v145_signal(pb):
    """Relative momentum strength for Raw level of pb over 42d window."""
    res = _z(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_mom_z_42d_v146_signal(pe):
    """Relative momentum strength for Raw level of pe over 42d window."""
    res = _z(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_mom_z_42d_v147_signal(ev):
    """Relative momentum strength for Raw level of ev over 42d window."""
    res = _z(_slope_pct(ev, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_mom_z_42d_v148_signal(pb):
    """Relative momentum strength for Long-term valuation cycle Z-score over 42d window."""
    res = _z(_slope_pct(_z(pb, 1260), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_mom_z_63d_v149_signal(pb):
    """Relative momentum strength for Raw level of pb over 63d window."""
    res = _z(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_mom_z_63d_v150_signal(pe):
    """Relative momentum strength for Raw level of pe over 63d window."""
    res = _z(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f46_valuation_reversion_fin_pb_slope_pct_5d_v001_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_5d_v001_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_5d_v002_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_5d_v002_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_5d_v003_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_5d_v003_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_5d_v004_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_5d_v004_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_10d_v005_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_10d_v005_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_10d_v006_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_10d_v006_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_10d_v007_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_10d_v007_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_10d_v008_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_10d_v008_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_21d_v009_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_21d_v009_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_21d_v010_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_21d_v010_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_21d_v011_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_21d_v011_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_21d_v012_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_21d_v012_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_42d_v013_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_42d_v013_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_42d_v014_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_42d_v014_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_42d_v015_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_42d_v015_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_42d_v016_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_42d_v016_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_63d_v017_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_63d_v017_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_63d_v018_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_63d_v018_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_63d_v019_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_63d_v019_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_63d_v020_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_63d_v020_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_126d_v021_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_126d_v021_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_126d_v022_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_126d_v022_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_126d_v023_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_126d_v023_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_126d_v024_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_126d_v024_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_252d_v025_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_252d_v025_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_252d_v026_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_252d_v026_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_252d_v027_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_252d_v027_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_252d_v028_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_252d_v028_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_504d_v029_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_504d_v029_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_504d_v030_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_504d_v030_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_504d_v031_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_504d_v031_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_504d_v032_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_504d_v032_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_756d_v033_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_756d_v033_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_756d_v034_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_756d_v034_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_756d_v035_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_756d_v035_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_756d_v036_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_756d_v036_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_1008d_v037_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_1008d_v037_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_1008d_v038_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_1008d_v038_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_1008d_v039_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_1008d_v039_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_1008d_v040_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_1008d_v040_signal},
    "f46_valuation_reversion_fin_pb_slope_pct_1260d_v041_signal": {"func": f46_valuation_reversion_fin_pb_slope_pct_1260d_v041_signal},
    "f46_valuation_reversion_fin_pe_slope_pct_1260d_v042_signal": {"func": f46_valuation_reversion_fin_pe_slope_pct_1260d_v042_signal},
    "f46_valuation_reversion_fin_ev_slope_pct_1260d_v043_signal": {"func": f46_valuation_reversion_fin_ev_slope_pct_1260d_v043_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_pct_1260d_v044_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_pct_1260d_v044_signal},
    "f46_valuation_reversion_fin_pb_jerk_5d_v045_signal": {"func": f46_valuation_reversion_fin_pb_jerk_5d_v045_signal},
    "f46_valuation_reversion_fin_pe_jerk_5d_v046_signal": {"func": f46_valuation_reversion_fin_pe_jerk_5d_v046_signal},
    "f46_valuation_reversion_fin_ev_jerk_5d_v047_signal": {"func": f46_valuation_reversion_fin_ev_jerk_5d_v047_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_5d_v048_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_5d_v048_signal},
    "f46_valuation_reversion_fin_pb_jerk_10d_v049_signal": {"func": f46_valuation_reversion_fin_pb_jerk_10d_v049_signal},
    "f46_valuation_reversion_fin_pe_jerk_10d_v050_signal": {"func": f46_valuation_reversion_fin_pe_jerk_10d_v050_signal},
    "f46_valuation_reversion_fin_ev_jerk_10d_v051_signal": {"func": f46_valuation_reversion_fin_ev_jerk_10d_v051_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_10d_v052_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_10d_v052_signal},
    "f46_valuation_reversion_fin_pb_jerk_21d_v053_signal": {"func": f46_valuation_reversion_fin_pb_jerk_21d_v053_signal},
    "f46_valuation_reversion_fin_pe_jerk_21d_v054_signal": {"func": f46_valuation_reversion_fin_pe_jerk_21d_v054_signal},
    "f46_valuation_reversion_fin_ev_jerk_21d_v055_signal": {"func": f46_valuation_reversion_fin_ev_jerk_21d_v055_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_21d_v056_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_21d_v056_signal},
    "f46_valuation_reversion_fin_pb_jerk_42d_v057_signal": {"func": f46_valuation_reversion_fin_pb_jerk_42d_v057_signal},
    "f46_valuation_reversion_fin_pe_jerk_42d_v058_signal": {"func": f46_valuation_reversion_fin_pe_jerk_42d_v058_signal},
    "f46_valuation_reversion_fin_ev_jerk_42d_v059_signal": {"func": f46_valuation_reversion_fin_ev_jerk_42d_v059_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_42d_v060_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_42d_v060_signal},
    "f46_valuation_reversion_fin_pb_jerk_63d_v061_signal": {"func": f46_valuation_reversion_fin_pb_jerk_63d_v061_signal},
    "f46_valuation_reversion_fin_pe_jerk_63d_v062_signal": {"func": f46_valuation_reversion_fin_pe_jerk_63d_v062_signal},
    "f46_valuation_reversion_fin_ev_jerk_63d_v063_signal": {"func": f46_valuation_reversion_fin_ev_jerk_63d_v063_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_63d_v064_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_63d_v064_signal},
    "f46_valuation_reversion_fin_pb_jerk_126d_v065_signal": {"func": f46_valuation_reversion_fin_pb_jerk_126d_v065_signal},
    "f46_valuation_reversion_fin_pe_jerk_126d_v066_signal": {"func": f46_valuation_reversion_fin_pe_jerk_126d_v066_signal},
    "f46_valuation_reversion_fin_ev_jerk_126d_v067_signal": {"func": f46_valuation_reversion_fin_ev_jerk_126d_v067_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_126d_v068_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_126d_v068_signal},
    "f46_valuation_reversion_fin_pb_jerk_252d_v069_signal": {"func": f46_valuation_reversion_fin_pb_jerk_252d_v069_signal},
    "f46_valuation_reversion_fin_pe_jerk_252d_v070_signal": {"func": f46_valuation_reversion_fin_pe_jerk_252d_v070_signal},
    "f46_valuation_reversion_fin_ev_jerk_252d_v071_signal": {"func": f46_valuation_reversion_fin_ev_jerk_252d_v071_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_252d_v072_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_252d_v072_signal},
    "f46_valuation_reversion_fin_pb_jerk_504d_v073_signal": {"func": f46_valuation_reversion_fin_pb_jerk_504d_v073_signal},
    "f46_valuation_reversion_fin_pe_jerk_504d_v074_signal": {"func": f46_valuation_reversion_fin_pe_jerk_504d_v074_signal},
    "f46_valuation_reversion_fin_ev_jerk_504d_v075_signal": {"func": f46_valuation_reversion_fin_ev_jerk_504d_v075_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_504d_v076_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_504d_v076_signal},
    "f46_valuation_reversion_fin_pb_jerk_756d_v077_signal": {"func": f46_valuation_reversion_fin_pb_jerk_756d_v077_signal},
    "f46_valuation_reversion_fin_pe_jerk_756d_v078_signal": {"func": f46_valuation_reversion_fin_pe_jerk_756d_v078_signal},
    "f46_valuation_reversion_fin_ev_jerk_756d_v079_signal": {"func": f46_valuation_reversion_fin_ev_jerk_756d_v079_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_756d_v080_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_756d_v080_signal},
    "f46_valuation_reversion_fin_pb_jerk_1008d_v081_signal": {"func": f46_valuation_reversion_fin_pb_jerk_1008d_v081_signal},
    "f46_valuation_reversion_fin_pe_jerk_1008d_v082_signal": {"func": f46_valuation_reversion_fin_pe_jerk_1008d_v082_signal},
    "f46_valuation_reversion_fin_ev_jerk_1008d_v083_signal": {"func": f46_valuation_reversion_fin_ev_jerk_1008d_v083_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_1008d_v084_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_1008d_v084_signal},
    "f46_valuation_reversion_fin_pb_jerk_1260d_v085_signal": {"func": f46_valuation_reversion_fin_pb_jerk_1260d_v085_signal},
    "f46_valuation_reversion_fin_pe_jerk_1260d_v086_signal": {"func": f46_valuation_reversion_fin_pe_jerk_1260d_v086_signal},
    "f46_valuation_reversion_fin_ev_jerk_1260d_v087_signal": {"func": f46_valuation_reversion_fin_ev_jerk_1260d_v087_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_jerk_1260d_v088_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_jerk_1260d_v088_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_5d_v089_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_5d_v089_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_5d_v090_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_5d_v090_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_5d_v091_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_5d_v091_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_5d_v092_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_5d_v092_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_10d_v093_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_10d_v093_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_10d_v094_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_10d_v094_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_10d_v095_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_10d_v095_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_10d_v096_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_10d_v096_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_21d_v097_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_21d_v097_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_21d_v098_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_21d_v098_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_21d_v099_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_21d_v099_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_21d_v100_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_21d_v100_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_42d_v101_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_42d_v101_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_42d_v102_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_42d_v102_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_42d_v103_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_42d_v103_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_42d_v104_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_42d_v104_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_63d_v105_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_63d_v105_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_63d_v106_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_63d_v106_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_63d_v107_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_63d_v107_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_63d_v108_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_63d_v108_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_126d_v109_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_126d_v109_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_126d_v110_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_126d_v110_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_126d_v111_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_126d_v111_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_126d_v112_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_126d_v112_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_252d_v113_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_252d_v113_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_252d_v114_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_252d_v114_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_252d_v115_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_252d_v115_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_252d_v116_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_252d_v116_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_504d_v117_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_504d_v117_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_504d_v118_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_504d_v118_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_504d_v119_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_504d_v119_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_504d_v120_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_504d_v120_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_756d_v121_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_756d_v121_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_756d_v122_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_756d_v122_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_756d_v123_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_756d_v123_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_756d_v124_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_756d_v124_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_1008d_v125_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_1008d_v125_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_1008d_v126_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_1008d_v126_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_1008d_v127_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_1008d_v127_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_1008d_v128_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_1008d_v128_signal},
    "f46_valuation_reversion_fin_pb_slope_diff_norm_1260d_v129_signal": {"func": f46_valuation_reversion_fin_pb_slope_diff_norm_1260d_v129_signal},
    "f46_valuation_reversion_fin_pe_slope_diff_norm_1260d_v130_signal": {"func": f46_valuation_reversion_fin_pe_slope_diff_norm_1260d_v130_signal},
    "f46_valuation_reversion_fin_ev_slope_diff_norm_1260d_v131_signal": {"func": f46_valuation_reversion_fin_ev_slope_diff_norm_1260d_v131_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_1260d_v132_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_slope_diff_norm_1260d_v132_signal},
    "f46_valuation_reversion_fin_pb_mom_z_5d_v133_signal": {"func": f46_valuation_reversion_fin_pb_mom_z_5d_v133_signal},
    "f46_valuation_reversion_fin_pe_mom_z_5d_v134_signal": {"func": f46_valuation_reversion_fin_pe_mom_z_5d_v134_signal},
    "f46_valuation_reversion_fin_ev_mom_z_5d_v135_signal": {"func": f46_valuation_reversion_fin_ev_mom_z_5d_v135_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_mom_z_5d_v136_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_mom_z_5d_v136_signal},
    "f46_valuation_reversion_fin_pb_mom_z_10d_v137_signal": {"func": f46_valuation_reversion_fin_pb_mom_z_10d_v137_signal},
    "f46_valuation_reversion_fin_pe_mom_z_10d_v138_signal": {"func": f46_valuation_reversion_fin_pe_mom_z_10d_v138_signal},
    "f46_valuation_reversion_fin_ev_mom_z_10d_v139_signal": {"func": f46_valuation_reversion_fin_ev_mom_z_10d_v139_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_mom_z_10d_v140_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_mom_z_10d_v140_signal},
    "f46_valuation_reversion_fin_pb_mom_z_21d_v141_signal": {"func": f46_valuation_reversion_fin_pb_mom_z_21d_v141_signal},
    "f46_valuation_reversion_fin_pe_mom_z_21d_v142_signal": {"func": f46_valuation_reversion_fin_pe_mom_z_21d_v142_signal},
    "f46_valuation_reversion_fin_ev_mom_z_21d_v143_signal": {"func": f46_valuation_reversion_fin_ev_mom_z_21d_v143_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_mom_z_21d_v144_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_mom_z_21d_v144_signal},
    "f46_valuation_reversion_fin_pb_mom_z_42d_v145_signal": {"func": f46_valuation_reversion_fin_pb_mom_z_42d_v145_signal},
    "f46_valuation_reversion_fin_pe_mom_z_42d_v146_signal": {"func": f46_valuation_reversion_fin_pe_mom_z_42d_v146_signal},
    "f46_valuation_reversion_fin_ev_mom_z_42d_v147_signal": {"func": f46_valuation_reversion_fin_ev_mom_z_42d_v147_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_mom_z_42d_v148_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_mom_z_42d_v148_signal},
    "f46_valuation_reversion_fin_pb_mom_z_63d_v149_signal": {"func": f46_valuation_reversion_fin_pb_mom_z_63d_v149_signal},
    "f46_valuation_reversion_fin_pe_mom_z_63d_v150_signal": {"func": f46_valuation_reversion_fin_pe_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 46...")
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
