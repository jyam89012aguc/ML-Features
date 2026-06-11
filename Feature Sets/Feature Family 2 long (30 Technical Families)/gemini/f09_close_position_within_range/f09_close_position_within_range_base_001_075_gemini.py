# f09_close_position_within_range_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 5)).std()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()

# Domain Primitives
def _close_in_range(h, l, c):
    """Calculates the relative position of close within the high-low range."""
    return (c - l) / (h - l).abs().replace(0, np.nan)

def _close_relative_mid(h, l, c):
    """Calculates the relative position of close relative to the range midpoint."""
    mid = (h + l) / 2.0
    return (c - mid) / ((h - l) / 2.0).abs().replace(0, np.nan)

def _close_range_z(h, l, c, w):
    """Calculates the z-score of the close position within a rolling window."""
    pos = _close_in_range(h, l, c)
    return (pos - pos.rolling(w, min_periods=min(w, 5)).mean()) / pos.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)

def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)

# --- Feature Functions 001-075 ---

def f09cpwr_f09_close_position_within_range_intraday_pos_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday close position within the current candle's high-low range."""
    res = _close_in_range(high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_mid_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday close position relative to the midpoint of the current candle."""
    res = _close_relative_mid(high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within the 5-day Donchian channel."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_10d_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within the 10-day Donchian channel."""
    res = _close_in_range(_max(high, 10), _min(low, 10), close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within the 21-day Donchian channel."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position within the 63-day Donchian channel using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position within the 126-day Donchian channel using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_252d_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position within the 252-day Donchian channel using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position relative to the 5-day range midpoint."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_21d_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position relative to the 21-day range midpoint."""
    res = _close_relative_mid(_max(high, 21), _min(low, 21), close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_21d_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday close position over 21 days."""
    res = _close_range_z(high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_63d_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Z-score of intraday close position over 63 days using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_range_z(high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_sma_pos_5d_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day SMA of the intraday close position."""
    res = _sma(_close_in_range(high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_sma_pos_21d_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the intraday close position."""
    res = _sma(_close_in_range(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_ema_pos_21d_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of the intraday close position."""
    res = _ema(_close_in_range(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_atr_norm_pos_21d_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within 21-day range normalized by 21-day ATR."""
    pos = _close_in_range(_max(high, 21), _min(low, 21), close)
    atr = _atr(high, low, close, 21)
    res = pos / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_skew_pos_21d_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling skewness of the intraday close position."""
    pos = _close_in_range(high, low, close)
    res = pos.rolling(21, min_periods=21).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_kurt_pos_21d_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling kurtosis of the intraday close position."""
    pos = _close_in_range(high, low, close)
    res = pos.rolling(21, min_periods=21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_rel_atr_5d_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position relative to range, divided by ATR 5d ratio."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close) / (_atr(high, low, close, 5) / close.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_rel_atr_10d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position relative to range, divided by ATR 10d ratio."""
    res = _close_in_range(_max(high, 10), _min(low, 10), close) / (_atr(high, low, close, 10) / close.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_rel_atr_21d_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position relative to range, divided by ATR 21d ratio."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close) / (_atr(high, low, close, 21) / close.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_rel_atr_63d_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position relative to range, divided by ATR 63d ratio using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj) / (_atr(high * adj, low * adj, closeadj, 63) / closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_rel_atr_126d_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position relative to range, divided by ATR 126d ratio using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj) / (_atr(high * adj, low * adj, closeadj, 126) / closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_rel_atr_252d_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position relative to range, divided by ATR 252d ratio using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj) / (_atr(high * adj, low * adj, closeadj, 252) / closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_max_pos_5d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rolling maximum of the intraday close position."""
    res = _max(_close_in_range(high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_min_pos_5d_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day rolling minimum of the intraday close position."""
    res = _min(_close_in_range(high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_max_pos_21d_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling maximum of the intraday close position."""
    res = _max(_close_in_range(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_min_pos_21d_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling minimum of the intraday close position."""
    res = _min(_close_in_range(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_max_pos_63d_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling maximum of the intraday close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _max(_close_in_range(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_min_pos_63d_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling minimum of the intraday close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _min(_close_in_range(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_std_pos_21d_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling standard deviation of the intraday close position."""
    res = _std(_close_in_range(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_std_pos_63d_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling standard deviation of the intraday close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _std(_close_in_range(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_norm_std_21d_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday close position normalized by its 21-day standard deviation."""
    pos = _close_in_range(high, low, close)
    res = pos / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_norm_std_63d_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Intraday close position normalized by its 63-day standard deviation using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(high * adj, low * adj, closeadj)
    res = pos / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_sma_21d_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the 5-day close position."""
    res = _sma(_close_in_range(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_10d_sma_21d_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the 10-day close position."""
    res = _sma(_close_in_range(_max(high, 10), _min(low, 10), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_sma_21d_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the 21-day close position."""
    res = _sma(_close_in_range(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_sma_21d_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of the 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_sma_21d_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of the 126-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_252d_sma_21d_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of the 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_ema_21d_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of the 5-day close position."""
    res = _ema(_close_in_range(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_ema_21d_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of the 21-day close position."""
    res = _ema(_close_in_range(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_ema_21d_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of the 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_ema_21d_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of the 126-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_252d_ema_21d_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of the 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_z_21d_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of the 5-day close position."""
    pos = _close_in_range(_max(high, 5), _min(low, 5), close)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_10d_z_21d_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of the 10-day close position."""
    pos = _close_in_range(_max(high, 10), _min(low, 10), close)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_z_21d_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of the 21-day close position."""
    pos = _close_in_range(_max(high, 21), _min(low, 21), close)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_z_21d_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of the 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_z_21d_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of the 126-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_252d_z_21d_v051_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of the 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_norm_atr_21d_v052_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day close position normalized by 21-day ATR."""
    pos = _close_in_range(_max(high, 5), _min(low, 5), close)
    atr = _atr(high, low, close, 21)
    res = pos / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_10d_norm_atr_21d_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day close position normalized by 21-day ATR."""
    pos = _close_in_range(_max(high, 10), _min(low, 10), close)
    atr = _atr(high, low, close, 21)
    res = pos / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)


def f09cpwr_f09_close_position_within_range_pos_63d_norm_atr_63d_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day close position normalized by 63-day ATR using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    atr = _atr(high * adj, low * adj, closeadj, 63)
    res = pos / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_norm_atr_126d_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """126-day close position normalized by 126-day ATR using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj)
    atr = _atr(high * adj, low * adj, closeadj, 126)
    res = pos / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_252d_norm_atr_252d_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """252-day close position normalized by 252-day ATR using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj)
    atr = _atr(high * adj, low * adj, closeadj, 252)
    res = pos / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_sma_21d_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the 5-day midpoint position."""
    res = _sma(_close_relative_mid(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_10d_sma_21d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the 10-day midpoint position."""
    res = _sma(_close_relative_mid(_max(high, 10), _min(low, 10), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_21d_sma_21d_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of the 21-day midpoint position."""
    res = _sma(_close_relative_mid(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_sma_21d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of the 63-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_126d_sma_21d_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of the 126-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_relative_mid(_max(high * adj, 126), _min(low * adj, 126), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_252d_sma_21d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of the 252-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_relative_mid(_max(high * adj, 252), _min(low * adj, 252), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_ema_21d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of the 5-day midpoint position."""
    res = _ema(_close_relative_mid(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_21d_ema_21d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of the 21-day midpoint position."""
    res = _ema(_close_relative_mid(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_ema_21d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of the 63-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_126d_ema_21d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of the 126-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_relative_mid(_max(high * adj, 126), _min(low * adj, 126), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_252d_ema_21d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of the 252-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_relative_mid(_max(high * adj, 252), _min(low * adj, 252), closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_z_21d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of the 5-day midpoint position."""
    pos = _close_relative_mid(_max(high, 5), _min(low, 5), close)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_10d_z_21d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of the 10-day midpoint position."""
    pos = _close_relative_mid(_max(high, 10), _min(low, 10), close)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_21d_z_21d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of the 21-day midpoint position."""
    pos = _close_relative_mid(_max(high, 21), _min(low, 21), close)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_z_21d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of the 63-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_126d_z_21d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of the 126-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_relative_mid(_max(high * adj, 126), _min(low * adj, 126), closeadj)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_252d_z_21d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day Z-score of the 252-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_relative_mid(_max(high * adj, 252), _min(low * adj, 252), closeadj)
    res = (pos - _sma(pos, 21)) / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_max_21d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day max of the 5-day close position."""
    res = _max(_close_in_range(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f09cpwr_") and f.endswith("_signal")]

F09_CLOSE_POSITION_WITHIN_RANGE_BASE_001_075 = {
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
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F09_CLOSE_POSITION_WITHIN_RANGE_BASE_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
