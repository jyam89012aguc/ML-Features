"""
117_price_clustering_psychology — Statistical Moments
Domain: price_clustering_psychology
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

def ppsy_376_round_number_proximity_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_376_round_number_proximity_skew_5d
    ECONOMIC RATIONALE: Skewness of round_number_proximity over 5d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(5).skew()

def ppsy_377_round_number_proximity_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_377_round_number_proximity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of round_number_proximity over 5d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(5).kurt()

def ppsy_378_round_number_proximity_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_378_round_number_proximity_skew_21d
    ECONOMIC RATIONALE: Skewness of round_number_proximity over 21d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(21).skew()

def ppsy_379_round_number_proximity_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_379_round_number_proximity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of round_number_proximity over 21d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(21).kurt()

def ppsy_380_round_number_proximity_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_380_round_number_proximity_skew_63d
    ECONOMIC RATIONALE: Skewness of round_number_proximity over 63d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(63).skew()

def ppsy_381_round_number_proximity_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_381_round_number_proximity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of round_number_proximity over 63d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(63).kurt()

def ppsy_382_round_number_proximity_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_382_round_number_proximity_skew_126d
    ECONOMIC RATIONALE: Skewness of round_number_proximity over 126d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(126).skew()

def ppsy_383_round_number_proximity_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_383_round_number_proximity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of round_number_proximity over 126d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(126).kurt()

def ppsy_384_round_number_proximity_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_384_round_number_proximity_skew_252d
    ECONOMIC RATIONALE: Skewness of round_number_proximity over 252d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(252).skew()

def ppsy_385_round_number_proximity_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_385_round_number_proximity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of round_number_proximity over 252d. Proximity to whole dollar amounts.
    """
    return (close % 1.0).rolling(252).kurt()

def ppsy_386_decade_number_proximity_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_386_decade_number_proximity_skew_5d
    ECONOMIC RATIONALE: Skewness of decade_number_proximity over 5d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(5).skew()

def ppsy_387_decade_number_proximity_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_387_decade_number_proximity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of decade_number_proximity over 5d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(5).kurt()

def ppsy_388_decade_number_proximity_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_388_decade_number_proximity_skew_21d
    ECONOMIC RATIONALE: Skewness of decade_number_proximity over 21d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(21).skew()

def ppsy_389_decade_number_proximity_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_389_decade_number_proximity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of decade_number_proximity over 21d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(21).kurt()

def ppsy_390_decade_number_proximity_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_390_decade_number_proximity_skew_63d
    ECONOMIC RATIONALE: Skewness of decade_number_proximity over 63d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(63).skew()

def ppsy_391_decade_number_proximity_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_391_decade_number_proximity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of decade_number_proximity over 63d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(63).kurt()

def ppsy_392_decade_number_proximity_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_392_decade_number_proximity_skew_126d
    ECONOMIC RATIONALE: Skewness of decade_number_proximity over 126d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(126).skew()

def ppsy_393_decade_number_proximity_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_393_decade_number_proximity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of decade_number_proximity over 126d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(126).kurt()

def ppsy_394_decade_number_proximity_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_394_decade_number_proximity_skew_252d
    ECONOMIC RATIONALE: Skewness of decade_number_proximity over 252d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(252).skew()

def ppsy_395_decade_number_proximity_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_395_decade_number_proximity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of decade_number_proximity over 252d. Proximity to ten-dollar increments.
    """
    return (close % 10.0).rolling(252).kurt()

def ppsy_396_century_number_proximity_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_396_century_number_proximity_skew_5d
    ECONOMIC RATIONALE: Skewness of century_number_proximity over 5d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(5).skew()

def ppsy_397_century_number_proximity_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_397_century_number_proximity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of century_number_proximity over 5d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(5).kurt()

def ppsy_398_century_number_proximity_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_398_century_number_proximity_skew_21d
    ECONOMIC RATIONALE: Skewness of century_number_proximity over 21d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(21).skew()

def ppsy_399_century_number_proximity_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_399_century_number_proximity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of century_number_proximity over 21d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(21).kurt()

def ppsy_400_century_number_proximity_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_400_century_number_proximity_skew_63d
    ECONOMIC RATIONALE: Skewness of century_number_proximity over 63d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(63).skew()

def ppsy_401_century_number_proximity_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_401_century_number_proximity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of century_number_proximity over 63d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(63).kurt()

def ppsy_402_century_number_proximity_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_402_century_number_proximity_skew_126d
    ECONOMIC RATIONALE: Skewness of century_number_proximity over 126d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(126).skew()

def ppsy_403_century_number_proximity_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_403_century_number_proximity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of century_number_proximity over 126d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(126).kurt()

def ppsy_404_century_number_proximity_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_404_century_number_proximity_skew_252d
    ECONOMIC RATIONALE: Skewness of century_number_proximity over 252d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(252).skew()

def ppsy_405_century_number_proximity_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_405_century_number_proximity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of century_number_proximity over 252d. Proximity to hundred-dollar increments.
    """
    return (close % 100.0).rolling(252).kurt()

