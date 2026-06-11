"""
111_jump_discontinuity — Statistical Moments
Domain: jump_discontinuity
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

def jump_376_price_jump_magnitude_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_376_price_jump_magnitude_skew_5d
    ECONOMIC RATIONALE: Skewness of price_jump_magnitude over 5d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(5).skew()

def jump_377_price_jump_magnitude_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_377_price_jump_magnitude_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_jump_magnitude over 5d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(5).kurt()

def jump_378_price_jump_magnitude_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_378_price_jump_magnitude_skew_21d
    ECONOMIC RATIONALE: Skewness of price_jump_magnitude over 21d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(21).skew()

def jump_379_price_jump_magnitude_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_379_price_jump_magnitude_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_jump_magnitude over 21d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(21).kurt()

def jump_380_price_jump_magnitude_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_380_price_jump_magnitude_skew_63d
    ECONOMIC RATIONALE: Skewness of price_jump_magnitude over 63d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(63).skew()

def jump_381_price_jump_magnitude_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_381_price_jump_magnitude_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_jump_magnitude over 63d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(63).kurt()

def jump_382_price_jump_magnitude_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_382_price_jump_magnitude_skew_126d
    ECONOMIC RATIONALE: Skewness of price_jump_magnitude over 126d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(126).skew()

def jump_383_price_jump_magnitude_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_383_price_jump_magnitude_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_jump_magnitude over 126d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(126).kurt()

def jump_384_price_jump_magnitude_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_384_price_jump_magnitude_skew_252d
    ECONOMIC RATIONALE: Skewness of price_jump_magnitude over 252d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(252).skew()

def jump_385_price_jump_magnitude_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_385_price_jump_magnitude_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_jump_magnitude over 252d. Size of daily price jumps relative to volatility.
    """
    return (close.diff(1).abs() / close.rolling(21).std()).rolling(252).kurt()

def jump_386_overnight_gap_jump_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_386_overnight_gap_jump_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_gap_jump over 5d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(5).skew()

def jump_387_overnight_gap_jump_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_387_overnight_gap_jump_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_jump over 5d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(5).kurt()

def jump_388_overnight_gap_jump_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_388_overnight_gap_jump_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_gap_jump over 21d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(21).skew()

def jump_389_overnight_gap_jump_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_389_overnight_gap_jump_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_jump over 21d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(21).kurt()

def jump_390_overnight_gap_jump_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_390_overnight_gap_jump_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_gap_jump over 63d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(63).skew()

def jump_391_overnight_gap_jump_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_391_overnight_gap_jump_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_jump over 63d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(63).kurt()

def jump_392_overnight_gap_jump_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_392_overnight_gap_jump_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_gap_jump over 126d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(126).skew()

def jump_393_overnight_gap_jump_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_393_overnight_gap_jump_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_jump over 126d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(126).kurt()

def jump_394_overnight_gap_jump_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_394_overnight_gap_jump_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_gap_jump over 252d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(252).skew()

def jump_395_overnight_gap_jump_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_395_overnight_gap_jump_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_jump over 252d. Magnitude of overnight gaps.
    """
    return ((open - close.shift(1)).abs() / close.rolling(21).std()).rolling(252).kurt()

def jump_396_jump_volume_intensity_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_396_jump_volume_intensity_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_volume_intensity over 5d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(5).skew()

def jump_397_jump_volume_intensity_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_397_jump_volume_intensity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_volume_intensity over 5d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(5).kurt()

def jump_398_jump_volume_intensity_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_398_jump_volume_intensity_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_volume_intensity over 21d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(21).skew()

def jump_399_jump_volume_intensity_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_399_jump_volume_intensity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_volume_intensity over 21d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(21).kurt()

def jump_400_jump_volume_intensity_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_400_jump_volume_intensity_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_volume_intensity over 63d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(63).skew()

def jump_401_jump_volume_intensity_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_401_jump_volume_intensity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_volume_intensity over 63d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(63).kurt()

def jump_402_jump_volume_intensity_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_402_jump_volume_intensity_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_volume_intensity over 126d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(126).skew()

def jump_403_jump_volume_intensity_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_403_jump_volume_intensity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_volume_intensity over 126d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(126).kurt()

def jump_404_jump_volume_intensity_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_404_jump_volume_intensity_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_volume_intensity over 252d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(252).skew()

def jump_405_jump_volume_intensity_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_405_jump_volume_intensity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_volume_intensity over 252d. Volume-weighted jump magnitude.
    """
    return (volume * close.diff(1).abs()).rolling(252).kurt()

