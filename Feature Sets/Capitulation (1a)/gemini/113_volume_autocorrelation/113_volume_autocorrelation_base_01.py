"""
113_volume_autocorrelation — Base Features Part 1
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

def vaut_001_vol_lag1_autocorr_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_001_vol_lag1_autocorr_lvl_5d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 5)

def vaut_002_vol_lag1_autocorr_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_002_vol_lag1_autocorr_zscore_5d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 5)

def vaut_003_vol_lag1_autocorr_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_003_vol_lag1_autocorr_rank_5d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 5)

def vaut_004_vol_lag1_autocorr_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_004_vol_lag1_autocorr_lvl_21d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 21)

def vaut_005_vol_lag1_autocorr_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_005_vol_lag1_autocorr_zscore_21d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 21)

def vaut_006_vol_lag1_autocorr_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_006_vol_lag1_autocorr_rank_21d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 21)

def vaut_007_vol_lag1_autocorr_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_007_vol_lag1_autocorr_lvl_63d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 63)

def vaut_008_vol_lag1_autocorr_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_008_vol_lag1_autocorr_zscore_63d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 63)

def vaut_009_vol_lag1_autocorr_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_009_vol_lag1_autocorr_rank_63d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 63)

def vaut_010_vol_lag1_autocorr_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_010_vol_lag1_autocorr_lvl_126d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 126)

def vaut_011_vol_lag1_autocorr_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_011_vol_lag1_autocorr_zscore_126d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 126)

def vaut_012_vol_lag1_autocorr_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_012_vol_lag1_autocorr_rank_126d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 126)

def vaut_013_vol_lag1_autocorr_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_013_vol_lag1_autocorr_lvl_252d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 252)

def vaut_014_vol_lag1_autocorr_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_014_vol_lag1_autocorr_zscore_252d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 252)

def vaut_015_vol_lag1_autocorr_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_015_vol_lag1_autocorr_rank_252d
    ECONOMIC RATIONALE: 21-day serial correlation of volume changes.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 252)

def vaut_016_vol_autocorr_zscore_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_016_vol_autocorr_zscore_lvl_5d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 5)

def vaut_017_vol_autocorr_zscore_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_017_vol_autocorr_zscore_zscore_5d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 5)

def vaut_018_vol_autocorr_zscore_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_018_vol_autocorr_zscore_rank_5d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 5)

def vaut_019_vol_autocorr_zscore_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_019_vol_autocorr_zscore_lvl_21d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 21)

def vaut_020_vol_autocorr_zscore_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_020_vol_autocorr_zscore_zscore_21d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 21)

def vaut_021_vol_autocorr_zscore_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_021_vol_autocorr_zscore_rank_21d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 21)

def vaut_022_vol_autocorr_zscore_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_022_vol_autocorr_zscore_lvl_63d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 63)

def vaut_023_vol_autocorr_zscore_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_023_vol_autocorr_zscore_zscore_63d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 63)

def vaut_024_vol_autocorr_zscore_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_024_vol_autocorr_zscore_rank_63d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 63)

def vaut_025_vol_autocorr_zscore_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_025_vol_autocorr_zscore_lvl_126d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 126)

def vaut_026_vol_autocorr_zscore_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_026_vol_autocorr_zscore_zscore_126d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 126)

def vaut_027_vol_autocorr_zscore_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_027_vol_autocorr_zscore_rank_126d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 126)

def vaut_028_vol_autocorr_zscore_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_028_vol_autocorr_zscore_lvl_252d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 252)

def vaut_029_vol_autocorr_zscore_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_029_vol_autocorr_zscore_zscore_252d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 252)

def vaut_030_vol_autocorr_zscore_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_030_vol_autocorr_zscore_rank_252d
    ECONOMIC RATIONALE: Anomaly in volume persistence.
    """
    base = _zscore_rolling(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 252)

def vaut_031_vol_persistence_trend_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_031_vol_persistence_trend_lvl_5d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 5)

def vaut_032_vol_persistence_trend_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_032_vol_persistence_trend_zscore_5d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 5)

def vaut_033_vol_persistence_trend_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_033_vol_persistence_trend_rank_5d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 5)

def vaut_034_vol_persistence_trend_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_034_vol_persistence_trend_lvl_21d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 21)

def vaut_035_vol_persistence_trend_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_035_vol_persistence_trend_zscore_21d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 21)

