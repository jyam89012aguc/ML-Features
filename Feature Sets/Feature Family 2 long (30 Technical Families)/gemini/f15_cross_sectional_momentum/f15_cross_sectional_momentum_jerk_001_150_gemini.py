# f15_cross_sectional_momentum_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _mom_zscore(price, w, lookback):
    roc = (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
    return (roc - roc.rolling(lookback).mean()) / roc.rolling(lookback).std().replace(0, np.nan)

def _mom_percentile_proxy(price, w, lookback):
    roc = (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
    return roc.rolling(lookback).rank(pct=True)

def _mom_persistence(price, w):
    roc = (price - price.shift(1)) / price.shift(1).abs().replace(0, np.nan)
    return (roc > 0).astype(float).rolling(w).mean()

def _mom_standardized(price, w, lookback):
    roc = (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
    return roc / roc.rolling(lookback).std().replace(0, np.nan)

def _mom_acceleration(price, w1, w2):
    roc1 = (price - price.shift(w1)) / price.shift(w1).abs().replace(0, np.nan)
    roc2 = (price.shift(w2) - price.shift(w1 + w2)) / price.shift(w1 + w2).abs().replace(0, np.nan)
    return (roc1 - roc2)

# Jerk of Momentum Z-score (5d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_5d_21l_jerk_5d_5d_v001_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 5, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (10d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_10d_21l_jerk_5d_5d_v002_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 10, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_21l_jerk_5d_5d_v003_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (63d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_zscore_63d_63l_jerk_21d_21d_v004_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 63, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (126d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_zscore_126d_63l_jerk_21d_21d_v005_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 126, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (252d, 63l) over (63d, 63d)
def f15csm_f15_cross_sectional_momentum_zscore_252d_63l_jerk_63d_63d_v006_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 252, 63)
    res = base.pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (5d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_5d_21l_jerk_5d_5d_v007_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 5, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (10d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_10d_21l_jerk_5d_5d_v008_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 10, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_21l_jerk_5d_5d_v009_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (63d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_percentile_63d_63l_jerk_21d_21d_v010_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 63, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (126d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_percentile_126d_63l_jerk_21d_21d_v011_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 126, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (252d, 63l) over (63d, 63d)
def f15csm_f15_cross_sectional_momentum_percentile_252d_63l_jerk_63d_63d_v012_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 252, 63)
    res = base.pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (5d) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_persistence_5d_jerk_5d_5d_v013_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 5)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (10d) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_persistence_10d_jerk_5d_5d_v014_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 10)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (21d) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_persistence_21d_jerk_5d_5d_v015_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (63d) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_persistence_63d_jerk_21d_21d_v016_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (126d) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_persistence_126d_jerk_21d_21d_v017_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 126)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (252d) over (63d, 63d)
def f15csm_f15_cross_sectional_momentum_persistence_252d_jerk_63d_63d_v018_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 252)
    res = base.pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (5d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_standardized_5d_21l_jerk_5d_5d_v019_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 5, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (10d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_standardized_10d_21l_jerk_5d_5d_v020_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 10, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (21d, 21l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_standardized_21d_21l_jerk_5d_5d_v021_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 21, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (63d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_standardized_63d_63l_jerk_21d_21d_v022_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 63, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (126d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_standardized_126d_63l_jerk_21d_21d_v023_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 126, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (252d, 63l) over (63d, 63d)
def f15csm_f15_cross_sectional_momentum_standardized_252d_63l_jerk_63d_63d_v024_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 252, 63)
    res = base.pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (5d, 5d) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_acceleration_5d_5d_jerk_5d_5d_v025_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 5, 5)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (10d, 10d) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_acceleration_10d_10d_jerk_5d_5d_v026_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 10, 10)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (21d, 21d) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_acceleration_21d_21d_jerk_5d_5d_v027_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 21, 21)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (63d, 63d) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_acceleration_63d_63d_jerk_21d_21d_v028_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 63, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (126d, 126d) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_acceleration_126d_126d_jerk_21d_21d_v029_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 126, 126)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (252d, 252d) over (63d, 63d)
def f15csm_f15_cross_sectional_momentum_acceleration_252d_252d_jerk_63d_63d_v030_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 252, 252)
    res = base.pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (5d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_5d_21l_jerk_10d_5d_v031_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 5, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (10d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_10d_21l_jerk_10d_5d_v032_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 10, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_21l_jerk_10d_5d_v033_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (63d, 63l) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_zscore_63d_63l_jerk_42d_21d_v034_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 63, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (126d, 63l) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_zscore_126d_63l_jerk_42d_21d_v035_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 126, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (252d, 63l) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_zscore_252d_63l_jerk_126d_63d_v036_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 252, 63)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (5d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_5d_21l_jerk_10d_5d_v037_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 5, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (10d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_10d_21l_jerk_10d_5d_v038_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 10, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_21l_jerk_10d_5d_v039_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (63d, 63l) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_percentile_63d_63l_jerk_42d_21d_v040_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 63, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (126d, 63l) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_percentile_126d_63l_jerk_42d_21d_v041_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 126, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (252d, 63l) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_percentile_252d_63l_jerk_126d_63d_v042_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 252, 63)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (5d) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_persistence_5d_jerk_10d_5d_v043_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 5)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (10d) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_persistence_10d_jerk_10d_5d_v044_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 10)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (21d) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_persistence_21d_jerk_10d_5d_v045_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (63d) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_persistence_63d_jerk_42d_21d_v046_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (126d) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_persistence_126d_jerk_42d_21d_v047_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 126)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (252d) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_persistence_252d_jerk_126d_63d_v048_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 252)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (5d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_standardized_5d_21l_jerk_10d_5d_v049_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 5, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (10d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_standardized_10d_21l_jerk_10d_5d_v050_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 10, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (21d, 21l) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_standardized_21d_21l_jerk_10d_5d_v051_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 21, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (63d, 63l) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_standardized_63d_63l_jerk_42d_21d_v052_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 63, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (126d, 63l) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_standardized_126d_63l_jerk_42d_21d_v053_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 126, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (252d, 63l) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_standardized_252d_63l_jerk_126d_63d_v054_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 252, 63)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (5d, 5d) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_acceleration_5d_5d_jerk_10d_5d_v055_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 5, 5)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (10d, 10d) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_acceleration_10d_10d_jerk_10d_5d_v056_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 10, 10)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (21d, 21d) over (10d, 5d)
