"""
108_drawdown_history_rank — Statistical Moments
Domain: drawdown_history_rank
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

def dhrk_376_current_drawdown_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_376_current_drawdown_skew_5d
    ECONOMIC RATIONALE: Skewness of current_drawdown over 5d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(5).skew()

def dhrk_377_current_drawdown_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_377_current_drawdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of current_drawdown over 5d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(5).kurt()

def dhrk_378_current_drawdown_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_378_current_drawdown_skew_21d
    ECONOMIC RATIONALE: Skewness of current_drawdown over 21d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(21).skew()

def dhrk_379_current_drawdown_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_379_current_drawdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of current_drawdown over 21d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(21).kurt()

def dhrk_380_current_drawdown_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_380_current_drawdown_skew_63d
    ECONOMIC RATIONALE: Skewness of current_drawdown over 63d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(63).skew()

def dhrk_381_current_drawdown_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_381_current_drawdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of current_drawdown over 63d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(63).kurt()

def dhrk_382_current_drawdown_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_382_current_drawdown_skew_126d
    ECONOMIC RATIONALE: Skewness of current_drawdown over 126d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(126).skew()

def dhrk_383_current_drawdown_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_383_current_drawdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of current_drawdown over 126d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(126).kurt()

def dhrk_384_current_drawdown_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_384_current_drawdown_skew_252d
    ECONOMIC RATIONALE: Skewness of current_drawdown over 252d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(252).skew()

def dhrk_385_current_drawdown_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_385_current_drawdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of current_drawdown over 252d. Drawdown from the 52-week high.
    """
    return (close / close.rolling(252).max() - 1).rolling(252).kurt()

def dhrk_386_drawdown_rank_252d_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_386_drawdown_rank_252d_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_rank_252d over 5d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(5).skew()

def dhrk_387_drawdown_rank_252d_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_387_drawdown_rank_252d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_rank_252d over 5d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(5).kurt()

def dhrk_388_drawdown_rank_252d_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_388_drawdown_rank_252d_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_rank_252d over 21d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(21).skew()

def dhrk_389_drawdown_rank_252d_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_389_drawdown_rank_252d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_rank_252d over 21d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(21).kurt()

def dhrk_390_drawdown_rank_252d_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_390_drawdown_rank_252d_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_rank_252d over 63d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(63).skew()

def dhrk_391_drawdown_rank_252d_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_391_drawdown_rank_252d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_rank_252d over 63d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(63).kurt()

def dhrk_392_drawdown_rank_252d_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_392_drawdown_rank_252d_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_rank_252d over 126d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(126).skew()

def dhrk_393_drawdown_rank_252d_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_393_drawdown_rank_252d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_rank_252d over 126d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(126).kurt()

def dhrk_394_drawdown_rank_252d_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_394_drawdown_rank_252d_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_rank_252d over 252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(252).skew()

def dhrk_395_drawdown_rank_252d_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_395_drawdown_rank_252d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_rank_252d over 252d. Historical rank of the current drawdown level.
    """
    return (_rank_pct(close / close.rolling(252).max() - 1, 252)).rolling(252).kurt()

def dhrk_396_drawdown_severity_z_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_396_drawdown_severity_z_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_z over 5d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(5).skew()

def dhrk_397_drawdown_severity_z_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_397_drawdown_severity_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_z over 5d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(5).kurt()

def dhrk_398_drawdown_severity_z_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_398_drawdown_severity_z_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_z over 21d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(21).skew()

def dhrk_399_drawdown_severity_z_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_399_drawdown_severity_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_z over 21d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(21).kurt()

def dhrk_400_drawdown_severity_z_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_400_drawdown_severity_z_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_z over 63d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(63).skew()

def dhrk_401_drawdown_severity_z_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_401_drawdown_severity_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_z over 63d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(63).kurt()

def dhrk_402_drawdown_severity_z_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_402_drawdown_severity_z_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_z over 126d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(126).skew()

def dhrk_403_drawdown_severity_z_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_403_drawdown_severity_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_z over 126d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(126).kurt()

def dhrk_404_drawdown_severity_z_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_404_drawdown_severity_z_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_z over 252d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(252).skew()

def dhrk_405_drawdown_severity_z_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_405_drawdown_severity_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_z over 252d. Z-score of current drawdown vs historical drawdowns.
    """
    return (_zscore_rolling(close / close.rolling(252).max() - 1, 252)).rolling(252).kurt()

def dhrk_406_drawdown_duration_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_406_drawdown_duration_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_duration over 5d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(5).skew()

def dhrk_407_drawdown_duration_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_407_drawdown_duration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_duration over 5d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(5).kurt()

def dhrk_408_drawdown_duration_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_408_drawdown_duration_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_duration over 21d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(21).skew()

def dhrk_409_drawdown_duration_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_409_drawdown_duration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_duration over 21d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(21).kurt()

def dhrk_410_drawdown_duration_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_410_drawdown_duration_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_duration over 63d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(63).skew()

def dhrk_411_drawdown_duration_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_411_drawdown_duration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_duration over 63d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(63).kurt()

def dhrk_412_drawdown_duration_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_412_drawdown_duration_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_duration over 126d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(126).skew()

def dhrk_413_drawdown_duration_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_413_drawdown_duration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_duration over 126d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(126).kurt()

def dhrk_414_drawdown_duration_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_414_drawdown_duration_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_duration over 252d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(252).skew()

