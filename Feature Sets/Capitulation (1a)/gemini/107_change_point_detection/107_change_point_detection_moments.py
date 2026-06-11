"""
107_change_point_detection — Statistical Moments
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

def cpdt_376_mean_shift_detection_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_376_mean_shift_detection_skew_5d
    ECONOMIC RATIONALE: Skewness of mean_shift_detection over 5d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(5).skew()

def cpdt_377_mean_shift_detection_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_377_mean_shift_detection_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of mean_shift_detection over 5d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(5).kurt()

def cpdt_378_mean_shift_detection_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_378_mean_shift_detection_skew_21d
    ECONOMIC RATIONALE: Skewness of mean_shift_detection over 21d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(21).skew()

def cpdt_379_mean_shift_detection_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_379_mean_shift_detection_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of mean_shift_detection over 21d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(21).kurt()

def cpdt_380_mean_shift_detection_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_380_mean_shift_detection_skew_63d
    ECONOMIC RATIONALE: Skewness of mean_shift_detection over 63d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(63).skew()

def cpdt_381_mean_shift_detection_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_381_mean_shift_detection_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of mean_shift_detection over 63d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(63).kurt()

def cpdt_382_mean_shift_detection_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_382_mean_shift_detection_skew_126d
    ECONOMIC RATIONALE: Skewness of mean_shift_detection over 126d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(126).skew()

def cpdt_383_mean_shift_detection_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_383_mean_shift_detection_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of mean_shift_detection over 126d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(126).kurt()

def cpdt_384_mean_shift_detection_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_384_mean_shift_detection_skew_252d
    ECONOMIC RATIONALE: Skewness of mean_shift_detection over 252d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(252).skew()

def cpdt_385_mean_shift_detection_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_385_mean_shift_detection_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of mean_shift_detection over 252d. Significant shift in the mean price level.
    """
    return ((close.rolling(21).mean() - close.rolling(21).mean().shift(21)).abs() / close.rolling(63).std()).rolling(252).kurt()

def cpdt_386_vol_regime_shift_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_386_vol_regime_shift_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_regime_shift over 5d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(5).skew()

def cpdt_387_vol_regime_shift_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_387_vol_regime_shift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_shift over 5d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(5).kurt()

def cpdt_388_vol_regime_shift_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_388_vol_regime_shift_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_regime_shift over 21d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(21).skew()

def cpdt_389_vol_regime_shift_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_389_vol_regime_shift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_shift over 21d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(21).kurt()

def cpdt_390_vol_regime_shift_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_390_vol_regime_shift_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_regime_shift over 63d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(63).skew()

def cpdt_391_vol_regime_shift_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_391_vol_regime_shift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_shift over 63d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(63).kurt()

def cpdt_392_vol_regime_shift_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_392_vol_regime_shift_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_regime_shift over 126d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(126).skew()

def cpdt_393_vol_regime_shift_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_393_vol_regime_shift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_shift over 126d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(126).kurt()

def cpdt_394_vol_regime_shift_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_394_vol_regime_shift_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_regime_shift over 252d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(252).skew()

def cpdt_395_vol_regime_shift_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_395_vol_regime_shift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_shift over 252d. Shift in the volatility of trading volume.
    """
    return (volume.rolling(21).std() / volume.rolling(252).std()).rolling(252).kurt()

def cpdt_396_cusum_proxy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_396_cusum_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of cusum_proxy over 5d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(5).skew()

def cpdt_397_cusum_proxy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_397_cusum_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of cusum_proxy over 5d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(5).kurt()

def cpdt_398_cusum_proxy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_398_cusum_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of cusum_proxy over 21d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(21).skew()

def cpdt_399_cusum_proxy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_399_cusum_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of cusum_proxy over 21d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(21).kurt()

def cpdt_400_cusum_proxy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_400_cusum_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of cusum_proxy over 63d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(63).skew()

def cpdt_401_cusum_proxy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_401_cusum_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of cusum_proxy over 63d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(63).kurt()

def cpdt_402_cusum_proxy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_402_cusum_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of cusum_proxy over 126d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(126).skew()

def cpdt_403_cusum_proxy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_403_cusum_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of cusum_proxy over 126d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(126).kurt()

def cpdt_404_cusum_proxy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_404_cusum_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of cusum_proxy over 252d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(252).skew()

def cpdt_405_cusum_proxy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_405_cusum_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of cusum_proxy over 252d. Cumulative sum of deviations from the mean.
    """
    return ((close.diff(1) - close.diff(1).rolling(252).mean()).cumsum()).rolling(252).kurt()

def cpdt_406_change_point_z_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_406_change_point_z_skew_5d
    ECONOMIC RATIONALE: Skewness of change_point_z over 5d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(5).skew()

def cpdt_407_change_point_z_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_407_change_point_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of change_point_z over 5d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(5).kurt()

