"""
113_volume_autocorrelation — Statistical Moments
Domain: volume_autocorrelation
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def vaut_376_vol_lag1_autocorr_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_376_vol_lag1_autocorr_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_lag1_autocorr over 5d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(5).skew()

def vaut_377_vol_lag1_autocorr_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_377_vol_lag1_autocorr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_lag1_autocorr over 5d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(5).kurt()

def vaut_378_vol_lag1_autocorr_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_378_vol_lag1_autocorr_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_lag1_autocorr over 21d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(21).skew()

def vaut_379_vol_lag1_autocorr_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_379_vol_lag1_autocorr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_lag1_autocorr over 21d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(21).kurt()

def vaut_380_vol_lag1_autocorr_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_380_vol_lag1_autocorr_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_lag1_autocorr over 63d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(63).skew()

def vaut_381_vol_lag1_autocorr_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_381_vol_lag1_autocorr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_lag1_autocorr over 63d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(63).kurt()

def vaut_382_vol_lag1_autocorr_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_382_vol_lag1_autocorr_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_lag1_autocorr over 126d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(126).skew()

def vaut_383_vol_lag1_autocorr_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_383_vol_lag1_autocorr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_lag1_autocorr over 126d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(126).kurt()

def vaut_384_vol_lag1_autocorr_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_384_vol_lag1_autocorr_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_lag1_autocorr over 252d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(252).skew()

def vaut_385_vol_lag1_autocorr_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_385_vol_lag1_autocorr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_lag1_autocorr over 252d. 21-day serial correlation of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(252).kurt()

def vaut_386_vol_autocorr_zscore_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_386_vol_autocorr_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_zscore over 5d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).skew()

def vaut_387_vol_autocorr_zscore_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_387_vol_autocorr_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_zscore over 5d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).kurt()

def vaut_388_vol_autocorr_zscore_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_388_vol_autocorr_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_zscore over 21d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).skew()

def vaut_389_vol_autocorr_zscore_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_389_vol_autocorr_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_zscore over 21d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).kurt()

def vaut_390_vol_autocorr_zscore_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_390_vol_autocorr_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_zscore over 63d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).skew()

def vaut_391_vol_autocorr_zscore_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_391_vol_autocorr_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_zscore over 63d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).kurt()

def vaut_392_vol_autocorr_zscore_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_392_vol_autocorr_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_zscore over 126d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).skew()

def vaut_393_vol_autocorr_zscore_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_393_vol_autocorr_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_zscore over 126d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).kurt()

def vaut_394_vol_autocorr_zscore_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_394_vol_autocorr_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_zscore over 252d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).skew()

def vaut_395_vol_autocorr_zscore_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_395_vol_autocorr_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_zscore over 252d. Anomaly in volume persistence.
    """
    return (_zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).kurt()

def vaut_396_vol_persistence_trend_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_396_vol_persistence_trend_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_persistence_trend over 5d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(5).skew()

def vaut_397_vol_persistence_trend_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_397_vol_persistence_trend_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_persistence_trend over 5d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(5).kurt()

def vaut_398_vol_persistence_trend_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_398_vol_persistence_trend_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_persistence_trend over 21d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(21).skew()

def vaut_399_vol_persistence_trend_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_399_vol_persistence_trend_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_persistence_trend over 21d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(21).kurt()

def vaut_400_vol_persistence_trend_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_400_vol_persistence_trend_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_persistence_trend over 63d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(63).skew()

def vaut_401_vol_persistence_trend_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_401_vol_persistence_trend_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_persistence_trend over 63d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(63).kurt()

def vaut_402_vol_persistence_trend_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_402_vol_persistence_trend_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_persistence_trend over 126d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(126).skew()

def vaut_403_vol_persistence_trend_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_403_vol_persistence_trend_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_persistence_trend over 126d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(126).kurt()

def vaut_404_vol_persistence_trend_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_404_vol_persistence_trend_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_persistence_trend over 252d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(252).skew()

def vaut_405_vol_persistence_trend_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_405_vol_persistence_trend_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_persistence_trend over 252d. Shift in volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(252).kurt()

def vaut_406_vol_clustering_index_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_406_vol_clustering_index_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_clustering_index over 5d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(5).skew()

def vaut_407_vol_clustering_index_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_407_vol_clustering_index_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_clustering_index over 5d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(5).kurt()

def vaut_408_vol_clustering_index_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_408_vol_clustering_index_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_clustering_index over 21d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(21).skew()

def vaut_409_vol_clustering_index_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_409_vol_clustering_index_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_clustering_index over 21d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(21).kurt()

def vaut_410_vol_clustering_index_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_410_vol_clustering_index_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_clustering_index over 63d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(63).skew()

def vaut_411_vol_clustering_index_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_411_vol_clustering_index_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_clustering_index over 63d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(63).kurt()

def vaut_412_vol_clustering_index_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_412_vol_clustering_index_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_clustering_index over 126d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(126).skew()

def vaut_413_vol_clustering_index_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_413_vol_clustering_index_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_clustering_index over 126d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(126).kurt()

def vaut_414_vol_clustering_index_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_414_vol_clustering_index_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_clustering_index over 252d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(252).skew()