def vaut_036_vol_persistence_trend_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_036_vol_persistence_trend_rank_21d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 21)

def vaut_037_vol_persistence_trend_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_037_vol_persistence_trend_lvl_63d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 63)

def vaut_038_vol_persistence_trend_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_038_vol_persistence_trend_zscore_63d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 63)

def vaut_039_vol_persistence_trend_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_039_vol_persistence_trend_rank_63d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 63)

def vaut_040_vol_persistence_trend_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_040_vol_persistence_trend_lvl_126d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 126)

def vaut_041_vol_persistence_trend_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_041_vol_persistence_trend_zscore_126d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 126)

def vaut_042_vol_persistence_trend_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_042_vol_persistence_trend_rank_126d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 126)

def vaut_043_vol_persistence_trend_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_043_vol_persistence_trend_lvl_252d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 252)

def vaut_044_vol_persistence_trend_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_044_vol_persistence_trend_zscore_252d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 252)

def vaut_045_vol_persistence_trend_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_045_vol_persistence_trend_rank_252d
    ECONOMIC RATIONALE: Shift in volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 252)

def vaut_046_vol_clustering_index_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_046_vol_clustering_index_lvl_5d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 5)

def vaut_047_vol_clustering_index_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_047_vol_clustering_index_zscore_5d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 5)

def vaut_048_vol_clustering_index_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_048_vol_clustering_index_rank_5d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rank_pct(base, 5)

def vaut_049_vol_clustering_index_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_049_vol_clustering_index_lvl_21d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 21)

def vaut_050_vol_clustering_index_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_050_vol_clustering_index_zscore_21d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 21)

def vaut_051_vol_clustering_index_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_051_vol_clustering_index_rank_21d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rank_pct(base, 21)

def vaut_052_vol_clustering_index_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_052_vol_clustering_index_lvl_63d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 63)

def vaut_053_vol_clustering_index_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_053_vol_clustering_index_zscore_63d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 63)

def vaut_054_vol_clustering_index_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_054_vol_clustering_index_rank_63d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rank_pct(base, 63)

def vaut_055_vol_clustering_index_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_055_vol_clustering_index_lvl_126d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 126)

def vaut_056_vol_clustering_index_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_056_vol_clustering_index_zscore_126d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 126)

def vaut_057_vol_clustering_index_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_057_vol_clustering_index_rank_126d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rank_pct(base, 126)

def vaut_058_vol_clustering_index_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_058_vol_clustering_index_lvl_252d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rolling_mean(base, 252)

def vaut_059_vol_clustering_index_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_059_vol_clustering_index_zscore_252d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _zscore_rolling(base, 252)

def vaut_060_vol_clustering_index_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_060_vol_clustering_index_rank_252d
    ECONOMIC RATIONALE: Autocorrelation of absolute volume changes.
    """
    base = volume.pct_change(1).abs().rolling(21).corr(volume.pct_change(1).abs().shift(1))
    return _rank_pct(base, 252)

def vaut_061_vol_autocorr_rank_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_061_vol_autocorr_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 5)

def vaut_062_vol_autocorr_rank_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_062_vol_autocorr_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 5)

def vaut_063_vol_autocorr_rank_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_063_vol_autocorr_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 5)

def vaut_064_vol_autocorr_rank_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_064_vol_autocorr_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 21)

def vaut_065_vol_autocorr_rank_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_065_vol_autocorr_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 21)

def vaut_066_vol_autocorr_rank_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_066_vol_autocorr_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 21)

def vaut_067_vol_autocorr_rank_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_067_vol_autocorr_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 63)

def vaut_068_vol_autocorr_rank_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_068_vol_autocorr_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 63)

def vaut_069_vol_autocorr_rank_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_069_vol_autocorr_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 63)

def vaut_070_vol_autocorr_rank_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_070_vol_autocorr_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 126)

def vaut_071_vol_autocorr_rank_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_071_vol_autocorr_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 126)

def vaut_072_vol_autocorr_rank_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_072_vol_autocorr_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 126)

def vaut_073_vol_autocorr_rank_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_073_vol_autocorr_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 252)

def vaut_074_vol_autocorr_rank_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_074_vol_autocorr_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 252)

def vaut_075_vol_autocorr_rank_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_075_vol_autocorr_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of volume persistence.
    """
    base = _rank_pct(volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 252)

def vaut_076_vol_autocorr_stability_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_076_vol_autocorr_stability_lvl_5d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 5)

