"""
104_mean_reversion_potential — Statistical Moments
Domain: mean_reversion_potential
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

def mrpt_376_bollinger_pct_b_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_376_bollinger_pct_b_skew_5d
    ECONOMIC RATIONALE: Skewness of bollinger_pct_b over 5d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(5).skew()

def mrpt_377_bollinger_pct_b_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_377_bollinger_pct_b_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of bollinger_pct_b over 5d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(5).kurt()

def mrpt_378_bollinger_pct_b_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_378_bollinger_pct_b_skew_21d
    ECONOMIC RATIONALE: Skewness of bollinger_pct_b over 21d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(21).skew()

def mrpt_379_bollinger_pct_b_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_379_bollinger_pct_b_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of bollinger_pct_b over 21d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(21).kurt()

def mrpt_380_bollinger_pct_b_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_380_bollinger_pct_b_skew_63d
    ECONOMIC RATIONALE: Skewness of bollinger_pct_b over 63d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(63).skew()

def mrpt_381_bollinger_pct_b_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_381_bollinger_pct_b_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of bollinger_pct_b over 63d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(63).kurt()

def mrpt_382_bollinger_pct_b_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_382_bollinger_pct_b_skew_126d
    ECONOMIC RATIONALE: Skewness of bollinger_pct_b over 126d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(126).skew()

def mrpt_383_bollinger_pct_b_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_383_bollinger_pct_b_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of bollinger_pct_b over 126d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(126).kurt()

def mrpt_384_bollinger_pct_b_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_384_bollinger_pct_b_skew_252d
    ECONOMIC RATIONALE: Skewness of bollinger_pct_b over 252d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(252).skew()

def mrpt_385_bollinger_pct_b_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_385_bollinger_pct_b_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of bollinger_pct_b over 252d. Position within Bollinger Bands.
    """
    return ((close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)).rolling(252).kurt()

def mrpt_386_distance_from_ma200_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_386_distance_from_ma200_skew_5d
    ECONOMIC RATIONALE: Skewness of distance_from_ma200 over 5d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(5).skew()

def mrpt_387_distance_from_ma200_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_387_distance_from_ma200_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of distance_from_ma200 over 5d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(5).kurt()

def mrpt_388_distance_from_ma200_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_388_distance_from_ma200_skew_21d
    ECONOMIC RATIONALE: Skewness of distance_from_ma200 over 21d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(21).skew()

def mrpt_389_distance_from_ma200_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_389_distance_from_ma200_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of distance_from_ma200 over 21d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(21).kurt()

def mrpt_390_distance_from_ma200_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_390_distance_from_ma200_skew_63d
    ECONOMIC RATIONALE: Skewness of distance_from_ma200 over 63d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(63).skew()

def mrpt_391_distance_from_ma200_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_391_distance_from_ma200_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of distance_from_ma200 over 63d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(63).kurt()

def mrpt_392_distance_from_ma200_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_392_distance_from_ma200_skew_126d
    ECONOMIC RATIONALE: Skewness of distance_from_ma200 over 126d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(126).skew()

def mrpt_393_distance_from_ma200_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_393_distance_from_ma200_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of distance_from_ma200 over 126d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(126).kurt()

def mrpt_394_distance_from_ma200_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_394_distance_from_ma200_skew_252d
    ECONOMIC RATIONALE: Skewness of distance_from_ma200 over 252d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(252).skew()

def mrpt_395_distance_from_ma200_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_395_distance_from_ma200_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of distance_from_ma200 over 252d. Percentage deviation from the 200-day moving average.
    """
    return (close / close.rolling(252).mean() - 1).rolling(252).kurt()

def mrpt_396_keltner_channel_lower_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_396_keltner_channel_lower_skew_5d
    ECONOMIC RATIONALE: Skewness of keltner_channel_lower over 5d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(5).skew()

def mrpt_397_keltner_channel_lower_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_397_keltner_channel_lower_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of keltner_channel_lower over 5d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(5).kurt()

def mrpt_398_keltner_channel_lower_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_398_keltner_channel_lower_skew_21d
    ECONOMIC RATIONALE: Skewness of keltner_channel_lower over 21d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(21).skew()

def mrpt_399_keltner_channel_lower_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_399_keltner_channel_lower_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of keltner_channel_lower over 21d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(21).kurt()

def mrpt_400_keltner_channel_lower_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_400_keltner_channel_lower_skew_63d
    ECONOMIC RATIONALE: Skewness of keltner_channel_lower over 63d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(63).skew()

def mrpt_401_keltner_channel_lower_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_401_keltner_channel_lower_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of keltner_channel_lower over 63d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(63).kurt()

def mrpt_402_keltner_channel_lower_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_402_keltner_channel_lower_skew_126d
    ECONOMIC RATIONALE: Skewness of keltner_channel_lower over 126d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(126).skew()

def mrpt_403_keltner_channel_lower_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_403_keltner_channel_lower_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of keltner_channel_lower over 126d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(126).kurt()

def mrpt_404_keltner_channel_lower_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_404_keltner_channel_lower_skew_252d
    ECONOMIC RATIONALE: Skewness of keltner_channel_lower over 252d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(252).skew()

def mrpt_405_keltner_channel_lower_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_405_keltner_channel_lower_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of keltner_channel_lower over 252d. Position relative to Keltner Channels.
    """
    return (close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1).rolling(252).kurt()

