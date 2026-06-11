"""
106_support_violation — Statistical Moments
Domain: support_violation
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

def supv_376_support_252d_break_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_376_support_252d_break_skew_5d
    ECONOMIC RATIONALE: Skewness of support_252d_break over 5d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(5).skew()

def supv_377_support_252d_break_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_377_support_252d_break_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_252d_break over 5d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(5).kurt()

def supv_378_support_252d_break_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_378_support_252d_break_skew_21d
    ECONOMIC RATIONALE: Skewness of support_252d_break over 21d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(21).skew()

def supv_379_support_252d_break_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_379_support_252d_break_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_252d_break over 21d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(21).kurt()

def supv_380_support_252d_break_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_380_support_252d_break_skew_63d
    ECONOMIC RATIONALE: Skewness of support_252d_break over 63d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(63).skew()

def supv_381_support_252d_break_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_381_support_252d_break_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_252d_break over 63d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(63).kurt()

def supv_382_support_252d_break_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_382_support_252d_break_skew_126d
    ECONOMIC RATIONALE: Skewness of support_252d_break over 126d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(126).skew()

def supv_383_support_252d_break_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_383_support_252d_break_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_252d_break over 126d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(126).kurt()

def supv_384_support_252d_break_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_384_support_252d_break_skew_252d
    ECONOMIC RATIONALE: Skewness of support_252d_break over 252d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(252).skew()

def supv_385_support_252d_break_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_385_support_252d_break_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_252d_break over 252d. Violation of the 52-week low.
    """
    return ((low < low.rolling(252).min().shift(1)).astype(float)).rolling(252).kurt()

def supv_386_support_63d_break_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_386_support_63d_break_skew_5d
    ECONOMIC RATIONALE: Skewness of support_63d_break over 5d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(5).skew()

def supv_387_support_63d_break_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_387_support_63d_break_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_63d_break over 5d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(5).kurt()

def supv_388_support_63d_break_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_388_support_63d_break_skew_21d
    ECONOMIC RATIONALE: Skewness of support_63d_break over 21d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(21).skew()

def supv_389_support_63d_break_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_389_support_63d_break_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_63d_break over 21d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(21).kurt()

def supv_390_support_63d_break_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_390_support_63d_break_skew_63d
    ECONOMIC RATIONALE: Skewness of support_63d_break over 63d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(63).skew()

def supv_391_support_63d_break_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_391_support_63d_break_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_63d_break over 63d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(63).kurt()

def supv_392_support_63d_break_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_392_support_63d_break_skew_126d
    ECONOMIC RATIONALE: Skewness of support_63d_break over 126d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(126).skew()

def supv_393_support_63d_break_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_393_support_63d_break_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_63d_break over 126d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(126).kurt()

def supv_394_support_63d_break_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_394_support_63d_break_skew_252d
    ECONOMIC RATIONALE: Skewness of support_63d_break over 252d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(252).skew()

def supv_395_support_63d_break_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_395_support_63d_break_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_63d_break over 252d. Violation of quarterly support.
    """
    return ((low < low.rolling(63).min().shift(1)).astype(float)).rolling(252).kurt()

def supv_396_volume_on_breakout_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_396_volume_on_breakout_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_on_breakout over 5d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(5).skew()

def supv_397_volume_on_breakout_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_397_volume_on_breakout_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_on_breakout over 5d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(5).kurt()

def supv_398_volume_on_breakout_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_398_volume_on_breakout_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_on_breakout over 21d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(21).skew()

def supv_399_volume_on_breakout_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_399_volume_on_breakout_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_on_breakout over 21d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(21).kurt()

def supv_400_volume_on_breakout_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_400_volume_on_breakout_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_on_breakout over 63d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(63).skew()

def supv_401_volume_on_breakout_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_401_volume_on_breakout_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_on_breakout over 63d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(63).kurt()

def supv_402_volume_on_breakout_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_402_volume_on_breakout_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_on_breakout over 126d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(126).skew()

def supv_403_volume_on_breakout_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_403_volume_on_breakout_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_on_breakout over 126d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(126).kurt()

def supv_404_volume_on_breakout_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_404_volume_on_breakout_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_on_breakout over 252d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(252).skew()

def supv_405_volume_on_breakout_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_405_volume_on_breakout_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_on_breakout over 252d. Volume intensity during support violation.
    """
    return (volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)).rolling(252).kurt()

def supv_406_support_proximity_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_406_support_proximity_skew_5d
    ECONOMIC RATIONALE: Skewness of support_proximity over 5d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(5).skew()

