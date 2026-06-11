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

# Features 001-007: SMA Distance
# (close - sma5) / sma5
def f01ma_f01_moving_average_systems_sma_dist_5d_base_v001_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 5)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (close - sma10) / sma10
def f01ma_f01_moving_average_systems_sma_dist_10d_base_v002_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 10)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (close - sma21) / sma21
def f01ma_f01_moving_average_systems_sma_dist_21d_base_v003_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 21)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - sma42) / sma42
def f01ma_f01_moving_average_systems_sma_dist_42d_base_v004_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 42)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - sma63) / sma63
def f01ma_f01_moving_average_systems_sma_dist_63d_base_v005_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 63)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - sma126) / sma126
def f01ma_f01_moving_average_systems_sma_dist_126d_base_v006_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 126)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - sma252) / sma252
def f01ma_f01_moving_average_systems_sma_dist_252d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# Features 008-014: EMA Distance
# (close - ema5) / ema5
def f01ma_f01_moving_average_systems_ema_dist_5d_base_v008_signal(close: pd.Series) -> pd.Series:
    ma = _ema(close, 5)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (close - ema10) / ema10
def f01ma_f01_moving_average_systems_ema_dist_10d_base_v009_signal(close: pd.Series) -> pd.Series:
    ma = _ema(close, 10)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (close - ema21) / ema21
def f01ma_f01_moving_average_systems_ema_dist_21d_base_v010_signal(close: pd.Series) -> pd.Series:
    ma = _ema(close, 21)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - ema42) / ema42
def f01ma_f01_moving_average_systems_ema_dist_42d_base_v011_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 42)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - ema63) / ema63
def f01ma_f01_moving_average_systems_ema_dist_63d_base_v012_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 63)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - ema126) / ema126
def f01ma_f01_moving_average_systems_ema_dist_126d_base_v013_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 126)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - ema252) / ema252
def f01ma_f01_moving_average_systems_ema_dist_252d_base_v014_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 252)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# Features 015-021: WMA Distance
# (close - wma5) / wma5
def f01ma_f01_moving_average_systems_wma_dist_5d_base_v015_signal(close: pd.Series) -> pd.Series:
    ma = _wma(close, 5)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (close - wma10) / wma10
def f01ma_f01_moving_average_systems_wma_dist_10d_base_v016_signal(close: pd.Series) -> pd.Series:
    ma = _wma(close, 10)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (close - wma21) / wma21
def f01ma_f01_moving_average_systems_wma_dist_21d_base_v017_signal(close: pd.Series) -> pd.Series:
    ma = _wma(close, 21)
    return _ma_distance(close, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - wma42) / wma42
def f01ma_f01_moving_average_systems_wma_dist_42d_base_v018_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 42)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - wma63) / wma63
def f01ma_f01_moving_average_systems_wma_dist_63d_base_v019_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 63)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - wma126) / wma126
def f01ma_f01_moving_average_systems_wma_dist_126d_base_v020_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 126)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# (closeadj - wma252) / wma252
def f01ma_f01_moving_average_systems_wma_dist_252d_base_v021_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 252)
    return _ma_distance(closeadj, ma).replace([np.inf, -np.inf], np.nan)

# Features 022-028: SMA Alignment
# (sma5 - sma21) / sma21
def f01ma_f01_moving_average_systems_sma_alignment_5_21d_base_v022_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 5), _sma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (sma10 - sma42) / sma42
def f01ma_f01_moving_average_systems_sma_alignment_10_42d_base_v023_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 10), _sma(closeadj, 42)).replace([np.inf, -np.inf], np.nan)

# (sma21 - sma63) / sma63
def f01ma_f01_moving_average_systems_sma_alignment_21_63d_base_v024_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 21), _sma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (sma42 - sma126) / sma126
def f01ma_f01_moving_average_systems_sma_alignment_42_126d_base_v025_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(closeadj, 42), _sma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# (sma63 - sma252) / sma252
def f01ma_f01_moving_average_systems_sma_alignment_63_252d_base_v026_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(closeadj, 63), _sma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (sma5 - sma63) / sma63
def f01ma_f01_moving_average_systems_sma_alignment_5_63d_base_v027_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 5), _sma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (sma10 - sma126) / sma126
def f01ma_f01_moving_average_systems_sma_alignment_10_126d_base_v028_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 10), _sma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# Features 029-035: EMA Alignment
# (ema5 - ema21) / ema21
def f01ma_f01_moving_average_systems_ema_alignment_5_21d_base_v029_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 5), _ema(close, 21)).replace([np.inf, -np.inf], np.nan)

# (ema10 - ema42) / ema42
def f01ma_f01_moving_average_systems_ema_alignment_10_42d_base_v030_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 10), _ema(closeadj, 42)).replace([np.inf, -np.inf], np.nan)