def ppsy_406_price_level_clustering_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_406_price_level_clustering_skew_5d
    ECONOMIC RATIONALE: Skewness of price_level_clustering over 5d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(5).skew()

def ppsy_407_price_level_clustering_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_407_price_level_clustering_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_level_clustering over 5d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(5).kurt()

def ppsy_408_price_level_clustering_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_408_price_level_clustering_skew_21d
    ECONOMIC RATIONALE: Skewness of price_level_clustering over 21d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(21).skew()

def ppsy_409_price_level_clustering_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_409_price_level_clustering_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_level_clustering over 21d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(21).kurt()

def ppsy_410_price_level_clustering_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_410_price_level_clustering_skew_63d
    ECONOMIC RATIONALE: Skewness of price_level_clustering over 63d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(63).skew()

def ppsy_411_price_level_clustering_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_411_price_level_clustering_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_level_clustering over 63d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(63).kurt()

def ppsy_412_price_level_clustering_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_412_price_level_clustering_skew_126d
    ECONOMIC RATIONALE: Skewness of price_level_clustering over 126d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(126).skew()

def ppsy_413_price_level_clustering_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_413_price_level_clustering_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_level_clustering over 126d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(126).kurt()

def ppsy_414_price_level_clustering_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_414_price_level_clustering_skew_252d
    ECONOMIC RATIONALE: Skewness of price_level_clustering over 252d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(252).skew()

def ppsy_415_price_level_clustering_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_415_price_level_clustering_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_level_clustering over 252d. Number of distinct price clusters recently visited.
    """
    return (close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))).rolling(252).kurt()

def ppsy_416_clustering_entropy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_416_clustering_entropy_skew_5d
    ECONOMIC RATIONALE: Skewness of clustering_entropy over 5d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(5).skew()

def ppsy_417_clustering_entropy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_417_clustering_entropy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of clustering_entropy over 5d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(5).kurt()

def ppsy_418_clustering_entropy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_418_clustering_entropy_skew_21d
    ECONOMIC RATIONALE: Skewness of clustering_entropy over 21d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(21).skew()

def ppsy_419_clustering_entropy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_419_clustering_entropy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of clustering_entropy over 21d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(21).kurt()

def ppsy_420_clustering_entropy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_420_clustering_entropy_skew_63d
    ECONOMIC RATIONALE: Skewness of clustering_entropy over 63d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(63).skew()

def ppsy_421_clustering_entropy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_421_clustering_entropy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of clustering_entropy over 63d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(63).kurt()

def ppsy_422_clustering_entropy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_422_clustering_entropy_skew_126d
    ECONOMIC RATIONALE: Skewness of clustering_entropy over 126d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(126).skew()

def ppsy_423_clustering_entropy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_423_clustering_entropy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of clustering_entropy over 126d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(126).kurt()

def ppsy_424_clustering_entropy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_424_clustering_entropy_skew_252d
    ECONOMIC RATIONALE: Skewness of clustering_entropy over 252d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(252).skew()

def ppsy_425_clustering_entropy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_425_clustering_entropy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of clustering_entropy over 252d. Entropy of price distribution across bins.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(252).kurt()

def ppsy_426_price_support_psych_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_426_price_support_psych_skew_5d
    ECONOMIC RATIONALE: Skewness of price_support_psych over 5d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(5).skew()

def ppsy_427_price_support_psych_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_427_price_support_psych_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_support_psych over 5d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(5).kurt()

def ppsy_428_price_support_psych_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_428_price_support_psych_skew_21d
    ECONOMIC RATIONALE: Skewness of price_support_psych over 21d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(21).skew()

def ppsy_429_price_support_psych_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_429_price_support_psych_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_support_psych over 21d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(21).kurt()

def ppsy_430_price_support_psych_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_430_price_support_psych_skew_63d
    ECONOMIC RATIONALE: Skewness of price_support_psych over 63d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(63).skew()

def ppsy_431_price_support_psych_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_431_price_support_psych_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_support_psych over 63d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(63).kurt()

def ppsy_432_price_support_psych_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_432_price_support_psych_skew_126d
    ECONOMIC RATIONALE: Skewness of price_support_psych over 126d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(126).skew()

def ppsy_433_price_support_psych_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_433_price_support_psych_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_support_psych over 126d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(126).kurt()

def ppsy_434_price_support_psych_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_434_price_support_psych_skew_252d
    ECONOMIC RATIONALE: Skewness of price_support_psych over 252d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(252).skew()

def ppsy_435_price_support_psych_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_435_price_support_psych_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_support_psych over 252d. Psychological anchoring to 52-week lows.
    """
    return (close / close.rolling(252).min() - 1 < 0.05).rolling(252).kurt()

def ppsy_436_price_resistance_psych_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_436_price_resistance_psych_skew_5d
    ECONOMIC RATIONALE: Skewness of price_resistance_psych over 5d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(5).skew()