def jump_406_jump_frequency_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_406_jump_frequency_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_frequency over 5d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(5).skew()

def jump_407_jump_frequency_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_407_jump_frequency_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_frequency over 5d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(5).kurt()

def jump_408_jump_frequency_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_408_jump_frequency_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_frequency over 21d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(21).skew()

def jump_409_jump_frequency_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_409_jump_frequency_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_frequency over 21d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(21).kurt()

def jump_410_jump_frequency_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_410_jump_frequency_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_frequency over 63d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(63).skew()

def jump_411_jump_frequency_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_411_jump_frequency_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_frequency over 63d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(63).kurt()

def jump_412_jump_frequency_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_412_jump_frequency_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_frequency over 126d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(126).skew()

def jump_413_jump_frequency_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_413_jump_frequency_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_frequency over 126d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(126).kurt()

def jump_414_jump_frequency_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_414_jump_frequency_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_frequency over 252d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(252).skew()

def jump_415_jump_frequency_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_415_jump_frequency_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_frequency over 252d. Frequency of significant price discontinuities.
    """
    return ((close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()).rolling(252).kurt()

def jump_416_jump_direction_bias_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_416_jump_direction_bias_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_direction_bias over 5d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(5).skew()

def jump_417_jump_direction_bias_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_417_jump_direction_bias_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_direction_bias over 5d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(5).kurt()

def jump_418_jump_direction_bias_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_418_jump_direction_bias_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_direction_bias over 21d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(21).skew()

def jump_419_jump_direction_bias_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_419_jump_direction_bias_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_direction_bias over 21d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(21).kurt()

def jump_420_jump_direction_bias_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_420_jump_direction_bias_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_direction_bias over 63d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(63).skew()

def jump_421_jump_direction_bias_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_421_jump_direction_bias_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_direction_bias over 63d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(63).kurt()

def jump_422_jump_direction_bias_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_422_jump_direction_bias_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_direction_bias over 126d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(126).skew()

def jump_423_jump_direction_bias_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_423_jump_direction_bias_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_direction_bias over 126d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(126).kurt()

def jump_424_jump_direction_bias_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_424_jump_direction_bias_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_direction_bias over 252d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(252).skew()

def jump_425_jump_direction_bias_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_425_jump_direction_bias_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_direction_bias over 252d. Predominance of jumps in one direction.
    """
    return (close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)).rolling(252).kurt()

def jump_426_jump_zscore_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_426_jump_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_zscore over 5d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(5).skew()

def jump_427_jump_zscore_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_427_jump_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_zscore over 5d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(5).kurt()

def jump_428_jump_zscore_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_428_jump_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_zscore over 21d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(21).skew()

def jump_429_jump_zscore_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_429_jump_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_zscore over 21d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(21).kurt()

def jump_430_jump_zscore_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_430_jump_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_zscore over 63d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(63).skew()

def jump_431_jump_zscore_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_431_jump_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_zscore over 63d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(63).kurt()

def jump_432_jump_zscore_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_432_jump_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_zscore over 126d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(126).skew()

def jump_433_jump_zscore_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_433_jump_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_zscore over 126d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(126).kurt()

def jump_434_jump_zscore_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_434_jump_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_zscore over 252d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(252).skew()

