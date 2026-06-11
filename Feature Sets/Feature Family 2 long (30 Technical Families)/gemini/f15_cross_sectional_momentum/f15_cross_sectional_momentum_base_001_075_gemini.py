# f15_cross_sectional_momentum_base_001_075_gemini.py
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

# Momentum Z-score for close price over 5 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_5d_21l_v001_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 10 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_10d_21l_v002_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 10, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 21 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_21d_21l_v003_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 63 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_63d_63l_v004_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 126 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_126d_63l_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 252 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_252d_63l_v006_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 252, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 5 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_5d_63l_v007_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 10 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_10d_63l_v008_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 21 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_21d_63l_v009_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 63 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_63d_126l_v010_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 63, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 126 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_126d_126l_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 252 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_252d_126l_v012_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 252, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 5 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_5d_126l_v013_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 5, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 10 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_10d_126l_v014_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 10, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 21 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_21d_126l_v015_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 5 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_5d_21l_v016_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 10 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_10d_21l_v017_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 10, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 21 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_21d_21l_v018_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 63 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_63d_63l_v019_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 126 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_126d_63l_v020_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 252 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_252d_63l_v021_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 252, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 5 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_5d_63l_v022_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 10 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_10d_63l_v023_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 21 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_21d_63l_v024_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 63 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_63d_126l_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 63, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 126 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_126d_126l_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 252 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_252d_126l_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 252, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 5 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_5d_126l_v028_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 5, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 10 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_10d_126l_v029_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 10, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 21 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_21d_126l_v030_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 5 days
def f15csm_f15_cross_sectional_momentum_persistence_5d_v031_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 10 days
def f15csm_f15_cross_sectional_momentum_persistence_10d_v032_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 21 days
def f15csm_f15_cross_sectional_momentum_persistence_21d_v033_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 63 days
def f15csm_f15_cross_sectional_momentum_persistence_63d_v034_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 126 days
def f15csm_f15_cross_sectional_momentum_persistence_126d_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 252 days
def f15csm_f15_cross_sectional_momentum_persistence_252d_v036_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 504 days
def f15csm_f15_cross_sectional_momentum_persistence_504d_v037_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 5 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_5d_21l_v038_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 10 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_10d_21l_v039_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 10, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 21 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_21d_21l_v040_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 63 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_63d_63l_v041_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 126 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_126d_63l_v042_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 126, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 252 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_252d_63l_v043_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 252, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 5 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_5d_63l_v044_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 10 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_10d_63l_v045_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 21 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_21d_63l_v046_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 63 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_63d_126l_v047_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 63, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 126 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_126d_126l_v048_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 252 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_252d_126l_v049_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 252, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 5 days vs 5 days
def f15csm_f15_cross_sectional_momentum_acceleration_5d_5d_v050_signal(close: pd.Series) -> pd.Series:
    res = _mom_acceleration(close, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 10 days vs 10 days
def f15csm_f15_cross_sectional_momentum_acceleration_10d_10d_v051_signal(close: pd.Series) -> pd.Series:
    res = _mom_acceleration(close, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 21 days vs 21 days
def f15csm_f15_cross_sectional_momentum_acceleration_21d_21d_v052_signal(close: pd.Series) -> pd.Series:
    res = _mom_acceleration(close, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 63 days vs 63 days
def f15csm_f15_cross_sectional_momentum_acceleration_63d_63d_v053_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 126 days vs 126 days
def f15csm_f15_cross_sectional_momentum_acceleration_126d_126d_v054_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 252 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_252d_252d_v055_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 5 days vs 10 days
def f15csm_f15_cross_sectional_momentum_acceleration_5d_10d_v056_signal(close: pd.Series) -> pd.Series:
    res = _mom_acceleration(close, 5, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 10 days vs 21 days
def f15csm_f15_cross_sectional_momentum_acceleration_10d_21d_v057_signal(close: pd.Series) -> pd.Series:
    res = _mom_acceleration(close, 10, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 21 days vs 63 days (mix)
def f15csm_f15_cross_sectional_momentum_acceleration_21d_63d_v058_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 63 days vs 126 days
def f15csm_f15_cross_sectional_momentum_acceleration_63d_126d_v059_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 63, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 126 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_126d_252d_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 2 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_2d_21l_v061_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 2, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 3 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_3d_21l_v062_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 3, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 4 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_4d_21l_v063_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 4, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 42 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_42d_63l_v064_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 42, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 84 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_84d_63l_v065_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 84, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 2 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_2d_21l_v066_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 2, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 3 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_3d_21l_v067_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 3, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 4 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_4d_21l_v068_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 4, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 42 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_42d_63l_v069_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 42, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 84 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_84d_63l_v070_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 84, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 2 days
def f15csm_f15_cross_sectional_momentum_persistence_2d_v071_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 3 days
def f15csm_f15_cross_sectional_momentum_persistence_3d_v072_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 4 days
def f15csm_f15_cross_sectional_momentum_persistence_4d_v073_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 4)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 42 days
def f15csm_f15_cross_sectional_momentum_persistence_42d_v074_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 84 days
def f15csm_f15_cross_sectional_momentum_persistence_84d_v075_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 84)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f15csm_") and f.endswith("_signal")]

F15_CROSS_SECTIONAL_MOMENTUM_BASE_REGISTRY_001_075 = {
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
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F15_CROSS_SECTIONAL_MOMENTUM_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
