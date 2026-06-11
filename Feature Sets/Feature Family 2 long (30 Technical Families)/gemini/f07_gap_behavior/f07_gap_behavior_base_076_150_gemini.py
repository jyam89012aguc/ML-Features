# f07_gap_behavior_base_076_150_gemini.py
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

# Feature v076: Gap size relative to 21-day range of gaps
def f07gb_f07_gap_behavior_gap_size_rel_range_21d_v076_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = (gap - _min(gap, 21)) / (_max(gap, 21) - _min(gap, 21)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v077: Gap size relative to 63-day range of gaps
def f07gb_f07_gap_behavior_gap_size_rel_range_63d_v077_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = (gap - _min(gap, 63)) / (_max(gap, 63) - _min(gap, 63)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v078: Gap fill ratio minus gap continuation ratio (spread)
def f07gb_f07_gap_behavior_gap_fill_cont_spread_1d_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    cont = _gap_continuation(open, close, close.shift(1))
    res = fill - cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v079: Gap fill ratio minus gap continuation ratio rolling mean 21d
def f07gb_f07_gap_behavior_gap_fill_cont_spread_sma_21d_v079_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(fill - cont, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v080: Gap fill ratio minus gap continuation ratio rolling mean 63d
def f07gb_f07_gap_behavior_gap_fill_cont_spread_sma_63d_v080_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    cont = _gap_continuation(open, close, close.shift(1))
    res = _sma(fill - cont, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v081: Cumulative gap persistence (10-day sum of overnight gaps)
def f07gb_f07_gap_behavior_gap_persistence_10d_cum_v081_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(10).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v082: Cumulative gap persistence (21-day sum of overnight gaps)
def f07gb_f07_gap_behavior_gap_persistence_21d_cum_v082_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = gap.rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v083: Probability of consecutive gaps in same direction (3-day)
def f07gb_f07_gap_behavior_consecutive_gap_prob_3d_v083_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    streak = (gap * gap.shift(1) > 0).astype(float) * (gap.shift(1) * gap.shift(2) > 0).astype(float)
    res = _sma(streak, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v084: Gap size relative to 21-day Bollinger Band width
def f07gb_f07_gap_behavior_gap_rel_bb_width_21d_v084_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap_abs = (open - close.shift(1)).abs()
    bb_width = 4 * close.rolling(21).std().replace(0, np.nan)
    res = gap_abs / bb_width
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v085: Gap size relative to 63-day Bollinger Band width
def f07gb_f07_gap_behavior_gap_rel_bb_width_63d_v085_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap_abs = (open_adj - closeadj.shift(1)).abs()
    bb_width = 4 * closeadj.rolling(63).std().replace(0, np.nan)
    res = gap_abs / bb_width
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v086: Gap size relative to ATR (rolling 126d mean)
def f07gb_f07_gap_behavior_gap_atr_ratio_sma_126d_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    atr = _atr(high_adj, low_adj, closeadj, 126)
    rel_gap = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    res = _sma(rel_gap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v087: Gap size relative to ATR (rolling 252d mean)
def f07gb_f07_gap_behavior_gap_atr_ratio_sma_252d_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    atr = _atr(high_adj, low_adj, closeadj, 252)
    rel_gap = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    res = _sma(rel_gap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v088: Probability of gap up and go (rolling 21d)
def f07gb_f07_gap_behavior_up_gap_and_go_prob_21d_v088_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    move = close - open
    res = ((gap > 0) & (move > 0)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v089: Probability of gap down and go (rolling 21d)
def f07gb_f07_gap_behavior_dn_gap_and_go_prob_21d_v089_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    move = close - open
    res = ((gap < 0) & (move < 0)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v090: Probability of gap up and reverse (rolling 21d)
def f07gb_f07_gap_behavior_up_gap_and_rev_prob_21d_v090_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    move = close - open
    res = ((gap > 0) & (move < 0)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v091: Probability of gap down and reverse (rolling 21d)
def f07gb_f07_gap_behavior_dn_gap_and_rev_prob_21d_v091_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    move = close - open
    res = ((gap < 0) & (move > 0)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v092: Gap size skewness relative to daytime return skewness (21d)
def f07gb_f07_gap_behavior_gap_skew_rel_day_21d_v092_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    day_ret = (close - open) / open.replace(0, np.nan)
    res = gap.rolling(21).skew() - day_ret.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v093: Gap size kurtosis relative to daytime return kurtosis (21d)
def f07gb_f07_gap_behavior_gap_kurt_rel_day_21d_v093_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    day_ret = (close - open) / open.replace(0, np.nan)
    res = gap.rolling(21).kurt() - day_ret.rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v094: Overnight gap mean / std ratio (Sharpe-like, 21d)
def f07gb_f07_gap_behavior_gap_mean_std_ratio_21d_v094_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    res = _sma(gap, 21) / gap.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v095: Overnight gap mean / std ratio (Sharpe-like, 63d)
def f07gb_f07_gap_behavior_gap_mean_std_ratio_63d_v095_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = _sma(gap, 63) / gap.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v096: Gap fill ratio z-score over 126 days
def f07gb_f07_gap_behavior_gap_fill_ratio_zscore_126d_v096_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    fill = _gap_fill_ratio(open_adj, high_adj, low_adj, closeadj.shift(1))
    res = (fill - _sma(fill, 126)) / fill.rolling(126, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v097: Gap continuation z-score over 126 days
def f07gb_f07_gap_behavior_gap_continuation_zscore_126d_v097_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    cont = _gap_continuation(open_adj, closeadj, closeadj.shift(1))
    res = (cont - _sma(cont, 126)) / cont.rolling(126, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v098: Gap size relative to previous day's high-low range (21d sma)
def f07gb_f07_gap_behavior_gap_rel_prev_range_sma_21d_v098_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    prev_range = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    res = _sma(gap / prev_range, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v099: Gap size relative to previous day's high-low range (63d sma)
def f07gb_f07_gap_behavior_gap_rel_prev_range_sma_63d_v099_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = (open_adj - closeadj.shift(1)).abs()
    prev_range = (high_adj.shift(1) - low_adj.shift(1)).replace(0, np.nan)
    res = _sma(gap / prev_range, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v100: Gap fill probability given small gap (<0.5 ATR, 21d)
def f07gb_f07_gap_behavior_small_gap_fill_prob_21d_v100_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    small = gap * close.shift(1) < 0.5 * atr
    fill = _gap_fill_ratio(open, high, low, close.shift(1)) >= 1.0
    res = (small & fill).rolling(21).sum() / small.rolling(21).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v101: Gap size relative to 21-day average true range (max over 5d)
def f07gb_f07_gap_behavior_gap_atr_ratio_max_5d_v101_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = rel_gap.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v102: Gap size relative to 21-day average true range (min over 5d)
def f07gb_f07_gap_behavior_gap_atr_ratio_min_5d_v102_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    res = rel_gap.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v103: Probability of gap up after down day (rolling 21d)
def f07gb_f07_gap_behavior_up_gap_after_dn_day_prob_21d_v103_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap_up = (open > close.shift(1))
    dn_day = (close.shift(1) < open.shift(1))
    res = (gap_up & dn_day).rolling(21).mean() / dn_day.rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v104: Probability of down gap after up day (rolling 21d)
def f07gb_f07_gap_behavior_dn_gap_after_up_day_prob_21d_v104_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap_dn = (open < close.shift(1))
    up_day = (close.shift(1) > open.shift(1))
    res = (gap_dn & up_day).rolling(21).mean() / up_day.rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v105: Gap size relative to typical daytime return (rolling 21d)
def f07gb_f07_gap_behavior_gap_rel_day_ret_21d_v105_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    day_ret = (close - open) / open.replace(0, np.nan)
    res = gap / day_ret.abs().rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v106: Gap fill ratio rolling std over 21 days
def f07gb_f07_gap_behavior_gap_fill_ratio_std_21d_v106_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    res = fill.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v107: Gap continuation rolling std over 21 days
def f07gb_f07_gap_behavior_gap_continuation_std_21d_v107_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    res = cont.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v108: Gap size relative to 504-day range of gaps
def f07gb_f07_gap_behavior_gap_size_rel_range_504d_v108_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = (gap - _min(gap, 504)) / (_max(gap, 504) - _min(gap, 504)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v109: Overnight gap z-score over 252 days
def f07gb_f07_gap_behavior_overnight_gap_zscore_252d_v109_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = (gap - _sma(gap, 252)) / gap.rolling(252, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v110: Gap fill ratio z-score over 252 days
def f07gb_f07_gap_behavior_gap_fill_ratio_zscore_252d_v110_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    fill = _gap_fill_ratio(open_adj, high_adj, low_adj, closeadj.shift(1))
    res = (fill - _sma(fill, 252)) / fill.rolling(252, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v111: Gap continuation z-score over 252 days
def f07gb_f07_gap_behavior_gap_continuation_zscore_252d_v111_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    cont = _gap_continuation(open_adj, closeadj, closeadj.shift(1))
    res = (cont - _sma(cont, 252)) / cont.rolling(252, min_periods=5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v112: Exhaustion gap indicator 63d
def f07gb_f07_gap_behavior_exhaustion_gap_idx_63d_v112_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    atr = _atr(high_adj, low_adj, closeadj, 63)
    rel_gap = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    fill = _gap_fill_ratio(open_adj, high_adj, low_adj, closeadj.shift(1))
    res = (rel_gap > 1.2).astype(float) * fill
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v113: Breakaway gap indicator 63d
def f07gb_f07_gap_behavior_breakaway_gap_idx_63d_v113_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    atr = _atr(high_adj, low_adj, closeadj, 63)
    rel_gap = gap * closeadj.shift(1) / atr.replace(0, np.nan)
    cont = _gap_continuation(open_adj, closeadj, closeadj.shift(1))
    res = (rel_gap > 1.2).astype(float) * cont
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v114: Gap direction vs 126-day trend
def f07gb_f07_gap_behavior_gap_vs_trend_126d_v114_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = open_adj - closeadj.shift(1)
    trend = closeadj.shift(1) - _sma(closeadj, 126).shift(1)
    res = (gap * trend > 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v115: Gap direction vs 252-day trend
def f07gb_f07_gap_behavior_gap_vs_trend_252d_v115_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = open_adj - closeadj.shift(1)
    trend = closeadj.shift(1) - _sma(closeadj, 252).shift(1)
    res = (gap * trend > 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v116: Rolling 126-day skewness of overnight gaps
def f07gb_f07_gap_behavior_gap_skew_126d_v116_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = gap.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v117: Rolling 126-day kurtosis of overnight gaps
def f07gb_f07_gap_behavior_gap_kurt_126d_v117_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = gap.rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v118: Probability of gap up and go (rolling 63d)
def f07gb_f07_gap_behavior_up_gap_and_go_prob_63d_v118_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    move = close - open
    res = ((gap > 0) & (move > 0)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v119: Probability of gap down and go (rolling 63d)
def f07gb_f07_gap_behavior_dn_gap_and_go_prob_63d_v119_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    move = close - open
    res = ((gap < 0) & (move < 0)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v120: Gap size relative to previous close (rolling 21d max)
def f07gb_f07_gap_behavior_overnight_gap_pct_max_21d_v120_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    res = gap.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v121: Gap size relative to previous close (rolling 21d min)
def f07gb_f07_gap_behavior_overnight_gap_pct_min_21d_v121_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1)).abs()
    res = gap.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v122: Gap size relative to 21-day average daytime range
def f07gb_f07_gap_behavior_gap_rel_avg_day_range_21d_v122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    day_range = (high - low).rolling(21).mean().replace(0, np.nan)
    res = gap / day_range
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v123: Gap size relative to 63-day average daytime range
def f07gb_f07_gap_behavior_gap_rel_avg_day_range_63d_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = (open_adj - closeadj.shift(1)).abs()
    day_range = (high_adj - low_adj).rolling(63).mean().replace(0, np.nan)
    res = gap / day_range
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v124: Probability of gap fill within 2 days (rolling 21d)
def f07gb_f07_gap_behavior_gap_fill_2d_prob_21d_v124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_val = open - close.shift(1)
    is_up = gap_val > 0
    is_dn = gap_val < 0
    fill_up = low.rolling(2).min() <= close.shift(1)
    fill_dn = high.rolling(2).max() >= close.shift(1)
    res = ((is_up & fill_up) | (is_dn & fill_dn)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v125: Probability of gap fill within 5 days (rolling 21d)
def f07gb_f07_gap_behavior_gap_fill_5d_prob_21d_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_val = open - close.shift(1)
    is_up = gap_val > 0
    is_dn = gap_val < 0
    fill_up = low.rolling(5).min() <= close.shift(1)
    fill_dn = high.rolling(5).max() >= close.shift(1)
    res = ((is_up & fill_up) | (is_dn & fill_dn)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v126: Gap continuation efficiency rolling mean 21d
def f07gb_f07_gap_behavior_gap_cont_eff_sma_21d_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cont = _gap_continuation(open, close, close.shift(1))
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    eff = cont / rel_gap.replace(0, np.nan)
    res = _sma(eff, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v127: Gap fill efficiency rolling mean 21d
def f07gb_f07_gap_behavior_gap_fill_eff_sma_21d_v127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    gap = _overnight_gap(open, close.shift(1)).abs()
    atr = _atr(high, low, close, 21)
    rel_gap = gap * close.shift(1) / atr.replace(0, np.nan)
    eff = fill / rel_gap.replace(0, np.nan)
    res = _sma(eff, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v128: Gap size relative to typical daytime return (63d)
def f07gb_f07_gap_behavior_gap_rel_day_ret_63d_v128_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    day_ret = (closeadj - open_adj) / open_adj.replace(0, np.nan)
    res = gap / day_ret.abs().rolling(63).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v129: Gap size relative to typical daytime return (126d)
def f07gb_f07_gap_behavior_gap_rel_day_ret_126d_v129_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    day_ret = (closeadj - open_adj) / open_adj.replace(0, np.nan)
    res = gap / day_ret.abs().rolling(126).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v130: Gap direction vs 21-day EMA
def f07gb_f07_gap_behavior_gap_vs_ema_21d_v130_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = open - close.shift(1)
    trend = close.shift(1) - _ema(close, 21).shift(1)
    res = (gap * trend > 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v131: Gap direction vs 63-day EMA
def f07gb_f07_gap_behavior_gap_vs_ema_63d_v131_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = open_adj - closeadj.shift(1)
    trend = closeadj.shift(1) - _ema(closeadj, 63).shift(1)
    res = (gap * trend > 0).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v132: Gap size relative to previous day's ATR (21d)
def f07gb_f07_gap_behavior_gap_rel_prev_atr_21d_v132_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    atr = _atr(high, low, close, 21).shift(1).replace(0, np.nan)
    res = gap / atr
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v133: Gap size relative to previous day's ATR (63d)
def f07gb_f07_gap_behavior_gap_rel_prev_atr_63d_v133_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = (open_adj - closeadj.shift(1)).abs()
    atr = _atr(high_adj, low_adj, closeadj, 63).shift(1).replace(0, np.nan)
    res = gap / atr
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v134: Probability of gap fill if gap > 2% (21d)
def f07gb_f07_gap_behavior_large_gap_pct_fill_prob_21d_v134_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap_pct = _overnight_gap(open, close.shift(1)).abs()
    large = gap_pct > 0.02
    fill = _gap_fill_ratio(open, high, low, close.shift(1)) >= 1.0
    res = (large & fill).rolling(21).sum() / large.rolling(21).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v135: Probability of gap continuation if gap > 2% (21d)
def f07gb_f07_gap_behavior_large_gap_pct_cont_prob_21d_v135_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap_pct = _overnight_gap(open, close.shift(1))
    large = gap_pct.abs() > 0.02
    cont = _gap_continuation(open, close, close.shift(1)) > 0.5
    res = (large & cont).rolling(21).sum() / large.rolling(21).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v136: Rolling 21-day average gap size relative to open price
def f07gb_f07_gap_behavior_gap_rel_open_sma_21d_v136_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    res = _sma(gap / open.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v137: Rolling 63-day average gap size relative to open price
def f07gb_f07_gap_behavior_gap_rel_open_sma_63d_v137_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = (open_adj - closeadj.shift(1)).abs()
    res = _sma(gap / open_adj.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v138: Gap fill ratio rolling mean over 126 days
def f07gb_f07_gap_behavior_gap_fill_ratio_sma_126d_v138_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    fill = _gap_fill_ratio(open_adj, high_adj, low_adj, closeadj.shift(1))
    res = _sma(fill, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v139: Gap continuation rolling mean over 126 days
def f07gb_f07_gap_behavior_gap_continuation_sma_126d_v139_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    cont = _gap_continuation(open_adj, closeadj, closeadj.shift(1))
    res = _sma(cont, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v140: Gap size relative to previous day's volatility (std 21d)
def f07gb_f07_gap_behavior_gap_rel_prev_vol_21d_v140_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    vol = close.rolling(21).std().shift(1).replace(0, np.nan)
    res = gap / vol
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v141: Gap size relative to previous day's volatility (std 63d)
def f07gb_f07_gap_behavior_gap_rel_prev_vol_63d_v141_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = (open_adj - closeadj.shift(1)).abs()
    vol = closeadj.rolling(63).std().shift(1).replace(0, np.nan)
    res = gap / vol
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v142: Cumulative gap persistence (63-day sum of overnight gaps)
def f07gb_f07_gap_behavior_gap_persistence_63d_cum_v142_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1))
    res = gap.rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v143: Probability of gap up given up trend (21d)
def f07gb_f07_gap_behavior_up_gap_in_up_trend_prob_21d_v143_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    up_trend = close.shift(1) > _sma(close, 21).shift(1)
    up_gap = open > close.shift(1)
    res = (up_trend & up_gap).rolling(21).mean() / up_trend.rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v144: Probability of down gap given down trend (21d)
def f07gb_f07_gap_behavior_dn_gap_in_dn_trend_prob_21d_v144_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    dn_trend = close.shift(1) < _sma(close, 21).shift(1)
    dn_gap = open < close.shift(1)
    res = (dn_trend & dn_gap).rolling(21).mean() / dn_trend.rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v145: Gap size relative to 21-day max range
def f07gb_f07_gap_behavior_gap_rel_max_range_21d_v145_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    gap = (open - close.shift(1)).abs()
    max_range = (high - low).rolling(21).max().replace(0, np.nan)
    res = gap / max_range
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v146: Gap size relative to 63-day max range
def f07gb_f07_gap_behavior_gap_rel_max_range_63d_v146_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    high_adj = high * adj
    low_adj = low * adj
    gap = (open_adj - closeadj.shift(1)).abs()
    max_range = (high_adj - low_adj).rolling(63).max().replace(0, np.nan)
    res = gap / max_range
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v147: Gap fill ratio vs continuation ratio (rolling 21d max)
def f07gb_f07_gap_behavior_gap_fill_cont_spread_max_21d_v147_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    cont = _gap_continuation(open, close, close.shift(1))
    res = (fill - cont).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v148: Gap fill ratio vs continuation ratio (rolling 21d min)
def f07gb_f07_gap_behavior_gap_fill_cont_spread_min_21d_v148_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    fill = _gap_fill_ratio(open, high, low, close.shift(1))
    cont = _gap_continuation(open, close, close.shift(1))
    res = (fill - cont).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v149: Gap size relative to typical daytime return (252d)
def f07gb_f07_gap_behavior_gap_rel_day_ret_252d_v149_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    open_adj = open * adj
    gap = _overnight_gap(open_adj, closeadj.shift(1)).abs()
    day_ret = (closeadj - open_adj) / open_adj.replace(0, np.nan)
    res = gap / day_ret.abs().rolling(252).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature v150: Probability of consecutive gaps (5-day streak)
def f07gb_f07_gap_behavior_consecutive_gap_prob_5d_v150_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    gap = _overnight_gap(open, close.shift(1))
    streak = (gap * gap.shift(1) > 0).astype(float)
    for i in range(2, 5):
        streak *= (gap.shift(i-1) * gap.shift(i) > 0).astype(float)
    res = _sma(streak, 63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f07gb_") and f.endswith("_signal")]

F07_GAP_BEHAVIOR_BASE_REGISTRY_076_150 = {
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
    for n, c in F07_GAP_BEHAVIOR_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("F07 Gap Behavior Base 076-150 OK")