def ppsy_437_price_resistance_psych_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_437_price_resistance_psych_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_resistance_psych over 5d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(5).kurt()

def ppsy_438_price_resistance_psych_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_438_price_resistance_psych_skew_21d
    ECONOMIC RATIONALE: Skewness of price_resistance_psych over 21d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(21).skew()

def ppsy_439_price_resistance_psych_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_439_price_resistance_psych_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_resistance_psych over 21d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(21).kurt()

def ppsy_440_price_resistance_psych_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_440_price_resistance_psych_skew_63d
    ECONOMIC RATIONALE: Skewness of price_resistance_psych over 63d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(63).skew()

def ppsy_441_price_resistance_psych_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_441_price_resistance_psych_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_resistance_psych over 63d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(63).kurt()

def ppsy_442_price_resistance_psych_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_442_price_resistance_psych_skew_126d
    ECONOMIC RATIONALE: Skewness of price_resistance_psych over 126d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(126).skew()

def ppsy_443_price_resistance_psych_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_443_price_resistance_psych_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_resistance_psych over 126d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(126).kurt()

def ppsy_444_price_resistance_psych_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_444_price_resistance_psych_skew_252d
    ECONOMIC RATIONALE: Skewness of price_resistance_psych over 252d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(252).skew()

def ppsy_445_price_resistance_psych_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_445_price_resistance_psych_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_resistance_psych over 252d. Psychological anchoring to 52-week highs.
    """
    return (close / close.rolling(252).max() - 1 > -0.05).rolling(252).kurt()

def ppsy_446_clustering_zscore_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_446_clustering_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of clustering_zscore over 5d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(5).skew()

def ppsy_447_clustering_zscore_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_447_clustering_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of clustering_zscore over 5d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(5).kurt()

def ppsy_448_clustering_zscore_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_448_clustering_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of clustering_zscore over 21d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(21).skew()

def ppsy_449_clustering_zscore_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_449_clustering_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of clustering_zscore over 21d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(21).kurt()

def ppsy_450_clustering_zscore_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_450_clustering_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of clustering_zscore over 63d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(63).skew()

def ppsy_451_clustering_zscore_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_451_clustering_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of clustering_zscore over 63d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(63).kurt()

def ppsy_452_clustering_zscore_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_452_clustering_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of clustering_zscore over 126d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(126).skew()

def ppsy_453_clustering_zscore_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_453_clustering_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of clustering_zscore over 126d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(126).kurt()

def ppsy_454_clustering_zscore_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_454_clustering_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of clustering_zscore over 252d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(252).skew()

def ppsy_455_clustering_zscore_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_455_clustering_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of clustering_zscore over 252d. Anomaly in price digit distribution.
    """
    return (_zscore_rolling(close % 1.0, 252)).rolling(252).kurt()

def ppsy_456_digit_bias_last_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_456_digit_bias_last_skew_5d
    ECONOMIC RATIONALE: Skewness of digit_bias_last over 5d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(5).skew()

def ppsy_457_digit_bias_last_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_457_digit_bias_last_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of digit_bias_last over 5d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(5).kurt()

def ppsy_458_digit_bias_last_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_458_digit_bias_last_skew_21d
    ECONOMIC RATIONALE: Skewness of digit_bias_last over 21d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(21).skew()

def ppsy_459_digit_bias_last_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_459_digit_bias_last_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of digit_bias_last over 21d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(21).kurt()

def ppsy_460_digit_bias_last_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_460_digit_bias_last_skew_63d
    ECONOMIC RATIONALE: Skewness of digit_bias_last over 63d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(63).skew()

def ppsy_461_digit_bias_last_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_461_digit_bias_last_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of digit_bias_last over 63d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(63).kurt()

def ppsy_462_digit_bias_last_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_462_digit_bias_last_skew_126d
    ECONOMIC RATIONALE: Skewness of digit_bias_last over 126d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(126).skew()

def ppsy_463_digit_bias_last_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_463_digit_bias_last_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of digit_bias_last over 126d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(126).kurt()

def ppsy_464_digit_bias_last_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_464_digit_bias_last_skew_252d
    ECONOMIC RATIONALE: Skewness of digit_bias_last over 252d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(252).skew()