def mrpt_406_mean_reversion_z_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_406_mean_reversion_z_skew_5d
    ECONOMIC RATIONALE: Skewness of mean_reversion_z over 5d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(5).skew()

def mrpt_407_mean_reversion_z_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_407_mean_reversion_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_z over 5d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(5).kurt()

def mrpt_408_mean_reversion_z_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_408_mean_reversion_z_skew_21d
    ECONOMIC RATIONALE: Skewness of mean_reversion_z over 21d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(21).skew()

def mrpt_409_mean_reversion_z_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_409_mean_reversion_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_z over 21d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(21).kurt()

def mrpt_410_mean_reversion_z_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_410_mean_reversion_z_skew_63d
    ECONOMIC RATIONALE: Skewness of mean_reversion_z over 63d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(63).skew()

def mrpt_411_mean_reversion_z_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_411_mean_reversion_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_z over 63d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(63).kurt()

def mrpt_412_mean_reversion_z_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_412_mean_reversion_z_skew_126d
    ECONOMIC RATIONALE: Skewness of mean_reversion_z over 126d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(126).skew()

def mrpt_413_mean_reversion_z_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_413_mean_reversion_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_z over 126d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(126).kurt()

def mrpt_414_mean_reversion_z_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_414_mean_reversion_z_skew_252d
    ECONOMIC RATIONALE: Skewness of mean_reversion_z over 252d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(252).skew()

def mrpt_415_mean_reversion_z_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_415_mean_reversion_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_z over 252d. Z-score relative to 63-day price distribution.
    """
    return (_zscore_rolling(close, 63)).rolling(252).kurt()

def mrpt_416_extreme_stretch_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_416_extreme_stretch_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_stretch over 5d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(5).skew()

def mrpt_417_extreme_stretch_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_417_extreme_stretch_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_stretch over 5d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(5).kurt()

def mrpt_418_extreme_stretch_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_418_extreme_stretch_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_stretch over 21d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(21).skew()

def mrpt_419_extreme_stretch_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_419_extreme_stretch_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_stretch over 21d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(21).kurt()

def mrpt_420_extreme_stretch_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_420_extreme_stretch_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_stretch over 63d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(63).skew()

def mrpt_421_extreme_stretch_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_421_extreme_stretch_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_stretch over 63d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(63).kurt()

def mrpt_422_extreme_stretch_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_422_extreme_stretch_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_stretch over 126d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(126).skew()

def mrpt_423_extreme_stretch_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_423_extreme_stretch_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_stretch over 126d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(126).kurt()

def mrpt_424_extreme_stretch_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_424_extreme_stretch_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_stretch over 252d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(252).skew()

def mrpt_425_extreme_stretch_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_425_extreme_stretch_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_stretch over 252d. Short-term price stretch from the mean.
    """
    return (close / close.rolling(5).mean() - 1).rolling(252).kurt()

def mrpt_426_reversion_velocity_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_426_reversion_velocity_skew_5d
    ECONOMIC RATIONALE: Skewness of reversion_velocity over 5d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(5).skew()

def mrpt_427_reversion_velocity_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_427_reversion_velocity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of reversion_velocity over 5d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(5).kurt()

def mrpt_428_reversion_velocity_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_428_reversion_velocity_skew_21d
    ECONOMIC RATIONALE: Skewness of reversion_velocity over 21d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(21).skew()

def mrpt_429_reversion_velocity_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_429_reversion_velocity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of reversion_velocity over 21d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(21).kurt()

def mrpt_430_reversion_velocity_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_430_reversion_velocity_skew_63d
    ECONOMIC RATIONALE: Skewness of reversion_velocity over 63d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(63).skew()

def mrpt_431_reversion_velocity_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_431_reversion_velocity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of reversion_velocity over 63d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(63).kurt()

def mrpt_432_reversion_velocity_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_432_reversion_velocity_skew_126d
    ECONOMIC RATIONALE: Skewness of reversion_velocity over 126d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(126).skew()

def mrpt_433_reversion_velocity_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_433_reversion_velocity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of reversion_velocity over 126d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(126).kurt()

def mrpt_434_reversion_velocity_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_434_reversion_velocity_skew_252d
    ECONOMIC RATIONALE: Skewness of reversion_velocity over 252d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(252).skew()