def f15csm_f15_cross_sectional_momentum_acceleration_21d_21d_jerk_10d_5d_v057_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 21, 21)
    res = base.pct_change(10).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (63d, 63d) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_acceleration_63d_63d_jerk_42d_21d_v058_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 63, 63)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (126d, 126d) over (42d, 21d)
def f15csm_f15_cross_sectional_momentum_acceleration_126d_126d_jerk_42d_21d_v059_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 126, 126)
    res = base.pct_change(42).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (252d, 252d) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_acceleration_252d_252d_jerk_126d_63d_v060_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 252, 252)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (5d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_5d_21l_jerk_21d_10d_v061_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 5, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (10d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_10d_21l_jerk_21d_10d_v062_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 10, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_21l_jerk_21d_10d_v063_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (63d, 63l) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_zscore_63d_63l_jerk_63d_42d_v064_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 63, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (126d, 63l) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_zscore_126d_63l_jerk_63d_42d_v065_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 126, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (5d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_5d_21l_jerk_21d_10d_v066_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 5, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (10d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_10d_21l_jerk_21d_10d_v067_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 10, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_21l_jerk_21d_10d_v068_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (63d, 63l) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_percentile_63d_63l_jerk_63d_42d_v069_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 63, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (126d, 63l) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_percentile_126d_63l_jerk_63d_42d_v070_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 126, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (5d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_persistence_5d_jerk_21d_10d_v071_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 5)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (10d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_persistence_10d_jerk_21d_10d_v072_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 10)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (21d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_persistence_21d_jerk_21d_10d_v073_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (63d) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_persistence_63d_jerk_63d_42d_v074_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (126d) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_persistence_126d_jerk_63d_42d_v075_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 126)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (5d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_standardized_5d_21l_jerk_21d_10d_v076_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 5, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (10d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_standardized_10d_21l_jerk_21d_10d_v077_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 10, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (21d, 21l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_standardized_21d_21l_jerk_21d_10d_v078_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 21, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (63d, 63l) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_standardized_63d_63l_jerk_63d_42d_v079_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 63, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (126d, 63l) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_standardized_126d_63l_jerk_63d_42d_v080_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 126, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (5d, 5d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_acceleration_5d_5d_jerk_21d_10d_v081_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 5, 5)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (10d, 10d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_acceleration_10d_10d_jerk_21d_10d_v082_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 10, 10)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (21d, 21d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_acceleration_21d_21d_jerk_21d_10d_v083_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 21, 21)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (63d, 63d) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_acceleration_63d_63d_jerk_63d_42d_v084_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 63, 63)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (126d, 126d) over (63d, 42d)
def f15csm_f15_cross_sectional_momentum_acceleration_126d_126d_jerk_63d_42d_v085_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 126, 126)
    res = base.pct_change(63).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (252d, 126l) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_zscore_252d_126l_jerk_126d_63d_v086_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 252, 126)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (252d, 252l) over (252d, 126d)
def f15csm_f15_cross_sectional_momentum_zscore_252d_252l_jerk_252d_126d_v087_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 252, 252)
    res = base.pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (252d, 126l) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_percentile_252d_126l_jerk_126d_63d_v088_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 252, 126)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (252d, 252l) over (252d, 126d)
def f15csm_f15_cross_sectional_momentum_percentile_252d_252l_jerk_252d_126d_v089_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 252, 252)
    res = base.pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (504d) over (252d, 126d)
def f15csm_f15_cross_sectional_momentum_persistence_504d_jerk_252d_126d_v090_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 504)
    res = base.pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (252d, 126l) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_standardized_252d_126l_jerk_126d_63d_v091_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 252, 126)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (252d, 252l) over (252d, 126d)