def cpdt_408_change_point_z_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_408_change_point_z_skew_21d
    ECONOMIC RATIONALE: Skewness of change_point_z over 21d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(21).skew()

def cpdt_409_change_point_z_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_409_change_point_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of change_point_z over 21d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(21).kurt()

def cpdt_410_change_point_z_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_410_change_point_z_skew_63d
    ECONOMIC RATIONALE: Skewness of change_point_z over 63d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(63).skew()

def cpdt_411_change_point_z_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_411_change_point_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of change_point_z over 63d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(63).kurt()

def cpdt_412_change_point_z_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_412_change_point_z_skew_126d
    ECONOMIC RATIONALE: Skewness of change_point_z over 126d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(126).skew()

def cpdt_413_change_point_z_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_413_change_point_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of change_point_z over 126d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(126).kurt()

def cpdt_414_change_point_z_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_414_change_point_z_skew_252d
    ECONOMIC RATIONALE: Skewness of change_point_z over 252d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(252).skew()

def cpdt_415_change_point_z_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_415_change_point_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of change_point_z over 252d. Anomaly detection in the magnitude of daily changes.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(252).kurt()

def cpdt_416_trend_regime_change_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_416_trend_regime_change_skew_5d
    ECONOMIC RATIONALE: Skewness of trend_regime_change over 5d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(5).skew()

def cpdt_417_trend_regime_change_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_417_trend_regime_change_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of trend_regime_change over 5d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(5).kurt()

def cpdt_418_trend_regime_change_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_418_trend_regime_change_skew_21d
    ECONOMIC RATIONALE: Skewness of trend_regime_change over 21d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(21).skew()

def cpdt_419_trend_regime_change_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_419_trend_regime_change_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of trend_regime_change over 21d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(21).kurt()

def cpdt_420_trend_regime_change_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_420_trend_regime_change_skew_63d
    ECONOMIC RATIONALE: Skewness of trend_regime_change over 63d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(63).skew()

def cpdt_421_trend_regime_change_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_421_trend_regime_change_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of trend_regime_change over 63d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(63).kurt()

def cpdt_422_trend_regime_change_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_422_trend_regime_change_skew_126d
    ECONOMIC RATIONALE: Skewness of trend_regime_change over 126d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(126).skew()

def cpdt_423_trend_regime_change_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_423_trend_regime_change_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of trend_regime_change over 126d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(126).kurt()

def cpdt_424_trend_regime_change_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_424_trend_regime_change_skew_252d
    ECONOMIC RATIONALE: Skewness of trend_regime_change over 252d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(252).skew()

def cpdt_425_trend_regime_change_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_425_trend_regime_change_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of trend_regime_change over 252d. Change in trend autocorrelation.
    """
    return (close.rolling(21).mean().diff(1).rolling(5).corr(close.rolling(21).mean().diff(1).shift(21))).rolling(252).kurt()

def cpdt_426_volatility_structural_break_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_426_volatility_structural_break_skew_5d
    ECONOMIC RATIONALE: Skewness of volatility_structural_break over 5d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(5).skew()

def cpdt_427_volatility_structural_break_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_427_volatility_structural_break_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volatility_structural_break over 5d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(5).kurt()

def cpdt_428_volatility_structural_break_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_428_volatility_structural_break_skew_21d
    ECONOMIC RATIONALE: Skewness of volatility_structural_break over 21d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(21).skew()

def cpdt_429_volatility_structural_break_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_429_volatility_structural_break_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volatility_structural_break over 21d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(21).kurt()

def cpdt_430_volatility_structural_break_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_430_volatility_structural_break_skew_63d
    ECONOMIC RATIONALE: Skewness of volatility_structural_break over 63d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(63).skew()

def cpdt_431_volatility_structural_break_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_431_volatility_structural_break_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volatility_structural_break over 63d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(63).kurt()

def cpdt_432_volatility_structural_break_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_432_volatility_structural_break_skew_126d
    ECONOMIC RATIONALE: Skewness of volatility_structural_break over 126d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(126).skew()

def cpdt_433_volatility_structural_break_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_433_volatility_structural_break_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volatility_structural_break over 126d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(126).kurt()

def cpdt_434_volatility_structural_break_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_434_volatility_structural_break_skew_252d
    ECONOMIC RATIONALE: Skewness of volatility_structural_break over 252d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(252).skew()

def cpdt_435_volatility_structural_break_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_435_volatility_structural_break_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volatility_structural_break over 252d. Sudden expansion or contraction of volatility.
    """
    return (close.rolling(21).std() / close.rolling(21).std().shift(21)).rolling(252).kurt()

def cpdt_436_distribution_entropy_shift_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_436_distribution_entropy_shift_skew_5d
    ECONOMIC RATIONALE: Skewness of distribution_entropy_shift over 5d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(5).skew()