def supv_407_support_proximity_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_407_support_proximity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_proximity over 5d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(5).kurt()

def supv_408_support_proximity_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_408_support_proximity_skew_21d
    ECONOMIC RATIONALE: Skewness of support_proximity over 21d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(21).skew()

def supv_409_support_proximity_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_409_support_proximity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_proximity over 21d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(21).kurt()

def supv_410_support_proximity_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_410_support_proximity_skew_63d
    ECONOMIC RATIONALE: Skewness of support_proximity over 63d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(63).skew()

def supv_411_support_proximity_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_411_support_proximity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_proximity over 63d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(63).kurt()

def supv_412_support_proximity_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_412_support_proximity_skew_126d
    ECONOMIC RATIONALE: Skewness of support_proximity over 126d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(126).skew()

def supv_413_support_proximity_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_413_support_proximity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_proximity over 126d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(126).kurt()

def supv_414_support_proximity_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_414_support_proximity_skew_252d
    ECONOMIC RATIONALE: Skewness of support_proximity over 252d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(252).skew()

def supv_415_support_proximity_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_415_support_proximity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_proximity over 252d. Closeness to major support levels.
    """
    return ((close - low.rolling(63).min()) / close).rolling(252).kurt()

def supv_416_support_bounce_failure_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_416_support_bounce_failure_skew_5d
    ECONOMIC RATIONALE: Skewness of support_bounce_failure over 5d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(5).skew()

def supv_417_support_bounce_failure_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_417_support_bounce_failure_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_bounce_failure over 5d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(5).kurt()

def supv_418_support_bounce_failure_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_418_support_bounce_failure_skew_21d
    ECONOMIC RATIONALE: Skewness of support_bounce_failure over 21d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(21).skew()

def supv_419_support_bounce_failure_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_419_support_bounce_failure_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_bounce_failure over 21d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(21).kurt()

def supv_420_support_bounce_failure_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_420_support_bounce_failure_skew_63d
    ECONOMIC RATIONALE: Skewness of support_bounce_failure over 63d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(63).skew()

def supv_421_support_bounce_failure_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_421_support_bounce_failure_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_bounce_failure over 63d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(63).kurt()

def supv_422_support_bounce_failure_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_422_support_bounce_failure_skew_126d
    ECONOMIC RATIONALE: Skewness of support_bounce_failure over 126d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(126).skew()

def supv_423_support_bounce_failure_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_423_support_bounce_failure_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_bounce_failure over 126d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(126).kurt()

def supv_424_support_bounce_failure_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_424_support_bounce_failure_skew_252d
    ECONOMIC RATIONALE: Skewness of support_bounce_failure over 252d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(252).skew()

def supv_425_support_bounce_failure_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_425_support_bounce_failure_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_bounce_failure over 252d. Failure to rally significantly after hitting support.
    """
    return ((close / low.rolling(63).min() - 1) < 0.02).rolling(252).kurt()

def supv_426_multiple_support_test_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_426_multiple_support_test_skew_5d
    ECONOMIC RATIONALE: Skewness of multiple_support_test over 5d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(5).skew()

def supv_427_multiple_support_test_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_427_multiple_support_test_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of multiple_support_test over 5d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(5).kurt()

def supv_428_multiple_support_test_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_428_multiple_support_test_skew_21d
    ECONOMIC RATIONALE: Skewness of multiple_support_test over 21d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(21).skew()

def supv_429_multiple_support_test_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_429_multiple_support_test_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of multiple_support_test over 21d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(21).kurt()

def supv_430_multiple_support_test_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_430_multiple_support_test_skew_63d
    ECONOMIC RATIONALE: Skewness of multiple_support_test over 63d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(63).skew()

def supv_431_multiple_support_test_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_431_multiple_support_test_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of multiple_support_test over 63d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(63).kurt()

def supv_432_multiple_support_test_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_432_multiple_support_test_skew_126d
    ECONOMIC RATIONALE: Skewness of multiple_support_test over 126d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(126).skew()

def supv_433_multiple_support_test_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_433_multiple_support_test_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of multiple_support_test over 126d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(126).kurt()

def supv_434_multiple_support_test_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_434_multiple_support_test_skew_252d
    ECONOMIC RATIONALE: Skewness of multiple_support_test over 252d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(252).skew()