def f15csm_f15_cross_sectional_momentum_standardized_252d_252l_jerk_252d_126d_v092_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 252, 252)
    res = base.pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (252d, 126d) over (126d, 63d)
def f15csm_f15_cross_sectional_momentum_acceleration_252d_126d_jerk_126d_63d_v093_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 252, 126)
    res = base.pct_change(126).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (252d, 252d) over (252d, 126d)
def f15csm_f15_cross_sectional_momentum_acceleration_252d_252d_jerk_252d_126d_v094_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 252, 252)
    res = base.pct_change(252).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (2d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_zscore_2d_21l_jerk_5d_2d_v095_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 2, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (3d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_zscore_3d_21l_jerk_5d_2d_v096_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 3, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (4d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_zscore_4d_21l_jerk_5d_2d_v097_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 4, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (1d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_zscore_1d_21l_jerk_5d_2d_v098_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 1, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (2d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_percentile_2d_21l_jerk_5d_2d_v099_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 2, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (3d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_percentile_3d_21l_jerk_5d_2d_v100_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 3, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (4d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_percentile_4d_21l_jerk_5d_2d_v101_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 4, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (1d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_percentile_1d_21l_jerk_5d_2d_v102_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 1, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (2d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_persistence_2d_jerk_5d_2d_v103_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 2)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (3d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_persistence_3d_jerk_5d_2d_v104_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 3)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (4d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_persistence_4d_jerk_5d_2d_v105_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 4)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (1d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_persistence_1d_jerk_5d_2d_v106_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 1)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (2d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_standardized_2d_21l_jerk_5d_2d_v107_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 2, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (3d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_standardized_3d_21l_jerk_5d_2d_v108_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 3, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (4d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_standardized_4d_21l_jerk_5d_2d_v109_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 4, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (1d, 21l) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_standardized_1d_21l_jerk_5d_2d_v110_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 1, 21)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (2d, 2d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_acceleration_2d_2d_jerk_5d_2d_v111_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 2, 2)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (3d, 3d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_acceleration_3d_3d_jerk_5d_2d_v112_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 3, 3)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (4d, 4d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_acceleration_4d_4d_jerk_5d_2d_v113_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 4, 4)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (1d, 1d) over (5d, 2d)
def f15csm_f15_cross_sectional_momentum_acceleration_1d_1d_jerk_5d_2d_v114_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 1, 1)
    res = base.pct_change(5).pct_change(2)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 126l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_126l_jerk_21d_10d_v115_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 126)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 252l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_252l_jerk_21d_10d_v116_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 252)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 126l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_126l_jerk_21d_10d_v117_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 126)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 252l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_252l_jerk_21d_10d_v118_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 252)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (42d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_persistence_42d_jerk_21d_10d_v119_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 42)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (21d, 126l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_standardized_21d_126l_jerk_21d_10d_v120_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 21, 126)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (21d, 252l) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_standardized_21d_252l_jerk_21d_10d_v121_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 21, 252)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (21d, 10d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_acceleration_21d_10d_jerk_21d_10d_v122_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 21, 10)
    res = base.pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (21d, 42d) over (21d, 10d)
def f15csm_f15_cross_sectional_momentum_acceleration_21d_42d_jerk_21d_10d_v123_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    roc1 = (close - close.shift(21)) / close.shift(21).abs().replace(0, np.nan)
    roc2 = (closeadj.shift(42) - closeadj.shift(21 + 42)) / closeadj.shift(21 + 42).abs().replace(0, np.nan)
    res = (roc1 - roc2).pct_change(21).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)


# Jerk of Momentum Z-score (15d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_zscore_15d_21l_jerk_15d_15d_v124_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 15, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (30d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_zscore_30d_21l_jerk_15d_15d_v125_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 30, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (45d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_zscore_45d_21l_jerk_15d_15d_v126_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_zscore(closeadj, 45, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (15d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_percentile_15d_21l_jerk_15d_15d_v127_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 15, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (30d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_percentile_30d_21l_jerk_15d_15d_v128_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 30, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (45d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_percentile_45d_21l_jerk_15d_15d_v129_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(closeadj, 45, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (15d) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_persistence_15d_jerk_15d_15d_v130_signal(close: pd.Series) -> pd.Series:
    base = _mom_persistence(close, 15)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (30d) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_persistence_30d_jerk_15d_15d_v131_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 30)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum persistence (45d) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_persistence_45d_jerk_15d_15d_v132_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_persistence(closeadj, 45)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (15d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_standardized_15d_21l_jerk_15d_15d_v133_signal(close: pd.Series) -> pd.Series:
    base = _mom_standardized(close, 15, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (30d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_standardized_30d_21l_jerk_15d_15d_v134_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 30, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Standardized momentum (45d, 21l) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_standardized_45d_21l_jerk_15d_15d_v135_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_standardized(closeadj, 45, 21)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (15d, 15d) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_acceleration_15d_15d_jerk_15d_15d_v136_signal(close: pd.Series) -> pd.Series:
    base = _mom_acceleration(close, 15, 15)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (30d, 30d) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_acceleration_30d_30d_jerk_15d_15d_v137_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 30, 30)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum acceleration (45d, 45d) over (15d, 15d)
def f15csm_f15_cross_sectional_momentum_acceleration_45d_45d_jerk_15d_15d_v138_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_acceleration(closeadj, 45, 45)
    res = base.pct_change(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (5d, 63l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_5d_63l_jerk_5d_5d_v139_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 5, 63)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (5d, 126l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_zscore_5d_126l_jerk_5d_5d_v140_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 5, 126)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (10d, 63l) over (10d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_10d_63l_jerk_10d_10d_v141_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 10, 63)
    res = base.pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (10d, 126l) over (10d, 10d)
def f15csm_f15_cross_sectional_momentum_zscore_10d_126l_jerk_10d_10d_v142_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 10, 126)
    res = base.pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_63l_jerk_21d_21d_v143_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum Z-score (21d, 126l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_zscore_21d_126l_jerk_21d_21d_v144_signal(close: pd.Series) -> pd.Series:
    base = _mom_zscore(close, 21, 126)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (5d, 63l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_5d_63l_jerk_5d_5d_v145_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 5, 63)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (5d, 126l) over (5d, 5d)
def f15csm_f15_cross_sectional_momentum_percentile_5d_126l_jerk_5d_5d_v146_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 5, 126)
    res = base.pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (10d, 63l) over (10d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_10d_63l_jerk_10d_10d_v147_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 10, 63)
    res = base.pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (10d, 126l) over (10d, 10d)
def f15csm_f15_cross_sectional_momentum_percentile_10d_126l_jerk_10d_10d_v148_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 10, 126)
    res = base.pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 63l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_63l_jerk_21d_21d_v149_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 63)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Momentum percentile proxy (21d, 126l) over (21d, 21d)
def f15csm_f15_cross_sectional_momentum_percentile_21d_126l_jerk_21d_21d_v150_signal(close: pd.Series) -> pd.Series:
    base = _mom_percentile_proxy(close, 21, 126)
    res = base.pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}

JERK_NAMES = [f for f in globals() if f.startswith("f15csm_") and f.endswith("_signal")]

F15_CROSS_SECTIONAL_MOMENTUM_JERK_REGISTRY_001_150 = {
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
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F15_CROSS_SECTIONAL_MOMENTUM_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