def vaut_077_vol_autocorr_stability_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_077_vol_autocorr_stability_zscore_5d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 5)

def vaut_078_vol_autocorr_stability_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_078_vol_autocorr_stability_rank_5d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 5)

def vaut_079_vol_autocorr_stability_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_079_vol_autocorr_stability_lvl_21d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 21)

def vaut_080_vol_autocorr_stability_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_080_vol_autocorr_stability_zscore_21d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 21)

def vaut_081_vol_autocorr_stability_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_081_vol_autocorr_stability_rank_21d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 21)

def vaut_082_vol_autocorr_stability_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_082_vol_autocorr_stability_lvl_63d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 63)

def vaut_083_vol_autocorr_stability_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_083_vol_autocorr_stability_zscore_63d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 63)

def vaut_084_vol_autocorr_stability_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_084_vol_autocorr_stability_rank_63d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 63)

def vaut_085_vol_autocorr_stability_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_085_vol_autocorr_stability_lvl_126d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 126)

def vaut_086_vol_autocorr_stability_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_086_vol_autocorr_stability_zscore_126d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 126)

def vaut_087_vol_autocorr_stability_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_087_vol_autocorr_stability_rank_126d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 126)

def vaut_088_vol_autocorr_stability_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_088_vol_autocorr_stability_lvl_252d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rolling_mean(base, 252)

def vaut_089_vol_autocorr_stability_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_089_vol_autocorr_stability_zscore_252d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _zscore_rolling(base, 252)

def vaut_090_vol_autocorr_stability_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_090_vol_autocorr_stability_rank_252d
    ECONOMIC RATIONALE: Stability of the volume persistence regime.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()
    return _rank_pct(base, 252)

def vaut_091_vol_autocorr_acceleration_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_091_vol_autocorr_acceleration_lvl_5d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 5)

def vaut_092_vol_autocorr_acceleration_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_092_vol_autocorr_acceleration_zscore_5d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 5)

def vaut_093_vol_autocorr_acceleration_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_093_vol_autocorr_acceleration_rank_5d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 5)

def vaut_094_vol_autocorr_acceleration_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_094_vol_autocorr_acceleration_lvl_21d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 21)

def vaut_095_vol_autocorr_acceleration_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_095_vol_autocorr_acceleration_zscore_21d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 21)

def vaut_096_vol_autocorr_acceleration_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_096_vol_autocorr_acceleration_rank_21d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 21)

def vaut_097_vol_autocorr_acceleration_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_097_vol_autocorr_acceleration_lvl_63d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 63)

def vaut_098_vol_autocorr_acceleration_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_098_vol_autocorr_acceleration_zscore_63d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 63)

def vaut_099_vol_autocorr_acceleration_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_099_vol_autocorr_acceleration_rank_63d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 63)

def vaut_100_vol_autocorr_acceleration_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_100_vol_autocorr_acceleration_lvl_126d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 126)

def vaut_101_vol_autocorr_acceleration_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_101_vol_autocorr_acceleration_zscore_126d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 126)

def vaut_102_vol_autocorr_acceleration_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_102_vol_autocorr_acceleration_rank_126d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 126)

def vaut_103_vol_autocorr_acceleration_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_103_vol_autocorr_acceleration_lvl_252d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rolling_mean(base, 252)

def vaut_104_vol_autocorr_acceleration_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_104_vol_autocorr_acceleration_zscore_252d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _zscore_rolling(base, 252)