def vaut_415_vol_clustering_index_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_415_vol_clustering_index_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_clustering_index over 252d. Autocorrelation of absolute volume changes.
    """
    return (volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))).rolling(252).kurt()

def vaut_416_vol_autocorr_rank_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_416_vol_autocorr_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_rank over 5d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).skew()

def vaut_417_vol_autocorr_rank_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_417_vol_autocorr_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_rank over 5d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).kurt()

def vaut_418_vol_autocorr_rank_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_418_vol_autocorr_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_rank over 21d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).skew()

def vaut_419_vol_autocorr_rank_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_419_vol_autocorr_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_rank over 21d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).kurt()

def vaut_420_vol_autocorr_rank_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_420_vol_autocorr_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_rank over 63d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).skew()

def vaut_421_vol_autocorr_rank_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_421_vol_autocorr_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_rank over 63d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).kurt()

def vaut_422_vol_autocorr_rank_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_422_vol_autocorr_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_rank over 126d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).skew()

def vaut_423_vol_autocorr_rank_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_423_vol_autocorr_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_rank over 126d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).kurt()

def vaut_424_vol_autocorr_rank_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_424_vol_autocorr_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_rank over 252d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).skew()

def vaut_425_vol_autocorr_rank_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_425_vol_autocorr_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_rank over 252d. Historical rank of volume persistence.
    """
    return (_rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).kurt()

def vaut_426_vol_autocorr_stability_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_426_vol_autocorr_stability_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_stability over 5d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(5).skew()

def vaut_427_vol_autocorr_stability_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_427_vol_autocorr_stability_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_stability over 5d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(5).kurt()

def vaut_428_vol_autocorr_stability_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_428_vol_autocorr_stability_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_stability over 21d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(21).skew()

def vaut_429_vol_autocorr_stability_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_429_vol_autocorr_stability_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_stability over 21d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(21).kurt()

def vaut_430_vol_autocorr_stability_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_430_vol_autocorr_stability_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_stability over 63d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(63).skew()

def vaut_431_vol_autocorr_stability_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_431_vol_autocorr_stability_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_stability over 63d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(63).kurt()

def vaut_432_vol_autocorr_stability_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_432_vol_autocorr_stability_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_stability over 126d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(126).skew()

def vaut_433_vol_autocorr_stability_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_433_vol_autocorr_stability_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_stability over 126d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(126).kurt()

def vaut_434_vol_autocorr_stability_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_434_vol_autocorr_stability_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_stability over 252d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(252).skew()

def vaut_435_vol_autocorr_stability_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_435_vol_autocorr_stability_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_stability over 252d. Stability of the volume persistence regime.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(252).kurt()

def vaut_436_vol_autocorr_acceleration_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_436_vol_autocorr_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_acceleration over 5d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(5).skew()

def vaut_437_vol_autocorr_acceleration_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_437_vol_autocorr_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_acceleration over 5d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(5).kurt()

def vaut_438_vol_autocorr_acceleration_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_438_vol_autocorr_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_acceleration over 21d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(21).skew()

def vaut_439_vol_autocorr_acceleration_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_439_vol_autocorr_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_acceleration over 21d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(21).kurt()

def vaut_440_vol_autocorr_acceleration_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_440_vol_autocorr_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_acceleration over 63d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(63).skew()

def vaut_441_vol_autocorr_acceleration_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_441_vol_autocorr_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_acceleration over 63d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(63).kurt()

def vaut_442_vol_autocorr_acceleration_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_442_vol_autocorr_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_acceleration over 126d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(126).skew()

def vaut_443_vol_autocorr_acceleration_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_443_vol_autocorr_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_acceleration over 126d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(126).kurt()

def vaut_444_vol_autocorr_acceleration_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_444_vol_autocorr_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_acceleration over 252d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(252).skew()

def vaut_445_vol_autocorr_acceleration_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_445_vol_autocorr_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_acceleration over 252d. Short-term change in volume persistence.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(252).kurt()

def vaut_446_vol_mean_reversion_flag_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_446_vol_mean_reversion_flag_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_flag over 5d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(5).skew()

def vaut_447_vol_mean_reversion_flag_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_447_vol_mean_reversion_flag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_flag over 5d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(5).kurt()

def vaut_448_vol_mean_reversion_flag_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_448_vol_mean_reversion_flag_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_flag over 21d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(21).skew()

def vaut_449_vol_mean_reversion_flag_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_449_vol_mean_reversion_flag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_flag over 21d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(21).kurt()

def vaut_450_vol_mean_reversion_flag_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_450_vol_mean_reversion_flag_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_flag over 63d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(63).skew()

def vaut_451_vol_mean_reversion_flag_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_451_vol_mean_reversion_flag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_flag over 63d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(63).kurt()

def vaut_452_vol_mean_reversion_flag_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_452_vol_mean_reversion_flag_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_flag over 126d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(126).skew()

def vaut_453_vol_mean_reversion_flag_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_453_vol_mean_reversion_flag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_flag over 126d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(126).kurt()

def vaut_454_vol_mean_reversion_flag_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_454_vol_mean_reversion_flag_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_flag over 252d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(252).skew()

def vaut_455_vol_mean_reversion_flag_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_455_vol_mean_reversion_flag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_flag over 252d. Volume mean-reverting regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)).rolling(252).kurt()

def vaut_456_vol_trend_persistence_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_456_vol_trend_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_trend_persistence over 5d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(5).skew()