def jump_435_jump_zscore_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_435_jump_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_zscore over 252d. Statistical abnormality of current price jump.
    """
    return (_zscore_rolling(close.diff(1).abs(), 252)).rolling(252).kurt()

def jump_436_jump_reversal_rate_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_436_jump_reversal_rate_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_reversal_rate over 5d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(5).skew()

def jump_437_jump_reversal_rate_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_437_jump_reversal_rate_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_reversal_rate over 5d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(5).kurt()

def jump_438_jump_reversal_rate_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_438_jump_reversal_rate_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_reversal_rate over 21d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(21).skew()

def jump_439_jump_reversal_rate_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_439_jump_reversal_rate_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_reversal_rate over 21d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(21).kurt()

def jump_440_jump_reversal_rate_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_440_jump_reversal_rate_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_reversal_rate over 63d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(63).skew()

def jump_441_jump_reversal_rate_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_441_jump_reversal_rate_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_reversal_rate over 63d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(63).kurt()

def jump_442_jump_reversal_rate_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_442_jump_reversal_rate_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_reversal_rate over 126d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(126).skew()

def jump_443_jump_reversal_rate_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_443_jump_reversal_rate_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_reversal_rate over 126d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(126).kurt()

def jump_444_jump_reversal_rate_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_444_jump_reversal_rate_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_reversal_rate over 252d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(252).skew()

def jump_445_jump_reversal_rate_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_445_jump_reversal_rate_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_reversal_rate over 252d. Frequency of jump reversals.
    """
    return (close.diff(1).shift(1) * close.diff(1) < 0).rolling(252).kurt()

def jump_446_vol_adjusted_jump_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_446_vol_adjusted_jump_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_adjusted_jump over 5d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(5).skew()

def jump_447_vol_adjusted_jump_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_447_vol_adjusted_jump_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_adjusted_jump over 5d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(5).kurt()

def jump_448_vol_adjusted_jump_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_448_vol_adjusted_jump_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_adjusted_jump over 21d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(21).skew()

def jump_449_vol_adjusted_jump_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_449_vol_adjusted_jump_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_adjusted_jump over 21d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(21).kurt()

def jump_450_vol_adjusted_jump_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_450_vol_adjusted_jump_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_adjusted_jump over 63d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(63).skew()

def jump_451_vol_adjusted_jump_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_451_vol_adjusted_jump_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_adjusted_jump over 63d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(63).kurt()

def jump_452_vol_adjusted_jump_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_452_vol_adjusted_jump_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_adjusted_jump over 126d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(126).skew()

def jump_453_vol_adjusted_jump_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_453_vol_adjusted_jump_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_adjusted_jump over 126d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(126).kurt()

def jump_454_vol_adjusted_jump_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_454_vol_adjusted_jump_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_adjusted_jump over 252d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(252).skew()

def jump_455_vol_adjusted_jump_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_455_vol_adjusted_jump_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_adjusted_jump over 252d. Jump magnitude relative to volume effort.
    """
    return (close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)).rolling(252).kurt()

def jump_456_jump_decay_rate_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_456_jump_decay_rate_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_decay_rate over 5d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(5).skew()

def jump_457_jump_decay_rate_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_457_jump_decay_rate_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_decay_rate over 5d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(5).kurt()

def jump_458_jump_decay_rate_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_458_jump_decay_rate_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_decay_rate over 21d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(21).skew()

def jump_459_jump_decay_rate_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_459_jump_decay_rate_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_decay_rate over 21d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(21).kurt()

def jump_460_jump_decay_rate_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_460_jump_decay_rate_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_decay_rate over 63d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(63).skew()

def jump_461_jump_decay_rate_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_461_jump_decay_rate_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_decay_rate over 63d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(63).kurt()

def jump_462_jump_decay_rate_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_462_jump_decay_rate_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_decay_rate over 126d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(126).skew()

def jump_463_jump_decay_rate_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_463_jump_decay_rate_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_decay_rate over 126d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(126).kurt()

def jump_464_jump_decay_rate_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_464_jump_decay_rate_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_decay_rate over 252d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(252).skew()

def jump_465_jump_decay_rate_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_465_jump_decay_rate_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_decay_rate over 252d. Decay of impact from recent jumps.
    """
    return (close.diff(1).abs().ewm(span=5).mean()).rolling(252).kurt()

def jump_466_jump_clustering_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_466_jump_clustering_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_clustering over 5d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(5).skew()

def jump_467_jump_clustering_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_467_jump_clustering_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_clustering over 5d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(5).kurt()

def jump_468_jump_clustering_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_468_jump_clustering_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_clustering over 21d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(21).skew()

def jump_469_jump_clustering_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_469_jump_clustering_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_clustering over 21d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(21).kurt()

def jump_470_jump_clustering_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_470_jump_clustering_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_clustering over 63d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(63).skew()

