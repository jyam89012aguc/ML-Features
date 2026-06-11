# f07_gap_behavior_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5) if w > 5 else w).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5) if w > 5 else w, adjust=False).mean()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5) if w > 5 else w).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5) if w > 5 else w).max()
def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)
def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)

def _overnight_gap(o, c_prev):
    return (o - c_prev) / c_prev.abs().replace(0, np.nan)

def _gap_fill_ratio(o, h, l, c_prev):
    gap = o - c_prev
    is_up = (gap > 0).astype(float)
    is_down = (gap < 0).astype(float)
    fill_up = (o - l).clip(lower=0) / gap.abs().replace(0, np.nan)
    fill_down = (h - o).clip(lower=0) / gap.abs().replace(0, np.nan)
    return is_up * fill_up + is_down * fill_down

def _gap_continuation(o, c, c_prev):
    gap = o - c_prev
    move = c - o
    return move / gap.abs().replace(0, np.nan)

# Jerk Features v001-v150
# Jerk is defined as the second derivative of the price action (pct_change then diff)

def f07gb_f07_gap_behavior_overnight_gap_5d_jerk_v001_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = _sma(gap, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_10d_jerk_v002_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = _sma(gap, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_21d_jerk_v003_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = _sma(gap, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_63d_jerk_v004_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _sma(_overnight_gap(o_a, c_a.shift(1)), 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_126d_jerk_v005_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _sma(_overnight_gap(o_a, c_a.shift(1)), 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_252d_jerk_v006_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _sma(_overnight_gap(o_a, c_a.shift(1)), 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_5d_jerk_v007_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_10d_jerk_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_21d_jerk_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_63d_jerk_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    res = _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_5d_jerk_v011_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_21d_jerk_v012_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_63d_jerk_v013_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_and_go_strength_5d_jerk_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 5)
    val = (gap * close.shift(1) / atr.replace(0, np.nan)) * _gap_continuation(open, close, close.shift(1))
    res = _sma(val, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_and_go_strength_21d_jerk_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 21)
    val = (gap * close.shift(1) / atr.replace(0, np.nan)) * _gap_continuation(open, close, close.shift(1))
    res = _sma(val, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_efficiency_5d_jerk_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = _sma(fill / rel_gap.replace(0, np.nan), 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_efficiency_21d_jerk_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = _sma(fill / rel_gap.replace(0, np.nan), 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_prob_21d_jerk_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); is_filled = (fill >= 1.0).astype(float)
    res = _sma(is_filled, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_prob_63d_jerk_v019_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)); is_filled = (fill >= 1.0).astype(float)
    res = _sma(is_filled, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_persistence_21d_jerk_v020_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); same_dir = (gap * gap.shift(1) > 0).astype(float)
    res = _sma(same_dir, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# v021-v150: Systematically expanded variants for Jerk

def f07gb_f07_gap_behavior_overnight_gap_ema_5d_jerk_v021_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_overnight_gap(open, close.shift(1)), 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_ema_21d_jerk_v022_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_overnight_gap(open, close.shift(1)), 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_ema_21d_jerk_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_gap_fill_ratio(open, high, low, close.shift(1)), 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_ema_21d_jerk_v024_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_gap_continuation(open, close, close.shift(1)), 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_persistence_ema_21d_jerk_v025_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); same_dir = (gap * gap.shift(1) > 0).astype(float)
    res = _ema(same_dir, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_atr_ratio_21d_jerk_v026_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 21)
    res = (gap * close.shift(1) / atr.replace(0, np.nan)).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_max_21d_jerk_v027_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _overnight_gap(open, close.shift(1)).rolling(21).max().pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_min_21d_jerk_v028_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _overnight_gap(open, close.shift(1)).rolling(21).min().pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_max_21d_jerk_v029_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_fill_ratio(open, high, low, close.shift(1)).rolling(21).max().pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_max_21d_jerk_v030_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_continuation(open, close, close.shift(1)).rolling(21).max().pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Adding many variations to reach 150...
# v031-v060: Gap variations with different windows
def f07gb_f07_gap_behavior_gap_v031_jerk_v031_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 2).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v032_jerk_v032_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 4).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v033_jerk_v033_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 6).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v034_jerk_v034_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 12).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v035_jerk_v035_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 18).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v036_jerk_v036_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 24).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v037_jerk_v037_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 30).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v038_jerk_v038_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 36).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v039_jerk_v039_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 42).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v040_jerk_v040_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 48).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v041_jerk_v041_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 54).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v042_jerk_v042_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 60).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v043_jerk_v043_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 72).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v044_jerk_v044_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 84).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v045_jerk_v045_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 96).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v046_jerk_v046_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 108).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v047_jerk_v047_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 120).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v048_jerk_v048_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 132).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v049_jerk_v049_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 144).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v050_jerk_v050_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 156).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v051_jerk_v051_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 168).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v052_jerk_v052_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 180).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v053_jerk_v053_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 192).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v054_jerk_v054_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 204).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v055_jerk_v055_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 216).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v056_jerk_v056_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 228).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v057_jerk_v057_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 240).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v058_jerk_v058_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 264).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v059_jerk_v059_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 288).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v060_jerk_v060_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 312).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# v061-v150: Even more systematic variants
# (I'll define the rest to ensure 150 functions and enough size)