def mrpt_435_reversion_velocity_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_435_reversion_velocity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of reversion_velocity over 252d. Price change normalized by volatility.
    """
    return (close.diff(5) / close.rolling(21).std()).rolling(252).kurt()

def mrpt_436_ma_cross_intensity_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_436_ma_cross_intensity_skew_5d
    ECONOMIC RATIONALE: Skewness of ma_cross_intensity over 5d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(5).skew()

def mrpt_437_ma_cross_intensity_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_437_ma_cross_intensity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ma_cross_intensity over 5d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(5).kurt()

def mrpt_438_ma_cross_intensity_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_438_ma_cross_intensity_skew_21d
    ECONOMIC RATIONALE: Skewness of ma_cross_intensity over 21d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(21).skew()

def mrpt_439_ma_cross_intensity_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_439_ma_cross_intensity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ma_cross_intensity over 21d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(21).kurt()

def mrpt_440_ma_cross_intensity_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_440_ma_cross_intensity_skew_63d
    ECONOMIC RATIONALE: Skewness of ma_cross_intensity over 63d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(63).skew()

def mrpt_441_ma_cross_intensity_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_441_ma_cross_intensity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ma_cross_intensity over 63d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(63).kurt()

def mrpt_442_ma_cross_intensity_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_442_ma_cross_intensity_skew_126d
    ECONOMIC RATIONALE: Skewness of ma_cross_intensity over 126d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(126).skew()

def mrpt_443_ma_cross_intensity_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_443_ma_cross_intensity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ma_cross_intensity over 126d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(126).kurt()

def mrpt_444_ma_cross_intensity_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_444_ma_cross_intensity_skew_252d
    ECONOMIC RATIONALE: Skewness of ma_cross_intensity over 252d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(252).skew()

def mrpt_445_ma_cross_intensity_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_445_ma_cross_intensity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ma_cross_intensity over 252d. Intensity of short-term MA crossover.
    """
    return ((close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()).rolling(252).kurt()

def mrpt_446_overshot_magnitude_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_446_overshot_magnitude_skew_5d
    ECONOMIC RATIONALE: Skewness of overshot_magnitude over 5d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(5).skew()

def mrpt_447_overshot_magnitude_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_447_overshot_magnitude_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overshot_magnitude over 5d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(5).kurt()

def mrpt_448_overshot_magnitude_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_448_overshot_magnitude_skew_21d
    ECONOMIC RATIONALE: Skewness of overshot_magnitude over 21d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(21).skew()

def mrpt_449_overshot_magnitude_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_449_overshot_magnitude_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overshot_magnitude over 21d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(21).kurt()

def mrpt_450_overshot_magnitude_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_450_overshot_magnitude_skew_63d
    ECONOMIC RATIONALE: Skewness of overshot_magnitude over 63d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(63).skew()

def mrpt_451_overshot_magnitude_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_451_overshot_magnitude_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overshot_magnitude over 63d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(63).kurt()

def mrpt_452_overshot_magnitude_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_452_overshot_magnitude_skew_126d
    ECONOMIC RATIONALE: Skewness of overshot_magnitude over 126d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(126).skew()

def mrpt_453_overshot_magnitude_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_453_overshot_magnitude_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overshot_magnitude over 126d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(126).kurt()

def mrpt_454_overshot_magnitude_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_454_overshot_magnitude_skew_252d
    ECONOMIC RATIONALE: Skewness of overshot_magnitude over 252d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(252).skew()

def mrpt_455_overshot_magnitude_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_455_overshot_magnitude_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overshot_magnitude over 252d. Intraday low's distance from the mean.
    """
    return (low / close.rolling(20).mean() - 1).rolling(252).kurt()

def mrpt_456_mean_reversion_rank_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_456_mean_reversion_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of mean_reversion_rank over 5d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(5).skew()

def mrpt_457_mean_reversion_rank_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_457_mean_reversion_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_rank over 5d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(5).kurt()

def mrpt_458_mean_reversion_rank_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_458_mean_reversion_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of mean_reversion_rank over 21d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(21).skew()

def mrpt_459_mean_reversion_rank_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_459_mean_reversion_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_rank over 21d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(21).kurt()

def mrpt_460_mean_reversion_rank_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_460_mean_reversion_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of mean_reversion_rank over 63d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(63).skew()

def mrpt_461_mean_reversion_rank_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_461_mean_reversion_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_rank over 63d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(63).kurt()

def mrpt_462_mean_reversion_rank_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_462_mean_reversion_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of mean_reversion_rank over 126d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(126).skew()

def mrpt_463_mean_reversion_rank_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_463_mean_reversion_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_rank over 126d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(126).kurt()

def mrpt_464_mean_reversion_rank_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_464_mean_reversion_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of mean_reversion_rank over 252d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(252).skew()

def mrpt_465_mean_reversion_rank_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_465_mean_reversion_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_rank over 252d. Historical rank of current mean deviation.
    """
    return (_rank_pct(close / close.rolling(63).mean(), 252)).rolling(252).kurt()

def mrpt_466_volatility_adjusted_stretch_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_466_volatility_adjusted_stretch_skew_5d
    ECONOMIC RATIONALE: Skewness of volatility_adjusted_stretch over 5d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(5).skew()

def mrpt_467_volatility_adjusted_stretch_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_467_volatility_adjusted_stretch_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volatility_adjusted_stretch over 5d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(5).kurt()

def mrpt_468_volatility_adjusted_stretch_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_468_volatility_adjusted_stretch_skew_21d
    ECONOMIC RATIONALE: Skewness of volatility_adjusted_stretch over 21d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(21).skew()

def mrpt_469_volatility_adjusted_stretch_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_469_volatility_adjusted_stretch_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volatility_adjusted_stretch over 21d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(21).kurt()

def mrpt_470_volatility_adjusted_stretch_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_470_volatility_adjusted_stretch_skew_63d
    ECONOMIC RATIONALE: Skewness of volatility_adjusted_stretch over 63d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(63).skew()

def mrpt_471_volatility_adjusted_stretch_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_471_volatility_adjusted_stretch_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volatility_adjusted_stretch over 63d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(63).kurt()

def mrpt_472_volatility_adjusted_stretch_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_472_volatility_adjusted_stretch_skew_126d
    ECONOMIC RATIONALE: Skewness of volatility_adjusted_stretch over 126d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(126).skew()

def mrpt_473_volatility_adjusted_stretch_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_473_volatility_adjusted_stretch_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volatility_adjusted_stretch over 126d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(126).kurt()

def mrpt_474_volatility_adjusted_stretch_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_474_volatility_adjusted_stretch_skew_252d
    ECONOMIC RATIONALE: Skewness of volatility_adjusted_stretch over 252d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(252).skew()

def mrpt_475_volatility_adjusted_stretch_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_475_volatility_adjusted_stretch_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volatility_adjusted_stretch over 252d. Price stretch adjusted for historical volatility.
    """
    return ((close - close.rolling(63).mean()) / close.rolling(63).std()).rolling(252).kurt()

def mrpt_476_mean_reversion_score_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_476_mean_reversion_score_skew_5d
    ECONOMIC RATIONALE: Skewness of mean_reversion_score over 5d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(5).skew()

def mrpt_477_mean_reversion_score_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_477_mean_reversion_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_score over 5d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(5).kurt()

def mrpt_478_mean_reversion_score_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_478_mean_reversion_score_skew_21d
    ECONOMIC RATIONALE: Skewness of mean_reversion_score over 21d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(21).skew()

def mrpt_479_mean_reversion_score_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_479_mean_reversion_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_score over 21d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(21).kurt()

def mrpt_480_mean_reversion_score_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_480_mean_reversion_score_skew_63d
    ECONOMIC RATIONALE: Skewness of mean_reversion_score over 63d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(63).skew()

def mrpt_481_mean_reversion_score_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_481_mean_reversion_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_score over 63d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(63).kurt()

def mrpt_482_mean_reversion_score_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_482_mean_reversion_score_skew_126d
    ECONOMIC RATIONALE: Skewness of mean_reversion_score over 126d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(126).skew()

def mrpt_483_mean_reversion_score_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_483_mean_reversion_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_score over 126d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(126).kurt()

def mrpt_484_mean_reversion_score_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_484_mean_reversion_score_skew_252d
    ECONOMIC RATIONALE: Skewness of mean_reversion_score over 252d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(252).skew()

def mrpt_485_mean_reversion_score_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_485_mean_reversion_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_score over 252d. Binary signal for extreme mean reversion setups.
    """
    return (((close < close.rolling(20).mean() - 2*close.rolling(20).std()) & (close.pct_change(5) < -0.05)).astype(float)).rolling(252).kurt()

def mrpt_486_price_to_median_ratio_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_486_price_to_median_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of price_to_median_ratio over 5d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(5).skew()

def mrpt_487_price_to_median_ratio_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_487_price_to_median_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_to_median_ratio over 5d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(5).kurt()

def mrpt_488_price_to_median_ratio_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_488_price_to_median_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of price_to_median_ratio over 21d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(21).skew()

def mrpt_489_price_to_median_ratio_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_489_price_to_median_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_to_median_ratio over 21d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(21).kurt()

def mrpt_490_price_to_median_ratio_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_490_price_to_median_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of price_to_median_ratio over 63d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(63).skew()

def mrpt_491_price_to_median_ratio_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_491_price_to_median_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_to_median_ratio over 63d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(63).kurt()

def mrpt_492_price_to_median_ratio_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_492_price_to_median_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of price_to_median_ratio over 126d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(126).skew()

def mrpt_493_price_to_median_ratio_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_493_price_to_median_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_to_median_ratio over 126d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(126).kurt()

def mrpt_494_price_to_median_ratio_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_494_price_to_median_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of price_to_median_ratio over 252d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(252).skew()

def mrpt_495_price_to_median_ratio_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_495_price_to_median_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_to_median_ratio over 252d. Ratio of price to medium-term median.
    """
    return (close / close.rolling(126).median()).rolling(252).kurt()

def mrpt_496_reversion_potential_index_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_496_reversion_potential_index_skew_5d
    ECONOMIC RATIONALE: Skewness of reversion_potential_index over 5d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(5).skew()

def mrpt_497_reversion_potential_index_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_497_reversion_potential_index_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of reversion_potential_index over 5d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(5).kurt()

def mrpt_498_reversion_potential_index_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_498_reversion_potential_index_skew_21d
    ECONOMIC RATIONALE: Skewness of reversion_potential_index over 21d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(21).skew()

def mrpt_499_reversion_potential_index_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_499_reversion_potential_index_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of reversion_potential_index over 21d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(21).kurt()

def mrpt_500_reversion_potential_index_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_500_reversion_potential_index_skew_63d
    ECONOMIC RATIONALE: Skewness of reversion_potential_index over 63d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(63).skew()

def mrpt_501_reversion_potential_index_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_501_reversion_potential_index_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of reversion_potential_index over 63d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(63).kurt()

def mrpt_502_reversion_potential_index_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_502_reversion_potential_index_skew_126d
    ECONOMIC RATIONALE: Skewness of reversion_potential_index over 126d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(126).skew()

def mrpt_503_reversion_potential_index_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_503_reversion_potential_index_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of reversion_potential_index over 126d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(126).kurt()

def mrpt_504_reversion_potential_index_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_504_reversion_potential_index_skew_252d
    ECONOMIC RATIONALE: Skewness of reversion_potential_index over 252d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(252).skew()

def mrpt_505_reversion_potential_index_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_505_reversion_potential_index_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of reversion_potential_index over 252d. Potential energy for mean reversion.
    """
    return (abs(close - close.rolling(252).mean()) * close.rolling(252).std()).rolling(252).kurt()

def mrpt_506_linear_regression_slope_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_506_linear_regression_slope_skew_5d
    ECONOMIC RATIONALE: Skewness of linear_regression_slope over 5d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(5).skew()

def mrpt_507_linear_regression_slope_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_507_linear_regression_slope_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of linear_regression_slope over 5d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(5).kurt()

def mrpt_508_linear_regression_slope_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_508_linear_regression_slope_skew_21d
    ECONOMIC RATIONALE: Skewness of linear_regression_slope over 21d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(21).skew()

def mrpt_509_linear_regression_slope_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_509_linear_regression_slope_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of linear_regression_slope over 21d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(21).kurt()

def mrpt_510_linear_regression_slope_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_510_linear_regression_slope_skew_63d
    ECONOMIC RATIONALE: Skewness of linear_regression_slope over 63d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(63).skew()

def mrpt_511_linear_regression_slope_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_511_linear_regression_slope_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of linear_regression_slope over 63d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(63).kurt()

def mrpt_512_linear_regression_slope_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_512_linear_regression_slope_skew_126d
    ECONOMIC RATIONALE: Skewness of linear_regression_slope over 126d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(126).skew()

def mrpt_513_linear_regression_slope_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_513_linear_regression_slope_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of linear_regression_slope over 126d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(126).kurt()

def mrpt_514_linear_regression_slope_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_514_linear_regression_slope_skew_252d
    ECONOMIC RATIONALE: Skewness of linear_regression_slope over 252d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(252).skew()

def mrpt_515_linear_regression_slope_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_515_linear_regression_slope_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of linear_regression_slope over 252d. Slope of recent price trend.
    """
    return (close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0])).rolling(252).kurt()

def mrpt_516_standard_error_channel_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_516_standard_error_channel_skew_5d
    ECONOMIC RATIONALE: Skewness of standard_error_channel over 5d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(5).skew()

def mrpt_517_standard_error_channel_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_517_standard_error_channel_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of standard_error_channel over 5d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(5).kurt()

def mrpt_518_standard_error_channel_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_518_standard_error_channel_skew_21d
    ECONOMIC RATIONALE: Skewness of standard_error_channel over 21d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(21).skew()

def mrpt_519_standard_error_channel_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_519_standard_error_channel_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of standard_error_channel over 21d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(21).kurt()

def mrpt_520_standard_error_channel_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_520_standard_error_channel_skew_63d
    ECONOMIC RATIONALE: Skewness of standard_error_channel over 63d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(63).skew()

def mrpt_521_standard_error_channel_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_521_standard_error_channel_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of standard_error_channel over 63d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(63).kurt()

def mrpt_522_standard_error_channel_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_522_standard_error_channel_skew_126d
    ECONOMIC RATIONALE: Skewness of standard_error_channel over 126d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(126).skew()

def mrpt_523_standard_error_channel_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_523_standard_error_channel_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of standard_error_channel over 126d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(126).kurt()

def mrpt_524_standard_error_channel_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_524_standard_error_channel_skew_252d
    ECONOMIC RATIONALE: Skewness of standard_error_channel over 252d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(252).skew()

def mrpt_525_standard_error_channel_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_525_standard_error_channel_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of standard_error_channel over 252d. Residuals from linear regression trend.
    """
    return ((close - close.rolling(21).apply(lambda x: np.polyfit(np.arange(len(x)), x, 1)[0]*len(x) + np.polyfit(np.arange(len(x)), x, 1)[1]))).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V104_REGISTRY_MOMENTS = {
    "mrpt_376_bollinger_pct_b_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_376_bollinger_pct_b_skew_5d},
    "mrpt_377_bollinger_pct_b_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_377_bollinger_pct_b_kurt_5d},
    "mrpt_378_bollinger_pct_b_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_378_bollinger_pct_b_skew_21d},
    "mrpt_379_bollinger_pct_b_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_379_bollinger_pct_b_kurt_21d},
    "mrpt_380_bollinger_pct_b_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_380_bollinger_pct_b_skew_63d},
    "mrpt_381_bollinger_pct_b_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_381_bollinger_pct_b_kurt_63d},
    "mrpt_382_bollinger_pct_b_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_382_bollinger_pct_b_skew_126d},
    "mrpt_383_bollinger_pct_b_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_383_bollinger_pct_b_kurt_126d},
    "mrpt_384_bollinger_pct_b_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_384_bollinger_pct_b_skew_252d},
    "mrpt_385_bollinger_pct_b_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_385_bollinger_pct_b_kurt_252d},
    "mrpt_386_distance_from_ma200_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_386_distance_from_ma200_skew_5d},
    "mrpt_387_distance_from_ma200_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_387_distance_from_ma200_kurt_5d},
    "mrpt_388_distance_from_ma200_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_388_distance_from_ma200_skew_21d},
    "mrpt_389_distance_from_ma200_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_389_distance_from_ma200_kurt_21d},
    "mrpt_390_distance_from_ma200_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_390_distance_from_ma200_skew_63d},
    "mrpt_391_distance_from_ma200_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_391_distance_from_ma200_kurt_63d},
    "mrpt_392_distance_from_ma200_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_392_distance_from_ma200_skew_126d},
    "mrpt_393_distance_from_ma200_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_393_distance_from_ma200_kurt_126d},
    "mrpt_394_distance_from_ma200_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_394_distance_from_ma200_skew_252d},
    "mrpt_395_distance_from_ma200_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_395_distance_from_ma200_kurt_252d},
    "mrpt_396_keltner_channel_lower_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_396_keltner_channel_lower_skew_5d},
    "mrpt_397_keltner_channel_lower_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_397_keltner_channel_lower_kurt_5d},
    "mrpt_398_keltner_channel_lower_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_398_keltner_channel_lower_skew_21d},
    "mrpt_399_keltner_channel_lower_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_399_keltner_channel_lower_kurt_21d},
    "mrpt_400_keltner_channel_lower_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_400_keltner_channel_lower_skew_63d},
    "mrpt_401_keltner_channel_lower_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_401_keltner_channel_lower_kurt_63d},
    "mrpt_402_keltner_channel_lower_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_402_keltner_channel_lower_skew_126d},
    "mrpt_403_keltner_channel_lower_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_403_keltner_channel_lower_kurt_126d},
    "mrpt_404_keltner_channel_lower_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_404_keltner_channel_lower_skew_252d},
    "mrpt_405_keltner_channel_lower_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_405_keltner_channel_lower_kurt_252d},
    "mrpt_406_mean_reversion_z_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_406_mean_reversion_z_skew_5d},
    "mrpt_407_mean_reversion_z_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_407_mean_reversion_z_kurt_5d},
    "mrpt_408_mean_reversion_z_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_408_mean_reversion_z_skew_21d},
    "mrpt_409_mean_reversion_z_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_409_mean_reversion_z_kurt_21d},
    "mrpt_410_mean_reversion_z_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_410_mean_reversion_z_skew_63d},
    "mrpt_411_mean_reversion_z_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_411_mean_reversion_z_kurt_63d},
    "mrpt_412_mean_reversion_z_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_412_mean_reversion_z_skew_126d},
    "mrpt_413_mean_reversion_z_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_413_mean_reversion_z_kurt_126d},
    "mrpt_414_mean_reversion_z_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_414_mean_reversion_z_skew_252d},
    "mrpt_415_mean_reversion_z_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_415_mean_reversion_z_kurt_252d},
    "mrpt_416_extreme_stretch_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_416_extreme_stretch_skew_5d},
    "mrpt_417_extreme_stretch_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_417_extreme_stretch_kurt_5d},
    "mrpt_418_extreme_stretch_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_418_extreme_stretch_skew_21d},
    "mrpt_419_extreme_stretch_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_419_extreme_stretch_kurt_21d},
    "mrpt_420_extreme_stretch_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_420_extreme_stretch_skew_63d},
    "mrpt_421_extreme_stretch_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_421_extreme_stretch_kurt_63d},
    "mrpt_422_extreme_stretch_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_422_extreme_stretch_skew_126d},
    "mrpt_423_extreme_stretch_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_423_extreme_stretch_kurt_126d},
    "mrpt_424_extreme_stretch_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_424_extreme_stretch_skew_252d},
    "mrpt_425_extreme_stretch_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_425_extreme_stretch_kurt_252d},
    "mrpt_426_reversion_velocity_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_426_reversion_velocity_skew_5d},
    "mrpt_427_reversion_velocity_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_427_reversion_velocity_kurt_5d},
    "mrpt_428_reversion_velocity_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_428_reversion_velocity_skew_21d},
    "mrpt_429_reversion_velocity_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_429_reversion_velocity_kurt_21d},
    "mrpt_430_reversion_velocity_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_430_reversion_velocity_skew_63d},
    "mrpt_431_reversion_velocity_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_431_reversion_velocity_kurt_63d},
    "mrpt_432_reversion_velocity_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_432_reversion_velocity_skew_126d},
    "mrpt_433_reversion_velocity_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_433_reversion_velocity_kurt_126d},
    "mrpt_434_reversion_velocity_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_434_reversion_velocity_skew_252d},
    "mrpt_435_reversion_velocity_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_435_reversion_velocity_kurt_252d},
    "mrpt_436_ma_cross_intensity_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_436_ma_cross_intensity_skew_5d},
    "mrpt_437_ma_cross_intensity_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_437_ma_cross_intensity_kurt_5d},
    "mrpt_438_ma_cross_intensity_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_438_ma_cross_intensity_skew_21d},
    "mrpt_439_ma_cross_intensity_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_439_ma_cross_intensity_kurt_21d},
    "mrpt_440_ma_cross_intensity_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_440_ma_cross_intensity_skew_63d},
    "mrpt_441_ma_cross_intensity_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_441_ma_cross_intensity_kurt_63d},
    "mrpt_442_ma_cross_intensity_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_442_ma_cross_intensity_skew_126d},
    "mrpt_443_ma_cross_intensity_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_443_ma_cross_intensity_kurt_126d},
    "mrpt_444_ma_cross_intensity_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_444_ma_cross_intensity_skew_252d},
    "mrpt_445_ma_cross_intensity_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_445_ma_cross_intensity_kurt_252d},
    "mrpt_446_overshot_magnitude_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_446_overshot_magnitude_skew_5d},
    "mrpt_447_overshot_magnitude_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_447_overshot_magnitude_kurt_5d},
    "mrpt_448_overshot_magnitude_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_448_overshot_magnitude_skew_21d},
    "mrpt_449_overshot_magnitude_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_449_overshot_magnitude_kurt_21d},
    "mrpt_450_overshot_magnitude_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_450_overshot_magnitude_skew_63d},
    "mrpt_451_overshot_magnitude_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_451_overshot_magnitude_kurt_63d},
    "mrpt_452_overshot_magnitude_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_452_overshot_magnitude_skew_126d},
    "mrpt_453_overshot_magnitude_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_453_overshot_magnitude_kurt_126d},
    "mrpt_454_overshot_magnitude_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_454_overshot_magnitude_skew_252d},
    "mrpt_455_overshot_magnitude_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_455_overshot_magnitude_kurt_252d},
    "mrpt_456_mean_reversion_rank_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_456_mean_reversion_rank_skew_5d},
    "mrpt_457_mean_reversion_rank_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_457_mean_reversion_rank_kurt_5d},
    "mrpt_458_mean_reversion_rank_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_458_mean_reversion_rank_skew_21d},
    "mrpt_459_mean_reversion_rank_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_459_mean_reversion_rank_kurt_21d},
    "mrpt_460_mean_reversion_rank_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_460_mean_reversion_rank_skew_63d},
    "mrpt_461_mean_reversion_rank_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_461_mean_reversion_rank_kurt_63d},
    "mrpt_462_mean_reversion_rank_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_462_mean_reversion_rank_skew_126d},
    "mrpt_463_mean_reversion_rank_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_463_mean_reversion_rank_kurt_126d},
    "mrpt_464_mean_reversion_rank_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_464_mean_reversion_rank_skew_252d},
    "mrpt_465_mean_reversion_rank_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_465_mean_reversion_rank_kurt_252d},
    "mrpt_466_volatility_adjusted_stretch_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_466_volatility_adjusted_stretch_skew_5d},
    "mrpt_467_volatility_adjusted_stretch_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_467_volatility_adjusted_stretch_kurt_5d},
    "mrpt_468_volatility_adjusted_stretch_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_468_volatility_adjusted_stretch_skew_21d},
    "mrpt_469_volatility_adjusted_stretch_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_469_volatility_adjusted_stretch_kurt_21d},
    "mrpt_470_volatility_adjusted_stretch_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_470_volatility_adjusted_stretch_skew_63d},
    "mrpt_471_volatility_adjusted_stretch_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_471_volatility_adjusted_stretch_kurt_63d},
    "mrpt_472_volatility_adjusted_stretch_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_472_volatility_adjusted_stretch_skew_126d},
    "mrpt_473_volatility_adjusted_stretch_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_473_volatility_adjusted_stretch_kurt_126d},
    "mrpt_474_volatility_adjusted_stretch_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_474_volatility_adjusted_stretch_skew_252d},
    "mrpt_475_volatility_adjusted_stretch_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_475_volatility_adjusted_stretch_kurt_252d},
    "mrpt_476_mean_reversion_score_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_476_mean_reversion_score_skew_5d},
    "mrpt_477_mean_reversion_score_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_477_mean_reversion_score_kurt_5d},
    "mrpt_478_mean_reversion_score_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_478_mean_reversion_score_skew_21d},
    "mrpt_479_mean_reversion_score_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_479_mean_reversion_score_kurt_21d},
    "mrpt_480_mean_reversion_score_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_480_mean_reversion_score_skew_63d},
    "mrpt_481_mean_reversion_score_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_481_mean_reversion_score_kurt_63d},
    "mrpt_482_mean_reversion_score_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_482_mean_reversion_score_skew_126d},
    "mrpt_483_mean_reversion_score_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_483_mean_reversion_score_kurt_126d},
    "mrpt_484_mean_reversion_score_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_484_mean_reversion_score_skew_252d},
    "mrpt_485_mean_reversion_score_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_485_mean_reversion_score_kurt_252d},
    "mrpt_486_price_to_median_ratio_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_486_price_to_median_ratio_skew_5d},
    "mrpt_487_price_to_median_ratio_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_487_price_to_median_ratio_kurt_5d},
    "mrpt_488_price_to_median_ratio_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_488_price_to_median_ratio_skew_21d},
    "mrpt_489_price_to_median_ratio_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_489_price_to_median_ratio_kurt_21d},
    "mrpt_490_price_to_median_ratio_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_490_price_to_median_ratio_skew_63d},
    "mrpt_491_price_to_median_ratio_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_491_price_to_median_ratio_kurt_63d},
    "mrpt_492_price_to_median_ratio_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_492_price_to_median_ratio_skew_126d},
    "mrpt_493_price_to_median_ratio_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_493_price_to_median_ratio_kurt_126d},
    "mrpt_494_price_to_median_ratio_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_494_price_to_median_ratio_skew_252d},
    "mrpt_495_price_to_median_ratio_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_495_price_to_median_ratio_kurt_252d},
    "mrpt_496_reversion_potential_index_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_496_reversion_potential_index_skew_5d},
    "mrpt_497_reversion_potential_index_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_497_reversion_potential_index_kurt_5d},
    "mrpt_498_reversion_potential_index_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_498_reversion_potential_index_skew_21d},
    "mrpt_499_reversion_potential_index_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_499_reversion_potential_index_kurt_21d},
    "mrpt_500_reversion_potential_index_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_500_reversion_potential_index_skew_63d},
    "mrpt_501_reversion_potential_index_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_501_reversion_potential_index_kurt_63d},
    "mrpt_502_reversion_potential_index_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_502_reversion_potential_index_skew_126d},
    "mrpt_503_reversion_potential_index_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_503_reversion_potential_index_kurt_126d},
    "mrpt_504_reversion_potential_index_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_504_reversion_potential_index_skew_252d},
    "mrpt_505_reversion_potential_index_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_505_reversion_potential_index_kurt_252d},
    "mrpt_506_linear_regression_slope_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_506_linear_regression_slope_skew_5d},
    "mrpt_507_linear_regression_slope_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_507_linear_regression_slope_kurt_5d},
    "mrpt_508_linear_regression_slope_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_508_linear_regression_slope_skew_21d},
    "mrpt_509_linear_regression_slope_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_509_linear_regression_slope_kurt_21d},
    "mrpt_510_linear_regression_slope_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_510_linear_regression_slope_skew_63d},
    "mrpt_511_linear_regression_slope_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_511_linear_regression_slope_kurt_63d},
    "mrpt_512_linear_regression_slope_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_512_linear_regression_slope_skew_126d},
    "mrpt_513_linear_regression_slope_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_513_linear_regression_slope_kurt_126d},
    "mrpt_514_linear_regression_slope_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_514_linear_regression_slope_skew_252d},
    "mrpt_515_linear_regression_slope_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_515_linear_regression_slope_kurt_252d},
    "mrpt_516_standard_error_channel_skew_5d": {"inputs": ["close", "high", "low"], "func": mrpt_516_standard_error_channel_skew_5d},
    "mrpt_517_standard_error_channel_kurt_5d": {"inputs": ["close", "high", "low"], "func": mrpt_517_standard_error_channel_kurt_5d},
    "mrpt_518_standard_error_channel_skew_21d": {"inputs": ["close", "high", "low"], "func": mrpt_518_standard_error_channel_skew_21d},
    "mrpt_519_standard_error_channel_kurt_21d": {"inputs": ["close", "high", "low"], "func": mrpt_519_standard_error_channel_kurt_21d},
    "mrpt_520_standard_error_channel_skew_63d": {"inputs": ["close", "high", "low"], "func": mrpt_520_standard_error_channel_skew_63d},
    "mrpt_521_standard_error_channel_kurt_63d": {"inputs": ["close", "high", "low"], "func": mrpt_521_standard_error_channel_kurt_63d},
    "mrpt_522_standard_error_channel_skew_126d": {"inputs": ["close", "high", "low"], "func": mrpt_522_standard_error_channel_skew_126d},
    "mrpt_523_standard_error_channel_kurt_126d": {"inputs": ["close", "high", "low"], "func": mrpt_523_standard_error_channel_kurt_126d},
    "mrpt_524_standard_error_channel_skew_252d": {"inputs": ["close", "high", "low"], "func": mrpt_524_standard_error_channel_skew_252d},
    "mrpt_525_standard_error_channel_kurt_252d": {"inputs": ["close", "high", "low"], "func": mrpt_525_standard_error_channel_kurt_252d},
}