def jump_471_jump_clustering_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_471_jump_clustering_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_clustering over 63d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(63).kurt()

def jump_472_jump_clustering_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_472_jump_clustering_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_clustering over 126d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(126).skew()

def jump_473_jump_clustering_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_473_jump_clustering_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_clustering over 126d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(126).kurt()

def jump_474_jump_clustering_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_474_jump_clustering_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_clustering over 252d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(252).skew()

def jump_475_jump_clustering_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_475_jump_clustering_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_clustering over 252d. Recent clusters of price jumps.
    """
    return ((close.diff(1).abs() > 2*close.rolling(63).std()).rolling(5).sum()).rolling(252).kurt()

def jump_476_intraday_jump_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_476_intraday_jump_skew_5d
    ECONOMIC RATIONALE: Skewness of intraday_jump over 5d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(5).skew()

def jump_477_intraday_jump_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_477_intraday_jump_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of intraday_jump over 5d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(5).kurt()

def jump_478_intraday_jump_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_478_intraday_jump_skew_21d
    ECONOMIC RATIONALE: Skewness of intraday_jump over 21d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(21).skew()

def jump_479_intraday_jump_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_479_intraday_jump_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of intraday_jump over 21d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(21).kurt()

def jump_480_intraday_jump_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_480_intraday_jump_skew_63d
    ECONOMIC RATIONALE: Skewness of intraday_jump over 63d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(63).skew()

def jump_481_intraday_jump_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_481_intraday_jump_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of intraday_jump over 63d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(63).kurt()

def jump_482_intraday_jump_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_482_intraday_jump_skew_126d
    ECONOMIC RATIONALE: Skewness of intraday_jump over 126d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(126).skew()

def jump_483_intraday_jump_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_483_intraday_jump_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of intraday_jump over 126d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(126).kurt()

def jump_484_intraday_jump_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_484_intraday_jump_skew_252d
    ECONOMIC RATIONALE: Skewness of intraday_jump over 252d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(252).skew()

def jump_485_intraday_jump_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_485_intraday_jump_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of intraday_jump over 252d. Intraday range as a proxy for jump potential.
    """
    return ((high - low) / close.rolling(21).std()).rolling(252).kurt()

def jump_486_jump_regime_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_486_jump_regime_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_regime over 5d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(5).skew()

def jump_487_jump_regime_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_487_jump_regime_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_regime over 5d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(5).kurt()

def jump_488_jump_regime_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_488_jump_regime_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_regime over 21d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(21).skew()

def jump_489_jump_regime_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_489_jump_regime_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_regime over 21d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(21).kurt()

def jump_490_jump_regime_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_490_jump_regime_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_regime over 63d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(63).skew()

def jump_491_jump_regime_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_491_jump_regime_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_regime over 63d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(63).kurt()

def jump_492_jump_regime_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_492_jump_regime_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_regime over 126d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(126).skew()

def jump_493_jump_regime_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_493_jump_regime_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_regime over 126d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(126).kurt()

def jump_494_jump_regime_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_494_jump_regime_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_regime over 252d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(252).skew()

def jump_495_jump_regime_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_495_jump_regime_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_regime over 252d. Ratio of recent to long-term jumpiness.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(252).kurt()

def jump_496_jump_impact_on_drawdown_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_496_jump_impact_on_drawdown_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_impact_on_drawdown over 5d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(5).skew()

def jump_497_jump_impact_on_drawdown_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_497_jump_impact_on_drawdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_impact_on_drawdown over 5d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(5).kurt()

def jump_498_jump_impact_on_drawdown_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_498_jump_impact_on_drawdown_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_impact_on_drawdown over 21d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(21).skew()

def jump_499_jump_impact_on_drawdown_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_499_jump_impact_on_drawdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_impact_on_drawdown over 21d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(21).kurt()

def jump_500_jump_impact_on_drawdown_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_500_jump_impact_on_drawdown_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_impact_on_drawdown over 63d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(63).skew()

def jump_501_jump_impact_on_drawdown_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_501_jump_impact_on_drawdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_impact_on_drawdown over 63d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(63).kurt()

