"""
107_change_point_detection — Base Features Part 1
Domain: change_point_detection
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

def cpdt_001_mean_shift_detection_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_001_mean_shift_detection_lvl_5d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rolling_mean(base, 5)

def cpdt_002_mean_shift_detection_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_002_mean_shift_detection_zscore_5d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _zscore_rolling(base, 5)

def cpdt_003_mean_shift_detection_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_003_mean_shift_detection_rank_5d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rank_pct(base, 5)

def cpdt_004_mean_shift_detection_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_004_mean_shift_detection_lvl_21d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rolling_mean(base, 21)

def cpdt_005_mean_shift_detection_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_005_mean_shift_detection_zscore_21d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _zscore_rolling(base, 21)

def cpdt_006_mean_shift_detection_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_006_mean_shift_detection_rank_21d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rank_pct(base, 21)

def cpdt_007_mean_shift_detection_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_007_mean_shift_detection_lvl_63d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rolling_mean(base, 63)

def cpdt_008_mean_shift_detection_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_008_mean_shift_detection_zscore_63d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _zscore_rolling(base, 63)

def cpdt_009_mean_shift_detection_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_009_mean_shift_detection_rank_63d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rank_pct(base, 63)

def cpdt_010_mean_shift_detection_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_010_mean_shift_detection_lvl_126d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rolling_mean(base, 126)

def cpdt_011_mean_shift_detection_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_011_mean_shift_detection_zscore_126d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _zscore_rolling(base, 126)

def cpdt_012_mean_shift_detection_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_012_mean_shift_detection_rank_126d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rank_pct(base, 126)

def cpdt_013_mean_shift_detection_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_013_mean_shift_detection_lvl_252d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rolling_mean(base, 252)

def cpdt_014_mean_shift_detection_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_014_mean_shift_detection_zscore_252d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _zscore_rolling(base, 252)

def cpdt_015_mean_shift_detection_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_015_mean_shift_detection_rank_252d
    ECONOMIC RATIONALE: Significant shift in the mean price level.
    """
    base = (close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()
    return _rank_pct(base, 252)

def cpdt_016_vol_regime_shift_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_016_vol_regime_shift_lvl_5d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rolling_mean(base, 5)

def cpdt_017_vol_regime_shift_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_017_vol_regime_shift_zscore_5d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _zscore_rolling(base, 5)

def cpdt_018_vol_regime_shift_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_018_vol_regime_shift_rank_5d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rank_pct(base, 5)

def cpdt_019_vol_regime_shift_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_019_vol_regime_shift_lvl_21d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rolling_mean(base, 21)

def cpdt_020_vol_regime_shift_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_020_vol_regime_shift_zscore_21d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _zscore_rolling(base, 21)

def cpdt_021_vol_regime_shift_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_021_vol_regime_shift_rank_21d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rank_pct(base, 21)

def cpdt_022_vol_regime_shift_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_022_vol_regime_shift_lvl_63d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rolling_mean(base, 63)

def cpdt_023_vol_regime_shift_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_023_vol_regime_shift_zscore_63d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _zscore_rolling(base, 63)

def cpdt_024_vol_regime_shift_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_024_vol_regime_shift_rank_63d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rank_pct(base, 63)

def cpdt_025_vol_regime_shift_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_025_vol_regime_shift_lvl_126d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rolling_mean(base, 126)

def cpdt_026_vol_regime_shift_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_026_vol_regime_shift_zscore_126d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _zscore_rolling(base, 126)

def cpdt_027_vol_regime_shift_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_027_vol_regime_shift_rank_126d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rank_pct(base, 126)

def cpdt_028_vol_regime_shift_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_028_vol_regime_shift_lvl_252d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rolling_mean(base, 252)

def cpdt_029_vol_regime_shift_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_029_vol_regime_shift_zscore_252d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _zscore_rolling(base, 252)

def cpdt_030_vol_regime_shift_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_030_vol_regime_shift_rank_252d
    ECONOMIC RATIONALE: Shift in the volatility of trading volume.
    """
    base = volume.rolling(21).std() / volume.rolling(252).std()
    return _rank_pct(base, 252)

def cpdt_031_cusum_proxy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_031_cusum_proxy_lvl_5d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rolling_mean(base, 5)

def cpdt_032_cusum_proxy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_032_cusum_proxy_zscore_5d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _zscore_rolling(base, 5)

def cpdt_033_cusum_proxy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_033_cusum_proxy_rank_5d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rank_pct(base, 5)

def cpdt_034_cusum_proxy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_034_cusum_proxy_lvl_21d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rolling_mean(base, 21)

def cpdt_035_cusum_proxy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_035_cusum_proxy_zscore_21d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _zscore_rolling(base, 21)

def cpdt_036_cusum_proxy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_036_cusum_proxy_rank_21d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rank_pct(base, 21)

def cpdt_037_cusum_proxy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_037_cusum_proxy_lvl_63d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rolling_mean(base, 63)

def cpdt_038_cusum_proxy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_038_cusum_proxy_zscore_63d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _zscore_rolling(base, 63)

def cpdt_039_cusum_proxy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_039_cusum_proxy_rank_63d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rank_pct(base, 63)

def cpdt_040_cusum_proxy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_040_cusum_proxy_lvl_126d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rolling_mean(base, 126)

def cpdt_041_cusum_proxy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_041_cusum_proxy_zscore_126d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _zscore_rolling(base, 126)

def cpdt_042_cusum_proxy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_042_cusum_proxy_rank_126d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rank_pct(base, 126)

def cpdt_043_cusum_proxy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_043_cusum_proxy_lvl_252d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rolling_mean(base, 252)

def cpdt_044_cusum_proxy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_044_cusum_proxy_zscore_252d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _zscore_rolling(base, 252)

def cpdt_045_cusum_proxy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_045_cusum_proxy_rank_252d
    ECONOMIC RATIONALE: Cumulative sum of deviations from the mean.
    """
    base = (close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()
    return _rank_pct(base, 252)

def cpdt_046_change_point_z_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_046_change_point_z_lvl_5d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 5)

def cpdt_047_change_point_z_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_047_change_point_z_zscore_5d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 5)

