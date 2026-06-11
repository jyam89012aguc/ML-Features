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

def f09_mna_valuation_pb_slope_pct_5d_v001_signal(pb):
    """Percentage slope for Raw level of pb over 5d window."""
    res = _slope_pct(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_5d_v002_signal(pe):
    """Percentage slope for Raw level of pe over 5d window."""
    res = _slope_pct(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_5d_v003_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_5d_v004_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 5d window."""
    res = _slope_pct(pb * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_5d_v005_signal(marketcap):
    """Percentage slope for Size-based discount factor over 5d window."""
    res = _slope_pct(1 / marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_10d_v006_signal(pb):
    """Percentage slope for Raw level of pb over 10d window."""
    res = _slope_pct(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_10d_v007_signal(pe):
    """Percentage slope for Raw level of pe over 10d window."""
    res = _slope_pct(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_10d_v008_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_10d_v009_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 10d window."""
    res = _slope_pct(pb * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_10d_v010_signal(marketcap):
    """Percentage slope for Size-based discount factor over 10d window."""
    res = _slope_pct(1 / marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_21d_v011_signal(pb):
    """Percentage slope for Raw level of pb over 21d window."""
    res = _slope_pct(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_21d_v012_signal(pe):
    """Percentage slope for Raw level of pe over 21d window."""
    res = _slope_pct(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_21d_v013_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_21d_v014_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 21d window."""
    res = _slope_pct(pb * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_21d_v015_signal(marketcap):
    """Percentage slope for Size-based discount factor over 21d window."""
    res = _slope_pct(1 / marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_42d_v016_signal(pb):
    """Percentage slope for Raw level of pb over 42d window."""
    res = _slope_pct(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_42d_v017_signal(pe):
    """Percentage slope for Raw level of pe over 42d window."""
    res = _slope_pct(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_42d_v018_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_42d_v019_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 42d window."""
    res = _slope_pct(pb * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_42d_v020_signal(marketcap):
    """Percentage slope for Size-based discount factor over 42d window."""
    res = _slope_pct(1 / marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_63d_v021_signal(pb):
    """Percentage slope for Raw level of pb over 63d window."""
    res = _slope_pct(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_63d_v022_signal(pe):
    """Percentage slope for Raw level of pe over 63d window."""
    res = _slope_pct(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_63d_v023_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_63d_v024_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 63d window."""
    res = _slope_pct(pb * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_63d_v025_signal(marketcap):
    """Percentage slope for Size-based discount factor over 63d window."""
    res = _slope_pct(1 / marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_126d_v026_signal(pb):
    """Percentage slope for Raw level of pb over 126d window."""
    res = _slope_pct(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_126d_v027_signal(pe):
    """Percentage slope for Raw level of pe over 126d window."""
    res = _slope_pct(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_126d_v028_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_126d_v029_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 126d window."""
    res = _slope_pct(pb * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_126d_v030_signal(marketcap):
    """Percentage slope for Size-based discount factor over 126d window."""
    res = _slope_pct(1 / marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_252d_v031_signal(pb):
    """Percentage slope for Raw level of pb over 252d window."""
    res = _slope_pct(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_252d_v032_signal(pe):
    """Percentage slope for Raw level of pe over 252d window."""
    res = _slope_pct(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_252d_v033_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_252d_v034_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 252d window."""
    res = _slope_pct(pb * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_252d_v035_signal(marketcap):
    """Percentage slope for Size-based discount factor over 252d window."""
    res = _slope_pct(1 / marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_504d_v036_signal(pb):
    """Percentage slope for Raw level of pb over 504d window."""
    res = _slope_pct(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_504d_v037_signal(pe):
    """Percentage slope for Raw level of pe over 504d window."""
    res = _slope_pct(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_504d_v038_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_504d_v039_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 504d window."""
    res = _slope_pct(pb * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_504d_v040_signal(marketcap):
    """Percentage slope for Size-based discount factor over 504d window."""
    res = _slope_pct(1 / marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_756d_v041_signal(pb):
    """Percentage slope for Raw level of pb over 756d window."""
    res = _slope_pct(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_756d_v042_signal(pe):
    """Percentage slope for Raw level of pe over 756d window."""
    res = _slope_pct(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_756d_v043_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_756d_v044_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 756d window."""
    res = _slope_pct(pb * pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_756d_v045_signal(marketcap):
    """Percentage slope for Size-based discount factor over 756d window."""
    res = _slope_pct(1 / marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_1008d_v046_signal(pb):
    """Percentage slope for Raw level of pb over 1008d window."""
    res = _slope_pct(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_1008d_v047_signal(pe):
    """Percentage slope for Raw level of pe over 1008d window."""
    res = _slope_pct(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_1008d_v048_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_1008d_v049_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 1008d window."""
    res = _slope_pct(pb * pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_1008d_v050_signal(marketcap):
    """Percentage slope for Size-based discount factor over 1008d window."""
    res = _slope_pct(1 / marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_pct_1260d_v051_signal(pb):
    """Percentage slope for Raw level of pb over 1260d window."""
    res = _slope_pct(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_pct_1260d_v052_signal(pe):
    """Percentage slope for Raw level of pe over 1260d window."""
    res = _slope_pct(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_pct_1260d_v053_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_pct_1260d_v054_signal(pb, pe):
    """Percentage slope for Combined P/B and P/E valuation metric over 1260d window."""
    res = _slope_pct(pb * pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_pct_1260d_v055_signal(marketcap):
    """Percentage slope for Size-based discount factor over 1260d window."""
    res = _slope_pct(1 / marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_5d_v056_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 5d window."""
    res = _jerk(pb, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_5d_v057_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 5d window."""
    res = _jerk(pe, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_5d_v058_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_5d_v059_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 5d window."""
    res = _jerk(pb * pe, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_5d_v060_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 5d window."""
    res = _jerk(1 / marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_10d_v061_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 10d window."""
    res = _jerk(pb, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_10d_v062_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 10d window."""
    res = _jerk(pe, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_10d_v063_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_10d_v064_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 10d window."""
    res = _jerk(pb * pe, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_10d_v065_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 10d window."""
    res = _jerk(1 / marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_21d_v066_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 21d window."""
    res = _jerk(pb, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_21d_v067_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 21d window."""
    res = _jerk(pe, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_21d_v068_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_21d_v069_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 21d window."""
    res = _jerk(pb * pe, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_21d_v070_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 21d window."""
    res = _jerk(1 / marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_42d_v071_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 42d window."""
    res = _jerk(pb, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_42d_v072_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 42d window."""
    res = _jerk(pe, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_42d_v073_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_42d_v074_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 42d window."""
    res = _jerk(pb * pe, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_42d_v075_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 42d window."""
    res = _jerk(1 / marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_63d_v076_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 63d window."""
    res = _jerk(pb, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_63d_v077_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 63d window."""
    res = _jerk(pe, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_63d_v078_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_63d_v079_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 63d window."""
    res = _jerk(pb * pe, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_63d_v080_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 63d window."""
    res = _jerk(1 / marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_126d_v081_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 126d window."""
    res = _jerk(pb, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_126d_v082_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 126d window."""
    res = _jerk(pe, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_126d_v083_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_126d_v084_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 126d window."""
    res = _jerk(pb * pe, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_126d_v085_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 126d window."""
    res = _jerk(1 / marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_252d_v086_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 252d window."""
    res = _jerk(pb, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_252d_v087_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 252d window."""
    res = _jerk(pe, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_252d_v088_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_252d_v089_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 252d window."""
    res = _jerk(pb * pe, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_252d_v090_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 252d window."""
    res = _jerk(1 / marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_504d_v091_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 504d window."""
    res = _jerk(pb, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_504d_v092_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 504d window."""
    res = _jerk(pe, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_504d_v093_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_504d_v094_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 504d window."""
    res = _jerk(pb * pe, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_504d_v095_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 504d window."""
    res = _jerk(1 / marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_756d_v096_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 756d window."""
    res = _jerk(pb, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_756d_v097_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 756d window."""
    res = _jerk(pe, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_756d_v098_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_756d_v099_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 756d window."""
    res = _jerk(pb * pe, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_756d_v100_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 756d window."""
    res = _jerk(1 / marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_1008d_v101_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1008d window."""
    res = _jerk(pb, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_1008d_v102_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 1008d window."""
    res = _jerk(pe, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_1008d_v103_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_1008d_v104_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 1008d window."""
    res = _jerk(pb * pe, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_1008d_v105_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 1008d window."""
    res = _jerk(1 / marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_jerk_1260d_v106_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1260d window."""
    res = _jerk(pb, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_jerk_1260d_v107_signal(pe):
    """Acceleration/Jerk for Raw level of pe over 1260d window."""
    res = _jerk(pe, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_jerk_1260d_v108_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_jerk_1260d_v109_signal(pb, pe):
    """Acceleration/Jerk for Combined P/B and P/E valuation metric over 1260d window."""
    res = _jerk(pb * pe, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_jerk_1260d_v110_signal(marketcap):
    """Acceleration/Jerk for Size-based discount factor over 1260d window."""
    res = _jerk(1 / marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_5d_v111_signal(pb):
    """Normalized slope change for Raw level of pb over 5d window."""
    res = (_slope_pct(pb, 5).diff(5) / _sma(pb.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_5d_v112_signal(pe):
    """Normalized slope change for Raw level of pe over 5d window."""
    res = (_slope_pct(pe, 5).diff(5) / _sma(pe.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_5d_v113_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_5d_v114_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 5d window."""
    res = (_slope_pct(pb * pe, 5).diff(5) / _sma(pb * pe.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_5d_v115_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 5d window."""
    res = (_slope_pct(1 / marketcap, 5).diff(5) / _sma(1 / marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_10d_v116_signal(pb):
    """Normalized slope change for Raw level of pb over 10d window."""
    res = (_slope_pct(pb, 10).diff(10) / _sma(pb.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_10d_v117_signal(pe):
    """Normalized slope change for Raw level of pe over 10d window."""
    res = (_slope_pct(pe, 10).diff(10) / _sma(pe.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_10d_v118_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_10d_v119_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 10d window."""
    res = (_slope_pct(pb * pe, 10).diff(10) / _sma(pb * pe.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_10d_v120_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 10d window."""
    res = (_slope_pct(1 / marketcap, 10).diff(10) / _sma(1 / marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_21d_v121_signal(pb):
    """Normalized slope change for Raw level of pb over 21d window."""
    res = (_slope_pct(pb, 21).diff(21) / _sma(pb.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_21d_v122_signal(pe):
    """Normalized slope change for Raw level of pe over 21d window."""
    res = (_slope_pct(pe, 21).diff(21) / _sma(pe.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_21d_v123_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_21d_v124_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 21d window."""
    res = (_slope_pct(pb * pe, 21).diff(21) / _sma(pb * pe.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_21d_v125_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 21d window."""
    res = (_slope_pct(1 / marketcap, 21).diff(21) / _sma(1 / marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_42d_v126_signal(pb):
    """Normalized slope change for Raw level of pb over 42d window."""
    res = (_slope_pct(pb, 42).diff(42) / _sma(pb.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_42d_v127_signal(pe):
    """Normalized slope change for Raw level of pe over 42d window."""
    res = (_slope_pct(pe, 42).diff(42) / _sma(pe.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_42d_v128_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_42d_v129_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 42d window."""
    res = (_slope_pct(pb * pe, 42).diff(42) / _sma(pb * pe.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_42d_v130_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 42d window."""
    res = (_slope_pct(1 / marketcap, 42).diff(42) / _sma(1 / marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_63d_v131_signal(pb):
    """Normalized slope change for Raw level of pb over 63d window."""
    res = (_slope_pct(pb, 63).diff(63) / _sma(pb.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_63d_v132_signal(pe):
    """Normalized slope change for Raw level of pe over 63d window."""
    res = (_slope_pct(pe, 63).diff(63) / _sma(pe.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_63d_v133_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_63d_v134_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 63d window."""
    res = (_slope_pct(pb * pe, 63).diff(63) / _sma(pb * pe.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_63d_v135_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 63d window."""
    res = (_slope_pct(1 / marketcap, 63).diff(63) / _sma(1 / marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_126d_v136_signal(pb):
    """Normalized slope change for Raw level of pb over 126d window."""
    res = (_slope_pct(pb, 126).diff(126) / _sma(pb.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_126d_v137_signal(pe):
    """Normalized slope change for Raw level of pe over 126d window."""
    res = (_slope_pct(pe, 126).diff(126) / _sma(pe.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_126d_v138_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_126d_v139_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 126d window."""
    res = (_slope_pct(pb * pe, 126).diff(126) / _sma(pb * pe.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_126d_v140_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 126d window."""
    res = (_slope_pct(1 / marketcap, 126).diff(126) / _sma(1 / marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_252d_v141_signal(pb):
    """Normalized slope change for Raw level of pb over 252d window."""
    res = (_slope_pct(pb, 252).diff(252) / _sma(pb.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_252d_v142_signal(pe):
    """Normalized slope change for Raw level of pe over 252d window."""
    res = (_slope_pct(pe, 252).diff(252) / _sma(pe.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_252d_v143_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_252d_v144_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 252d window."""
    res = (_slope_pct(pb * pe, 252).diff(252) / _sma(pb * pe.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_252d_v145_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 252d window."""
    res = (_slope_pct(1 / marketcap, 252).diff(252) / _sma(1 / marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_504d_v146_signal(pb):
    """Normalized slope change for Raw level of pb over 504d window."""
    res = (_slope_pct(pb, 504).diff(504) / _sma(pb.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_504d_v147_signal(pe):
    """Normalized slope change for Raw level of pe over 504d window."""
    res = (_slope_pct(pe, 504).diff(504) / _sma(pe.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_504d_v148_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_504d_v149_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 504d window."""
    res = (_slope_pct(pb * pe, 504).diff(504) / _sma(pb * pe.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_504d_v150_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 504d window."""
    res = (_slope_pct(1 / marketcap, 504).diff(504) / _sma(1 / marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f09_mna_valuation_pb_slope_pct_5d_v001_signal": {"func": f09_mna_valuation_pb_slope_pct_5d_v001_signal},
    "f09_mna_valuation_pe_slope_pct_5d_v002_signal": {"func": f09_mna_valuation_pe_slope_pct_5d_v002_signal},
    "f09_mna_valuation_marketcap_slope_pct_5d_v003_signal": {"func": f09_mna_valuation_marketcap_slope_pct_5d_v003_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_5d_v004_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_5d_v004_signal},
    "f09_mna_valuation_size_factor_slope_pct_5d_v005_signal": {"func": f09_mna_valuation_size_factor_slope_pct_5d_v005_signal},
    "f09_mna_valuation_pb_slope_pct_10d_v006_signal": {"func": f09_mna_valuation_pb_slope_pct_10d_v006_signal},
    "f09_mna_valuation_pe_slope_pct_10d_v007_signal": {"func": f09_mna_valuation_pe_slope_pct_10d_v007_signal},
    "f09_mna_valuation_marketcap_slope_pct_10d_v008_signal": {"func": f09_mna_valuation_marketcap_slope_pct_10d_v008_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_10d_v009_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_10d_v009_signal},
    "f09_mna_valuation_size_factor_slope_pct_10d_v010_signal": {"func": f09_mna_valuation_size_factor_slope_pct_10d_v010_signal},
    "f09_mna_valuation_pb_slope_pct_21d_v011_signal": {"func": f09_mna_valuation_pb_slope_pct_21d_v011_signal},
    "f09_mna_valuation_pe_slope_pct_21d_v012_signal": {"func": f09_mna_valuation_pe_slope_pct_21d_v012_signal},
    "f09_mna_valuation_marketcap_slope_pct_21d_v013_signal": {"func": f09_mna_valuation_marketcap_slope_pct_21d_v013_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_21d_v014_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_21d_v014_signal},
    "f09_mna_valuation_size_factor_slope_pct_21d_v015_signal": {"func": f09_mna_valuation_size_factor_slope_pct_21d_v015_signal},
    "f09_mna_valuation_pb_slope_pct_42d_v016_signal": {"func": f09_mna_valuation_pb_slope_pct_42d_v016_signal},
    "f09_mna_valuation_pe_slope_pct_42d_v017_signal": {"func": f09_mna_valuation_pe_slope_pct_42d_v017_signal},
    "f09_mna_valuation_marketcap_slope_pct_42d_v018_signal": {"func": f09_mna_valuation_marketcap_slope_pct_42d_v018_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_42d_v019_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_42d_v019_signal},
    "f09_mna_valuation_size_factor_slope_pct_42d_v020_signal": {"func": f09_mna_valuation_size_factor_slope_pct_42d_v020_signal},
    "f09_mna_valuation_pb_slope_pct_63d_v021_signal": {"func": f09_mna_valuation_pb_slope_pct_63d_v021_signal},
    "f09_mna_valuation_pe_slope_pct_63d_v022_signal": {"func": f09_mna_valuation_pe_slope_pct_63d_v022_signal},
    "f09_mna_valuation_marketcap_slope_pct_63d_v023_signal": {"func": f09_mna_valuation_marketcap_slope_pct_63d_v023_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_63d_v024_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_63d_v024_signal},
    "f09_mna_valuation_size_factor_slope_pct_63d_v025_signal": {"func": f09_mna_valuation_size_factor_slope_pct_63d_v025_signal},
    "f09_mna_valuation_pb_slope_pct_126d_v026_signal": {"func": f09_mna_valuation_pb_slope_pct_126d_v026_signal},
    "f09_mna_valuation_pe_slope_pct_126d_v027_signal": {"func": f09_mna_valuation_pe_slope_pct_126d_v027_signal},
    "f09_mna_valuation_marketcap_slope_pct_126d_v028_signal": {"func": f09_mna_valuation_marketcap_slope_pct_126d_v028_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_126d_v029_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_126d_v029_signal},
    "f09_mna_valuation_size_factor_slope_pct_126d_v030_signal": {"func": f09_mna_valuation_size_factor_slope_pct_126d_v030_signal},
    "f09_mna_valuation_pb_slope_pct_252d_v031_signal": {"func": f09_mna_valuation_pb_slope_pct_252d_v031_signal},
    "f09_mna_valuation_pe_slope_pct_252d_v032_signal": {"func": f09_mna_valuation_pe_slope_pct_252d_v032_signal},
    "f09_mna_valuation_marketcap_slope_pct_252d_v033_signal": {"func": f09_mna_valuation_marketcap_slope_pct_252d_v033_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_252d_v034_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_252d_v034_signal},
    "f09_mna_valuation_size_factor_slope_pct_252d_v035_signal": {"func": f09_mna_valuation_size_factor_slope_pct_252d_v035_signal},
    "f09_mna_valuation_pb_slope_pct_504d_v036_signal": {"func": f09_mna_valuation_pb_slope_pct_504d_v036_signal},
    "f09_mna_valuation_pe_slope_pct_504d_v037_signal": {"func": f09_mna_valuation_pe_slope_pct_504d_v037_signal},
    "f09_mna_valuation_marketcap_slope_pct_504d_v038_signal": {"func": f09_mna_valuation_marketcap_slope_pct_504d_v038_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_504d_v039_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_504d_v039_signal},
    "f09_mna_valuation_size_factor_slope_pct_504d_v040_signal": {"func": f09_mna_valuation_size_factor_slope_pct_504d_v040_signal},
    "f09_mna_valuation_pb_slope_pct_756d_v041_signal": {"func": f09_mna_valuation_pb_slope_pct_756d_v041_signal},
    "f09_mna_valuation_pe_slope_pct_756d_v042_signal": {"func": f09_mna_valuation_pe_slope_pct_756d_v042_signal},
    "f09_mna_valuation_marketcap_slope_pct_756d_v043_signal": {"func": f09_mna_valuation_marketcap_slope_pct_756d_v043_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_756d_v044_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_756d_v044_signal},
    "f09_mna_valuation_size_factor_slope_pct_756d_v045_signal": {"func": f09_mna_valuation_size_factor_slope_pct_756d_v045_signal},
    "f09_mna_valuation_pb_slope_pct_1008d_v046_signal": {"func": f09_mna_valuation_pb_slope_pct_1008d_v046_signal},
    "f09_mna_valuation_pe_slope_pct_1008d_v047_signal": {"func": f09_mna_valuation_pe_slope_pct_1008d_v047_signal},
    "f09_mna_valuation_marketcap_slope_pct_1008d_v048_signal": {"func": f09_mna_valuation_marketcap_slope_pct_1008d_v048_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_1008d_v049_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_1008d_v049_signal},
    "f09_mna_valuation_size_factor_slope_pct_1008d_v050_signal": {"func": f09_mna_valuation_size_factor_slope_pct_1008d_v050_signal},
    "f09_mna_valuation_pb_slope_pct_1260d_v051_signal": {"func": f09_mna_valuation_pb_slope_pct_1260d_v051_signal},
    "f09_mna_valuation_pe_slope_pct_1260d_v052_signal": {"func": f09_mna_valuation_pe_slope_pct_1260d_v052_signal},
    "f09_mna_valuation_marketcap_slope_pct_1260d_v053_signal": {"func": f09_mna_valuation_marketcap_slope_pct_1260d_v053_signal},
    "f09_mna_valuation_valuation_composite_slope_pct_1260d_v054_signal": {"func": f09_mna_valuation_valuation_composite_slope_pct_1260d_v054_signal},
    "f09_mna_valuation_size_factor_slope_pct_1260d_v055_signal": {"func": f09_mna_valuation_size_factor_slope_pct_1260d_v055_signal},
    "f09_mna_valuation_pb_jerk_5d_v056_signal": {"func": f09_mna_valuation_pb_jerk_5d_v056_signal},
    "f09_mna_valuation_pe_jerk_5d_v057_signal": {"func": f09_mna_valuation_pe_jerk_5d_v057_signal},
    "f09_mna_valuation_marketcap_jerk_5d_v058_signal": {"func": f09_mna_valuation_marketcap_jerk_5d_v058_signal},
    "f09_mna_valuation_valuation_composite_jerk_5d_v059_signal": {"func": f09_mna_valuation_valuation_composite_jerk_5d_v059_signal},
    "f09_mna_valuation_size_factor_jerk_5d_v060_signal": {"func": f09_mna_valuation_size_factor_jerk_5d_v060_signal},
    "f09_mna_valuation_pb_jerk_10d_v061_signal": {"func": f09_mna_valuation_pb_jerk_10d_v061_signal},
    "f09_mna_valuation_pe_jerk_10d_v062_signal": {"func": f09_mna_valuation_pe_jerk_10d_v062_signal},
    "f09_mna_valuation_marketcap_jerk_10d_v063_signal": {"func": f09_mna_valuation_marketcap_jerk_10d_v063_signal},
    "f09_mna_valuation_valuation_composite_jerk_10d_v064_signal": {"func": f09_mna_valuation_valuation_composite_jerk_10d_v064_signal},
    "f09_mna_valuation_size_factor_jerk_10d_v065_signal": {"func": f09_mna_valuation_size_factor_jerk_10d_v065_signal},
    "f09_mna_valuation_pb_jerk_21d_v066_signal": {"func": f09_mna_valuation_pb_jerk_21d_v066_signal},
    "f09_mna_valuation_pe_jerk_21d_v067_signal": {"func": f09_mna_valuation_pe_jerk_21d_v067_signal},
    "f09_mna_valuation_marketcap_jerk_21d_v068_signal": {"func": f09_mna_valuation_marketcap_jerk_21d_v068_signal},
    "f09_mna_valuation_valuation_composite_jerk_21d_v069_signal": {"func": f09_mna_valuation_valuation_composite_jerk_21d_v069_signal},
    "f09_mna_valuation_size_factor_jerk_21d_v070_signal": {"func": f09_mna_valuation_size_factor_jerk_21d_v070_signal},
    "f09_mna_valuation_pb_jerk_42d_v071_signal": {"func": f09_mna_valuation_pb_jerk_42d_v071_signal},
    "f09_mna_valuation_pe_jerk_42d_v072_signal": {"func": f09_mna_valuation_pe_jerk_42d_v072_signal},
    "f09_mna_valuation_marketcap_jerk_42d_v073_signal": {"func": f09_mna_valuation_marketcap_jerk_42d_v073_signal},
    "f09_mna_valuation_valuation_composite_jerk_42d_v074_signal": {"func": f09_mna_valuation_valuation_composite_jerk_42d_v074_signal},
    "f09_mna_valuation_size_factor_jerk_42d_v075_signal": {"func": f09_mna_valuation_size_factor_jerk_42d_v075_signal},
    "f09_mna_valuation_pb_jerk_63d_v076_signal": {"func": f09_mna_valuation_pb_jerk_63d_v076_signal},
    "f09_mna_valuation_pe_jerk_63d_v077_signal": {"func": f09_mna_valuation_pe_jerk_63d_v077_signal},
    "f09_mna_valuation_marketcap_jerk_63d_v078_signal": {"func": f09_mna_valuation_marketcap_jerk_63d_v078_signal},
    "f09_mna_valuation_valuation_composite_jerk_63d_v079_signal": {"func": f09_mna_valuation_valuation_composite_jerk_63d_v079_signal},
    "f09_mna_valuation_size_factor_jerk_63d_v080_signal": {"func": f09_mna_valuation_size_factor_jerk_63d_v080_signal},
    "f09_mna_valuation_pb_jerk_126d_v081_signal": {"func": f09_mna_valuation_pb_jerk_126d_v081_signal},
    "f09_mna_valuation_pe_jerk_126d_v082_signal": {"func": f09_mna_valuation_pe_jerk_126d_v082_signal},
    "f09_mna_valuation_marketcap_jerk_126d_v083_signal": {"func": f09_mna_valuation_marketcap_jerk_126d_v083_signal},
    "f09_mna_valuation_valuation_composite_jerk_126d_v084_signal": {"func": f09_mna_valuation_valuation_composite_jerk_126d_v084_signal},
    "f09_mna_valuation_size_factor_jerk_126d_v085_signal": {"func": f09_mna_valuation_size_factor_jerk_126d_v085_signal},
    "f09_mna_valuation_pb_jerk_252d_v086_signal": {"func": f09_mna_valuation_pb_jerk_252d_v086_signal},
    "f09_mna_valuation_pe_jerk_252d_v087_signal": {"func": f09_mna_valuation_pe_jerk_252d_v087_signal},
    "f09_mna_valuation_marketcap_jerk_252d_v088_signal": {"func": f09_mna_valuation_marketcap_jerk_252d_v088_signal},
    "f09_mna_valuation_valuation_composite_jerk_252d_v089_signal": {"func": f09_mna_valuation_valuation_composite_jerk_252d_v089_signal},
    "f09_mna_valuation_size_factor_jerk_252d_v090_signal": {"func": f09_mna_valuation_size_factor_jerk_252d_v090_signal},
    "f09_mna_valuation_pb_jerk_504d_v091_signal": {"func": f09_mna_valuation_pb_jerk_504d_v091_signal},
    "f09_mna_valuation_pe_jerk_504d_v092_signal": {"func": f09_mna_valuation_pe_jerk_504d_v092_signal},
    "f09_mna_valuation_marketcap_jerk_504d_v093_signal": {"func": f09_mna_valuation_marketcap_jerk_504d_v093_signal},
    "f09_mna_valuation_valuation_composite_jerk_504d_v094_signal": {"func": f09_mna_valuation_valuation_composite_jerk_504d_v094_signal},
    "f09_mna_valuation_size_factor_jerk_504d_v095_signal": {"func": f09_mna_valuation_size_factor_jerk_504d_v095_signal},
    "f09_mna_valuation_pb_jerk_756d_v096_signal": {"func": f09_mna_valuation_pb_jerk_756d_v096_signal},
    "f09_mna_valuation_pe_jerk_756d_v097_signal": {"func": f09_mna_valuation_pe_jerk_756d_v097_signal},
    "f09_mna_valuation_marketcap_jerk_756d_v098_signal": {"func": f09_mna_valuation_marketcap_jerk_756d_v098_signal},
    "f09_mna_valuation_valuation_composite_jerk_756d_v099_signal": {"func": f09_mna_valuation_valuation_composite_jerk_756d_v099_signal},
    "f09_mna_valuation_size_factor_jerk_756d_v100_signal": {"func": f09_mna_valuation_size_factor_jerk_756d_v100_signal},
    "f09_mna_valuation_pb_jerk_1008d_v101_signal": {"func": f09_mna_valuation_pb_jerk_1008d_v101_signal},
    "f09_mna_valuation_pe_jerk_1008d_v102_signal": {"func": f09_mna_valuation_pe_jerk_1008d_v102_signal},
    "f09_mna_valuation_marketcap_jerk_1008d_v103_signal": {"func": f09_mna_valuation_marketcap_jerk_1008d_v103_signal},
    "f09_mna_valuation_valuation_composite_jerk_1008d_v104_signal": {"func": f09_mna_valuation_valuation_composite_jerk_1008d_v104_signal},
    "f09_mna_valuation_size_factor_jerk_1008d_v105_signal": {"func": f09_mna_valuation_size_factor_jerk_1008d_v105_signal},
    "f09_mna_valuation_pb_jerk_1260d_v106_signal": {"func": f09_mna_valuation_pb_jerk_1260d_v106_signal},
    "f09_mna_valuation_pe_jerk_1260d_v107_signal": {"func": f09_mna_valuation_pe_jerk_1260d_v107_signal},
    "f09_mna_valuation_marketcap_jerk_1260d_v108_signal": {"func": f09_mna_valuation_marketcap_jerk_1260d_v108_signal},
    "f09_mna_valuation_valuation_composite_jerk_1260d_v109_signal": {"func": f09_mna_valuation_valuation_composite_jerk_1260d_v109_signal},
    "f09_mna_valuation_size_factor_jerk_1260d_v110_signal": {"func": f09_mna_valuation_size_factor_jerk_1260d_v110_signal},
    "f09_mna_valuation_pb_slope_diff_norm_5d_v111_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_5d_v111_signal},
    "f09_mna_valuation_pe_slope_diff_norm_5d_v112_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_5d_v112_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_5d_v113_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_5d_v113_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_5d_v114_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_5d_v114_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_5d_v115_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_5d_v115_signal},
    "f09_mna_valuation_pb_slope_diff_norm_10d_v116_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_10d_v116_signal},
    "f09_mna_valuation_pe_slope_diff_norm_10d_v117_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_10d_v117_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_10d_v118_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_10d_v118_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_10d_v119_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_10d_v119_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_10d_v120_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_10d_v120_signal},
    "f09_mna_valuation_pb_slope_diff_norm_21d_v121_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_21d_v121_signal},
    "f09_mna_valuation_pe_slope_diff_norm_21d_v122_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_21d_v122_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_21d_v123_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_21d_v123_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_21d_v124_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_21d_v124_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_21d_v125_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_21d_v125_signal},
    "f09_mna_valuation_pb_slope_diff_norm_42d_v126_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_42d_v126_signal},
    "f09_mna_valuation_pe_slope_diff_norm_42d_v127_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_42d_v127_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_42d_v128_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_42d_v128_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_42d_v129_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_42d_v129_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_42d_v130_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_42d_v130_signal},
    "f09_mna_valuation_pb_slope_diff_norm_63d_v131_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_63d_v131_signal},
    "f09_mna_valuation_pe_slope_diff_norm_63d_v132_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_63d_v132_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_63d_v133_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_63d_v133_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_63d_v134_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_63d_v134_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_63d_v135_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_63d_v135_signal},
    "f09_mna_valuation_pb_slope_diff_norm_126d_v136_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_126d_v136_signal},
    "f09_mna_valuation_pe_slope_diff_norm_126d_v137_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_126d_v137_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_126d_v138_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_126d_v138_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_126d_v139_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_126d_v139_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_126d_v140_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_126d_v140_signal},
    "f09_mna_valuation_pb_slope_diff_norm_252d_v141_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_252d_v141_signal},
    "f09_mna_valuation_pe_slope_diff_norm_252d_v142_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_252d_v142_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_252d_v143_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_252d_v143_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_252d_v144_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_252d_v144_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_252d_v145_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_252d_v145_signal},
    "f09_mna_valuation_pb_slope_diff_norm_504d_v146_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_504d_v146_signal},
    "f09_mna_valuation_pe_slope_diff_norm_504d_v147_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_504d_v147_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_504d_v148_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_504d_v148_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_504d_v149_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_504d_v149_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_504d_v150_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 09...")
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
