# f04_support_resistance_proximity_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _support_dist(price, low, w):
    s = low.rolling(w, min_periods=min(w, 5)).min()
    return (price - s) / s.abs().replace(0, np.nan)

def _resistance_dist(price, high, w):
    r = high.rolling(w, min_periods=min(w, 5)).max()
    return (r - price) / r.abs().replace(0, np.nan)

def _pivot_pos(price, high, low, close):
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    return (price - p) / p.abs().replace(0, np.nan)

# Base Features 076-150

# 126-day Fib 61.8% retracement support distance
def f04sr_fib_618_support_126d_v076_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126, min_periods=5).max()
    l = (low * adj).rolling(126, min_periods=5).min()
    fib = l + (h - l) * 0.618
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Fib 61.8% retracement support distance
def f04sr_fib_618_support_252d_v077_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.618
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day psychological round 500 support
def f04sr_psych_500_support_252d_v078_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l252 = (low * adj).rolling(252).min()
    level = (l252 / 500).round() * 500
    res = (closeadj - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day psychological round 500 resistance
def f04sr_psych_500_resistance_252d_v079_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h252 = (high * adj).rolling(252).max()
    level = (h252 / 500).round() * 500
    res = (level - closeadj) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_504d_v080_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(504, min_periods=5).max()
    l = (low * adj).rolling(504, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504-day volume-weighted support distance
def f04sr_vw_support_504d_v081_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    vw_low = (l_adj * volume).rolling(504, min_periods=5).sum() / volume.rolling(504, min_periods=5).sum().replace(0, np.nan)
    res = (closeadj - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504-day volume-weighted resistance distance
def f04sr_vw_resistance_504d_v082_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    vw_high = (h_adj * volume).rolling(504, min_periods=5).sum() / volume.rolling(504, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - closeadj) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day Camarilla Pivot R3 distance
def f04sr_camarilla_r3_dist_10d_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h10 = high.shift(1).rolling(10).max()
    l10 = low.shift(1).rolling(10).min()
    c = close.shift(1)
    r3 = c + (h10 - l10) * 1.1 / 4.0
    res = (r3 - close) / r3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day Camarilla Pivot S3 distance
def f04sr_camarilla_s3_dist_10d_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h10 = high.shift(1).rolling(10).max()
    l10 = low.shift(1).rolling(10).min()
    c = close.shift(1)
    s3 = c - (h10 - l10) * 1.1 / 4.0
    res = (close - s3) / s3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Camarilla Pivot R3 distance
def f04sr_camarilla_r3_dist_21d_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h21 = high.shift(1).rolling(21).max()
    l21 = low.shift(1).rolling(21).min()
    c = close.shift(1)
    r3 = c + (h21 - l21) * 1.1 / 4.0
    res = (r3 - close) / r3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Camarilla Pivot S3 distance
def f04sr_camarilla_s3_dist_21d_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h21 = high.shift(1).rolling(21).max()
    l21 = low.shift(1).rolling(21).min()
    c = close.shift(1)
    s3 = c - (h21 - l21) * 1.1 / 4.0
    res = (close - s3) / s3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Woodie Pivot Position
def f04sr_woodie_pivot_pos_21d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    h21 = high.shift(1).rolling(21).max()
    l21 = low.shift(1).rolling(21).min()
    p = (h21 + l21 + 2 * close.shift(1)) / 4.0
    res = (close - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Woodie Pivot Position
def f04sr_woodie_pivot_pos_63d_v088_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h63 = (high * adj).shift(1).rolling(63).max()
    l63 = (low * adj).shift(1).rolling(63).min()
    p = (h63 + l63 + 2 * closeadj.shift(1)) / 4.0
    res = (closeadj - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Woodie Pivot Position
def f04sr_woodie_pivot_pos_126d_v089_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h126 = (high * adj).shift(1).rolling(126).max()
    l126 = (low * adj).shift(1).rolling(126).min()
    p = (h126 + l126 + 2 * closeadj.shift(1)) / 4.0
    res = (closeadj - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Woodie Pivot Position
def f04sr_woodie_pivot_pos_252d_v090_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h252 = (high * adj).shift(1).rolling(252).max()
    l252 = (low * adj).shift(1).rolling(252).min()
    p = (h252 + l252 + 2 * closeadj.shift(1)) / 4.0
    res = (closeadj - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day deMark Pivot R1 distance
def f04sr_demark_r1_dist_63d_v091_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h63 = (high * adj).shift(1).rolling(63).max()
    l63 = (low * adj).shift(1).rolling(63).min()
    c = closeadj.shift(1)
    o = closeadj.shift(2)
    x = pd.Series(0.0, index=close.index)
    x[c < o] = h63 + 2*l63 + c
    x[c > o] = 2*h63 + l63 + c
    x[c == o] = h63 + l63 + 2*c
    r1 = x / 2.0 - l63
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day deMark Pivot R1 distance
def f04sr_demark_r1_dist_126d_v092_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h126 = (high * adj).shift(1).rolling(126).max()
    l126 = (low * adj).shift(1).rolling(126).min()
    c = closeadj.shift(1)
    o = closeadj.shift(2)
    x = pd.Series(0.0, index=close.index)
    x[c < o] = h126 + 2*l126 + c
    x[c > o] = 2*h126 + l126 + c
    x[c == o] = h126 + l126 + 2*c
    r1 = x / 2.0 - l126
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day deMark Pivot R1 distance
def f04sr_demark_r1_dist_252d_v093_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h252 = (high * adj).shift(1).rolling(252).max()
    l252 = (low * adj).shift(1).rolling(252).min()
    c = closeadj.shift(1)
    o = closeadj.shift(2)
    x = pd.Series(0.0, index=close.index)
    x[c < o] = h252 + 2*l252 + c
    x[c > o] = 2*h252 + l252 + c
    x[c == o] = h252 + l252 + 2*c
    r1 = x / 2.0 - l252
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day support distance using close

# 30-day support distance using close
def f04sr_support_dist_30d_v095_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# 40-day support distance using close
def f04sr_support_dist_40d_v096_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 40)
    return res.replace([np.inf, -np.inf], np.nan)

# 50-day support distance using close
def f04sr_support_dist_50d_v097_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# 60-day support distance using close
def f04sr_support_dist_60d_v098_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 60)
    return res.replace([np.inf, -np.inf], np.nan)

# 70-day support distance using close
def f04sr_support_dist_70d_v099_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 70)
    return res.replace([np.inf, -np.inf], np.nan)

# 80-day support distance using close
def f04sr_support_dist_80d_v100_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 80)
    return res.replace([np.inf, -np.inf], np.nan)

# 90-day support distance using close
def f04sr_support_dist_90d_v101_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# 100-day support distance using close
def f04sr_support_dist_100d_v102_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 100)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day resistance distance using close

# 30-day resistance distance using close
def f04sr_resistance_dist_30d_v104_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# 40-day resistance distance using close
def f04sr_resistance_dist_40d_v105_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 40)
    return res.replace([np.inf, -np.inf], np.nan)

# 50-day resistance distance using close
def f04sr_resistance_dist_50d_v106_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# 60-day resistance distance using close
def f04sr_resistance_dist_60d_v107_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 60)
    return res.replace([np.inf, -np.inf], np.nan)