def cpdt_048_change_point_z_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_048_change_point_z_rank_5d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 5)

def cpdt_049_change_point_z_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_049_change_point_z_lvl_21d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 21)

def cpdt_050_change_point_z_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_050_change_point_z_zscore_21d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 21)

def cpdt_051_change_point_z_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_051_change_point_z_rank_21d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 21)

def cpdt_052_change_point_z_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_052_change_point_z_lvl_63d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 63)

def cpdt_053_change_point_z_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_053_change_point_z_zscore_63d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 63)

def cpdt_054_change_point_z_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_054_change_point_z_rank_63d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 63)

def cpdt_055_change_point_z_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_055_change_point_z_lvl_126d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 126)

def cpdt_056_change_point_z_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_056_change_point_z_zscore_126d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 126)

def cpdt_057_change_point_z_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_057_change_point_z_rank_126d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 126)

def cpdt_058_change_point_z_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_058_change_point_z_lvl_252d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 252)

def cpdt_059_change_point_z_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_059_change_point_z_zscore_252d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 252)

def cpdt_060_change_point_z_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_060_change_point_z_rank_252d
    ECONOMIC RATIONALE: Anomaly detection in the magnitude of daily changes.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 252)

def cpdt_061_trend_regime_change_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_061_trend_regime_change_lvl_5d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rolling_mean(base, 5)

def cpdt_062_trend_regime_change_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_062_trend_regime_change_zscore_5d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _zscore_rolling(base, 5)

def cpdt_063_trend_regime_change_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_063_trend_regime_change_rank_5d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rank_pct(base, 5)

def cpdt_064_trend_regime_change_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_064_trend_regime_change_lvl_21d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rolling_mean(base, 21)

def cpdt_065_trend_regime_change_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_065_trend_regime_change_zscore_21d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _zscore_rolling(base, 21)

