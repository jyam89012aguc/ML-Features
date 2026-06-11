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

# Features 001-007: SMA Distance Jerk
# (sma_dist_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_dist_5d_jerk_v001_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 5)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_dist_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_dist_10d_jerk_v002_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 10)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_dist_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_dist_21d_jerk_v003_signal(close: pd.Series) -> pd.Series:
    ma = _sma(close, 21)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_dist_42d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_dist_42d_jerk_v004_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 42)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_dist_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_dist_63d_jerk_v005_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 63)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_dist_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_dist_126d_jerk_v006_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 126)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_dist_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_sma_dist_252d_jerk_v007_signal(closeadj: pd.Series) -> pd.Series:
    ma = _sma(closeadj, 252)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Features 008-014: EMA Distance Jerk
# (ema_dist_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_dist_5d_jerk_v008_signal(close: pd.Series) -> pd.Series:
    ma = _ema(close, 5)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_dist_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_dist_10d_jerk_v009_signal(close: pd.Series) -> pd.Series:
    ma = _ema(close, 10)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_dist_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_dist_21d_jerk_v010_signal(close: pd.Series) -> pd.Series:
    ma = _ema(close, 21)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_dist_42d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_dist_42d_jerk_v011_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 42)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_dist_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_dist_63d_jerk_v012_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 63)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_dist_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_dist_126d_jerk_v013_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 126)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_dist_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_ema_dist_252d_jerk_v014_signal(closeadj: pd.Series) -> pd.Series:
    ma = _ema(closeadj, 252)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Features 015-021: WMA Distance Jerk
# (wma_dist_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_dist_5d_jerk_v015_signal(close: pd.Series) -> pd.Series:
    ma = _wma(close, 5)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_dist_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_dist_10d_jerk_v016_signal(close: pd.Series) -> pd.Series:
    ma = _wma(close, 10)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_dist_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_dist_21d_jerk_v017_signal(close: pd.Series) -> pd.Series:
    ma = _wma(close, 21)
    res = _ma_distance(close, ma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_dist_42d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_dist_42d_jerk_v018_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 42)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_dist_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_dist_63d_jerk_v019_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 63)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_dist_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_dist_126d_jerk_v020_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 126)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_dist_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_wma_dist_252d_jerk_v021_signal(closeadj: pd.Series) -> pd.Series:
    ma = _wma(closeadj, 252)
    res = _ma_distance(closeadj, ma)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Features 022-028: SMA Alignment Jerk