# 70-day resistance distance using close
def f04sr_resistance_dist_70d_v108_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 70)
    return res.replace([np.inf, -np.inf], np.nan)

# 80-day resistance distance using close
def f04sr_resistance_dist_80d_v109_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 80)
    return res.replace([np.inf, -np.inf], np.nan)

# 90-day resistance distance using close
def f04sr_resistance_dist_90d_v110_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# 100-day resistance distance using close
def f04sr_resistance_dist_100d_v111_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 100)
    return res.replace([np.inf, -np.inf], np.nan)

# Psychological distance to nearest 250
def f04sr_psych_250_v112_signal(closeadj: pd.Series) -> pd.Series:
    level = (closeadj / 250).round() * 250
    res = (closeadj - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Psychological distance to nearest 1000
def f04sr_psych_1000_v113_signal(closeadj: pd.Series) -> pd.Series:
    level = (closeadj / 1000).round() * 1000
    res = (closeadj - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Pivot R1 distance using closeadj
def f04sr_pivot_r1_dist_21d_adj_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = high * adj
    l = low * adj
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    r1 = 2 * p - l.shift(1)
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Pivot S1 distance using closeadj
def f04sr_pivot_s1_dist_21d_adj_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = high * adj
    l = low * adj
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    s1 = 2 * p - h.shift(1)
    res = (closeadj - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Pivot R1 distance using closeadj
def f04sr_pivot_r1_dist_63d_adj_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63).max()
    l = (low * adj).rolling(63).min()
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    r1 = 2 * p - l.shift(1)
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Pivot S1 distance using closeadj
def f04sr_pivot_s1_dist_63d_adj_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63).max()
    l = (low * adj).rolling(63).min()
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    s1 = 2 * p - h.shift(1)
    res = (closeadj - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Pivot R1 distance using closeadj
def f04sr_pivot_r1_dist_126d_adj_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126).max()
    l = (low * adj).rolling(126).min()
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    r1 = 2 * p - l.shift(1)
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Pivot S1 distance using closeadj
def f04sr_pivot_s1_dist_126d_adj_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126).max()
    l = (low * adj).rolling(126).min()
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    s1 = 2 * p - h.shift(1)
    res = (closeadj - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Pivot R1 distance using closeadj
def f04sr_pivot_r1_dist_252d_adj_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252).max()
    l = (low * adj).rolling(252).min()
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    r1 = 2 * p - l.shift(1)
    res = (r1 - closeadj) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Pivot S1 distance using closeadj