def cpdt_437_distribution_entropy_shift_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_437_distribution_entropy_shift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of distribution_entropy_shift over 5d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(5).kurt()

def cpdt_438_distribution_entropy_shift_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_438_distribution_entropy_shift_skew_21d
    ECONOMIC RATIONALE: Skewness of distribution_entropy_shift over 21d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(21).skew()

def cpdt_439_distribution_entropy_shift_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_439_distribution_entropy_shift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of distribution_entropy_shift over 21d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(21).kurt()

def cpdt_440_distribution_entropy_shift_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_440_distribution_entropy_shift_skew_63d
    ECONOMIC RATIONALE: Skewness of distribution_entropy_shift over 63d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(63).skew()

def cpdt_441_distribution_entropy_shift_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_441_distribution_entropy_shift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of distribution_entropy_shift over 63d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(63).kurt()

def cpdt_442_distribution_entropy_shift_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_442_distribution_entropy_shift_skew_126d
    ECONOMIC RATIONALE: Skewness of distribution_entropy_shift over 126d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(126).skew()

def cpdt_443_distribution_entropy_shift_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_443_distribution_entropy_shift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of distribution_entropy_shift over 126d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(126).kurt()

def cpdt_444_distribution_entropy_shift_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_444_distribution_entropy_shift_skew_252d
    ECONOMIC RATIONALE: Skewness of distribution_entropy_shift over 252d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(252).skew()

def cpdt_445_distribution_entropy_shift_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_445_distribution_entropy_shift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of distribution_entropy_shift over 252d. Change in the shape of price distribution.
    """
    return (close.rolling(21).apply(lambda x: np.histogram(x)[0]).diff(21).abs().sum()).rolling(252).kurt()

def cpdt_446_change_point_momentum_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_446_change_point_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of change_point_momentum over 5d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(5).skew()

def cpdt_447_change_point_momentum_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_447_change_point_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of change_point_momentum over 5d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(5).kurt()

def cpdt_448_change_point_momentum_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_448_change_point_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of change_point_momentum over 21d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(21).skew()

def cpdt_449_change_point_momentum_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_449_change_point_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of change_point_momentum over 21d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(21).kurt()

def cpdt_450_change_point_momentum_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_450_change_point_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of change_point_momentum over 63d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(63).skew()

def cpdt_451_change_point_momentum_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_451_change_point_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of change_point_momentum over 63d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(63).kurt()

def cpdt_452_change_point_momentum_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_452_change_point_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of change_point_momentum over 126d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(126).skew()

def cpdt_453_change_point_momentum_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_453_change_point_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of change_point_momentum over 126d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(126).kurt()

def cpdt_454_change_point_momentum_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_454_change_point_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of change_point_momentum over 252d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(252).skew()

def cpdt_455_change_point_momentum_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_455_change_point_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of change_point_momentum over 252d. Acceleration of change magnitude.
    """
    return (close.pct_change(21).abs().diff(21)).rolling(252).kurt()

def cpdt_456_volume_regime_break_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_456_volume_regime_break_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_regime_break over 5d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(5).skew()

def cpdt_457_volume_regime_break_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_457_volume_regime_break_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_regime_break over 5d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(5).kurt()

def cpdt_458_volume_regime_break_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_458_volume_regime_break_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_regime_break over 21d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(21).skew()

def cpdt_459_volume_regime_break_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_459_volume_regime_break_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_regime_break over 21d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(21).kurt()

def cpdt_460_volume_regime_break_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_460_volume_regime_break_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_regime_break over 63d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(63).skew()

def cpdt_461_volume_regime_break_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_461_volume_regime_break_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_regime_break over 63d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(63).kurt()

def cpdt_462_volume_regime_break_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_462_volume_regime_break_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_regime_break over 126d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(126).skew()

def cpdt_463_volume_regime_break_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_463_volume_regime_break_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_regime_break over 126d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(126).kurt()

def cpdt_464_volume_regime_break_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_464_volume_regime_break_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_regime_break over 252d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(252).skew()

