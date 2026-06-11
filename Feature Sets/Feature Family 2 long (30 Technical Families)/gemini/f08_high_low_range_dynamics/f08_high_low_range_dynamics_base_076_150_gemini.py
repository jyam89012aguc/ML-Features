# f08_high_low_range_dynamics_base_076_150_gemini.py
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

# High-low range expansion index over 5d
def f08hl_range_expansion_index_5d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _max(rp, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range expansion index over 10d
def f08hl_range_expansion_index_10d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _max(rp, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range expansion index over 21d
def f08hl_range_expansion_index_21d_v078_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _max(rp, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range expansion index over 63d
def f08hl_range_expansion_index_63d_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _max(rp, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range expansion index over 126d
def f08hl_range_expansion_index_126d_v080_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _max(rp, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range expansion index over 252d
def f08hl_range_expansion_index_252d_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _max(rp, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range expansion index over 504d
def f08hl_range_expansion_index_504d_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _max(rp, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 5d
def f08hl_range_contraction_index_5d_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _min(rp, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 10d
def f08hl_range_contraction_index_10d_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _min(rp, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 21d
def f08hl_range_contraction_index_21d_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _min(rp, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 63d
def f08hl_range_contraction_index_63d_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _min(rp, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 126d
def f08hl_range_contraction_index_126d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _min(rp, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 252d
def f08hl_range_contraction_index_252d_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _min(rp, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range contraction index over 504d
def f08hl_range_contraction_index_504d_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _min(rp, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 5d average
def f08hl_true_range_relative_5d_v090_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = _tr(high, low, close)
    res = tr / _sma(tr, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 10d average
def f08hl_true_range_relative_10d_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = _tr(high, low, close)
    res = tr / _sma(tr, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 21d average
def f08hl_true_range_relative_21d_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = _tr(high, low, close)
    res = tr / _sma(tr, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 63d average
def f08hl_true_range_relative_63d_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    tr = _tr(high * adj, low * adj, closeadj)
    res = tr / _sma(tr, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 126d average
def f08hl_true_range_relative_126d_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    tr = _tr(high * adj, low * adj, closeadj)
    res = tr / _sma(tr, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 252d average
def f08hl_true_range_relative_252d_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    tr = _tr(high * adj, low * adj, closeadj)
    res = tr / _sma(tr, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# True range relative to its 504d average
def f08hl_true_range_relative_504d_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    tr = _tr(high * adj, low * adj, closeadj)
    res = tr / _sma(tr, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 5d average true range
def f08hl_range_vs_avg_tr_5d_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _sma(_tr(high, low, close), 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 10d average true range
def f08hl_range_vs_avg_tr_10d_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _sma(_tr(high, low, close), 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 21d average true range
def f08hl_range_vs_avg_tr_21d_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (high - low) / _sma(_tr(high, low, close), 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 63d average true range
def f08hl_range_vs_avg_tr_63d_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(_tr(high * adj, low * adj, closeadj), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 126d average true range
def f08hl_range_vs_avg_tr_126d_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(_tr(high * adj, low * adj, closeadj), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 252d average true range
def f08hl_range_vs_avg_tr_252d_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(_tr(high * adj, low * adj, closeadj), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Daily range relative to 504d average true range
def f08hl_range_vs_avg_tr_504d_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = (high * adj - low * adj) / _sma(_tr(high * adj, low * adj, closeadj), 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 5d
def f08hl_range_ema_z_5d_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = (rp - _ema(rp, 5)) / _std(rp, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 10d
def f08hl_range_ema_z_10d_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = (rp - _ema(rp, 10)) / _std(rp, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 21d
def f08hl_range_ema_z_21d_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = (rp - _ema(rp, 21)) / _std(rp, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 63d
def f08hl_range_ema_z_63d_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = (rp - _ema(rp, 63)) / _std(rp, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 126d
def f08hl_range_ema_z_126d_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = (rp - _ema(rp, 126)) / _std(rp, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 252d
def f08hl_range_ema_z_252d_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = (rp - _ema(rp, 252)) / _std(rp, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range EMA Z-score over 504d
def f08hl_range_ema_z_504d_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = (rp - _ema(rp, 504)) / _std(rp, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 5d EMA
def f08hl_range_rel_ema_5d_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _ema(rp, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 10d EMA
def f08hl_range_rel_ema_10d_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _ema(rp, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 21d EMA
def f08hl_range_rel_ema_21d_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _hl_range_pct(high, low, close)
    res = rp / _ema(rp, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 63d EMA
def f08hl_range_rel_ema_63d_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _ema(rp, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 126d EMA
def f08hl_range_rel_ema_126d_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _ema(rp, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 252d EMA
def f08hl_range_rel_ema_252d_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _ema(rp, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# High-low range relative to its 504d EMA
def f08hl_range_rel_ema_504d_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high * adj, low * adj, closeadj)
    res = rp / _ema(rp, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5d ATR pct (standardized by average close)
def f08hl_atr_pct_5d_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _atr(high, low, close, 5) / _sma(close, 5).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10d ATR pct (standardized by average close)
def f08hl_atr_pct_10d_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _atr(high, low, close, 10) / _sma(close, 10).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21d ATR pct (standardized by average close)
def f08hl_atr_pct_21d_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _atr(high, low, close, 21) / _sma(close, 21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d ATR pct (standardized by average close)
def f08hl_atr_pct_63d_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr(high * adj, low * adj, closeadj, 63) / _sma(closeadj, 63).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d ATR pct (standardized by average close)
def f08hl_atr_pct_126d_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr(high * adj, low * adj, closeadj, 126) / _sma(closeadj, 126).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d ATR pct (standardized by average close)
def f08hl_atr_pct_252d_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr(high * adj, low * adj, closeadj, 252) / _sma(closeadj, 252).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d ATR pct (standardized by average close)
def f08hl_atr_pct_504d_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr(high * adj, low * adj, closeadj, 504) / _sma(closeadj, 504).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5d channel range relative to 5d ATR
def f08hl_channel_vs_atr_5d_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 5) - _min(low, 5)) / _atr(high, low, close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 10d channel range relative to 10d ATR
def f08hl_channel_vs_atr_10d_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 10) - _min(low, 10)) / _atr(high, low, close, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 21d channel range relative to 21d ATR
def f08hl_channel_vs_atr_21d_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_max(high, 21) - _min(low, 21)) / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d channel range relative to 63d ATR
def f08hl_channel_vs_atr_63d_v128_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_max(h_adj, 63) - _min(l_adj, 63)) / _atr(h_adj, l_adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d channel range relative to 126d ATR
def f08hl_channel_vs_atr_126d_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_max(h_adj, 126) - _min(l_adj, 126)) / _atr(h_adj, l_adj, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d channel range relative to 252d ATR
def f08hl_channel_vs_atr_252d_v130_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_max(h_adj, 252) - _min(l_adj, 252)) / _atr(h_adj, l_adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d channel range relative to 504d ATR
def f08hl_channel_vs_atr_504d_v131_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    res = (_max(h_adj, 504) - _min(l_adj, 504)) / _atr(h_adj, l_adj, closeadj, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 5d
def f08hl_smooth_range_z_5_5_v132_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_z(high, low, close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 10d
def f08hl_smooth_range_z_5_10_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_z(high, low, close, 5), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 21d
def f08hl_smooth_range_z_5_21_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_hl_range_z(high, low, close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 63d
def f08hl_smooth_range_z_5_63_v135_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_z(high, low, close, 5), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 126d
def f08hl_smooth_range_z_5_126_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_z(high, low, close, 5), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 252d
def f08hl_smooth_range_z_5_252_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_z(high, low, close, 5), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Smoothed 5d range Z-score over 504d
def f08hl_smooth_range_z_5_504_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _sma(_hl_range_z(high, low, close, 5), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 5d
def f08hl_range_pct_vol_5d_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _std(_hl_range_pct(high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 10d
def f08hl_range_pct_vol_10d_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _std(_hl_range_pct(high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 21d
def f08hl_range_pct_vol_21d_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _std(_hl_range_pct(high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 63d
def f08hl_range_pct_vol_63d_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _std(_hl_range_pct(high * adj, low * adj, closeadj), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 126d
def f08hl_range_pct_vol_126d_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _std(_hl_range_pct(high * adj, low * adj, closeadj), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 252d
def f08hl_range_pct_vol_252d_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _std(_hl_range_pct(high * adj, low * adj, closeadj), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility of high-low range pct over 504d
def f08hl_range_pct_vol_504d_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _std(_hl_range_pct(high * adj, low * adj, closeadj), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of ATR(5) to ATR(21)
def f08hl_atr_ratio_5_21_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _atr(high, low, close, 5) / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of ATR(21) to ATR(63)
def f08hl_atr_ratio_21_63_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr(high, low, close, 21) / _atr(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of range Z-score over 5d to range Z-score over 21d
def f08hl_range_z_ratio_5_21_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _hl_range_z(high, low, close, 5) / _hl_range_z(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Max range pct over 21d relative to 252d
def f08hl_max_range_rel_21_252_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high, low, close)
    rp_adj = _hl_range_pct(high * adj, low * adj, closeadj)
    res = _max(rp, 21) / _max(rp_adj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Min range pct over 21d relative to 252d
def f08hl_min_range_rel_21_252_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rp = _hl_range_pct(high, low, close)
    rp_adj = _hl_range_pct(high * adj, low * adj, closeadj)
    res = _min(rp, 21) / _min(rp_adj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f08hl_") and f.endswith("_signal")]

F08_HIGH_LOW_RANGE_DYNAMICS_BASE_REGISTRY_076_150 = {
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
    for n, c in F08_HIGH_LOW_RANGE_DYNAMICS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