def supv_435_multiple_support_test_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_435_multiple_support_test_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of multiple_support_test over 252d. Frequency of new lows being made.
    """
    return (((low < low.rolling(21).min().shift(1)).rolling(63).sum())).rolling(252).kurt()

def supv_436_support_zone_density_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_436_support_zone_density_skew_5d
    ECONOMIC RATIONALE: Skewness of support_zone_density over 5d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(5).skew()

def supv_437_support_zone_density_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_437_support_zone_density_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_zone_density over 5d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(5).kurt()

def supv_438_support_zone_density_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_438_support_zone_density_skew_21d
    ECONOMIC RATIONALE: Skewness of support_zone_density over 21d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(21).skew()

def supv_439_support_zone_density_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_439_support_zone_density_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_zone_density over 21d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(21).kurt()

def supv_440_support_zone_density_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_440_support_zone_density_skew_63d
    ECONOMIC RATIONALE: Skewness of support_zone_density over 63d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(63).skew()

def supv_441_support_zone_density_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_441_support_zone_density_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_zone_density over 63d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(63).kurt()

def supv_442_support_zone_density_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_442_support_zone_density_skew_126d
    ECONOMIC RATIONALE: Skewness of support_zone_density over 126d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(126).skew()

def supv_443_support_zone_density_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_443_support_zone_density_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_zone_density over 126d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(126).kurt()

def supv_444_support_zone_density_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_444_support_zone_density_skew_252d
    ECONOMIC RATIONALE: Skewness of support_zone_density over 252d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(252).skew()

def supv_445_support_zone_density_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_445_support_zone_density_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_zone_density over 252d. Time spent near support zones.
    """
    return (((low < low.rolling(63).min() * 1.02).rolling(21).sum())).rolling(252).kurt()

def supv_446_breakdown_momentum_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_446_breakdown_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of breakdown_momentum over 5d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(5).skew()

def supv_447_breakdown_momentum_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_447_breakdown_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of breakdown_momentum over 5d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(5).kurt()

def supv_448_breakdown_momentum_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_448_breakdown_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of breakdown_momentum over 21d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(21).skew()

def supv_449_breakdown_momentum_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_449_breakdown_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of breakdown_momentum over 21d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(21).kurt()

def supv_450_breakdown_momentum_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_450_breakdown_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of breakdown_momentum over 63d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(63).skew()

def supv_451_breakdown_momentum_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_451_breakdown_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of breakdown_momentum over 63d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(63).kurt()

def supv_452_breakdown_momentum_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_452_breakdown_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of breakdown_momentum over 126d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(126).skew()

def supv_453_breakdown_momentum_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_453_breakdown_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of breakdown_momentum over 126d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(126).kurt()

def supv_454_breakdown_momentum_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_454_breakdown_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of breakdown_momentum over 252d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(252).skew()

def supv_455_breakdown_momentum_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_455_breakdown_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of breakdown_momentum over 252d. Speed of price drop following support break.
    """
    return (close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)).rolling(252).kurt()

def supv_456_support_reversal_trap_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_456_support_reversal_trap_skew_5d
    ECONOMIC RATIONALE: Skewness of support_reversal_trap over 5d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(5).skew()

def supv_457_support_reversal_trap_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_457_support_reversal_trap_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_reversal_trap over 5d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(5).kurt()

def supv_458_support_reversal_trap_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_458_support_reversal_trap_skew_21d
    ECONOMIC RATIONALE: Skewness of support_reversal_trap over 21d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(21).skew()

def supv_459_support_reversal_trap_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_459_support_reversal_trap_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_reversal_trap over 21d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(21).kurt()

def supv_460_support_reversal_trap_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_460_support_reversal_trap_skew_63d
    ECONOMIC RATIONALE: Skewness of support_reversal_trap over 63d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(63).skew()

def supv_461_support_reversal_trap_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_461_support_reversal_trap_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_reversal_trap over 63d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(63).kurt()

def supv_462_support_reversal_trap_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_462_support_reversal_trap_skew_126d
    ECONOMIC RATIONALE: Skewness of support_reversal_trap over 126d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(126).skew()

def supv_463_support_reversal_trap_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_463_support_reversal_trap_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_reversal_trap over 126d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(126).kurt()

def supv_464_support_reversal_trap_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_464_support_reversal_trap_skew_252d
    ECONOMIC RATIONALE: Skewness of support_reversal_trap over 252d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(252).skew()

def supv_465_support_reversal_trap_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_465_support_reversal_trap_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_reversal_trap over 252d. Attempted intraday reversal at support.
    """
    return ((low < low.rolling(63).min().shift(1)) & (close > open)).rolling(252).kurt()

