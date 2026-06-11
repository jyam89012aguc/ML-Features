# f04_support_resistance_proximity_slope_001_150_gemini.py
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

# 150 Explicit Slope Features

def f04sr_support_dist_5d_slope_v001_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_10d_slope_v002_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_21d_slope_v003_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_63d_slope_v004_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_126d_slope_v005_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_252d_slope_v006_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_504d_slope_v007_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_5d_slope_v008_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_10d_slope_v009_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_21d_slope_v010_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 21).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_63d_slope_v011_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 63).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_126d_slope_v012_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 126).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_252d_slope_v013_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 252).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_504d_slope_v014_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 504).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_pos_std_slope_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _pivot_pos(close, high, low, close).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_pos_adj_slope_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _pivot_pos(closeadj, high * adj, low * adj, closeadj).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_r1_dist_5d_slope_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2 * p - low.shift(1)
    res = ((close - r1) / r1.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_s1_dist_5d_slope_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2 * p - high.shift(1)
    res = ((close - s1) / s1.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_500_support_21d_slope_v019_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21, min_periods=5).max()
    l = low.rolling(21, min_periods=5).min()
    fib = l + (h - l) * 0.5
    res = ((close - fib) / fib.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_500_support_63d_slope_v020_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63, min_periods=5).max()
    l = (low * adj).rolling(63, min_periods=5).min()
    fib = l + (h - l) * 0.5
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_500_support_126d_slope_v021_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126, min_periods=5).max()
    l = (low * adj).rolling(126, min_periods=5).min()
    fib = l + (h - l) * 0.5
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_500_support_252d_slope_v022_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252, min_periods=5).max()
    l = (low * adj).rolling(252, min_periods=5).min()
    fib = l + (h - l) * 0.5
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_support_5d_slope_v023_signal(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vw_low = (low * volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0, np.nan)
    res = ((close - vw_low) / vw_low.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_support_21d_slope_v024_signal(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    vw_low = (low * volume).rolling(21, min_periods=5).sum() / volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    res = ((close - vw_low) / vw_low.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_support_63d_slope_v025_signal(closeadj: pd.Series, low: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vw_low = ((low * adj) * volume).rolling(63, min_periods=5).sum() / volume.rolling(63, min_periods=5).sum().replace(0, np.nan)
    res = ((closeadj - vw_low) / vw_low.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_10_slope_v026_signal(close: pd.Series) -> pd.Series:
    level = (close / 10).round() * 10
    res = ((close - level) / level.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_sma_support_21d_slope_v027_signal(close: pd.Series) -> pd.Series:
    sma = close.rolling(21).mean()
    res = ((close - sma) / sma.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_sma_support_63d_slope_v028_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(63).mean()
    res = ((closeadj - sma) / sma.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_sma_support_252d_slope_v029_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(252).mean()
    res = ((closeadj - sma) / sma.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_5d_slope_v030_signal(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=5, adjust=False).mean()
    res = ((close - ema) / ema.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_30d_slope_v031_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 30).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_30d_slope_v032_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 30).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_40d_slope_v033_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 40).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_40d_slope_v034_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 40).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_50d_slope_v035_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 50).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_50d_slope_v036_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 50).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_70d_slope_v037_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 70).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_70d_slope_v038_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 70).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_80d_slope_v039_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 80).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_80d_slope_v040_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 80).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_90d_slope_v041_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 90).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_90d_slope_v042_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 90).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_110d_slope_v043_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 110).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_110d_slope_v044_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 110).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_150d_slope_v045_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 150).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_150d_slope_v046_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 150).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_200d_slope_v047_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 200).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_200d_slope_v048_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 200).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_236_support_21d_slope_v049_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21).max(); l = low.rolling(21).min()
    fib = l + (h - l) * 0.236
    res = ((close - fib) / fib.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_382_support_21d_slope_v050_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21).max(); l = low.rolling(21).min()
    fib = l + (h - l) * 0.382
    res = ((close - fib) / fib.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_618_support_21d_slope_v051_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21).max(); l = low.rolling(21).min()
    fib = l + (h - l) * 0.618
    res = ((close - fib) / fib.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_786_support_21d_slope_v052_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    h = high.rolling(21).max(); l = low.rolling(21).min()
    fib = l + (h - l) * 0.786
    res = ((close - fib) / fib.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_236_support_63d_slope_v053_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63).max(); l = (low * adj).rolling(63).min()
    fib = l + (h - l) * 0.236
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_382_support_63d_slope_v054_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63).max(); l = (low * adj).rolling(63).min()
    fib = l + (h - l) * 0.382
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_618_support_63d_slope_v055_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63).max(); l = (low * adj).rolling(63).min()
    fib = l + (h - l) * 0.618
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_786_support_63d_slope_v056_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(63).max(); l = (low * adj).rolling(63).min()
    fib = l + (h - l) * 0.786
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_236_support_126d_slope_v057_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126).max(); l = (low * adj).rolling(126).min()
    fib = l + (h - l) * 0.236
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_382_support_126d_slope_v058_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126).max(); l = (low * adj).rolling(126).min()
    fib = l + (h - l) * 0.382
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_618_support_126d_slope_v059_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126).max(); l = (low * adj).rolling(126).min()
    fib = l + (h - l) * 0.618
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_786_support_126d_slope_v060_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(126).max(); l = (low * adj).rolling(126).min()
    fib = l + (h - l) * 0.786
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_236_support_252d_slope_v061_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252).max(); l = (low * adj).rolling(252).min()
    fib = l + (h - l) * 0.236
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_382_support_252d_slope_v062_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252).max(); l = (low * adj).rolling(252).min()
    fib = l + (h - l) * 0.382
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_618_support_252d_slope_v063_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252).max(); l = (low * adj).rolling(252).min()
    fib = l + (h - l) * 0.618
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_786_support_252d_slope_v064_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(252).max(); l = (low * adj).rolling(252).min()
    fib = l + (h - l) * 0.786
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_236_support_504d_slope_v065_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(504).max(); l = (low * adj).rolling(504).min()
    fib = l + (h - l) * 0.236
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_382_support_504d_slope_v066_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(504).max(); l = (low * adj).rolling(504).min()
    fib = l + (h - l) * 0.382
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_618_support_504d_slope_v067_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(504).max(); l = (low * adj).rolling(504).min()
    fib = l + (h - l) * 0.618
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_fib_786_support_504d_slope_v068_signal(closeadj: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h = (high * adj).rolling(504).max(); l = (low * adj).rolling(504).min()
    fib = l + (h - l) * 0.786
    res = ((closeadj - fib) / fib.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_25_slope_v069_signal(close: pd.Series) -> pd.Series:
    level = (close / 25).round() * 25
    res = ((close - level) / level.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_50_slope_v070_signal(close: pd.Series) -> pd.Series:
    level = (close / 50).round() * 50
    res = ((close - level) / level.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_100_slope_v071_signal(close: pd.Series) -> pd.Series:
    level = (close / 100).round() * 100
    res = ((close - level) / level.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_250_slope_v072_signal(closeadj: pd.Series) -> pd.Series:
    level = (closeadj / 250).round() * 250
    res = ((closeadj - level) / level.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_500_slope_v073_signal(closeadj: pd.Series) -> pd.Series:
    level = (closeadj / 500).round() * 500
    res = ((closeadj - level) / level.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_psych_1000_slope_v074_signal(closeadj: pd.Series) -> pd.Series:
    level = (closeadj / 1000).round() * 1000
    res = ((closeadj - level) / level.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_resistance_5d_slope_v075_signal(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    vw_high = (high * volume).rolling(5).sum() / volume.rolling(5).sum().replace(0, np.nan)
    res = ((vw_high - close) / vw_high.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_resistance_21d_slope_v076_signal(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    vw_high = (high * volume).rolling(21).sum() / volume.rolling(21).sum().replace(0, np.nan)
    res = ((vw_high - close) / vw_high.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_resistance_63d_slope_v077_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vw_high = ((high * adj) * volume).rolling(63).sum() / volume.rolling(63).sum().replace(0, np.nan)
    res = ((vw_high - closeadj) / vw_high.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_resistance_126d_slope_v078_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vw_high = ((high * adj) * volume).rolling(126).sum() / volume.rolling(126).sum().replace(0, np.nan)
    res = ((vw_high - closeadj) / vw_high.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_resistance_252d_slope_v079_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vw_high = ((high * adj) * volume).rolling(252).sum() / volume.rolling(252).sum().replace(0, np.nan)
    res = ((vw_high - closeadj) / vw_high.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_vw_resistance_504d_slope_v080_signal(closeadj: pd.Series, high: pd.Series, volume: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vw_high = ((high * adj) * volume).rolling(504).sum() / volume.rolling(504).sum().replace(0, np.nan)
    res = ((vw_high - closeadj) / vw_high.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_10d_slope_v081_signal(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=10, adjust=False).mean()
    res = ((close - ema) / ema.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_21d_slope_v082_signal(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=21, adjust=False).mean()
    res = ((close - ema) / ema.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_63d_slope_v083_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=63, adjust=False).mean()
    res = ((closeadj - ema) / ema.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_126d_slope_v084_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=126, adjust=False).mean()
    res = ((closeadj - ema) / ema.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_252d_slope_v085_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=252, adjust=False).mean()
    res = ((closeadj - ema) / ema.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_ema_support_504d_slope_v086_signal(closeadj: pd.Series) -> pd.Series:
    ema = closeadj.ewm(span=504, adjust=False).mean()
    res = ((closeadj - ema) / ema.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_sma_support_10d_slope_v087_signal(close: pd.Series) -> pd.Series:
    sma = close.rolling(10).mean()
    res = ((close - sma) / sma.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_sma_support_126d_slope_v088_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(126).mean()
    res = ((closeadj - sma) / sma.abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_sma_support_504d_slope_v089_signal(closeadj: pd.Series) -> pd.Series:
    sma = closeadj.rolling(504).mean()
    res = ((closeadj - sma) / sma.abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_r2_dist_5d_slope_v090_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r2 = p + (high.shift(1) - low.shift(1))
    res = ((close - r2) / r2.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_s2_dist_5d_slope_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s2 = p - (high.shift(1) - low.shift(1))
    res = ((close - s2) / s2.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_r3_dist_5d_slope_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r3 = high.shift(1) + 2 * (p - low.shift(1))
    res = ((close - r3) / r3.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_pivot_s3_dist_5d_slope_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s3 = low.shift(1) - 2 * (high.shift(1) - p)
    res = ((close - s3) / s3.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_woodie_r1_dist_slope_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2 * close.shift(1)) / 4.0
    r1 = 2 * p - low.shift(1)
    res = ((r1 - close) / r1.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_woodie_s1_dist_slope_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p = (high.shift(1) + low.shift(1) + 2 * close.shift(1)) / 4.0
    s1 = 2 * p - high.shift(1)
    res = ((close - s1) / s1.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_camarilla_r4_dist_slope_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r4 = close.shift(1) + (high.shift(1) - low.shift(1)) * 1.1 / 2.0
    res = ((r4 - close) / r4.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_camarilla_s4_dist_slope_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    s4 = close.shift(1) - (high.shift(1) - low.shift(1)) * 1.1 / 2.0
    res = ((close - s4) / s4.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_demark_s1_dist_slope_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    c = close.shift(1); o = close.shift(2); h = high.shift(1); l = low.shift(1)
    x = pd.Series(0.0, index=close.index)
    x[c < o] = h + 2*l + c; x[c > o] = 2*h + l + c; x[c == o] = h + l + 2*c
    s1 = x / 2.0 - h
    res = ((close - s1) / s1.abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_15d_slope_v099_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 15).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_15d_slope_v100_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 15).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_25d_slope_v101_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 25).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_25d_slope_v102_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 25).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_35d_slope_v103_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 35).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_35d_slope_v104_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 35).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_45d_slope_v105_signal(close: pd.Series, low: pd.Series) -> pd.Series:
    res = _support_dist(close, low, 45).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_45d_slope_v106_signal(close: pd.Series, high: pd.Series) -> pd.Series:
    res = _resistance_dist(close, high, 45).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_55d_slope_v107_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 55).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_55d_slope_v108_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 55).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_65d_slope_v109_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 65).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_65d_slope_v110_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 65).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_75d_slope_v111_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 75).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_75d_slope_v112_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 75).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_85d_slope_v113_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 85).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_85d_slope_v114_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 85).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_95d_slope_v115_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 95).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_95d_slope_v116_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 95).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_105d_slope_v117_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 105).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_105d_slope_v118_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 105).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_115d_slope_v119_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 115).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_115d_slope_v120_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 115).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_125d_slope_v121_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 125).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_125d_slope_v122_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 125).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_135d_slope_v123_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 135).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_135d_slope_v124_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 135).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_145d_slope_v125_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 145).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_145d_slope_v126_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 145).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_160d_slope_v127_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 160).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_160d_slope_v128_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 160).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_170d_slope_v129_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 170).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_170d_slope_v130_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 170).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_180d_slope_v131_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 180).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_180d_slope_v132_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 180).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_190d_slope_v133_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 190).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_190d_slope_v134_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 190).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_210d_slope_v135_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 210).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_210d_slope_v136_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 210).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_220d_slope_v137_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 220).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_220d_slope_v138_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 220).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_230d_slope_v139_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 230).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_230d_slope_v140_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 230).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_240d_slope_v141_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 240).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_240d_slope_v142_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 240).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_260d_slope_v143_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 260).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_260d_slope_v144_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 260).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_270d_slope_v145_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 270).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_270d_slope_v146_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 270).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_280d_slope_v147_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 280).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_280d_slope_v148_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 280).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_support_dist_290d_slope_v149_signal(closeadj: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _support_dist(closeadj, low * adj, 290).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04sr_resistance_dist_290d_slope_v150_signal(closeadj: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _resistance_dist(closeadj, high * adj, 290).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

SLOPE_NAMES = [f for f in globals() if f.startswith("f04sr_") and f.endswith("_signal")]

F04_SUPPORT_RESISTANCE_PROXIMITY_SLOPE_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(SLOPE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "volume": np.random.rand(sz)*1000000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F04_SUPPORT_RESISTANCE_PROXIMITY_SLOPE_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("slope 001-150 OK")