def dhrk_415_drawdown_duration_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_415_drawdown_duration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_duration over 252d. Number of days since the last 52-week high.
    """
    return ((close < close.rolling(252).max()).rolling(252).sum()).rolling(252).kurt()

def dhrk_416_peak_to_trough_momentum_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_416_peak_to_trough_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of peak_to_trough_momentum over 5d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(5).skew()

def dhrk_417_peak_to_trough_momentum_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_417_peak_to_trough_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of peak_to_trough_momentum over 5d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(5).kurt()

def dhrk_418_peak_to_trough_momentum_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_418_peak_to_trough_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of peak_to_trough_momentum over 21d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(21).skew()

def dhrk_419_peak_to_trough_momentum_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_419_peak_to_trough_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of peak_to_trough_momentum over 21d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(21).kurt()

def dhrk_420_peak_to_trough_momentum_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_420_peak_to_trough_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of peak_to_trough_momentum over 63d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(63).skew()

def dhrk_421_peak_to_trough_momentum_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_421_peak_to_trough_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of peak_to_trough_momentum over 63d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(63).kurt()

def dhrk_422_peak_to_trough_momentum_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_422_peak_to_trough_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of peak_to_trough_momentum over 126d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(126).skew()

def dhrk_423_peak_to_trough_momentum_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_423_peak_to_trough_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of peak_to_trough_momentum over 126d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(126).kurt()

def dhrk_424_peak_to_trough_momentum_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_424_peak_to_trough_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of peak_to_trough_momentum over 252d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(252).skew()

def dhrk_425_peak_to_trough_momentum_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_425_peak_to_trough_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of peak_to_trough_momentum over 252d. Average rate of wealth destruction from peak.
    """
    return ((close.rolling(252).max() - close) / 252).rolling(252).kurt()

def dhrk_426_drawdown_acceleration_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_426_drawdown_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_acceleration over 5d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(5).skew()

def dhrk_427_drawdown_acceleration_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_427_drawdown_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_acceleration over 5d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(5).kurt()

def dhrk_428_drawdown_acceleration_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_428_drawdown_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_acceleration over 21d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(21).skew()

def dhrk_429_drawdown_acceleration_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_429_drawdown_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_acceleration over 21d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(21).kurt()

def dhrk_430_drawdown_acceleration_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_430_drawdown_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_acceleration over 63d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(63).skew()

def dhrk_431_drawdown_acceleration_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_431_drawdown_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_acceleration over 63d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(63).kurt()

def dhrk_432_drawdown_acceleration_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_432_drawdown_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_acceleration over 126d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(126).skew()

def dhrk_433_drawdown_acceleration_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_433_drawdown_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_acceleration over 126d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(126).kurt()

def dhrk_434_drawdown_acceleration_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_434_drawdown_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_acceleration over 252d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(252).skew()

def dhrk_435_drawdown_acceleration_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_435_drawdown_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_acceleration over 252d. Speed at which the drawdown is deepening.
    """
    return ((close / close.rolling(252).max() - 1).diff(21)).rolling(252).kurt()

def dhrk_436_drawdown_vol_ratio_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_436_drawdown_vol_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_vol_ratio over 5d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(5).skew()

def dhrk_437_drawdown_vol_ratio_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_437_drawdown_vol_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_vol_ratio over 5d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(5).kurt()

def dhrk_438_drawdown_vol_ratio_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_438_drawdown_vol_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_vol_ratio over 21d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(21).skew()

def dhrk_439_drawdown_vol_ratio_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_439_drawdown_vol_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_vol_ratio over 21d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(21).kurt()

def dhrk_440_drawdown_vol_ratio_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_440_drawdown_vol_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_vol_ratio over 63d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(63).skew()

def dhrk_441_drawdown_vol_ratio_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_441_drawdown_vol_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_vol_ratio over 63d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(63).kurt()

def dhrk_442_drawdown_vol_ratio_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_442_drawdown_vol_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_vol_ratio over 126d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(126).skew()

def dhrk_443_drawdown_vol_ratio_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_443_drawdown_vol_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_vol_ratio over 126d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(126).kurt()

def dhrk_444_drawdown_vol_ratio_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_444_drawdown_vol_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_vol_ratio over 252d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(252).skew()

def dhrk_445_drawdown_vol_ratio_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_445_drawdown_vol_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_vol_ratio over 252d. Drawdown depth normalized by volatility.
    """
    return ((close / close.rolling(252).max() - 1) / close.rolling(252).std()).rolling(252).kurt()

def dhrk_446_recovery_from_lows_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_446_recovery_from_lows_skew_5d
    ECONOMIC RATIONALE: Skewness of recovery_from_lows over 5d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(5).skew()

def dhrk_447_recovery_from_lows_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_447_recovery_from_lows_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of recovery_from_lows over 5d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(5).kurt()

def dhrk_448_recovery_from_lows_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_448_recovery_from_lows_skew_21d
    ECONOMIC RATIONALE: Skewness of recovery_from_lows over 21d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(21).skew()

def dhrk_449_recovery_from_lows_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_449_recovery_from_lows_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of recovery_from_lows over 21d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(21).kurt()

def dhrk_450_recovery_from_lows_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_450_recovery_from_lows_skew_63d
    ECONOMIC RATIONALE: Skewness of recovery_from_lows over 63d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(63).skew()

def dhrk_451_recovery_from_lows_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_451_recovery_from_lows_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of recovery_from_lows over 63d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(63).kurt()

def dhrk_452_recovery_from_lows_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_452_recovery_from_lows_skew_126d
    ECONOMIC RATIONALE: Skewness of recovery_from_lows over 126d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(126).skew()

def dhrk_453_recovery_from_lows_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_453_recovery_from_lows_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of recovery_from_lows over 126d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(126).kurt()

def dhrk_454_recovery_from_lows_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_454_recovery_from_lows_skew_252d
    ECONOMIC RATIONALE: Skewness of recovery_from_lows over 252d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(252).skew()