# (sma_alignment_5_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_5_21d_jerk_v022_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 5), _sma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_10_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_10_42d_jerk_v023_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 10), _sma(closeadj, 42))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_21_63d_jerk_v024_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 21), _sma(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_42_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_alignment_42_126d_jerk_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(closeadj, 42), _sma(closeadj, 126))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_63_252d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_alignment_63_252d_jerk_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(closeadj, 63), _sma(closeadj, 252))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_5_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_5_63d_jerk_v027_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 5), _sma(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_10_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_10_126d_jerk_v028_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 10), _sma(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 029-035: EMA Alignment Jerk
# (ema_alignment_5_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_5_21d_jerk_v029_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 5), _ema(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_10_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_10_42d_jerk_v030_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 10), _ema(closeadj, 42))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_21_63d_jerk_v031_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 21), _ema(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_42_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_alignment_42_126d_jerk_v032_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(closeadj, 42), _ema(closeadj, 126))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_63_252d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_alignment_63_252d_jerk_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(closeadj, 63), _ema(closeadj, 252))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_5_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_5_63d_jerk_v034_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 5), _ema(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_10_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_10_126d_jerk_v035_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 10), _ema(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 036-042: WMA Alignment Jerk
# (wma_alignment_5_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_5_21d_jerk_v036_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 5), _wma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_10_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_10_42d_jerk_v037_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 10), _wma(closeadj, 42))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_21_63d_jerk_v038_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 21), _wma(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_42_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_alignment_42_126d_jerk_v039_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(closeadj, 42), _wma(closeadj, 126))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_63_252d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_alignment_63_252d_jerk_v040_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(closeadj, 63), _wma(closeadj, 252))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_5_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_5_63d_jerk_v041_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 5), _wma(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_10_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_10_126d_jerk_v042_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 10), _wma(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 043-049: SMA Relative Slope (5d lookback) Jerk
# (sma_rel_slope_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_5d_jerk_v043_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(close, 5), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_rel_slope_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_10d_jerk_v044_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(close, 10), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_rel_slope_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_21d_jerk_v045_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(close, 21), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_rel_slope_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_42d_jerk_v046_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(closeadj, 42), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_rel_slope_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_63d_jerk_v047_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(closeadj, 63), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_rel_slope_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_126d_jerk_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(closeadj, 126), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_rel_slope_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_rel_slope_252d_jerk_v049_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_sma(closeadj, 252), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 050-056: EMA Relative Slope (5d lookback) Jerk
# (ema_rel_slope_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_5d_jerk_v050_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(close, 5), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_rel_slope_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_10d_jerk_v051_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(close, 10), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_rel_slope_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_21d_jerk_v052_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(close, 21), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_rel_slope_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_42d_jerk_v053_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(closeadj, 42), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_rel_slope_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_63d_jerk_v054_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(closeadj, 63), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_rel_slope_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_126d_jerk_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(closeadj, 126), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_rel_slope_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_rel_slope_252d_jerk_v056_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_ema(closeadj, 252), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 057-063: WMA Relative Slope (5d lookback) Jerk
# (wma_rel_slope_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_5d_jerk_v057_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(close, 5), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_rel_slope_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_10d_jerk_v058_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(close, 10), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_rel_slope_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_21d_jerk_v059_signal(close: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(close, 21), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_rel_slope_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_42d_jerk_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(closeadj, 42), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_rel_slope_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_63d_jerk_v061_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(closeadj, 63), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_rel_slope_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_126d_jerk_v062_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(closeadj, 126), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_rel_slope_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_rel_slope_252d_jerk_v063_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_rel_slope(_wma(closeadj, 252), 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 064-069: Mixed Alignments Jerk
# (ma_alignment_sma21_ema21).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ma_alignment_sma21_ema21_jerk_v064_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 21), _ema(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ma_alignment_sma63_ema63).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ma_alignment_sma63_ema63_jerk_v065_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(closeadj, 63), _ema(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ma_alignment_sma252_ema252).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_ma_alignment_sma252_ema252_jerk_v066_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(closeadj, 252), _ema(closeadj, 252))
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# (ma_alignment_wma21_sma21).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ma_alignment_wma21_sma21_jerk_v067_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 21), _sma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ma_alignment_wma63_sma63).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ma_alignment_wma63_sma63_jerk_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(closeadj, 63), _sma(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ma_alignment_wma252_sma252).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_ma_alignment_wma252_sma252_jerk_v069_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(closeadj, 252), _sma(closeadj, 252))
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Features 070-075: Z-scores of distances Jerk
# (sma_dist_zscore_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_dist_zscore_21_63d_jerk_v070_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(close, _sma(close, 21))
    res = _z(dist, 63)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_dist_zscore_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_dist_zscore_21_63d_jerk_v071_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(close, _ema(close, 21))
    res = _z(dist, 63)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_dist_zscore_63_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_dist_zscore_63_126d_jerk_v072_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _sma(closeadj, 63))
    res = _z(dist, 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_dist_zscore_63_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_dist_zscore_63_126d_jerk_v073_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _ema(closeadj, 63))
    res = _z(dist, 126)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_dist_zscore_252_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_sma_dist_zscore_252_252d_jerk_v074_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _sma(closeadj, 252))
    res = _z(dist, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# (ema_dist_zscore_252_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_ema_dist_zscore_252_252d_jerk_v075_signal(closeadj: pd.Series) -> pd.Series:
    dist = _ma_distance(closeadj, _ema(closeadj, 252))
    res = _z(dist, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Features 076-082: SMA Alignment (Variations) Jerk
# (sma_alignment_10_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_10_21d_jerk_v076_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 10), _sma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_5_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_5_42d_jerk_v077_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 5), _sma(closeadj, 42))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_21_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_21_126d_jerk_v078_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 21), _sma(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_42_252d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_alignment_42_252d_jerk_v079_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(closeadj, 42), _sma(closeadj, 252))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_10_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_10_63d_jerk_v080_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 10), _sma(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_21_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_21_252d_jerk_v081_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 21), _sma(closeadj, 252))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_alignment_5_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_alignment_5_126d_jerk_v082_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_sma(close, 5), _sma(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 083-089: EMA Alignment (Variations) Jerk
# (ema_alignment_10_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_10_21d_jerk_v083_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 10), _ema(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_5_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_5_42d_jerk_v084_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 5), _ema(closeadj, 42))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_21_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_21_126d_jerk_v085_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 21), _ema(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_42_252d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_alignment_42_252d_jerk_v086_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(closeadj, 42), _ema(closeadj, 252))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_10_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_10_63d_jerk_v087_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 10), _ema(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_21_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_21_252d_jerk_v088_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 21), _ema(closeadj, 252))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_alignment_5_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_alignment_5_126d_jerk_v089_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_ema(close, 5), _ema(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 090-096: WMA Alignment (Variations) Jerk
# (wma_alignment_10_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_10_21d_jerk_v090_signal(close: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 10), _wma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_5_42d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_5_42d_jerk_v091_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 5), _wma(closeadj, 42))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_21_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_21_126d_jerk_v092_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 21), _wma(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_42_252d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_alignment_42_252d_jerk_v093_signal(closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(closeadj, 42), _wma(closeadj, 252))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_10_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_10_63d_jerk_v094_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 10), _wma(closeadj, 63))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_21_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_21_252d_jerk_v095_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 21), _wma(closeadj, 252))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_alignment_5_126d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_alignment_5_126d_jerk_v096_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_alignment(_wma(close, 5), _wma(closeadj, 126))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 097-103: High Distance to SMA Jerk
# (high_dist_sma_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_high_dist_sma_5d_jerk_v097_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(high, _sma(close, 5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (high_dist_sma_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_high_dist_sma_21d_jerk_v098_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(high, _sma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (high_dist_sma_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_high_dist_sma_63d_jerk_v099_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_distance(high, _sma(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (high_dist_ema_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_high_dist_ema_21d_jerk_v100_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(high, _ema(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (high_dist_ema_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_high_dist_ema_63d_jerk_v101_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_distance(high, _ema(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (high_dist_wma_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_high_dist_wma_21d_jerk_v102_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(high, _wma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (high_dist_wma_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_high_dist_wma_63d_jerk_v103_signal(high: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_distance(high, _wma(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 104-110: Low Distance to SMA Jerk
# (low_dist_sma_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_low_dist_sma_5d_jerk_v104_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(low, _sma(close, 5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (low_dist_sma_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_low_dist_sma_21d_jerk_v105_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(low, _sma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (low_dist_sma_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_low_dist_sma_63d_jerk_v106_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_distance(low, _sma(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (low_dist_ema_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_low_dist_ema_21d_jerk_v107_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(low, _ema(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (low_dist_ema_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_low_dist_ema_63d_jerk_v108_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_distance(low, _ema(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (low_dist_wma_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_low_dist_wma_21d_jerk_v109_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ma_distance(low, _wma(close, 21))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (low_dist_wma_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_low_dist_wma_63d_jerk_v110_signal(low: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _ma_distance(low, _wma(closeadj, 63))
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 111-117: VWMA Distance Jerk
# (vwma_dist_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_vwma_dist_5d_jerk_v111_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 5) / _sma(volume, 5).replace(0, np.nan)
    res = _ma_distance(close, vwma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (vwma_dist_10d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_vwma_dist_10d_jerk_v112_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 10) / _sma(volume, 10).replace(0, np.nan)
    res = _ma_distance(close, vwma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (vwma_dist_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_vwma_dist_21d_jerk_v113_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 21) / _sma(volume, 21).replace(0, np.nan)
    res = _ma_distance(close, vwma)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (vwma_dist_42d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_vwma_dist_42d_jerk_v114_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 42) / _sma(volume, 42).replace(0, np.nan)
    res = _ma_distance(closeadj, vwma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (vwma_dist_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_vwma_dist_63d_jerk_v115_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 63) / _sma(volume, 63).replace(0, np.nan)
    res = _ma_distance(closeadj, vwma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (vwma_dist_126d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_vwma_dist_126d_jerk_v116_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 126) / _sma(volume, 126).replace(0, np.nan)
    res = _ma_distance(closeadj, vwma)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (vwma_dist_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_vwma_dist_252d_jerk_v117_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(closeadj * volume, 252) / _sma(volume, 252).replace(0, np.nan)
    res = _ma_distance(closeadj, vwma)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# Features 118-124: Price Z-score Relative to SMA Jerk
# (price_zscore_5d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_price_zscore_5d_jerk_v118_signal(close: pd.Series) -> pd.Series:
    res = _z(close, 5)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (price_zscore_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_price_zscore_21d_jerk_v119_signal(close: pd.Series) -> pd.Series:
    res = _z(close, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (price_zscore_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_price_zscore_63d_jerk_v120_signal(closeadj: pd.Series) -> pd.Series:
    res = _z(closeadj, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (price_zscore_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_price_zscore_252d_jerk_v121_signal(closeadj: pd.Series) -> pd.Series:
    res = _z(closeadj, 252)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# (volume_zscore_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_volume_zscore_21d_jerk_v122_signal(volume: pd.Series) -> pd.Series:
    res = _z(volume, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (volume_zscore_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_volume_zscore_63d_jerk_v123_signal(volume: pd.Series) -> pd.Series:
    res = _z(volume, 63)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (range_zscore_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_range_zscore_21d_jerk_v124_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _z(high - low, 21)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 125-131: MA Stacking Jerk
# (ma_stack_rank_5_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ma_stack_rank_5_21_63d_jerk_v125_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    s5 = _sma(close, 5)
    s21 = _sma(close, 21)
    s63 = _sma(closeadj, 63)
    res = ((s5 > s21).astype(float) + (s21 > s63).astype(float)) / 2.0
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_stack_rank_5_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_stack_rank_5_21_63d_jerk_v126_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    e5 = _ema(close, 5)
    e21 = _ema(close, 21)
    e63 = _ema(closeadj, 63)
    res = ((e5 > e21).astype(float) + (e21 > e63).astype(float)) / 2.0
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ma_stack_rank_21_63_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ma_stack_rank_21_63_252d_jerk_v127_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    s21 = _sma(close, 21)
    s63 = _sma(closeadj, 63)
    s252 = _sma(closeadj, 252)
    res = ((s21 > s63).astype(float) + (s63 > s252).astype(float)) / 2.0
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_stack_rank_21_63_252d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_stack_rank_21_63_252d_jerk_v128_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    e21 = _ema(close, 21)
    e63 = _ema(closeadj, 63)
    e252 = _ema(closeadj, 252)
    res = ((e21 > e63).astype(float) + (e63 > e252).astype(float)) / 2.0
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_stack_rank_5_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_stack_rank_5_21_63d_jerk_v129_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    w5 = _wma(close, 5)
    w21 = _wma(close, 21)
    w63 = _wma(closeadj, 63)
    res = ((w5 > w21).astype(float) + (w21 > w63).astype(float)) / 2.0
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (vwma_stack_rank_21_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_vwma_stack_rank_21_63d_jerk_v130_signal(close: pd.Series, closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    vw21 = _sma(close * volume, 21) / _sma(volume, 21).replace(0, np.nan)
    s21 = _sma(close, 21)
    s63 = _sma(closeadj, 63)
    res = ((vw21 > s21).astype(float) + (s21 > s63).astype(float)) / 2.0
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (price_above_all_ma).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_price_above_all_ma_jerk_v131_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = ((close > _sma(close, 5)) & (close > _sma(close, 21)) & (close > _sma(closeadj, 63))).astype(float)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# Features 132-138: MA Stretch Jerk
# (sma_stretch_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_stretch_21d_jerk_v132_signal(close: pd.Series) -> pd.Series:
    res = (close - _sma(close, 21)) / (_max(close, 21) - _min(close, 21)).replace(0, np.nan)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_stretch_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_sma_stretch_63d_jerk_v133_signal(closeadj: pd.Series) -> pd.Series:
    res = (closeadj - _sma(closeadj, 63)) / (_max(closeadj, 63) - _min(closeadj, 63)).replace(0, np.nan)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (sma_stretch_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_sma_stretch_252d_jerk_v134_signal(closeadj: pd.Series) -> pd.Series:
    res = (closeadj - _sma(closeadj, 252)) / (_max(closeadj, 252) - _min(closeadj, 252)).replace(0, np.nan)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# (ema_stretch_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_stretch_21d_jerk_v135_signal(close: pd.Series) -> pd.Series:
    res = (close - _ema(close, 21)) / (_max(close, 21) - _min(close, 21)).replace(0, np.nan)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_stretch_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_stretch_63d_jerk_v136_signal(closeadj: pd.Series) -> pd.Series:
    res = (closeadj - _ema(closeadj, 63)) / (_max(closeadj, 63) - _min(closeadj, 63)).replace(0, np.nan)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_stretch_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_stretch_21d_jerk_v137_signal(close: pd.Series) -> pd.Series:
    res = (close - _wma(close, 21)) / (_max(close, 21) - _min(close, 21)).replace(0, np.nan)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_stretch_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_stretch_63d_jerk_v138_signal(closeadj: pd.Series) -> pd.Series:
    res = (closeadj - _wma(closeadj, 63)) / (_max(closeadj, 63) - _min(closeadj, 63)).replace(0, np.nan)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 139-145: MA Channel Position Jerk
# (ma_channel_pos_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ma_channel_pos_21d_jerk_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    s_low = _sma(low, 21)
    s_high = _sma(high, 21)
    res = (close - s_low) / (s_high - s_low).replace(0, np.nan)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ma_channel_pos_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ma_channel_pos_63d_jerk_v140_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    s_low = _sma(low, 63)
    s_high = _sma(high, 63)
    res = (closeadj - s_low) / (s_high - s_low).replace(0, np.nan)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (ma_channel_pos_252d).pct_change(63).diff(63)
def f01ma_f01_moving_average_systems_ma_channel_pos_252d_jerk_v141_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    s_low = _sma(low, 252)
    s_high = _sma(high, 252)
    res = (closeadj - s_low) / (s_high - s_low).replace(0, np.nan)
    return res.pct_change(63).diff(63).replace([np.inf, -np.inf], np.nan)

# (ema_channel_pos_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_channel_pos_21d_jerk_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    e_low = _ema(low, 21)
    e_high = _ema(high, 21)
    res = (close - e_low) / (e_high - e_low).replace(0, np.nan)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_channel_pos_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_ema_channel_pos_63d_jerk_v143_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    e_low = _ema(low, 63)
    e_high = _ema(high, 63)
    res = (closeadj - e_low) / (e_high - e_low).replace(0, np.nan)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# (wma_channel_pos_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_wma_channel_pos_21d_jerk_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    w_low = _wma(low, 21)
    w_high = _wma(high, 21)
    res = (close - w_low) / (w_high - w_low).replace(0, np.nan)
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (wma_channel_pos_63d).pct_change(21).diff(21)
def f01ma_f01_moving_average_systems_wma_channel_pos_63d_jerk_v145_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    w_low = _wma(low, 63)
    w_high = _wma(high, 63)
    res = (closeadj - w_low) / (w_high - w_low).replace(0, np.nan)
    return res.pct_change(21).diff(21).replace([np.inf, -np.inf], np.nan)

# Features 146-150: MA Acceleration Jerk
# (sma_accel_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_accel_21d_jerk_v146_signal(close: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_sma(close, 21), 5)
    res = (slope - slope.shift(5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_accel_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_accel_21d_jerk_v147_signal(close: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_ema(close, 21), 5)
    res = (slope - slope.shift(5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (sma_accel_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_sma_accel_63d_jerk_v148_signal(closeadj: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_sma(closeadj, 63), 5)
    res = (slope - slope.shift(5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (ema_accel_63d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_ema_accel_63d_jerk_v149_signal(closeadj: pd.Series) -> pd.Series:
    slope = _ma_rel_slope(_ema(closeadj, 63), 5)
    res = (slope - slope.shift(5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

# (vwma_accel_21d).pct_change(5).diff(5)
def f01ma_f01_moving_average_systems_vwma_accel_21d_jerk_v150_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    vwma = _sma(close * volume, 21) / _sma(volume, 21).replace(0, np.nan)
    slope = _ma_rel_slope(vwma, 5)
    res = (slope - slope.shift(5))
    return res.pct_change(5).diff(5).replace([np.inf, -np.inf], np.nan)

F01_MOVING_AVERAGE_SYSTEMS_JERK_REGISTRY = {
    name: {
        "func": globals()[name],
        "inputs": [arg for arg in ["high", "low", "close", "closeadj", "volume"] if arg in globals()[name].__code__.co_varnames]
    }
    for name in globals() if name.startswith("f01ma_f01_moving_average_systems_") and "jerk" in name
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
    
    for name, info in F01_MOVING_AVERAGE_SYSTEMS_JERK_REGISTRY.items():
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