def vaut_457_vol_trend_persistence_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_457_vol_trend_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_trend_persistence over 5d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(5).kurt()

def vaut_458_vol_trend_persistence_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_458_vol_trend_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_trend_persistence over 21d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(21).skew()

def vaut_459_vol_trend_persistence_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_459_vol_trend_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_trend_persistence over 21d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(21).kurt()

def vaut_460_vol_trend_persistence_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_460_vol_trend_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_trend_persistence over 63d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(63).skew()

def vaut_461_vol_trend_persistence_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_461_vol_trend_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_trend_persistence over 63d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(63).kurt()

def vaut_462_vol_trend_persistence_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_462_vol_trend_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_trend_persistence over 126d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(126).skew()

def vaut_463_vol_trend_persistence_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_463_vol_trend_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_trend_persistence over 126d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(126).kurt()

def vaut_464_vol_trend_persistence_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_464_vol_trend_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_trend_persistence over 252d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(252).skew()

def vaut_465_vol_trend_persistence_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_465_vol_trend_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_trend_persistence over 252d. Volume trending regime.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.2).astype(float)).rolling(252).kurt()

def vaut_466_vol_autocorr_vs_price_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_466_vol_autocorr_vs_price_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_vs_price over 5d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(5).skew()

def vaut_467_vol_autocorr_vs_price_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_467_vol_autocorr_vs_price_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_vs_price over 5d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(5).kurt()

def vaut_468_vol_autocorr_vs_price_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_468_vol_autocorr_vs_price_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_vs_price over 21d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(21).skew()

def vaut_469_vol_autocorr_vs_price_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_469_vol_autocorr_vs_price_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_vs_price over 21d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(21).kurt()

def vaut_470_vol_autocorr_vs_price_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_470_vol_autocorr_vs_price_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_vs_price over 63d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(63).skew()

def vaut_471_vol_autocorr_vs_price_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_471_vol_autocorr_vs_price_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_vs_price over 63d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(63).kurt()

def vaut_472_vol_autocorr_vs_price_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_472_vol_autocorr_vs_price_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_vs_price over 126d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(126).skew()

def vaut_473_vol_autocorr_vs_price_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_473_vol_autocorr_vs_price_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_vs_price over 126d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(126).kurt()

def vaut_474_vol_autocorr_vs_price_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_474_vol_autocorr_vs_price_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_vs_price over 252d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(252).skew()

def vaut_475_vol_autocorr_vs_price_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_475_vol_autocorr_vs_price_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_vs_price over 252d. Relationship between volume persistence and price direction.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.pct_change(1))).rolling(252).kurt()

def vaut_476_vol_autocorr_peak_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_476_vol_autocorr_peak_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_peak over 5d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(5).skew()

def vaut_477_vol_autocorr_peak_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_477_vol_autocorr_peak_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_peak over 5d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(5).kurt()

def vaut_478_vol_autocorr_peak_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_478_vol_autocorr_peak_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_peak over 21d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(21).skew()

def vaut_479_vol_autocorr_peak_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_479_vol_autocorr_peak_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_peak over 21d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(21).kurt()

def vaut_480_vol_autocorr_peak_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_480_vol_autocorr_peak_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_peak over 63d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(63).skew()

def vaut_481_vol_autocorr_peak_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_481_vol_autocorr_peak_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_peak over 63d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(63).kurt()

def vaut_482_vol_autocorr_peak_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_482_vol_autocorr_peak_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_peak over 126d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(126).skew()

def vaut_483_vol_autocorr_peak_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_483_vol_autocorr_peak_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_peak over 126d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(126).kurt()

def vaut_484_vol_autocorr_peak_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_484_vol_autocorr_peak_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_peak over 252d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(252).skew()

def vaut_485_vol_autocorr_peak_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_485_vol_autocorr_peak_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_peak over 252d. Maximum volume persistence in the last quarter.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).max()).rolling(252).kurt()

def vaut_486_vol_autocorr_entropy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_486_vol_autocorr_entropy_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_entropy over 5d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(5).skew()

def vaut_487_vol_autocorr_entropy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_487_vol_autocorr_entropy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_entropy over 5d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(5).kurt()

def vaut_488_vol_autocorr_entropy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_488_vol_autocorr_entropy_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_entropy over 21d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(21).skew()

def vaut_489_vol_autocorr_entropy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_489_vol_autocorr_entropy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_entropy over 21d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(21).kurt()

def vaut_490_vol_autocorr_entropy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_490_vol_autocorr_entropy_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_entropy over 63d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(63).skew()

def vaut_491_vol_autocorr_entropy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_491_vol_autocorr_entropy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_entropy over 63d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(63).kurt()

def vaut_492_vol_autocorr_entropy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_492_vol_autocorr_entropy_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_entropy over 126d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(126).skew()

def vaut_493_vol_autocorr_entropy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_493_vol_autocorr_entropy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_entropy over 126d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(126).kurt()

def vaut_494_vol_autocorr_entropy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_494_vol_autocorr_entropy_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_entropy over 252d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(252).skew()

def vaut_495_vol_autocorr_entropy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_495_vol_autocorr_entropy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_entropy over 252d. Unpredictability of volume changes.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: -np.sum(x*np.log(abs(x)+1e-9)))).rolling(252).kurt()

