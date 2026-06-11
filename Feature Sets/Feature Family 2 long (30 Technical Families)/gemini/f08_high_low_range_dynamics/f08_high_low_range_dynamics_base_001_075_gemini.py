# f08_high_low_range_dynamics_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 5)).std()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)
def _atr(h, l, c, w): return _sma(_tr(h, l, c), w)

def _hl_range_pct(h, l, c):
    return (h - l) / c.abs().replace(0, np.nan)
def _hl_range_relative(h, l, c, w):
    curr = _hl_range_pct(h, l, c)
    avg = _sma(curr, w)
    return curr / avg.replace(0, np.nan)
def _hl_range_z(h, l, c, w):
    curr = _hl_range_pct(h, l, c)
    return (curr - _sma(curr, w)) / _std(curr, w).replace(0, np.nan)

# High-low range relative to 5d average close
def f08hl_high_low_range_pct_vs_sma_5d_v001_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _sma(close, 5).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to 10d average close
def f08hl_high_low_range_pct_vs_sma_10d_v002_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _sma(close, 10).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to 21d average close
def f08hl_high_low_range_pct_vs_sma_21d_v003_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _sma(close, 21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to 63d average close
def f08hl_high_low_range_pct_vs_sma_63d_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(closeadj, 63).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to 126d average close
def f08hl_high_low_range_pct_vs_sma_126d_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(closeadj, 126).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to 252d average close
def f08hl_high_low_range_pct_vs_sma_252d_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(closeadj, 252).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to 504d average close
def f08hl_high_low_range_pct_vs_sma_504d_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(closeadj, 504).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 5d moving average
def f08hl_high_low_range_relative_5d_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_relative(high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 10d moving average
def f08hl_high_low_range_relative_10d_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_relative(high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 21d moving average
def f08hl_high_low_range_relative_21d_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_relative(high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 63d moving average
def f08hl_high_low_range_relative_63d_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_relative(high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 126d moving average
def f08hl_high_low_range_relative_126d_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_relative(high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 252d moving average
def f08hl_high_low_range_relative_252d_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_relative(high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 504d moving average
def f08hl_high_low_range_relative_504d_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_relative(high * adj, low * adj, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 5d
def f08hl_high_low_range_z_5d_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_z(high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 10d
def f08hl_high_low_range_z_10d_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_z(high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 21d
def f08hl_high_low_range_z_21d_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_z(high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 63d
def f08hl_high_low_range_z_63d_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_z(high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 126d
def f08hl_high_low_range_z_126d_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_z(high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 252d
def f08hl_high_low_range_z_252d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_z(high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range Z-score over 504d
def f08hl_high_low_range_z_504d_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_z(high * adj, low * adj, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 5d ATR
def f08hl_high_low_range_std_atr_5d_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _atr(high, low, close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 10d ATR
def f08hl_high_low_range_std_atr_10d_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _atr(high, low, close, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 21d ATR
def f08hl_high_low_range_std_atr_21d_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 63d ATR
def f08hl_high_low_range_std_atr_63d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / _atr(h_adj, l_adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 126d ATR
def f08hl_high_low_range_std_atr_126d_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / _atr(h_adj, l_adj, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 252d ATR
def f08hl_high_low_range_std_atr_252d_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / _atr(h_adj, l_adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range standardized by 504d ATR
def f08hl_high_low_range_std_atr_504d_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / _atr(h_adj, l_adj, closeadj, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 5d ATR
def f08hl_true_range_std_atr_5d_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _tr(high, low, close) / _atr(high, low, close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 10d ATR
def f08hl_true_range_std_atr_10d_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _tr(high, low, close) / _atr(high, low, close, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 21d ATR
def f08hl_true_range_std_atr_21d_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _tr(high, low, close) / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 63d ATR
def f08hl_true_range_std_atr_63d_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _tr(h_adj, l_adj, closeadj) / _atr(h_adj, l_adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 126d ATR
def f08hl_true_range_std_atr_126d_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _tr(h_adj, l_adj, closeadj) / _atr(h_adj, l_adj, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 252d ATR
def f08hl_true_range_std_atr_252d_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _tr(h_adj, l_adj, closeadj) / _atr(h_adj, l_adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range standardized by 504d ATR
def f08hl_true_range_std_atr_504d_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = _tr(h_adj, l_adj, closeadj) / _atr(h_adj, l_adj, closeadj, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5d channel range pct
def f08hl_channel_range_pct_5d_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 5) - _min(low, 5)) / close.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10d channel range pct
def f08hl_channel_range_pct_10d_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 10) - _min(low, 10)) / close.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21d channel range pct
def f08hl_channel_range_pct_21d_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 21) - _min(low, 21)) / close.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d channel range pct
def f08hl_channel_range_pct_63d_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 63) - _min(low * adj, 63)) / closeadj.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d channel range pct
def f08hl_channel_range_pct_126d_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 126) - _min(low * adj, 126)) / closeadj.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d channel range pct
def f08hl_channel_range_pct_252d_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 252) - _min(low * adj, 252)) / closeadj.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d channel range pct
def f08hl_channel_range_pct_504d_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 504) - _min(low * adj, 504)) / closeadj.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5d channel range relative to average close
def f08hl_channel_range_rel_sma_5d_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 5) - _min(low, 5)) / _sma(close, 5).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10d channel range relative to average close
def f08hl_channel_range_rel_sma_10d_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 10) - _min(low, 10)) / _sma(close, 10).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.nan], np.nan)

# 21d channel range relative to average close
def f08hl_channel_range_rel_sma_21d_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 21) - _min(low, 21)) / _sma(close, 21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d channel range relative to average close
def f08hl_channel_range_rel_sma_63d_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 63) - _min(low * adj, 63)) / _sma(closeadj, 63).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d channel range relative to average close
def f08hl_channel_range_rel_sma_126d_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 126) - _min(low * adj, 126)) / _sma(closeadj, 126).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d channel range relative to average close
def f08hl_channel_range_rel_sma_252d_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 252) - _min(low * adj, 252)) / _sma(closeadj, 252).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d channel range relative to average close
def f08hl_channel_range_rel_sma_504d_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (_max(high * adj, 504) - _min(low * adj, 504)) / _sma(closeadj, 504).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 5d channel range
def f08hl_range_vs_channel_5d_v050_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (high - low) / (_max(high, 5) - _min(low, 5)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 10d channel range
def f08hl_range_vs_channel_10d_v051_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (high - low) / (_max(high, 10) - _min(low, 10)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 21d channel range
def f08hl_range_vs_channel_21d_v052_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = (high - low) / (_max(high, 21) - _min(low, 21)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 63d channel range
def f08hl_range_vs_channel_63d_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / (_max(h_adj, 63) - _min(l_adj, 63)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 126d channel range
def f08hl_range_vs_channel_126d_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / (_max(h_adj, 126) - _min(l_adj, 126)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 252d channel range
def f08hl_range_vs_channel_252d_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / (_max(h_adj, 252) - _min(l_adj, 252)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 504d channel range
def f08hl_range_vs_channel_504d_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (h_adj - l_adj) / (_max(h_adj, 504) - _min(l_adj, 504)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 5d high-low range pct
def f08hl_avg_range_pct_5d_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_pct(high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 10d high-low range pct
def f08hl_avg_range_pct_10d_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_pct(high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 21d high-low range pct
def f08hl_avg_range_pct_21d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_pct(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 63d high-low range pct
def f08hl_avg_range_pct_63d_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_pct(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 126d high-low range pct
def f08hl_avg_range_pct_126d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_pct(high * adj, low * adj, closeadj), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 252d high-low range pct
def f08hl_avg_range_pct_252d_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_pct(high * adj, low * adj, closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Average 504d high-low range pct
def f08hl_avg_range_pct_504d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_pct(high * adj, low * adj, closeadj), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 5d high-low range pct
def f08hl_ema_range_pct_5d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_hl_range_pct(high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 10d high-low range pct
def f08hl_ema_range_pct_10d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_hl_range_pct(high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 21d high-low range pct
def f08hl_ema_range_pct_21d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_hl_range_pct(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 63d high-low range pct
def f08hl_ema_range_pct_63d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_hl_range_pct(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 126d high-low range pct
def f08hl_ema_range_pct_126d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_hl_range_pct(high * adj, low * adj, closeadj), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 252d high-low range pct
def f08hl_ema_range_pct_252d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_hl_range_pct(high * adj, low * adj, closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Exponential average 504d high-low range pct
def f08hl_ema_range_pct_504d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _ema(_hl_range_pct(high * adj, low * adj, closeadj), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range pct divided by 5d ATR relative
def f08hl_range_pct_div_atr_5d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_pct(high, low, close) / (_atr(high, low, close, 5) / close.abs()).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of true range to high-low range
def f08hl_tr_to_hl_ratio_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _tr(high, low, close) / (high - low).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 21d range Z-score to 63d range Z-score
def f08hl_range_z_ratio_21_63_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _hl_range_z(high, low, close, 21) / _hl_range_z(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d relative range
def f08hl_smooth_rel_range_5_10_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_relative(high, low, close, 5), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of range pct over 10d
def f08hl_range_pct_volatility_10d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = _max(rp, 10) / _min(rp, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f08hl_") and f.endswith("_signal")]

F08_HIGH_LOW_RANGE_DYNAMICS_BASE_REGISTRY_001_075 = {
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
    for n, c in F08_HIGH_LOW_RANGE_DYNAMICS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
