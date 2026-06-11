# f07_gap_behavior_base_001_075_gemini.py
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
    """Calculates the overnight gap relative to the previous close."""
    return (o - c_prev) / c_prev.abs().replace(0, np.nan)

def _gap_fill_ratio(o, h, l, c_prev):
    """Calculates the ratio of the gap that was filled during the day."""
    gap = o - c_prev
    is_up = (gap > 0).astype(float)
    is_down = (gap < 0).astype(float)
    fill_up = (o - l).clip(lower=0) / gap.abs().replace(0, np.nan)
    fill_down = (h - o).clip(lower=0) / gap.abs().replace(0, np.nan)
    return is_up * fill_up + is_down * fill_down

def _gap_continuation(o, c, c_prev):
    """Calculates the move after the gap relative to the gap size."""
    gap = o - c_prev
    move = c - o
    return move / gap.abs().replace(0, np.nan)

# Feature v001: Overnight gap relative to 5-day ATR
def f07gb_f07_gap_behavior_overnight_gap_atr_5d_v001_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    atr = _atr(high, low, close, 5)
    res = gap * close.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v002: Overnight gap relative to 10-day ATR
def f07gb_f07_gap_behavior_overnight_gap_atr_10d_v002_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    atr = _atr(high, low, close, 10)
    res = gap * close.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v003: Overnight gap relative to 21-day ATR
def f07gb_f07_gap_behavior_overnight_gap_atr_21d_v003_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    atr = _atr(high, low, close, 21)
    res = gap * close.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v004: Overnight gap relative to 63-day ATR using adjusted prices
def f07gb_f07_gap_behavior_overnight_gap_atr_63d_v004_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    atr = _atr(high_adj, low_adj, closeadj, 63)
    res = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v005: Overnight gap relative to 126-day ATR using adjusted prices
def f07gb_f07_gap_behavior_overnight_gap_atr_126d_v005_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    atr = _atr(high_adj, low_adj, closeadj, 126)
    res = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v006: Overnight gap relative to 252-day ATR using adjusted prices
def f07gb_f07_gap_behavior_overnight_gap_atr_252d_v006_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    atr = _atr(high_adj, low_adj, closeadj, 252)
    res = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v007: Gap fill ratio for 1-day window