def cpdt_465_volume_regime_break_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_465_volume_regime_break_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_regime_break over 252d. Significant change in average volume levels.
    """
    return (volume.rolling(21).mean() / volume.rolling(252).mean()).rolling(252).kurt()

def cpdt_466_price_level_stability_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_466_price_level_stability_skew_5d
    ECONOMIC RATIONALE: Skewness of price_level_stability over 5d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(5).skew()

def cpdt_467_price_level_stability_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_467_price_level_stability_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_level_stability over 5d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(5).kurt()

def cpdt_468_price_level_stability_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_468_price_level_stability_skew_21d
    ECONOMIC RATIONALE: Skewness of price_level_stability over 21d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(21).skew()

def cpdt_469_price_level_stability_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_469_price_level_stability_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_level_stability over 21d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(21).kurt()

def cpdt_470_price_level_stability_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_470_price_level_stability_skew_63d
    ECONOMIC RATIONALE: Skewness of price_level_stability over 63d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(63).skew()

def cpdt_471_price_level_stability_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_471_price_level_stability_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_level_stability over 63d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(63).kurt()

def cpdt_472_price_level_stability_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_472_price_level_stability_skew_126d
    ECONOMIC RATIONALE: Skewness of price_level_stability over 126d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(126).skew()

def cpdt_473_price_level_stability_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_473_price_level_stability_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_level_stability over 126d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(126).kurt()

def cpdt_474_price_level_stability_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_474_price_level_stability_skew_252d
    ECONOMIC RATIONALE: Skewness of price_level_stability over 252d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(252).skew()

def cpdt_475_price_level_stability_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_475_price_level_stability_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_level_stability over 252d. Inversely related to regime stability.
    """
    return (close.rolling(21).std() / close).rolling(252).kurt()

def cpdt_476_structural_break_score_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_476_structural_break_score_skew_5d
    ECONOMIC RATIONALE: Skewness of structural_break_score over 5d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(5).skew()

def cpdt_477_structural_break_score_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_477_structural_break_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of structural_break_score over 5d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(5).kurt()

def cpdt_478_structural_break_score_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_478_structural_break_score_skew_21d
    ECONOMIC RATIONALE: Skewness of structural_break_score over 21d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(21).skew()

def cpdt_479_structural_break_score_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_479_structural_break_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of structural_break_score over 21d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(21).kurt()

def cpdt_480_structural_break_score_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_480_structural_break_score_skew_63d
    ECONOMIC RATIONALE: Skewness of structural_break_score over 63d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(63).skew()

def cpdt_481_structural_break_score_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_481_structural_break_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of structural_break_score over 63d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(63).kurt()

def cpdt_482_structural_break_score_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_482_structural_break_score_skew_126d
    ECONOMIC RATIONALE: Skewness of structural_break_score over 126d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(126).skew()

def cpdt_483_structural_break_score_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_483_structural_break_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of structural_break_score over 126d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(126).kurt()

def cpdt_484_structural_break_score_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_484_structural_break_score_skew_252d
    ECONOMIC RATIONALE: Skewness of structural_break_score over 252d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(252).skew()

def cpdt_485_structural_break_score_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_485_structural_break_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of structural_break_score over 252d. Binary indicator of structural price breaks.
    """
    return ((close.diff(21).abs() > 2*close.rolling(252).std()).astype(float)).rolling(252).kurt()

def cpdt_486_regime_switching_proxy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_486_regime_switching_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of regime_switching_proxy over 5d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(5).skew()

def cpdt_487_regime_switching_proxy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_487_regime_switching_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of regime_switching_proxy over 5d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(5).kurt()

def cpdt_488_regime_switching_proxy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_488_regime_switching_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of regime_switching_proxy over 21d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(21).skew()

def cpdt_489_regime_switching_proxy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_489_regime_switching_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of regime_switching_proxy over 21d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(21).kurt()

def cpdt_490_regime_switching_proxy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_490_regime_switching_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of regime_switching_proxy over 63d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(63).skew()

def cpdt_491_regime_switching_proxy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_491_regime_switching_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of regime_switching_proxy over 63d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(63).kurt()

def cpdt_492_regime_switching_proxy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_492_regime_switching_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of regime_switching_proxy over 126d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(126).skew()

def cpdt_493_regime_switching_proxy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_493_regime_switching_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of regime_switching_proxy over 126d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(126).kurt()

def cpdt_494_regime_switching_proxy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_494_regime_switching_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of regime_switching_proxy over 252d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(252).skew()

def cpdt_495_regime_switching_proxy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_495_regime_switching_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of regime_switching_proxy over 252d. Stability of the current local trend.
    """
    return (close.rolling(10).mean().corr(np.arange(10))).rolling(252).kurt()

def cpdt_496_autocorr_regime_shift_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_496_autocorr_regime_shift_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_shift over 5d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(5).skew()

def cpdt_497_autocorr_regime_shift_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_497_autocorr_regime_shift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_shift over 5d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(5).kurt()

def cpdt_498_autocorr_regime_shift_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_498_autocorr_regime_shift_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_shift over 21d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(21).skew()

def cpdt_499_autocorr_regime_shift_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_499_autocorr_regime_shift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_shift over 21d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(21).kurt()

def cpdt_500_autocorr_regime_shift_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_500_autocorr_regime_shift_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_shift over 63d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(63).skew()

def cpdt_501_autocorr_regime_shift_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_501_autocorr_regime_shift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_shift over 63d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(63).kurt()

