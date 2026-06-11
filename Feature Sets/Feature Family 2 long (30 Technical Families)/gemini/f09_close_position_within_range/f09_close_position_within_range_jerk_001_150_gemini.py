# f09_close_position_within_range_jerk_001_150_gemini.py
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

# --- Jerk (ROC of ROC) Feature Functions 001-150 ---

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk (ROC of ROC) of intraday close position."""
    res = _close_in_range(high, low, close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_jerk_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day jerk of intraday close position."""
    res = _close_in_range(high, low, close).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_mid_5d_jerk_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of intraday midpoint position."""
    res = _close_relative_mid(high, low, close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 5-day Donchian close position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_5d_jerk_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 21-day Donchian close position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_21d_jerk_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day jerk of 63-day Donchian close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_126d_21d_jerk_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day jerk of 126-day Donchian close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 126), _min(low * adj, 126), closeadj).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_5d_jerk_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_21d_5d_jerk_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 21-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 21), _min(low, 21), close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_21d_jerk_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day jerk of 63-day Donchian midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_21d_5d_jerk_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 21-day close range z-score."""
    res = _close_range_z(high, low, close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_63d_21d_jerk_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day jerk of 63-day close range z-score using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_range_z(high * adj, low * adj, closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_5d_jerk_v013_signal(close: pd.Series) -> pd.Series:
    """5-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_50d_21d_jerk_v014_signal(closeadj: pd.Series) -> pd.Series:
    """21-day jerk of 50-day BB position using adjusted prices."""
    ma = _sma(closeadj, 50)
    std = _std(closeadj, 50)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, closeadj).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_20d_5d_jerk_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 20-day Keltner position."""
    ma = _sma(close, 20)
    atr = _atr(high, low, close, 20)
    res = _close_in_range(ma + 2 * atr, ma - 2 * atr, close).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_keltner_pos_50d_21d_jerk_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day jerk of 50-day Keltner position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    ma = _sma(closeadj, 50)
    atr = _atr(high * adj, low * adj, closeadj, 50)
    res = _close_in_range(ma + 2 * atr, ma - 2 * atr, closeadj).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_sma_21d_5d_jerk_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 21-day SMA of 5-day close position."""
    res = _sma(_close_in_range(_max(high, 5), _min(low, 5), close), 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_sma_21d_5d_jerk_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 21-day SMA of 21-day close position."""
    res = _sma(_close_in_range(_max(high, 21), _min(low, 21), close), 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_sma_21d_5d_jerk_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 21-day SMA of 5-day midpoint position."""
    res = _sma(_close_relative_mid(_max(high, 5), _min(low, 5), close), 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_sma_21d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 5-day jerk of intraday close position."""
    res = _sma(_close_in_range(high, low, close).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_sma_21d_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 5-day jerk of 5-day Donchian close position."""
    res = _sma(_close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_21d_5d_jerk_sma_21d_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 5-day jerk of 21-day close range z-score."""
    res = _sma(_close_range_z(high, low, close, 21).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_5d_jerk_sma_21d_v023_signal(close: pd.Series) -> pd.Series:
    """21-day SMA of 5-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _sma(_close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_ema_21d_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 5-day jerk of intraday close position."""
    res = _ema(_close_in_range(high, low, close).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_ema_21d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 5-day jerk of 5-day Donchian close position."""
    res = _ema(_close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_z_21d_5d_jerk_ema_21d_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 5-day jerk of 21-day close range z-score."""
    res = _ema(_close_range_z(high, low, close, 21).pct_change(5).pct_change(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_z_21d_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 5-day jerk of intraday close position."""
    jrk = _close_in_range(high, low, close).pct_change(5).pct_change(5)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_z_21d_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 5-day jerk of 5-day Donchian close position."""
    jrk = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_norm_atr_21d_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of intraday close position normalized by 21-day ATR."""
    jrk = _close_in_range(high, low, close).pct_change(5).pct_change(5)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_norm_atr_21d_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day jerk of 5-day Donchian close position normalized by 21-day ATR."""
    jrk = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_abs_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 5-day jerk of intraday close position."""
    res = _close_in_range(high, low, close).pct_change(5).pct_change(5).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_abs_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 5-day jerk of 5-day Donchian close position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_5d_jerk_abs_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 5-day jerk of 21-day Donchian close position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(5).pct_change(5).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_5d_jerk_abs_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 5-day jerk of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(5).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_5d_jerk_abs_v035_signal(close: pd.Series) -> pd.Series:
    """Absolute value of 5-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(5).pct_change(5).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_5d_jerk_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 10-day ROC of 5-day ROC of intraday position."""
    res = _close_in_range(high, low, close).pct_change(5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_10d_5d_jerk_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 10-day ROC of 5-day ROC of 5-day Donchian position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_10d_5d_jerk_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 10-day ROC of 5-day ROC of 21-day Donchian position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_10d_5d_jerk_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 10-day ROC of 5-day ROC of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_10d_5d_jerk_v040_signal(close: pd.Series) -> pd.Series:
    """Jerk calculated as 10-day ROC of 5-day ROC of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(5).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_5d_jerk_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of intraday position."""
    res = _close_in_range(high, low, close).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_5d_jerk_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 5-day Donchian position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_5d_jerk_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 21-day Donchian position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_5d_jerk_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_5d_jerk_v045_signal(close: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_21d_5d_jerk_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 63-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_21d_5d_jerk_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 63-day Donchian midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_50d_21d_5d_jerk_v048_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk calculated as 21-day ROC of 5-day ROC of 50-day BB position using adjusted prices."""
    ma = _sma(closeadj, 50)
    std = _std(closeadj, 50)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, closeadj).pct_change(5).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_sma_63d_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 5-day jerk of intraday position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(high * adj, low * adj, closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_sma_63d_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 5-day jerk of 5-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_5d_jerk_sma_63d_v051_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 5-day jerk of 21-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_5d_jerk_sma_63d_v052_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day SMA of 5-day jerk of 20-day BB position using adjusted prices."""
    ma = _sma(closeadj, 20)
    std = _std(closeadj, 20)
    res = _sma(_close_in_range(ma + 2 * std, ma - 2 * std, closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_ema_63d_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day EMA of 5-day jerk of intraday position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(high * adj, low * adj, closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_ema_63d_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day EMA of 5-day jerk of 5-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_5d_jerk_ema_63d_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day EMA of 5-day jerk of 21-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_5d_jerk_ema_63d_v056_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day EMA of 5-day jerk of 20-day BB position using adjusted prices."""
    ma = _sma(closeadj, 20)
    std = _std(closeadj, 20)
    res = _ema(_close_in_range(ma + 2 * std, ma - 2 * std, closeadj).pct_change(5).pct_change(5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_5d_jerk_z_63d_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 5-day jerk of intraday position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    jrk = _close_in_range(high * adj, low * adj, closeadj).pct_change(5).pct_change(5)
    res = (jrk - _sma(jrk, 63)) / _std(jrk, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_5d_jerk_z_63d_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 5-day jerk of 5-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    jrk = _close_in_range(_max(high * adj, 5), _min(low * adj, 5), closeadj).pct_change(5).pct_change(5)
    res = (jrk - _sma(jrk, 63)) / _std(jrk, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_5d_jerk_z_63d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 5-day jerk of 21-day Donchian position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    jrk = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj).pct_change(5).pct_change(5)
    res = (jrk - _sma(jrk, 63)) / _std(jrk, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_5d_jerk_z_63d_v060_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day Z-score of 5-day jerk of 20-day BB position using adjusted prices."""
    ma = _sma(closeadj, 20)
    std = _std(closeadj, 20)
    jrk = _close_in_range(ma + 2 * std, ma - 2 * std, closeadj).pct_change(5).pct_change(5)
    res = (jrk - _sma(jrk, 63)) / _std(jrk, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_jerk_sma_21d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 10-day jerk of intraday close position."""
    res = _sma(_close_in_range(high, low, close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_10d_jerk_sma_21d_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 10-day jerk of 5-day Donchian close position."""
    res = _sma(_close_in_range(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_10d_jerk_sma_21d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 10-day jerk of 21-day Donchian close position."""
    res = _sma(_close_in_range(_max(high, 21), _min(low, 21), close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_10d_jerk_sma_21d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 10-day jerk of 5-day Donchian midpoint position."""
    res = _sma(_close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_10d_jerk_sma_21d_v065_signal(close: pd.Series) -> pd.Series:
    """21-day SMA of 10-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _sma(_close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_jerk_ema_21d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 10-day jerk of intraday close position."""
    res = _ema(_close_in_range(high, low, close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_10d_jerk_ema_21d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 10-day jerk of 5-day Donchian close position."""
    res = _ema(_close_in_range(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_10d_jerk_ema_21d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 10-day jerk of 21-day Donchian close position."""
    res = _ema(_close_in_range(_max(high, 21), _min(low, 21), close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_10d_jerk_ema_21d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 10-day jerk of 5-day Donchian midpoint position."""
    res = _ema(_close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_10d_jerk_ema_21d_v070_signal(close: pd.Series) -> pd.Series:
    """21-day EMA of 10-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _ema(_close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(10).pct_change(10), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_jerk_z_21d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 10-day jerk of intraday close position."""
    jrk = _close_in_range(high, low, close).pct_change(10).pct_change(10)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_10d_jerk_z_21d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 10-day jerk of 5-day Donchian close position."""
    jrk = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_10d_jerk_z_21d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 10-day jerk of 21-day Donchian close position."""
    jrk = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(10).pct_change(10)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_10d_jerk_z_21d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 10-day jerk of 5-day Donchian midpoint position."""
    jrk = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_10d_jerk_z_21d_v075_signal(close: pd.Series) -> pd.Series:
    """21-day Z-score of 10-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    jrk = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(10).pct_change(10)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_jerk_norm_atr_21d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day jerk of intraday close position normalized by 21-day ATR."""
    jrk = _close_in_range(high, low, close).pct_change(10).pct_change(10)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_10d_jerk_norm_atr_21d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day jerk of 5-day Donchian close position normalized by 21-day ATR."""
    jrk = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_10d_jerk_norm_atr_21d_v078_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day jerk of 21-day Donchian close position normalized by 21-day ATR."""
    jrk = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(10).pct_change(10)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_10d_jerk_norm_atr_21d_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day jerk of 5-day Donchian midpoint position normalized by 21-day ATR."""
    jrk = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_10d_jerk_norm_atr_21d_v080_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day jerk of 20-day BB position normalized by 21-day ATR."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    jrk = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(10).pct_change(10)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_10d_jerk_abs_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 10-day jerk of intraday close position."""
    res = _close_in_range(high, low, close).pct_change(10).pct_change(10).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_10d_jerk_abs_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 10-day jerk of 5-day Donchian close position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_10d_jerk_abs_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 10-day jerk of 21-day Donchian close position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(10).pct_change(10).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_10d_jerk_abs_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 10-day jerk of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(10).pct_change(10).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_10d_jerk_abs_v085_signal(close: pd.Series) -> pd.Series:
    """Absolute value of 10-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(10).pct_change(10).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_jerk_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of intraday close position."""
    res = _close_in_range(high, low, close).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_jerk_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of 5-day Donchian close position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_jerk_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of 21-day Donchian close position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_jerk_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_jerk_v090_signal(close: pd.Series) -> pd.Series:
    """21-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_63d_63d_jerk_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day jerk of 63-day Donchian close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_63d_63d_jerk_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """63-day jerk of 63-day Donchian midpoint position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _close_relative_mid(_max(high * adj, 63), _min(low * adj, 63), closeadj).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_50d_63d_jerk_v093_signal(closeadj: pd.Series) -> pd.Series:
    """63-day jerk of 50-day BB position using adjusted prices."""
    ma = _sma(closeadj, 50)
    std = _std(closeadj, 50)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, closeadj).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_jerk_sma_21d_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day jerk of intraday close position."""
    res = _sma(_close_in_range(high, low, close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_jerk_sma_21d_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day jerk of 5-day Donchian close position."""
    res = _sma(_close_in_range(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_jerk_sma_21d_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day jerk of 21-day Donchian close position."""
    res = _sma(_close_in_range(_max(high, 21), _min(low, 21), close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_jerk_sma_21d_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day jerk of 5-day Donchian midpoint position."""
    res = _sma(_close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_jerk_sma_21d_v098_signal(close: pd.Series) -> pd.Series:
    """21-day SMA of 21-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _sma(_close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_jerk_ema_21d_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day jerk of intraday close position."""
    res = _ema(_close_in_range(high, low, close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_jerk_ema_21d_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day jerk of 5-day Donchian close position."""
    res = _ema(_close_in_range(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_jerk_ema_21d_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day jerk of 21-day Donchian close position."""
    res = _ema(_close_in_range(_max(high, 21), _min(low, 21), close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_jerk_ema_21d_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day jerk of 5-day Donchian midpoint position."""
    res = _ema(_close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_jerk_ema_21d_v103_signal(close: pd.Series) -> pd.Series:
    """21-day EMA of 21-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _ema(_close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(21).pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_jerk_z_21d_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 21-day jerk of intraday close position."""
    jrk = _close_in_range(high, low, close).pct_change(21).pct_change(21)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_jerk_z_21d_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 21-day jerk of 5-day Donchian close position."""
    jrk = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_jerk_z_21d_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 21-day jerk of 21-day Donchian close position."""
    jrk = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(21).pct_change(21)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_jerk_z_21d_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Z-score of 21-day jerk of 5-day Donchian midpoint position."""
    jrk = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_jerk_z_21d_v108_signal(close: pd.Series) -> pd.Series:
    """21-day Z-score of 21-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    jrk = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(21).pct_change(21)
    res = (jrk - _sma(jrk, 21)) / _std(jrk, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_jerk_norm_atr_21d_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of intraday close position normalized by 21-day ATR."""
    jrk = _close_in_range(high, low, close).pct_change(21).pct_change(21)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_jerk_norm_atr_21d_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of 5-day Donchian close position normalized by 21-day ATR."""
    jrk = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_jerk_norm_atr_21d_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of 21-day Donchian close position normalized by 21-day ATR."""
    jrk = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(21).pct_change(21)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_jerk_norm_atr_21d_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of 5-day Donchian midpoint position normalized by 21-day ATR."""
    jrk = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_jerk_norm_atr_21d_v113_signal(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day jerk of 20-day BB position normalized by 21-day ATR."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    jrk = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(21).pct_change(21)
    atr = _atr(high, low, close, 21)
    res = jrk / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_intraday_pos_21d_jerk_abs_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 21-day jerk of intraday close position."""
    res = _close_in_range(high, low, close).pct_change(21).pct_change(21).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_21d_jerk_abs_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 21-day jerk of 5-day Donchian close position."""
    res = _close_in_range(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_21d_jerk_abs_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 21-day jerk of 21-day Donchian close position."""
    res = _close_in_range(_max(high, 21), _min(low, 21), close).pct_change(21).pct_change(21).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_mid_5d_21d_jerk_abs_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 21-day jerk of 5-day Donchian midpoint position."""
    res = _close_relative_mid(_max(high, 5), _min(low, 5), close).pct_change(21).pct_change(21).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_bb_pos_20d_21d_jerk_abs_v118_signal(close: pd.Series) -> pd.Series:
    """Absolute value of 21-day jerk of 20-day BB position."""
    ma = _sma(close, 20)
    std = _std(close, 20)
    res = _close_in_range(ma + 2 * std, ma - 2 * std, close).pct_change(21).pct_change(21).abs()
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_5d_vs_21d_21d_jerk_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day jerk of ratio of 5-day close position to 21-day close position."""
    pos5 = _close_in_range(_max(high, 5), _min(low, 5), close)
    pos21 = _close_in_range(_max(high, 21), _min(low, 21), close).replace(0, np.nan)
    res = (pos5 / pos21).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09cpwr_f09_close_position_within_range_pos_21d_vs_63d_21d_jerk_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-day jerk of ratio of 21-day close position to 63-day close position using adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    pos21 = _close_in_range(_max(high * adj, 21), _min(low * adj, 21), closeadj)
    pos63 = _close_in_range(_max(high * adj, 63), _min(low * adj, 63), closeadj).replace(0, np.nan)
    res = (pos21 / pos63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

JERK_NAMES = [f for f in globals() if f.startswith("f09cpwr_") and f.endswith("_signal")]

F09_CLOSE_POSITION_WITHIN_RANGE_JERK_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F09_CLOSE_POSITION_WITHIN_RANGE_JERK_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
