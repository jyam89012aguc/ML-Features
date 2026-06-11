# f02_price_channel_position_base_001_075_gemini.py

import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _z(s, w):
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _min(s, w):
    return s.rolling(w, min_periods=min(w, 5)).min()

def _max(s, w):
    return s.rolling(w, min_periods=min(w, 5)).max()

def _channel_pos(price, low, high):
    return (price - low) / (high - low).replace(0, np.nan)

def _channel_width(low, high, mid):
    return (high - low) / mid.abs().replace(0, np.nan)

def _channel_breakout(price, boundary):
    return (price - boundary) / boundary.abs().replace(0, np.nan)

def _tr(h, l, c):
    c_prev = c.shift(1)
    return pd.concat([h - l, (h - c_prev).abs(), (l - c_prev).abs()], axis=1).max(axis=1)

def _atr(h, l, c, w):
    return _sma(_tr(h, l, c), w)

# --- Features 001 - 007: Donchian Position ---

def f02pc_f02_price_channel_position_donchian_pos_5d_base_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, _min(low, 5), _max(high, 5))
    res = _channel_pos(close, _min(low, 5), _max(high, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_10d_base_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, _min(low, 10), _max(high, 10))
    res = _channel_pos(close, _min(low, 10), _max(high, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_21d_base_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, _min(low, 21), _max(high, 21))
    res = _channel_pos(close, _min(low, 21), _max(high, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_63d_base_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _min(low * (closeadj/close), 63), _max(high * (closeadj/close), 63))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_pos(closeadj, _min(low * adj, 63), _max(high * adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_126d_base_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _min(low * (closeadj/close), 126), _max(high * (closeadj/close), 126))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_pos(closeadj, _min(low * adj, 126), _max(high * adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_252d_base_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _min(low * (closeadj/close), 252), _max(high * (closeadj/close), 252))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_pos(closeadj, _min(low * adj, 252), _max(high * adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_504d_base_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _min(low * (closeadj/close), 504), _max(high * (closeadj/close), 504))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_pos(closeadj, _min(low * adj, 504), _max(high * adj, 504))
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 008 - 014: Donchian Width ---

def f02pc_f02_price_channel_position_donchian_width_5d_base_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low, 5), _max(high, 5), _sma(close, 5))
    res = _channel_width(_min(low, 5), _max(high, 5), _sma(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_10d_base_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low, 10), _max(high, 10), _sma(close, 10))
    res = _channel_width(_min(low, 10), _max(high, 10), _sma(close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_21d_base_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low, 21), _max(high, 21), _sma(close, 21))
    res = _channel_width(_min(low, 21), _max(high, 21), _sma(close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_63d_base_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low_adj, 63), _max(high_adj, 63), _sma(closeadj, 63))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_width(_min(low * adj, 63), _max(high * adj, 63), _sma(closeadj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_126d_base_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low_adj, 126), _max(high_adj, 126), _sma(closeadj, 126))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_width(_min(low * adj, 126), _max(high * adj, 126), _sma(closeadj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_252d_base_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low_adj, 252), _max(high_adj, 252), _sma(closeadj, 252))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_width(_min(low * adj, 252), _max(high * adj, 252), _sma(closeadj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_504d_base_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(_min(low_adj, 504), _max(high_adj, 504), _sma(closeadj, 504))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_width(_min(low * adj, 504), _max(high * adj, 504), _sma(closeadj, 504))
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 015 - 021: Bollinger Band Position (2.0 std) ---

def f02pc_f02_price_channel_position_bb_pos_5d_base_v015_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, _sma(close, 5) - 2 * close.rolling(5).std(), _sma(close, 5) + 2 * close.rolling(5).std())
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = _channel_pos(close, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_10d_base_v016_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, _sma(close, 10) - 2 * close.rolling(10).std(), _sma(close, 10) + 2 * close.rolling(10).std())
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = _channel_pos(close, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_21d_base_v017_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, _sma(close, 21) - 2 * close.rolling(21).std(), _sma(close, 21) + 2 * close.rolling(21).std())
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = _channel_pos(close, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_63d_base_v018_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _sma(closeadj, 63) - 2 * closeadj.rolling(63).std(), _sma(closeadj, 63) + 2 * closeadj.rolling(63).std())
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_126d_base_v019_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _sma(closeadj, 126) - 2 * closeadj.rolling(126).std(), _sma(closeadj, 126) + 2 * closeadj.rolling(126).std())
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_252d_base_v020_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _sma(closeadj, 252) - 2 * closeadj.rolling(252).std(), _sma(closeadj, 252) + 2 * closeadj.rolling(252).std())
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_504d_base_v021_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, _sma(closeadj, 504) - 2 * closeadj.rolling(504).std(), _sma(closeadj, 504) + 2 * closeadj.rolling(504).std())
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 022 - 028: Bollinger Band Width (2.0 std) ---

def f02pc_f02_price_channel_position_bb_width_5d_base_v022_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_10d_base_v023_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_21d_base_v024_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_63d_base_v025_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_126d_base_v026_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_252d_base_v027_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_504d_base_v028_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*std, ma + 2*std, ma)
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = _channel_width(ma - 2 * std, ma + 2 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 029 - 035: Keltner Channel Position (2.0 ATR) ---

def f02pc_f02_price_channel_position_keltner_pos_5d_base_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 2*atr, ma + 2*atr)
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = _channel_pos(close, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_10d_base_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 2*atr, ma + 2*atr)
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = _channel_pos(close, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_21d_base_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 2*atr, ma + 2*atr)
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = _channel_pos(close, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_63d_base_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 2*atr, ma + 2*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_126d_base_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 2*atr, ma + 2*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_252d_base_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 2*atr, ma + 2*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_504d_base_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 2*atr, ma + 2*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 036 - 042: Keltner Width (2.0 ATR) ---

def f02pc_f02_price_channel_position_keltner_width_5d_base_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_10d_base_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_21d_base_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_63d_base_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_126d_base_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_252d_base_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_504d_base_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 2*atr, ma + 2*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = _channel_width(ma - 2 * atr, ma + 2 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 043 - 049: SMA 1% Percentage Position ---

def f02pc_f02_price_channel_position_sma_1pct_pos_5d_base_v043_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.99, ma * 1.01)
    ma = _sma(close, 5)
    res = _channel_pos(close, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_10d_base_v044_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.99, ma * 1.01)
    ma = _sma(close, 10)
    res = _channel_pos(close, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_21d_base_v045_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.99, ma * 1.01)
    ma = _sma(close, 21)
    res = _channel_pos(close, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_63d_base_v046_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_126d_base_v047_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_252d_base_v048_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_504d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma * 0.99, ma * 1.01)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 050 - 056: SMA 5% Percentage Position ---

def f02pc_f02_price_channel_position_sma_5pct_pos_5d_base_v050_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.95, ma * 1.05)
    ma = _sma(close, 5)
    res = _channel_pos(close, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_10d_base_v051_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.95, ma * 1.05)
    ma = _sma(close, 10)
    res = _channel_pos(close, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_21d_base_v052_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.95, ma * 1.05)
    ma = _sma(close, 21)
    res = _channel_pos(close, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_63d_base_v053_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_126d_base_v054_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_252d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_504d_base_v056_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma * 0.95, ma * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 057 - 063: EMA 2% Percentage Position ---

def f02pc_f02_price_channel_position_ema_2pct_pos_5d_base_v057_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ema * 0.98, ema * 1.02)
    ema = _ema(close, 5)
    res = _channel_pos(close, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_10d_base_v058_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ema * 0.98, ema * 1.02)
    ema = _ema(close, 10)
    res = _channel_pos(close, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_21d_base_v059_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ema * 0.98, ema * 1.02)
    ema = _ema(close, 21)
    res = _channel_pos(close, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_63d_base_v060_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    ema = _ema(closeadj, 63)
    res = _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_126d_base_v061_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    ema = _ema(closeadj, 126)
    res = _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_252d_base_v062_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    ema = _ema(closeadj, 252)
    res = _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_504d_base_v063_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    ema = _ema(closeadj, 504)
    res = _channel_pos(closeadj, ema * 0.98, ema * 1.02)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 064 - 070: Donchian Breakout High ---

def f02pc_f02_price_channel_position_donchian_breakout_high_5d_base_v064_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(close, _max(high, 5).shift(1))
    res = _channel_breakout(close, _max(high, 5).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_10d_base_v065_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(close, _max(high, 10).shift(1))
    res = _channel_breakout(close, _max(high, 10).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_21d_base_v066_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(close, _max(high, 21).shift(1))
    res = _channel_breakout(close, _max(high, 21).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_63d_base_v067_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _max(high_adj, 63).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _max(high * adj, 63).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_126d_base_v068_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _max(high_adj, 126).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _max(high * adj, 126).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_252d_base_v069_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _max(high_adj, 252).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _max(high * adj, 252).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_504d_base_v070_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _max(high_adj, 504).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _max(high * adj, 504).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 071 - 075: Donchian Breakout Low ---

def f02pc_f02_price_channel_position_donchian_breakout_low_5d_base_v071_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(close, _min(low, 5).shift(1))
    res = _channel_breakout(close, _min(low, 5).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_10d_base_v072_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(close, _min(low, 10).shift(1))
    res = _channel_breakout(close, _min(low, 10).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_21d_base_v073_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(close, _min(low, 21).shift(1))
    res = _channel_breakout(close, _min(low, 21).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_63d_base_v074_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _min(low_adj, 63).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _min(low * adj, 63).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_126d_base_v075_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _min(low_adj, 126).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _min(low * adj, 126).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

# --- SilverDB schema/source metadata ---
SILVERDB_ACCESS = "read_only"
SOURCE_TABLE = "sep"
ENTITY_COLUMN = "ticker"
DATE_COLUMN = "date"
ORDER_BY = [ENTITY_COLUMN, DATE_COLUMN]
NO_FORWARD_LOOKING = True

SOURCE_COLUMNS = {
    "close": "sep.close",
    "closeadj": "sep.closeadj",
    "high": "sep.high",
    "low": "sep.low",
}

FEATURE_INPUTS = {
    "f02pc_f02_price_channel_position_donchian_pos_5d_base_v001_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_donchian_pos_10d_base_v002_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_donchian_pos_21d_base_v003_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_donchian_pos_63d_base_v004_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_pos_126d_base_v005_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_pos_252d_base_v006_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_pos_504d_base_v007_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_width_5d_base_v008_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_donchian_width_10d_base_v009_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_donchian_width_21d_base_v010_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_donchian_width_63d_base_v011_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_width_126d_base_v012_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_width_252d_base_v013_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_width_504d_base_v014_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_5d_base_v015_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_pos_10d_base_v016_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_pos_21d_base_v017_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_pos_63d_base_v018_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_126d_base_v019_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_252d_base_v020_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_504d_base_v021_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_5d_base_v022_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_width_10d_base_v023_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_width_21d_base_v024_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_width_63d_base_v025_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_126d_base_v026_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_252d_base_v027_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_504d_base_v028_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_5d_base_v029_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_pos_10d_base_v030_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_pos_21d_base_v031_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_pos_63d_base_v032_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_126d_base_v033_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_252d_base_v034_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_504d_base_v035_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_5d_base_v036_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_width_10d_base_v037_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_width_21d_base_v038_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_width_63d_base_v039_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_126d_base_v040_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_252d_base_v041_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_504d_base_v042_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_5d_base_v043_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_10d_base_v044_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_21d_base_v045_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_63d_base_v046_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_126d_base_v047_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_252d_base_v048_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_1pct_pos_504d_base_v049_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_5d_base_v050_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_10d_base_v051_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_21d_base_v052_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_63d_base_v053_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_126d_base_v054_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_252d_base_v055_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_5pct_pos_504d_base_v056_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_5d_base_v057_signal": ["close"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_10d_base_v058_signal": ["close"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_21d_base_v059_signal": ["close"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_63d_base_v060_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_126d_base_v061_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_252d_base_v062_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_2pct_pos_504d_base_v063_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_5d_base_v064_signal": ["high", "close"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_10d_base_v065_signal": ["high", "close"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_21d_base_v066_signal": ["high", "close"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_63d_base_v067_signal": ["high", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_126d_base_v068_signal": ["high", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_252d_base_v069_signal": ["high", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_high_504d_base_v070_signal": ["high", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_low_5d_base_v071_signal": ["low", "close"],
    "f02pc_f02_price_channel_position_donchian_breakout_low_10d_base_v072_signal": ["low", "close"],
    "f02pc_f02_price_channel_position_donchian_breakout_low_21d_base_v073_signal": ["low", "close"],
    "f02pc_f02_price_channel_position_donchian_breakout_low_63d_base_v074_signal": ["low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_low_126d_base_v075_signal": ["low", "close", "closeadj"],
}

F02_PRICE_CHANNEL_POSITION_REGISTRY_001_075 = {
    name: {
        "inputs": FEATURE_INPUTS[name],
        "source_table": SOURCE_TABLE,
        "source_columns": {col: SOURCE_COLUMNS[col] for col in FEATURE_INPUTS[name]},
        "entity_column": ENTITY_COLUMN,
        "date_column": DATE_COLUMN,
        "order_by": ORDER_BY,
        "no_forward_looking": NO_FORWARD_LOOKING,
        "func": globals()[name],
    }
    for name in FEATURE_INPUTS
}

assert len(F02_PRICE_CHANNEL_POSITION_REGISTRY_001_075) == 75