def cpdt_502_autocorr_regime_shift_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_502_autocorr_regime_shift_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_shift over 126d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(126).skew()

def cpdt_503_autocorr_regime_shift_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_503_autocorr_regime_shift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_shift over 126d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(126).kurt()

def cpdt_504_autocorr_regime_shift_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_504_autocorr_regime_shift_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_shift over 252d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(252).skew()

def cpdt_505_autocorr_regime_shift_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_505_autocorr_regime_shift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_shift over 252d. Shift in the serial correlation of returns.
    """
    return (close.rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(252).kurt()

def cpdt_506_tail_event_density_change_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_506_tail_event_density_change_skew_5d
    ECONOMIC RATIONALE: Skewness of tail_event_density_change over 5d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(5).skew()

def cpdt_507_tail_event_density_change_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_507_tail_event_density_change_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density_change over 5d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(5).kurt()

def cpdt_508_tail_event_density_change_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_508_tail_event_density_change_skew_21d
    ECONOMIC RATIONALE: Skewness of tail_event_density_change over 21d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(21).skew()

def cpdt_509_tail_event_density_change_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_509_tail_event_density_change_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density_change over 21d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(21).kurt()

def cpdt_510_tail_event_density_change_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_510_tail_event_density_change_skew_63d
    ECONOMIC RATIONALE: Skewness of tail_event_density_change over 63d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(63).skew()

def cpdt_511_tail_event_density_change_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_511_tail_event_density_change_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density_change over 63d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(63).kurt()

def cpdt_512_tail_event_density_change_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_512_tail_event_density_change_skew_126d
    ECONOMIC RATIONALE: Skewness of tail_event_density_change over 126d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(126).skew()

def cpdt_513_tail_event_density_change_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_513_tail_event_density_change_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density_change over 126d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(126).kurt()

def cpdt_514_tail_event_density_change_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_514_tail_event_density_change_skew_252d
    ECONOMIC RATIONALE: Skewness of tail_event_density_change over 252d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(252).skew()

def cpdt_515_tail_event_density_change_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_515_tail_event_density_change_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tail_event_density_change over 252d. Change in the frequency of tail events.
    """
    return ((close.pct_change(1).abs() > 2*close.pct_change(1).rolling(252).std()).rolling(21).sum()).rolling(252).kurt()

def cpdt_516_price_volume_regime_corr_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_516_price_volume_regime_corr_skew_5d
    ECONOMIC RATIONALE: Skewness of price_volume_regime_corr over 5d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(5).skew()

def cpdt_517_price_volume_regime_corr_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_517_price_volume_regime_corr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_volume_regime_corr over 5d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(5).kurt()

def cpdt_518_price_volume_regime_corr_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_518_price_volume_regime_corr_skew_21d
    ECONOMIC RATIONALE: Skewness of price_volume_regime_corr over 21d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(21).skew()

def cpdt_519_price_volume_regime_corr_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_519_price_volume_regime_corr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_volume_regime_corr over 21d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(21).kurt()

def cpdt_520_price_volume_regime_corr_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_520_price_volume_regime_corr_skew_63d
    ECONOMIC RATIONALE: Skewness of price_volume_regime_corr over 63d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(63).skew()

def cpdt_521_price_volume_regime_corr_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_521_price_volume_regime_corr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_volume_regime_corr over 63d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(63).kurt()

def cpdt_522_price_volume_regime_corr_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_522_price_volume_regime_corr_skew_126d
    ECONOMIC RATIONALE: Skewness of price_volume_regime_corr over 126d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(126).skew()

def cpdt_523_price_volume_regime_corr_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_523_price_volume_regime_corr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_volume_regime_corr over 126d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(126).kurt()

def cpdt_524_price_volume_regime_corr_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_524_price_volume_regime_corr_skew_252d
    ECONOMIC RATIONALE: Skewness of price_volume_regime_corr over 252d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(252).skew()