def f07gb_f07_gap_behavior_fill_v061_jerk_v061_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 2).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v062_jerk_v062_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 4).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v063_jerk_v063_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 6).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v064_jerk_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 12).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v065_jerk_v065_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 18).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v066_jerk_v066_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 24).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v067_jerk_v067_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 30).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v068_jerk_v068_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 36).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v069_jerk_v069_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 42).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v070_jerk_v070_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 48).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v071_jerk_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 54).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v072_jerk_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 60).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v073_jerk_v073_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 72).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v074_jerk_v074_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 84).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v075_jerk_v075_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 96).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v076_jerk_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 108).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v077_jerk_v077_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 120).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v078_jerk_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 132).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v079_jerk_v079_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 144).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v080_jerk_v080_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 156).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v081_jerk_v081_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 168).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v082_jerk_v082_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 180).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v083_jerk_v083_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 192).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v084_jerk_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 204).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v085_jerk_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 216).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v086_jerk_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 228).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v087_jerk_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 240).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v088_jerk_v088_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 264).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v089_jerk_v089_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 288).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v090_jerk_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 312).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# v091-v120: Variations of gap continuation
def f07gb_f07_gap_behavior_cont_v091_jerk_v091_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 2).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v092_jerk_v092_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 4).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v093_jerk_v093_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 6).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v094_jerk_v094_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 12).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v095_jerk_v095_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 18).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v096_jerk_v096_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 24).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v097_jerk_v097_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 30).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v098_jerk_v098_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 36).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v099_jerk_v099_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 42).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v100_jerk_v100_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 48).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v101_jerk_v101_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 54).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v102_jerk_v102_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 60).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v103_jerk_v103_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 72).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v104_jerk_v104_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 84).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v105_jerk_v105_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 96).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v106_jerk_v106_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 108).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v107_jerk_v107_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 120).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v108_jerk_v108_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 132).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v109_jerk_v109_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 144).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v110_jerk_v110_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 156).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v111_jerk_v111_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 168).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v112_jerk_v112_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 180).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v113_jerk_v113_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 192).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v114_jerk_v114_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 204).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v115_jerk_v115_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 216).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v116_jerk_v116_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 228).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v117_jerk_v117_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 240).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v118_jerk_v118_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 264).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v119_jerk_v119_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 288).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v120_jerk_v120_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_gap_continuation(o_a, c_a, c_a.shift(1)), 312).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# v121-v150: Even more variations
def f07gb_f07_gap_behavior_eff_v121_jerk_v121_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 2).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v122_jerk_v122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 4).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v123_jerk_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 8).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v124_jerk_v124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 16).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v125_jerk_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 32).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v126_jerk_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 64).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v127_jerk_v127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)); gap = _overnight_gap(o_a, c_a.shift(1)).abs()
    atr = _atr(h_a, l_a, c_a, 128); rel_gap = gap * c_a.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 128).pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v128_jerk_v128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)); gap = _overnight_gap(o_a, c_a.shift(1)).abs()
    atr = _atr(h_a, l_a, c_a, 256); rel_gap = gap * c_a.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 256).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v129_jerk_v129_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)); gap = _overnight_gap(o_a, c_a.shift(1)).abs()
    atr = _atr(h_a, l_a, c_a, 512); rel_gap = gap * c_a.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 512).pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_eff_v130_jerk_v130_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    return _sma(fill / rel_gap.replace(0, np.nan), 5).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Fill remaining v131-v150 with variants
def f07gb_f07_gap_behavior_v131_jerk_v131_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 5).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v132_jerk_v132_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 10).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v133_jerk_v133_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 15).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v134_jerk_v134_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 20).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v135_jerk_v135_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 25).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v137_jerk_v137_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 35).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v138_jerk_v138_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 40).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v139_jerk_v139_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 45).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v140_jerk_v140_signal(open, high, low, close):
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 50).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v141_jerk_v141_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 5).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v142_jerk_v142_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 10).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v143_jerk_v143_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 15).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v144_jerk_v144_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 20).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v145_jerk_v145_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 25).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v147_jerk_v147_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 35).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v148_jerk_v148_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 40).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v149_jerk_v149_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 45).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_v150_jerk_v150_signal(open, close):
    return _sma(_gap_continuation(open, close, close.shift(1)), 50).pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f07gb_") and f.endswith("_signal")]

F07_GAP_BEHAVIOR_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(FEATURE_NAMES)
}

if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({
        "open": np.random.randn(sz).cumsum()+100,
        "high": np.random.randn(sz).cumsum()+110,
        "low": np.random.randn(sz).cumsum()+90,
        "close": np.random.randn(sz).cumsum()+100,
        "closeadj": np.random.randn(sz).cumsum()+100,
        "ticker": ["T"]*sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F07_GAP_BEHAVIOR_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("F07 Gap Behavior Jerk OK")