# (ema21 - ema63) / ema63
def f01ma_f01_moving_average_systems_ema_alignment_21_63d_base_v031_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 21), _ema(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (ema42 - ema126) / ema126
def f01ma_f01_moving_average_systems_ema_alignment_42_126d_base_v032_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(closeadj, 42), _ema(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# (ema63 - ema252) / ema252
def f01ma_f01_moving_average_systems_ema_alignment_63_252d_base_v033_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(closeadj, 63), _ema(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (ema5 - ema63) / ema63
def f01ma_f01_moving_average_systems_ema_alignment_5_63d_base_v034_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 5), _ema(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (ema10 - ema126) / ema126
def f01ma_f01_moving_average_systems_ema_alignment_10_126d_base_v035_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_ema(close, 10), _ema(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# Features 036-042: WMA Alignment
# (wma5 - wma21) / wma21
def f01ma_f01_moving_average_systems_wma_alignment_5_21d_base_v036_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 5), _wma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (wma10 - wma42) / wma42
def f01ma_f01_moving_average_systems_wma_alignment_10_42d_base_v037_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 10), _wma(closeadj, 42)).replace([np.inf, -np.inf], np.nan)

# (wma21 - wma63) / wma63
def f01ma_f01_moving_average_systems_wma_alignment_21_63d_base_v038_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 21), _wma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (wma42 - wma126) / wma126
def f01ma_f01_moving_average_systems_wma_alignment_42_126d_base_v039_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(closeadj, 42), _wma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# (wma63 - wma252) / wma252
def f01ma_f01_moving_average_systems_wma_alignment_63_252d_base_v040_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(closeadj, 63), _wma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (wma5 - wma63) / wma63
def f01ma_f01_moving_average_systems_wma_alignment_5_63d_base_v041_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 5), _wma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (wma10 - wma126) / wma126
def f01ma_f01_moving_average_systems_wma_alignment_10_126d_base_v042_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 10), _wma(closeadj, 126)).replace([np.inf, -np.inf], np.nan)

# Features 043-049: SMA Relative Slope (5d lookback)
# (sma5 - sma5.shift(5)) / sma5.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_5d_base_v043_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(close, 5), 5).replace([np.inf, -np.inf], np.nan)

# (sma10 - sma10.shift(5)) / sma10.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_10d_base_v044_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(close, 10), 5).replace([np.inf, -np.inf], np.nan)

# (sma21 - sma21.shift(5)) / sma21.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_21d_base_v045_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(close, 21), 5).replace([np.inf, -np.inf], np.nan)

# (sma42 - sma42.shift(5)) / sma42.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_42d_base_v046_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(closeadj, 42), 5).replace([np.inf, -np.inf], np.nan)

# (sma63 - sma63.shift(5)) / sma63.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_63d_base_v047_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(closeadj, 63), 5).replace([np.inf, -np.inf], np.nan)

# (sma126 - sma126.shift(5)) / sma126.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_126d_base_v048_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(closeadj, 126), 5).replace([np.inf, -np.inf], np.nan)

# (sma252 - sma252.shift(5)) / sma252.shift(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_252d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_sma(closeadj, 252), 5).replace([np.inf, -np.inf], np.nan)

# Features 050-056: EMA Relative Slope (5d lookback)
# (ema5 - ema5.shift(5)) / ema5.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_5d_base_v050_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(close, 5), 5).replace([np.inf, -np.inf], np.nan)

# (ema10 - ema10.shift(5)) / ema10.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_10d_base_v051_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(close, 10), 5).replace([np.inf, -np.inf], np.nan)

# (ema21 - ema21.shift(5)) / ema21.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_21d_base_v052_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(close, 21), 5).replace([np.inf, -np.inf], np.nan)

# (ema42 - ema42.shift(5)) / ema42.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_42d_base_v053_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(closeadj, 42), 5).replace([np.inf, -np.inf], np.nan)

# (ema63 - ema63.shift(5)) / ema63.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_63d_base_v054_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(closeadj, 63), 5).replace([np.inf, -np.inf], np.nan)

# (ema126 - ema126.shift(5)) / ema126.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_126d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(closeadj, 126), 5).replace([np.inf, -np.inf], np.nan)

# (ema252 - ema252.shift(5)) / ema252.shift(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_252d_base_v056_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_ema(closeadj, 252), 5).replace([np.inf, -np.inf], np.nan)

# Features 057-063: WMA Relative Slope (5d lookback)
# (wma5 - wma5.shift(5)) / wma5.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_5d_base_v057_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(close, 5), 5).replace([np.inf, -np.inf], np.nan)