def cpdt_525_price_volume_regime_corr_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    cpdt_525_price_volume_regime_corr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_volume_regime_corr over 252d. Shift in the relationship between price and volume.
    """
    return (close.rolling(21).corr(volume).diff(21)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V107_REGISTRY_MOMENTS = {
    "cpdt_376_mean_shift_detection_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_376_mean_shift_detection_skew_5d},
    "cpdt_377_mean_shift_detection_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_377_mean_shift_detection_kurt_5d},
    "cpdt_378_mean_shift_detection_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_378_mean_shift_detection_skew_21d},
    "cpdt_379_mean_shift_detection_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_379_mean_shift_detection_kurt_21d},
    "cpdt_380_mean_shift_detection_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_380_mean_shift_detection_skew_63d},
    "cpdt_381_mean_shift_detection_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_381_mean_shift_detection_kurt_63d},
    "cpdt_382_mean_shift_detection_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_382_mean_shift_detection_skew_126d},
    "cpdt_383_mean_shift_detection_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_383_mean_shift_detection_kurt_126d},
    "cpdt_384_mean_shift_detection_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_384_mean_shift_detection_skew_252d},
    "cpdt_385_mean_shift_detection_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_385_mean_shift_detection_kurt_252d},
    "cpdt_386_vol_regime_shift_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_386_vol_regime_shift_skew_5d},
    "cpdt_387_vol_regime_shift_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_387_vol_regime_shift_kurt_5d},
    "cpdt_388_vol_regime_shift_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_388_vol_regime_shift_skew_21d},
    "cpdt_389_vol_regime_shift_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_389_vol_regime_shift_kurt_21d},
    "cpdt_390_vol_regime_shift_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_390_vol_regime_shift_skew_63d},
    "cpdt_391_vol_regime_shift_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_391_vol_regime_shift_kurt_63d},
    "cpdt_392_vol_regime_shift_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_392_vol_regime_shift_skew_126d},
    "cpdt_393_vol_regime_shift_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_393_vol_regime_shift_kurt_126d},
    "cpdt_394_vol_regime_shift_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_394_vol_regime_shift_skew_252d},
    "cpdt_395_vol_regime_shift_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_395_vol_regime_shift_kurt_252d},
    "cpdt_396_cusum_proxy_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_396_cusum_proxy_skew_5d},
    "cpdt_397_cusum_proxy_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_397_cusum_proxy_kurt_5d},
    "cpdt_398_cusum_proxy_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_398_cusum_proxy_skew_21d},
    "cpdt_399_cusum_proxy_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_399_cusum_proxy_kurt_21d},
    "cpdt_400_cusum_proxy_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_400_cusum_proxy_skew_63d},
    "cpdt_401_cusum_proxy_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_401_cusum_proxy_kurt_63d},
    "cpdt_402_cusum_proxy_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_402_cusum_proxy_skew_126d},
    "cpdt_403_cusum_proxy_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_403_cusum_proxy_kurt_126d},
    "cpdt_404_cusum_proxy_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_404_cusum_proxy_skew_252d},
    "cpdt_405_cusum_proxy_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_405_cusum_proxy_kurt_252d},
    "cpdt_406_change_point_z_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_406_change_point_z_skew_5d},
    "cpdt_407_change_point_z_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_407_change_point_z_kurt_5d},
    "cpdt_408_change_point_z_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_408_change_point_z_skew_21d},
    "cpdt_409_change_point_z_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_409_change_point_z_kurt_21d},
    "cpdt_410_change_point_z_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_410_change_point_z_skew_63d},
    "cpdt_411_change_point_z_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_411_change_point_z_kurt_63d},
    "cpdt_412_change_point_z_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_412_change_point_z_skew_126d},
    "cpdt_413_change_point_z_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_413_change_point_z_kurt_126d},
    "cpdt_414_change_point_z_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_414_change_point_z_skew_252d},
    "cpdt_415_change_point_z_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_415_change_point_z_kurt_252d},
    "cpdt_416_trend_regime_change_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_416_trend_regime_change_skew_5d},
    "cpdt_417_trend_regime_change_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_417_trend_regime_change_kurt_5d},
    "cpdt_418_trend_regime_change_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_418_trend_regime_change_skew_21d},
    "cpdt_419_trend_regime_change_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_419_trend_regime_change_kurt_21d},
    "cpdt_420_trend_regime_change_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_420_trend_regime_change_skew_63d},
    "cpdt_421_trend_regime_change_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_421_trend_regime_change_kurt_63d},
    "cpdt_422_trend_regime_change_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_422_trend_regime_change_skew_126d},
    "cpdt_423_trend_regime_change_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_423_trend_regime_change_kurt_126d},
    "cpdt_424_trend_regime_change_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_424_trend_regime_change_skew_252d},
    "cpdt_425_trend_regime_change_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_425_trend_regime_change_kurt_252d},
    "cpdt_426_volatility_structural_break_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_426_volatility_structural_break_skew_5d},
    "cpdt_427_volatility_structural_break_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_427_volatility_structural_break_kurt_5d},
    "cpdt_428_volatility_structural_break_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_428_volatility_structural_break_skew_21d},
    "cpdt_429_volatility_structural_break_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_429_volatility_structural_break_kurt_21d},
    "cpdt_430_volatility_structural_break_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_430_volatility_structural_break_skew_63d},
    "cpdt_431_volatility_structural_break_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_431_volatility_structural_break_kurt_63d},
    "cpdt_432_volatility_structural_break_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_432_volatility_structural_break_skew_126d},
    "cpdt_433_volatility_structural_break_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_433_volatility_structural_break_kurt_126d},
    "cpdt_434_volatility_structural_break_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_434_volatility_structural_break_skew_252d},
    "cpdt_435_volatility_structural_break_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_435_volatility_structural_break_kurt_252d},
    "cpdt_436_distribution_entropy_shift_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_436_distribution_entropy_shift_skew_5d},
    "cpdt_437_distribution_entropy_shift_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_437_distribution_entropy_shift_kurt_5d},
    "cpdt_438_distribution_entropy_shift_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_438_distribution_entropy_shift_skew_21d},
    "cpdt_439_distribution_entropy_shift_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_439_distribution_entropy_shift_kurt_21d},
    "cpdt_440_distribution_entropy_shift_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_440_distribution_entropy_shift_skew_63d},
    "cpdt_441_distribution_entropy_shift_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_441_distribution_entropy_shift_kurt_63d},
    "cpdt_442_distribution_entropy_shift_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_442_distribution_entropy_shift_skew_126d},
    "cpdt_443_distribution_entropy_shift_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_443_distribution_entropy_shift_kurt_126d},
    "cpdt_444_distribution_entropy_shift_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_444_distribution_entropy_shift_skew_252d},
    "cpdt_445_distribution_entropy_shift_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_445_distribution_entropy_shift_kurt_252d},
    "cpdt_446_change_point_momentum_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_446_change_point_momentum_skew_5d},
    "cpdt_447_change_point_momentum_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_447_change_point_momentum_kurt_5d},
    "cpdt_448_change_point_momentum_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_448_change_point_momentum_skew_21d},
    "cpdt_449_change_point_momentum_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_449_change_point_momentum_kurt_21d},
    "cpdt_450_change_point_momentum_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_450_change_point_momentum_skew_63d},
    "cpdt_451_change_point_momentum_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_451_change_point_momentum_kurt_63d},
    "cpdt_452_change_point_momentum_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_452_change_point_momentum_skew_126d},
    "cpdt_453_change_point_momentum_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_453_change_point_momentum_kurt_126d},
    "cpdt_454_change_point_momentum_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_454_change_point_momentum_skew_252d},
    "cpdt_455_change_point_momentum_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_455_change_point_momentum_kurt_252d},
    "cpdt_456_volume_regime_break_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_456_volume_regime_break_skew_5d},
    "cpdt_457_volume_regime_break_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_457_volume_regime_break_kurt_5d},
    "cpdt_458_volume_regime_break_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_458_volume_regime_break_skew_21d},
    "cpdt_459_volume_regime_break_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_459_volume_regime_break_kurt_21d},
    "cpdt_460_volume_regime_break_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_460_volume_regime_break_skew_63d},
    "cpdt_461_volume_regime_break_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_461_volume_regime_break_kurt_63d},
    "cpdt_462_volume_regime_break_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_462_volume_regime_break_skew_126d},
    "cpdt_463_volume_regime_break_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_463_volume_regime_break_kurt_126d},
    "cpdt_464_volume_regime_break_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_464_volume_regime_break_skew_252d},
    "cpdt_465_volume_regime_break_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_465_volume_regime_break_kurt_252d},
    "cpdt_466_price_level_stability_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_466_price_level_stability_skew_5d},
    "cpdt_467_price_level_stability_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_467_price_level_stability_kurt_5d},
    "cpdt_468_price_level_stability_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_468_price_level_stability_skew_21d},
    "cpdt_469_price_level_stability_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_469_price_level_stability_kurt_21d},
    "cpdt_470_price_level_stability_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_470_price_level_stability_skew_63d},
    "cpdt_471_price_level_stability_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_471_price_level_stability_kurt_63d},
    "cpdt_472_price_level_stability_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_472_price_level_stability_skew_126d},
    "cpdt_473_price_level_stability_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_473_price_level_stability_kurt_126d},
    "cpdt_474_price_level_stability_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_474_price_level_stability_skew_252d},
    "cpdt_475_price_level_stability_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_475_price_level_stability_kurt_252d},
    "cpdt_476_structural_break_score_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_476_structural_break_score_skew_5d},
    "cpdt_477_structural_break_score_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_477_structural_break_score_kurt_5d},
    "cpdt_478_structural_break_score_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_478_structural_break_score_skew_21d},
    "cpdt_479_structural_break_score_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_479_structural_break_score_kurt_21d},
    "cpdt_480_structural_break_score_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_480_structural_break_score_skew_63d},
    "cpdt_481_structural_break_score_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_481_structural_break_score_kurt_63d},
    "cpdt_482_structural_break_score_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_482_structural_break_score_skew_126d},
    "cpdt_483_structural_break_score_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_483_structural_break_score_kurt_126d},
    "cpdt_484_structural_break_score_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_484_structural_break_score_skew_252d},
    "cpdt_485_structural_break_score_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_485_structural_break_score_kurt_252d},
    "cpdt_486_regime_switching_proxy_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_486_regime_switching_proxy_skew_5d},
    "cpdt_487_regime_switching_proxy_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_487_regime_switching_proxy_kurt_5d},
    "cpdt_488_regime_switching_proxy_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_488_regime_switching_proxy_skew_21d},
    "cpdt_489_regime_switching_proxy_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_489_regime_switching_proxy_kurt_21d},
    "cpdt_490_regime_switching_proxy_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_490_regime_switching_proxy_skew_63d},
    "cpdt_491_regime_switching_proxy_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_491_regime_switching_proxy_kurt_63d},
    "cpdt_492_regime_switching_proxy_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_492_regime_switching_proxy_skew_126d},
    "cpdt_493_regime_switching_proxy_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_493_regime_switching_proxy_kurt_126d},
    "cpdt_494_regime_switching_proxy_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_494_regime_switching_proxy_skew_252d},
    "cpdt_495_regime_switching_proxy_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_495_regime_switching_proxy_kurt_252d},
    "cpdt_496_autocorr_regime_shift_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_496_autocorr_regime_shift_skew_5d},
    "cpdt_497_autocorr_regime_shift_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_497_autocorr_regime_shift_kurt_5d},
    "cpdt_498_autocorr_regime_shift_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_498_autocorr_regime_shift_skew_21d},
    "cpdt_499_autocorr_regime_shift_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_499_autocorr_regime_shift_kurt_21d},
    "cpdt_500_autocorr_regime_shift_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_500_autocorr_regime_shift_skew_63d},
    "cpdt_501_autocorr_regime_shift_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_501_autocorr_regime_shift_kurt_63d},
    "cpdt_502_autocorr_regime_shift_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_502_autocorr_regime_shift_skew_126d},
    "cpdt_503_autocorr_regime_shift_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_503_autocorr_regime_shift_kurt_126d},
    "cpdt_504_autocorr_regime_shift_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_504_autocorr_regime_shift_skew_252d},
    "cpdt_505_autocorr_regime_shift_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_505_autocorr_regime_shift_kurt_252d},
    "cpdt_506_tail_event_density_change_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_506_tail_event_density_change_skew_5d},
    "cpdt_507_tail_event_density_change_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_507_tail_event_density_change_kurt_5d},
    "cpdt_508_tail_event_density_change_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_508_tail_event_density_change_skew_21d},
    "cpdt_509_tail_event_density_change_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_509_tail_event_density_change_kurt_21d},
    "cpdt_510_tail_event_density_change_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_510_tail_event_density_change_skew_63d},
    "cpdt_511_tail_event_density_change_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_511_tail_event_density_change_kurt_63d},
    "cpdt_512_tail_event_density_change_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_512_tail_event_density_change_skew_126d},
    "cpdt_513_tail_event_density_change_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_513_tail_event_density_change_kurt_126d},
    "cpdt_514_tail_event_density_change_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_514_tail_event_density_change_skew_252d},
    "cpdt_515_tail_event_density_change_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_515_tail_event_density_change_kurt_252d},
    "cpdt_516_price_volume_regime_corr_skew_5d": {"inputs": ["close", "volume"], "func": cpdt_516_price_volume_regime_corr_skew_5d},
    "cpdt_517_price_volume_regime_corr_kurt_5d": {"inputs": ["close", "volume"], "func": cpdt_517_price_volume_regime_corr_kurt_5d},
    "cpdt_518_price_volume_regime_corr_skew_21d": {"inputs": ["close", "volume"], "func": cpdt_518_price_volume_regime_corr_skew_21d},
    "cpdt_519_price_volume_regime_corr_kurt_21d": {"inputs": ["close", "volume"], "func": cpdt_519_price_volume_regime_corr_kurt_21d},
    "cpdt_520_price_volume_regime_corr_skew_63d": {"inputs": ["close", "volume"], "func": cpdt_520_price_volume_regime_corr_skew_63d},
    "cpdt_521_price_volume_regime_corr_kurt_63d": {"inputs": ["close", "volume"], "func": cpdt_521_price_volume_regime_corr_kurt_63d},
    "cpdt_522_price_volume_regime_corr_skew_126d": {"inputs": ["close", "volume"], "func": cpdt_522_price_volume_regime_corr_skew_126d},
    "cpdt_523_price_volume_regime_corr_kurt_126d": {"inputs": ["close", "volume"], "func": cpdt_523_price_volume_regime_corr_kurt_126d},
    "cpdt_524_price_volume_regime_corr_skew_252d": {"inputs": ["close", "volume"], "func": cpdt_524_price_volume_regime_corr_skew_252d},
    "cpdt_525_price_volume_regime_corr_kurt_252d": {"inputs": ["close", "volume"], "func": cpdt_525_price_volume_regime_corr_kurt_252d},
}