def f04sr_pivot_s1_dist_252d_adj_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252).max()
    l = (low * adj).rolling(252).min()
    c = closeadj
    p = (h.shift(1) + l.shift(1) + c.shift(1)) / 3.0
    s1 = 2 * p - h.shift(1)
    res = (closeadj - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Fib 23.6% retracement support distance
def f04sr_fib_236_support_5d_v122_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(5, min_periods=5).max()
    l = low.rolling(5, min_periods=5).min()
    fib = l + (h - l) * 0.236
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day Fib 23.6% retracement support distance
def f04sr_fib_236_support_10d_v123_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(10, min_periods=5).max()
    l = low.rolling(10, min_periods=5).min()
    fib = l + (h - l) * 0.236
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Fib 23.6% retracement support distance
def f04sr_fib_236_support_63d_v124_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63, min_periods=5).max()
    l = (low * adj).rolling(63, min_periods=5).min()
    fib = l + (h - l) * 0.236
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Fib 23.6% retracement support distance
def f04sr_fib_236_support_126d_v125_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126, min_periods=5).max()
    l = (low * adj).rolling(126, min_periods=5).min()
    fib = l + (h - l) * 0.236
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Fib 23.6% retracement support distance
def f04sr_fib_236_support_252d_v126_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.236
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Fib 78.6% retracement support distance
def f04sr_fib_786_support_5d_v127_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(5, min_periods=5).max()
    l = low.rolling(5, min_periods=5).min()
    fib = l + (h - l) * 0.786
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day Fib 78.6% retracement support distance
def f04sr_fib_786_support_10d_v128_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(10, min_periods=5).max()
    l = low.rolling(10, min_periods=5).min()
    fib = l + (h - l) * 0.786
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Fib 78.6% retracement support distance
def f04sr_fib_786_support_63d_v129_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63, min_periods=5).max()
    l = (low * adj).rolling(63, min_periods=5).min()
    fib = l + (h - l) * 0.786
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Fib 78.6% retracement support distance
def f04sr_fib_786_support_126d_v130_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126, min_periods=5).max()
    l = (low * adj).rolling(126, min_periods=5).min()
    fib = l + (h - l) * 0.786
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Fib 78.6% retracement support distance
def f04sr_fib_786_support_252d_v131_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.786
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day volume-weighted support distance using closeadj
def f04sr_vw_support_10d_adj_v132_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    vw_low = (l_adj * volume).rolling(10, min_periods=5).sum() / volume.rolling(10, min_periods=5).sum().replace(0, np.nan)
    res = (closeadj - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day volume-weighted support distance using closeadj
def f04sr_vw_support_21d_adj_v133_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    vw_low = (l_adj * volume).rolling(21, min_periods=5).sum() / volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    res = (closeadj - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day volume-weighted resistance distance using closeadj
def f04sr_vw_resistance_10d_adj_v134_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    vw_high = (h_adj * volume).rolling(10, min_periods=5).sum() / volume.rolling(10, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - closeadj) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day volume-weighted resistance distance using closeadj
def f04sr_vw_resistance_21d_adj_v135_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    vw_high = (h_adj * volume).rolling(21, min_periods=5).sum() / volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - closeadj) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 5-day EMA as support
def f04sr_ema_support_5d_v136_signal(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=5, adjust=False).mean()
    res = (close - ema) / ema.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 10-day EMA as support
def f04sr_ema_support_10d_v137_signal(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=10, adjust=False).mean()
    res = (close - ema) / ema.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 21-day EMA as support
def f04sr_ema_support_21d_v138_signal(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=21, adjust=False).mean()
    res = (close - ema) / ema.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 63-day EMA as support
def f04sr_ema_support_63d_v139_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=63, adjust=False).mean()
    res = (closeadj - ema) / ema.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 126-day EMA as support