def jump_502_jump_impact_on_drawdown_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_502_jump_impact_on_drawdown_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_impact_on_drawdown over 126d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(126).skew()

def jump_503_jump_impact_on_drawdown_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_503_jump_impact_on_drawdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_impact_on_drawdown over 126d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(126).kurt()

def jump_504_jump_impact_on_drawdown_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_504_jump_impact_on_drawdown_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_impact_on_drawdown over 252d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(252).skew()

def jump_505_jump_impact_on_drawdown_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_505_jump_impact_on_drawdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_impact_on_drawdown over 252d. Jumps occurring within established drawdowns.
    """
    return (close.diff(1) * (close < close.rolling(63).max())).rolling(252).kurt()

def jump_506_jump_entropy_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_506_jump_entropy_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_entropy over 5d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(5).skew()

def jump_507_jump_entropy_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_507_jump_entropy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_entropy over 5d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(5).kurt()

def jump_508_jump_entropy_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_508_jump_entropy_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_entropy over 21d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(21).skew()

def jump_509_jump_entropy_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_509_jump_entropy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_entropy over 21d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(21).kurt()

def jump_510_jump_entropy_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_510_jump_entropy_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_entropy over 63d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(63).skew()

def jump_511_jump_entropy_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_511_jump_entropy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_entropy over 63d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(63).kurt()

def jump_512_jump_entropy_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_512_jump_entropy_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_entropy over 126d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(126).skew()

def jump_513_jump_entropy_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_513_jump_entropy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_entropy over 126d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(126).kurt()

def jump_514_jump_entropy_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_514_jump_entropy_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_entropy over 252d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(252).skew()

def jump_515_jump_entropy_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_515_jump_entropy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_entropy over 252d. Unpredictability of price jump magnitudes.
    """
    return (close.diff(1).abs().rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(252).kurt()

def jump_516_jump_tail_risk_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_516_jump_tail_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of jump_tail_risk over 5d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(5).skew()

def jump_517_jump_tail_risk_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_517_jump_tail_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of jump_tail_risk over 5d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(5).kurt()

def jump_518_jump_tail_risk_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_518_jump_tail_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of jump_tail_risk over 21d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(21).skew()

def jump_519_jump_tail_risk_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_519_jump_tail_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of jump_tail_risk over 21d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(21).kurt()

def jump_520_jump_tail_risk_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_520_jump_tail_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of jump_tail_risk over 63d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(63).skew()

def jump_521_jump_tail_risk_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_521_jump_tail_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of jump_tail_risk over 63d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(63).kurt()

def jump_522_jump_tail_risk_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_522_jump_tail_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of jump_tail_risk over 126d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(126).skew()

def jump_523_jump_tail_risk_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_523_jump_tail_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of jump_tail_risk over 126d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(126).kurt()

def jump_524_jump_tail_risk_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_524_jump_tail_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of jump_tail_risk over 252d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(252).skew()

def jump_525_jump_tail_risk_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_525_jump_tail_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of jump_tail_risk over 252d. Binary indicator of severe negative jumps.
    """
    return ((close.diff(1) < -3*close.rolling(252).std()).astype(float)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V111_REGISTRY_MOMENTS = {
    "jump_376_price_jump_magnitude_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_376_price_jump_magnitude_skew_5d},
    "jump_377_price_jump_magnitude_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_377_price_jump_magnitude_kurt_5d},
    "jump_378_price_jump_magnitude_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_378_price_jump_magnitude_skew_21d},
    "jump_379_price_jump_magnitude_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_379_price_jump_magnitude_kurt_21d},
    "jump_380_price_jump_magnitude_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_380_price_jump_magnitude_skew_63d},
    "jump_381_price_jump_magnitude_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_381_price_jump_magnitude_kurt_63d},
    "jump_382_price_jump_magnitude_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_382_price_jump_magnitude_skew_126d},
    "jump_383_price_jump_magnitude_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_383_price_jump_magnitude_kurt_126d},
    "jump_384_price_jump_magnitude_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_384_price_jump_magnitude_skew_252d},
    "jump_385_price_jump_magnitude_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_385_price_jump_magnitude_kurt_252d},
    "jump_386_overnight_gap_jump_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_386_overnight_gap_jump_skew_5d},
    "jump_387_overnight_gap_jump_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_387_overnight_gap_jump_kurt_5d},
    "jump_388_overnight_gap_jump_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_388_overnight_gap_jump_skew_21d},
    "jump_389_overnight_gap_jump_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_389_overnight_gap_jump_kurt_21d},
    "jump_390_overnight_gap_jump_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_390_overnight_gap_jump_skew_63d},
    "jump_391_overnight_gap_jump_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_391_overnight_gap_jump_kurt_63d},
    "jump_392_overnight_gap_jump_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_392_overnight_gap_jump_skew_126d},
    "jump_393_overnight_gap_jump_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_393_overnight_gap_jump_kurt_126d},
    "jump_394_overnight_gap_jump_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_394_overnight_gap_jump_skew_252d},
    "jump_395_overnight_gap_jump_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_395_overnight_gap_jump_kurt_252d},
    "jump_396_jump_volume_intensity_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_396_jump_volume_intensity_skew_5d},
    "jump_397_jump_volume_intensity_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_397_jump_volume_intensity_kurt_5d},
    "jump_398_jump_volume_intensity_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_398_jump_volume_intensity_skew_21d},
    "jump_399_jump_volume_intensity_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_399_jump_volume_intensity_kurt_21d},
    "jump_400_jump_volume_intensity_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_400_jump_volume_intensity_skew_63d},
    "jump_401_jump_volume_intensity_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_401_jump_volume_intensity_kurt_63d},
    "jump_402_jump_volume_intensity_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_402_jump_volume_intensity_skew_126d},
    "jump_403_jump_volume_intensity_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_403_jump_volume_intensity_kurt_126d},
    "jump_404_jump_volume_intensity_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_404_jump_volume_intensity_skew_252d},
    "jump_405_jump_volume_intensity_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_405_jump_volume_intensity_kurt_252d},
    "jump_406_jump_frequency_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_406_jump_frequency_skew_5d},
    "jump_407_jump_frequency_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_407_jump_frequency_kurt_5d},
    "jump_408_jump_frequency_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_408_jump_frequency_skew_21d},
    "jump_409_jump_frequency_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_409_jump_frequency_kurt_21d},
    "jump_410_jump_frequency_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_410_jump_frequency_skew_63d},
    "jump_411_jump_frequency_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_411_jump_frequency_kurt_63d},
    "jump_412_jump_frequency_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_412_jump_frequency_skew_126d},
    "jump_413_jump_frequency_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_413_jump_frequency_kurt_126d},
    "jump_414_jump_frequency_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_414_jump_frequency_skew_252d},
    "jump_415_jump_frequency_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_415_jump_frequency_kurt_252d},
    "jump_416_jump_direction_bias_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_416_jump_direction_bias_skew_5d},
    "jump_417_jump_direction_bias_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_417_jump_direction_bias_kurt_5d},
    "jump_418_jump_direction_bias_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_418_jump_direction_bias_skew_21d},
    "jump_419_jump_direction_bias_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_419_jump_direction_bias_kurt_21d},
    "jump_420_jump_direction_bias_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_420_jump_direction_bias_skew_63d},
    "jump_421_jump_direction_bias_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_421_jump_direction_bias_kurt_63d},
    "jump_422_jump_direction_bias_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_422_jump_direction_bias_skew_126d},
    "jump_423_jump_direction_bias_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_423_jump_direction_bias_kurt_126d},
    "jump_424_jump_direction_bias_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_424_jump_direction_bias_skew_252d},
    "jump_425_jump_direction_bias_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_425_jump_direction_bias_kurt_252d},
    "jump_426_jump_zscore_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_426_jump_zscore_skew_5d},
    "jump_427_jump_zscore_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_427_jump_zscore_kurt_5d},
    "jump_428_jump_zscore_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_428_jump_zscore_skew_21d},
    "jump_429_jump_zscore_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_429_jump_zscore_kurt_21d},
    "jump_430_jump_zscore_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_430_jump_zscore_skew_63d},
    "jump_431_jump_zscore_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_431_jump_zscore_kurt_63d},
    "jump_432_jump_zscore_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_432_jump_zscore_skew_126d},
    "jump_433_jump_zscore_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_433_jump_zscore_kurt_126d},
    "jump_434_jump_zscore_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_434_jump_zscore_skew_252d},
    "jump_435_jump_zscore_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_435_jump_zscore_kurt_252d},
    "jump_436_jump_reversal_rate_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_436_jump_reversal_rate_skew_5d},
    "jump_437_jump_reversal_rate_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_437_jump_reversal_rate_kurt_5d},
    "jump_438_jump_reversal_rate_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_438_jump_reversal_rate_skew_21d},
    "jump_439_jump_reversal_rate_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_439_jump_reversal_rate_kurt_21d},
    "jump_440_jump_reversal_rate_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_440_jump_reversal_rate_skew_63d},
    "jump_441_jump_reversal_rate_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_441_jump_reversal_rate_kurt_63d},
    "jump_442_jump_reversal_rate_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_442_jump_reversal_rate_skew_126d},
    "jump_443_jump_reversal_rate_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_443_jump_reversal_rate_kurt_126d},
    "jump_444_jump_reversal_rate_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_444_jump_reversal_rate_skew_252d},
    "jump_445_jump_reversal_rate_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_445_jump_reversal_rate_kurt_252d},
    "jump_446_vol_adjusted_jump_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_446_vol_adjusted_jump_skew_5d},
    "jump_447_vol_adjusted_jump_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_447_vol_adjusted_jump_kurt_5d},
    "jump_448_vol_adjusted_jump_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_448_vol_adjusted_jump_skew_21d},
    "jump_449_vol_adjusted_jump_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_449_vol_adjusted_jump_kurt_21d},
    "jump_450_vol_adjusted_jump_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_450_vol_adjusted_jump_skew_63d},
    "jump_451_vol_adjusted_jump_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_451_vol_adjusted_jump_kurt_63d},
    "jump_452_vol_adjusted_jump_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_452_vol_adjusted_jump_skew_126d},
    "jump_453_vol_adjusted_jump_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_453_vol_adjusted_jump_kurt_126d},
    "jump_454_vol_adjusted_jump_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_454_vol_adjusted_jump_skew_252d},
    "jump_455_vol_adjusted_jump_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_455_vol_adjusted_jump_kurt_252d},
    "jump_456_jump_decay_rate_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_456_jump_decay_rate_skew_5d},
    "jump_457_jump_decay_rate_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_457_jump_decay_rate_kurt_5d},
    "jump_458_jump_decay_rate_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_458_jump_decay_rate_skew_21d},
    "jump_459_jump_decay_rate_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_459_jump_decay_rate_kurt_21d},
    "jump_460_jump_decay_rate_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_460_jump_decay_rate_skew_63d},
    "jump_461_jump_decay_rate_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_461_jump_decay_rate_kurt_63d},
    "jump_462_jump_decay_rate_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_462_jump_decay_rate_skew_126d},
    "jump_463_jump_decay_rate_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_463_jump_decay_rate_kurt_126d},
    "jump_464_jump_decay_rate_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_464_jump_decay_rate_skew_252d},
    "jump_465_jump_decay_rate_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_465_jump_decay_rate_kurt_252d},
    "jump_466_jump_clustering_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_466_jump_clustering_skew_5d},
    "jump_467_jump_clustering_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_467_jump_clustering_kurt_5d},
    "jump_468_jump_clustering_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_468_jump_clustering_skew_21d},
    "jump_469_jump_clustering_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_469_jump_clustering_kurt_21d},
    "jump_470_jump_clustering_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_470_jump_clustering_skew_63d},
    "jump_471_jump_clustering_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_471_jump_clustering_kurt_63d},
    "jump_472_jump_clustering_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_472_jump_clustering_skew_126d},
    "jump_473_jump_clustering_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_473_jump_clustering_kurt_126d},
    "jump_474_jump_clustering_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_474_jump_clustering_skew_252d},
    "jump_475_jump_clustering_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_475_jump_clustering_kurt_252d},
    "jump_476_intraday_jump_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_476_intraday_jump_skew_5d},
    "jump_477_intraday_jump_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_477_intraday_jump_kurt_5d},
    "jump_478_intraday_jump_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_478_intraday_jump_skew_21d},
    "jump_479_intraday_jump_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_479_intraday_jump_kurt_21d},
    "jump_480_intraday_jump_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_480_intraday_jump_skew_63d},
    "jump_481_intraday_jump_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_481_intraday_jump_kurt_63d},
    "jump_482_intraday_jump_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_482_intraday_jump_skew_126d},
    "jump_483_intraday_jump_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_483_intraday_jump_kurt_126d},
    "jump_484_intraday_jump_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_484_intraday_jump_skew_252d},
    "jump_485_intraday_jump_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_485_intraday_jump_kurt_252d},
    "jump_486_jump_regime_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_486_jump_regime_skew_5d},
    "jump_487_jump_regime_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_487_jump_regime_kurt_5d},
    "jump_488_jump_regime_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_488_jump_regime_skew_21d},
    "jump_489_jump_regime_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_489_jump_regime_kurt_21d},
    "jump_490_jump_regime_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_490_jump_regime_skew_63d},
    "jump_491_jump_regime_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_491_jump_regime_kurt_63d},
    "jump_492_jump_regime_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_492_jump_regime_skew_126d},
    "jump_493_jump_regime_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_493_jump_regime_kurt_126d},
    "jump_494_jump_regime_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_494_jump_regime_skew_252d},
    "jump_495_jump_regime_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_495_jump_regime_kurt_252d},
    "jump_496_jump_impact_on_drawdown_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_496_jump_impact_on_drawdown_skew_5d},
    "jump_497_jump_impact_on_drawdown_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_497_jump_impact_on_drawdown_kurt_5d},
    "jump_498_jump_impact_on_drawdown_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_498_jump_impact_on_drawdown_skew_21d},
    "jump_499_jump_impact_on_drawdown_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_499_jump_impact_on_drawdown_kurt_21d},
    "jump_500_jump_impact_on_drawdown_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_500_jump_impact_on_drawdown_skew_63d},
    "jump_501_jump_impact_on_drawdown_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_501_jump_impact_on_drawdown_kurt_63d},
    "jump_502_jump_impact_on_drawdown_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_502_jump_impact_on_drawdown_skew_126d},
    "jump_503_jump_impact_on_drawdown_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_503_jump_impact_on_drawdown_kurt_126d},
    "jump_504_jump_impact_on_drawdown_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_504_jump_impact_on_drawdown_skew_252d},
    "jump_505_jump_impact_on_drawdown_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_505_jump_impact_on_drawdown_kurt_252d},
    "jump_506_jump_entropy_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_506_jump_entropy_skew_5d},
    "jump_507_jump_entropy_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_507_jump_entropy_kurt_5d},
    "jump_508_jump_entropy_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_508_jump_entropy_skew_21d},
    "jump_509_jump_entropy_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_509_jump_entropy_kurt_21d},
    "jump_510_jump_entropy_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_510_jump_entropy_skew_63d},
    "jump_511_jump_entropy_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_511_jump_entropy_kurt_63d},
    "jump_512_jump_entropy_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_512_jump_entropy_skew_126d},
    "jump_513_jump_entropy_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_513_jump_entropy_kurt_126d},
    "jump_514_jump_entropy_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_514_jump_entropy_skew_252d},
    "jump_515_jump_entropy_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_515_jump_entropy_kurt_252d},
    "jump_516_jump_tail_risk_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_516_jump_tail_risk_skew_5d},
    "jump_517_jump_tail_risk_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_517_jump_tail_risk_kurt_5d},
    "jump_518_jump_tail_risk_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_518_jump_tail_risk_skew_21d},
    "jump_519_jump_tail_risk_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_519_jump_tail_risk_kurt_21d},
    "jump_520_jump_tail_risk_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_520_jump_tail_risk_skew_63d},
    "jump_521_jump_tail_risk_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_521_jump_tail_risk_kurt_63d},
    "jump_522_jump_tail_risk_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_522_jump_tail_risk_skew_126d},
    "jump_523_jump_tail_risk_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_523_jump_tail_risk_kurt_126d},
    "jump_524_jump_tail_risk_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_524_jump_tail_risk_skew_252d},
    "jump_525_jump_tail_risk_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_525_jump_tail_risk_kurt_252d},
}
