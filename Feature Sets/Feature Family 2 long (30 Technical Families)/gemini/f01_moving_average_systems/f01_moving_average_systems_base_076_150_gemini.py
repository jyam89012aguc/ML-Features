import pandas as pd
import numpy as np

# Helpers
def _sma(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=w//2 if w>1 else 1, adjust=False).mean()
def _wma(s, w):
    weights = np.arange(1, w + 1)
    return s.rolling(w, min_periods=w).apply(lambda x: np.dot(x, weights) / weights.sum() if len(x)==w else np.nan, raw=True)
def _z(s, w):
    rolling = s.rolling(w, min_periods=w//2 if w>1 else 1)
    return (s - rolling.mean()) / rolling.std().replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).min()
def _max(s, w): return s.rolling(w, min_periods=w//2 if w>1 else 1).max()

# Domain Primitives
def _ma_distance(price, ma):
    return (price - ma) / ma.abs().replace(0, np.nan)
def _ma_alignment(ma_short, ma_long):
    return (ma_short - ma_long) / ma_long.abs().replace(0, np.nan)
def _ma_rel_slope(ma, w):
    return (ma - ma.shift(w)) / ma.shift(w).abs().replace(0, np.nan)

# Features 076-082: SMA Alignment (Variations)
# (sma10 - sma21) / sma21
def f01ma_f01_moving_average_systems_sma_alignment_10_21d_base_v076_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 10), _sma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (sma5 - sma42) / sma42
def f01ma_f01_moving_average_systems_sma_alignment_5_42d_base_v077_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 5), _sma(closeadj, 42)).replace([np.inf, -np.inf], np.nan)

# (sma21 - sma126) / sma126
def f01ma_f01_moving_average_systems_sma_alignment_21_126d_base_v078_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 21), _sma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# (sma42 - sma252) / sma252
def f01ma_f01_moving_average_systems_sma_alignment_42_252d_base_v079_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(closeadj, 42), _sma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (sma10 - sma63) / sma63
def f01ma_f01_moving_average_systems_sma_alignment_10_63d_base_v080_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 10), _sma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (sma21 - sma252) / sma252
def f01ma_f01_moving_average_systems_sma_alignment_21_252d_base_v081_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 21), _sma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (sma5 - sma126) / sma126
def f01ma_f01_moving_average_systems_sma_alignment_5_126d_base_v082_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 5), _sma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# Features 083-089: EMA Alignment (Variations)
# (ema10 - ema21) / ema21
def f01ma_f01_moving_average_systems_ema_alignment_10_21d_base_v083_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 10), _ema(close, 21)).replace([np.inf, -np.inf], np.nan)

# (ema5 - ema42) / ema42
def f01ma_f01_moving_average_systems_ema_alignment_5_42d_base_v084_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 5), _ema(closeadj, 42)).replace([np.inf, -np.inf], np.nan)

# (ema21 - ema126) / ema126
def f01ma_f01_moving_average_systems_ema_alignment_21_126d_base_v085_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 21), _ema(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# (ema42 - ema252) / ema252
def f01ma_f01_moving_average_systems_ema_alignment_42_252d_base_v086_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(closeadj, 42), _ema(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (ema10 - ema63) / ema63
def f01ma_f01_moving_average_systems_ema_alignment_10_63d_base_v087_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 10), _ema(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (ema21 - ema252) / ema252
def f01ma_f01_moving_average_systems_ema_alignment_21_252d_base_v088_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 21), _ema(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (ema5 - ema126) / ema126
def f01ma_f01_moving_average_systems_ema_alignment_5_126d_base_v089_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 5), _ema(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# Features 090-096: WMA Alignment (Variations)
# (wma10 - wma21) / wma21
def f01ma_f01_moving_average_systems_wma_alignment_10_21d_base_v090_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 10), _wma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (wma5 - wma42) / wma42
def f01ma_f01_moving_average_systems_wma_alignment_5_42d_base_v091_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 5), _wma(closeadj, 42)).replace([np.inf, -np.inf], np.nan)