def vaut_496_vol_autocorr_regime_switch_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_496_vol_autocorr_regime_switch_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_regime_switch over 5d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(5).skew()

def vaut_497_vol_autocorr_regime_switch_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_497_vol_autocorr_regime_switch_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_regime_switch over 5d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(5).kurt()

def vaut_498_vol_autocorr_regime_switch_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_498_vol_autocorr_regime_switch_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_regime_switch over 21d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(21).skew()

def vaut_499_vol_autocorr_regime_switch_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_499_vol_autocorr_regime_switch_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_regime_switch over 21d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(21).kurt()

def vaut_500_vol_autocorr_regime_switch_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_500_vol_autocorr_regime_switch_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_regime_switch over 63d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(63).skew()

def vaut_501_vol_autocorr_regime_switch_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_501_vol_autocorr_regime_switch_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_regime_switch over 63d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(63).kurt()

def vaut_502_vol_autocorr_regime_switch_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_502_vol_autocorr_regime_switch_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_regime_switch over 126d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(126).skew()

def vaut_503_vol_autocorr_regime_switch_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_503_vol_autocorr_regime_switch_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_regime_switch over 126d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(126).kurt()

def vaut_504_vol_autocorr_regime_switch_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_504_vol_autocorr_regime_switch_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_regime_switch over 252d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(252).skew()

def vaut_505_vol_autocorr_regime_switch_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_505_vol_autocorr_regime_switch_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_regime_switch over 252d. Sudden switch in volume behavior.
    """
    return ((volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.3).astype(float)).rolling(252).kurt()

def vaut_506_vol_autocorr_ma_spread_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_506_vol_autocorr_ma_spread_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_ma_spread over 5d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(5).skew()

def vaut_507_vol_autocorr_ma_spread_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_507_vol_autocorr_ma_spread_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_ma_spread over 5d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(5).kurt()

def vaut_508_vol_autocorr_ma_spread_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_508_vol_autocorr_ma_spread_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_ma_spread over 21d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(21).skew()

def vaut_509_vol_autocorr_ma_spread_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_509_vol_autocorr_ma_spread_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_ma_spread over 21d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(21).kurt()

def vaut_510_vol_autocorr_ma_spread_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_510_vol_autocorr_ma_spread_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_ma_spread over 63d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(63).skew()

def vaut_511_vol_autocorr_ma_spread_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_511_vol_autocorr_ma_spread_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_ma_spread over 63d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(63).kurt()

def vaut_512_vol_autocorr_ma_spread_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_512_vol_autocorr_ma_spread_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_ma_spread over 126d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(126).skew()

def vaut_513_vol_autocorr_ma_spread_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_513_vol_autocorr_ma_spread_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_ma_spread over 126d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(126).kurt()

def vaut_514_vol_autocorr_ma_spread_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_514_vol_autocorr_ma_spread_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_ma_spread over 252d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(252).skew()

def vaut_515_vol_autocorr_ma_spread_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_515_vol_autocorr_ma_spread_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_ma_spread over 252d. Spread between short and long term volume persistence.
    """
    return (volume.pct_change(1).rolling(5).apply(lambda x: x.autocorr(1)) - volume.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1))).rolling(252).kurt()

def vaut_516_vol_autocorr_low_liquidity_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_516_vol_autocorr_low_liquidity_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_low_liquidity over 5d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(5).skew()

def vaut_517_vol_autocorr_low_liquidity_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_517_vol_autocorr_low_liquidity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_low_liquidity over 5d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(5).kurt()

def vaut_518_vol_autocorr_low_liquidity_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_518_vol_autocorr_low_liquidity_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_low_liquidity over 21d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(21).skew()

def vaut_519_vol_autocorr_low_liquidity_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_519_vol_autocorr_low_liquidity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_low_liquidity over 21d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(21).kurt()

def vaut_520_vol_autocorr_low_liquidity_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_520_vol_autocorr_low_liquidity_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_low_liquidity over 63d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(63).skew()

def vaut_521_vol_autocorr_low_liquidity_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_521_vol_autocorr_low_liquidity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_low_liquidity over 63d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(63).kurt()

def vaut_522_vol_autocorr_low_liquidity_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_522_vol_autocorr_low_liquidity_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_low_liquidity over 126d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(126).skew()

def vaut_523_vol_autocorr_low_liquidity_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_523_vol_autocorr_low_liquidity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_low_liquidity over 126d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(126).kurt()

def vaut_524_vol_autocorr_low_liquidity_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_524_vol_autocorr_low_liquidity_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_autocorr_low_liquidity over 252d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(252).skew()