def dhrk_455_recovery_from_lows_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_455_recovery_from_lows_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of recovery_from_lows over 252d. Percentage rally from the 52-week low.
    """
    return (close / close.rolling(252).min() - 1).rolling(252).kurt()

def dhrk_456_drawdown_persistence_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_456_drawdown_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_persistence over 5d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(5).skew()

def dhrk_457_drawdown_persistence_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_457_drawdown_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_persistence over 5d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(5).kurt()

def dhrk_458_drawdown_persistence_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_458_drawdown_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_persistence over 21d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(21).skew()

def dhrk_459_drawdown_persistence_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_459_drawdown_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_persistence over 21d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(21).kurt()

def dhrk_460_drawdown_persistence_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_460_drawdown_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_persistence over 63d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(63).skew()

def dhrk_461_drawdown_persistence_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_461_drawdown_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_persistence over 63d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(63).kurt()

def dhrk_462_drawdown_persistence_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_462_drawdown_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_persistence over 126d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(126).skew()

def dhrk_463_drawdown_persistence_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_463_drawdown_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_persistence over 126d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(126).kurt()

def dhrk_464_drawdown_persistence_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_464_drawdown_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_persistence over 252d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(252).skew()

def dhrk_465_drawdown_persistence_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_465_drawdown_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_persistence over 252d. Time spent in 'bear market' territory.
    """
    return (((close / close.rolling(252).max() - 1) < -0.2).rolling(63).sum()).rolling(252).kurt()

def dhrk_466_drawdown_regime_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_466_drawdown_regime_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_regime over 5d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(5).skew()

def dhrk_467_drawdown_regime_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_467_drawdown_regime_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_regime over 5d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(5).kurt()

def dhrk_468_drawdown_regime_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_468_drawdown_regime_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_regime over 21d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(21).skew()

def dhrk_469_drawdown_regime_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_469_drawdown_regime_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_regime over 21d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(21).kurt()

def dhrk_470_drawdown_regime_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_470_drawdown_regime_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_regime over 63d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(63).skew()

def dhrk_471_drawdown_regime_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_471_drawdown_regime_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_regime over 63d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(63).kurt()

def dhrk_472_drawdown_regime_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_472_drawdown_regime_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_regime over 126d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(126).skew()

def dhrk_473_drawdown_regime_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_473_drawdown_regime_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_regime over 126d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(126).kurt()

def dhrk_474_drawdown_regime_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_474_drawdown_regime_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_regime over 252d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(252).skew()

def dhrk_475_drawdown_regime_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_475_drawdown_regime_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_regime over 252d. Deviation from average drawdown level.
    """
    return ((close / close.rolling(252).max() - 1) - (close / close.rolling(252).max() - 1).rolling(252).mean()).rolling(252).kurt()

def dhrk_476_drawdown_impact_score_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_476_drawdown_impact_score_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_impact_score over 5d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(5).skew()

def dhrk_477_drawdown_impact_score_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_477_drawdown_impact_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_impact_score over 5d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(5).kurt()

def dhrk_478_drawdown_impact_score_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_478_drawdown_impact_score_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_impact_score over 21d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(21).skew()

def dhrk_479_drawdown_impact_score_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_479_drawdown_impact_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_impact_score over 21d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(21).kurt()

def dhrk_480_drawdown_impact_score_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_480_drawdown_impact_score_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_impact_score over 63d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(63).skew()

def dhrk_481_drawdown_impact_score_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_481_drawdown_impact_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_impact_score over 63d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(63).kurt()

def dhrk_482_drawdown_impact_score_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_482_drawdown_impact_score_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_impact_score over 126d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(126).skew()

def dhrk_483_drawdown_impact_score_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_483_drawdown_impact_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_impact_score over 126d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(126).kurt()

def dhrk_484_drawdown_impact_score_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_484_drawdown_impact_score_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_impact_score over 252d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(252).skew()

def dhrk_485_drawdown_impact_score_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_485_drawdown_impact_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_impact_score over 252d. Depth combined with recent negative momentum.
    """
    return ((close / close.rolling(252).max() - 1) * close.pct_change(21)).rolling(252).kurt()

def dhrk_486_historical_max_drawdown_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_486_historical_max_drawdown_skew_5d
    ECONOMIC RATIONALE: Skewness of historical_max_drawdown over 5d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(5).skew()

def dhrk_487_historical_max_drawdown_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_487_historical_max_drawdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of historical_max_drawdown over 5d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(5).kurt()

def dhrk_488_historical_max_drawdown_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_488_historical_max_drawdown_skew_21d
    ECONOMIC RATIONALE: Skewness of historical_max_drawdown over 21d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(21).skew()

def dhrk_489_historical_max_drawdown_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_489_historical_max_drawdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of historical_max_drawdown over 21d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(21).kurt()

def dhrk_490_historical_max_drawdown_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_490_historical_max_drawdown_skew_63d
    ECONOMIC RATIONALE: Skewness of historical_max_drawdown over 63d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(63).skew()

def dhrk_491_historical_max_drawdown_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_491_historical_max_drawdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of historical_max_drawdown over 63d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(63).kurt()

def dhrk_492_historical_max_drawdown_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_492_historical_max_drawdown_skew_126d
    ECONOMIC RATIONALE: Skewness of historical_max_drawdown over 126d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(126).skew()

def dhrk_493_historical_max_drawdown_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_493_historical_max_drawdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of historical_max_drawdown over 126d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(126).kurt()

def dhrk_494_historical_max_drawdown_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_494_historical_max_drawdown_skew_252d
    ECONOMIC RATIONALE: Skewness of historical_max_drawdown over 252d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(252).skew()

