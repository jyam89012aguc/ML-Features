# f03_trend_strength_metrics_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _trend_slope(price, w):
    return (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
def _trend_consistency(price, w):
    return (price > price.shift(1)).astype(float).rolling(w).mean()
def _trend_efficiency(price, w):
    net_move = (price - price.shift(w)).abs()
    total_path = price.diff().abs().rolling(w).sum()
    return net_move / total_path.replace(0, np.nan)

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)
def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)
def _dm(h, l):
    dh = h.diff()
    dl = l.shift(1) - l
    dp = np.where((dh > dl) & (dh > 0), dh, 0)
    dm = np.where((dl > dh) & (dl > 0), dl, 0)
    return pd.Series(dp, index=h.index), pd.Series(dm, index=l.index)

# Trend slope of close price over 5 days
def f03ts_trend_slope_close_5d_v001_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of close price over 10 days
def f03ts_trend_slope_close_10d_v002_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of close price over 21 days
def f03ts_trend_slope_close_21d_v003_signal(close: pd.Series) -> pd.Series:
    res = _trend_slope(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of closeadj price over 63 days
def f03ts_trend_slope_close_63d_v004_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of closeadj price over 126 days
def f03ts_trend_slope_close_126d_v005_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of closeadj price over 252 days
def f03ts_trend_slope_close_252d_v006_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of closeadj price over 504 days
def f03ts_trend_slope_close_504d_v007_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _trend_slope(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of high price over 5 days
def f03ts_trend_slope_high_5d_v008_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of high price over 10 days
def f03ts_trend_slope_high_10d_v009_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(high, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of high price over 21 days
def f03ts_trend_slope_high_21d_v010_signal(high: pd.Series) -> pd.Series:
    res = _trend_slope(high, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted high price over 63 days
def f03ts_trend_slope_high_63d_v011_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted high price over 126 days
def f03ts_trend_slope_high_126d_v012_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted high price over 252 days
def f03ts_trend_slope_high_252d_v013_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted high price over 504 days
def f03ts_trend_slope_high_504d_v014_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(high * adj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of low price over 5 days
def f03ts_trend_slope_low_5d_v015_signal(low: pd.Series) -> pd.Series:
    res = _trend_slope(low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of low price over 10 days
def f03ts_trend_slope_low_10d_v016_signal(low: pd.Series) -> pd.Series:
    res = _trend_slope(low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of low price over 21 days
def f03ts_trend_slope_low_21d_v017_signal(low: pd.Series) -> pd.Series:
    res = _trend_slope(low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted low price over 63 days
def f03ts_trend_slope_low_63d_v018_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted low price over 126 days
def f03ts_trend_slope_low_126d_v019_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted low price over 252 days
def f03ts_trend_slope_low_252d_v020_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend slope of adjusted low price over 504 days
def f03ts_trend_slope_low_504d_v021_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _trend_slope(low * adj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of close price over 5 days
def f03ts_trend_consistency_close_5d_v022_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of close price over 10 days
def f03ts_trend_consistency_close_10d_v023_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of close price over 21 days
def f03ts_trend_consistency_close_21d_v024_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of closeadj price over 63 days
def f03ts_trend_consistency_close_63d_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of closeadj price over 126 days
def f03ts_trend_consistency_close_126d_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of closeadj price over 252 days
def f03ts_trend_consistency_close_252d_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of closeadj price over 504 days
def f03ts_trend_consistency_close_504d_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of close price over 5 days
def f03ts_trend_consistency_ema_5d_v029_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of close price over 10 days
def f03ts_trend_consistency_ema_10d_v030_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of close price over 21 days
def f03ts_trend_consistency_ema_21d_v031_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of closeadj price over 63 days
def f03ts_trend_consistency_ema_63d_v032_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of closeadj price over 126 days
def f03ts_trend_consistency_ema_126d_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of closeadj price over 252 days
def f03ts_trend_consistency_ema_252d_v034_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of EMA of closeadj price over 504 days
def f03ts_trend_consistency_ema_504d_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_ema(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of close price over 5 days
def f03ts_trend_consistency_sma_5d_v036_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of close price over 10 days
def f03ts_trend_consistency_sma_10d_v037_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of close price over 21 days
def f03ts_trend_consistency_sma_21d_v038_signal(close: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of closeadj price over 63 days
def f03ts_trend_consistency_sma_63d_v039_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of closeadj price over 126 days
def f03ts_trend_consistency_sma_126d_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of closeadj price over 252 days
def f03ts_trend_consistency_sma_252d_v041_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of SMA of closeadj price over 504 days
def f03ts_trend_consistency_sma_504d_v042_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_consistency(_sma(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price over 5 days
def f03ts_trend_efficiency_close_5d_v043_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price over 10 days
def f03ts_trend_efficiency_close_10d_v044_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of close price over 21 days
def f03ts_trend_efficiency_close_21d_v045_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of closeadj price over 63 days
def f03ts_trend_efficiency_close_63d_v046_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of closeadj price over 126 days
def f03ts_trend_efficiency_close_126d_v047_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of closeadj price over 252 days
def f03ts_trend_efficiency_close_252d_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of closeadj price over 504 days
def f03ts_trend_efficiency_close_504d_v049_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of close price over 5 days
def f03ts_trend_efficiency_ema_5d_v050_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of close price over 10 days
def f03ts_trend_efficiency_ema_10d_v051_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of close price over 21 days
def f03ts_trend_efficiency_ema_21d_v052_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of closeadj price over 63 days
def f03ts_trend_efficiency_ema_63d_v053_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of closeadj price over 126 days
def f03ts_trend_efficiency_ema_126d_v054_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of closeadj price over 252 days
def f03ts_trend_efficiency_ema_252d_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of EMA of closeadj price over 504 days
def f03ts_trend_efficiency_ema_504d_v056_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_ema(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of close price over 5 days
def f03ts_trend_efficiency_sma_5d_v057_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of close price over 10 days
def f03ts_trend_efficiency_sma_10d_v058_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of close price over 21 days
def f03ts_trend_efficiency_sma_21d_v059_signal(close: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of closeadj price over 63 days
def f03ts_trend_efficiency_sma_63d_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of closeadj price over 126 days
def f03ts_trend_efficiency_sma_126d_v061_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of closeadj price over 252 days
def f03ts_trend_efficiency_sma_252d_v062_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of SMA of closeadj price over 504 days
def f03ts_trend_efficiency_sma_504d_v063_signal(closeadj: pd.Series) -> pd.Series:
    res = _trend_efficiency(_sma(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of DI+ over 10 days
def f03ts_trend_consistency_di_plus_10d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    dp, dm = _dm(high, low)
    tr = _atr(high, low, close, 10)
    dip = 100 * _sma(dp, 10) / tr.replace(0, np.nan)
    res = _trend_consistency(dip, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of DI+ over 21 days
def f03ts_trend_consistency_di_plus_21d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    dp, dm = _dm(high, low)
    tr = _atr(high, low, close, 21)
    dip = 100 * _sma(dp, 21) / tr.replace(0, np.nan)
    res = _trend_consistency(dip, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of DI+ over 63 days (adjusted)
def f03ts_trend_consistency_di_plus_63d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 63)
    dip = 100 * _sma(dp, 63) / tr.replace(0, np.nan)
    res = _trend_consistency(dip, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of DI+ over 126 days (adjusted)
def f03ts_trend_consistency_di_plus_126d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 126)
    dip = 100 * _sma(dp, 126) / tr.replace(0, np.nan)
    res = _trend_consistency(dip, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of DI+ over 252 days (adjusted)
def f03ts_trend_consistency_di_plus_252d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 252)
    dip = 100 * _sma(dp, 252) / tr.replace(0, np.nan)
    res = _trend_consistency(dip, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend consistency of DI+ over 504 days (adjusted)
def f03ts_trend_consistency_di_plus_504d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 504)
    dip = 100 * _sma(dp, 504) / tr.replace(0, np.nan)
    res = _trend_consistency(dip, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of DI- over 10 days
def f03ts_trend_efficiency_di_minus_10d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    dp, dm = _dm(high, low)
    tr = _atr(high, low, close, 10)
    dim = 100 * _sma(dm, 10) / tr.replace(0, np.nan)
    res = _trend_efficiency(dim, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of DI- over 21 days
def f03ts_trend_efficiency_di_minus_21d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    dp, dm = _dm(high, low)
    tr = _atr(high, low, close, 21)
    dim = 100 * _sma(dm, 21) / tr.replace(0, np.nan)
    res = _trend_efficiency(dim, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of DI- over 63 days (adjusted)
def f03ts_trend_efficiency_di_minus_63d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 63)
    dim = 100 * _sma(dm, 63) / tr.replace(0, np.nan)
    res = _trend_efficiency(dim, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of DI- over 126 days (adjusted)
def f03ts_trend_efficiency_di_minus_126d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 126)
    dim = 100 * _sma(dm, 126) / tr.replace(0, np.nan)
    res = _trend_efficiency(dim, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of DI- over 252 days (adjusted)
def f03ts_trend_efficiency_di_minus_252d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 252)
    dim = 100 * _sma(dm, 252) / tr.replace(0, np.nan)
    res = _trend_efficiency(dim, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Trend efficiency of DI- over 504 days (adjusted)
def f03ts_trend_efficiency_di_minus_504d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    dp, dm = _dm(h_adj, l_adj)
    tr = _atr(h_adj, l_adj, closeadj, 504)
    dim = 100 * _sma(dm, 504) / tr.replace(0, np.nan)
    res = _trend_efficiency(dim, 504)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f03ts_") and f.endswith("_signal")]

F03_TREND_STRENGTH_METRICS_BASE_REGISTRY_001_075 = {
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
    for n, c in F03_TREND_STRENGTH_METRICS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