def supv_466_support_gap_down_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_466_support_gap_down_skew_5d
    ECONOMIC RATIONALE: Skewness of support_gap_down over 5d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(5).skew()

def supv_467_support_gap_down_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_467_support_gap_down_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_gap_down over 5d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(5).kurt()

def supv_468_support_gap_down_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_468_support_gap_down_skew_21d
    ECONOMIC RATIONALE: Skewness of support_gap_down over 21d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(21).skew()

def supv_469_support_gap_down_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_469_support_gap_down_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_gap_down over 21d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(21).kurt()

def supv_470_support_gap_down_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_470_support_gap_down_skew_63d
    ECONOMIC RATIONALE: Skewness of support_gap_down over 63d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(63).skew()

def supv_471_support_gap_down_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_471_support_gap_down_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_gap_down over 63d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(63).kurt()

def supv_472_support_gap_down_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_472_support_gap_down_skew_126d
    ECONOMIC RATIONALE: Skewness of support_gap_down over 126d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(126).skew()

def supv_473_support_gap_down_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_473_support_gap_down_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_gap_down over 126d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(126).kurt()

def supv_474_support_gap_down_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_474_support_gap_down_skew_252d
    ECONOMIC RATIONALE: Skewness of support_gap_down over 252d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(252).skew()

def supv_475_support_gap_down_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_475_support_gap_down_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_gap_down over 252d. Gapping down through major support.
    """
    return ((high < low.shift(1)) & (low < low.rolling(63).min())).rolling(252).kurt()

def supv_476_psychological_support_100_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_476_psychological_support_100_skew_5d
    ECONOMIC RATIONALE: Skewness of psychological_support_100 over 5d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(5).skew()

def supv_477_psychological_support_100_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_477_psychological_support_100_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of psychological_support_100 over 5d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(5).kurt()

def supv_478_psychological_support_100_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_478_psychological_support_100_skew_21d
    ECONOMIC RATIONALE: Skewness of psychological_support_100 over 21d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(21).skew()

def supv_479_psychological_support_100_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_479_psychological_support_100_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of psychological_support_100 over 21d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(21).kurt()

def supv_480_psychological_support_100_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_480_psychological_support_100_skew_63d
    ECONOMIC RATIONALE: Skewness of psychological_support_100 over 63d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(63).skew()

def supv_481_psychological_support_100_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_481_psychological_support_100_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of psychological_support_100 over 63d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(63).kurt()

def supv_482_psychological_support_100_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_482_psychological_support_100_skew_126d
    ECONOMIC RATIONALE: Skewness of psychological_support_100 over 126d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(126).skew()

def supv_483_psychological_support_100_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_483_psychological_support_100_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of psychological_support_100 over 126d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(126).kurt()

def supv_484_psychological_support_100_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_484_psychological_support_100_skew_252d
    ECONOMIC RATIONALE: Skewness of psychological_support_100 over 252d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(252).skew()

def supv_485_psychological_support_100_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_485_psychological_support_100_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of psychological_support_100 over 252d. Proximity to round number support levels.
    """
    return ((close % 100 < 2).astype(float)).rolling(252).kurt()

def supv_486_support_vol_z_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_486_support_vol_z_skew_5d
    ECONOMIC RATIONALE: Skewness of support_vol_z over 5d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(5).skew()

def supv_487_support_vol_z_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_487_support_vol_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_vol_z over 5d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(5).kurt()

def supv_488_support_vol_z_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_488_support_vol_z_skew_21d
    ECONOMIC RATIONALE: Skewness of support_vol_z over 21d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(21).skew()

def supv_489_support_vol_z_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_489_support_vol_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_vol_z over 21d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(21).kurt()

def supv_490_support_vol_z_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_490_support_vol_z_skew_63d
    ECONOMIC RATIONALE: Skewness of support_vol_z over 63d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(63).skew()

def supv_491_support_vol_z_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_491_support_vol_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_vol_z over 63d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(63).kurt()

def supv_492_support_vol_z_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_492_support_vol_z_skew_126d
    ECONOMIC RATIONALE: Skewness of support_vol_z over 126d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(126).skew()

def supv_493_support_vol_z_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_493_support_vol_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_vol_z over 126d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(126).kurt()

def supv_494_support_vol_z_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_494_support_vol_z_skew_252d
    ECONOMIC RATIONALE: Skewness of support_vol_z over 252d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(252).skew()

