# f04_support_resistance_proximity_base_001_075_gemini.py
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

# Base Features 001-075

# 5-day support distance
def f04sr_support_dist_5d_v001_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day support distance
def f04sr_support_dist_10d_v002_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day support distance
def f04sr_support_dist_21d_v003_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day support distance using closeadj
def f04sr_support_dist_63d_v004_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day support distance using closeadj
def f04sr_support_dist_126d_v005_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day support distance using closeadj
def f04sr_support_dist_252d_v006_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day resistance distance
def f04sr_resistance_dist_5d_v007_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day resistance distance
def f04sr_resistance_dist_10d_v008_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day resistance distance
def f04sr_resistance_dist_21d_v009_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day resistance distance using closeadj
def f04sr_resistance_dist_63d_v010_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day resistance distance using closeadj
def f04sr_resistance_dist_126d_v011_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day resistance distance using closeadj
def f04sr_resistance_dist_252d_v012_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standard Pivot Position
def f04sr_pivot_pos_std_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _pivot_pos(close, high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

# Pivot Position using closeadj
def f04sr_pivot_pos_adj_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _pivot_pos(closeadj, high * adj, low * adj, closeadj)
    return res.replace([np.inf, -np.inf], np.nan)

# 504-day support distance
def f04sr_support_dist_504d_v015_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 504-day resistance distance
def f04sr_resistance_dist_504d_v016_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Pivot R1 proximity (synthetic pivot pos)
def f04sr_pivot_r1_dist_5d_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2 * p - low.shift(1)
    res = (close - r1) / r1.abs().replace(0, np.nan)
    # Using pivot_pos logic internally but specifically for R1
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Pivot S1 proximity
def f04sr_pivot_s1_dist_5d_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2 * p - high.shift(1)
    res = (close - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Pivot R2 proximity
def f04sr_pivot_r2_dist_5d_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    res = (close - r2) / r2.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Pivot S2 proximity
def f04sr_pivot_s2_dist_5d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s2 = p - (high.shift(1) - low.shift(1))
    res = (close - s2) / s2.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 20-day Fib 23.6% retracement support distance
def f04sr_fib_236_support_21d_v021_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.236
    res = (close - fib) / fib.abs().replace(0, np.nan)
    # Framed as a support distance
    return res.replace([np.inf, -np.inf], np.nan)

# 20-day Fib 38.2% retracement support distance
def f04sr_fib_382_support_21d_v022_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.382
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 20-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_21d_v023_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 20-day Fib 61.8% retracement support distance
def f04sr_fib_618_support_21d_v024_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.618
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 20-day Fib 78.6% retracement support distance
def f04sr_fib_786_support_21d_v025_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.786
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Psychological distance to nearest 10
def f04sr_psych_10_v026_signal(close: pd.Series) -> pd.Series:
    level = (close / 10).round() * 10
    res = (close - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Psychological distance to nearest 50
def f04sr_psych_50_v027_signal(close: pd.Series) -> pd.Series:
    level = (close / 50).round() * 50
    res = (close - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Psychological distance to nearest 100
def f04sr_psych_100_v028_signal(close: pd.Series) -> pd.Series:
    level = (close / 100).round() * 100
    res = (close - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_63d_v029_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63, min_periods=5).max()
    l = (low * adj).rolling(63, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_126d_v030_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126, min_periods=5).max()
    l = (low * adj).rolling(126, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_252d_v031_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day volume-weighted support distance (simplified)
def f04sr_vw_support_5d_v032_signal(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vw_low = (low * volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0, np.nan)
    res = (close - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day volume-weighted support distance
def f04sr_vw_support_21d_v033_signal(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vw_low = (low * volume).rolling(21, min_periods=5).sum() / volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    res = (close - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day volume-weighted support distance
def f04sr_vw_support_63d_v034_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    vw_low = (l_adj * volume).rolling(63, min_periods=5).sum() / volume.rolling(63, min_periods=5).sum().replace(0, np.nan)
    res = (closeadj - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day volume-weighted support distance
def f04sr_vw_support_126d_v035_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    vw_low = (l_adj * volume).rolling(126, min_periods=5).sum() / volume.rolling(126, min_periods=5).sum().replace(0, np.nan)
    res = (closeadj - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day volume-weighted support distance
def f04sr_vw_support_252d_v036_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    vw_low = (l_adj * volume).rolling(252, min_periods=5).sum() / volume.rolling(252, min_periods=5).sum().replace(0, np.nan)
    res = (closeadj - vw_low) / vw_low.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day volume-weighted resistance distance
def f04sr_vw_resistance_5d_v037_signal(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    vw_high = (high * volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - close) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day volume-weighted resistance distance
def f04sr_vw_resistance_21d_v038_signal(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    vw_high = (high * volume).rolling(21, min_periods=5).sum() / volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - close) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day volume-weighted resistance distance
def f04sr_vw_resistance_63d_v039_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    vw_high = (h_adj * volume).rolling(63, min_periods=5).sum() / volume.rolling(63, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - closeadj) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day volume-weighted resistance distance
def f04sr_vw_resistance_126d_v040_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    vw_high = (h_adj * volume).rolling(126, min_periods=5).sum() / volume.rolling(126, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - closeadj) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day volume-weighted resistance distance
def f04sr_vw_resistance_252d_v041_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    vw_high = (h_adj * volume).rolling(252, min_periods=5).sum() / volume.rolling(252, min_periods=5).sum().replace(0, np.nan)
    res = (vw_high - closeadj) / vw_high.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Average of 5, 10, 21 day support distance
def f04sr_support_dist_avg_short_v042_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    s5 = low.rolling(5).min()
    s10 = low.rolling(10).min()
    s21 = low.rolling(21).min()
    s_avg = (s5 + s10 + s21) / 3.0
    res = (close - s_avg) / s_avg.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Average of 63, 126, 252 day support distance
def f04sr_support_dist_avg_long_v043_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l_adj = low * adj
    s63 = l_adj.rolling(63).min()
    s126 = l_adj.rolling(126).min()
    s252 = l_adj.rolling(252).min()
    s_avg = (s63 + s126 + s252) / 3.0
    res = (closeadj - s_avg) / s_avg.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Average of 5, 10, 21 day resistance distance
def f04sr_resistance_dist_avg_short_v044_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    r5 = high.rolling(5).max()
    r10 = high.rolling(10).max()
    r21 = high.rolling(21).max()
    r_avg = (r5 + r10 + r21) / 3.0
    res = (r_avg - close) / r_avg.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Average of 63, 126, 252 day resistance distance
def f04sr_resistance_dist_avg_long_v045_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    r63 = h_adj.rolling(63).max()
    r126 = h_adj.rolling(126).max()
    r252 = h_adj.rolling(252).max()
    r_avg = (r63 + r126 + r252) / 3.0
    res = (r_avg - closeadj) / r_avg.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Pivot Midpoint (P) distance
def f04sr_pivot_p_dist_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    res = (close - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Pivot R3 distance
def f04sr_pivot_r3_dist_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r3 = high.shift(1) + 2 * (p - low.shift(1))
    res = (r3 - close) / r3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Pivot S3 distance
def f04sr_pivot_s3_dist_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s3 = low.shift(1) - 2 * (high.shift(1) - p)
    res = (close - s3) / s3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 42-day support distance
def f04sr_support_dist_42d_v049_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# 42-day resistance distance
def f04sr_resistance_dist_42d_v050_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# 10-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_10d_v051_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(10, min_periods=5).max()
    l = low.rolling(10, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Fib 50.0% retracement support distance
def f04sr_fib_500_support_5d_v052_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(5, min_periods=5).max()
    l = low.rolling(5, min_periods=5).min()
    fib = l + (h - l) * 0.500
    res = (close - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day psychological round 10 support
def f04sr_psych_10_support_21d_v053_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    l21 = low.rolling(21).min()
    level = (l21 / 10).round() * 10
    res = (close - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day psychological round 10 resistance
def f04sr_psych_10_resistance_21d_v054_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    h21 = high.rolling(21).max()
    level = (h21 / 10).round() * 10
    res = (level - close) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day psychological round 100 support
def f04sr_psych_100_support_63d_v055_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    l63 = (low * adj).rolling(63).min()
    level = (l63 / 100).round() * 100
    res = (closeadj - level) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day psychological round 100 resistance
def f04sr_psych_100_resistance_63d_v056_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h63 = (high * adj).rolling(63).max()
    level = (h63 / 100).round() * 100
    res = (level - closeadj) / level.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Woodie Pivot Position
def f04sr_woodie_pivot_pos_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2 * close) / 4.0
    res = (close - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Woodie R1 distance
def f04sr_woodie_r1_dist_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2 * close) / 4.0
    r1 = 2 * p - low.shift(1)
    res = (r1 - close) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day Woodie S1 distance
def f04sr_woodie_s1_dist_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2 * close) / 4.0
    s1 = 2 * p - high.shift(1)
    res = (close - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Camarilla Pivot R3 distance
def f04sr_camarilla_r3_dist_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r3 = close.shift(1) + (high.shift(1) - low.shift(1)) * 1.1 / 4.0
    res = (r3 - close) / r3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Camarilla Pivot S3 distance
def f04sr_camarilla_s3_dist_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    s3 = close.shift(1) - (high.shift(1) - low.shift(1)) * 1.1 / 4.0
    res = (close - s3) / s3.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Camarilla Pivot R4 distance
def f04sr_camarilla_r4_dist_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r4 = close.shift(1) + (high.shift(1) - low.shift(1)) * 1.1 / 2.0
    res = (r4 - close) / r4.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Camarilla Pivot S4 distance
def f04sr_camarilla_s4_dist_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    s4 = close.shift(1) - (high.shift(1) - low.shift(1)) * 1.1 / 2.0
    res = (close - s4) / s4.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Fibonacci 0% (Low) distance
def f04sr_fib_000_support_21d_v064_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    l21 = low.rolling(21, min_periods=5).min()
    res = (close - l21) / l21.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Fibonacci 100% (High) distance
def f04sr_fib_100_resistance_21d_v065_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    h21 = high.rolling(21, min_periods=5).max()
    res = (h21 - close) / h21.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day support distance to closeadj-based low
def f04sr_support_dist_closeadj_63d_v066_signal(closeadj: pd.Series) -> pd.Series:
    res = _support_dist(closeadj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 63-day resistance distance to closeadj-based high
def f04sr_resistance_dist_closeadj_63d_v067_signal(closeadj: pd.Series) -> pd.Series:
    res = _resistance_dist(closeadj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day support distance to closeadj-based low
def f04sr_support_dist_closeadj_126d_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = _support_dist(closeadj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 126-day resistance distance to closeadj-based high
def f04sr_resistance_dist_closeadj_126d_v069_signal(closeadj: pd.Series) -> pd.Series:
    res = _resistance_dist(closeadj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day support distance to closeadj-based low
def f04sr_support_dist_closeadj_252d_v070_signal(closeadj: pd.Series) -> pd.Series:
    res = _support_dist(closeadj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day resistance distance to closeadj-based high
def f04sr_resistance_dist_closeadj_252d_v071_signal(closeadj: pd.Series) -> pd.Series:
    res = _resistance_dist(closeadj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day Pivot Pos Variation (using typical price)
def f04sr_pivot_pos_typical_21d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    typical = (high + low + close) / 3.0
    p = typical.shift(1).rolling(21).mean()
    res = (close - p) / p.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day deMark Pivot R1 distance
def f04sr_demark_r1_dist_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    c = close.shift(1)
    o = close.shift(2) # Simplified open
    h = high.shift(1)
    l = low.shift(1)
    x = pd.Series(0.0, index=close.index)
    mask1 = c < o
    x[mask1] = h + 2*l + c
    mask2 = c > o
    x[mask2] = 2*h + l + c
    mask3 = c == o
    x[mask3] = h + l + 2*c
    r1 = x / 2.0 - l
    res = (r1 - close) / r1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day deMark Pivot S1 distance
def f04sr_demark_s1_dist_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    c = close.shift(1)
    o = close.shift(2)
    h = high.shift(1)
    l = low.shift(1)
    x = pd.Series(0.0, index=close.index)
    mask1 = c < o
    x[mask1] = h + 2*l + c
    mask2 = c > o
    x[mask2] = 2*h + l + c
    mask3 = c == o
    x[mask3] = h + l + 2*c
    s1 = x / 2.0 - h
    res = (close - s1) / s1.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252-day Fib 38.2% retracement support distance
def f04sr_fib_382_support_252d_v075_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.382
    res = (closeadj - fib) / fib.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f04sr_") and f.endswith("_signal")]

F04_SUPPORT_RESISTANCE_PROXIMITY_BASE_001_075 = {
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
    for n, c in F04_SUPPORT_RESISTANCE_PROXIMITY_BASE_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
