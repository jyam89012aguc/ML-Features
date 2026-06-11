# f02_price_channel_position_slope_001_150_gemini.py
import pandas as pd
import numpy as np
def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _channel_pos(p, l, h): return (p - l) / (h - l).replace(0, np.nan)
def _channel_width(l, h, m): return (h - l) / m.abs().replace(0, np.nan)
def _channel_breakout(p, b): return (p - b) / b.abs().replace(0, np.nan)
def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)
def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)

def f02pc_f02_price_channel_position_donchian_pos_5d_slope_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_pos(close, _min(low, 5), _max(high, 5)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_10d_slope_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_pos(close, _min(low, 10), _max(high, 10)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_21d_slope_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_pos(close, _min(low, 21), _max(high, 21)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_63d_slope_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_pos(closeadj, _min(low * adj, 63), _max(high * adj, 63)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_126d_slope_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_pos(closeadj, _min(low * adj, 126), _max(high * adj, 126)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_252d_slope_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_pos(closeadj, _min(low * adj, 252), _max(high * adj, 252)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_pos_504d_slope_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_pos(closeadj, _min(low * adj, 504), _max(high * adj, 504)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_5d_slope_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_width(_min(low, 5), _max(high, 5), _sma(close, 5)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_10d_slope_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_width(_min(low, 10), _max(high, 10), _sma(close, 10)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_21d_slope_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_width(_min(low, 21), _max(high, 21), _sma(close, 21)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_63d_slope_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_width(_min(low * adj, 63), _max(high * adj, 63), _sma(closeadj, 63)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_126d_slope_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_width(_min(low * adj, 126), _max(high * adj, 126), _sma(closeadj, 126)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_252d_slope_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_width(_min(low * adj, 252), _max(high * adj, 252), _sma(closeadj, 252)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_width_504d_slope_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_width(_min(low * adj, 504), _max(high * adj, 504), _sma(closeadj, 504)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_5d_slope_v015_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma - 2 * std, ma + 2 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_10d_slope_v016_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma - 2 * std, ma + 2 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_21d_slope_v017_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma - 2 * std, ma + 2 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_63d_slope_v018_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma - 2 * std, ma + 2 * std).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_126d_slope_v019_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma - 2 * std, ma + 2 * std).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_252d_slope_v020_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma - 2 * std, ma + 2 * std).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_504d_slope_v021_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma - 2 * std, ma + 2 * std).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_5d_slope_v022_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_10d_slope_v023_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_21d_slope_v024_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_63d_slope_v025_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_126d_slope_v026_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_252d_slope_v027_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_504d_slope_v028_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = (_channel_width(ma - 2 * std, ma + 2 * std, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_5d_slope_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma - 2 * atr, ma + 2 * atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_10d_slope_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma - 2 * atr, ma + 2 * atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_21d_slope_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma - 2 * atr, ma + 2 * atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_63d_slope_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_126d_slope_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_252d_slope_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_504d_slope_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma - 2 * atr, ma + 2 * atr).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_5d_slope_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_10d_slope_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_21d_slope_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_63d_slope_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_126d_slope_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_252d_slope_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_504d_slope_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = (_channel_width(ma - 2 * atr, ma + 2 * atr, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_5d_slope_v043_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma * 0.99, ma * 1.01).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_10d_slope_v044_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma * 0.99, ma * 1.01).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_21d_slope_v045_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma * 0.99, ma * 1.01).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_63d_slope_v046_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma * 0.99, ma * 1.01).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_126d_slope_v047_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma * 0.99, ma * 1.01).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_252d_slope_v048_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma * 0.99, ma * 1.01).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_1pct_pos_504d_slope_v049_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma * 0.99, ma * 1.01).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_5d_slope_v050_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma * 0.95, ma * 1.05).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_10d_slope_v051_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma * 0.95, ma * 1.05).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_21d_slope_v052_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma * 0.95, ma * 1.05).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_63d_slope_v053_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma * 0.95, ma * 1.05).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_126d_slope_v054_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma * 0.95, ma * 1.05).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_252d_slope_v055_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma * 0.95, ma * 1.05).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_5pct_pos_504d_slope_v056_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma * 0.95, ma * 1.05).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_5d_slope_v057_signal(close: pd.Series) -> pd.Series:
    ema = _ema(close, 5)
    res = (_channel_pos(close, ema * 0.98, ema * 1.02).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_10d_slope_v058_signal(close: pd.Series) -> pd.Series:
    ema = _ema(close, 10)
    res = (_channel_pos(close, ema * 0.98, ema * 1.02).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_21d_slope_v059_signal(close: pd.Series) -> pd.Series:
    ema = _ema(close, 21)
    res = (_channel_pos(close, ema * 0.98, ema * 1.02).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_63d_slope_v060_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 63)
    res = (_channel_pos(closeadj, ema * 0.98, ema * 1.02).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_126d_slope_v061_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 126)
    res = (_channel_pos(closeadj, ema * 0.98, ema * 1.02).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_252d_slope_v062_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 252)
    res = (_channel_pos(closeadj, ema * 0.98, ema * 1.02).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_2pct_pos_504d_slope_v063_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 504)
    res = (_channel_pos(closeadj, ema * 0.98, ema * 1.02).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_5d_slope_v064_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_breakout(close, _max(high, 5).shift(1)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_10d_slope_v065_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_breakout(close, _max(high, 10).shift(1)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_21d_slope_v066_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_breakout(close, _max(high, 21).shift(1)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_63d_slope_v067_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _max(high * adj, 63).shift(1)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_126d_slope_v068_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _max(high * adj, 126).shift(1)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_252d_slope_v069_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _max(high * adj, 252).shift(1)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_high_504d_slope_v070_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _max(high * adj, 504).shift(1)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_5d_slope_v071_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_breakout(close, _min(low, 5).shift(1)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_10d_slope_v072_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_breakout(close, _min(low, 10).shift(1)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_21d_slope_v073_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_channel_breakout(close, _min(low, 21).shift(1)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_63d_slope_v074_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _min(low * adj, 63).shift(1)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_126d_slope_v075_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _min(low * adj, 126).shift(1)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_252d_slope_v076_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _min(low * adj, 252).shift(1)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_504d_slope_v077_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_channel_breakout(closeadj, _min(low * adj, 504).shift(1)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_5d_slope_v078_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma - 1.5 * std, ma + 1.5 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_10d_slope_v079_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma - 1.5 * std, ma + 1.5 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_21d_slope_v080_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma - 1.5 * std, ma + 1.5 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_63d_slope_v081_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_126d_slope_v082_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_252d_slope_v083_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_504d_slope_v084_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_5d_slope_v085_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_10d_slope_v086_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_21d_slope_v087_signal(close: pd.Series) -> pd.Series:
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_63d_slope_v088_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_126d_slope_v089_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_252d_slope_v090_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_504d_slope_v091_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = (_channel_width(ma - 1.5 * std, ma + 1.5 * std, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_5d_slope_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_10d_slope_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_21d_slope_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_63d_slope_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_126d_slope_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_252d_slope_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_504d_slope_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_5d_slope_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_10d_slope_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_21d_slope_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_63d_slope_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_126d_slope_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_252d_slope_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_504d_slope_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = (_channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_5d_slope_v106_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 5)
    res = (_channel_pos(close, ma * 0.90, ma * 1.10).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_10d_slope_v107_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 10)
    res = (_channel_pos(close, ma * 0.90, ma * 1.10).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_21d_slope_v108_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 21)
    res = (_channel_pos(close, ma * 0.90, ma * 1.10).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_63d_slope_v109_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 63)
    res = (_channel_pos(closeadj, ma * 0.90, ma * 1.10).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_126d_slope_v110_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 126)
    res = (_channel_pos(closeadj, ma * 0.90, ma * 1.10).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_252d_slope_v111_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    res = (_channel_pos(closeadj, ma * 0.90, ma * 1.10).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_504d_slope_v112_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 504)
    res = (_channel_pos(closeadj, ma * 0.90, ma * 1.10).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_5d_slope_v113_signal(close: pd.Series) -> pd.Series:
    ema = _ema(close, 5)
    res = (_channel_pos(close, ema * 0.95, ema * 1.05).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_10d_slope_v114_signal(close: pd.Series) -> pd.Series:
    ema = _ema(close, 10)
    res = (_channel_pos(close, ema * 0.95, ema * 1.05).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_21d_slope_v115_signal(close: pd.Series) -> pd.Series:
    ema = _ema(close, 21)
    res = (_channel_pos(close, ema * 0.95, ema * 1.05).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_63d_slope_v116_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 63)
    res = (_channel_pos(closeadj, ema * 0.95, ema * 1.05).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_126d_slope_v117_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 126)
    res = (_channel_pos(closeadj, ema * 0.95, ema * 1.05).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_252d_slope_v118_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 252)
    res = (_channel_pos(closeadj, ema * 0.95, ema * 1.05).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_504d_slope_v119_signal(closeadj: pd.Series) -> pd.Series:
    ema = _ema(closeadj, 504)
    res = (_channel_pos(closeadj, ema * 0.95, ema * 1.05).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_5d_slope_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    std = close.rolling(5, min_periods=5).std()
    atr = _atr(high, low, close, 5)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_10d_slope_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    std = close.rolling(10, min_periods=5).std()
    atr = _atr(high, low, close, 10)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_21d_slope_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    std = close.rolling(21, min_periods=5).std()
    atr = _atr(high, low, close, 21)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_63d_slope_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(63, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 63)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_126d_slope_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(126, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 126)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_252d_slope_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(252, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 252)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_504d_slope_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(504, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 504)
    res = (_channel_pos(std, pd.Series(0, index=std.index), atr).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_5d_slope_v127_signal(close: pd.Series) -> pd.Series:
    ma5 = _sma(close, 5)
    ma = _sma(close, 5)
    std = close.rolling(5, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_10d_slope_v128_signal(close: pd.Series) -> pd.Series:
    ma5 = _sma(close, 5)
    ma = _sma(close, 10)
    std = close.rolling(10, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_21d_slope_v129_signal(close: pd.Series) -> pd.Series:
    ma5 = _sma(close, 5)
    ma = _sma(close, 21)
    std = close.rolling(21, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_63d_slope_v130_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 63)
    std = closeadj.rolling(63, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_126d_slope_v131_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 126)
    std = closeadj.rolling(126, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_252d_slope_v132_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 252)
    std = closeadj.rolling(252, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_504d_slope_v133_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 504)
    std = closeadj.rolling(504, min_periods=5).std()
    res = (_channel_pos(ma5, ma - 2 * std, ma + 2 * std).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_5d_slope_v134_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (_channel_pos(high, _min(low, 5), _max(high, 5)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_10d_slope_v135_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (_channel_pos(high, _min(low, 10), _max(high, 10)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_21d_slope_v136_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (_channel_pos(high, _min(low, 21), _max(high, 21)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_63d_slope_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(h_adj, _min(l_adj, 63), _max(h_adj, 63)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_126d_slope_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(h_adj, _min(l_adj, 126), _max(h_adj, 126)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_252d_slope_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(h_adj, _min(l_adj, 252), _max(h_adj, 252)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_504d_slope_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(h_adj, _min(l_adj, 504), _max(h_adj, 504)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_5d_slope_v141_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (_channel_pos(low, _min(low, 5), _max(high, 5)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_10d_slope_v142_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (_channel_pos(low, _min(low, 10), _max(high, 10)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_21d_slope_v143_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (_channel_pos(low, _min(low, 21), _max(high, 21)).pct_change(5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_63d_slope_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(l_adj, _min(l_adj, 63), _max(h_adj, 63)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_126d_slope_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(l_adj, _min(l_adj, 126), _max(h_adj, 126)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_252d_slope_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(l_adj, _min(l_adj, 252), _max(h_adj, 252)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_504d_slope_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_channel_pos(l_adj, _min(l_adj, 504), _max(h_adj, 504)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_breakout_high_63d_slope_v148_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = (_channel_breakout(closeadj, (ma + 2 * std).shift(1)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_breakout_high_126d_slope_v149_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = (_channel_breakout(closeadj, (ma + 2 * std).shift(1)).pct_change(21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_breakout_high_252d_slope_v150_signal(closeadj: pd.Series) -> pd.Series:
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = (_channel_breakout(closeadj, (ma + 2 * std).shift(1)).pct_change(63))
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

SLOPE_NAMES = [f for f in globals() if f.startswith("f02pc_") and f.endswith("_signal")]

F02_PRICE_CHANNEL_POSITION_SLOPE_REGISTRY_001_150 = {
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
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F02_PRICE_CHANNEL_POSITION_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("slope OK")