def supv_495_support_vol_z_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_495_support_vol_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_vol_z over 252d. Abnormal volume during support breaks.
    """
    return (_zscore_rolling(volume * (low < low.rolling(63).min().shift(1)), 252)).rolling(252).kurt()

def supv_496_structural_breakdown_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_496_structural_breakdown_skew_5d
    ECONOMIC RATIONALE: Skewness of structural_breakdown over 5d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(5).skew()

def supv_497_structural_breakdown_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_497_structural_breakdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of structural_breakdown over 5d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(5).kurt()

def supv_498_structural_breakdown_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_498_structural_breakdown_skew_21d
    ECONOMIC RATIONALE: Skewness of structural_breakdown over 21d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(21).skew()

def supv_499_structural_breakdown_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_499_structural_breakdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of structural_breakdown over 21d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(21).kurt()

def supv_500_structural_breakdown_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_500_structural_breakdown_skew_63d
    ECONOMIC RATIONALE: Skewness of structural_breakdown over 63d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(63).skew()

def supv_501_structural_breakdown_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_501_structural_breakdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of structural_breakdown over 63d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(63).kurt()

def supv_502_structural_breakdown_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_502_structural_breakdown_skew_126d
    ECONOMIC RATIONALE: Skewness of structural_breakdown over 126d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(126).skew()

def supv_503_structural_breakdown_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_503_structural_breakdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of structural_breakdown over 126d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(126).kurt()

def supv_504_structural_breakdown_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_504_structural_breakdown_skew_252d
    ECONOMIC RATIONALE: Skewness of structural_breakdown over 252d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(252).skew()

def supv_505_structural_breakdown_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_505_structural_breakdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of structural_breakdown over 252d. Breakdown below long-term structural envelopes.
    """
    return (close < low.rolling(252).mean() - 2*low.rolling(252).std()).rolling(252).kurt()

def supv_506_support_recovery_rate_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_506_support_recovery_rate_skew_5d
    ECONOMIC RATIONALE: Skewness of support_recovery_rate over 5d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(5).skew()

def supv_507_support_recovery_rate_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_507_support_recovery_rate_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_recovery_rate over 5d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(5).kurt()

def supv_508_support_recovery_rate_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_508_support_recovery_rate_skew_21d
    ECONOMIC RATIONALE: Skewness of support_recovery_rate over 21d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(21).skew()

def supv_509_support_recovery_rate_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_509_support_recovery_rate_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_recovery_rate over 21d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(21).kurt()

def supv_510_support_recovery_rate_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_510_support_recovery_rate_skew_63d
    ECONOMIC RATIONALE: Skewness of support_recovery_rate over 63d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(63).skew()

def supv_511_support_recovery_rate_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_511_support_recovery_rate_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_recovery_rate over 63d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(63).kurt()

def supv_512_support_recovery_rate_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_512_support_recovery_rate_skew_126d
    ECONOMIC RATIONALE: Skewness of support_recovery_rate over 126d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(126).skew()

def supv_513_support_recovery_rate_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_513_support_recovery_rate_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_recovery_rate over 126d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(126).kurt()

def supv_514_support_recovery_rate_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_514_support_recovery_rate_skew_252d
    ECONOMIC RATIONALE: Skewness of support_recovery_rate over 252d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(252).skew()

