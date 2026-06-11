# f19_atr_normalized_price_base_076_150_gemini.py
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

# Feature f19anp_v076: Price distance to Upper ATR band (SMA 21 + 2*ATR 21)
def f19anp_f19_atr_normalized_price_upper_band_21d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    ma = _sma(close, 21)
    res = (close - (ma + 2 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v077: Price distance to Lower ATR band (SMA 21 - 2*ATR 21)
def f19anp_f19_atr_normalized_price_lower_band_21d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    ma = _sma(close, 21)
    res = (close - (ma - 2 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v078: Price distance to Upper ATR band (SMA 63 + 2*ATR 63)
def f19anp_f19_atr_normalized_price_upper_band_63d_v078_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = (closeadj - (ma + 2 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v079: Price distance to Lower ATR band (SMA 63 - 2*ATR 63)
def f19anp_f19_atr_normalized_price_lower_band_63d_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    ma = _sma(closeadj, 63)
    res = (closeadj - (ma - 2 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v080: ATR 5d ROC normalized
def f19anp_f19_atr_normalized_price_atr_roc_5d_v080_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = atr.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v081: ATR 21d ROC normalized
def f19anp_f19_atr_normalized_price_atr_roc_21d_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = atr.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v082: Range expansion: (High-Low) / ATR 21
def f19anp_f19_atr_normalized_price_range_expansion_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (high - low) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v083: Range expansion 5d average / ATR 21

# Feature f19anp_v084: ATR 5d vs ATR 63d z-score (252d window)
def f19anp_f19_atr_normalized_price_atr_rel_zscore_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr5 = _atr_val(high * adj, low * adj, closeadj, 5)
    atr63 = _atr_val(high * adj, low * adj, closeadj, 63)
    ratio = atr5 / atr63.replace(0, np.nan)
    res = (ratio - ratio.rolling(252).mean()) / ratio.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v085: Price move 5d vs ATR 5d
def f19anp_f19_atr_normalized_price_move_5d_atr_5d_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = (close - close.shift(5)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v086: Price move 21d vs ATR 21d
def f19anp_f19_atr_normalized_price_move_21d_atr_21d_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (close - close.shift(21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v087: Price move 63d vs ATR 63d
def f19anp_f19_atr_normalized_price_move_63d_atr_63d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = (closeadj - closeadj.shift(63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v088: Distance to 252d SMA normalized by 21d ATR
def f19anp_f19_atr_normalized_price_sma252_dist_atr21_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = (closeadj - _sma(closeadj, 252)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v089: Distance to 126d EMA normalized by 21d ATR
def f19anp_f19_atr_normalized_price_ema126_dist_atr21_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = (closeadj - _ema(closeadj, 126)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v090: Close relative to 5d high/low range normalized by 21d ATR
def f19anp_f19_atr_normalized_price_range_pos_5d_norm_v090_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    ma_range = (_max(high, 5) + _min(low, 5)) / 2
    res = (close - ma_range) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v091: Close relative to 21d high/low range normalized by 21d ATR
def f19anp_f19_atr_normalized_price_range_pos_21d_norm_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    ma_range = (_max(high, 21) + _min(low, 21)) / 2
    res = (close - ma_range) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v092: ATR 252d relative to price level

# Feature f19anp_v093: ATR 504d relative to price level
def f19anp_f19_atr_normalized_price_atr_pct_504d_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 504)
    res = atr / closeadj.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v094: SMA 5d of ATR % 63d
def f19anp_f19_atr_normalized_price_atr_pct_63d_ma5_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr_pct = _atr_val(high * adj, low * adj, closeadj, 63) / closeadj.replace(0, np.nan)
    res = _sma(atr_pct, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v095: Trailing stop 1.5 ATR 10d
def f19anp_f19_atr_normalized_price_trailing_stop_1_5atr_10d_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 10)
    stop = _max(high, 10) - 1.5 * atr
    res = (close - stop) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v096: Trailing stop 2.5 ATR 63d
def f19anp_f19_atr_normalized_price_trailing_stop_2_5atr_63d_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    atr = _atr_val(h_adj, low * adj, closeadj, 63)
    stop = _max(h_adj, 63) - 2.5 * atr
    res = (closeadj - stop) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v097: ATR 21d vs 252d SMA of ATR 21d z-score
def f19anp_f19_atr_normalized_price_atr_long_zscore_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = _atr_zscore(atr, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v098: 10d Price move vs 252d SMA of ATR 21d
def f19anp_f19_atr_normalized_price_move10_atr252_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr_ma = _sma(_atr_val(high * adj, low * adj, closeadj, 21), 252)
    res = (closeadj - closeadj.shift(10)) / atr_ma.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v099: Price vs 21d EMA + 1 ATR
def f19anp_f19_atr_normalized_price_ema21_1atr_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (close - (_ema(close, 21) + atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v100: Price vs 21d EMA - 1 ATR
def f19anp_f19_atr_normalized_price_ema21_neg_1atr_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (close - (_ema(close, 21) - atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v101: ATR 5d volatility (std) z-score 63d
def f19anp_f19_atr_normalized_price_atr_vol_zscore_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    atr_std = atr.rolling(21).std()
    res = (atr_std - atr_std.rolling(63).mean()) / atr_std.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v102: SMA 21d of ATR % z-score 252d
def f19anp_f19_atr_normalized_price_atr_pct_zscore_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr_pct = _atr_val(high * adj, low * adj, closeadj, 21) / closeadj.replace(0, np.nan)
    res = (atr_pct - atr_pct.rolling(252).mean()) / atr_pct.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v103: Price move 126d normalized by ATR 126d
def f19anp_f19_atr_normalized_price_move126_atr126_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = (closeadj - closeadj.shift(126)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v104: Price move 252d normalized by ATR 252d
def f19anp_f19_atr_normalized_price_move252_atr252_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 252)
    res = (closeadj - closeadj.shift(252)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v105: ATR 5d vs 21d EMA of ATR 5d
def f19anp_f19_atr_normalized_price_atr5_ema21_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = (atr - _ema(atr, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v106: ATR 21d vs 63d EMA of ATR 21d
def f19anp_f19_atr_normalized_price_atr21_ema63_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = (atr - _ema(atr, 63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v107: SMA 5d of price distance to SMA 21d normalized by ATR 21d
def f19anp_f19_atr_normalized_price_ma_dist_norm_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    dist = (close - _sma(close, 21)) / atr.replace(0, np.nan)
    res = _sma(dist, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v108: SMA 21d of price distance to SMA 63d normalized by ATR 63d
def f19anp_f19_atr_normalized_price_ma_dist_norm_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    dist = (closeadj - _sma(closeadj, 63)) / atr.replace(0, np.nan)
    res = _sma(dist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v109: ATR 126d z-score 504d

# Feature f19anp_v110: ATR 5d relative to 252d high ATR
def f19anp_f19_atr_normalized_price_atr5_high252_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 5)
    res = atr / _max(atr, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v111: ATR 5d relative to 252d low ATR
def f19anp_f19_atr_normalized_price_atr5_low252_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 5)
    res = atr / _min(atr, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v112: ATR 21d relative to 504d high ATR
def f19anp_f19_atr_normalized_price_atr21_high504_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = atr / _max(atr, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v113: ATR 21d relative to 504d low ATR
def f19anp_f19_atr_normalized_price_atr21_low504_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = atr / _min(atr, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v114: SMA 5d of ATR ROC 5d
def f19anp_f19_atr_normalized_price_atr_roc5_ma5_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    res = _sma(atr.pct_change(5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v115: SMA 21d of ATR ROC 21d
def f19anp_f19_atr_normalized_price_atr_roc21_ma21_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = _sma(atr.pct_change(21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v116: Price vs (SMA 21 + 1 ATR 21)
def f19anp_f19_atr_normalized_price_sma21_1atr_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (close - (_sma(close, 21) + atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v117: Price vs (SMA 21 - 1 ATR 21)
def f19anp_f19_atr_normalized_price_sma21_neg_1atr_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (close - (_sma(close, 21) - atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v118: Price vs (SMA 63 + 1.5 ATR 63)
def f19anp_f19_atr_normalized_price_sma63_1_5atr_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = (closeadj - (_sma(closeadj, 63) + 1.5 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v119: Price vs (SMA 63 - 1.5 ATR 63)
def f19anp_f19_atr_normalized_price_sma63_neg_1_5atr_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = (closeadj - (_sma(closeadj, 63) - 1.5 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v120: ATR 5d vs 5d SMA of ATR 21d
def f19anp_f19_atr_normalized_price_atr5_atr21ma_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr5 = _atr_val(high, low, close, 5)
    atr21ma = _sma(_atr_val(high, low, close, 21), 5)
    res = (atr5 - atr21ma) / atr21ma.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v121: Close vs 5d high/low mid normalized by 5d ATR
def f19anp_f19_atr_normalized_price_mid5_norm5_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    mid = (_max(high, 5) + _min(low, 5)) / 2
    res = (close - mid) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v122: Close vs 21d high/low mid normalized by 21d ATR
def f19anp_f19_atr_normalized_price_mid21_norm21_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    mid = (_max(high, 21) + _min(low, 21)) / 2
    res = (close - mid) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v123: Close vs 63d high/low mid normalized by 63d ATR
def f19anp_f19_atr_normalized_price_mid63_norm63_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 63)
    mid = (_max(h_adj, 63) + _min(l_adj, 63)) / 2
    res = (closeadj - mid) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v124: Range (high-low) vs 5d SMA of range
def f19anp_f19_atr_normalized_price_range_ma_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    res = (rng - _sma(rng, 5)) / _atr_val(high, low, close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v125: Range (high-low) vs 21d SMA of range
def f19anp_f19_atr_normalized_price_range_ma_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = high - low
    res = (rng - _sma(rng, 21)) / _atr_val(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v126: ATR 5d vs High-Low 5d
def f19anp_f19_atr_normalized_price_atr5_hl5_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    hl = high - low
    res = (atr - hl) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v127: ATR 21d vs High-Low 21d
def f19anp_f19_atr_normalized_price_atr21_hl21_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    hl = high - low
    res = (atr - hl) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v128: 5d ROC of Price / ATR 21d
def f19anp_f19_atr_normalized_price_roc5_atr21_v128_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = close.pct_change(5) / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v129: 21d ROC of Price / ATR 63d
def f19anp_f19_atr_normalized_price_roc21_atr63_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = closeadj.pct_change(21) / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v130: 63d ROC of Price / ATR 126d
def f19anp_f19_atr_normalized_price_roc63_atr126_v130_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 126)
    res = closeadj.pct_change(63) / (atr / closeadj.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v131: ATR 5d z-score 252d
def f19anp_f19_atr_normalized_price_atr5_z252_v131_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 5)
    res = _atr_zscore(atr, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v132: ATR 21d z-score 504d
def f19anp_f19_atr_normalized_price_atr21_z504_v132_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = _atr_zscore(atr, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v133: ATR 63d z-score 504d
def f19anp_f19_atr_normalized_price_atr63_z504_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 63)
    res = _atr_zscore(atr, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v134: SMA 5d of ATR 5d / ATR 63d
def f19anp_f19_atr_normalized_price_atr_ratio_ma5_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    ratio = _atr_val(high * adj, low * adj, closeadj, 5) / _atr_val(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    res = _sma(ratio, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v135: SMA 21d of ATR 21d / ATR 126d
def f19anp_f19_atr_normalized_price_atr_ratio_ma21_v135_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    ratio = _atr_val(high * adj, low * adj, closeadj, 21) / _atr_val(high * adj, low * adj, closeadj, 126).replace(0, np.nan)
    res = _sma(ratio, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v136: Distance to Upper Donchian 21d / ATR 21d
def f19anp_f19_atr_normalized_price_donchian_upper_dist_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (_max(high, 21) - close) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v137: Distance to Lower Donchian 21d / ATR 21d
def f19anp_f19_atr_normalized_price_donchian_lower_dist_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    res = (close - _min(low, 21)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v138: Distance to Upper Donchian 63d / ATR 63d
def f19anp_f19_atr_normalized_price_donchian_upper_dist_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 63)
    res = (_max(h_adj, 63) - closeadj) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v139: Distance to Lower Donchian 63d / ATR 63d
def f19anp_f19_atr_normalized_price_donchian_lower_dist_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj, l_adj = high * adj, low * adj
    atr = _atr_val(h_adj, l_adj, closeadj, 63)
    res = (closeadj - _min(l_adj, 63)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v140: ATR 5d relative to 21d SMA of ATR 5d z-score 63d
def f19anp_f19_atr_normalized_price_atr_ma_zscore_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 5)
    rel = atr / _sma(atr, 21).replace(0, np.nan)
    res = (rel - rel.rolling(63).mean()) / rel.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v141: Close vs (SMA 252 + 2 ATR 21)
def f19anp_f19_atr_normalized_price_sma252_2atr_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = (closeadj - (_sma(closeadj, 252) + 2 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v142: Close vs (SMA 252 - 2 ATR 21)
def f19anp_f19_atr_normalized_price_sma252_neg_2atr_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr = _atr_val(high * adj, low * adj, closeadj, 21)
    res = (closeadj - (_sma(closeadj, 252) - 2 * atr)) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v143: ATR % 21d z-score 504d
def f19anp_f19_atr_normalized_price_atr_pct_z504_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr_pct = _atr_val(high * adj, low * adj, closeadj, 21) / closeadj.replace(0, np.nan)
    res = (atr_pct - atr_pct.rolling(504).mean()) / atr_pct.rolling(504).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v144: ATR % 63d z-score 504d
def f19anp_f19_atr_normalized_price_atr_pct_z504_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    atr_pct = _atr_val(high * adj, low * adj, closeadj, 63) / closeadj.replace(0, np.nan)
    res = (atr_pct - atr_pct.rolling(504).mean()) / atr_pct.rolling(504).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v145: ATR 5d / ATR 252d ratio
def f19anp_f19_atr_normalized_price_atr_ratio_5_252_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr_val(high * adj, low * adj, closeadj, 5) / _atr_val(high * adj, low * adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v146: ATR 21d / ATR 504d ratio
def f19anp_f19_atr_normalized_price_atr_ratio_21_504_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _atr_val(high * adj, low * adj, closeadj, 21) / _atr_val(high * adj, low * adj, closeadj, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v147: SMA 5d of Range expansion v082
def f19anp_f19_atr_normalized_price_range_exp_ma5_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    exp = (high - low) / atr.replace(0, np.nan)
    res = _sma(exp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v148: SMA 21d of Range expansion v082
def f19anp_f19_atr_normalized_price_range_exp_ma21_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr_val(high, low, close, 21)
    exp = (high - low) / atr.replace(0, np.nan)
    res = _sma(exp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v149: Trailing stop distance (4 ATR, 63d)
def f19anp_f19_atr_normalized_price_trailing_stop_4atr_63d_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    atr = _atr_val(h_adj, low * adj, closeadj, 63)
    stop = _max(h_adj, 63) - 4 * atr
    res = (closeadj - stop) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature f19anp_v150: Trailing stop distance (5 ATR, 252d)
def f19anp_f19_atr_normalized_price_trailing_stop_5atr_252d_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    atr = _atr_val(h_adj, low * adj, closeadj, 252)
    stop = _max(h_adj, 252) - 5 * atr
    res = (closeadj - stop) / atr.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f19anp_") and f.endswith("_signal")]

F19_ATR_NORMALIZED_PRICE_BASE_REGISTRY_076_150 = {
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
    for n, c in F19_ATR_NORMALIZED_PRICE_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076_150 OK")
