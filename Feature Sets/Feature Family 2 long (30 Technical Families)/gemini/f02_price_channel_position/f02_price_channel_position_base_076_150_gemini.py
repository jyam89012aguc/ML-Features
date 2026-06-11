# f02_price_channel_position_base_076_150_gemini.py

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

# --- Features 076 - 077: Donchian Breakout Low (Continued) ---

def f02pc_f02_price_channel_position_donchian_breakout_low_252d_base_v076_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _min(low_adj, 252).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _min(low * adj, 252).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_donchian_breakout_low_504d_base_v077_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, _min(low_adj, 504).shift(1))
    adj = closeadj / close.replace(0, np.nan)
    res = _channel_breakout(closeadj, _min(low * adj, 504).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 078 - 084: Bollinger Band Position (1.5 std) ---

def f02pc_f02_price_channel_position_bb_pos_1_5std_5d_base_v078_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 1.5*std, ma + 1.5*std)
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = _channel_pos(close, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_10d_base_v079_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 1.5*std, ma + 1.5*std)
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = _channel_pos(close, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_21d_base_v080_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 1.5*std, ma + 1.5*std)
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = _channel_pos(close, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_63d_base_v081_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*std, ma + 1.5*std)
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_126d_base_v082_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*std, ma + 1.5*std)
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_252d_base_v083_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*std, ma + 1.5*std)
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_pos_1_5std_504d_base_v084_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*std, ma + 1.5*std)
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma - 1.5 * std, ma + 1.5 * std)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 085 - 091: Bollinger Band Width (1.5 std) ---

def f02pc_f02_price_channel_position_bb_width_1_5std_5d_base_v085_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = close.rolling(5, min_periods=5).std()
    ma = _sma(close, 5)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_10d_base_v086_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = close.rolling(10, min_periods=5).std()
    ma = _sma(close, 10)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_21d_base_v087_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = close.rolling(21, min_periods=5).std()
    ma = _sma(close, 21)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_63d_base_v088_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_126d_base_v089_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_252d_base_v090_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_width_1_5std_504d_base_v091_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*std, ma + 1.5*std, ma)
    std = closeadj.rolling(504, min_periods=5).std()
    ma = _sma(closeadj, 504)
    res = _channel_width(ma - 1.5 * std, ma + 1.5 * std, ma)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 092 - 098: Keltner Channel Position (1.5 ATR) ---

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_5d_base_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 1.5*atr, ma + 1.5*atr)
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = _channel_pos(close, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_10d_base_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 1.5*atr, ma + 1.5*atr)
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = _channel_pos(close, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_21d_base_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma - 1.5*atr, ma + 1.5*atr)
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = _channel_pos(close, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_63d_base_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*atr, ma + 1.5*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_126d_base_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*atr, ma + 1.5*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_252d_base_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*atr, ma + 1.5*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_pos_1_5atr_504d_base_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma - 1.5*atr, ma + 1.5*atr)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma - 1.5 * atr, ma + 1.5 * atr)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 099 - 105: Keltner Width (1.5 ATR) ---

def f02pc_f02_price_channel_position_keltner_width_1_5atr_5d_base_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    atr = _atr(high, low, close, 5)
    ma = _sma(close, 5)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_10d_base_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    atr = _atr(high, low, close, 10)
    ma = _sma(close, 10)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_21d_base_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    atr = _atr(high, low, close, 21)
    ma = _sma(close, 21)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_63d_base_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_126d_base_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 126)
    ma = _sma(closeadj, 126)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_252d_base_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 252)
    ma = _sma(closeadj, 252)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_keltner_width_1_5atr_504d_base_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_width(ma - 1.5*atr, ma + 1.5*atr, ma)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr(h_adj, l_adj, closeadj, 504)
    ma = _sma(closeadj, 504)
    res = _channel_width(ma - 1.5 * atr, ma + 1.5 * atr, ma)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 106 - 112: SMA 10% Percentage Position ---