def supv_515_support_recovery_rate_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_515_support_recovery_rate_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_recovery_rate over 252d. Ratio of current price to quarterly support.
    """
    return (close / low.rolling(63).min()).rolling(252).kurt()

def supv_516_support_cascade_risk_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_516_support_cascade_risk_skew_5d
    ECONOMIC RATIONALE: Skewness of support_cascade_risk over 5d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(5).skew()

def supv_517_support_cascade_risk_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_517_support_cascade_risk_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_cascade_risk over 5d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(5).kurt()

def supv_518_support_cascade_risk_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_518_support_cascade_risk_skew_21d
    ECONOMIC RATIONALE: Skewness of support_cascade_risk over 21d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(21).skew()

def supv_519_support_cascade_risk_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_519_support_cascade_risk_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_cascade_risk over 21d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(21).kurt()

def supv_520_support_cascade_risk_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_520_support_cascade_risk_skew_63d
    ECONOMIC RATIONALE: Skewness of support_cascade_risk over 63d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(63).skew()

def supv_521_support_cascade_risk_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_521_support_cascade_risk_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_cascade_risk over 63d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(63).kurt()

def supv_522_support_cascade_risk_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_522_support_cascade_risk_skew_126d
    ECONOMIC RATIONALE: Skewness of support_cascade_risk over 126d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(126).skew()

def supv_523_support_cascade_risk_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_523_support_cascade_risk_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_cascade_risk over 126d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(126).kurt()

def supv_524_support_cascade_risk_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_524_support_cascade_risk_skew_252d
    ECONOMIC RATIONALE: Skewness of support_cascade_risk over 252d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(252).skew()

def supv_525_support_cascade_risk_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_525_support_cascade_risk_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_cascade_risk over 252d. Sequential support violations indicating a cascade.
    """
    return ((low < low.rolling(21).min().shift(1)).rolling(5).sum() > 2).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V106_REGISTRY_MOMENTS = {
    "supv_376_support_252d_break_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_376_support_252d_break_skew_5d},
    "supv_377_support_252d_break_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_377_support_252d_break_kurt_5d},
    "supv_378_support_252d_break_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_378_support_252d_break_skew_21d},
    "supv_379_support_252d_break_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_379_support_252d_break_kurt_21d},
    "supv_380_support_252d_break_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_380_support_252d_break_skew_63d},
    "supv_381_support_252d_break_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_381_support_252d_break_kurt_63d},
    "supv_382_support_252d_break_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_382_support_252d_break_skew_126d},
    "supv_383_support_252d_break_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_383_support_252d_break_kurt_126d},
    "supv_384_support_252d_break_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_384_support_252d_break_skew_252d},
    "supv_385_support_252d_break_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_385_support_252d_break_kurt_252d},
    "supv_386_support_63d_break_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_386_support_63d_break_skew_5d},
    "supv_387_support_63d_break_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_387_support_63d_break_kurt_5d},
    "supv_388_support_63d_break_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_388_support_63d_break_skew_21d},
    "supv_389_support_63d_break_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_389_support_63d_break_kurt_21d},
    "supv_390_support_63d_break_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_390_support_63d_break_skew_63d},
    "supv_391_support_63d_break_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_391_support_63d_break_kurt_63d},
    "supv_392_support_63d_break_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_392_support_63d_break_skew_126d},
    "supv_393_support_63d_break_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_393_support_63d_break_kurt_126d},
    "supv_394_support_63d_break_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_394_support_63d_break_skew_252d},
    "supv_395_support_63d_break_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_395_support_63d_break_kurt_252d},
    "supv_396_volume_on_breakout_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_396_volume_on_breakout_skew_5d},
    "supv_397_volume_on_breakout_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_397_volume_on_breakout_kurt_5d},
    "supv_398_volume_on_breakout_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_398_volume_on_breakout_skew_21d},
    "supv_399_volume_on_breakout_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_399_volume_on_breakout_kurt_21d},
    "supv_400_volume_on_breakout_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_400_volume_on_breakout_skew_63d},
    "supv_401_volume_on_breakout_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_401_volume_on_breakout_kurt_63d},
    "supv_402_volume_on_breakout_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_402_volume_on_breakout_skew_126d},
    "supv_403_volume_on_breakout_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_403_volume_on_breakout_kurt_126d},
    "supv_404_volume_on_breakout_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_404_volume_on_breakout_skew_252d},
    "supv_405_volume_on_breakout_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_405_volume_on_breakout_kurt_252d},
    "supv_406_support_proximity_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_406_support_proximity_skew_5d},
    "supv_407_support_proximity_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_407_support_proximity_kurt_5d},
    "supv_408_support_proximity_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_408_support_proximity_skew_21d},
    "supv_409_support_proximity_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_409_support_proximity_kurt_21d},
    "supv_410_support_proximity_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_410_support_proximity_skew_63d},
    "supv_411_support_proximity_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_411_support_proximity_kurt_63d},
    "supv_412_support_proximity_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_412_support_proximity_skew_126d},
    "supv_413_support_proximity_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_413_support_proximity_kurt_126d},
    "supv_414_support_proximity_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_414_support_proximity_skew_252d},
    "supv_415_support_proximity_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_415_support_proximity_kurt_252d},
    "supv_416_support_bounce_failure_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_416_support_bounce_failure_skew_5d},
    "supv_417_support_bounce_failure_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_417_support_bounce_failure_kurt_5d},
    "supv_418_support_bounce_failure_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_418_support_bounce_failure_skew_21d},
    "supv_419_support_bounce_failure_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_419_support_bounce_failure_kurt_21d},
    "supv_420_support_bounce_failure_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_420_support_bounce_failure_skew_63d},
    "supv_421_support_bounce_failure_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_421_support_bounce_failure_kurt_63d},
    "supv_422_support_bounce_failure_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_422_support_bounce_failure_skew_126d},
    "supv_423_support_bounce_failure_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_423_support_bounce_failure_kurt_126d},
    "supv_424_support_bounce_failure_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_424_support_bounce_failure_skew_252d},
    "supv_425_support_bounce_failure_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_425_support_bounce_failure_kurt_252d},
    "supv_426_multiple_support_test_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_426_multiple_support_test_skew_5d},
    "supv_427_multiple_support_test_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_427_multiple_support_test_kurt_5d},
    "supv_428_multiple_support_test_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_428_multiple_support_test_skew_21d},
    "supv_429_multiple_support_test_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_429_multiple_support_test_kurt_21d},
    "supv_430_multiple_support_test_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_430_multiple_support_test_skew_63d},
    "supv_431_multiple_support_test_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_431_multiple_support_test_kurt_63d},
    "supv_432_multiple_support_test_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_432_multiple_support_test_skew_126d},
    "supv_433_multiple_support_test_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_433_multiple_support_test_kurt_126d},
    "supv_434_multiple_support_test_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_434_multiple_support_test_skew_252d},
    "supv_435_multiple_support_test_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_435_multiple_support_test_kurt_252d},
    "supv_436_support_zone_density_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_436_support_zone_density_skew_5d},
    "supv_437_support_zone_density_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_437_support_zone_density_kurt_5d},
    "supv_438_support_zone_density_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_438_support_zone_density_skew_21d},
    "supv_439_support_zone_density_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_439_support_zone_density_kurt_21d},
    "supv_440_support_zone_density_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_440_support_zone_density_skew_63d},
    "supv_441_support_zone_density_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_441_support_zone_density_kurt_63d},
    "supv_442_support_zone_density_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_442_support_zone_density_skew_126d},
    "supv_443_support_zone_density_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_443_support_zone_density_kurt_126d},
    "supv_444_support_zone_density_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_444_support_zone_density_skew_252d},
    "supv_445_support_zone_density_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_445_support_zone_density_kurt_252d},
    "supv_446_breakdown_momentum_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_446_breakdown_momentum_skew_5d},
    "supv_447_breakdown_momentum_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_447_breakdown_momentum_kurt_5d},
    "supv_448_breakdown_momentum_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_448_breakdown_momentum_skew_21d},
    "supv_449_breakdown_momentum_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_449_breakdown_momentum_kurt_21d},
    "supv_450_breakdown_momentum_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_450_breakdown_momentum_skew_63d},
    "supv_451_breakdown_momentum_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_451_breakdown_momentum_kurt_63d},
    "supv_452_breakdown_momentum_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_452_breakdown_momentum_skew_126d},
    "supv_453_breakdown_momentum_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_453_breakdown_momentum_kurt_126d},
    "supv_454_breakdown_momentum_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_454_breakdown_momentum_skew_252d},
    "supv_455_breakdown_momentum_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_455_breakdown_momentum_kurt_252d},
    "supv_456_support_reversal_trap_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_456_support_reversal_trap_skew_5d},
    "supv_457_support_reversal_trap_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_457_support_reversal_trap_kurt_5d},
    "supv_458_support_reversal_trap_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_458_support_reversal_trap_skew_21d},
    "supv_459_support_reversal_trap_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_459_support_reversal_trap_kurt_21d},
    "supv_460_support_reversal_trap_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_460_support_reversal_trap_skew_63d},
    "supv_461_support_reversal_trap_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_461_support_reversal_trap_kurt_63d},
    "supv_462_support_reversal_trap_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_462_support_reversal_trap_skew_126d},
    "supv_463_support_reversal_trap_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_463_support_reversal_trap_kurt_126d},
    "supv_464_support_reversal_trap_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_464_support_reversal_trap_skew_252d},
    "supv_465_support_reversal_trap_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_465_support_reversal_trap_kurt_252d},
    "supv_466_support_gap_down_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_466_support_gap_down_skew_5d},
    "supv_467_support_gap_down_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_467_support_gap_down_kurt_5d},
    "supv_468_support_gap_down_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_468_support_gap_down_skew_21d},
    "supv_469_support_gap_down_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_469_support_gap_down_kurt_21d},
    "supv_470_support_gap_down_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_470_support_gap_down_skew_63d},
    "supv_471_support_gap_down_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_471_support_gap_down_kurt_63d},
    "supv_472_support_gap_down_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_472_support_gap_down_skew_126d},
    "supv_473_support_gap_down_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_473_support_gap_down_kurt_126d},
    "supv_474_support_gap_down_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_474_support_gap_down_skew_252d},
    "supv_475_support_gap_down_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_475_support_gap_down_kurt_252d},
    "supv_476_psychological_support_100_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_476_psychological_support_100_skew_5d},
    "supv_477_psychological_support_100_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_477_psychological_support_100_kurt_5d},
    "supv_478_psychological_support_100_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_478_psychological_support_100_skew_21d},
    "supv_479_psychological_support_100_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_479_psychological_support_100_kurt_21d},
    "supv_480_psychological_support_100_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_480_psychological_support_100_skew_63d},
    "supv_481_psychological_support_100_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_481_psychological_support_100_kurt_63d},
    "supv_482_psychological_support_100_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_482_psychological_support_100_skew_126d},
    "supv_483_psychological_support_100_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_483_psychological_support_100_kurt_126d},
    "supv_484_psychological_support_100_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_484_psychological_support_100_skew_252d},
    "supv_485_psychological_support_100_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_485_psychological_support_100_kurt_252d},
    "supv_486_support_vol_z_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_486_support_vol_z_skew_5d},
    "supv_487_support_vol_z_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_487_support_vol_z_kurt_5d},
    "supv_488_support_vol_z_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_488_support_vol_z_skew_21d},
    "supv_489_support_vol_z_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_489_support_vol_z_kurt_21d},
    "supv_490_support_vol_z_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_490_support_vol_z_skew_63d},
    "supv_491_support_vol_z_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_491_support_vol_z_kurt_63d},
    "supv_492_support_vol_z_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_492_support_vol_z_skew_126d},
    "supv_493_support_vol_z_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_493_support_vol_z_kurt_126d},
    "supv_494_support_vol_z_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_494_support_vol_z_skew_252d},
    "supv_495_support_vol_z_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_495_support_vol_z_kurt_252d},
    "supv_496_structural_breakdown_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_496_structural_breakdown_skew_5d},
    "supv_497_structural_breakdown_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_497_structural_breakdown_kurt_5d},
    "supv_498_structural_breakdown_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_498_structural_breakdown_skew_21d},
    "supv_499_structural_breakdown_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_499_structural_breakdown_kurt_21d},
    "supv_500_structural_breakdown_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_500_structural_breakdown_skew_63d},
    "supv_501_structural_breakdown_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_501_structural_breakdown_kurt_63d},
    "supv_502_structural_breakdown_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_502_structural_breakdown_skew_126d},
    "supv_503_structural_breakdown_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_503_structural_breakdown_kurt_126d},
    "supv_504_structural_breakdown_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_504_structural_breakdown_skew_252d},
    "supv_505_structural_breakdown_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_505_structural_breakdown_kurt_252d},
    "supv_506_support_recovery_rate_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_506_support_recovery_rate_skew_5d},
    "supv_507_support_recovery_rate_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_507_support_recovery_rate_kurt_5d},
    "supv_508_support_recovery_rate_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_508_support_recovery_rate_skew_21d},
    "supv_509_support_recovery_rate_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_509_support_recovery_rate_kurt_21d},
    "supv_510_support_recovery_rate_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_510_support_recovery_rate_skew_63d},
    "supv_511_support_recovery_rate_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_511_support_recovery_rate_kurt_63d},
    "supv_512_support_recovery_rate_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_512_support_recovery_rate_skew_126d},
    "supv_513_support_recovery_rate_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_513_support_recovery_rate_kurt_126d},
    "supv_514_support_recovery_rate_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_514_support_recovery_rate_skew_252d},
    "supv_515_support_recovery_rate_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_515_support_recovery_rate_kurt_252d},
    "supv_516_support_cascade_risk_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_516_support_cascade_risk_skew_5d},
    "supv_517_support_cascade_risk_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_517_support_cascade_risk_kurt_5d},
    "supv_518_support_cascade_risk_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_518_support_cascade_risk_skew_21d},
    "supv_519_support_cascade_risk_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_519_support_cascade_risk_kurt_21d},
    "supv_520_support_cascade_risk_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_520_support_cascade_risk_skew_63d},
    "supv_521_support_cascade_risk_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_521_support_cascade_risk_kurt_63d},
    "supv_522_support_cascade_risk_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_522_support_cascade_risk_skew_126d},
    "supv_523_support_cascade_risk_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_523_support_cascade_risk_kurt_126d},
    "supv_524_support_cascade_risk_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_524_support_cascade_risk_skew_252d},
    "supv_525_support_cascade_risk_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_525_support_cascade_risk_kurt_252d},
}