def cpdt_066_trend_regime_change_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_066_trend_regime_change_rank_21d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rank_pct(base, 21)

def cpdt_067_trend_regime_change_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_067_trend_regime_change_lvl_63d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rolling_mean(base, 63)

def cpdt_068_trend_regime_change_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_068_trend_regime_change_zscore_63d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _zscore_rolling(base, 63)

def cpdt_069_trend_regime_change_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_069_trend_regime_change_rank_63d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rank_pct(base, 63)

def cpdt_070_trend_regime_change_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_070_trend_regime_change_lvl_126d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rolling_mean(base, 126)

def cpdt_071_trend_regime_change_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_071_trend_regime_change_zscore_126d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _zscore_rolling(base, 126)

def cpdt_072_trend_regime_change_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_072_trend_regime_change_rank_126d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rank_pct(base, 126)

def cpdt_073_trend_regime_change_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_073_trend_regime_change_lvl_252d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rolling_mean(base, 252)

def cpdt_074_trend_regime_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_074_trend_regime_change_zscore_252d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _zscore_rolling(base, 252)

def cpdt_075_trend_regime_change_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_075_trend_regime_change_rank_252d
    ECONOMIC RATIONALE: Change in trend autocorrelation.
    """
    base = close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))
    return _rank_pct(base, 252)

def cpdt_076_volatility_structural_break_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_076_volatility_structural_break_lvl_5d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rolling_mean(base, 5)

def cpdt_077_volatility_structural_break_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_077_volatility_structural_break_zscore_5d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _zscore_rolling(base, 5)

def cpdt_078_volatility_structural_break_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_078_volatility_structural_break_rank_5d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rank_pct(base, 5)

def cpdt_079_volatility_structural_break_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_079_volatility_structural_break_lvl_21d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rolling_mean(base, 21)

def cpdt_080_volatility_structural_break_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_080_volatility_structural_break_zscore_21d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _zscore_rolling(base, 21)

def cpdt_081_volatility_structural_break_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_081_volatility_structural_break_rank_21d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rank_pct(base, 21)

def cpdt_082_volatility_structural_break_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_082_volatility_structural_break_lvl_63d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rolling_mean(base, 63)

def cpdt_083_volatility_structural_break_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_083_volatility_structural_break_zscore_63d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _zscore_rolling(base, 63)

def cpdt_084_volatility_structural_break_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_084_volatility_structural_break_rank_63d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rank_pct(base, 63)

def cpdt_085_volatility_structural_break_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_085_volatility_structural_break_lvl_126d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rolling_mean(base, 126)

def cpdt_086_volatility_structural_break_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_086_volatility_structural_break_zscore_126d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _zscore_rolling(base, 126)

def cpdt_087_volatility_structural_break_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_087_volatility_structural_break_rank_126d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rank_pct(base, 126)

def cpdt_088_volatility_structural_break_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_088_volatility_structural_break_lvl_252d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rolling_mean(base, 252)

def cpdt_089_volatility_structural_break_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_089_volatility_structural_break_zscore_252d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _zscore_rolling(base, 252)

def cpdt_090_volatility_structural_break_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_090_volatility_structural_break_rank_252d
    ECONOMIC RATIONALE: Sudden expansion or contraction of volatility.
    """
    base = close.rolling(21).std() / close.rolling(21).std().shift(21)
    return _rank_pct(base, 252)

def cpdt_091_distribution_entropy_shift_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_091_distribution_entropy_shift_lvl_5d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rolling_mean(base, 5)

def cpdt_092_distribution_entropy_shift_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_092_distribution_entropy_shift_zscore_5d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _zscore_rolling(base, 5)

def cpdt_093_distribution_entropy_shift_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_093_distribution_entropy_shift_rank_5d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rank_pct(base, 5)

def cpdt_094_distribution_entropy_shift_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_094_distribution_entropy_shift_lvl_21d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rolling_mean(base, 21)