def ppsy_465_digit_bias_last_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_465_digit_bias_last_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of digit_bias_last over 252d. Bias in the final cent digit.
    """
    return ((close * 100 % 10).rolling(63).mean()).rolling(252).kurt()

def ppsy_466_price_magnet_effect_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_466_price_magnet_effect_skew_5d
    ECONOMIC RATIONALE: Skewness of price_magnet_effect over 5d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(5).skew()

def ppsy_467_price_magnet_effect_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_467_price_magnet_effect_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_magnet_effect over 5d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(5).kurt()

def ppsy_468_price_magnet_effect_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_468_price_magnet_effect_skew_21d
    ECONOMIC RATIONALE: Skewness of price_magnet_effect over 21d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(21).skew()

def ppsy_469_price_magnet_effect_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_469_price_magnet_effect_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_magnet_effect over 21d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(21).kurt()

def ppsy_470_price_magnet_effect_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_470_price_magnet_effect_skew_63d
    ECONOMIC RATIONALE: Skewness of price_magnet_effect over 63d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(63).skew()

def ppsy_471_price_magnet_effect_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_471_price_magnet_effect_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_magnet_effect over 63d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(63).kurt()

def ppsy_472_price_magnet_effect_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_472_price_magnet_effect_skew_126d
    ECONOMIC RATIONALE: Skewness of price_magnet_effect over 126d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(126).skew()

def ppsy_473_price_magnet_effect_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_473_price_magnet_effect_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_magnet_effect over 126d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(126).kurt()

def ppsy_474_price_magnet_effect_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_474_price_magnet_effect_skew_252d
    ECONOMIC RATIONALE: Skewness of price_magnet_effect over 252d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(252).skew()

def ppsy_475_price_magnet_effect_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_475_price_magnet_effect_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_magnet_effect over 252d. Attraction to nearest whole number.
    """
    return (abs(close - round(close))).rolling(252).kurt()

def ppsy_476_clustering_regime_shift_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_476_clustering_regime_shift_skew_5d
    ECONOMIC RATIONALE: Skewness of clustering_regime_shift over 5d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(5).skew()

def ppsy_477_clustering_regime_shift_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_477_clustering_regime_shift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of clustering_regime_shift over 5d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(5).kurt()

def ppsy_478_clustering_regime_shift_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_478_clustering_regime_shift_skew_21d
    ECONOMIC RATIONALE: Skewness of clustering_regime_shift over 21d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(21).skew()

def ppsy_479_clustering_regime_shift_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_479_clustering_regime_shift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of clustering_regime_shift over 21d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(21).kurt()

def ppsy_480_clustering_regime_shift_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_480_clustering_regime_shift_skew_63d
    ECONOMIC RATIONALE: Skewness of clustering_regime_shift over 63d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(63).skew()

def ppsy_481_clustering_regime_shift_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_481_clustering_regime_shift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of clustering_regime_shift over 63d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(63).kurt()

def ppsy_482_clustering_regime_shift_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_482_clustering_regime_shift_skew_126d
    ECONOMIC RATIONALE: Skewness of clustering_regime_shift over 126d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(126).skew()

def ppsy_483_clustering_regime_shift_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_483_clustering_regime_shift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of clustering_regime_shift over 126d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(126).kurt()

def ppsy_484_clustering_regime_shift_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_484_clustering_regime_shift_skew_252d
    ECONOMIC RATIONALE: Skewness of clustering_regime_shift over 252d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(252).skew()

def ppsy_485_clustering_regime_shift_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_485_clustering_regime_shift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of clustering_regime_shift over 252d. Shift in price stability around clusters.
    """
    return (close.rolling(21).std().diff(21)).rolling(252).kurt()

def ppsy_486_psychological_breakthrough_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_486_psychological_breakthrough_skew_5d
    ECONOMIC RATIONALE: Skewness of psychological_breakthrough over 5d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(5).skew()

def ppsy_487_psychological_breakthrough_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_487_psychological_breakthrough_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of psychological_breakthrough over 5d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(5).kurt()

def ppsy_488_psychological_breakthrough_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_488_psychological_breakthrough_skew_21d
    ECONOMIC RATIONALE: Skewness of psychological_breakthrough over 21d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(21).skew()

def ppsy_489_psychological_breakthrough_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_489_psychological_breakthrough_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of psychological_breakthrough over 21d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(21).kurt()

def ppsy_490_psychological_breakthrough_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_490_psychological_breakthrough_skew_63d
    ECONOMIC RATIONALE: Skewness of psychological_breakthrough over 63d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(63).skew()

def ppsy_491_psychological_breakthrough_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_491_psychological_breakthrough_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of psychological_breakthrough over 63d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(63).kurt()

def ppsy_492_psychological_breakthrough_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_492_psychological_breakthrough_skew_126d
    ECONOMIC RATIONALE: Skewness of psychological_breakthrough over 126d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(126).skew()

def ppsy_493_psychological_breakthrough_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_493_psychological_breakthrough_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of psychological_breakthrough over 126d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(126).kurt()

def ppsy_494_psychological_breakthrough_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_494_psychological_breakthrough_skew_252d
    ECONOMIC RATIONALE: Skewness of psychological_breakthrough over 252d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(252).skew()

def ppsy_495_psychological_breakthrough_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_495_psychological_breakthrough_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of psychological_breakthrough over 252d. Crossing of psychological whole-number barriers.
    """
    return ((close.shift(1) < round(close.shift(1))) & (close > round(close.shift(1)))).rolling(252).kurt()

def ppsy_496_price_stickiness_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_496_price_stickiness_skew_5d
    ECONOMIC RATIONALE: Skewness of price_stickiness over 5d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(5).skew()