def f04sr_ema_support_126d_v140_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=126, adjust=False).mean()
    res = (closeadj - ema) / ema.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 252-day EMA as support
def f04sr_ema_support_252d_v141_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=252, adjust=False).mean()
    res = (closeadj - ema) / ema.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 21-day SMA as support
def f04sr_sma_support_21d_v142_signal(close: pd.Series) -> pd.Series:
    sma = close.rolling(21).mean()
    res = (close - sma) / sma.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 63-day SMA as support
def f04sr_sma_support_63d_v143_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(63).mean()
    res = (closeadj - sma) / sma.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 126-day SMA as support
def f04sr_sma_support_126d_v144_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(126).mean()
    res = (closeadj - sma) / sma.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# distance to 252-day SMA as support
def f04sr_sma_support_252d_v145_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(252).mean()
    res = (closeadj - sma) / sma.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Fib 50.0% retracement resistance distance
def f04sr_fib_500_resistance_252d_v146_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (fib - closeadj) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Fib 50.0% retracement resistance distance
def f04sr_fib_500_resistance_126d_v147_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126, min_periods=5).max()
    l = (low * adj).rolling(126, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (fib - closeadj) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Fib 50.0% retracement resistance distance
def f04sr_fib_500_resistance_63d_v148_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63, min_periods=5).max()
    l = (low * adj).rolling(63, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (fib - closeadj) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Fib 50.0% retracement resistance distance
def f04sr_fib_500_resistance_21d_v149_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (fib - close) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504-day Woodie Pivot Position
def f04sr_woodie_pivot_pos_504d_v150_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h504 = (high * adj).shift(1).rolling(504).max()
    l504 = (low * adj).shift(1).rolling(504).min()
    p = (h504 + l504 + 2 * closeadj.shift(1)) / 4.0
    res = (closeadj - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f04sr_") and f.endswith("_signal")]

F04_SUPPORT_RESISTANCE_PROXIMITY_BASE_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 600; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "volume": np.random.rand(sz)*1000000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F04_SUPPORT_RESISTANCE_PROXIMITY_BASE_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