# (wma10 - wma10.shift(5)) / wma10.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_10d_base_v058_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(close, 10), 5).replace([np.inf, -np.inf], np.nan)

# (wma21 - wma21.shift(5)) / wma21.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_21d_base_v059_signal(close: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(close, 21), 5).replace([np.inf, -np.inf], np.nan)

# (wma42 - wma42.shift(5)) / wma42.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_42d_base_v060_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(closeadj, 42), 5).replace([np.inf, -np.inf], np.nan)

# (wma63 - wma63.shift(5)) / wma63.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_63d_base_v061_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(closeadj, 63), 5).replace([np.inf, -np.inf], np.nan)

# (wma126 - wma126.shift(5)) / wma126.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_126d_base_v062_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(closeadj, 126), 5).replace([np.inf, -np.inf], np.nan)

# (wma252 - wma252.shift(5)) / wma252.shift(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_252d_base_v063_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_rel_slope(_wma(closeadj, 252), 5).replace([np.inf, -np.inf], np.nan)

# Features 064-069: Mixed Alignments
# (sma21 - ema21) / ema21
def f01ma_f01_moving_average_systems_ma_alignment_sma21_ema21_base_v064_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(close, 21), _ema(close, 21)).replace([np.inf, -np.inf], np.nan)

# (sma63 - ema63) / ema63
def f01ma_f01_moving_average_systems_ma_alignment_sma63_ema63_base_v065_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(closeadj, 63), _ema(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (sma252 - ema252) / ema252
def f01ma_f01_moving_average_systems_ma_alignment_sma252_ema252_base_v066_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_sma(closeadj, 252), _ema(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# (wma21 - sma21) / sma21
def f01ma_f01_moving_average_systems_ma_alignment_wma21_sma21_base_v067_signal(close: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(close, 21), _sma(close, 21)).replace([np.inf, -np.inf], np.nan)

# (wma63 - sma63) / sma63
def f01ma_f01_moving_average_systems_ma_alignment_wma63_sma63_base_v068_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(closeadj, 63), _sma(closeadj, 63)).replace([np.inf, -np.inf], np.nan)

# (wma252 - sma252) / sma252
def f01ma_f01_moving_average_systems_ma_alignment_wma252_sma252_base_v069_signal(closeadj: pd.Series) -> pd.Series:
    return _ma_alignment(_wma(closeadj, 252), _sma(closeadj, 252)).replace([np.inf, -np.inf], np.nan)

# Features 070-075: Z-scores of distances
# zscore((close - sma21) / sma21, 63)
def f01ma_f01_moving_average_systems_sma_dist_zscore_21_63d_base_v070_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(close, _sma(close, 21))
    return _z(dist, 63).replace([np.inf, -np.inf], np.nan)

# zscore((close - ema21) / ema21, 63)
def f01ma_f01_moving_average_systems_ema_dist_zscore_21_63d_base_v071_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(close, _ema(close, 21))
    return _z(dist, 63).replace([np.inf, -np.inf], np.nan)

# zscore((closeadj - sma63) / sma63, 126)
def f01ma_f01_moving_average_systems_sma_dist_zscore_63_126d_base_v072_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _sma(closeadj, 63))
    return _z(dist, 126).replace([np.inf, -np.inf], np.nan)

# zscore((closeadj - ema63) / ema63, 126)
def f01ma_f01_moving_average_systems_ema_dist_zscore_63_126d_base_v073_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _ema(closeadj, 63))
    return _z(dist, 126).replace([np.inf, -np.inf], np.nan)

# zscore((closeadj - sma252) / sma252, 252)
def f01ma_f01_moving_average_systems_sma_dist_zscore_252_252d_base_v074_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _sma(closeadj, 252))
    return _z(dist, 252).replace([np.inf, -np.inf], np.nan)

# zscore((closeadj - ema252) / ema252, 252)
def f01ma_f01_moving_average_systems_ema_dist_zscore_252_252d_base_v075_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _ema(closeadj, 252))
    return _z(dist, 252).replace([np.inf, -np.inf], np.nan)

F01_MOVING_AVERAGE_SYSTEMS_BASE_REGISTRY_001_075 = {
    name: {
        "func": globals()[name],
        "inputs": [arg for arg in ["close", "closeadj"] if arg in globals()[name].__code__.co_varnames]
    }
    for name in globals() if name.startswith("f01ma_f01_moving_average_systems_")
}

if __name__ == "__main__":
    import numpy as np
    np.random.seed(42)
    n = 800
    close = pd.Series(np.random.normal(100, 5, n), name="close")
    closeadj = close * 1.05 # synthetic adjusted close
    
    input_map = {"close": close, "closeadj": closeadj}
    
    for name, info in F01_MOVING_AVERAGE_SYSTEMS_BASE_REGISTRY_001_075.items():
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