def ppsy_497_price_stickiness_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_497_price_stickiness_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness over 5d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(5).kurt()

def ppsy_498_price_stickiness_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_498_price_stickiness_skew_21d
    ECONOMIC RATIONALE: Skewness of price_stickiness over 21d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(21).skew()

def ppsy_499_price_stickiness_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_499_price_stickiness_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness over 21d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(21).kurt()

def ppsy_500_price_stickiness_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_500_price_stickiness_skew_63d
    ECONOMIC RATIONALE: Skewness of price_stickiness over 63d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(63).skew()

def ppsy_501_price_stickiness_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_501_price_stickiness_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness over 63d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(63).kurt()

def ppsy_502_price_stickiness_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_502_price_stickiness_skew_126d
    ECONOMIC RATIONALE: Skewness of price_stickiness over 126d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(126).skew()

def ppsy_503_price_stickiness_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_503_price_stickiness_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness over 126d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(126).kurt()

def ppsy_504_price_stickiness_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_504_price_stickiness_skew_252d
    ECONOMIC RATIONALE: Skewness of price_stickiness over 252d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(252).skew()

def ppsy_505_price_stickiness_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_505_price_stickiness_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness over 252d. Frequency of minimal price movement (price stickiness).
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).sum()).rolling(252).kurt()

def ppsy_506_clustering_vol_corr_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_506_clustering_vol_corr_skew_5d
    ECONOMIC RATIONALE: Skewness of clustering_vol_corr over 5d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(5).skew()

def ppsy_507_clustering_vol_corr_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_507_clustering_vol_corr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of clustering_vol_corr over 5d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(5).kurt()

def ppsy_508_clustering_vol_corr_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_508_clustering_vol_corr_skew_21d
    ECONOMIC RATIONALE: Skewness of clustering_vol_corr over 21d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(21).skew()

def ppsy_509_clustering_vol_corr_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_509_clustering_vol_corr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of clustering_vol_corr over 21d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(21).kurt()

def ppsy_510_clustering_vol_corr_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_510_clustering_vol_corr_skew_63d
    ECONOMIC RATIONALE: Skewness of clustering_vol_corr over 63d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(63).skew()

def ppsy_511_clustering_vol_corr_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_511_clustering_vol_corr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of clustering_vol_corr over 63d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(63).kurt()

def ppsy_512_clustering_vol_corr_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_512_clustering_vol_corr_skew_126d
    ECONOMIC RATIONALE: Skewness of clustering_vol_corr over 126d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(126).skew()

def ppsy_513_clustering_vol_corr_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_513_clustering_vol_corr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of clustering_vol_corr over 126d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(126).kurt()

def ppsy_514_clustering_vol_corr_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_514_clustering_vol_corr_skew_252d
    ECONOMIC RATIONALE: Skewness of clustering_vol_corr over 252d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(252).skew()

