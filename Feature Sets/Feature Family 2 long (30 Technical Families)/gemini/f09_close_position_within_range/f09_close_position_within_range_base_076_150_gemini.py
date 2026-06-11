# f09_close_position_within_range_base_076_150_gemini.py
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

# --- Feature Functions 076-150 ---

def f09cpwr_f09_close_position_within_range_pos_5d_min_21d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day min of the 5-day close position."""
    res = _min(_close_in_range(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_10d_max_21d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day max of the 10-day close position."""
    res = _max(_close_in_range(_max(high, 10), _min(low, 10), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_10d_min_21d_v078_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day min of the 10-day close position."""
    res = _min(_close_in_range(_max(high, 10), _min(low, 10), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_v079_signal(close: pd.Series) -> pd.Series:
    """Close position within 20-day Bollinger Bands (2 std)."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_50d_v080_signal(closeadj: pd.Series) -> pd.Series:
    """Close position within 50-day Bollinger Bands (2 std) using adjusted prices."""
    ma = _sma(closeadj, 50)
    std = _std(closeadj, 50)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, closeadj)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_mid_20d_v081_signal(close: pd.Series) -> pd.Series:
    """Close position relative to midpoint of 20-day Bollinger Bands."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_relative_mid(ma + 2 * std, ma - 2 * std, close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_20d_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within 20-day Keltner Channel (2 ATR)."""
    ma = _sma(close, 20)
    atr = _atr(high, low, close, 20)
    res = _close_in_range(ma + 2 * atr, ma - 2 * atr, close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_50d_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Close position within 50-day Keltner Channel (2 ATR) using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    ma = _sma(closeadj, 50)
    atr = _atr(high * adj, low * adj, closeadj, 50)
    res = _close_in_range(ma + 2 * atr, ma - 2 * atr, closeadj)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_mid_20d_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position relative to midpoint of 20-day Keltner Channel."""
    ma = _sma(close, 20)
    atr = _atr(high, low, close, 20)
    res = _close_relative_mid(ma + 2 * atr, ma - 2 * atr, close)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_norm_range_63d_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day close position normalized by the 63-day range height."""
    pos = _close_in_range(_max(high, 21), _min(low, 21), close)
    range_63 = (_max(high, 63) - _min(low, 63)).replace(0, np.nan)
    res = pos * (close / range_63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_vs_21d_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day close position to 21-day close position."""
    pos5 = _close_in_range(_max(high, 5), _min(low, 5), close)
    pos21 = _close_in_range(_max(high, 21), _min(low, 21), close).replace(0, np.nan)
    res = pos5 / pos21
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_vs_63d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of 21-day close position to 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos21 = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    pos63 = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj).replace(0, np.nan)
    res = pos21 / pos63
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_sma_5d_pos_5d_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day SMA of 5-day close position."""
    res = _sma(_close_in_range(_max(high, 5), _min(low, 5), close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_sma_10d_pos_10d_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day SMA of 10-day close position."""
    res = _sma(_close_in_range(_max(high, 10), _min(low, 10), close), 10)
    return res.replace([np.inf, -np.inf], np.nan)


def f09cpwr_f09_close_position_within_range_sma_63d_pos_63d_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_sma_126d_pos_126d_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """126-day SMA of 126-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_sma_252d_pos_252d_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """252-day SMA of 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_ema_5d_pos_5d_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day EMA of 5-day close position."""
    res = _ema(_close_in_range(_max(high, 5), _min(low, 5), close), 5)
    return res.replace([np.inf, -np.inf], np.nan)


def f09cpwr_f09_close_position_within_range_ema_63d_pos_63d_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day EMA of 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_z_63d_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 5-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj)
    res = (pos - _sma(pos, 63)) / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_z_63d_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 21-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    res = (pos - _sma(pos, 63)) / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_z_63d_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = (pos - _sma(pos, 63)) / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_z_63d_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 5-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_relative_mid(_max(high * adj, 5), _min(low * adj, 5), closeadj)
    res = (pos - _sma(pos, 63)) / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_21d_z_63d_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 21-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_relative_mid(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    res = (pos - _sma(pos, 63)) / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_z_63d_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 63-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = (pos - _sma(pos, 63)) / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_norm_atr_63d_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """5-day close position normalized by 63-day ATR using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj)
    atr = _atr(high * adj, low * adj, closeadj, 63)
    res = pos / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_norm_atr_63d_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day close position normalized by 63-day ATR using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    atr = _atr(high * adj, low * adj, closeadj, 63)
    res = pos / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)


def f09cpwr_f09_close_position_within_range_intraday_pos_sma_63d_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of intraday close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_mid_sma_21d_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of intraday midpoint position."""
    res = _sma(_close_relative_mid(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_mid_sma_63d_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of intraday midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_relative_mid(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_std_21d_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling standard deviation of 5-day close position."""
    res = _std(_close_in_range(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_std_21d_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling standard deviation of 21-day close position."""
    res = _std(_close_in_range(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_std_63d_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling standard deviation of 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _std(_close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_skew_63d_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling skewness of 5-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj)
    res = pos.rolling(63, min_periods=63).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_skew_63d_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling skewness of 21-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    res = pos.rolling(63, min_periods=63).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_kurt_63d_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of 5-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj)
    res = pos.rolling(63, min_periods=63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_kurt_63d_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day rolling kurtosis of 21-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    res = pos.rolling(63, min_periods=63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)





def f09cpwr_f09_close_position_within_range_pos_5d_norm_std_21d_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day close position normalized by its 21-day standard deviation."""
    pos = _close_in_range(_max(high, 5), _min(low, 5), close)
    res = pos / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_norm_std_21d_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day close position normalized by its 21-day standard deviation."""
    pos = _close_in_range(_max(high, 21), _min(low, 21), close)
    res = pos / _std(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_norm_std_63d_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day close position normalized by its 63-day standard deviation using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = pos / _std(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_sma_21d_v123_signal(close: pd.Series) -> pd.Series:
    """21-day SMA of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _sma(_close_in_range(ma + 2 * std, ma - 2 * std, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_50d_sma_21d_v124_signal(closeadj: pd.Series) -> pd.Series:
    """21-day SMA of 50-day BB position using adjusted prices."""
    ma = _sma(closeadj, 50)
    std = _std(closeadj, 50)
    res = _sma(_close_in_range(ma + 2 * std, ma - 2 * std, closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_20d_sma_21d_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 20-day Keltner position."""
    ma = _sma(close, 20)
    atr = _atr(high, low, close, 20)
    res = _sma(_close_in_range(ma + 2 * atr, ma - 2 * atr, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_50d_sma_21d_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of 50-day Keltner position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    ma = _sma(closeadj, 50)
    atr = _atr(high * adj, low * adj, closeadj, 50)
    res = _sma(_close_in_range(ma + 2 * atr, ma - 2 * atr, closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_ema_21d_v127_signal(close: pd.Series) -> pd.Series:
    """21-day EMA of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _ema(_close_in_range(ma + 2 * std, ma - 2 * std, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_50d_ema_21d_v128_signal(closeadj: pd.Series) -> pd.Series:
    """21-day EMA of 50-day BB position using adjusted prices."""
    ma = _sma(closeadj, 50)
    std = _std(closeadj, 50)
    res = _ema(_close_in_range(ma + 2 * std, ma - 2 * std, closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_20d_ema_21d_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 20-day Keltner position."""
    ma = _sma(close, 20)
    atr = _atr(high, low, close, 20)
    res = _ema(_close_in_range(ma + 2 * atr, ma - 2 * atr, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_50d_ema_21d_v130_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of 50-day Keltner position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    ma = _sma(closeadj, 50)
    atr = _atr(high * adj, low * adj, closeadj, 50)
    res = _ema(_close_in_range(ma + 2 * atr, ma - 2 * atr, closeadj), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_vs_sma_21d_v131_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day close position relative to its 21-day SMA."""
    pos = _close_in_range(_max(high, 5), _min(low, 5), close)
    res = pos / _sma(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_vs_sma_21d_v132_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day close position relative to its 21-day SMA."""
    pos = _close_in_range(_max(high, 21), _min(low, 21), close)
    res = pos / _sma(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_vs_sma_63d_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day close position relative to its 63-day SMA using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = pos / _sma(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_vs_ema_21d_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day close position relative to its 21-day EMA."""
    pos = _close_in_range(_max(high, 5), _min(low, 5), close)
    res = pos / _ema(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_vs_ema_21d_v135_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day close position relative to its 21-day EMA."""
    pos = _close_in_range(_max(high, 21), _min(low, 21), close)
    res = pos / _ema(pos, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_vs_ema_63d_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day close position relative to its 63-day EMA using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    res = pos / _ema(pos, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_max_mid_5d_21d_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day max of 5-day midpoint position."""
    res = _max(_close_relative_mid(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_min_mid_5d_21d_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day min of 5-day midpoint position."""
    res = _min(_close_relative_mid(_max(high, 5), _min(low, 5), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_max_mid_21d_21d_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day max of 21-day midpoint position."""
    res = _max(_close_relative_mid(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_min_mid_21d_21d_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day min of 21-day midpoint position."""
    res = _min(_close_relative_mid(_max(high, 21), _min(low, 21), close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_max_mid_63d_63d_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day max of 63-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _max(_close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_min_mid_63d_63d_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day min of 63-day midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _min(_close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_vs_252d_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of 5-day close position to 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos5 = _close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj)
    pos252 = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj).replace(0, np.nan)
    res = pos5 / pos252
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_vs_252d_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of 21-day close position to 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos21 = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    pos252 = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj).replace(0, np.nan)
    res = pos21 / pos252
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_vs_252d_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of 63-day close position to 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos63 = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj)
    pos252 = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj).replace(0, np.nan)
    res = pos63 / pos252
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_vs_252d_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of 126-day close position to 252-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos126 = _close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj)
    pos252 = _close_in_range(_max(high * adj, 252), _min(low * adj, 252), closeadj).replace(0, np.nan)
    res = pos126 / pos252
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_21d_sma_21d_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day z-score of intraday close position."""
    res = _sma(_close_range_z(high, low, close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_63d_sma_21d_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day SMA of 63-day z-score of intraday close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_range_z(high * adj, low * adj, closeadj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_21d_ema_21d_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day z-score of intraday close position."""
    res = _ema(_close_range_z(high, low, close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_63d_ema_21d_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day EMA of 63-day z-score of intraday close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_range_z(high * adj, low * adj, closeadj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f09cpwr_") and f.endswith("_signal")]

F09_CLOSE_POSITION_WITHIN_RANGE_BASE_076_150 = {
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
    for n, c in F09_CLOSE_POSITION_WITHIN_RANGE_BASE_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