def vaut_105_vol_autocorr_acceleration_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_105_vol_autocorr_acceleration_rank_252d
    ECONOMIC RATIONALE: Short-term change in volume persistence.
    """
    base = volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)
    return _rank_pct(base, 252)

def vaut_106_vol_mean_reversion_flag_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_106_vol_mean_reversion_flag_lvl_5d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rolling_mean(base, 5)

def vaut_107_vol_mean_reversion_flag_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_107_vol_mean_reversion_flag_zscore_5d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _zscore_rolling(base, 5)

def vaut_108_vol_mean_reversion_flag_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_108_vol_mean_reversion_flag_rank_5d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rank_pct(base, 5)

def vaut_109_vol_mean_reversion_flag_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_109_vol_mean_reversion_flag_lvl_21d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rolling_mean(base, 21)

def vaut_110_vol_mean_reversion_flag_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_110_vol_mean_reversion_flag_zscore_21d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _zscore_rolling(base, 21)

def vaut_111_vol_mean_reversion_flag_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_111_vol_mean_reversion_flag_rank_21d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rank_pct(base, 21)

def vaut_112_vol_mean_reversion_flag_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_112_vol_mean_reversion_flag_lvl_63d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rolling_mean(base, 63)

def vaut_113_vol_mean_reversion_flag_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_113_vol_mean_reversion_flag_zscore_63d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _zscore_rolling(base, 63)

def vaut_114_vol_mean_reversion_flag_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_114_vol_mean_reversion_flag_rank_63d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rank_pct(base, 63)

def vaut_115_vol_mean_reversion_flag_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_115_vol_mean_reversion_flag_lvl_126d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rolling_mean(base, 126)

def vaut_116_vol_mean_reversion_flag_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_116_vol_mean_reversion_flag_zscore_126d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _zscore_rolling(base, 126)

def vaut_117_vol_mean_reversion_flag_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_117_vol_mean_reversion_flag_rank_126d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rank_pct(base, 126)

def vaut_118_vol_mean_reversion_flag_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_118_vol_mean_reversion_flag_lvl_252d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rolling_mean(base, 252)

def vaut_119_vol_mean_reversion_flag_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_119_vol_mean_reversion_flag_zscore_252d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _zscore_rolling(base, 252)

def vaut_120_vol_mean_reversion_flag_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vaut_120_vol_mean_reversion_flag_rank_252d
    ECONOMIC RATIONALE: Volume mean-reverting regime.
    """
    base = (volume.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.2).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V113_REGISTRY_1 = {
    "vaut_001_vol_lag1_autocorr_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_001_vol_lag1_autocorr_lvl_5d},
    "vaut_002_vol_lag1_autocorr_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_002_vol_lag1_autocorr_zscore_5d},
    "vaut_003_vol_lag1_autocorr_rank_5d": {"inputs": ["close", "volume"], "func": vaut_003_vol_lag1_autocorr_rank_5d},
    "vaut_004_vol_lag1_autocorr_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_004_vol_lag1_autocorr_lvl_21d},
    "vaut_005_vol_lag1_autocorr_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_005_vol_lag1_autocorr_zscore_21d},
    "vaut_006_vol_lag1_autocorr_rank_21d": {"inputs": ["close", "volume"], "func": vaut_006_vol_lag1_autocorr_rank_21d},
    "vaut_007_vol_lag1_autocorr_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_007_vol_lag1_autocorr_lvl_63d},
    "vaut_008_vol_lag1_autocorr_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_008_vol_lag1_autocorr_zscore_63d},
    "vaut_009_vol_lag1_autocorr_rank_63d": {"inputs": ["close", "volume"], "func": vaut_009_vol_lag1_autocorr_rank_63d},
    "vaut_010_vol_lag1_autocorr_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_010_vol_lag1_autocorr_lvl_126d},
    "vaut_011_vol_lag1_autocorr_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_011_vol_lag1_autocorr_zscore_126d},
    "vaut_012_vol_lag1_autocorr_rank_126d": {"inputs": ["close", "volume"], "func": vaut_012_vol_lag1_autocorr_rank_126d},
    "vaut_013_vol_lag1_autocorr_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_013_vol_lag1_autocorr_lvl_252d},
    "vaut_014_vol_lag1_autocorr_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_014_vol_lag1_autocorr_zscore_252d},
    "vaut_015_vol_lag1_autocorr_rank_252d": {"inputs": ["close", "volume"], "func": vaut_015_vol_lag1_autocorr_rank_252d},
    "vaut_016_vol_autocorr_zscore_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_016_vol_autocorr_zscore_lvl_5d},
    "vaut_017_vol_autocorr_zscore_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_017_vol_autocorr_zscore_zscore_5d},
    "vaut_018_vol_autocorr_zscore_rank_5d": {"inputs": ["close", "volume"], "func": vaut_018_vol_autocorr_zscore_rank_5d},
    "vaut_019_vol_autocorr_zscore_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_019_vol_autocorr_zscore_lvl_21d},
    "vaut_020_vol_autocorr_zscore_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_020_vol_autocorr_zscore_zscore_21d},
    "vaut_021_vol_autocorr_zscore_rank_21d": {"inputs": ["close", "volume"], "func": vaut_021_vol_autocorr_zscore_rank_21d},
    "vaut_022_vol_autocorr_zscore_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_022_vol_autocorr_zscore_lvl_63d},
    "vaut_023_vol_autocorr_zscore_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_023_vol_autocorr_zscore_zscore_63d},
    "vaut_024_vol_autocorr_zscore_rank_63d": {"inputs": ["close", "volume"], "func": vaut_024_vol_autocorr_zscore_rank_63d},
    "vaut_025_vol_autocorr_zscore_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_025_vol_autocorr_zscore_lvl_126d},
    "vaut_026_vol_autocorr_zscore_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_026_vol_autocorr_zscore_zscore_126d},
    "vaut_027_vol_autocorr_zscore_rank_126d": {"inputs": ["close", "volume"], "func": vaut_027_vol_autocorr_zscore_rank_126d},
    "vaut_028_vol_autocorr_zscore_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_028_vol_autocorr_zscore_lvl_252d},
    "vaut_029_vol_autocorr_zscore_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_029_vol_autocorr_zscore_zscore_252d},
    "vaut_030_vol_autocorr_zscore_rank_252d": {"inputs": ["close", "volume"], "func": vaut_030_vol_autocorr_zscore_rank_252d},
    "vaut_031_vol_persistence_trend_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_031_vol_persistence_trend_lvl_5d},
    "vaut_032_vol_persistence_trend_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_032_vol_persistence_trend_zscore_5d},
    "vaut_033_vol_persistence_trend_rank_5d": {"inputs": ["close", "volume"], "func": vaut_033_vol_persistence_trend_rank_5d},
    "vaut_034_vol_persistence_trend_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_034_vol_persistence_trend_lvl_21d},
    "vaut_035_vol_persistence_trend_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_035_vol_persistence_trend_zscore_21d},
    "vaut_036_vol_persistence_trend_rank_21d": {"inputs": ["close", "volume"], "func": vaut_036_vol_persistence_trend_rank_21d},
    "vaut_037_vol_persistence_trend_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_037_vol_persistence_trend_lvl_63d},
    "vaut_038_vol_persistence_trend_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_038_vol_persistence_trend_zscore_63d},
    "vaut_039_vol_persistence_trend_rank_63d": {"inputs": ["close", "volume"], "func": vaut_039_vol_persistence_trend_rank_63d},
    "vaut_040_vol_persistence_trend_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_040_vol_persistence_trend_lvl_126d},
    "vaut_041_vol_persistence_trend_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_041_vol_persistence_trend_zscore_126d},
    "vaut_042_vol_persistence_trend_rank_126d": {"inputs": ["close", "volume"], "func": vaut_042_vol_persistence_trend_rank_126d},
    "vaut_043_vol_persistence_trend_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_043_vol_persistence_trend_lvl_252d},
    "vaut_044_vol_persistence_trend_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_044_vol_persistence_trend_zscore_252d},
    "vaut_045_vol_persistence_trend_rank_252d": {"inputs": ["close", "volume"], "func": vaut_045_vol_persistence_trend_rank_252d},
    "vaut_046_vol_clustering_index_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_046_vol_clustering_index_lvl_5d},
    "vaut_047_vol_clustering_index_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_047_vol_clustering_index_zscore_5d},
    "vaut_048_vol_clustering_index_rank_5d": {"inputs": ["close", "volume"], "func": vaut_048_vol_clustering_index_rank_5d},
    "vaut_049_vol_clustering_index_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_049_vol_clustering_index_lvl_21d},
    "vaut_050_vol_clustering_index_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_050_vol_clustering_index_zscore_21d},
    "vaut_051_vol_clustering_index_rank_21d": {"inputs": ["close", "volume"], "func": vaut_051_vol_clustering_index_rank_21d},
    "vaut_052_vol_clustering_index_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_052_vol_clustering_index_lvl_63d},
    "vaut_053_vol_clustering_index_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_053_vol_clustering_index_zscore_63d},
    "vaut_054_vol_clustering_index_rank_63d": {"inputs": ["close", "volume"], "func": vaut_054_vol_clustering_index_rank_63d},
    "vaut_055_vol_clustering_index_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_055_vol_clustering_index_lvl_126d},
    "vaut_056_vol_clustering_index_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_056_vol_clustering_index_zscore_126d},
    "vaut_057_vol_clustering_index_rank_126d": {"inputs": ["close", "volume"], "func": vaut_057_vol_clustering_index_rank_126d},
    "vaut_058_vol_clustering_index_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_058_vol_clustering_index_lvl_252d},
    "vaut_059_vol_clustering_index_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_059_vol_clustering_index_zscore_252d},
    "vaut_060_vol_clustering_index_rank_252d": {"inputs": ["close", "volume"], "func": vaut_060_vol_clustering_index_rank_252d},
    "vaut_061_vol_autocorr_rank_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_061_vol_autocorr_rank_lvl_5d},
    "vaut_062_vol_autocorr_rank_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_062_vol_autocorr_rank_zscore_5d},
    "vaut_063_vol_autocorr_rank_rank_5d": {"inputs": ["close", "volume"], "func": vaut_063_vol_autocorr_rank_rank_5d},
    "vaut_064_vol_autocorr_rank_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_064_vol_autocorr_rank_lvl_21d},
    "vaut_065_vol_autocorr_rank_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_065_vol_autocorr_rank_zscore_21d},
    "vaut_066_vol_autocorr_rank_rank_21d": {"inputs": ["close", "volume"], "func": vaut_066_vol_autocorr_rank_rank_21d},
    "vaut_067_vol_autocorr_rank_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_067_vol_autocorr_rank_lvl_63d},
    "vaut_068_vol_autocorr_rank_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_068_vol_autocorr_rank_zscore_63d},
    "vaut_069_vol_autocorr_rank_rank_63d": {"inputs": ["close", "volume"], "func": vaut_069_vol_autocorr_rank_rank_63d},
    "vaut_070_vol_autocorr_rank_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_070_vol_autocorr_rank_lvl_126d},
    "vaut_071_vol_autocorr_rank_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_071_vol_autocorr_rank_zscore_126d},
    "vaut_072_vol_autocorr_rank_rank_126d": {"inputs": ["close", "volume"], "func": vaut_072_vol_autocorr_rank_rank_126d},
    "vaut_073_vol_autocorr_rank_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_073_vol_autocorr_rank_lvl_252d},
    "vaut_074_vol_autocorr_rank_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_074_vol_autocorr_rank_zscore_252d},
    "vaut_075_vol_autocorr_rank_rank_252d": {"inputs": ["close", "volume"], "func": vaut_075_vol_autocorr_rank_rank_252d},
    "vaut_076_vol_autocorr_stability_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_076_vol_autocorr_stability_lvl_5d},
    "vaut_077_vol_autocorr_stability_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_077_vol_autocorr_stability_zscore_5d},
    "vaut_078_vol_autocorr_stability_rank_5d": {"inputs": ["close", "volume"], "func": vaut_078_vol_autocorr_stability_rank_5d},
    "vaut_079_vol_autocorr_stability_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_079_vol_autocorr_stability_lvl_21d},
    "vaut_080_vol_autocorr_stability_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_080_vol_autocorr_stability_zscore_21d},
    "vaut_081_vol_autocorr_stability_rank_21d": {"inputs": ["close", "volume"], "func": vaut_081_vol_autocorr_stability_rank_21d},
    "vaut_082_vol_autocorr_stability_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_082_vol_autocorr_stability_lvl_63d},
    "vaut_083_vol_autocorr_stability_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_083_vol_autocorr_stability_zscore_63d},
    "vaut_084_vol_autocorr_stability_rank_63d": {"inputs": ["close", "volume"], "func": vaut_084_vol_autocorr_stability_rank_63d},
    "vaut_085_vol_autocorr_stability_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_085_vol_autocorr_stability_lvl_126d},
    "vaut_086_vol_autocorr_stability_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_086_vol_autocorr_stability_zscore_126d},
    "vaut_087_vol_autocorr_stability_rank_126d": {"inputs": ["close", "volume"], "func": vaut_087_vol_autocorr_stability_rank_126d},
    "vaut_088_vol_autocorr_stability_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_088_vol_autocorr_stability_lvl_252d},
    "vaut_089_vol_autocorr_stability_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_089_vol_autocorr_stability_zscore_252d},
    "vaut_090_vol_autocorr_stability_rank_252d": {"inputs": ["close", "volume"], "func": vaut_090_vol_autocorr_stability_rank_252d},
    "vaut_091_vol_autocorr_acceleration_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_091_vol_autocorr_acceleration_lvl_5d},
    "vaut_092_vol_autocorr_acceleration_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_092_vol_autocorr_acceleration_zscore_5d},
    "vaut_093_vol_autocorr_acceleration_rank_5d": {"inputs": ["close", "volume"], "func": vaut_093_vol_autocorr_acceleration_rank_5d},
    "vaut_094_vol_autocorr_acceleration_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_094_vol_autocorr_acceleration_lvl_21d},
    "vaut_095_vol_autocorr_acceleration_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_095_vol_autocorr_acceleration_zscore_21d},
    "vaut_096_vol_autocorr_acceleration_rank_21d": {"inputs": ["close", "volume"], "func": vaut_096_vol_autocorr_acceleration_rank_21d},
    "vaut_097_vol_autocorr_acceleration_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_097_vol_autocorr_acceleration_lvl_63d},
    "vaut_098_vol_autocorr_acceleration_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_098_vol_autocorr_acceleration_zscore_63d},
    "vaut_099_vol_autocorr_acceleration_rank_63d": {"inputs": ["close", "volume"], "func": vaut_099_vol_autocorr_acceleration_rank_63d},
    "vaut_100_vol_autocorr_acceleration_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_100_vol_autocorr_acceleration_lvl_126d},
    "vaut_101_vol_autocorr_acceleration_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_101_vol_autocorr_acceleration_zscore_126d},
    "vaut_102_vol_autocorr_acceleration_rank_126d": {"inputs": ["close", "volume"], "func": vaut_102_vol_autocorr_acceleration_rank_126d},
    "vaut_103_vol_autocorr_acceleration_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_103_vol_autocorr_acceleration_lvl_252d},
    "vaut_104_vol_autocorr_acceleration_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_104_vol_autocorr_acceleration_zscore_252d},
    "vaut_105_vol_autocorr_acceleration_rank_252d": {"inputs": ["close", "volume"], "func": vaut_105_vol_autocorr_acceleration_rank_252d},
    "vaut_106_vol_mean_reversion_flag_lvl_5d": {"inputs": ["close", "volume"], "func": vaut_106_vol_mean_reversion_flag_lvl_5d},
    "vaut_107_vol_mean_reversion_flag_zscore_5d": {"inputs": ["close", "volume"], "func": vaut_107_vol_mean_reversion_flag_zscore_5d},
    "vaut_108_vol_mean_reversion_flag_rank_5d": {"inputs": ["close", "volume"], "func": vaut_108_vol_mean_reversion_flag_rank_5d},
    "vaut_109_vol_mean_reversion_flag_lvl_21d": {"inputs": ["close", "volume"], "func": vaut_109_vol_mean_reversion_flag_lvl_21d},
    "vaut_110_vol_mean_reversion_flag_zscore_21d": {"inputs": ["close", "volume"], "func": vaut_110_vol_mean_reversion_flag_zscore_21d},
    "vaut_111_vol_mean_reversion_flag_rank_21d": {"inputs": ["close", "volume"], "func": vaut_111_vol_mean_reversion_flag_rank_21d},
    "vaut_112_vol_mean_reversion_flag_lvl_63d": {"inputs": ["close", "volume"], "func": vaut_112_vol_mean_reversion_flag_lvl_63d},
    "vaut_113_vol_mean_reversion_flag_zscore_63d": {"inputs": ["close", "volume"], "func": vaut_113_vol_mean_reversion_flag_zscore_63d},
    "vaut_114_vol_mean_reversion_flag_rank_63d": {"inputs": ["close", "volume"], "func": vaut_114_vol_mean_reversion_flag_rank_63d},
    "vaut_115_vol_mean_reversion_flag_lvl_126d": {"inputs": ["close", "volume"], "func": vaut_115_vol_mean_reversion_flag_lvl_126d},
    "vaut_116_vol_mean_reversion_flag_zscore_126d": {"inputs": ["close", "volume"], "func": vaut_116_vol_mean_reversion_flag_zscore_126d},
    "vaut_117_vol_mean_reversion_flag_rank_126d": {"inputs": ["close", "volume"], "func": vaut_117_vol_mean_reversion_flag_rank_126d},
    "vaut_118_vol_mean_reversion_flag_lvl_252d": {"inputs": ["close", "volume"], "func": vaut_118_vol_mean_reversion_flag_lvl_252d},
    "vaut_119_vol_mean_reversion_flag_zscore_252d": {"inputs": ["close", "volume"], "func": vaut_119_vol_mean_reversion_flag_zscore_252d},
    "vaut_120_vol_mean_reversion_flag_rank_252d": {"inputs": ["close", "volume"], "func": vaut_120_vol_mean_reversion_flag_rank_252d},
}