def ppsy_515_clustering_vol_corr_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_515_clustering_vol_corr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of clustering_vol_corr over 252d. Correlation of volume with round-number proximity.
    """
    return (volume.rolling(21).corr(close % 1.0)).rolling(252).kurt()

def ppsy_516_psych_exhaustion_proxy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_516_psych_exhaustion_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of psych_exhaustion_proxy over 5d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(5).skew()

def ppsy_517_psych_exhaustion_proxy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_517_psych_exhaustion_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of psych_exhaustion_proxy over 5d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(5).kurt()

def ppsy_518_psych_exhaustion_proxy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_518_psych_exhaustion_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of psych_exhaustion_proxy over 21d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(21).skew()

def ppsy_519_psych_exhaustion_proxy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_519_psych_exhaustion_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of psych_exhaustion_proxy over 21d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(21).kurt()

def ppsy_520_psych_exhaustion_proxy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_520_psych_exhaustion_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of psych_exhaustion_proxy over 63d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(63).skew()

def ppsy_521_psych_exhaustion_proxy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_521_psych_exhaustion_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of psych_exhaustion_proxy over 63d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(63).kurt()

def ppsy_522_psych_exhaustion_proxy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_522_psych_exhaustion_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of psych_exhaustion_proxy over 126d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(126).skew()

def ppsy_523_psych_exhaustion_proxy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_523_psych_exhaustion_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of psych_exhaustion_proxy over 126d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(126).kurt()

def ppsy_524_psych_exhaustion_proxy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_524_psych_exhaustion_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of psych_exhaustion_proxy over 252d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(252).skew()

def ppsy_525_psych_exhaustion_proxy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_525_psych_exhaustion_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of psych_exhaustion_proxy over 252d. Persistent hovering near round numbers.
    """
    return ((close % 1.0 < 0.05).rolling(10).sum()).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V117_REGISTRY_MOMENTS = {
    "ppsy_376_round_number_proximity_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_376_round_number_proximity_skew_5d},
    "ppsy_377_round_number_proximity_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_377_round_number_proximity_kurt_5d},
    "ppsy_378_round_number_proximity_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_378_round_number_proximity_skew_21d},
    "ppsy_379_round_number_proximity_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_379_round_number_proximity_kurt_21d},
    "ppsy_380_round_number_proximity_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_380_round_number_proximity_skew_63d},
    "ppsy_381_round_number_proximity_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_381_round_number_proximity_kurt_63d},
    "ppsy_382_round_number_proximity_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_382_round_number_proximity_skew_126d},
    "ppsy_383_round_number_proximity_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_383_round_number_proximity_kurt_126d},
    "ppsy_384_round_number_proximity_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_384_round_number_proximity_skew_252d},
    "ppsy_385_round_number_proximity_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_385_round_number_proximity_kurt_252d},
    "ppsy_386_decade_number_proximity_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_386_decade_number_proximity_skew_5d},
    "ppsy_387_decade_number_proximity_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_387_decade_number_proximity_kurt_5d},
    "ppsy_388_decade_number_proximity_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_388_decade_number_proximity_skew_21d},
    "ppsy_389_decade_number_proximity_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_389_decade_number_proximity_kurt_21d},
    "ppsy_390_decade_number_proximity_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_390_decade_number_proximity_skew_63d},
    "ppsy_391_decade_number_proximity_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_391_decade_number_proximity_kurt_63d},
    "ppsy_392_decade_number_proximity_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_392_decade_number_proximity_skew_126d},
    "ppsy_393_decade_number_proximity_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_393_decade_number_proximity_kurt_126d},
    "ppsy_394_decade_number_proximity_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_394_decade_number_proximity_skew_252d},
    "ppsy_395_decade_number_proximity_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_395_decade_number_proximity_kurt_252d},
    "ppsy_396_century_number_proximity_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_396_century_number_proximity_skew_5d},
    "ppsy_397_century_number_proximity_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_397_century_number_proximity_kurt_5d},
    "ppsy_398_century_number_proximity_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_398_century_number_proximity_skew_21d},
    "ppsy_399_century_number_proximity_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_399_century_number_proximity_kurt_21d},
    "ppsy_400_century_number_proximity_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_400_century_number_proximity_skew_63d},
    "ppsy_401_century_number_proximity_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_401_century_number_proximity_kurt_63d},
    "ppsy_402_century_number_proximity_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_402_century_number_proximity_skew_126d},
    "ppsy_403_century_number_proximity_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_403_century_number_proximity_kurt_126d},
    "ppsy_404_century_number_proximity_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_404_century_number_proximity_skew_252d},
    "ppsy_405_century_number_proximity_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_405_century_number_proximity_kurt_252d},
    "ppsy_406_price_level_clustering_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_406_price_level_clustering_skew_5d},
    "ppsy_407_price_level_clustering_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_407_price_level_clustering_kurt_5d},
    "ppsy_408_price_level_clustering_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_408_price_level_clustering_skew_21d},
    "ppsy_409_price_level_clustering_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_409_price_level_clustering_kurt_21d},
    "ppsy_410_price_level_clustering_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_410_price_level_clustering_skew_63d},
    "ppsy_411_price_level_clustering_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_411_price_level_clustering_kurt_63d},
    "ppsy_412_price_level_clustering_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_412_price_level_clustering_skew_126d},
    "ppsy_413_price_level_clustering_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_413_price_level_clustering_kurt_126d},
    "ppsy_414_price_level_clustering_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_414_price_level_clustering_skew_252d},
    "ppsy_415_price_level_clustering_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_415_price_level_clustering_kurt_252d},
    "ppsy_416_clustering_entropy_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_416_clustering_entropy_skew_5d},
    "ppsy_417_clustering_entropy_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_417_clustering_entropy_kurt_5d},
    "ppsy_418_clustering_entropy_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_418_clustering_entropy_skew_21d},
    "ppsy_419_clustering_entropy_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_419_clustering_entropy_kurt_21d},
    "ppsy_420_clustering_entropy_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_420_clustering_entropy_skew_63d},
    "ppsy_421_clustering_entropy_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_421_clustering_entropy_kurt_63d},
    "ppsy_422_clustering_entropy_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_422_clustering_entropy_skew_126d},
    "ppsy_423_clustering_entropy_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_423_clustering_entropy_kurt_126d},
    "ppsy_424_clustering_entropy_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_424_clustering_entropy_skew_252d},
    "ppsy_425_clustering_entropy_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_425_clustering_entropy_kurt_252d},
    "ppsy_426_price_support_psych_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_426_price_support_psych_skew_5d},
    "ppsy_427_price_support_psych_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_427_price_support_psych_kurt_5d},
    "ppsy_428_price_support_psych_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_428_price_support_psych_skew_21d},
    "ppsy_429_price_support_psych_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_429_price_support_psych_kurt_21d},
    "ppsy_430_price_support_psych_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_430_price_support_psych_skew_63d},
    "ppsy_431_price_support_psych_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_431_price_support_psych_kurt_63d},
    "ppsy_432_price_support_psych_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_432_price_support_psych_skew_126d},
    "ppsy_433_price_support_psych_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_433_price_support_psych_kurt_126d},
    "ppsy_434_price_support_psych_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_434_price_support_psych_skew_252d},
    "ppsy_435_price_support_psych_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_435_price_support_psych_kurt_252d},
    "ppsy_436_price_resistance_psych_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_436_price_resistance_psych_skew_5d},
    "ppsy_437_price_resistance_psych_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_437_price_resistance_psych_kurt_5d},
    "ppsy_438_price_resistance_psych_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_438_price_resistance_psych_skew_21d},
    "ppsy_439_price_resistance_psych_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_439_price_resistance_psych_kurt_21d},
    "ppsy_440_price_resistance_psych_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_440_price_resistance_psych_skew_63d},
    "ppsy_441_price_resistance_psych_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_441_price_resistance_psych_kurt_63d},
    "ppsy_442_price_resistance_psych_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_442_price_resistance_psych_skew_126d},
    "ppsy_443_price_resistance_psych_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_443_price_resistance_psych_kurt_126d},
    "ppsy_444_price_resistance_psych_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_444_price_resistance_psych_skew_252d},
    "ppsy_445_price_resistance_psych_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_445_price_resistance_psych_kurt_252d},
    "ppsy_446_clustering_zscore_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_446_clustering_zscore_skew_5d},
    "ppsy_447_clustering_zscore_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_447_clustering_zscore_kurt_5d},
    "ppsy_448_clustering_zscore_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_448_clustering_zscore_skew_21d},
    "ppsy_449_clustering_zscore_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_449_clustering_zscore_kurt_21d},
    "ppsy_450_clustering_zscore_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_450_clustering_zscore_skew_63d},
    "ppsy_451_clustering_zscore_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_451_clustering_zscore_kurt_63d},
    "ppsy_452_clustering_zscore_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_452_clustering_zscore_skew_126d},
    "ppsy_453_clustering_zscore_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_453_clustering_zscore_kurt_126d},
    "ppsy_454_clustering_zscore_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_454_clustering_zscore_skew_252d},
    "ppsy_455_clustering_zscore_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_455_clustering_zscore_kurt_252d},
    "ppsy_456_digit_bias_last_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_456_digit_bias_last_skew_5d},
    "ppsy_457_digit_bias_last_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_457_digit_bias_last_kurt_5d},
    "ppsy_458_digit_bias_last_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_458_digit_bias_last_skew_21d},
    "ppsy_459_digit_bias_last_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_459_digit_bias_last_kurt_21d},
    "ppsy_460_digit_bias_last_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_460_digit_bias_last_skew_63d},
    "ppsy_461_digit_bias_last_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_461_digit_bias_last_kurt_63d},
    "ppsy_462_digit_bias_last_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_462_digit_bias_last_skew_126d},
    "ppsy_463_digit_bias_last_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_463_digit_bias_last_kurt_126d},
    "ppsy_464_digit_bias_last_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_464_digit_bias_last_skew_252d},
    "ppsy_465_digit_bias_last_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_465_digit_bias_last_kurt_252d},
    "ppsy_466_price_magnet_effect_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_466_price_magnet_effect_skew_5d},
    "ppsy_467_price_magnet_effect_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_467_price_magnet_effect_kurt_5d},
    "ppsy_468_price_magnet_effect_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_468_price_magnet_effect_skew_21d},
    "ppsy_469_price_magnet_effect_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_469_price_magnet_effect_kurt_21d},
    "ppsy_470_price_magnet_effect_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_470_price_magnet_effect_skew_63d},
    "ppsy_471_price_magnet_effect_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_471_price_magnet_effect_kurt_63d},
    "ppsy_472_price_magnet_effect_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_472_price_magnet_effect_skew_126d},
    "ppsy_473_price_magnet_effect_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_473_price_magnet_effect_kurt_126d},
    "ppsy_474_price_magnet_effect_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_474_price_magnet_effect_skew_252d},
    "ppsy_475_price_magnet_effect_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_475_price_magnet_effect_kurt_252d},
    "ppsy_476_clustering_regime_shift_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_476_clustering_regime_shift_skew_5d},
    "ppsy_477_clustering_regime_shift_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_477_clustering_regime_shift_kurt_5d},
    "ppsy_478_clustering_regime_shift_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_478_clustering_regime_shift_skew_21d},
    "ppsy_479_clustering_regime_shift_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_479_clustering_regime_shift_kurt_21d},
    "ppsy_480_clustering_regime_shift_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_480_clustering_regime_shift_skew_63d},
    "ppsy_481_clustering_regime_shift_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_481_clustering_regime_shift_kurt_63d},
    "ppsy_482_clustering_regime_shift_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_482_clustering_regime_shift_skew_126d},
    "ppsy_483_clustering_regime_shift_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_483_clustering_regime_shift_kurt_126d},
    "ppsy_484_clustering_regime_shift_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_484_clustering_regime_shift_skew_252d},
    "ppsy_485_clustering_regime_shift_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_485_clustering_regime_shift_kurt_252d},
    "ppsy_486_psychological_breakthrough_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_486_psychological_breakthrough_skew_5d},
    "ppsy_487_psychological_breakthrough_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_487_psychological_breakthrough_kurt_5d},
    "ppsy_488_psychological_breakthrough_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_488_psychological_breakthrough_skew_21d},
    "ppsy_489_psychological_breakthrough_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_489_psychological_breakthrough_kurt_21d},
    "ppsy_490_psychological_breakthrough_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_490_psychological_breakthrough_skew_63d},
    "ppsy_491_psychological_breakthrough_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_491_psychological_breakthrough_kurt_63d},
    "ppsy_492_psychological_breakthrough_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_492_psychological_breakthrough_skew_126d},
    "ppsy_493_psychological_breakthrough_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_493_psychological_breakthrough_kurt_126d},
    "ppsy_494_psychological_breakthrough_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_494_psychological_breakthrough_skew_252d},
    "ppsy_495_psychological_breakthrough_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_495_psychological_breakthrough_kurt_252d},
    "ppsy_496_price_stickiness_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_496_price_stickiness_skew_5d},
    "ppsy_497_price_stickiness_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_497_price_stickiness_kurt_5d},
    "ppsy_498_price_stickiness_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_498_price_stickiness_skew_21d},
    "ppsy_499_price_stickiness_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_499_price_stickiness_kurt_21d},
    "ppsy_500_price_stickiness_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_500_price_stickiness_skew_63d},
    "ppsy_501_price_stickiness_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_501_price_stickiness_kurt_63d},
    "ppsy_502_price_stickiness_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_502_price_stickiness_skew_126d},
    "ppsy_503_price_stickiness_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_503_price_stickiness_kurt_126d},
    "ppsy_504_price_stickiness_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_504_price_stickiness_skew_252d},
    "ppsy_505_price_stickiness_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_505_price_stickiness_kurt_252d},
    "ppsy_506_clustering_vol_corr_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_506_clustering_vol_corr_skew_5d},
    "ppsy_507_clustering_vol_corr_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_507_clustering_vol_corr_kurt_5d},
    "ppsy_508_clustering_vol_corr_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_508_clustering_vol_corr_skew_21d},
    "ppsy_509_clustering_vol_corr_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_509_clustering_vol_corr_kurt_21d},
    "ppsy_510_clustering_vol_corr_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_510_clustering_vol_corr_skew_63d},
    "ppsy_511_clustering_vol_corr_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_511_clustering_vol_corr_kurt_63d},
    "ppsy_512_clustering_vol_corr_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_512_clustering_vol_corr_skew_126d},
    "ppsy_513_clustering_vol_corr_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_513_clustering_vol_corr_kurt_126d},
    "ppsy_514_clustering_vol_corr_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_514_clustering_vol_corr_skew_252d},
    "ppsy_515_clustering_vol_corr_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_515_clustering_vol_corr_kurt_252d},
    "ppsy_516_psych_exhaustion_proxy_skew_5d": {"inputs": ["close", "volume"], "func": ppsy_516_psych_exhaustion_proxy_skew_5d},
    "ppsy_517_psych_exhaustion_proxy_kurt_5d": {"inputs": ["close", "volume"], "func": ppsy_517_psych_exhaustion_proxy_kurt_5d},
    "ppsy_518_psych_exhaustion_proxy_skew_21d": {"inputs": ["close", "volume"], "func": ppsy_518_psych_exhaustion_proxy_skew_21d},
    "ppsy_519_psych_exhaustion_proxy_kurt_21d": {"inputs": ["close", "volume"], "func": ppsy_519_psych_exhaustion_proxy_kurt_21d},
    "ppsy_520_psych_exhaustion_proxy_skew_63d": {"inputs": ["close", "volume"], "func": ppsy_520_psych_exhaustion_proxy_skew_63d},
    "ppsy_521_psych_exhaustion_proxy_kurt_63d": {"inputs": ["close", "volume"], "func": ppsy_521_psych_exhaustion_proxy_kurt_63d},
    "ppsy_522_psych_exhaustion_proxy_skew_126d": {"inputs": ["close", "volume"], "func": ppsy_522_psych_exhaustion_proxy_skew_126d},
    "ppsy_523_psych_exhaustion_proxy_kurt_126d": {"inputs": ["close", "volume"], "func": ppsy_523_psych_exhaustion_proxy_kurt_126d},
    "ppsy_524_psych_exhaustion_proxy_skew_252d": {"inputs": ["close", "volume"], "func": ppsy_524_psych_exhaustion_proxy_skew_252d},
    "ppsy_525_psych_exhaustion_proxy_kurt_252d": {"inputs": ["close", "volume"], "func": ppsy_525_psych_exhaustion_proxy_kurt_252d},
}