def dhrk_495_historical_max_drawdown_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_495_historical_max_drawdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of historical_max_drawdown over 252d. Rolling 252-day maximum drawdown.
    """
    return (((close / close.rolling(252).max() - 1).rolling(252).min())).rolling(252).kurt()

def dhrk_496_drawdown_exhaustion_proxy_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_496_drawdown_exhaustion_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_exhaustion_proxy over 5d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(5).skew()

def dhrk_497_drawdown_exhaustion_proxy_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_497_drawdown_exhaustion_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_exhaustion_proxy over 5d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(5).kurt()

def dhrk_498_drawdown_exhaustion_proxy_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_498_drawdown_exhaustion_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_exhaustion_proxy over 21d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(21).skew()

def dhrk_499_drawdown_exhaustion_proxy_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_499_drawdown_exhaustion_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_exhaustion_proxy over 21d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(21).kurt()

def dhrk_500_drawdown_exhaustion_proxy_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_500_drawdown_exhaustion_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_exhaustion_proxy over 63d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(63).skew()

def dhrk_501_drawdown_exhaustion_proxy_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_501_drawdown_exhaustion_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_exhaustion_proxy over 63d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(63).kurt()

def dhrk_502_drawdown_exhaustion_proxy_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_502_drawdown_exhaustion_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_exhaustion_proxy over 126d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(126).skew()

def dhrk_503_drawdown_exhaustion_proxy_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_503_drawdown_exhaustion_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_exhaustion_proxy over 126d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(126).kurt()

def dhrk_504_drawdown_exhaustion_proxy_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_504_drawdown_exhaustion_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_exhaustion_proxy over 252d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(252).skew()

def dhrk_505_drawdown_exhaustion_proxy_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_505_drawdown_exhaustion_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_exhaustion_proxy over 252d. Current drawdown relative to recent maximum.
    """
    return ((close / close.rolling(252).max() - 1) / (close.rolling(252).min() / close.rolling(252).max() - 1).replace(0, 1e-9)).rolling(252).kurt()

def dhrk_506_drawdown_oscillator_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_506_drawdown_oscillator_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_oscillator over 5d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(5).skew()

def dhrk_507_drawdown_oscillator_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_507_drawdown_oscillator_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_oscillator over 5d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(5).kurt()

def dhrk_508_drawdown_oscillator_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_508_drawdown_oscillator_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_oscillator over 21d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(21).skew()

def dhrk_509_drawdown_oscillator_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_509_drawdown_oscillator_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_oscillator over 21d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(21).kurt()

def dhrk_510_drawdown_oscillator_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_510_drawdown_oscillator_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_oscillator over 63d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(63).skew()

def dhrk_511_drawdown_oscillator_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_511_drawdown_oscillator_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_oscillator over 63d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(63).kurt()

def dhrk_512_drawdown_oscillator_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_512_drawdown_oscillator_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_oscillator over 126d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(126).skew()

def dhrk_513_drawdown_oscillator_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_513_drawdown_oscillator_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_oscillator over 126d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(126).kurt()

def dhrk_514_drawdown_oscillator_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_514_drawdown_oscillator_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_oscillator over 252d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(252).skew()

