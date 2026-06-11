# f07_gap_behavior_slope_001_150_gemini.py
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

# Slope Features v001-v150

# v001-v030: Overnight gap variations
def f07gb_f07_gap_behavior_overnight_gap_5d_roc5_slope_v001_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1))
    res = _sma(val, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_10d_roc5_slope_v002_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1))
    res = _sma(val, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_21d_roc5_slope_v003_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1))
    res = _sma(val, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_63d_roc21_slope_v004_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    val = _overnight_gap(o_a, c_a.shift(1))
    res = _sma(val, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_126d_roc21_slope_v005_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    val = _overnight_gap(o_a, c_a.shift(1))
    res = _sma(val, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_252d_roc63_slope_v006_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    val = _overnight_gap(o_a, c_a.shift(1))
    res = _sma(val, 252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_504d_roc63_slope_v007_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    val = _overnight_gap(o_a, c_a.shift(1))
    res = _sma(val, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_zscore_21d_roc5_slope_v008_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    z = (gap - _sma(gap, 21)) / gap.rolling(21, min_periods=5).std().replace(0, np.nan)
    res = _sma(z, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_zscore_63d_roc21_slope_v009_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    gap = _overnight_gap(o_a, c_a.shift(1))
    z = (gap - _sma(gap, 63)) / gap.rolling(63, min_periods=5).std().replace(0, np.nan)
    res = _sma(z, 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_max_21d_roc5_slope_v010_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    val = gap.rolling(21).max()
    res = val.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# v011-v030 (Continuing overnight gap variants)
def f07gb_f07_gap_behavior_overnight_gap_atr_ratio_5d_slope_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 5)
    res = (gap * close.shift(1) / atr.replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_atr_ratio_21d_slope_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 21)
    res = (gap * close.shift(1) / atr.replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_atr_ratio_63d_slope_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    gap = _overnight_gap(o_a, c_a.shift(1)); atr = _atr(h_a, l_a, c_a, 63)
    res = (gap * c_a.shift(1) / atr.replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_ema_5d_slope_v014_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_overnight_gap(open, close.shift(1)), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_ema_21d_slope_v015_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_overnight_gap(open, close.shift(1)), 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_ema_63d_slope_v016_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _ema(_overnight_gap(o_a, c_a.shift(1)), 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_size_abs_pct_5d_slope_v017_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1)).abs()
    res = _sma(val, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_size_abs_pct_21d_slope_v018_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1)).abs()
    res = _sma(val, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_size_abs_pct_63d_slope_v019_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    val = _overnight_gap(o_a, c_a.shift(1)).abs()
    res = _sma(val, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_persistence_10d_slope_v020_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); same_dir = (gap * gap.shift(1) > 0).astype(float)
    res = _sma(same_dir, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_dir_count_21d_slope_v021_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1); dir = (gap > 0).astype(float) - (gap < 0).astype(float)
    res = _sma(dir, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_dir_count_63d_slope_v022_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    gap = o_a - c_a.shift(1); dir = (gap > 0).astype(float) - (gap < 0).astype(float)
    res = _sma(dir, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_up_gap_prob_21d_slope_v023_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    up_gap = (open > close.shift(1)).astype(float)
    res = _sma(up_gap, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_dn_gap_prob_21d_slope_v024_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    dn_gap = (open < close.shift(1)).astype(float)
    res = _sma(dn_gap, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_large_gap_count_21d_slope_v025_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs(); atr = _atr(high, low, close, 21)
    large = (gap * close.shift(1) > atr).astype(float)
    res = _sma(large, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_skew_21d_slope_v026_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1)).rolling(21).skew()
    res = val.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_kurt_21d_slope_v027_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    val = _overnight_gap(open, close.shift(1)).rolling(21).kurt()
    res = val.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_std_norm_21d_slope_v028_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)) * close.shift(1)
    val = gap.rolling(21).std() / _atr(high, low, close, 21).replace(0, np.nan)
    res = val.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_ema_126d_slope_v029_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _ema(_overnight_gap(o_a, c_a.shift(1)), 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_overnight_gap_ema_252d_slope_v030_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _ema(_overnight_gap(o_a, c_a.shift(1)), 252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# v031-v060: Gap fill ratio variations
def f07gb_f07_gap_behavior_gap_fill_ratio_5d_slope_v031_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_21d_slope_v032_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_63d_slope_v033_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1))
    res = _sma(fill, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_126d_slope_v034_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1))
    res = _sma(fill, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_252d_slope_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1))
    res = _sma(fill, 252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_prob_21d_slope_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); prob = (fill >= 1.0).astype(float)
    res = _sma(prob, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_prob_63d_slope_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)); prob = (fill >= 1.0).astype(float)
    res = _sma(prob, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_ema_5d_slope_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _ema(fill, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_ema_21d_slope_v039_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _ema(fill, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_ema_63d_slope_v040_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1))
    res = _ema(fill, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_max_21d_slope_v041_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = fill.rolling(21).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_min_21d_slope_v042_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = fill.rolling(21).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_std_21d_slope_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = fill.rolling(21).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_zscore_21d_slope_v044_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    z = (fill - _sma(fill, 21)) / fill.rolling(21, min_periods=5).std().replace(0, np.nan)
    res = _sma(z, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_efficiency_5d_slope_v045_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = _sma(fill / rel_gap.replace(0, np.nan), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_efficiency_21d_slope_v046_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = _sma(fill / rel_gap.replace(0, np.nan), 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_efficiency_63d_slope_v047_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)); gap = _overnight_gap(o_a, c_a.shift(1)).abs()
    atr = _atr(h_a, l_a, c_a, 63); rel_gap = gap * c_a.shift(1) / atr.replace(0, np.nan)
    res = _sma(fill / rel_gap.replace(0, np.nan), 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_trend_21d_slope_v048_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1)); trend = _sma(fill, 5) - _sma(fill, 21)
    res = trend.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_exhaustion_gap_idx_21d_slope_v049_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs(); atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan); fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(rel_gap * fill, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_fill_ratio_sma_norm_63d_slope_v050_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    fill = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1))
    res = (_sma(fill, 63) / _sma(fill, 252).replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# v051-v080: Gap continuation variations
def f07gb_f07_gap_behavior_gap_continuation_5d_slope_v051_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_21d_slope_v052_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_63d_slope_v053_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    cont = _gap_continuation(o_a, c_a, c_a.shift(1))
    res = _sma(cont, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_126d_slope_v054_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    cont = _gap_continuation(o_a, c_a, c_a.shift(1))
    res = _sma(cont, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_252d_slope_v055_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    cont = _gap_continuation(o_a, c_a, c_a.shift(1))
    res = _sma(cont, 252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_and_go_strength_5d_slope_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 5)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan); cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(rel_gap * cont, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_and_go_strength_21d_slope_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan); cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(rel_gap * cont, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_and_go_strength_63d_slope_v058_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    gap = _overnight_gap(o_a, c_a.shift(1)); atr = _atr(h_a, l_a, c_a, 63)
    rel_gap = gap * c_a.shift(1) / atr.replace(0, np.nan); cont = _gap_continuation(o_a, c_a, c_a.shift(1))
    res = _sma(rel_gap * cont, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_ema_5d_slope_v059_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_gap_continuation(open, close, close.shift(1)), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_ema_21d_slope_v060_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_gap_continuation(open, close, close.shift(1)), 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_ema_63d_slope_v061_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    res = _ema(_gap_continuation(o_a, c_a, c_a.shift(1)), 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_max_21d_slope_v062_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_continuation(open, close, close.shift(1)).rolling(21).max().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_min_21d_slope_v063_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_continuation(open, close, close.shift(1)).rolling(21).min().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_continuation_std_21d_slope_v064_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_continuation(open, close, close.shift(1)).rolling(21).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_breakaway_gap_idx_21d_slope_v065_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs(); atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan); cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(rel_gap * cont, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_cont_efficiency_5d_slope_v066_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = _sma(cont / rel_gap.replace(0, np.nan), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_cont_efficiency_21d_slope_v067_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1)); gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21); rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = _sma(cont / rel_gap.replace(0, np.nan), 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_cont_efficiency_63d_slope_v068_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    cont = _gap_continuation(o_a, c_a, c_a.shift(1)); gap = _overnight_gap(o_a, c_a.shift(1)).abs()
    atr = _atr(h_a, l_a, c_a, 63); rel_gap = gap * c_a.shift(1) / atr.replace(0, np.nan)
    res = _sma(cont / rel_gap.replace(0, np.nan), 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_cont_trend_21d_slope_v069_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1)); trend = _sma(cont, 5) - _sma(cont, 21)
    res = trend.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_cont_sma_norm_63d_slope_v070_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    cont = _gap_continuation(o_a, c_a, c_a.shift(1))
    res = (_sma(cont, 63) / _sma(cont, 252).replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# v071-v100: Complex combinations and spreads
def f07gb_f07_gap_behavior_fill_cont_spread_5d_slope_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spread = _gap_fill_ratio(open, high, low, close.shift(1)) - _gap_continuation(open, close, close.shift(1))
    res = _sma(spread, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_fill_cont_spread_21d_slope_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    spread = _gap_fill_ratio(open, high, low, close.shift(1)) - _gap_continuation(open, close, close.shift(1))
    res = _sma(spread, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_fill_cont_spread_63d_slope_v073_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    spread = _gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)) - _gap_continuation(o_a, c_a, c_a.shift(1))
    res = _sma(spread, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_rel_bb_width_21d_slope_v074_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs(); bb_width = 4 * close.rolling(21).std().replace(0, np.nan)
    res = _sma(gap / bb_width, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_rel_bb_width_63d_slope_v075_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    gap = (o_a - c_a.shift(1)).abs(); bb_width = 4 * c_a.rolling(63).std().replace(0, np.nan)
    res = _sma(gap / bb_width, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_reversal_prob_norm_63d_slope_v076_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    rev = ((o_a - c_a.shift(1)) * (c_a - o_a) < 0).astype(float)
    res = (_sma(rev, 63) / _sma(rev, 252).replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_vol_rel_day_21d_slope_v077_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); day_ret = (close - open) / open.replace(0, np.nan)
    vol_ratio = gap.rolling(21).std() / day_ret.rolling(21).std().replace(0, np.nan)
    res = vol_ratio.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_vol_rel_day_63d_slope_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    gap = _overnight_gap(o_a, c_a.shift(1)); day_ret = (c_a - o_a) / o_a.replace(0, np.nan)
    vol_ratio = gap.rolling(63).std() / day_ret.rolling(63).std().replace(0, np.nan)
    res = vol_ratio.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_skew_diff_21d_slope_v079_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); day_ret = (close - open) / open.replace(0, np.nan)
    skew_diff = gap.rolling(21).skew() - day_ret.rolling(21).skew()
    res = skew_diff.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07gb_f07_gap_behavior_gap_kurt_diff_21d_slope_v080_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)); day_ret = (close - open) / open.replace(0, np.nan)
    kurt_diff = gap.rolling(21).kurt() - day_ret.rolling(21).kurt()
    res = kurt_diff.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# v081-v110: More systematic variations of overnight gaps
def f07gb_f07_gap_behavior_gap_v081_slope_v081_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 2).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v082_slope_v082_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 4).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v083_slope_v083_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 6).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v084_slope_v084_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 12).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v085_slope_v085_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 18).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v086_slope_v086_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 24).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v087_slope_v087_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 30).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v088_slope_v088_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 36).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v089_slope_v089_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 42).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v090_slope_v090_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 48).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v091_slope_v091_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 54).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v092_slope_v092_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_overnight_gap(open, close.shift(1)), 60).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v093_slope_v093_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 72).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v094_slope_v094_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 84).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v095_slope_v095_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 96).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v096_slope_v096_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 108).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v097_slope_v097_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 120).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v098_slope_v098_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 132).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v099_slope_v099_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 144).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v100_slope_v100_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 156).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v101_slope_v101_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 168).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v102_slope_v102_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 180).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v103_slope_v103_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 192).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v104_slope_v104_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 204).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v105_slope_v105_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 216).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v106_slope_v106_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 228).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v107_slope_v107_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 240).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v108_slope_v108_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 264).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v109_slope_v109_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 288).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_gap_v110_slope_v110_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, c_a = open * adj, closeadj
    return _sma(_overnight_gap(o_a, c_a.shift(1)), 312).pct_change(63).replace([np.inf, -np.inf], np.nan)

