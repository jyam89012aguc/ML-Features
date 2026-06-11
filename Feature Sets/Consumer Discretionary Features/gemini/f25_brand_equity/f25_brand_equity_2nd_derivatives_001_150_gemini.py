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

def f25_brand_equity_grossmargin_slope_pct_5d_v001_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 5d window."""
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_5d_v002_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 5d window."""
    res = _slope_pct(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_5d_v003_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 5d window."""
    res = _slope_pct(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_5d_v004_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 5d window."""
    res = _slope_pct(grossmargin * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_10d_v005_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 10d window."""
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_10d_v006_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 10d window."""
    res = _slope_pct(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_10d_v007_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 10d window."""
    res = _slope_pct(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_10d_v008_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 10d window."""
    res = _slope_pct(grossmargin * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_21d_v009_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 21d window."""
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_21d_v010_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 21d window."""
    res = _slope_pct(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_21d_v011_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 21d window."""
    res = _slope_pct(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_21d_v012_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 21d window."""
    res = _slope_pct(grossmargin * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_42d_v013_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 42d window."""
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_42d_v014_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 42d window."""
    res = _slope_pct(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_42d_v015_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 42d window."""
    res = _slope_pct(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_42d_v016_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 42d window."""
    res = _slope_pct(grossmargin * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_63d_v017_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 63d window."""
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_63d_v018_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 63d window."""
    res = _slope_pct(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_63d_v019_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 63d window."""
    res = _slope_pct(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_63d_v020_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 63d window."""
    res = _slope_pct(grossmargin * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_126d_v021_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 126d window."""
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_126d_v022_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 126d window."""
    res = _slope_pct(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_126d_v023_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 126d window."""
    res = _slope_pct(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_126d_v024_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 126d window."""
    res = _slope_pct(grossmargin * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_252d_v025_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 252d window."""
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_252d_v026_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 252d window."""
    res = _slope_pct(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_252d_v027_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 252d window."""
    res = _slope_pct(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_252d_v028_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 252d window."""
    res = _slope_pct(grossmargin * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_504d_v029_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 504d window."""
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_504d_v030_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 504d window."""
    res = _slope_pct(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_504d_v031_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 504d window."""
    res = _slope_pct(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_504d_v032_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 504d window."""
    res = _slope_pct(grossmargin * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_756d_v033_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 756d window."""
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_756d_v034_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 756d window."""
    res = _slope_pct(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_756d_v035_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 756d window."""
    res = _slope_pct(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_756d_v036_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 756d window."""
    res = _slope_pct(grossmargin * pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_1008d_v037_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 1008d window."""
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_1008d_v038_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 1008d window."""
    res = _slope_pct(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_1008d_v039_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 1008d window."""
    res = _slope_pct(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_1008d_v040_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 1008d window."""
    res = _slope_pct(grossmargin * pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_pct_1260d_v041_signal(grossmargin):
    """Percentage slope for momentum for Raw level of grossmargin over 1260d window."""
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_pct_1260d_v042_signal(pe):
    """Percentage slope for momentum for Raw level of pe over 1260d window."""
    res = _slope_pct(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_pct_1260d_v043_signal(pb):
    """Percentage slope for momentum for Raw level of pb over 1260d window."""
    res = _slope_pct(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_pct_1260d_v044_signal(grossmargin, pe):
    """Percentage slope for momentum for Brand margin amplified by market valuation multiples over 1260d window."""
    res = _slope_pct(grossmargin * pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_5d_v045_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 5d window."""
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_5d_v046_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 5d window."""
    res = _jerk(pe, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_5d_v047_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 5d window."""
    res = _jerk(pb, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_5d_v048_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 5d window."""
    res = _jerk(grossmargin * pe, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_10d_v049_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 10d window."""
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_10d_v050_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 10d window."""
    res = _jerk(pe, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_10d_v051_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 10d window."""
    res = _jerk(pb, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_10d_v052_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 10d window."""
    res = _jerk(grossmargin * pe, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_21d_v053_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 21d window."""
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_21d_v054_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 21d window."""
    res = _jerk(pe, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_21d_v055_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 21d window."""
    res = _jerk(pb, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_21d_v056_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 21d window."""
    res = _jerk(grossmargin * pe, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_42d_v057_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 42d window."""
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_42d_v058_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 42d window."""
    res = _jerk(pe, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_42d_v059_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 42d window."""
    res = _jerk(pb, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_42d_v060_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 42d window."""
    res = _jerk(grossmargin * pe, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_63d_v061_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 63d window."""
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_63d_v062_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 63d window."""
    res = _jerk(pe, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_63d_v063_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 63d window."""
    res = _jerk(pb, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_63d_v064_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 63d window."""
    res = _jerk(grossmargin * pe, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_126d_v065_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 126d window."""
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_126d_v066_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 126d window."""
    res = _jerk(pe, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_126d_v067_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 126d window."""
    res = _jerk(pb, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_126d_v068_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 126d window."""
    res = _jerk(grossmargin * pe, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_252d_v069_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 252d window."""
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_252d_v070_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 252d window."""
    res = _jerk(pe, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_252d_v071_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 252d window."""
    res = _jerk(pb, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_252d_v072_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 252d window."""
    res = _jerk(grossmargin * pe, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_504d_v073_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 504d window."""
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_504d_v074_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 504d window."""
    res = _jerk(pe, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_504d_v075_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 504d window."""
    res = _jerk(pb, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_504d_v076_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 504d window."""
    res = _jerk(grossmargin * pe, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_756d_v077_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 756d window."""
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_756d_v078_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 756d window."""
    res = _jerk(pe, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_756d_v079_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 756d window."""
    res = _jerk(pb, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_756d_v080_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 756d window."""
    res = _jerk(grossmargin * pe, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_1008d_v081_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 1008d window."""
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_1008d_v082_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 1008d window."""
    res = _jerk(pe, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_1008d_v083_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 1008d window."""
    res = _jerk(pb, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_1008d_v084_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 1008d window."""
    res = _jerk(grossmargin * pe, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_jerk_1260d_v085_signal(grossmargin):
    """Acceleration/Jerk for structural shifts for Raw level of grossmargin over 1260d window."""
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_jerk_1260d_v086_signal(pe):
    """Acceleration/Jerk for structural shifts for Raw level of pe over 1260d window."""
    res = _jerk(pe, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_jerk_1260d_v087_signal(pb):
    """Acceleration/Jerk for structural shifts for Raw level of pb over 1260d window."""
    res = _jerk(pb, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_jerk_1260d_v088_signal(grossmargin, pe):
    """Acceleration/Jerk for structural shifts for Brand margin amplified by market valuation multiples over 1260d window."""
    res = _jerk(grossmargin * pe, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_5d_v089_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 5d window."""
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_5d_v090_signal(pe):
    """Normalized slope change for Raw level of pe over 5d window."""
    res = (_slope_pct(pe, 5).diff(5) / _sma(pe.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_5d_v091_signal(pb):
    """Normalized slope change for Raw level of pb over 5d window."""
    res = (_slope_pct(pb, 5).diff(5) / _sma(pb.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_5d_v092_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 5d window."""
    res = (_slope_pct(grossmargin * pe, 5).diff(5) / _sma(grossmargin * pe.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_10d_v093_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 10d window."""
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_10d_v094_signal(pe):
    """Normalized slope change for Raw level of pe over 10d window."""
    res = (_slope_pct(pe, 10).diff(10) / _sma(pe.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_10d_v095_signal(pb):
    """Normalized slope change for Raw level of pb over 10d window."""
    res = (_slope_pct(pb, 10).diff(10) / _sma(pb.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_10d_v096_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 10d window."""
    res = (_slope_pct(grossmargin * pe, 10).diff(10) / _sma(grossmargin * pe.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_21d_v097_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 21d window."""
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_21d_v098_signal(pe):
    """Normalized slope change for Raw level of pe over 21d window."""
    res = (_slope_pct(pe, 21).diff(21) / _sma(pe.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_21d_v099_signal(pb):
    """Normalized slope change for Raw level of pb over 21d window."""
    res = (_slope_pct(pb, 21).diff(21) / _sma(pb.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_21d_v100_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 21d window."""
    res = (_slope_pct(grossmargin * pe, 21).diff(21) / _sma(grossmargin * pe.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_42d_v101_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 42d window."""
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_42d_v102_signal(pe):
    """Normalized slope change for Raw level of pe over 42d window."""
    res = (_slope_pct(pe, 42).diff(42) / _sma(pe.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_42d_v103_signal(pb):
    """Normalized slope change for Raw level of pb over 42d window."""
    res = (_slope_pct(pb, 42).diff(42) / _sma(pb.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_42d_v104_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 42d window."""
    res = (_slope_pct(grossmargin * pe, 42).diff(42) / _sma(grossmargin * pe.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_63d_v105_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 63d window."""
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_63d_v106_signal(pe):
    """Normalized slope change for Raw level of pe over 63d window."""
    res = (_slope_pct(pe, 63).diff(63) / _sma(pe.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_63d_v107_signal(pb):
    """Normalized slope change for Raw level of pb over 63d window."""
    res = (_slope_pct(pb, 63).diff(63) / _sma(pb.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_63d_v108_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 63d window."""
    res = (_slope_pct(grossmargin * pe, 63).diff(63) / _sma(grossmargin * pe.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_126d_v109_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 126d window."""
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_126d_v110_signal(pe):
    """Normalized slope change for Raw level of pe over 126d window."""
    res = (_slope_pct(pe, 126).diff(126) / _sma(pe.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_126d_v111_signal(pb):
    """Normalized slope change for Raw level of pb over 126d window."""
    res = (_slope_pct(pb, 126).diff(126) / _sma(pb.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_126d_v112_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 126d window."""
    res = (_slope_pct(grossmargin * pe, 126).diff(126) / _sma(grossmargin * pe.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_252d_v113_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 252d window."""
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_252d_v114_signal(pe):
    """Normalized slope change for Raw level of pe over 252d window."""
    res = (_slope_pct(pe, 252).diff(252) / _sma(pe.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_252d_v115_signal(pb):
    """Normalized slope change for Raw level of pb over 252d window."""
    res = (_slope_pct(pb, 252).diff(252) / _sma(pb.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_252d_v116_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 252d window."""
    res = (_slope_pct(grossmargin * pe, 252).diff(252) / _sma(grossmargin * pe.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_504d_v117_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 504d window."""
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_504d_v118_signal(pe):
    """Normalized slope change for Raw level of pe over 504d window."""
    res = (_slope_pct(pe, 504).diff(504) / _sma(pe.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_504d_v119_signal(pb):
    """Normalized slope change for Raw level of pb over 504d window."""
    res = (_slope_pct(pb, 504).diff(504) / _sma(pb.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_504d_v120_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 504d window."""
    res = (_slope_pct(grossmargin * pe, 504).diff(504) / _sma(grossmargin * pe.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_756d_v121_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 756d window."""
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_756d_v122_signal(pe):
    """Normalized slope change for Raw level of pe over 756d window."""
    res = (_slope_pct(pe, 756).diff(756) / _sma(pe.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_756d_v123_signal(pb):
    """Normalized slope change for Raw level of pb over 756d window."""
    res = (_slope_pct(pb, 756).diff(756) / _sma(pb.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_756d_v124_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 756d window."""
    res = (_slope_pct(grossmargin * pe, 756).diff(756) / _sma(grossmargin * pe.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_1008d_v125_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1008d window."""
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_1008d_v126_signal(pe):
    """Normalized slope change for Raw level of pe over 1008d window."""
    res = (_slope_pct(pe, 1008).diff(1008) / _sma(pe.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_1008d_v127_signal(pb):
    """Normalized slope change for Raw level of pb over 1008d window."""
    res = (_slope_pct(pb, 1008).diff(1008) / _sma(pb.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_1008d_v128_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 1008d window."""
    res = (_slope_pct(grossmargin * pe, 1008).diff(1008) / _sma(grossmargin * pe.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_slope_diff_norm_1260d_v129_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1260d window."""
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_slope_diff_norm_1260d_v130_signal(pe):
    """Normalized slope change for Raw level of pe over 1260d window."""
    res = (_slope_pct(pe, 1260).diff(1260) / _sma(pe.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_slope_diff_norm_1260d_v131_signal(pb):
    """Normalized slope change for Raw level of pb over 1260d window."""
    res = (_slope_pct(pb, 1260).diff(1260) / _sma(pb.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_slope_diff_norm_1260d_v132_signal(grossmargin, pe):
    """Normalized slope change for Brand margin amplified by market valuation multiples over 1260d window."""
    res = (_slope_pct(grossmargin * pe, 1260).diff(1260) / _sma(grossmargin * pe.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_mom_z_5d_v133_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 5d window."""
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_mom_z_5d_v134_signal(pe):
    """Relative momentum strength for Raw level of pe over 5d window."""
    res = _z(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_mom_z_5d_v135_signal(pb):
    """Relative momentum strength for Raw level of pb over 5d window."""
    res = _z(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_mom_z_5d_v136_signal(grossmargin, pe):
    """Relative momentum strength for Brand margin amplified by market valuation multiples over 5d window."""
    res = _z(_slope_pct(grossmargin * pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_mom_z_10d_v137_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 10d window."""
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_mom_z_10d_v138_signal(pe):
    """Relative momentum strength for Raw level of pe over 10d window."""
    res = _z(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_mom_z_10d_v139_signal(pb):
    """Relative momentum strength for Raw level of pb over 10d window."""
    res = _z(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_mom_z_10d_v140_signal(grossmargin, pe):
    """Relative momentum strength for Brand margin amplified by market valuation multiples over 10d window."""
    res = _z(_slope_pct(grossmargin * pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_mom_z_21d_v141_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 21d window."""
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_mom_z_21d_v142_signal(pe):
    """Relative momentum strength for Raw level of pe over 21d window."""
    res = _z(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_mom_z_21d_v143_signal(pb):
    """Relative momentum strength for Raw level of pb over 21d window."""
    res = _z(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_mom_z_21d_v144_signal(grossmargin, pe):
    """Relative momentum strength for Brand margin amplified by market valuation multiples over 21d window."""
    res = _z(_slope_pct(grossmargin * pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_mom_z_42d_v145_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 42d window."""
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_mom_z_42d_v146_signal(pe):
    """Relative momentum strength for Raw level of pe over 42d window."""
    res = _z(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_mom_z_42d_v147_signal(pb):
    """Relative momentum strength for Raw level of pb over 42d window."""
    res = _z(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_mom_z_42d_v148_signal(grossmargin, pe):
    """Relative momentum strength for Brand margin amplified by market valuation multiples over 42d window."""
    res = _z(_slope_pct(grossmargin * pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_mom_z_63d_v149_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 63d window."""
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_mom_z_63d_v150_signal(pe):
    """Relative momentum strength for Raw level of pe over 63d window."""
    res = _z(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f25_brand_equity_grossmargin_slope_pct_5d_v001_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_5d_v001_signal},    "f25_brand_equity_pe_slope_pct_5d_v002_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_5d_v002_signal},    "f25_brand_equity_pb_slope_pct_5d_v003_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_5d_v003_signal},    "f25_brand_equity_equity_moat_slope_pct_5d_v004_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_5d_v004_signal},    "f25_brand_equity_grossmargin_slope_pct_10d_v005_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_10d_v005_signal},    "f25_brand_equity_pe_slope_pct_10d_v006_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_10d_v006_signal},    "f25_brand_equity_pb_slope_pct_10d_v007_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_10d_v007_signal},    "f25_brand_equity_equity_moat_slope_pct_10d_v008_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_10d_v008_signal},    "f25_brand_equity_grossmargin_slope_pct_21d_v009_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_21d_v009_signal},    "f25_brand_equity_pe_slope_pct_21d_v010_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_21d_v010_signal},    "f25_brand_equity_pb_slope_pct_21d_v011_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_21d_v011_signal},    "f25_brand_equity_equity_moat_slope_pct_21d_v012_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_21d_v012_signal},    "f25_brand_equity_grossmargin_slope_pct_42d_v013_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_42d_v013_signal},    "f25_brand_equity_pe_slope_pct_42d_v014_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_42d_v014_signal},    "f25_brand_equity_pb_slope_pct_42d_v015_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_42d_v015_signal},    "f25_brand_equity_equity_moat_slope_pct_42d_v016_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_42d_v016_signal},    "f25_brand_equity_grossmargin_slope_pct_63d_v017_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_63d_v017_signal},    "f25_brand_equity_pe_slope_pct_63d_v018_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_63d_v018_signal},    "f25_brand_equity_pb_slope_pct_63d_v019_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_63d_v019_signal},    "f25_brand_equity_equity_moat_slope_pct_63d_v020_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_63d_v020_signal},    "f25_brand_equity_grossmargin_slope_pct_126d_v021_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_126d_v021_signal},    "f25_brand_equity_pe_slope_pct_126d_v022_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_126d_v022_signal},    "f25_brand_equity_pb_slope_pct_126d_v023_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_126d_v023_signal},    "f25_brand_equity_equity_moat_slope_pct_126d_v024_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_126d_v024_signal},    "f25_brand_equity_grossmargin_slope_pct_252d_v025_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_252d_v025_signal},    "f25_brand_equity_pe_slope_pct_252d_v026_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_252d_v026_signal},    "f25_brand_equity_pb_slope_pct_252d_v027_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_252d_v027_signal},    "f25_brand_equity_equity_moat_slope_pct_252d_v028_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_252d_v028_signal},    "f25_brand_equity_grossmargin_slope_pct_504d_v029_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_504d_v029_signal},    "f25_brand_equity_pe_slope_pct_504d_v030_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_504d_v030_signal},    "f25_brand_equity_pb_slope_pct_504d_v031_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_504d_v031_signal},    "f25_brand_equity_equity_moat_slope_pct_504d_v032_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_504d_v032_signal},    "f25_brand_equity_grossmargin_slope_pct_756d_v033_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_756d_v033_signal},    "f25_brand_equity_pe_slope_pct_756d_v034_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_756d_v034_signal},    "f25_brand_equity_pb_slope_pct_756d_v035_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_756d_v035_signal},    "f25_brand_equity_equity_moat_slope_pct_756d_v036_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_756d_v036_signal},    "f25_brand_equity_grossmargin_slope_pct_1008d_v037_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_1008d_v037_signal},    "f25_brand_equity_pe_slope_pct_1008d_v038_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_1008d_v038_signal},    "f25_brand_equity_pb_slope_pct_1008d_v039_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_1008d_v039_signal},    "f25_brand_equity_equity_moat_slope_pct_1008d_v040_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_1008d_v040_signal},    "f25_brand_equity_grossmargin_slope_pct_1260d_v041_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_pct_1260d_v041_signal},    "f25_brand_equity_pe_slope_pct_1260d_v042_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_pct_1260d_v042_signal},    "f25_brand_equity_pb_slope_pct_1260d_v043_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_pct_1260d_v043_signal},    "f25_brand_equity_equity_moat_slope_pct_1260d_v044_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_pct_1260d_v044_signal},    "f25_brand_equity_grossmargin_jerk_5d_v045_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_5d_v045_signal},    "f25_brand_equity_pe_jerk_5d_v046_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_5d_v046_signal},    "f25_brand_equity_pb_jerk_5d_v047_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_5d_v047_signal},    "f25_brand_equity_equity_moat_jerk_5d_v048_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_5d_v048_signal},    "f25_brand_equity_grossmargin_jerk_10d_v049_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_10d_v049_signal},    "f25_brand_equity_pe_jerk_10d_v050_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_10d_v050_signal},    "f25_brand_equity_pb_jerk_10d_v051_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_10d_v051_signal},    "f25_brand_equity_equity_moat_jerk_10d_v052_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_10d_v052_signal},    "f25_brand_equity_grossmargin_jerk_21d_v053_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_21d_v053_signal},    "f25_brand_equity_pe_jerk_21d_v054_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_21d_v054_signal},    "f25_brand_equity_pb_jerk_21d_v055_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_21d_v055_signal},    "f25_brand_equity_equity_moat_jerk_21d_v056_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_21d_v056_signal},    "f25_brand_equity_grossmargin_jerk_42d_v057_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_42d_v057_signal},    "f25_brand_equity_pe_jerk_42d_v058_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_42d_v058_signal},    "f25_brand_equity_pb_jerk_42d_v059_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_42d_v059_signal},    "f25_brand_equity_equity_moat_jerk_42d_v060_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_42d_v060_signal},    "f25_brand_equity_grossmargin_jerk_63d_v061_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_63d_v061_signal},    "f25_brand_equity_pe_jerk_63d_v062_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_63d_v062_signal},    "f25_brand_equity_pb_jerk_63d_v063_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_63d_v063_signal},    "f25_brand_equity_equity_moat_jerk_63d_v064_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_63d_v064_signal},    "f25_brand_equity_grossmargin_jerk_126d_v065_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_126d_v065_signal},    "f25_brand_equity_pe_jerk_126d_v066_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_126d_v066_signal},    "f25_brand_equity_pb_jerk_126d_v067_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_126d_v067_signal},    "f25_brand_equity_equity_moat_jerk_126d_v068_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_126d_v068_signal},    "f25_brand_equity_grossmargin_jerk_252d_v069_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_252d_v069_signal},    "f25_brand_equity_pe_jerk_252d_v070_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_252d_v070_signal},    "f25_brand_equity_pb_jerk_252d_v071_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_252d_v071_signal},    "f25_brand_equity_equity_moat_jerk_252d_v072_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_252d_v072_signal},    "f25_brand_equity_grossmargin_jerk_504d_v073_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_504d_v073_signal},    "f25_brand_equity_pe_jerk_504d_v074_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_504d_v074_signal},    "f25_brand_equity_pb_jerk_504d_v075_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_504d_v075_signal},    "f25_brand_equity_equity_moat_jerk_504d_v076_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_504d_v076_signal},    "f25_brand_equity_grossmargin_jerk_756d_v077_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_756d_v077_signal},    "f25_brand_equity_pe_jerk_756d_v078_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_756d_v078_signal},    "f25_brand_equity_pb_jerk_756d_v079_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_756d_v079_signal},    "f25_brand_equity_equity_moat_jerk_756d_v080_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_756d_v080_signal},    "f25_brand_equity_grossmargin_jerk_1008d_v081_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_1008d_v081_signal},    "f25_brand_equity_pe_jerk_1008d_v082_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_1008d_v082_signal},    "f25_brand_equity_pb_jerk_1008d_v083_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_1008d_v083_signal},    "f25_brand_equity_equity_moat_jerk_1008d_v084_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_1008d_v084_signal},    "f25_brand_equity_grossmargin_jerk_1260d_v085_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_jerk_1260d_v085_signal},    "f25_brand_equity_pe_jerk_1260d_v086_signal": {"inputs": [], "func": f25_brand_equity_pe_jerk_1260d_v086_signal},    "f25_brand_equity_pb_jerk_1260d_v087_signal": {"inputs": [], "func": f25_brand_equity_pb_jerk_1260d_v087_signal},    "f25_brand_equity_equity_moat_jerk_1260d_v088_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_jerk_1260d_v088_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_5d_v089_signal},    "f25_brand_equity_pe_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_5d_v090_signal},    "f25_brand_equity_pb_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_5d_v091_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_5d_v092_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_10d_v093_signal},    "f25_brand_equity_pe_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_10d_v094_signal},    "f25_brand_equity_pb_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_10d_v095_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_10d_v096_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_21d_v097_signal},    "f25_brand_equity_pe_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_21d_v098_signal},    "f25_brand_equity_pb_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_21d_v099_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_21d_v100_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_42d_v101_signal},    "f25_brand_equity_pe_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_42d_v102_signal},    "f25_brand_equity_pb_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_42d_v103_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_42d_v104_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_63d_v105_signal},    "f25_brand_equity_pe_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_63d_v106_signal},    "f25_brand_equity_pb_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_63d_v107_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_63d_v108_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_126d_v109_signal},    "f25_brand_equity_pe_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_126d_v110_signal},    "f25_brand_equity_pb_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_126d_v111_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_126d_v112_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_252d_v113_signal},    "f25_brand_equity_pe_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_252d_v114_signal},    "f25_brand_equity_pb_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_252d_v115_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_252d_v116_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_504d_v117_signal},    "f25_brand_equity_pe_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_504d_v118_signal},    "f25_brand_equity_pb_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_504d_v119_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_504d_v120_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_756d_v121_signal},    "f25_brand_equity_pe_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_756d_v122_signal},    "f25_brand_equity_pb_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_756d_v123_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_756d_v124_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_1008d_v125_signal},    "f25_brand_equity_pe_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_1008d_v126_signal},    "f25_brand_equity_pb_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_1008d_v127_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_1008d_v128_signal},    "f25_brand_equity_grossmargin_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_slope_diff_norm_1260d_v129_signal},    "f25_brand_equity_pe_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f25_brand_equity_pe_slope_diff_norm_1260d_v130_signal},    "f25_brand_equity_pb_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f25_brand_equity_pb_slope_diff_norm_1260d_v131_signal},    "f25_brand_equity_equity_moat_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_slope_diff_norm_1260d_v132_signal},    "f25_brand_equity_grossmargin_mom_z_5d_v133_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_mom_z_5d_v133_signal},    "f25_brand_equity_pe_mom_z_5d_v134_signal": {"inputs": [], "func": f25_brand_equity_pe_mom_z_5d_v134_signal},    "f25_brand_equity_pb_mom_z_5d_v135_signal": {"inputs": [], "func": f25_brand_equity_pb_mom_z_5d_v135_signal},    "f25_brand_equity_equity_moat_mom_z_5d_v136_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_mom_z_5d_v136_signal},    "f25_brand_equity_grossmargin_mom_z_10d_v137_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_mom_z_10d_v137_signal},    "f25_brand_equity_pe_mom_z_10d_v138_signal": {"inputs": [], "func": f25_brand_equity_pe_mom_z_10d_v138_signal},    "f25_brand_equity_pb_mom_z_10d_v139_signal": {"inputs": [], "func": f25_brand_equity_pb_mom_z_10d_v139_signal},    "f25_brand_equity_equity_moat_mom_z_10d_v140_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_mom_z_10d_v140_signal},    "f25_brand_equity_grossmargin_mom_z_21d_v141_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_mom_z_21d_v141_signal},    "f25_brand_equity_pe_mom_z_21d_v142_signal": {"inputs": [], "func": f25_brand_equity_pe_mom_z_21d_v142_signal},    "f25_brand_equity_pb_mom_z_21d_v143_signal": {"inputs": [], "func": f25_brand_equity_pb_mom_z_21d_v143_signal},    "f25_brand_equity_equity_moat_mom_z_21d_v144_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_mom_z_21d_v144_signal},    "f25_brand_equity_grossmargin_mom_z_42d_v145_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_mom_z_42d_v145_signal},    "f25_brand_equity_pe_mom_z_42d_v146_signal": {"inputs": [], "func": f25_brand_equity_pe_mom_z_42d_v146_signal},    "f25_brand_equity_pb_mom_z_42d_v147_signal": {"inputs": [], "func": f25_brand_equity_pb_mom_z_42d_v147_signal},    "f25_brand_equity_equity_moat_mom_z_42d_v148_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_mom_z_42d_v148_signal},    "f25_brand_equity_grossmargin_mom_z_63d_v149_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_mom_z_63d_v149_signal},    "f25_brand_equity_pe_mom_z_63d_v150_signal": {"inputs": [], "func": f25_brand_equity_pe_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 25...")
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