def f07gb_f07_gap_behavior_gap_fill_ratio_1d_v007_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_fill_ratio(open, high, low, close.shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v008: Gap fill ratio rolling mean over 5 days
def f07gb_f07_gap_behavior_gap_fill_ratio_sma_5d_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v009: Gap fill ratio rolling mean over 10 days
def f07gb_f07_gap_behavior_gap_fill_ratio_sma_10d_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v010: Gap fill ratio rolling mean over 21 days
def f07gb_f07_gap_behavior_gap_fill_ratio_sma_21d_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v011: Gap continuation for 1-day window
def f07gb_f07_gap_behavior_gap_continuation_1d_v011_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _gap_continuation(open, close, close.shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v012: Gap continuation rolling mean over 5 days
def f07gb_f07_gap_behavior_gap_continuation_sma_5d_v012_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v013: Gap continuation rolling mean over 10 days
def f07gb_f07_gap_behavior_gap_continuation_sma_10d_v013_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v014: Gap continuation rolling mean over 21 days
def f07gb_f07_gap_behavior_gap_continuation_sma_21d_v014_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v015: Overnight gap z-score over 21 days
def f07gb_f07_gap_behavior_overnight_gap_zscore_21d_v015_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = (gap - _sma(gap, 21)) / gap.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v016: Overnight gap z-score over 63 days using adjusted prices
def f07gb_f07_gap_behavior_overnight_gap_zscore_63d_v016_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = (gap - _sma(gap, 63)) / gap.rolling(63, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v017: Exhaustion gap indicator (large gap with high fill ratio)
def f07gb_f07_gap_behavior_exhaustion_gap_idx_5d_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = (rel_gap > 2.0).astype(float) * fill
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v018: Breakaway gap indicator (large gap with high continuation)
def f07gb_f07_gap_behavior_breakaway_gap_idx_5d_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    cont = _gap_continuation(open, close, close.shift(1))
    res = (rel_gap > 2.0).astype(float) * cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v019: Gap persistence - probability of gap in same direction as yesterday
def f07gb_f07_gap_behavior_gap_persistence_5d_v019_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    same_dir = (gap * gap.shift(1) > 0).astype(float)
    res = _sma(same_dir, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v020: Gap persistence - probability of gap in same direction as yesterday over 21 days
def f07gb_f07_gap_behavior_gap_persistence_21d_v020_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    same_dir = (gap * gap.shift(1) > 0).astype(float)
    res = _sma(same_dir, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v021: Gap size relative to previous day's range
def f07gb_f07_gap_behavior_gap_rel_range_1d_v021_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_abs = (open - close.shift(1)).abs()
    prev_range = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    res = gap_abs / prev_range
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v022: Rolling mean of gap size relative to range over 5 days
def f07gb_f07_gap_behavior_gap_rel_range_sma_5d_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_abs = (open - close.shift(1)).abs()
    prev_range = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    rel_gap = gap_abs / prev_range
    res = _sma(rel_gap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v023: Gap-and-go strength (continuation * gap size relative to ATR)
def f07gb_f07_gap_behavior_gap_and_go_strength_5d_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    atr = _atr(high, low, close, 5)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    cont = _gap_continuation(open, close, close.shift(1))
    res = rel_gap * cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v024: Gap-and-go strength over 21 days
def f07gb_f07_gap_behavior_gap_and_go_strength_21d_v024_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    cont = _gap_continuation(open, close, close.shift(1))
    res = rel_gap * cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v025: Probability of gap being filled within the day (rolling 21d)
def f07gb_f07_gap_behavior_gap_fill_prob_21d_v025_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    is_filled = (fill >= 1.0).astype(float)
    res = _sma(is_filled, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v026: Probability of gap being filled within the day (rolling 63d)
def f07gb_f07_gap_behavior_gap_fill_prob_63d_v026_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    is_filled = (fill >= 1.0).astype(float)
    res = _sma(is_filled, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v027: Multi-day gap persistence (3-day cumulative gap)
def f07gb_f07_gap_behavior_gap_persistence_3d_cum_v027_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(3).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v028: Multi-day gap persistence (5-day cumulative gap)
def f07gb_f07_gap_behavior_gap_persistence_5d_cum_v028_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v029: Gap size relative to typical gap size (rolling 21d)
def f07gb_f07_gap_behavior_gap_size_rel_norm_21d_v029_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    res = gap / _sma(gap, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v030: Gap size relative to typical gap size (rolling 63d)
def f07gb_f07_gap_behavior_gap_size_rel_norm_63d_v030_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    res = gap / _sma(gap, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v031: Gap continuation z-score over 21 days
def f07gb_f07_gap_behavior_gap_continuation_zscore_21d_v031_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = (cont - _sma(cont, 21)) / cont.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v032: Gap fill ratio z-score over 21 days
def f07gb_f07_gap_behavior_gap_fill_ratio_zscore_21d_v032_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = (fill - _sma(fill, 21)) / fill.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v033: Gap reversal probability (gap up but close down or vice versa)
def f07gb_f07_gap_behavior_gap_reversal_prob_21d_v033_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    day_move = close - open
    reversal = (gap * day_move < 0).astype(float)
    res = _sma(reversal, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v034: Gap reversal probability over 63 days
def f07gb_f07_gap_behavior_gap_reversal_prob_63d_v034_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    day_move = close - open
    reversal = (gap * day_move < 0).astype(float)
    res = _sma(reversal, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v035: Gap size asymmetry (up gaps vs down gaps frequency 21d)
def f07gb_f07_gap_behavior_gap_asymmetry_freq_21d_v035_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    up_gap = (gap > 0).astype(float)
    dn_gap = (gap < 0).astype(float)
    res = (_sma(up_gap, 21) - _sma(dn_gap, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v036: Gap size asymmetry (up gaps vs down gaps magnitude 21d)
def f07gb_f07_gap_behavior_gap_asymmetry_mag_21d_v036_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    up_mag = gap.clip(lower=0)
    dn_mag = gap.clip(upper=0).abs()
    res = (_sma(up_mag, 21) - _sma(dn_mag, 21)) / (_sma(up_mag, 21) + _sma(dn_mag, 21)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v037: Overnight gap volatility relative to daytime volatility (21d)
def f07gb_f07_gap_behavior_gap_vol_rel_day_21d_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    day_ret = (close - open) / open.replace(0, np.nan)
    res = gap.rolling(21).std() / day_ret.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v038: Gap fill efficiency (fill ratio per unit of gap size relative to ATR)
def f07gb_f07_gap_behavior_gap_fill_efficiency_5d_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = fill / rel_gap.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v039: Gap continuation efficiency
def f07gb_f07_gap_behavior_gap_cont_efficiency_5d_v039_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 5)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = cont / rel_gap.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v040: Large gap count over 21 days (>1 ATR)
def f07gb_f07_gap_behavior_large_gap_count_21d_v040_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    is_large = (gap * close.shift(1) > atr).astype(float)
    res = is_large.rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v041: Gap direction vs 21-day trend
def f07gb_f07_gap_behavior_gap_vs_trend_21d_v041_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    trend = close.shift(1) - _sma(close, 21).shift(1)
    res = (gap * trend > 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v042: Gap direction vs 63-day trend
def f07gb_f07_gap_behavior_gap_vs_trend_63d_v042_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = open_adj - closeadj.shift(1)
    trend = closeadj.shift(1) - _sma(closeadj, 63).shift(1)
    res = (gap * trend > 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v043: Gap fill trend (sma5 of fill ratio minus sma21)
def f07gb_f07_gap_behavior_gap_fill_trend_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 5) - _sma(fill, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v044: Gap continuation trend
def f07gb_f07_gap_behavior_gap_cont_trend_v044_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 5) - _sma(cont, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v045: Normalized gap volatility (std of gaps / atr)
def f07gb_f07_gap_behavior_gap_vol_norm_21d_v045_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)) * close.shift(1)
    gap_std = gap.rolling(21).std()
    atr = _atr(high, low, close, 21)
    res = gap_std / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v046: Overnight gap relative to 504-day ATR using adjusted prices
def f07gb_f07_gap_behavior_overnight_gap_atr_504d_v046_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    atr = _atr(high_adj, low_adj, closeadj, 504)
    res = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v047: Gap fill ratio rolling mean over 63 days
def f07gb_f07_gap_behavior_gap_fill_ratio_sma_63d_v047_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = _sma(fill, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v048: Gap continuation rolling mean over 63 days
def f07gb_f07_gap_behavior_gap_continuation_sma_63d_v048_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(cont, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v049: Gap size relative to previous close (percent)
def f07gb_f07_gap_behavior_overnight_gap_pct_v049_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _overnight_gap(open, close.shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v050: Gap size relative to previous day's close (abs percent)
def f07gb_f07_gap_behavior_overnight_gap_abs_pct_v050_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    res = _overnight_gap(open, close.shift(1)).abs()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v051: Rolling max gap over 21 days
def f07gb_f07_gap_behavior_overnight_gap_max_21d_v051_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v052: Rolling min gap over 21 days
def f07gb_f07_gap_behavior_overnight_gap_min_21d_v052_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v053: Gap fill ratio z-score over 63 days
def f07gb_f07_gap_behavior_gap_fill_ratio_zscore_63d_v053_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = (fill - _sma(fill, 63)) / fill.rolling(63, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v054: Gap continuation z-score over 63 days
def f07gb_f07_gap_behavior_gap_continuation_zscore_63d_v054_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = (cont - _sma(cont, 63)) / cont.rolling(63, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v055: Gap size relative to range (rolling 21d mean)
def f07gb_f07_gap_behavior_gap_rel_range_sma_21d_v055_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_abs = (open - close.shift(1)).abs()
    prev_range = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    rel_gap = gap_abs / prev_range
    res = _sma(rel_gap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v056: Gap-and-go strength over 63 days
def f07gb_f07_gap_behavior_gap_and_go_strength_63d_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    atr = _atr(high_adj, low_adj, closeadj, 63)
    rel_gap = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    cont = _gap_continuation(open_adj, closeadj, closeadj.shift(1))
    res = rel_gap * cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v057: Exhaustion gap indicator 21d
def f07gb_f07_gap_behavior_exhaustion_gap_idx_21d_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = (rel_gap > 1.5).astype(float) * fill
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v058: Breakaway gap indicator 21d
def f07gb_f07_gap_behavior_breakaway_gap_idx_21d_v058_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    cont = _gap_continuation(open, close, close.shift(1))
    res = (rel_gap > 1.5).astype(float) * cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v059: Gap direction persistence count (3 days)
def f07gb_f07_gap_behavior_gap_dir_persistence_3d_v059_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    is_up = (gap > 0).astype(float)
    is_dn = (gap < 0).astype(float)
    res = is_up.rolling(3).sum() - is_dn.rolling(3).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v060: Gap direction persistence count (5 days)
def f07gb_f07_gap_behavior_gap_dir_persistence_5d_v060_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    is_up = (gap > 0).astype(float)
    is_dn = (gap < 0).astype(float)
    res = is_up.rolling(5).sum() - is_dn.rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v061: Overnight gap vs ATR ratio (rolling 21d max)
def f07gb_f07_gap_behavior_overnight_gap_atr_max_21d_v061_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = rel_gap.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v062: Overnight gap vs ATR ratio (rolling 21d min)
def f07gb_f07_gap_behavior_overnight_gap_atr_min_21d_v062_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = rel_gap.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v063: Gap fill efficiency z-score 21d
def f07gb_f07_gap_behavior_gap_fill_eff_zscore_21d_v063_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    eff = fill / rel_gap.replace(0, np.nan)
    res = (eff - _sma(eff, 21)) / eff.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v064: Gap continuation efficiency z-score 21d
def f07gb_f07_gap_behavior_gap_cont_eff_zscore_21d_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    eff = cont / rel_gap.replace(0, np.nan)
    res = (eff - _sma(eff, 21)) / eff.rolling(21, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v065: Probability of up gap (rolling 21d)
def f07gb_f07_gap_behavior_up_gap_prob_21d_v065_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    res = (gap > 0).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v066: Probability of down gap (rolling 21d)
def f07gb_f07_gap_behavior_dn_gap_prob_21d_v066_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    res = (gap < 0).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v067: Mean gap size when up (rolling 21d)
def f07gb_f07_gap_behavior_up_gap_size_avg_21d_v067_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.where(gap > 0).rolling(21, min_periods=1).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v068: Mean gap size when down (rolling 21d)
def f07gb_f07_gap_behavior_dn_gap_size_avg_21d_v068_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.where(gap < 0).rolling(21, min_periods=1).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v069: Gap size relative to 126-day rolling std of gaps
def f07gb_f07_gap_behavior_gap_rel_std_126d_v069_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = gap / gap.rolling(126, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v070: Gap fill probability given large gap (>1 ATR, 63d)
def f07gb_f07_gap_behavior_large_gap_fill_prob_63d_v070_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    large = gap * close.shift(1) > atr
    fill = _gap_fill_ratio(open, high, low, close.shift(1)) >= 1.0
    res = (large & fill).rolling(63).sum() / large.rolling(63).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v071: Gap continuation probability given large gap (>1 ATR, 63d)
def f07gb_f07_gap_behavior_large_gap_cont_prob_63d_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_val = _overnight_gap(open, close.shift(1))
    atr = _atr(high, low, close, 21)
    large = gap_val.abs() * close.shift(1) > atr
    cont = _gap_continuation(open, close, close.shift(1)) > 0.5
    res = (large & cont).rolling(63).sum() / large.rolling(63).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v072: Rolling 21-day skewness of overnight gaps
def f07gb_f07_gap_behavior_gap_skew_21d_v072_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v073: Rolling 63-day skewness of overnight gaps
def f07gb_f07_gap_behavior_gap_skew_63d_v073_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = gap.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v074: Rolling 21-day kurtosis of overnight gaps
def f07gb_f07_gap_behavior_gap_kurt_21d_v074_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v075: Rolling 63-day kurtosis of overnight gaps
def f07gb_f07_gap_behavior_gap_kurt_63d_v075_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = gap.rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f07gb_") and f.endswith("_signal")]

F07_GAP_BEHAVIOR_BASE_REGISTRY_001_075 = {
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
    for n, c in F07_GAP_BEHAVIOR_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("F07 Gap Behavior Base 001-075 OK")