def cpdt_095_distribution_entropy_shift_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_095_distribution_entropy_shift_zscore_21d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _zscore_rolling(base, 21)

def cpdt_096_distribution_entropy_shift_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_096_distribution_entropy_shift_rank_21d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rank_pct(base, 21)

def cpdt_097_distribution_entropy_shift_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_097_distribution_entropy_shift_lvl_63d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rolling_mean(base, 63)

def cpdt_098_distribution_entropy_shift_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_098_distribution_entropy_shift_zscore_63d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _zscore_rolling(base, 63)

def cpdt_099_distribution_entropy_shift_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_099_distribution_entropy_shift_rank_63d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rank_pct(base, 63)

def cpdt_100_distribution_entropy_shift_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_100_distribution_entropy_shift_lvl_126d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rolling_mean(base, 126)

def cpdt_101_distribution_entropy_shift_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_101_distribution_entropy_shift_zscore_126d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _zscore_rolling(base, 126)

def cpdt_102_distribution_entropy_shift_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_102_distribution_entropy_shift_rank_126d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rank_pct(base, 126)

def cpdt_103_distribution_entropy_shift_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_103_distribution_entropy_shift_lvl_252d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rolling_mean(base, 252)

def cpdt_104_distribution_entropy_shift_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_104_distribution_entropy_shift_zscore_252d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _zscore_rolling(base, 252)