# (wma21 - wma126) / wma126
def f01ma_f01_moving_average_systems_wma_alignment_21_126d_base_v092_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 21), _wma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# (wma42 - wma252) / wma252
def f01ma_f01_moving_average_systems_wma_alignment_42_252d_base_v093_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(closeadj, 42), _wma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (wma10 - wma63) / wma63
def f01ma_f01_moving_average_systems_wma_alignment_10_63d_base_v094_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 10), _wma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (wma21 - wma252) / wma252
def f01ma_f01_moving_average_systems_wma_alignment_21_252d_base_v095_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 21), _wma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (wma5 - wma126) / wma126
def f01ma_f01_moving_average_systems_wma_alignment_5_126d_base_v096_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 5), _wma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# Features 097-103: High Distance to SMA
# (high - sma5) / sma5
def f01ma_f01_moving_average_systems_high_dist_sma_5d_base_v097_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(high, _sma(close, 5)).replace([np.inf, -np.inf], np.nan)

# (high - sma21) / sma21
def f01ma_f01_moving_average_systems_high_dist_sma_21d_base_v098_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(high, _sma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (high - sma63) / sma63
def f01ma_f01_moving_average_systems_high_dist_sma_63d_base_v099_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_distance(high, _sma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (high - ema21) / ema21
def f01ma_f01_moving_average_systems_high_dist_ema_21d_base_v100_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(high, _ema(close, 21)).replace([np.inf, -np.inf], np.nan)

# (high - ema63) / ema63
def f01ma_f01_moving_average_systems_high_dist_ema_63d_base_v101_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_distance(high, _ema(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (high - wma21) / wma21
def f01ma_f01_moving_average_systems_high_dist_wma_21d_base_v102_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(high, _wma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (high - wma63) / wma63
def f01ma_f01_moving_average_systems_high_dist_wma_63d_base_v103_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_distance(high, _wma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# Features 104-110: Low Distance to SMA
# (low - sma5) / sma5
def f01ma_f01_moving_average_systems_low_dist_sma_5d_base_v104_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(low, _sma(close, 5)).replace([np.inf, -np.inf], np.nan)

# (low - sma21) / sma21
def f01ma_f01_moving_average_systems_low_dist_sma_21d_base_v105_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(low, _sma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (low - sma63) / sma63
def f01ma_f01_moving_average_systems_low_dist_sma_63d_base_v106_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_distance(low, _sma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (low - ema21) / ema21
def f01ma_f01_moving_average_systems_low_dist_ema_21d_base_v107_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(low, _ema(close, 21)).replace([np.inf, -np.inf], np.nan)

# (low - ema63) / ema63
def f01ma_f01_moving_average_systems_low_dist_ema_63d_base_v108_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_distance(low, _ema(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (low - wma21) / wma21
def f01ma_f01_moving_average_systems_low_dist_wma_21d_base_v109_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    return _ma_distance(low, _wma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (low - wma63) / wma63
def f01ma_f01_moving_average_systems_low_dist_wma_63d_base_v110_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_distance(low, _wma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# Features 111-117: VWMA Distance
# (close - vwma5) / vwma5
def f01ma_f01_moving_average_systems_vwma_dist_5d_base_v111_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 5) / _sma(volume, 5).replace(0, np.nan)
    return _ma_distance(close, vwma).replace([np.inf, -np.inf], np.nan)

# (close - vwma10) / vwma10
def f01ma_f01_moving_average_systems_vwma_dist_10d_base_v112_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 10) / _sma(volume, 10).replace(0, np.nan)
    return _ma_distance(close, vwma).replace([np.inf, -np.inf], np.nan)

# (close - vwma21) / vwma21
def f01ma_f01_moving_average_systems_vwma_dist_21d_base_v113_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 21) / _sma(volume, 21).replace(0, np.nan)
    return _ma_distance(close, vwma).replace([np.inf, -np.inf], np.nan)

# (closeadj - vwma42) / vwma42
def f01ma_f01_moving_average_systems_vwma_dist_42d_base_v114_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 42) / _sma(volume, 42).replace(0, np.nan)
    return _ma_distance(closeadj, vwma).replace([np.inf, -np.inf], np.nan)

# (closeadj - vwma63) / vwma63
def f01ma_f01_moving_average_systems_vwma_dist_63d_base_v115_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 63) / _sma(volume, 63).replace(0, np.nan)
    return _ma_distance(closeadj, vwma).replace([np.inf, -np.inf], np.nan)

# (closeadj - vwma126) / vwma126
def f01ma_f01_moving_average_systems_vwma_dist_126d_base_v116_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 126) / _sma(volume, 126).replace(0, np.nan)
    return _ma_distance(closeadj, vwma).replace([np.inf, -np.inf], np.nan)

# (closeadj - vwma252) / vwma252
def f01ma_f01_moving_average_systems_vwma_dist_252d_base_v117_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 252) / _sma(volume, 252).replace(0, np.nan)
    return _ma_distance(closeadj, vwma).replace([np.inf, -np.inf], np.nan)

# Features 118-124: Price Z-score Relative to SMA (Volatility)
# zscore(close, 5)
def f01ma_f01_moving_average_systems_price_zscore_5d_base_v118_signal(close: pd.Series) -> pd.Series:
    return _z(close, 5).replace([np.inf, -np.inf], np.nan)

# zscore(close, 21)
def f01ma_f01_moving_average_systems_price_zscore_21d_base_v119_signal(close: pd.Series) -> pd.Series:
    return _z(close, 21).replace([np.inf, -np.inf], np.nan)

# zscore(closeadj, 63)
def f01ma_f01_moving_average_systems_price_zscore_63d_base_v120_signal(closeadj: pd.Series) -> pd.Series:
    return _z(closeadj, 63).replace([np.inf, -np.inf], np.nan)

# zscore(closeadj, 252)
def f01ma_f01_moving_average_systems_price_zscore_252d_base_v121_signal(closeadj: pd.Series) -> pd.Series:
    return _z(closeadj, 252).replace([np.inf, -np.inf], np.nan)

# zscore(volume, 21)
def f01ma_f01_moving_average_systems_volume_zscore_21d_base_v122_signal(volume: pd.Series) -> pd.Series:
    return _z(volume, 21).replace([np.inf, -np.inf], np.nan)

# zscore(volume, 63)
def f01ma_f01_moving_average_systems_volume_zscore_63d_base_v123_signal(volume: pd.Series) -> pd.Series:
    return _z(volume, 63).replace([np.inf, -np.inf], np.nan)

# zscore(high-low, 21)
def f01ma_f01_moving_average_systems_range_zscore_21d_base_v124_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    return _z(high - low, 21).replace([np.inf, -np.inf], np.nan)

# Features 125-131: MA Stacking
# ((sma5 > sma21).astype(float) + (sma21 > sma63).astype(float)) / 2.0
def f01ma_f01_moving_average_systems_ma_stack_rank_5_21_63d_base_v125_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    s5 = _sma(close, 5)
    s21 = _sma(close, 21)
    s63 = _sma(closeadj, 63)
    return ((s5 > s21).astype(float) + (s21 > s63).astype(float)) / 2.0

# ((ema5 > ema21).astype(float) + (ema21 > ema63).astype(float)) / 2.0
def f01ma_f01_moving_average_systems_ema_stack_rank_5_21_63d_base_v126_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    e5 = _ema(close, 5)
    e21 = _ema(close, 21)
    e63 = _ema(closeadj, 63)
    return ((e5 > e21).astype(float) + (e21 > e63).astype(float)) / 2.0

# ((sma21 > sma63).astype(float) + (sma63 > sma252).astype(float)) / 2.0
def f01ma_f01_moving_average_systems_ma_stack_rank_21_63_252d_base_v127_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    s21 = _sma(close, 21)
    s63 = _sma(closeadj, 63)
    s252 = _sma(closeadj, 252)
    return ((s21 > s63).astype(float) + (s63 > s252).astype(float)) / 2.0

# ((ema21 > ema63).astype(float) + (ema63 > ema252).astype(float)) / 2.0
def f01ma_f01_moving_average_systems_ema_stack_rank_21_63_252d_base_v128_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    e21 = _ema(close, 21)
    e63 = _ema(closeadj, 63)
    e252 = _ema(closeadj, 252)
    return ((e21 > e63).astype(float) + (e63 > e252).astype(float)) / 2.0

# ((wma5 > wma21).astype(float) + (wma21 > wma63).astype(float)) / 2.0
def f01ma_f01_moving_average_systems_wma_stack_rank_5_21_63d_base_v129_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    w5 = _wma(close, 5)
    w21 = _wma(close, 21)
    w63 = _wma(closeadj, 63)
    return ((w5 > w21).astype(float) + (w21 > w63).astype(float)) / 2.0

# ((vwma21 > sma21).astype(float) + (sma21 > sma63).astype(float)) / 2.0
def f01ma_f01_moving_average_systems_vwma_stack_rank_21_63d_base_v130_signal(close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vw21 = _sma(close * volume, 21) / _sma(volume, 21).replace(0, np.nan)
    s21 = _sma(close, 21)
    s63 = _sma(closeadj, 63)
    return ((vw21 > s21).astype(float) + (s21 > s63).astype(float)) / 2.0

# (close > sma5) & (close > sma21) & (close > sma63)
def f01ma_f01_moving_average_systems_price_above_all_ma_base_v131_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return ((close > _sma(close, 5)) & (close > _sma(close, 21)) & (close > _sma(closeadj, 63))).astype(float)

# Features 132-138: MA Stretch
# (close - sma21) / (max(close, 21) - min(close, 21))
def f01ma_f01_moving_average_systems_sma_stretch_21d_base_v132_signal(close: pd.Series) -> pd.Series:
    return (close - _sma(close, 21)) / (_max(close, 21) - _min(close, 21)).replace(0, np.nan)

# (closeadj - sma63) / (max(closeadj, 63) - min(closeadj, 63))
def f01ma_f01_moving_average_systems_sma_stretch_63d_base_v133_signal(closeadj: pd.Series) -> pd.Series:
    return (closeadj - _sma(closeadj, 63)) / (_max(closeadj, 63) - _min(closeadj, 63)).replace(0, np.nan)

# (closeadj - sma252) / (max(closeadj, 252) - min(closeadj, 252))
def f01ma_f01_moving_average_systems_sma_stretch_252d_base_v134_signal(closeadj: pd.Series) -> pd.Series:
    return (closeadj - _sma(closeadj, 252)) / (_max(closeadj, 252) - _min(closeadj, 252)).replace(0, np.nan)

# (close - ema21) / (max(close, 21) - min(close, 21))
def f01ma_f01_moving_average_systems_ema_stretch_21d_base_v135_signal(close: pd.Series) -> pd.Series:
    return (close - _ema(close, 21)) / (_max(close, 21) - _min(close, 21)).replace(0, np.nan)

# (closeadj - ema63) / (max(closeadj, 63) - min(closeadj, 63))
def f01ma_f01_moving_average_systems_ema_stretch_63d_base_v136_signal(closeadj: pd.Series) -> pd.Series:
    return (closeadj - _ema(closeadj, 63)) / (_max(closeadj, 63) - _min(closeadj, 63)).replace(0, np.nan)

# (close - wma21) / (max(close, 21) - min(close, 21))
def f01ma_f01_moving_average_systems_wma_stretch_21d_base_v137_signal(close: pd.Series) -> pd.Series:
    return (close - _wma(close, 21)) / (_max(close, 21) - _min(close, 21)).replace(0, np.nan)

# (closeadj - wma63) / (max(closeadj, 63) - min(closeadj, 63))
def f01ma_f01_moving_average_systems_wma_stretch_63d_base_v138_signal(closeadj: pd.Series) -> pd.Series:
    return (closeadj - _wma(closeadj, 63)) / (_max(closeadj, 63) - _min(closeadj, 63)).replace(0, np.nan)

# Features 139-145: MA Channel Position
# (close - sma(low, 21)) / (sma(high, 21) - sma(low, 21))
def f01ma_f01_moving_average_systems_ma_channel_pos_21d_base_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    s_low = _sma(low, 21)
    s_high = _sma(high, 21)
    return (close - s_low) / (s_high - s_low).replace(0, np.nan)

# (closeadj - sma(low, 63)) / (sma(high, 63) - sma(low, 63))
def f01ma_f01_moving_average_systems_ma_channel_pos_63d_base_v140_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    s_low = _sma(low, 63)
    s_high = _sma(high, 63)
    return (closeadj - s_low) / (s_high - s_low).replace(0, np.nan)

# (closeadj - sma(low, 252)) / (sma(high, 252) - sma(low, 252))
def f01ma_f01_moving_average_systems_ma_channel_pos_252d_base_v141_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    s_low = _sma(low, 252)
    s_high = _sma(high, 252)
    return (closeadj - s_low) / (s_high - s_low).replace(0, np.nan)

# (close - ema(low, 21)) / (ema(high, 21) - ema(low, 21))
def f01ma_f01_moving_average_systems_ema_channel_pos_21d_base_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e_low = _ema(low, 21)
    e_high = _ema(high, 21)
    return (close - e_low) / (e_high - e_low).replace(0, np.nan)

# (closeadj - ema(low, 63)) / (ema(high, 63) - ema(low, 63))
def f01ma_f01_moving_average_systems_ema_channel_pos_63d_base_v143_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    e_low = _ema(low, 63)
    e_high = _ema(high, 63)
    return (closeadj - e_low) / (e_high - e_low).replace(0, np.nan)

# (close - wma(low, 21)) / (wma(high, 21) - wma(low, 21))
def f01ma_f01_moving_average_systems_wma_channel_pos_21d_base_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    w_low = _wma(low, 21)
    w_high = _wma(high, 21)
    return (close - w_low) / (w_high - w_low).replace(0, np.nan)

# (closeadj - wma(low, 63)) / (wma(high, 63) - wma(low, 63))
def f01ma_f01_moving_average_systems_wma_channel_pos_63d_base_v145_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    w_low = _wma(low, 63)
    w_high = _wma(high, 63)
    return (closeadj - w_low) / (w_high - w_low).replace(0, np.nan)

# Features 146-150: MA Acceleration (Momentum of Momentum)
# rel_slope(sma21, 5) - rel_slope(sma21, 5).shift(5)
def f01ma_f01_moving_average_systems_sma_accel_21d_base_v146_signal(close: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_sma(close, 21), 5)
    return (slope - slope.shift(5)).replace([np.inf, -np.inf], np.nan)

# rel_slope(ema21, 5) - rel_slope(ema21, 5).shift(5)
def f01ma_f01_moving_average_systems_ema_accel_21d_base_v147_signal(close: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_ema(close, 21), 5)
    return (slope - slope.shift(5)).replace([np.inf, -np.inf], np.nan)

# rel_slope(sma63, 5) - rel_slope(sma63, 5).shift(5)
def f01ma_f01_moving_average_systems_sma_accel_63d_base_v148_signal(closeadj: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_sma(closeadj, 63), 5)
    return (slope - slope.shift(5)).replace([np.inf, -np.inf], np.nan)

# rel_slope(ema63, 5) - rel_slope(ema63, 5).shift(5)
def f01ma_f01_moving_average_systems_ema_accel_63d_base_v149_signal(closeadj: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_ema(closeadj, 63), 5)
    return (slope - slope.shift(5)).replace([np.inf, -np.inf], np.nan)

# rel_slope(vwma21, 5) - rel_slope(vwma21, 5).shift(5)
def f01ma_f01_moving_average_systems_vwma_accel_21d_base_v150_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 21) / _sma(volume, 21).replace(0, np.nan)
    slope = _ma_rel_slope(vwma, 5)
    return (slope - slope.shift(5)).replace([np.inf, -np.inf], np.nan)

F01_MOVING_AVERAGE_SYSTEMS_BASE_REGISTRY_076_150 = {
    name: {
        "func": globals()[name],
        "inputs": [arg for arg in ["high", "low", "close", "closeadj", "volume"] if arg in globals()[name].__code__.co_varnames]
    }
    for name in globals() if name.startswith("f01ma_f01_moving_average_systems_")
}

if __name__ == "__main__":
    import numpy as np
    np.random.seed(42)
    n = 1000
    close = pd.Series(np.random.normal(100, 5, n), name="close")
    closeadj = close * 1.05
    high = close + np.random.uniform(0, 2, n)
    low = close - np.random.uniform(0, 2, n)
    volume = pd.Series(np.random.uniform(1000, 5000, n), name="volume")
    
    input_map = {"close": close, "closeadj": closeadj, "high": high, "low": low, "volume": volume}
    
    for name, info in F01_MOVING_AVERAGE_SYSTEMS_BASE_REGISTRY_076_150.items():
        func = info["func"]
        inputs = [input_map[arg] for arg in info["inputs"]]
        
        # Determinism check
        y1 = func(*inputs)
        y2 = func(*inputs)
        pd.testing.assert_series_equal(y1, y2)
        
        # Non-trivial output check
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, f"Feature {name} returned all NaNs after warmup"
        print(f"Feature {name}: OK")