def f02pc_f02_price_channel_position_sma_10pct_pos_5d_base_v106_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.90, ma * 1.10)
    ma = _sma(close, 5)
    res = _channel_pos(close, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_10d_base_v107_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.90, ma * 1.10)
    ma = _sma(close, 10)
    res = _channel_pos(close, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_21d_base_v108_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ma * 0.90, ma * 1.10)
    ma = _sma(close, 21)
    res = _channel_pos(close, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_63d_base_v109_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    ma = _sma(closeadj, 63)
    res = _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_126d_base_v110_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    ma = _sma(closeadj, 126)
    res = _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_252d_base_v111_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    ma = _sma(closeadj, 252)
    res = _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma_10pct_pos_504d_base_v112_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    ma = _sma(closeadj, 504)
    res = _channel_pos(closeadj, ma * 0.90, ma * 1.10)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 113 - 119: EMA 5% Percentage Position ---

def f02pc_f02_price_channel_position_ema_5pct_pos_5d_base_v113_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ema * 0.95, ema * 1.05)
    ema = _ema(close, 5)
    res = _channel_pos(close, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_10d_base_v114_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ema * 0.95, ema * 1.05)
    ema = _ema(close, 10)
    res = _channel_pos(close, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_21d_base_v115_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close, ema * 0.95, ema * 1.05)
    ema = _ema(close, 21)
    res = _channel_pos(close, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_63d_base_v116_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    ema = _ema(closeadj, 63)
    res = _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_126d_base_v117_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    ema = _ema(closeadj, 126)
    res = _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_252d_base_v118_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    ema = _ema(closeadj, 252)
    res = _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_ema_5pct_pos_504d_base_v119_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    ema = _ema(closeadj, 504)
    res = _channel_pos(closeadj, ema * 0.95, ema * 1.05)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 120 - 126: Volatility Channel Position (Std relative to ATR) ---

def f02pc_f02_price_channel_position_vol_pos_5d_base_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close.rolling(5).std(), 0, _atr(high, low, close, 5))
    std = close.rolling(5, min_periods=5).std()
    atr = _atr(high, low, close, 5)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_10d_base_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close.rolling(10).std(), 0, _atr(high, low, close, 10))
    std = close.rolling(10, min_periods=5).std()
    atr = _atr(high, low, close, 10)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_21d_base_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(close.rolling(21).std(), 0, _atr(high, low, close, 21))
    std = close.rolling(21, min_periods=5).std()
    atr = _atr(high, low, close, 21)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_63d_base_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj.rolling(63).std(), 0, atr_adj)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(63, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 63)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_126d_base_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj.rolling(126).std(), 0, atr_adj)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(126, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 126)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_252d_base_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj.rolling(252).std(), 0, atr_adj)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(252, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 252)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_vol_pos_504d_base_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(closeadj.rolling(504).std(), 0, atr_adj)
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    std = closeadj.rolling(504, min_periods=5).std()
    atr = _atr(h_adj, l_adj, closeadj, 504)
    res = _channel_pos(std, pd.Series(0, index=std.index), atr)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 127 - 133: Channel Position of SMA(5) within SMA(W) +/- 2std ---