def cpdt_105_distribution_entropy_shift_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_105_distribution_entropy_shift_rank_252d
    ECONOMIC RATIONALE: Change in the shape of price distribution.
    """
    base = close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()
    return _rank_pct(base, 252)

def cpdt_106_change_point_momentum_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_106_change_point_momentum_lvl_5d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rolling_mean(base, 5)

def cpdt_107_change_point_momentum_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_107_change_point_momentum_zscore_5d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _zscore_rolling(base, 5)

def cpdt_108_change_point_momentum_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_108_change_point_momentum_rank_5d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rank_pct(base, 5)

def cpdt_109_change_point_momentum_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_109_change_point_momentum_lvl_21d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rolling_mean(base, 21)

def cpdt_110_change_point_momentum_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_110_change_point_momentum_zscore_21d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _zscore_rolling(base, 21)

def cpdt_111_change_point_momentum_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_111_change_point_momentum_rank_21d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rank_pct(base, 21)

def cpdt_112_change_point_momentum_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_112_change_point_momentum_lvl_63d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rolling_mean(base, 63)

def cpdt_113_change_point_momentum_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_113_change_point_momentum_zscore_63d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _zscore_rolling(base, 63)

def cpdt_114_change_point_momentum_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_114_change_point_momentum_rank_63d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rank_pct(base, 63)

def cpdt_115_change_point_momentum_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_115_change_point_momentum_lvl_126d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rolling_mean(base, 126)

def cpdt_116_change_point_momentum_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_116_change_point_momentum_zscore_126d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _zscore_rolling(base, 126)

def cpdt_117_change_point_momentum_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_117_change_point_momentum_rank_126d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rank_pct(base, 126)

def cpdt_118_change_point_momentum_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_118_change_point_momentum_lvl_252d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rolling_mean(base, 252)

def cpdt_119_change_point_momentum_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_119_change_point_momentum_zscore_252d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _zscore_rolling(base, 252)

def cpdt_120_change_point_momentum_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_120_change_point_momentum_rank_252d
    ECONOMIC RATIONALE: Acceleration of change magnitude.
    """
    base = close.pct_change(21).abs().diff(21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V107_REGISTRY_1 = {
    "cpdt_001_mean_shift_detection_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_001_mean_shift_detection_lvl_5d},
    "cpdt_002_mean_shift_detection_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_002_mean_shift_detection_zscore_5d},
    "cpdt_003_mean_shift_detection_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_003_mean_shift_detection_rank_5d},
    "cpdt_004_mean_shift_detection_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_004_mean_shift_detection_lvl_21d},
    "cpdt_005_mean_shift_detection_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_005_mean_shift_detection_zscore_21d},
    "cpdt_006_mean_shift_detection_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_006_mean_shift_detection_rank_21d},
    "cpdt_007_mean_shift_detection_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_007_mean_shift_detection_lvl_63d},
    "cpdt_008_mean_shift_detection_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_008_mean_shift_detection_zscore_63d},
    "cpdt_009_mean_shift_detection_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_009_mean_shift_detection_rank_63d},
    "cpdt_010_mean_shift_detection_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_010_mean_shift_detection_lvl_126d},
    "cpdt_011_mean_shift_detection_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_011_mean_shift_detection_zscore_126d},
    "cpdt_012_mean_shift_detection_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_012_mean_shift_detection_rank_126d},
    "cpdt_013_mean_shift_detection_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_013_mean_shift_detection_lvl_252d},
    "cpdt_014_mean_shift_detection_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_014_mean_shift_detection_zscore_252d},
    "cpdt_015_mean_shift_detection_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_015_mean_shift_detection_rank_252d},
    "cpdt_016_vol_regime_shift_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_016_vol_regime_shift_lvl_5d},
    "cpdt_017_vol_regime_shift_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_017_vol_regime_shift_zscore_5d},
    "cpdt_018_vol_regime_shift_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_018_vol_regime_shift_rank_5d},
    "cpdt_019_vol_regime_shift_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_019_vol_regime_shift_lvl_21d},
    "cpdt_020_vol_regime_shift_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_020_vol_regime_shift_zscore_21d},
    "cpdt_021_vol_regime_shift_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_021_vol_regime_shift_rank_21d},
    "cpdt_022_vol_regime_shift_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_022_vol_regime_shift_lvl_63d},
    "cpdt_023_vol_regime_shift_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_023_vol_regime_shift_zscore_63d},
    "cpdt_024_vol_regime_shift_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_024_vol_regime_shift_rank_63d},
    "cpdt_025_vol_regime_shift_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_025_vol_regime_shift_lvl_126d},
    "cpdt_026_vol_regime_shift_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_026_vol_regime_shift_zscore_126d},
    "cpdt_027_vol_regime_shift_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_027_vol_regime_shift_rank_126d},
    "cpdt_028_vol_regime_shift_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_028_vol_regime_shift_lvl_252d},
    "cpdt_029_vol_regime_shift_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_029_vol_regime_shift_zscore_252d},
    "cpdt_030_vol_regime_shift_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_030_vol_regime_shift_rank_252d},
    "cpdt_031_cusum_proxy_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_031_cusum_proxy_lvl_5d},
    "cpdt_032_cusum_proxy_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_032_cusum_proxy_zscore_5d},
    "cpdt_033_cusum_proxy_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_033_cusum_proxy_rank_5d},
    "cpdt_034_cusum_proxy_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_034_cusum_proxy_lvl_21d},
    "cpdt_035_cusum_proxy_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_035_cusum_proxy_zscore_21d},
    "cpdt_036_cusum_proxy_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_036_cusum_proxy_rank_21d},
    "cpdt_037_cusum_proxy_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_037_cusum_proxy_lvl_63d},
    "cpdt_038_cusum_proxy_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_038_cusum_proxy_zscore_63d},
    "cpdt_039_cusum_proxy_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_039_cusum_proxy_rank_63d},
    "cpdt_040_cusum_proxy_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_040_cusum_proxy_lvl_126d},
    "cpdt_041_cusum_proxy_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_041_cusum_proxy_zscore_126d},
    "cpdt_042_cusum_proxy_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_042_cusum_proxy_rank_126d},
    "cpdt_043_cusum_proxy_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_043_cusum_proxy_lvl_252d},
    "cpdt_044_cusum_proxy_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_044_cusum_proxy_zscore_252d},
    "cpdt_045_cusum_proxy_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_045_cusum_proxy_rank_252d},
    "cpdt_046_change_point_z_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_046_change_point_z_lvl_5d},
    "cpdt_047_change_point_z_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_047_change_point_z_zscore_5d},
    "cpdt_048_change_point_z_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_048_change_point_z_rank_5d},
    "cpdt_049_change_point_z_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_049_change_point_z_lvl_21d},
    "cpdt_050_change_point_z_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_050_change_point_z_zscore_21d},
    "cpdt_051_change_point_z_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_051_change_point_z_rank_21d},
    "cpdt_052_change_point_z_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_052_change_point_z_lvl_63d},
    "cpdt_053_change_point_z_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_053_change_point_z_zscore_63d},
    "cpdt_054_change_point_z_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_054_change_point_z_rank_63d},
    "cpdt_055_change_point_z_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_055_change_point_z_lvl_126d},
    "cpdt_056_change_point_z_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_056_change_point_z_zscore_126d},
    "cpdt_057_change_point_z_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_057_change_point_z_rank_126d},
    "cpdt_058_change_point_z_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_058_change_point_z_lvl_252d},
    "cpdt_059_change_point_z_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_059_change_point_z_zscore_252d},
    "cpdt_060_change_point_z_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_060_change_point_z_rank_252d},
    "cpdt_061_trend_regime_change_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_061_trend_regime_change_lvl_5d},
    "cpdt_062_trend_regime_change_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_062_trend_regime_change_zscore_5d},
    "cpdt_063_trend_regime_change_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_063_trend_regime_change_rank_5d},
    "cpdt_064_trend_regime_change_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_064_trend_regime_change_lvl_21d},
    "cpdt_065_trend_regime_change_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_065_trend_regime_change_zscore_21d},
    "cpdt_066_trend_regime_change_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_066_trend_regime_change_rank_21d},
    "cpdt_067_trend_regime_change_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_067_trend_regime_change_lvl_63d},
    "cpdt_068_trend_regime_change_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_068_trend_regime_change_zscore_63d},
    "cpdt_069_trend_regime_change_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_069_trend_regime_change_rank_63d},
    "cpdt_070_trend_regime_change_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_070_trend_regime_change_lvl_126d},
    "cpdt_071_trend_regime_change_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_071_trend_regime_change_zscore_126d},
    "cpdt_072_trend_regime_change_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_072_trend_regime_change_rank_126d},
    "cpdt_073_trend_regime_change_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_073_trend_regime_change_lvl_252d},
    "cpdt_074_trend_regime_change_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_074_trend_regime_change_zscore_252d},
    "cpdt_075_trend_regime_change_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_075_trend_regime_change_rank_252d},
    "cpdt_076_volatility_structural_break_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_076_volatility_structural_break_lvl_5d},
    "cpdt_077_volatility_structural_break_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_077_volatility_structural_break_zscore_5d},
    "cpdt_078_volatility_structural_break_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_078_volatility_structural_break_rank_5d},
    "cpdt_079_volatility_structural_break_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_079_volatility_structural_break_lvl_21d},
    "cpdt_080_volatility_structural_break_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_080_volatility_structural_break_zscore_21d},
    "cpdt_081_volatility_structural_break_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_081_volatility_structural_break_rank_21d},
    "cpdt_082_volatility_structural_break_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_082_volatility_structural_break_lvl_63d},
    "cpdt_083_volatility_structural_break_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_083_volatility_structural_break_zscore_63d},
    "cpdt_084_volatility_structural_break_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_084_volatility_structural_break_rank_63d},
    "cpdt_085_volatility_structural_break_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_085_volatility_structural_break_lvl_126d},
    "cpdt_086_volatility_structural_break_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_086_volatility_structural_break_zscore_126d},
    "cpdt_087_volatility_structural_break_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_087_volatility_structural_break_rank_126d},
    "cpdt_088_volatility_structural_break_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_088_volatility_structural_break_lvl_252d},
    "cpdt_089_volatility_structural_break_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_089_volatility_structural_break_zscore_252d},
    "cpdt_090_volatility_structural_break_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_090_volatility_structural_break_rank_252d},
    "cpdt_091_distribution_entropy_shift_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_091_distribution_entropy_shift_lvl_5d},
    "cpdt_092_distribution_entropy_shift_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_092_distribution_entropy_shift_zscore_5d},
    "cpdt_093_distribution_entropy_shift_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_093_distribution_entropy_shift_rank_5d},
    "cpdt_094_distribution_entropy_shift_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_094_distribution_entropy_shift_lvl_21d},
    "cpdt_095_distribution_entropy_shift_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_095_distribution_entropy_shift_zscore_21d},
    "cpdt_096_distribution_entropy_shift_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_096_distribution_entropy_shift_rank_21d},
    "cpdt_097_distribution_entropy_shift_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_097_distribution_entropy_shift_lvl_63d},
    "cpdt_098_distribution_entropy_shift_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_098_distribution_entropy_shift_zscore_63d},
    "cpdt_099_distribution_entropy_shift_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_099_distribution_entropy_shift_rank_63d},
    "cpdt_100_distribution_entropy_shift_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_100_distribution_entropy_shift_lvl_126d},
    "cpdt_101_distribution_entropy_shift_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_101_distribution_entropy_shift_zscore_126d},
    "cpdt_102_distribution_entropy_shift_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_102_distribution_entropy_shift_rank_126d},
    "cpdt_103_distribution_entropy_shift_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_103_distribution_entropy_shift_lvl_252d},
    "cpdt_104_distribution_entropy_shift_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_104_distribution_entropy_shift_zscore_252d},
    "cpdt_105_distribution_entropy_shift_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_105_distribution_entropy_shift_rank_252d},
    "cpdt_106_change_point_momentum_lvl_5d": {"inputs": ["close", "volume"], "func": cpdt_106_change_point_momentum_lvl_5d},
    "cpdt_107_change_point_momentum_zscore_5d": {"inputs": ["close", "volume"], "func": cpdt_107_change_point_momentum_zscore_5d},
    "cpdt_108_change_point_momentum_rank_5d": {"inputs": ["close", "volume"], "func": cpdt_108_change_point_momentum_rank_5d},
    "cpdt_109_change_point_momentum_lvl_21d": {"inputs": ["close", "volume"], "func": cpdt_109_change_point_momentum_lvl_21d},
    "cpdt_110_change_point_momentum_zscore_21d": {"inputs": ["close", "volume"], "func": cpdt_110_change_point_momentum_zscore_21d},
    "cpdt_111_change_point_momentum_rank_21d": {"inputs": ["close", "volume"], "func": cpdt_111_change_point_momentum_rank_21d},
    "cpdt_112_change_point_momentum_lvl_63d": {"inputs": ["close", "volume"], "func": cpdt_112_change_point_momentum_lvl_63d},
    "cpdt_113_change_point_momentum_zscore_63d": {"inputs": ["close", "volume"], "func": cpdt_113_change_point_momentum_zscore_63d},
    "cpdt_114_change_point_momentum_rank_63d": {"inputs": ["close", "volume"], "func": cpdt_114_change_point_momentum_rank_63d},
    "cpdt_115_change_point_momentum_lvl_126d": {"inputs": ["close", "volume"], "func": cpdt_115_change_point_momentum_lvl_126d},
    "cpdt_116_change_point_momentum_zscore_126d": {"inputs": ["close", "volume"], "func": cpdt_116_change_point_momentum_zscore_126d},
    "cpdt_117_change_point_momentum_rank_126d": {"inputs": ["close", "volume"], "func": cpdt_117_change_point_momentum_rank_126d},
    "cpdt_118_change_point_momentum_lvl_252d": {"inputs": ["close", "volume"], "func": cpdt_118_change_point_momentum_lvl_252d},
    "cpdt_119_change_point_momentum_zscore_252d": {"inputs": ["close", "volume"], "func": cpdt_119_change_point_momentum_zscore_252d},
    "cpdt_120_change_point_momentum_rank_252d": {"inputs": ["close", "volume"], "func": cpdt_120_change_point_momentum_rank_252d},
}
