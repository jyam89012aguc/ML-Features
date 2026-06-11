# f15_cross_sectional_momentum_base_076_150_gemini.py
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

# Momentum Z-score for closeadj price over 252 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_252d_252l_v076_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 504 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_504d_252l_v077_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 504, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 63 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_63d_252l_v078_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 126 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_126d_252l_v079_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 252 days with 504-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_252d_504l_v080_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 252, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 504 days with 504-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_504d_504l_v081_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 21 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_21d_252l_v082_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 10 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_10d_252l_v083_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 10, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 5 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_5d_252l_v084_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 5, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 252 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_252d_252l_v085_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 504 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_504d_252l_v086_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 504, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 63 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_63d_252l_v087_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 126 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_126d_252l_v088_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 252 days with 504-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_252d_504l_v089_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 252, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 504 days with 504-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_504d_504l_v090_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 21 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_21d_252l_v091_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 10 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_10d_252l_v092_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 10, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 5 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_5d_252l_v093_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 5, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 756 days
def f15csm_f15_cross_sectional_momentum_persistence_756d_v094_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 1008 days
def f15csm_f15_cross_sectional_momentum_persistence_1008d_v095_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 1260 days
def f15csm_f15_cross_sectional_momentum_persistence_1260d_v096_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 252 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_252d_252l_v097_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 504 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_504d_252l_v098_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 504, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 63 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_63d_252l_v099_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 126 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_126d_252l_v100_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 252 days with 504-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_252d_504l_v101_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 252, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 504 days with 504-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_504d_504l_v102_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 21 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_21d_252l_v103_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 10 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_10d_252l_v104_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 10, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 5 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_5d_252l_v105_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 5, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 252 days vs 252 days

# Momentum acceleration for closeadj price over 504 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_504d_252d_v107_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 504, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 63 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_63d_252d_v108_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 126 days vs 252 days

# Momentum acceleration for closeadj price over 252 days vs 504 days
def f15csm_f15_cross_sectional_momentum_acceleration_252d_504d_v110_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 252, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 504 days vs 504 days
def f15csm_f15_cross_sectional_momentum_acceleration_504d_504d_v111_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 21 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_21d_252d_v112_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    roc1 = (close - close.shift(21)) / close.shift(21).abs().replace(0, np.nan)
    roc2 = (closeadj.shift(252) - closeadj.shift(21 + 252)) / closeadj.shift(21 + 252).abs().replace(0, np.nan)
    res = (roc1 - roc2)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 10 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_10d_252d_v113_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    roc1 = (close - close.shift(10)) / close.shift(10).abs().replace(0, np.nan)
    roc2 = (closeadj.shift(252) - closeadj.shift(10 + 252)) / closeadj.shift(10 + 252).abs().replace(0, np.nan)
    res = (roc1 - roc2)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 5 days vs 252 days
def f15csm_f15_cross_sectional_momentum_acceleration_5d_252d_v114_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    roc1 = (close - close.shift(5)) / close.shift(5).abs().replace(0, np.nan)
    roc2 = (closeadj.shift(252) - closeadj.shift(5 + 252)) / closeadj.shift(5 + 252).abs().replace(0, np.nan)
    res = (roc1 - roc2)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 15 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_15d_21l_v115_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 15, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 45 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_45d_63l_v116_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 45, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 90 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_90d_126l_v117_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 90, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 180 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_180d_252l_v118_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 180, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 15 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_15d_21l_v119_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 15, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 45 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_45d_63l_v120_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 45, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 90 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_90d_126l_v121_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 90, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 180 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_180d_252l_v122_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 180, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 15 days
def f15csm_f15_cross_sectional_momentum_persistence_15d_v123_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 45 days
def f15csm_f15_cross_sectional_momentum_persistence_45d_v124_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 90 days
def f15csm_f15_cross_sectional_momentum_persistence_90d_v125_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 180 days
def f15csm_f15_cross_sectional_momentum_persistence_180d_v126_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 180)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for close price over 15 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_15d_21l_v127_signal(close: pd.Series) -> pd.Series:
    res = _mom_standardized(close, 15, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 45 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_45d_63l_v128_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 45, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 90 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_90d_126l_v129_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 90, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Standardized momentum for closeadj price over 180 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_standardized_180d_252l_v130_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_standardized(closeadj, 180, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for close price over 15 days vs 15 days
def f15csm_f15_cross_sectional_momentum_acceleration_15d_15d_v131_signal(close: pd.Series) -> pd.Series:
    res = _mom_acceleration(close, 15, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 45 days vs 45 days
def f15csm_f15_cross_sectional_momentum_acceleration_45d_45d_v132_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 45, 45)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 90 days vs 90 days
def f15csm_f15_cross_sectional_momentum_acceleration_90d_90d_v133_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 90, 90)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum acceleration for closeadj price over 180 days vs 180 days
def f15csm_f15_cross_sectional_momentum_acceleration_180d_180d_v134_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_acceleration(closeadj, 180, 180)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 7 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_7d_21l_v135_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 7, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for close price over 14 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_14d_21l_v136_signal(close: pd.Series) -> pd.Series:
    res = _mom_zscore(close, 14, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 28 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_28d_63l_v137_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 28, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 56 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_56d_63l_v138_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 56, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 112 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_112d_126l_v139_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 112, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Z-score for closeadj price over 224 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_zscore_224d_252l_v140_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_zscore(closeadj, 224, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 7 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_7d_21l_v141_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 7, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for close price over 14 days with 21-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_14d_21l_v142_signal(close: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(close, 14, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 28 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_28d_63l_v143_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 28, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 56 days with 63-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_56d_63l_v144_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 56, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 112 days with 126-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_112d_126l_v145_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 112, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum percentile proxy for closeadj price over 224 days with 252-day lookback
def f15csm_f15_cross_sectional_momentum_percentile_224d_252l_v146_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_percentile_proxy(closeadj, 224, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 7 days
def f15csm_f15_cross_sectional_momentum_persistence_7d_v147_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 7)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for close price over 14 days
def f15csm_f15_cross_sectional_momentum_persistence_14d_v148_signal(close: pd.Series) -> pd.Series:
    res = _mom_persistence(close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 28 days
def f15csm_f15_cross_sectional_momentum_persistence_28d_v149_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 28)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum persistence for closeadj price over 56 days
def f15csm_f15_cross_sectional_momentum_persistence_56d_v150_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_persistence(closeadj, 56)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f15csm_") and f.endswith("_signal")]

F15_CROSS_SECTIONAL_MOMENTUM_BASE_REGISTRY_076_150 = {
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
    sz = 1500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F15_CROSS_SECTIONAL_MOMENTUM_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
