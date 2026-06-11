# f19_atr_normalized_price_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _atr_val(h, l, c, w):
    tr = np.maximum(h - l, np.maximum((h - c.shift(1)).abs(), (l - c.shift(1)).abs()))
    return tr.rolling(w, min_periods=min(w, 5)).mean()
def _price_atr_norm(price, level, atr):
    return (price - level) / atr.replace(0, np.nan)
def _atr_zscore(atr, w):
    return (atr - atr.rolling(w, min_periods=min(w, 5)).mean()) / atr.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

# Feature f19anp_v001: Price distance to 5d SMA normalized by 5d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_5d_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _price_atr_norm(close, _sma(close, 5), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v002: Price distance to 10d SMA normalized by 10d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_10d_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = _price_atr_norm(close, _sma(close, 10), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v003: Price distance to 21d SMA normalized by 21d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_21d_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, _sma(close, 21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v004: Price distance to 63d SMA normalized by 63d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_63d_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _price_atr_norm(closeadj, _sma(closeadj, 63), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v005: Price distance to 126d SMA normalized by 126d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_126d_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = _price_atr_norm(closeadj, _sma(closeadj, 126), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v006: Price distance to 252d SMA normalized by 252d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_252d_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = _price_atr_norm(closeadj, _sma(closeadj, 252), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v007: Price distance to 504d SMA normalized by 504d ATR
def f19anp_f19_atr_normalized_price_sma_dist_norm_504d_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 504)
    res = _price_atr_norm(closeadj, _sma(closeadj, 504), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v008: 5d price move normalized by 21d ATR
def f19anp_f19_atr_normalized_price_move_5d_norm_21d_atr_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, close.shift(5), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v009: 10d price move normalized by 21d ATR
def f19anp_f19_atr_normalized_price_move_10d_norm_21d_atr_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, close.shift(10), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v010: 21d price move normalized by 21d ATR
def f19anp_f19_atr_normalized_price_move_21d_norm_21d_atr_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, close.shift(21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v011: 63d price move normalized by 63d ATR
def f19anp_f19_atr_normalized_price_move_63d_norm_63d_atr_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _price_atr_norm(closeadj, closeadj.shift(63), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v012: 126d price move normalized by 126d ATR
def f19anp_f19_atr_normalized_price_move_126d_norm_126d_atr_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = _price_atr_norm(closeadj, closeadj.shift(126), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v013: 252d price move normalized by 252d ATR
def f19anp_f19_atr_normalized_price_move_252d_norm_252d_atr_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = _price_atr_norm(closeadj, closeadj.shift(252), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v014: 5d Donchian channel width normalized by 5d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_5d_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = (_max(high, 5) - _min(low, 5)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v015: 10d Donchian channel width normalized by 10d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_10d_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = (_max(high, 10) - _min(low, 10)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v016: 21d Donchian channel width normalized by 21d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_21d_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (_max(high, 21) - _min(low, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v017: 63d Donchian channel width normalized by 63d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_63d_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 63)
    res = (_max(h_adj, 63) - _min(l_adj, 63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v018: 126d Donchian channel width normalized by 126d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_126d_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 126)
    res = (_max(h_adj, 126) - _min(l_adj, 126)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v019: 252d Donchian channel width normalized by 252d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_252d_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 252)
    res = (_max(h_adj, 252) - _min(l_adj, 252)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v020: 504d Donchian channel width normalized by 504d ATR
def f19anp_f19_atr_normalized_price_donchian_width_norm_504d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 504)
    res = (_max(h_adj, 504) - _min(l_adj, 504)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v021: 5d ATR z-score (21d window)
def f19anp_f19_atr_normalized_price_atr_zscore_5d_21d_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _atr_zscore(atr, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v022: 10d ATR z-score (21d window)
def f19anp_f19_atr_normalized_price_atr_zscore_10d_21d_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = _atr_zscore(atr, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v023: 21d ATR z-score (63d window)
def f19anp_f19_atr_normalized_price_atr_zscore_21d_63d_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _atr_zscore(atr, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v024: 63d ATR z-score (126d window)
def f19anp_f19_atr_normalized_price_atr_zscore_63d_126d_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _atr_zscore(atr, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v025: 126d ATR z-score (252d window)
def f19anp_f19_atr_normalized_price_atr_zscore_126d_252d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = _atr_zscore(atr, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v026: 5d ATR relative to price level (ATR %)
def f19anp_f19_atr_normalized_price_atr_pct_5d_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = atr / close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v027: 10d ATR relative to price level (ATR %)
def f19anp_f19_atr_normalized_price_atr_pct_10d_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = atr / close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v028: 21d ATR relative to price level (ATR %)
def f19anp_f19_atr_normalized_price_atr_pct_21d_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = atr / close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v029: 63d ATR relative to price level (ATR %)
def f19anp_f19_atr_normalized_price_atr_pct_63d_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = atr / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v030: 126d ATR relative to price level (ATR %)
def f19anp_f19_atr_normalized_price_atr_pct_126d_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = atr / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v031: 252d ATR relative to price level (ATR %)
def f19anp_f19_atr_normalized_price_atr_pct_252d_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = atr / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v032: Trailing stop distance (2 ATR, 21d)
def f19anp_f19_atr_normalized_price_trailing_stop_2atr_21d_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    stop = _max(high, 21) - 2 * atr
    res = (close - stop) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v033: Trailing stop distance (3 ATR, 21d)
def f19anp_f19_atr_normalized_price_trailing_stop_3atr_21d_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    stop = _max(high, 21) - 3 * atr
    res = (close - stop) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v034: Price distance to 5d EMA normalized by 5d ATR
def f19anp_f19_atr_normalized_price_ema_dist_norm_5d_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _price_atr_norm(close, _ema(close, 5), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v035: Price distance to 21d EMA normalized by 21d ATR
def f19anp_f19_atr_normalized_price_ema_dist_norm_21d_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, _ema(close, 21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v036: Price distance to 63d EMA normalized by 63d ATR
def f19anp_f19_atr_normalized_price_ema_dist_norm_63d_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _price_atr_norm(closeadj, _ema(closeadj, 63), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v037: 5d price move normalized by 5d ATR
def f19anp_f19_atr_normalized_price_move_5d_norm_5d_atr_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _price_atr_norm(close, close.shift(5), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v038: 10d price move normalized by 10d ATR
def f19anp_f19_atr_normalized_price_move_10d_norm_10d_atr_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = _price_atr_norm(close, close.shift(10), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v039: 21d price move normalized by 10d ATR
def f19anp_f19_atr_normalized_price_move_21d_norm_10d_atr_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = _price_atr_norm(close, close.shift(21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v040: Price range (high-low) 5d average normalized by 21d ATR
def f19anp_f19_atr_normalized_price_range_5d_norm_21d_atr_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (high - low).rolling(5).mean() / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v041: Price range (high-low) 21d average normalized by 21d ATR
def f19anp_f19_atr_normalized_price_range_21d_norm_21d_atr_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (high - low).rolling(21).mean() / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v042: 5d SMA of close vs 21d SMA of close normalized by 21d ATR
def f19anp_f19_atr_normalized_price_sma_cross_norm_21d_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(_sma(close, 5), _sma(close, 21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v043: 10d SMA of close vs 63d SMA of close normalized by 63d ATR
def f19anp_f19_atr_normalized_price_sma_cross_norm_63d_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _price_atr_norm(_sma(closeadj, 10), _sma(closeadj, 63), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v044: 21d SMA of close vs 252d SMA of close normalized by 252d ATR
def f19anp_f19_atr_normalized_price_sma_cross_norm_252d_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = _price_atr_norm(_sma(closeadj, 21), _sma(closeadj, 252), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v045: 5d high vs 5d low normalized by 21d ATR
def f19anp_f19_atr_normalized_price_high_low_norm_21d_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (_max(high, 5) - _min(low, 5)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v046: 21d high vs 21d low normalized by 63d ATR
def f19anp_f19_atr_normalized_price_high_low_norm_63d_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = (_max(high * adj, 21) - _min(low * adj, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v047: Close distance to 5d high normalized by 5d ATR
def f19anp_f19_atr_normalized_price_close_high_dist_norm_5d_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _price_atr_norm(close, _max(high, 5), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v048: Close distance to 21d high normalized by 21d ATR
def f19anp_f19_atr_normalized_price_close_high_dist_norm_21d_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, _max(high, 21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v049: Close distance to 5d low normalized by 5d ATR
def f19anp_f19_atr_normalized_price_close_low_dist_norm_5d_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _price_atr_norm(close, _min(low, 5), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v050: Close distance to 21d low normalized by 21d ATR
def f19anp_f19_atr_normalized_price_close_low_dist_norm_21d_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _price_atr_norm(close, _min(low, 21), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v051: ATR(5) / ATR(21) ratio
def f19anp_f19_atr_normalized_price_atr_ratio_5d_21d_v051_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _atr_val(high, low, close, 5) / _atr_val(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v052: ATR(10) / ATR(63) ratio
def f19anp_f19_atr_normalized_price_atr_ratio_10d_63d_v052_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr_val(high * adj, low * adj, closeadj, 10) / _atr_val(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v053: ATR(21) / ATR(252) ratio
def f19anp_f19_atr_normalized_price_atr_ratio_21d_252d_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr_val(high * adj, low * adj, closeadj, 21) / _atr_val(high * adj, low * adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v054: Close distance to 252d high normalized by 252d ATR
def f19anp_f19_atr_normalized_price_close_high_dist_norm_252d_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = _price_atr_norm(closeadj, _max(high * adj, 252), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v055: Close distance to 252d low normalized by 252d ATR
def f19anp_f19_atr_normalized_price_close_low_dist_norm_252d_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = _price_atr_norm(closeadj, _min(low * adj, 252), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v056: 5d SMA of ATR(5) normalized by price
def f19anp_f19_atr_normalized_price_atr_ma_norm_5d_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _sma(atr, 5) / close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v057: 21d SMA of ATR(21) normalized by price
def f19anp_f19_atr_normalized_price_atr_ma_norm_21d_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _sma(atr, 21) / close.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v058: 63d SMA of ATR(63) normalized by price
def f19anp_f19_atr_normalized_price_atr_ma_norm_63d_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _sma(atr, 63) / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v059: 5d price volatility (std) normalized by 5d ATR
def f19anp_f19_atr_normalized_price_vol_norm_5d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = close.rolling(5).std() / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v060: 21d price volatility (std) normalized by 21d ATR
def f19anp_f19_atr_normalized_price_vol_norm_21d_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = close.rolling(21).std() / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v061: 63d price volatility (std) normalized by 63d ATR
def f19anp_f19_atr_normalized_price_vol_norm_63d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = closeadj.rolling(63).std() / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v062: 5d price move normalized by 5d SMA of ATR(21)
def f19anp_f19_atr_normalized_price_move_5d_norm_atr_ma_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr_ma = _sma(_atr_val(high, low, close, 21), 5)
    res = _price_atr_norm(close, close.shift(5), atr_ma)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v063: 21d price move normalized by 21d SMA of ATR(63)
def f19anp_f19_atr_normalized_price_move_21d_norm_atr_ma_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr_ma = _sma(_atr_val(high * adj, low * adj, closeadj, 63), 21)
    res = _price_atr_norm(closeadj, closeadj.shift(21), atr_ma)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v064: 5d high distance to 21d high normalized by 21d ATR
def f19anp_f19_atr_normalized_price_high_dist_norm_21d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (_max(high, 5) - _max(high, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v065: 5d low distance to 21d low normalized by 21d ATR
def f19anp_f19_atr_normalized_price_low_dist_norm_21d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (_min(low, 5) - _min(low, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v066: 10d high distance to 63d high normalized by 63d ATR
def f19anp_f19_atr_normalized_price_high_dist_norm_63d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 63)
    res = (_max(h_adj, 10) - _max(h_adj, 63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v067: 10d low distance to 63d low normalized by 63d ATR
def f19anp_f19_atr_normalized_price_low_dist_norm_63d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 63)
    res = (_min(l_adj, 10) - _min(l_adj, 63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v068: Price distance to 5d EMA vs 21d EMA normalized by 21d ATR
def f19anp_f19_atr_normalized_price_ema_cross_dist_norm_21d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (_ema(close, 5) - _ema(close, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v069: Price distance to 21d EMA vs 63d EMA normalized by 63d ATR
def f19anp_f19_atr_normalized_price_ema_cross_dist_norm_63d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = (_ema(closeadj, 21) - _ema(closeadj, 63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v070: 5d ATR z-score (63d window)
def f19anp_f19_atr_normalized_price_atr_zscore_5d_63d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _atr_zscore(atr, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v071: 10d ATR z-score (63d window)
def f19anp_f19_atr_normalized_price_atr_zscore_10d_63d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    res = _atr_zscore(atr, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v072: 21d ATR z-score (126d window)
def f19anp_f19_atr_normalized_price_atr_zscore_21d_126d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = _atr_zscore(atr, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v073: 63d ATR z-score (252d window)
def f19anp_f19_atr_normalized_price_atr_zscore_63d_252d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _atr_zscore(atr, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v074: 126d ATR z-score (504d window)
def f19anp_f19_atr_normalized_price_atr_zscore_126d_504d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = _atr_zscore(atr, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v075: 5d SMA of ATR % (21d)
def f19anp_f19_atr_normalized_price_atr_pct_ma_5d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr_pct = _atr_val(high, low, close, 21) / close.replace(0, np.nan)
    res = _sma(atr_pct, 5)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f19anp_") and f.endswith("_signal")]

F19_ATR_NORMALIZED_PRICE_BASE_REGISTRY_001_075 = {
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
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F19_ATR_NORMALIZED_PRICE_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001_075 OK")