def dhrk_515_drawdown_oscillator_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_515_drawdown_oscillator_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_oscillator over 252d. Position within the annual range.
    """
    return ((close - close.rolling(252).min()) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(252).kurt()

def dhrk_516_drawdown_tail_risk_skew_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_516_drawdown_tail_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_tail_risk over 5d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(5).skew()

def dhrk_517_drawdown_tail_risk_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_517_drawdown_tail_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_tail_risk over 5d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(5).kurt()

def dhrk_518_drawdown_tail_risk_skew_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_518_drawdown_tail_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_tail_risk over 21d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(21).skew()

def dhrk_519_drawdown_tail_risk_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_519_drawdown_tail_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_tail_risk over 21d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(21).kurt()

def dhrk_520_drawdown_tail_risk_skew_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_520_drawdown_tail_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_tail_risk over 63d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(63).skew()

def dhrk_521_drawdown_tail_risk_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_521_drawdown_tail_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_tail_risk over 63d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(63).kurt()

def dhrk_522_drawdown_tail_risk_skew_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_522_drawdown_tail_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_tail_risk over 126d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(126).skew()

def dhrk_523_drawdown_tail_risk_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_523_drawdown_tail_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_tail_risk over 126d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(126).kurt()

def dhrk_524_drawdown_tail_risk_skew_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_524_drawdown_tail_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_tail_risk over 252d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(252).skew()

def dhrk_525_drawdown_tail_risk_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_525_drawdown_tail_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_tail_risk over 252d. Binary indicator of extreme wealth destruction.
    """
    return (((close / close.rolling(252).max() - 1) < -0.5).astype(float)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V108_REGISTRY_MOMENTS = {
    "dhrk_376_current_drawdown_skew_5d": {"inputs": ["close"], "func": dhrk_376_current_drawdown_skew_5d},
    "dhrk_377_current_drawdown_kurt_5d": {"inputs": ["close"], "func": dhrk_377_current_drawdown_kurt_5d},
    "dhrk_378_current_drawdown_skew_21d": {"inputs": ["close"], "func": dhrk_378_current_drawdown_skew_21d},
    "dhrk_379_current_drawdown_kurt_21d": {"inputs": ["close"], "func": dhrk_379_current_drawdown_kurt_21d},
    "dhrk_380_current_drawdown_skew_63d": {"inputs": ["close"], "func": dhrk_380_current_drawdown_skew_63d},
    "dhrk_381_current_drawdown_kurt_63d": {"inputs": ["close"], "func": dhrk_381_current_drawdown_kurt_63d},
    "dhrk_382_current_drawdown_skew_126d": {"inputs": ["close"], "func": dhrk_382_current_drawdown_skew_126d},
    "dhrk_383_current_drawdown_kurt_126d": {"inputs": ["close"], "func": dhrk_383_current_drawdown_kurt_126d},
    "dhrk_384_current_drawdown_skew_252d": {"inputs": ["close"], "func": dhrk_384_current_drawdown_skew_252d},
    "dhrk_385_current_drawdown_kurt_252d": {"inputs": ["close"], "func": dhrk_385_current_drawdown_kurt_252d},
    "dhrk_386_drawdown_rank_252d_skew_5d": {"inputs": ["close"], "func": dhrk_386_drawdown_rank_252d_skew_5d},
    "dhrk_387_drawdown_rank_252d_kurt_5d": {"inputs": ["close"], "func": dhrk_387_drawdown_rank_252d_kurt_5d},
    "dhrk_388_drawdown_rank_252d_skew_21d": {"inputs": ["close"], "func": dhrk_388_drawdown_rank_252d_skew_21d},
    "dhrk_389_drawdown_rank_252d_kurt_21d": {"inputs": ["close"], "func": dhrk_389_drawdown_rank_252d_kurt_21d},
    "dhrk_390_drawdown_rank_252d_skew_63d": {"inputs": ["close"], "func": dhrk_390_drawdown_rank_252d_skew_63d},
    "dhrk_391_drawdown_rank_252d_kurt_63d": {"inputs": ["close"], "func": dhrk_391_drawdown_rank_252d_kurt_63d},
    "dhrk_392_drawdown_rank_252d_skew_126d": {"inputs": ["close"], "func": dhrk_392_drawdown_rank_252d_skew_126d},
    "dhrk_393_drawdown_rank_252d_kurt_126d": {"inputs": ["close"], "func": dhrk_393_drawdown_rank_252d_kurt_126d},
    "dhrk_394_drawdown_rank_252d_skew_252d": {"inputs": ["close"], "func": dhrk_394_drawdown_rank_252d_skew_252d},
    "dhrk_395_drawdown_rank_252d_kurt_252d": {"inputs": ["close"], "func": dhrk_395_drawdown_rank_252d_kurt_252d},
    "dhrk_396_drawdown_severity_z_skew_5d": {"inputs": ["close"], "func": dhrk_396_drawdown_severity_z_skew_5d},
    "dhrk_397_drawdown_severity_z_kurt_5d": {"inputs": ["close"], "func": dhrk_397_drawdown_severity_z_kurt_5d},
    "dhrk_398_drawdown_severity_z_skew_21d": {"inputs": ["close"], "func": dhrk_398_drawdown_severity_z_skew_21d},
    "dhrk_399_drawdown_severity_z_kurt_21d": {"inputs": ["close"], "func": dhrk_399_drawdown_severity_z_kurt_21d},
    "dhrk_400_drawdown_severity_z_skew_63d": {"inputs": ["close"], "func": dhrk_400_drawdown_severity_z_skew_63d},
    "dhrk_401_drawdown_severity_z_kurt_63d": {"inputs": ["close"], "func": dhrk_401_drawdown_severity_z_kurt_63d},
    "dhrk_402_drawdown_severity_z_skew_126d": {"inputs": ["close"], "func": dhrk_402_drawdown_severity_z_skew_126d},
    "dhrk_403_drawdown_severity_z_kurt_126d": {"inputs": ["close"], "func": dhrk_403_drawdown_severity_z_kurt_126d},
    "dhrk_404_drawdown_severity_z_skew_252d": {"inputs": ["close"], "func": dhrk_404_drawdown_severity_z_skew_252d},
    "dhrk_405_drawdown_severity_z_kurt_252d": {"inputs": ["close"], "func": dhrk_405_drawdown_severity_z_kurt_252d},
    "dhrk_406_drawdown_duration_skew_5d": {"inputs": ["close"], "func": dhrk_406_drawdown_duration_skew_5d},
    "dhrk_407_drawdown_duration_kurt_5d": {"inputs": ["close"], "func": dhrk_407_drawdown_duration_kurt_5d},
    "dhrk_408_drawdown_duration_skew_21d": {"inputs": ["close"], "func": dhrk_408_drawdown_duration_skew_21d},
    "dhrk_409_drawdown_duration_kurt_21d": {"inputs": ["close"], "func": dhrk_409_drawdown_duration_kurt_21d},
    "dhrk_410_drawdown_duration_skew_63d": {"inputs": ["close"], "func": dhrk_410_drawdown_duration_skew_63d},
    "dhrk_411_drawdown_duration_kurt_63d": {"inputs": ["close"], "func": dhrk_411_drawdown_duration_kurt_63d},
    "dhrk_412_drawdown_duration_skew_126d": {"inputs": ["close"], "func": dhrk_412_drawdown_duration_skew_126d},
    "dhrk_413_drawdown_duration_kurt_126d": {"inputs": ["close"], "func": dhrk_413_drawdown_duration_kurt_126d},
    "dhrk_414_drawdown_duration_skew_252d": {"inputs": ["close"], "func": dhrk_414_drawdown_duration_skew_252d},
    "dhrk_415_drawdown_duration_kurt_252d": {"inputs": ["close"], "func": dhrk_415_drawdown_duration_kurt_252d},
    "dhrk_416_peak_to_trough_momentum_skew_5d": {"inputs": ["close"], "func": dhrk_416_peak_to_trough_momentum_skew_5d},
    "dhrk_417_peak_to_trough_momentum_kurt_5d": {"inputs": ["close"], "func": dhrk_417_peak_to_trough_momentum_kurt_5d},
    "dhrk_418_peak_to_trough_momentum_skew_21d": {"inputs": ["close"], "func": dhrk_418_peak_to_trough_momentum_skew_21d},
    "dhrk_419_peak_to_trough_momentum_kurt_21d": {"inputs": ["close"], "func": dhrk_419_peak_to_trough_momentum_kurt_21d},
    "dhrk_420_peak_to_trough_momentum_skew_63d": {"inputs": ["close"], "func": dhrk_420_peak_to_trough_momentum_skew_63d},
    "dhrk_421_peak_to_trough_momentum_kurt_63d": {"inputs": ["close"], "func": dhrk_421_peak_to_trough_momentum_kurt_63d},
    "dhrk_422_peak_to_trough_momentum_skew_126d": {"inputs": ["close"], "func": dhrk_422_peak_to_trough_momentum_skew_126d},
    "dhrk_423_peak_to_trough_momentum_kurt_126d": {"inputs": ["close"], "func": dhrk_423_peak_to_trough_momentum_kurt_126d},
    "dhrk_424_peak_to_trough_momentum_skew_252d": {"inputs": ["close"], "func": dhrk_424_peak_to_trough_momentum_skew_252d},
    "dhrk_425_peak_to_trough_momentum_kurt_252d": {"inputs": ["close"], "func": dhrk_425_peak_to_trough_momentum_kurt_252d},
    "dhrk_426_drawdown_acceleration_skew_5d": {"inputs": ["close"], "func": dhrk_426_drawdown_acceleration_skew_5d},
    "dhrk_427_drawdown_acceleration_kurt_5d": {"inputs": ["close"], "func": dhrk_427_drawdown_acceleration_kurt_5d},
    "dhrk_428_drawdown_acceleration_skew_21d": {"inputs": ["close"], "func": dhrk_428_drawdown_acceleration_skew_21d},
    "dhrk_429_drawdown_acceleration_kurt_21d": {"inputs": ["close"], "func": dhrk_429_drawdown_acceleration_kurt_21d},
    "dhrk_430_drawdown_acceleration_skew_63d": {"inputs": ["close"], "func": dhrk_430_drawdown_acceleration_skew_63d},
    "dhrk_431_drawdown_acceleration_kurt_63d": {"inputs": ["close"], "func": dhrk_431_drawdown_acceleration_kurt_63d},
    "dhrk_432_drawdown_acceleration_skew_126d": {"inputs": ["close"], "func": dhrk_432_drawdown_acceleration_skew_126d},
    "dhrk_433_drawdown_acceleration_kurt_126d": {"inputs": ["close"], "func": dhrk_433_drawdown_acceleration_kurt_126d},
    "dhrk_434_drawdown_acceleration_skew_252d": {"inputs": ["close"], "func": dhrk_434_drawdown_acceleration_skew_252d},
    "dhrk_435_drawdown_acceleration_kurt_252d": {"inputs": ["close"], "func": dhrk_435_drawdown_acceleration_kurt_252d},
    "dhrk_436_drawdown_vol_ratio_skew_5d": {"inputs": ["close"], "func": dhrk_436_drawdown_vol_ratio_skew_5d},
    "dhrk_437_drawdown_vol_ratio_kurt_5d": {"inputs": ["close"], "func": dhrk_437_drawdown_vol_ratio_kurt_5d},
    "dhrk_438_drawdown_vol_ratio_skew_21d": {"inputs": ["close"], "func": dhrk_438_drawdown_vol_ratio_skew_21d},
    "dhrk_439_drawdown_vol_ratio_kurt_21d": {"inputs": ["close"], "func": dhrk_439_drawdown_vol_ratio_kurt_21d},
    "dhrk_440_drawdown_vol_ratio_skew_63d": {"inputs": ["close"], "func": dhrk_440_drawdown_vol_ratio_skew_63d},
    "dhrk_441_drawdown_vol_ratio_kurt_63d": {"inputs": ["close"], "func": dhrk_441_drawdown_vol_ratio_kurt_63d},
    "dhrk_442_drawdown_vol_ratio_skew_126d": {"inputs": ["close"], "func": dhrk_442_drawdown_vol_ratio_skew_126d},
    "dhrk_443_drawdown_vol_ratio_kurt_126d": {"inputs": ["close"], "func": dhrk_443_drawdown_vol_ratio_kurt_126d},
    "dhrk_444_drawdown_vol_ratio_skew_252d": {"inputs": ["close"], "func": dhrk_444_drawdown_vol_ratio_skew_252d},
    "dhrk_445_drawdown_vol_ratio_kurt_252d": {"inputs": ["close"], "func": dhrk_445_drawdown_vol_ratio_kurt_252d},
    "dhrk_446_recovery_from_lows_skew_5d": {"inputs": ["close"], "func": dhrk_446_recovery_from_lows_skew_5d},
    "dhrk_447_recovery_from_lows_kurt_5d": {"inputs": ["close"], "func": dhrk_447_recovery_from_lows_kurt_5d},
    "dhrk_448_recovery_from_lows_skew_21d": {"inputs": ["close"], "func": dhrk_448_recovery_from_lows_skew_21d},
    "dhrk_449_recovery_from_lows_kurt_21d": {"inputs": ["close"], "func": dhrk_449_recovery_from_lows_kurt_21d},
    "dhrk_450_recovery_from_lows_skew_63d": {"inputs": ["close"], "func": dhrk_450_recovery_from_lows_skew_63d},
    "dhrk_451_recovery_from_lows_kurt_63d": {"inputs": ["close"], "func": dhrk_451_recovery_from_lows_kurt_63d},
    "dhrk_452_recovery_from_lows_skew_126d": {"inputs": ["close"], "func": dhrk_452_recovery_from_lows_skew_126d},
    "dhrk_453_recovery_from_lows_kurt_126d": {"inputs": ["close"], "func": dhrk_453_recovery_from_lows_kurt_126d},
    "dhrk_454_recovery_from_lows_skew_252d": {"inputs": ["close"], "func": dhrk_454_recovery_from_lows_skew_252d},
    "dhrk_455_recovery_from_lows_kurt_252d": {"inputs": ["close"], "func": dhrk_455_recovery_from_lows_kurt_252d},
    "dhrk_456_drawdown_persistence_skew_5d": {"inputs": ["close"], "func": dhrk_456_drawdown_persistence_skew_5d},
    "dhrk_457_drawdown_persistence_kurt_5d": {"inputs": ["close"], "func": dhrk_457_drawdown_persistence_kurt_5d},
    "dhrk_458_drawdown_persistence_skew_21d": {"inputs": ["close"], "func": dhrk_458_drawdown_persistence_skew_21d},
    "dhrk_459_drawdown_persistence_kurt_21d": {"inputs": ["close"], "func": dhrk_459_drawdown_persistence_kurt_21d},
    "dhrk_460_drawdown_persistence_skew_63d": {"inputs": ["close"], "func": dhrk_460_drawdown_persistence_skew_63d},
    "dhrk_461_drawdown_persistence_kurt_63d": {"inputs": ["close"], "func": dhrk_461_drawdown_persistence_kurt_63d},
    "dhrk_462_drawdown_persistence_skew_126d": {"inputs": ["close"], "func": dhrk_462_drawdown_persistence_skew_126d},
    "dhrk_463_drawdown_persistence_kurt_126d": {"inputs": ["close"], "func": dhrk_463_drawdown_persistence_kurt_126d},
    "dhrk_464_drawdown_persistence_skew_252d": {"inputs": ["close"], "func": dhrk_464_drawdown_persistence_skew_252d},
    "dhrk_465_drawdown_persistence_kurt_252d": {"inputs": ["close"], "func": dhrk_465_drawdown_persistence_kurt_252d},
    "dhrk_466_drawdown_regime_skew_5d": {"inputs": ["close"], "func": dhrk_466_drawdown_regime_skew_5d},
    "dhrk_467_drawdown_regime_kurt_5d": {"inputs": ["close"], "func": dhrk_467_drawdown_regime_kurt_5d},
    "dhrk_468_drawdown_regime_skew_21d": {"inputs": ["close"], "func": dhrk_468_drawdown_regime_skew_21d},
    "dhrk_469_drawdown_regime_kurt_21d": {"inputs": ["close"], "func": dhrk_469_drawdown_regime_kurt_21d},
    "dhrk_470_drawdown_regime_skew_63d": {"inputs": ["close"], "func": dhrk_470_drawdown_regime_skew_63d},
    "dhrk_471_drawdown_regime_kurt_63d": {"inputs": ["close"], "func": dhrk_471_drawdown_regime_kurt_63d},
    "dhrk_472_drawdown_regime_skew_126d": {"inputs": ["close"], "func": dhrk_472_drawdown_regime_skew_126d},
    "dhrk_473_drawdown_regime_kurt_126d": {"inputs": ["close"], "func": dhrk_473_drawdown_regime_kurt_126d},
    "dhrk_474_drawdown_regime_skew_252d": {"inputs": ["close"], "func": dhrk_474_drawdown_regime_skew_252d},
    "dhrk_475_drawdown_regime_kurt_252d": {"inputs": ["close"], "func": dhrk_475_drawdown_regime_kurt_252d},
    "dhrk_476_drawdown_impact_score_skew_5d": {"inputs": ["close"], "func": dhrk_476_drawdown_impact_score_skew_5d},
    "dhrk_477_drawdown_impact_score_kurt_5d": {"inputs": ["close"], "func": dhrk_477_drawdown_impact_score_kurt_5d},
    "dhrk_478_drawdown_impact_score_skew_21d": {"inputs": ["close"], "func": dhrk_478_drawdown_impact_score_skew_21d},
    "dhrk_479_drawdown_impact_score_kurt_21d": {"inputs": ["close"], "func": dhrk_479_drawdown_impact_score_kurt_21d},
    "dhrk_480_drawdown_impact_score_skew_63d": {"inputs": ["close"], "func": dhrk_480_drawdown_impact_score_skew_63d},
    "dhrk_481_drawdown_impact_score_kurt_63d": {"inputs": ["close"], "func": dhrk_481_drawdown_impact_score_kurt_63d},
    "dhrk_482_drawdown_impact_score_skew_126d": {"inputs": ["close"], "func": dhrk_482_drawdown_impact_score_skew_126d},
    "dhrk_483_drawdown_impact_score_kurt_126d": {"inputs": ["close"], "func": dhrk_483_drawdown_impact_score_kurt_126d},
    "dhrk_484_drawdown_impact_score_skew_252d": {"inputs": ["close"], "func": dhrk_484_drawdown_impact_score_skew_252d},
    "dhrk_485_drawdown_impact_score_kurt_252d": {"inputs": ["close"], "func": dhrk_485_drawdown_impact_score_kurt_252d},
    "dhrk_486_historical_max_drawdown_skew_5d": {"inputs": ["close"], "func": dhrk_486_historical_max_drawdown_skew_5d},
    "dhrk_487_historical_max_drawdown_kurt_5d": {"inputs": ["close"], "func": dhrk_487_historical_max_drawdown_kurt_5d},
    "dhrk_488_historical_max_drawdown_skew_21d": {"inputs": ["close"], "func": dhrk_488_historical_max_drawdown_skew_21d},
    "dhrk_489_historical_max_drawdown_kurt_21d": {"inputs": ["close"], "func": dhrk_489_historical_max_drawdown_kurt_21d},
    "dhrk_490_historical_max_drawdown_skew_63d": {"inputs": ["close"], "func": dhrk_490_historical_max_drawdown_skew_63d},
    "dhrk_491_historical_max_drawdown_kurt_63d": {"inputs": ["close"], "func": dhrk_491_historical_max_drawdown_kurt_63d},
    "dhrk_492_historical_max_drawdown_skew_126d": {"inputs": ["close"], "func": dhrk_492_historical_max_drawdown_skew_126d},
    "dhrk_493_historical_max_drawdown_kurt_126d": {"inputs": ["close"], "func": dhrk_493_historical_max_drawdown_kurt_126d},
    "dhrk_494_historical_max_drawdown_skew_252d": {"inputs": ["close"], "func": dhrk_494_historical_max_drawdown_skew_252d},
    "dhrk_495_historical_max_drawdown_kurt_252d": {"inputs": ["close"], "func": dhrk_495_historical_max_drawdown_kurt_252d},
    "dhrk_496_drawdown_exhaustion_proxy_skew_5d": {"inputs": ["close"], "func": dhrk_496_drawdown_exhaustion_proxy_skew_5d},
    "dhrk_497_drawdown_exhaustion_proxy_kurt_5d": {"inputs": ["close"], "func": dhrk_497_drawdown_exhaustion_proxy_kurt_5d},
    "dhrk_498_drawdown_exhaustion_proxy_skew_21d": {"inputs": ["close"], "func": dhrk_498_drawdown_exhaustion_proxy_skew_21d},
    "dhrk_499_drawdown_exhaustion_proxy_kurt_21d": {"inputs": ["close"], "func": dhrk_499_drawdown_exhaustion_proxy_kurt_21d},
    "dhrk_500_drawdown_exhaustion_proxy_skew_63d": {"inputs": ["close"], "func": dhrk_500_drawdown_exhaustion_proxy_skew_63d},
    "dhrk_501_drawdown_exhaustion_proxy_kurt_63d": {"inputs": ["close"], "func": dhrk_501_drawdown_exhaustion_proxy_kurt_63d},
    "dhrk_502_drawdown_exhaustion_proxy_skew_126d": {"inputs": ["close"], "func": dhrk_502_drawdown_exhaustion_proxy_skew_126d},
    "dhrk_503_drawdown_exhaustion_proxy_kurt_126d": {"inputs": ["close"], "func": dhrk_503_drawdown_exhaustion_proxy_kurt_126d},
    "dhrk_504_drawdown_exhaustion_proxy_skew_252d": {"inputs": ["close"], "func": dhrk_504_drawdown_exhaustion_proxy_skew_252d},
    "dhrk_505_drawdown_exhaustion_proxy_kurt_252d": {"inputs": ["close"], "func": dhrk_505_drawdown_exhaustion_proxy_kurt_252d},
    "dhrk_506_drawdown_oscillator_skew_5d": {"inputs": ["close"], "func": dhrk_506_drawdown_oscillator_skew_5d},
    "dhrk_507_drawdown_oscillator_kurt_5d": {"inputs": ["close"], "func": dhrk_507_drawdown_oscillator_kurt_5d},
    "dhrk_508_drawdown_oscillator_skew_21d": {"inputs": ["close"], "func": dhrk_508_drawdown_oscillator_skew_21d},
    "dhrk_509_drawdown_oscillator_kurt_21d": {"inputs": ["close"], "func": dhrk_509_drawdown_oscillator_kurt_21d},
    "dhrk_510_drawdown_oscillator_skew_63d": {"inputs": ["close"], "func": dhrk_510_drawdown_oscillator_skew_63d},
    "dhrk_511_drawdown_oscillator_kurt_63d": {"inputs": ["close"], "func": dhrk_511_drawdown_oscillator_kurt_63d},
    "dhrk_512_drawdown_oscillator_skew_126d": {"inputs": ["close"], "func": dhrk_512_drawdown_oscillator_skew_126d},
    "dhrk_513_drawdown_oscillator_kurt_126d": {"inputs": ["close"], "func": dhrk_513_drawdown_oscillator_kurt_126d},
    "dhrk_514_drawdown_oscillator_skew_252d": {"inputs": ["close"], "func": dhrk_514_drawdown_oscillator_skew_252d},
    "dhrk_515_drawdown_oscillator_kurt_252d": {"inputs": ["close"], "func": dhrk_515_drawdown_oscillator_kurt_252d},
    "dhrk_516_drawdown_tail_risk_skew_5d": {"inputs": ["close"], "func": dhrk_516_drawdown_tail_risk_skew_5d},
    "dhrk_517_drawdown_tail_risk_kurt_5d": {"inputs": ["close"], "func": dhrk_517_drawdown_tail_risk_kurt_5d},
    "dhrk_518_drawdown_tail_risk_skew_21d": {"inputs": ["close"], "func": dhrk_518_drawdown_tail_risk_skew_21d},
    "dhrk_519_drawdown_tail_risk_kurt_21d": {"inputs": ["close"], "func": dhrk_519_drawdown_tail_risk_kurt_21d},
    "dhrk_520_drawdown_tail_risk_skew_63d": {"inputs": ["close"], "func": dhrk_520_drawdown_tail_risk_skew_63d},
    "dhrk_521_drawdown_tail_risk_kurt_63d": {"inputs": ["close"], "func": dhrk_521_drawdown_tail_risk_kurt_63d},
    "dhrk_522_drawdown_tail_risk_skew_126d": {"inputs": ["close"], "func": dhrk_522_drawdown_tail_risk_skew_126d},
    "dhrk_523_drawdown_tail_risk_kurt_126d": {"inputs": ["close"], "func": dhrk_523_drawdown_tail_risk_kurt_126d},
    "dhrk_524_drawdown_tail_risk_skew_252d": {"inputs": ["close"], "func": dhrk_524_drawdown_tail_risk_skew_252d},
    "dhrk_525_drawdown_tail_risk_kurt_252d": {"inputs": ["close"], "func": dhrk_525_drawdown_tail_risk_kurt_252d},
}