# v111-v140: Variations of gap fill ratio
def f07gb_f07_gap_behavior_fill_v111_slope_v111_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 2).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v112_slope_v112_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 4).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v113_slope_v113_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 6).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v114_slope_v114_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 12).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v115_slope_v115_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 18).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v116_slope_v116_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 24).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v117_slope_v117_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 30).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v118_slope_v118_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 36).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v119_slope_v119_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 42).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v120_slope_v120_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 48).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v121_slope_v121_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 54).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v122_slope_v122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_fill_ratio(open, high, low, close.shift(1)), 60).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v123_slope_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 72).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v124_slope_v124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 84).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v125_slope_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 96).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v126_slope_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 108).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v127_slope_v127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 120).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v128_slope_v128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 132).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v129_slope_v129_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 144).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v130_slope_v130_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 156).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v131_slope_v131_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 168).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v132_slope_v132_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 180).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v133_slope_v133_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 192).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v134_slope_v134_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 204).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v135_slope_v135_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 216).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v136_slope_v136_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 228).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v137_slope_v137_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 240).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v138_slope_v138_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 264).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v139_slope_v139_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 288).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_fill_v140_slope_v140_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan); o_a, h_a, l_a, c_a = open * adj, high * adj, low * adj, closeadj
    return _sma(_gap_fill_ratio(o_a, h_a, l_a, c_a.shift(1)), 312).pct_change(63).replace([np.inf, -np.inf], np.nan)

# v141-v150: Variations of gap continuation
def f07gb_f07_gap_behavior_cont_v141_slope_v141_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 2).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v142_slope_v142_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 4).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v143_slope_v143_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 6).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v144_slope_v144_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 12).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v145_slope_v145_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 18).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v146_slope_v146_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 24).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v147_slope_v147_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 30).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v148_slope_v148_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 36).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v149_slope_v149_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 42).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f07gb_f07_gap_behavior_cont_v150_slope_v150_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    return _sma(_gap_continuation(open, close, close.shift(1)), 48).pct_change(5).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f07gb_") and f.endswith("_signal")]

F07_GAP_BEHAVIOR_SLOPE_REGISTRY_001_150 = {
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
    for n, c in F07_GAP_BEHAVIOR_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("F07 Gap Behavior Slope OK")