def vaut_525_vol_autocorr_low_liquidity_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_525_vol_autocorr_low_liquidity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_autocorr_low_liquidity over 252d. Persistence during low volume periods.
    """
    return (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) * (volume < volume.rolling(252).mean())).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V113_REGISTRY_MOMENTS = {
    "vaut_376_vol_lag1_autocorr_skew_5d": {"inputs": ["close", "volume"], "func": vaut_376_vol_lag1_autocorr_skew_5d},
    "vaut_377_vol_lag1_autocorr_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_377_vol_lag1_autocorr_kurt_5d},
    "vaut_378_vol_lag1_autocorr_skew_21d": {"inputs": ["close", "volume"], "func": vaut_378_vol_lag1_autocorr_skew_21d},
    "vaut_379_vol_lag1_autocorr_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_379_vol_lag1_autocorr_kurt_21d},
    "vaut_380_vol_lag1_autocorr_skew_63d": {"inputs": ["close", "volume"], "func": vaut_380_vol_lag1_autocorr_skew_63d},
    "vaut_381_vol_lag1_autocorr_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_381_vol_lag1_autocorr_kurt_63d},
    "vaut_382_vol_lag1_autocorr_skew_126d": {"inputs": ["close", "volume"], "func": vaut_382_vol_lag1_autocorr_skew_126d},
    "vaut_383_vol_lag1_autocorr_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_383_vol_lag1_autocorr_kurt_126d},
    "vaut_384_vol_lag1_autocorr_skew_252d": {"inputs": ["close", "volume"], "func": vaut_384_vol_lag1_autocorr_skew_252d},
    "vaut_385_vol_lag1_autocorr_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_385_vol_lag1_autocorr_kurt_252d},
    "vaut_386_vol_autocorr_zscore_skew_5d": {"inputs": ["close", "volume"], "func": vaut_386_vol_autocorr_zscore_skew_5d},
    "vaut_387_vol_autocorr_zscore_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_387_vol_autocorr_zscore_kurt_5d},
    "vaut_388_vol_autocorr_zscore_skew_21d": {"inputs": ["close", "volume"], "func": vaut_388_vol_autocorr_zscore_skew_21d},
    "vaut_389_vol_autocorr_zscore_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_389_vol_autocorr_zscore_kurt_21d},
    "vaut_390_vol_autocorr_zscore_skew_63d": {"inputs": ["close", "volume"], "func": vaut_390_vol_autocorr_zscore_skew_63d},
    "vaut_391_vol_autocorr_zscore_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_391_vol_autocorr_zscore_kurt_63d},
    "vaut_392_vol_autocorr_zscore_skew_126d": {"inputs": ["close", "volume"], "func": vaut_392_vol_autocorr_zscore_skew_126d},
    "vaut_393_vol_autocorr_zscore_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_393_vol_autocorr_zscore_kurt_126d},
    "vaut_394_vol_autocorr_zscore_skew_252d": {"inputs": ["close", "volume"], "func": vaut_394_vol_autocorr_zscore_skew_252d},
    "vaut_395_vol_autocorr_zscore_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_395_vol_autocorr_zscore_kurt_252d},
    "vaut_396_vol_persistence_trend_skew_5d": {"inputs": ["close", "volume"], "func": vaut_396_vol_persistence_trend_skew_5d},
    "vaut_397_vol_persistence_trend_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_397_vol_persistence_trend_kurt_5d},
    "vaut_398_vol_persistence_trend_skew_21d": {"inputs": ["close", "volume"], "func": vaut_398_vol_persistence_trend_skew_21d},
    "vaut_399_vol_persistence_trend_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_399_vol_persistence_trend_kurt_21d},
    "vaut_400_vol_persistence_trend_skew_63d": {"inputs": ["close", "volume"], "func": vaut_400_vol_persistence_trend_skew_63d},
    "vaut_401_vol_persistence_trend_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_401_vol_persistence_trend_kurt_63d},
    "vaut_402_vol_persistence_trend_skew_126d": {"inputs": ["close", "volume"], "func": vaut_402_vol_persistence_trend_skew_126d},
    "vaut_403_vol_persistence_trend_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_403_vol_persistence_trend_kurt_126d},
    "vaut_404_vol_persistence_trend_skew_252d": {"inputs": ["close", "volume"], "func": vaut_404_vol_persistence_trend_skew_252d},
    "vaut_405_vol_persistence_trend_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_405_vol_persistence_trend_kurt_252d},
    "vaut_406_vol_clustering_index_skew_5d": {"inputs": ["close", "volume"], "func": vaut_406_vol_clustering_index_skew_5d},
    "vaut_407_vol_clustering_index_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_407_vol_clustering_index_kurt_5d},
    "vaut_408_vol_clustering_index_skew_21d": {"inputs": ["close", "volume"], "func": vaut_408_vol_clustering_index_skew_21d},
    "vaut_409_vol_clustering_index_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_409_vol_clustering_index_kurt_21d},
    "vaut_410_vol_clustering_index_skew_63d": {"inputs": ["close", "volume"], "func": vaut_410_vol_clustering_index_skew_63d},
    "vaut_411_vol_clustering_index_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_411_vol_clustering_index_kurt_63d},
    "vaut_412_vol_clustering_index_skew_126d": {"inputs": ["close", "volume"], "func": vaut_412_vol_clustering_index_skew_126d},
    "vaut_413_vol_clustering_index_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_413_vol_clustering_index_kurt_126d},
    "vaut_414_vol_clustering_index_skew_252d": {"inputs": ["close", "volume"], "func": vaut_414_vol_clustering_index_skew_252d},
    "vaut_415_vol_clustering_index_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_415_vol_clustering_index_kurt_252d},
    "vaut_416_vol_autocorr_rank_skew_5d": {"inputs": ["close", "volume"], "func": vaut_416_vol_autocorr_rank_skew_5d},
    "vaut_417_vol_autocorr_rank_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_417_vol_autocorr_rank_kurt_5d},
    "vaut_418_vol_autocorr_rank_skew_21d": {"inputs": ["close", "volume"], "func": vaut_418_vol_autocorr_rank_skew_21d},
    "vaut_419_vol_autocorr_rank_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_419_vol_autocorr_rank_kurt_21d},
    "vaut_420_vol_autocorr_rank_skew_63d": {"inputs": ["close", "volume"], "func": vaut_420_vol_autocorr_rank_skew_63d},
    "vaut_421_vol_autocorr_rank_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_421_vol_autocorr_rank_kurt_63d},
    "vaut_422_vol_autocorr_rank_skew_126d": {"inputs": ["close", "volume"], "func": vaut_422_vol_autocorr_rank_skew_126d},
    "vaut_423_vol_autocorr_rank_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_423_vol_autocorr_rank_kurt_126d},
    "vaut_424_vol_autocorr_rank_skew_252d": {"inputs": ["close", "volume"], "func": vaut_424_vol_autocorr_rank_skew_252d},
    "vaut_425_vol_autocorr_rank_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_425_vol_autocorr_rank_kurt_252d},
    "vaut_426_vol_autocorr_stability_skew_5d": {"inputs": ["close", "volume"], "func": vaut_426_vol_autocorr_stability_skew_5d},
    "vaut_427_vol_autocorr_stability_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_427_vol_autocorr_stability_kurt_5d},
    "vaut_428_vol_autocorr_stability_skew_21d": {"inputs": ["close", "volume"], "func": vaut_428_vol_autocorr_stability_skew_21d},
    "vaut_429_vol_autocorr_stability_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_429_vol_autocorr_stability_kurt_21d},
    "vaut_430_vol_autocorr_stability_skew_63d": {"inputs": ["close", "volume"], "func": vaut_430_vol_autocorr_stability_skew_63d},
    "vaut_431_vol_autocorr_stability_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_431_vol_autocorr_stability_kurt_63d},
    "vaut_432_vol_autocorr_stability_skew_126d": {"inputs": ["close", "volume"], "func": vaut_432_vol_autocorr_stability_skew_126d},
    "vaut_433_vol_autocorr_stability_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_433_vol_autocorr_stability_kurt_126d},
    "vaut_434_vol_autocorr_stability_skew_252d": {"inputs": ["close", "volume"], "func": vaut_434_vol_autocorr_stability_skew_252d},
    "vaut_435_vol_autocorr_stability_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_435_vol_autocorr_stability_kurt_252d},
    "vaut_436_vol_autocorr_acceleration_skew_5d": {"inputs": ["close", "volume"], "func": vaut_436_vol_autocorr_acceleration_skew_5d},
    "vaut_437_vol_autocorr_acceleration_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_437_vol_autocorr_acceleration_kurt_5d},
    "vaut_438_vol_autocorr_acceleration_skew_21d": {"inputs": ["close", "volume"], "func": vaut_438_vol_autocorr_acceleration_skew_21d},
    "vaut_439_vol_autocorr_acceleration_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_439_vol_autocorr_acceleration_kurt_21d},
    "vaut_440_vol_autocorr_acceleration_skew_63d": {"inputs": ["close", "volume"], "func": vaut_440_vol_autocorr_acceleration_skew_63d},
    "vaut_441_vol_autocorr_acceleration_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_441_vol_autocorr_acceleration_kurt_63d},
    "vaut_442_vol_autocorr_acceleration_skew_126d": {"inputs": ["close", "volume"], "func": vaut_442_vol_autocorr_acceleration_skew_126d},
    "vaut_443_vol_autocorr_acceleration_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_443_vol_autocorr_acceleration_kurt_126d},
    "vaut_444_vol_autocorr_acceleration_skew_252d": {"inputs": ["close", "volume"], "func": vaut_444_vol_autocorr_acceleration_skew_252d},
    "vaut_445_vol_autocorr_acceleration_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_445_vol_autocorr_acceleration_kurt_252d},
    "vaut_446_vol_mean_reversion_flag_skew_5d": {"inputs": ["close", "volume"], "func": vaut_446_vol_mean_reversion_flag_skew_5d},
    "vaut_447_vol_mean_reversion_flag_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_447_vol_mean_reversion_flag_kurt_5d},
    "vaut_448_vol_mean_reversion_flag_skew_21d": {"inputs": ["close", "volume"], "func": vaut_448_vol_mean_reversion_flag_skew_21d},
    "vaut_449_vol_mean_reversion_flag_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_449_vol_mean_reversion_flag_kurt_21d},
    "vaut_450_vol_mean_reversion_flag_skew_63d": {"inputs": ["close", "volume"], "func": vaut_450_vol_mean_reversion_flag_skew_63d},
    "vaut_451_vol_mean_reversion_flag_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_451_vol_mean_reversion_flag_kurt_63d},
    "vaut_452_vol_mean_reversion_flag_skew_126d": {"inputs": ["close", "volume"], "func": vaut_452_vol_mean_reversion_flag_skew_126d},
    "vaut_453_vol_mean_reversion_flag_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_453_vol_mean_reversion_flag_kurt_126d},
    "vaut_454_vol_mean_reversion_flag_skew_252d": {"inputs": ["close", "volume"], "func": vaut_454_vol_mean_reversion_flag_skew_252d},
    "vaut_455_vol_mean_reversion_flag_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_455_vol_mean_reversion_flag_kurt_252d},
    "vaut_456_vol_trend_persistence_skew_5d": {"inputs": ["close", "volume"], "func": vaut_456_vol_trend_persistence_skew_5d},
    "vaut_457_vol_trend_persistence_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_457_vol_trend_persistence_kurt_5d},
    "vaut_458_vol_trend_persistence_skew_21d": {"inputs": ["close", "volume"], "func": vaut_458_vol_trend_persistence_skew_21d},
    "vaut_459_vol_trend_persistence_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_459_vol_trend_persistence_kurt_21d},
    "vaut_460_vol_trend_persistence_skew_63d": {"inputs": ["close", "volume"], "func": vaut_460_vol_trend_persistence_skew_63d},
    "vaut_461_vol_trend_persistence_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_461_vol_trend_persistence_kurt_63d},
    "vaut_462_vol_trend_persistence_skew_126d": {"inputs": ["close", "volume"], "func": vaut_462_vol_trend_persistence_skew_126d},
    "vaut_463_vol_trend_persistence_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_463_vol_trend_persistence_kurt_126d},
    "vaut_464_vol_trend_persistence_skew_252d": {"inputs": ["close", "volume"], "func": vaut_464_vol_trend_persistence_skew_252d},
    "vaut_465_vol_trend_persistence_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_465_vol_trend_persistence_kurt_252d},
    "vaut_466_vol_autocorr_vs_price_skew_5d": {"inputs": ["close", "volume"], "func": vaut_466_vol_autocorr_vs_price_skew_5d},
    "vaut_467_vol_autocorr_vs_price_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_467_vol_autocorr_vs_price_kurt_5d},
    "vaut_468_vol_autocorr_vs_price_skew_21d": {"inputs": ["close", "volume"], "func": vaut_468_vol_autocorr_vs_price_skew_21d},
    "vaut_469_vol_autocorr_vs_price_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_469_vol_autocorr_vs_price_kurt_21d},
    "vaut_470_vol_autocorr_vs_price_skew_63d": {"inputs": ["close", "volume"], "func": vaut_470_vol_autocorr_vs_price_skew_63d},
    "vaut_471_vol_autocorr_vs_price_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_471_vol_autocorr_vs_price_kurt_63d},
    "vaut_472_vol_autocorr_vs_price_skew_126d": {"inputs": ["close", "volume"], "func": vaut_472_vol_autocorr_vs_price_skew_126d},
    "vaut_473_vol_autocorr_vs_price_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_473_vol_autocorr_vs_price_kurt_126d},
    "vaut_474_vol_autocorr_vs_price_skew_252d": {"inputs": ["close", "volume"], "func": vaut_474_vol_autocorr_vs_price_skew_252d},
    "vaut_475_vol_autocorr_vs_price_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_475_vol_autocorr_vs_price_kurt_252d},
    "vaut_476_vol_autocorr_peak_skew_5d": {"inputs": ["close", "volume"], "func": vaut_476_vol_autocorr_peak_skew_5d},
    "vaut_477_vol_autocorr_peak_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_477_vol_autocorr_peak_kurt_5d},
    "vaut_478_vol_autocorr_peak_skew_21d": {"inputs": ["close", "volume"], "func": vaut_478_vol_autocorr_peak_skew_21d},
    "vaut_479_vol_autocorr_peak_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_479_vol_autocorr_peak_kurt_21d},
    "vaut_480_vol_autocorr_peak_skew_63d": {"inputs": ["close", "volume"], "func": vaut_480_vol_autocorr_peak_skew_63d},
    "vaut_481_vol_autocorr_peak_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_481_vol_autocorr_peak_kurt_63d},
    "vaut_482_vol_autocorr_peak_skew_126d": {"inputs": ["close", "volume"], "func": vaut_482_vol_autocorr_peak_skew_126d},
    "vaut_483_vol_autocorr_peak_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_483_vol_autocorr_peak_kurt_126d},
    "vaut_484_vol_autocorr_peak_skew_252d": {"inputs": ["close", "volume"], "func": vaut_484_vol_autocorr_peak_skew_252d},
    "vaut_485_vol_autocorr_peak_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_485_vol_autocorr_peak_kurt_252d},
    "vaut_486_vol_autocorr_entropy_skew_5d": {"inputs": ["close", "volume"], "func": vaut_486_vol_autocorr_entropy_skew_5d},
    "vaut_487_vol_autocorr_entropy_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_487_vol_autocorr_entropy_kurt_5d},
    "vaut_488_vol_autocorr_entropy_skew_21d": {"inputs": ["close", "volume"], "func": vaut_488_vol_autocorr_entropy_skew_21d},
    "vaut_489_vol_autocorr_entropy_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_489_vol_autocorr_entropy_kurt_21d},
    "vaut_490_vol_autocorr_entropy_skew_63d": {"inputs": ["close", "volume"], "func": vaut_490_vol_autocorr_entropy_skew_63d},
    "vaut_491_vol_autocorr_entropy_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_491_vol_autocorr_entropy_kurt_63d},
    "vaut_492_vol_autocorr_entropy_skew_126d": {"inputs": ["close", "volume"], "func": vaut_492_vol_autocorr_entropy_skew_126d},
    "vaut_493_vol_autocorr_entropy_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_493_vol_autocorr_entropy_kurt_126d},
    "vaut_494_vol_autocorr_entropy_skew_252d": {"inputs": ["close", "volume"], "func": vaut_494_vol_autocorr_entropy_skew_252d},
    "vaut_495_vol_autocorr_entropy_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_495_vol_autocorr_entropy_kurt_252d},
    "vaut_496_vol_autocorr_regime_switch_skew_5d": {"inputs": ["close", "volume"], "func": vaut_496_vol_autocorr_regime_switch_skew_5d},
    "vaut_497_vol_autocorr_regime_switch_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_497_vol_autocorr_regime_switch_kurt_5d},
    "vaut_498_vol_autocorr_regime_switch_skew_21d": {"inputs": ["close", "volume"], "func": vaut_498_vol_autocorr_regime_switch_skew_21d},
    "vaut_499_vol_autocorr_regime_switch_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_499_vol_autocorr_regime_switch_kurt_21d},
    "vaut_500_vol_autocorr_regime_switch_skew_63d": {"inputs": ["close", "volume"], "func": vaut_500_vol_autocorr_regime_switch_skew_63d},
    "vaut_501_vol_autocorr_regime_switch_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_501_vol_autocorr_regime_switch_kurt_63d},
    "vaut_502_vol_autocorr_regime_switch_skew_126d": {"inputs": ["close", "volume"], "func": vaut_502_vol_autocorr_regime_switch_skew_126d},
    "vaut_503_vol_autocorr_regime_switch_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_503_vol_autocorr_regime_switch_kurt_126d},
    "vaut_504_vol_autocorr_regime_switch_skew_252d": {"inputs": ["close", "volume"], "func": vaut_504_vol_autocorr_regime_switch_skew_252d},
    "vaut_505_vol_autocorr_regime_switch_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_505_vol_autocorr_regime_switch_kurt_252d},
    "vaut_506_vol_autocorr_ma_spread_skew_5d": {"inputs": ["close", "volume"], "func": vaut_506_vol_autocorr_ma_spread_skew_5d},
    "vaut_507_vol_autocorr_ma_spread_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_507_vol_autocorr_ma_spread_kurt_5d},
    "vaut_508_vol_autocorr_ma_spread_skew_21d": {"inputs": ["close", "volume"], "func": vaut_508_vol_autocorr_ma_spread_skew_21d},
    "vaut_509_vol_autocorr_ma_spread_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_509_vol_autocorr_ma_spread_kurt_21d},
    "vaut_510_vol_autocorr_ma_spread_skew_63d": {"inputs": ["close", "volume"], "func": vaut_510_vol_autocorr_ma_spread_skew_63d},
    "vaut_511_vol_autocorr_ma_spread_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_511_vol_autocorr_ma_spread_kurt_63d},
    "vaut_512_vol_autocorr_ma_spread_skew_126d": {"inputs": ["close", "volume"], "func": vaut_512_vol_autocorr_ma_spread_skew_126d},
    "vaut_513_vol_autocorr_ma_spread_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_513_vol_autocorr_ma_spread_kurt_126d},
    "vaut_514_vol_autocorr_ma_spread_skew_252d": {"inputs": ["close", "volume"], "func": vaut_514_vol_autocorr_ma_spread_skew_252d},
    "vaut_515_vol_autocorr_ma_spread_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_515_vol_autocorr_ma_spread_kurt_252d},
    "vaut_516_vol_autocorr_low_liquidity_skew_5d": {"inputs": ["close", "volume"], "func": vaut_516_vol_autocorr_low_liquidity_skew_5d},
    "vaut_517_vol_autocorr_low_liquidity_kurt_5d": {"inputs": ["close", "volume"], "func": vaut_517_vol_autocorr_low_liquidity_kurt_5d},
    "vaut_518_vol_autocorr_low_liquidity_skew_21d": {"inputs": ["close", "volume"], "func": vaut_518_vol_autocorr_low_liquidity_skew_21d},
    "vaut_519_vol_autocorr_low_liquidity_kurt_21d": {"inputs": ["close", "volume"], "func": vaut_519_vol_autocorr_low_liquidity_kurt_21d},
    "vaut_520_vol_autocorr_low_liquidity_skew_63d": {"inputs": ["close", "volume"], "func": vaut_520_vol_autocorr_low_liquidity_skew_63d},
    "vaut_521_vol_autocorr_low_liquidity_kurt_63d": {"inputs": ["close", "volume"], "func": vaut_521_vol_autocorr_low_liquidity_kurt_63d},
    "vaut_522_vol_autocorr_low_liquidity_skew_126d": {"inputs": ["close", "volume"], "func": vaut_522_vol_autocorr_low_liquidity_skew_126d},
    "vaut_523_vol_autocorr_low_liquidity_kurt_126d": {"inputs": ["close", "volume"], "func": vaut_523_vol_autocorr_low_liquidity_kurt_126d},
    "vaut_524_vol_autocorr_low_liquidity_skew_252d": {"inputs": ["close", "volume"], "func": vaut_524_vol_autocorr_low_liquidity_skew_252d},
    "vaut_525_vol_autocorr_low_liquidity_kurt_252d": {"inputs": ["close", "volume"], "func": vaut_525_vol_autocorr_low_liquidity_kurt_252d},
}