def f02pc_f02_price_channel_position_sma5_in_bb_5d_base_v127_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(close, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(close, 5)
    ma = _sma(close, 5)
    std = close.rolling(5, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_10d_base_v128_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(close, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(close, 5)
    ma = _sma(close, 10)
    std = close.rolling(10, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_21d_base_v129_signal(close: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(close, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(close, 5)
    ma = _sma(close, 21)
    std = close.rolling(21, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_63d_base_v130_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(closeadj, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 63)
    std = closeadj.rolling(63, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_126d_base_v131_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(closeadj, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 126)
    std = closeadj.rolling(126, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_252d_base_v132_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(closeadj, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 252)
    std = closeadj.rolling(252, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_sma5_in_bb_504d_base_v133_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(_sma(closeadj, 5), ma - 2*std, ma + 2*std)
    ma5 = _sma(closeadj, 5)
    ma = _sma(closeadj, 504)
    std = closeadj.rolling(504, min_periods=5).std()
    res = _channel_pos(ma5, ma - 2 * std, ma + 2 * std)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 134 - 140: Channel Position of High within Donchian(W) ---

def f02pc_f02_price_channel_position_high_in_donchian_5d_base_v134_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high, _min(low, 5), _max(high, 5))
    res = _channel_pos(high, _min(low, 5), _max(high, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_10d_base_v135_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high, _min(low, 10), _max(high, 10))
    res = _channel_pos(high, _min(low, 10), _max(high, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_21d_base_v136_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high, _min(low, 21), _max(high, 21))
    res = _channel_pos(high, _min(low, 21), _max(high, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_63d_base_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high_adj, _min(low_adj, 63), _max(high_adj, 63))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(h_adj, _min(l_adj, 63), _max(h_adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_126d_base_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high_adj, _min(low_adj, 126), _max(high_adj, 126))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(h_adj, _min(l_adj, 126), _max(h_adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_252d_base_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high_adj, _min(low_adj, 252), _max(high_adj, 252))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(h_adj, _min(l_adj, 252), _max(h_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_high_in_donchian_504d_base_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(high_adj, _min(low_adj, 504), _max(high_adj, 504))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(h_adj, _min(l_adj, 504), _max(h_adj, 504))
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 141 - 147: Channel Position of Low within Donchian(W) ---

def f02pc_f02_price_channel_position_low_in_donchian_5d_base_v141_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low, _min(low, 5), _max(high, 5))
    res = _channel_pos(low, _min(low, 5), _max(high, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_10d_base_v142_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low, _min(low, 10), _max(high, 10))
    res = _channel_pos(low, _min(low, 10), _max(high, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_21d_base_v143_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low, _min(low, 21), _max(high, 21))
    res = _channel_pos(low, _min(low, 21), _max(high, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_63d_base_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low_adj, _min(low_adj, 63), _max(high_adj, 63))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(l_adj, _min(l_adj, 63), _max(h_adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_126d_base_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low_adj, _min(low_adj, 126), _max(high_adj, 126))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(l_adj, _min(l_adj, 126), _max(h_adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_252d_base_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low_adj, _min(low_adj, 252), _max(high_adj, 252))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(l_adj, _min(l_adj, 252), _max(h_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_low_in_donchian_504d_base_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_pos(low_adj, _min(low_adj, 504), _max(high_adj, 504))
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _channel_pos(l_adj, _min(l_adj, 504), _max(h_adj, 504))
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 148 - 150: BB Breakout High ---

def f02pc_f02_price_channel_position_bb_breakout_high_63d_base_v148_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, (_sma(closeadj, 63) + 2 * closeadj.rolling(63).std()).shift(1))
    std = closeadj.rolling(63, min_periods=5).std()
    ma = _sma(closeadj, 63)
    res = _channel_breakout(closeadj, (ma + 2 * std).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_breakout_high_126d_base_v149_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, (_sma(closeadj, 126) + 2 * closeadj.rolling(126).std()).shift(1))
    std = closeadj.rolling(126, min_periods=5).std()
    ma = _sma(closeadj, 126)
    res = _channel_breakout(closeadj, (ma + 2 * std).shift(1))
    return res.replace([np.inf, -np.inf], np.nan)

def f02pc_f02_price_channel_position_bb_breakout_high_252d_base_v150_signal(closeadj: pd.Series) -> pd.Series:
    # Formula: _channel_breakout(closeadj, (_sma(closeadj, 252) + 2 * closeadj.rolling(252).std()).shift(1))
    std = closeadj.rolling(252, min_periods=5).std()
    ma = _sma(closeadj, 252)
    res = _channel_breakout(closeadj, (ma + 2 * std).shift(1))
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
    "f02pc_f02_price_channel_position_donchian_breakout_low_252d_base_v076_signal": ["low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_donchian_breakout_low_504d_base_v077_signal": ["low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_5d_base_v078_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_10d_base_v079_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_21d_base_v080_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_63d_base_v081_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_126d_base_v082_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_252d_base_v083_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_pos_1_5std_504d_base_v084_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_5d_base_v085_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_10d_base_v086_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_21d_base_v087_signal": ["close"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_63d_base_v088_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_126d_base_v089_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_252d_base_v090_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_width_1_5std_504d_base_v091_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_5d_base_v092_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_10d_base_v093_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_21d_base_v094_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_63d_base_v095_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_126d_base_v096_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_252d_base_v097_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_pos_1_5atr_504d_base_v098_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_5d_base_v099_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_10d_base_v100_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_21d_base_v101_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_63d_base_v102_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_126d_base_v103_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_252d_base_v104_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_keltner_width_1_5atr_504d_base_v105_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_5d_base_v106_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_10d_base_v107_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_21d_base_v108_signal": ["close"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_63d_base_v109_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_126d_base_v110_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_252d_base_v111_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_sma_10pct_pos_504d_base_v112_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_5d_base_v113_signal": ["close"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_10d_base_v114_signal": ["close"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_21d_base_v115_signal": ["close"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_63d_base_v116_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_126d_base_v117_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_252d_base_v118_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_ema_5pct_pos_504d_base_v119_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_vol_pos_5d_base_v120_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_vol_pos_10d_base_v121_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_vol_pos_21d_base_v122_signal": ["high", "low", "close"],
    "f02pc_f02_price_channel_position_vol_pos_63d_base_v123_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_vol_pos_126d_base_v124_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_vol_pos_252d_base_v125_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_vol_pos_504d_base_v126_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_sma5_in_bb_5d_base_v127_signal": ["close"],
    "f02pc_f02_price_channel_position_sma5_in_bb_10d_base_v128_signal": ["close"],
    "f02pc_f02_price_channel_position_sma5_in_bb_21d_base_v129_signal": ["close"],
    "f02pc_f02_price_channel_position_sma5_in_bb_63d_base_v130_signal": ["close", "closeadj"],
    "f02pc_f02_price_channel_position_sma5_in_bb_126d_base_v131_signal": ["close", "closeadj"],
    "f02pc_f02_price_channel_position_sma5_in_bb_252d_base_v132_signal": ["close", "closeadj"],
    "f02pc_f02_price_channel_position_sma5_in_bb_504d_base_v133_signal": ["close", "closeadj"],
    "f02pc_f02_price_channel_position_high_in_donchian_5d_base_v134_signal": ["high", "low"],
    "f02pc_f02_price_channel_position_high_in_donchian_10d_base_v135_signal": ["high", "low"],
    "f02pc_f02_price_channel_position_high_in_donchian_21d_base_v136_signal": ["high", "low"],
    "f02pc_f02_price_channel_position_high_in_donchian_63d_base_v137_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_high_in_donchian_126d_base_v138_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_high_in_donchian_252d_base_v139_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_high_in_donchian_504d_base_v140_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_low_in_donchian_5d_base_v141_signal": ["high", "low"],
    "f02pc_f02_price_channel_position_low_in_donchian_10d_base_v142_signal": ["high", "low"],
    "f02pc_f02_price_channel_position_low_in_donchian_21d_base_v143_signal": ["high", "low"],
    "f02pc_f02_price_channel_position_low_in_donchian_63d_base_v144_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_low_in_donchian_126d_base_v145_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_low_in_donchian_252d_base_v146_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_low_in_donchian_504d_base_v147_signal": ["high", "low", "close", "closeadj"],
    "f02pc_f02_price_channel_position_bb_breakout_high_63d_base_v148_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_breakout_high_126d_base_v149_signal": ["closeadj"],
    "f02pc_f02_price_channel_position_bb_breakout_high_252d_base_v150_signal": ["closeadj"],
}

F02_PRICE_CHANNEL_POSITION_REGISTRY_076_150 = {
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

assert len(F02_PRICE_CHANNEL_POSITION_REGISTRY_076_150) == 75
