"""
115_volatility_term_structure — Statistical Moments
Domain: volatility_term_structure
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

def vts_376_vol_5d_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_376_vol_5d_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_5d over 5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(5).skew()

def vts_377_vol_5d_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_377_vol_5d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_5d over 5d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(5).kurt()

def vts_378_vol_5d_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_378_vol_5d_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_5d over 21d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(21).skew()

def vts_379_vol_5d_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_379_vol_5d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_5d over 21d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(21).kurt()

def vts_380_vol_5d_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_380_vol_5d_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_5d over 63d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(63).skew()

def vts_381_vol_5d_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_381_vol_5d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_5d over 63d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(63).kurt()

def vts_382_vol_5d_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_382_vol_5d_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_5d over 126d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(126).skew()

def vts_383_vol_5d_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_383_vol_5d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_5d over 126d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(126).kurt()

def vts_384_vol_5d_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_384_vol_5d_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_5d over 252d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(252).skew()

def vts_385_vol_5d_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_385_vol_5d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_5d over 252d. Short-term realized volatility.
    """
    return (close.pct_change(1).rolling(5).std()).rolling(252).kurt()

def vts_386_vol_21d_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_386_vol_21d_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_21d over 5d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(5).skew()

def vts_387_vol_21d_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_387_vol_21d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_21d over 5d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(5).kurt()

def vts_388_vol_21d_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_388_vol_21d_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_21d over 21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(21).skew()

def vts_389_vol_21d_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_389_vol_21d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_21d over 21d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(21).kurt()

def vts_390_vol_21d_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_390_vol_21d_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_21d over 63d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(63).skew()

def vts_391_vol_21d_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_391_vol_21d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_21d over 63d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(63).kurt()

def vts_392_vol_21d_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_392_vol_21d_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_21d over 126d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(126).skew()

def vts_393_vol_21d_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_393_vol_21d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_21d over 126d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(126).kurt()

def vts_394_vol_21d_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_394_vol_21d_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_21d over 252d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(252).skew()

def vts_395_vol_21d_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_395_vol_21d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_21d over 252d. Monthly realized volatility.
    """
    return (close.pct_change(1).rolling(21).std()).rolling(252).kurt()

def vts_396_vol_63d_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_396_vol_63d_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_63d over 5d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(5).skew()

def vts_397_vol_63d_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_397_vol_63d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_63d over 5d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(5).kurt()

def vts_398_vol_63d_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_398_vol_63d_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_63d over 21d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(21).skew()

def vts_399_vol_63d_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_399_vol_63d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_63d over 21d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(21).kurt()

def vts_400_vol_63d_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_400_vol_63d_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_63d over 63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(63).skew()

def vts_401_vol_63d_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_401_vol_63d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_63d over 63d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(63).kurt()

def vts_402_vol_63d_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_402_vol_63d_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_63d over 126d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(126).skew()

def vts_403_vol_63d_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_403_vol_63d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_63d over 126d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(126).kurt()

def vts_404_vol_63d_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_404_vol_63d_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_63d over 252d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(252).skew()

def vts_405_vol_63d_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_405_vol_63d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_63d over 252d. Quarterly realized volatility.
    """
    return (close.pct_change(1).rolling(63).std()).rolling(252).kurt()

def vts_406_vol_spread_short_long_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_406_vol_spread_short_long_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_spread_short_long over 5d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(5).skew()

def vts_407_vol_spread_short_long_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_407_vol_spread_short_long_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_spread_short_long over 5d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(5).kurt()

def vts_408_vol_spread_short_long_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_408_vol_spread_short_long_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_spread_short_long over 21d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(21).skew()

def vts_409_vol_spread_short_long_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_409_vol_spread_short_long_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_spread_short_long over 21d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(21).kurt()

def vts_410_vol_spread_short_long_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_410_vol_spread_short_long_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_spread_short_long over 63d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(63).skew()

def vts_411_vol_spread_short_long_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_411_vol_spread_short_long_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_spread_short_long over 63d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(63).kurt()

def vts_412_vol_spread_short_long_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_412_vol_spread_short_long_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_spread_short_long over 126d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(126).skew()

def vts_413_vol_spread_short_long_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_413_vol_spread_short_long_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_spread_short_long over 126d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(126).kurt()

def vts_414_vol_spread_short_long_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_414_vol_spread_short_long_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_spread_short_long over 252d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(252).skew()

def vts_415_vol_spread_short_long_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_415_vol_spread_short_long_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_spread_short_long over 252d. Spread between short and long term volatility.
    """
    return (close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()).rolling(252).kurt()

def vts_416_vol_term_slope_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_416_vol_term_slope_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_term_slope over 5d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(5).skew()

def vts_417_vol_term_slope_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_417_vol_term_slope_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_term_slope over 5d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(5).kurt()

def vts_418_vol_term_slope_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_418_vol_term_slope_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_term_slope over 21d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(21).skew()

def vts_419_vol_term_slope_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_419_vol_term_slope_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_term_slope over 21d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(21).kurt()

def vts_420_vol_term_slope_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_420_vol_term_slope_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_term_slope over 63d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(63).skew()

def vts_421_vol_term_slope_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_421_vol_term_slope_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_term_slope over 63d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(63).kurt()

def vts_422_vol_term_slope_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_422_vol_term_slope_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_term_slope over 126d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(126).skew()

def vts_423_vol_term_slope_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_423_vol_term_slope_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_term_slope over 126d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(126).kurt()

def vts_424_vol_term_slope_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_424_vol_term_slope_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_term_slope over 252d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(252).skew()

def vts_425_vol_term_slope_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_425_vol_term_slope_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_term_slope over 252d. Slope of the volatility term structure.
    """
    return ((close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231).rolling(252).kurt()

def vts_426_vol_convexity_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_426_vol_convexity_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_convexity over 5d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(5).skew()

def vts_427_vol_convexity_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_427_vol_convexity_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_convexity over 5d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(5).kurt()

def vts_428_vol_convexity_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_428_vol_convexity_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_convexity over 21d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(21).skew()

def vts_429_vol_convexity_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_429_vol_convexity_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_convexity over 21d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(21).kurt()

def vts_430_vol_convexity_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_430_vol_convexity_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_convexity over 63d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(63).skew()

def vts_431_vol_convexity_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_431_vol_convexity_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_convexity over 63d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(63).kurt()

def vts_432_vol_convexity_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_432_vol_convexity_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_convexity over 126d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(126).skew()

def vts_433_vol_convexity_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_433_vol_convexity_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_convexity over 126d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(126).kurt()

def vts_434_vol_convexity_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_434_vol_convexity_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_convexity over 252d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(252).skew()

def vts_435_vol_convexity_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_435_vol_convexity_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_convexity over 252d. Change in the rate of volatility change.
    """
    return (close.pct_change(1).rolling(21).std().diff(1).diff(1)).rolling(252).kurt()

def vts_436_vol_mean_reversion_speed_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_436_vol_mean_reversion_speed_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_speed over 5d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(5).skew()

def vts_437_vol_mean_reversion_speed_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_437_vol_mean_reversion_speed_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_speed over 5d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(5).kurt()

def vts_438_vol_mean_reversion_speed_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_438_vol_mean_reversion_speed_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_speed over 21d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(21).skew()

def vts_439_vol_mean_reversion_speed_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_439_vol_mean_reversion_speed_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_speed over 21d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(21).kurt()

def vts_440_vol_mean_reversion_speed_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_440_vol_mean_reversion_speed_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_speed over 63d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(63).skew()

def vts_441_vol_mean_reversion_speed_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_441_vol_mean_reversion_speed_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_speed over 63d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(63).kurt()

def vts_442_vol_mean_reversion_speed_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_442_vol_mean_reversion_speed_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_speed over 126d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(126).skew()

def vts_443_vol_mean_reversion_speed_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_443_vol_mean_reversion_speed_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_speed over 126d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(126).kurt()

def vts_444_vol_mean_reversion_speed_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_444_vol_mean_reversion_speed_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_mean_reversion_speed over 252d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(252).skew()

def vts_445_vol_mean_reversion_speed_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_445_vol_mean_reversion_speed_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_mean_reversion_speed over 252d. Distance from long-term volatility mean.
    """
    return ((close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()).rolling(252).kurt()

def vts_446_vol_regime_z_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_446_vol_regime_z_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_regime_z over 5d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(5).skew()

def vts_447_vol_regime_z_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_447_vol_regime_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_z over 5d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(5).kurt()

def vts_448_vol_regime_z_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_448_vol_regime_z_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_regime_z over 21d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(21).skew()

def vts_449_vol_regime_z_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_449_vol_regime_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_z over 21d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(21).kurt()

def vts_450_vol_regime_z_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_450_vol_regime_z_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_regime_z over 63d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(63).skew()

def vts_451_vol_regime_z_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_451_vol_regime_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_z over 63d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(63).kurt()

def vts_452_vol_regime_z_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_452_vol_regime_z_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_regime_z over 126d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(126).skew()

def vts_453_vol_regime_z_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_453_vol_regime_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_z over 126d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(126).kurt()

def vts_454_vol_regime_z_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_454_vol_regime_z_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_regime_z over 252d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(252).skew()

def vts_455_vol_regime_z_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_455_vol_regime_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_regime_z over 252d. Z-score of current volatility regime.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).std(), 252)).rolling(252).kurt()

def vts_456_vol_acceleration_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_456_vol_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_acceleration over 5d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(5).skew()

def vts_457_vol_acceleration_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_457_vol_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_acceleration over 5d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(5).kurt()

def vts_458_vol_acceleration_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_458_vol_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_acceleration over 21d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(21).skew()

def vts_459_vol_acceleration_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_459_vol_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_acceleration over 21d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(21).kurt()

def vts_460_vol_acceleration_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_460_vol_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_acceleration over 63d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(63).skew()

def vts_461_vol_acceleration_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_461_vol_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_acceleration over 63d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(63).kurt()

def vts_462_vol_acceleration_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_462_vol_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_acceleration over 126d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(126).skew()

def vts_463_vol_acceleration_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_463_vol_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_acceleration over 126d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(126).kurt()

def vts_464_vol_acceleration_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_464_vol_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_acceleration over 252d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(252).skew()

def vts_465_vol_acceleration_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_465_vol_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_acceleration over 252d. Recent acceleration in realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().pct_change(5)).rolling(252).kurt()

def vts_466_vol_of_vol_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_466_vol_of_vol_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_of_vol over 5d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(5).skew()

def vts_467_vol_of_vol_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_467_vol_of_vol_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_of_vol over 5d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(5).kurt()

def vts_468_vol_of_vol_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_468_vol_of_vol_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_of_vol over 21d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(21).skew()

def vts_469_vol_of_vol_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_469_vol_of_vol_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_of_vol over 21d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(21).kurt()

def vts_470_vol_of_vol_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_470_vol_of_vol_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_of_vol over 63d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(63).skew()

def vts_471_vol_of_vol_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_471_vol_of_vol_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_of_vol over 63d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(63).kurt()

def vts_472_vol_of_vol_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_472_vol_of_vol_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_of_vol over 126d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(126).skew()

def vts_473_vol_of_vol_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_473_vol_of_vol_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_of_vol over 126d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(126).kurt()

def vts_474_vol_of_vol_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_474_vol_of_vol_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_of_vol over 252d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(252).skew()

def vts_475_vol_of_vol_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_475_vol_of_vol_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_of_vol over 252d. Volatility of the realized volatility.
    """
    return (close.pct_change(1).rolling(21).std().rolling(21).std()).rolling(252).kurt()

def vts_476_vol_decay_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_476_vol_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_decay over 5d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(5).skew()

def vts_477_vol_decay_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_477_vol_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_decay over 5d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(5).kurt()

def vts_478_vol_decay_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_478_vol_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_decay over 21d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(21).skew()

def vts_479_vol_decay_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_479_vol_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_decay over 21d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(21).kurt()

def vts_480_vol_decay_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_480_vol_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_decay over 63d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(63).skew()

def vts_481_vol_decay_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_481_vol_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_decay over 63d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(63).kurt()

def vts_482_vol_decay_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_482_vol_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_decay over 126d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(126).skew()

def vts_483_vol_decay_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_483_vol_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_decay over 126d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(126).kurt()

def vts_484_vol_decay_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_484_vol_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_decay over 252d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(252).skew()

def vts_485_vol_decay_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_485_vol_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_decay over 252d. Smoothed volatility decay.
    """
    return (close.pct_change(1).rolling(21).std().ewm(span=63).mean()).rolling(252).kurt()

def vts_486_vol_term_inversion_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_486_vol_term_inversion_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_term_inversion over 5d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(5).skew()

def vts_487_vol_term_inversion_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_487_vol_term_inversion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_term_inversion over 5d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(5).kurt()

def vts_488_vol_term_inversion_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_488_vol_term_inversion_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_term_inversion over 21d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(21).skew()

def vts_489_vol_term_inversion_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_489_vol_term_inversion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_term_inversion over 21d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(21).kurt()

def vts_490_vol_term_inversion_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_490_vol_term_inversion_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_term_inversion over 63d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(63).skew()

def vts_491_vol_term_inversion_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_491_vol_term_inversion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_term_inversion over 63d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(63).kurt()

def vts_492_vol_term_inversion_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_492_vol_term_inversion_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_term_inversion over 126d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(126).skew()

def vts_493_vol_term_inversion_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_493_vol_term_inversion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_term_inversion over 126d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(126).kurt()

def vts_494_vol_term_inversion_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_494_vol_term_inversion_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_term_inversion over 252d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(252).skew()

def vts_495_vol_term_inversion_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_495_vol_term_inversion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_term_inversion over 252d. Binary indicator of volatility term structure inversion.
    """
    return ((close.pct_change(1).rolling(5).std() > close.pct_change(1).rolling(252).std()).astype(float)).rolling(252).kurt()

def vts_496_vol_peak_dist_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_496_vol_peak_dist_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_peak_dist over 5d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(5).skew()

def vts_497_vol_peak_dist_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_497_vol_peak_dist_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_peak_dist over 5d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(5).kurt()

def vts_498_vol_peak_dist_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_498_vol_peak_dist_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_peak_dist over 21d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(21).skew()

def vts_499_vol_peak_dist_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_499_vol_peak_dist_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_peak_dist over 21d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(21).kurt()

def vts_500_vol_peak_dist_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_500_vol_peak_dist_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_peak_dist over 63d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(63).skew()

def vts_501_vol_peak_dist_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_501_vol_peak_dist_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_peak_dist over 63d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(63).kurt()

def vts_502_vol_peak_dist_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_502_vol_peak_dist_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_peak_dist over 126d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(126).skew()

def vts_503_vol_peak_dist_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_503_vol_peak_dist_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_peak_dist over 126d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(126).kurt()

def vts_504_vol_peak_dist_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_504_vol_peak_dist_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_peak_dist over 252d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(252).skew()

def vts_505_vol_peak_dist_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_505_vol_peak_dist_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_peak_dist over 252d. Current volatility relative to its annual peak.
    """
    return (close.pct_change(1).rolling(21).std() / close.pct_change(1).rolling(252).std().rolling(252).max()).rolling(252).kurt()

def vts_506_vol_tail_spread_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_506_vol_tail_spread_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_tail_spread over 5d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(5).skew()

def vts_507_vol_tail_spread_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_507_vol_tail_spread_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_tail_spread over 5d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(5).kurt()

def vts_508_vol_tail_spread_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_508_vol_tail_spread_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_tail_spread over 21d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(21).skew()

def vts_509_vol_tail_spread_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_509_vol_tail_spread_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_tail_spread over 21d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(21).kurt()

def vts_510_vol_tail_spread_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_510_vol_tail_spread_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_tail_spread over 63d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(63).skew()

def vts_511_vol_tail_spread_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_511_vol_tail_spread_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_tail_spread over 63d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(63).kurt()

def vts_512_vol_tail_spread_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_512_vol_tail_spread_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_tail_spread over 126d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(126).skew()

def vts_513_vol_tail_spread_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_513_vol_tail_spread_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_tail_spread over 126d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(126).kurt()

def vts_514_vol_tail_spread_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_514_vol_tail_spread_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_tail_spread over 252d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(252).skew()

def vts_515_vol_tail_spread_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_515_vol_tail_spread_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_tail_spread over 252d. Volatility of the tails relative to the mean.
    """
    return (close.pct_change(1).rolling(252).quantile(0.95).std() / close.pct_change(1).rolling(252).std()).rolling(252).kurt()

def vts_516_vol_structural_stability_skew_5d(close: pd.Series) -> pd.Series:
    """
    vts_516_vol_structural_stability_skew_5d
    ECONOMIC RATIONALE: Skewness of vol_structural_stability over 5d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(5).skew()

def vts_517_vol_structural_stability_kurt_5d(close: pd.Series) -> pd.Series:
    """
    vts_517_vol_structural_stability_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vol_structural_stability over 5d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(5).kurt()

def vts_518_vol_structural_stability_skew_21d(close: pd.Series) -> pd.Series:
    """
    vts_518_vol_structural_stability_skew_21d
    ECONOMIC RATIONALE: Skewness of vol_structural_stability over 21d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(21).skew()

def vts_519_vol_structural_stability_kurt_21d(close: pd.Series) -> pd.Series:
    """
    vts_519_vol_structural_stability_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vol_structural_stability over 21d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(21).kurt()

def vts_520_vol_structural_stability_skew_63d(close: pd.Series) -> pd.Series:
    """
    vts_520_vol_structural_stability_skew_63d
    ECONOMIC RATIONALE: Skewness of vol_structural_stability over 63d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(63).skew()

def vts_521_vol_structural_stability_kurt_63d(close: pd.Series) -> pd.Series:
    """
    vts_521_vol_structural_stability_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vol_structural_stability over 63d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(63).kurt()

def vts_522_vol_structural_stability_skew_126d(close: pd.Series) -> pd.Series:
    """
    vts_522_vol_structural_stability_skew_126d
    ECONOMIC RATIONALE: Skewness of vol_structural_stability over 126d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(126).skew()

def vts_523_vol_structural_stability_kurt_126d(close: pd.Series) -> pd.Series:
    """
    vts_523_vol_structural_stability_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vol_structural_stability over 126d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(126).kurt()

def vts_524_vol_structural_stability_skew_252d(close: pd.Series) -> pd.Series:
    """
    vts_524_vol_structural_stability_skew_252d
    ECONOMIC RATIONALE: Skewness of vol_structural_stability over 252d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(252).skew()

def vts_525_vol_structural_stability_kurt_252d(close: pd.Series) -> pd.Series:
    """
    vts_525_vol_structural_stability_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vol_structural_stability over 252d. Stability of the long-term volatility structure.
    """
    return (close.pct_change(1).rolling(252).std().rolling(63).std() / close.pct_change(1).rolling(252).std()).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V115_REGISTRY_MOMENTS = {
    "vts_376_vol_5d_skew_5d": {"inputs": ["close"], "func": vts_376_vol_5d_skew_5d},
    "vts_377_vol_5d_kurt_5d": {"inputs": ["close"], "func": vts_377_vol_5d_kurt_5d},
    "vts_378_vol_5d_skew_21d": {"inputs": ["close"], "func": vts_378_vol_5d_skew_21d},
    "vts_379_vol_5d_kurt_21d": {"inputs": ["close"], "func": vts_379_vol_5d_kurt_21d},
    "vts_380_vol_5d_skew_63d": {"inputs": ["close"], "func": vts_380_vol_5d_skew_63d},
    "vts_381_vol_5d_kurt_63d": {"inputs": ["close"], "func": vts_381_vol_5d_kurt_63d},
    "vts_382_vol_5d_skew_126d": {"inputs": ["close"], "func": vts_382_vol_5d_skew_126d},
    "vts_383_vol_5d_kurt_126d": {"inputs": ["close"], "func": vts_383_vol_5d_kurt_126d},
    "vts_384_vol_5d_skew_252d": {"inputs": ["close"], "func": vts_384_vol_5d_skew_252d},
    "vts_385_vol_5d_kurt_252d": {"inputs": ["close"], "func": vts_385_vol_5d_kurt_252d},
    "vts_386_vol_21d_skew_5d": {"inputs": ["close"], "func": vts_386_vol_21d_skew_5d},
    "vts_387_vol_21d_kurt_5d": {"inputs": ["close"], "func": vts_387_vol_21d_kurt_5d},
    "vts_388_vol_21d_skew_21d": {"inputs": ["close"], "func": vts_388_vol_21d_skew_21d},
    "vts_389_vol_21d_kurt_21d": {"inputs": ["close"], "func": vts_389_vol_21d_kurt_21d},
    "vts_390_vol_21d_skew_63d": {"inputs": ["close"], "func": vts_390_vol_21d_skew_63d},
    "vts_391_vol_21d_kurt_63d": {"inputs": ["close"], "func": vts_391_vol_21d_kurt_63d},
    "vts_392_vol_21d_skew_126d": {"inputs": ["close"], "func": vts_392_vol_21d_skew_126d},
    "vts_393_vol_21d_kurt_126d": {"inputs": ["close"], "func": vts_393_vol_21d_kurt_126d},
    "vts_394_vol_21d_skew_252d": {"inputs": ["close"], "func": vts_394_vol_21d_skew_252d},
    "vts_395_vol_21d_kurt_252d": {"inputs": ["close"], "func": vts_395_vol_21d_kurt_252d},
    "vts_396_vol_63d_skew_5d": {"inputs": ["close"], "func": vts_396_vol_63d_skew_5d},
    "vts_397_vol_63d_kurt_5d": {"inputs": ["close"], "func": vts_397_vol_63d_kurt_5d},
    "vts_398_vol_63d_skew_21d": {"inputs": ["close"], "func": vts_398_vol_63d_skew_21d},
    "vts_399_vol_63d_kurt_21d": {"inputs": ["close"], "func": vts_399_vol_63d_kurt_21d},
    "vts_400_vol_63d_skew_63d": {"inputs": ["close"], "func": vts_400_vol_63d_skew_63d},
    "vts_401_vol_63d_kurt_63d": {"inputs": ["close"], "func": vts_401_vol_63d_kurt_63d},
    "vts_402_vol_63d_skew_126d": {"inputs": ["close"], "func": vts_402_vol_63d_skew_126d},
    "vts_403_vol_63d_kurt_126d": {"inputs": ["close"], "func": vts_403_vol_63d_kurt_126d},
    "vts_404_vol_63d_skew_252d": {"inputs": ["close"], "func": vts_404_vol_63d_skew_252d},
    "vts_405_vol_63d_kurt_252d": {"inputs": ["close"], "func": vts_405_vol_63d_kurt_252d},
    "vts_406_vol_spread_short_long_skew_5d": {"inputs": ["close"], "func": vts_406_vol_spread_short_long_skew_5d},
    "vts_407_vol_spread_short_long_kurt_5d": {"inputs": ["close"], "func": vts_407_vol_spread_short_long_kurt_5d},
    "vts_408_vol_spread_short_long_skew_21d": {"inputs": ["close"], "func": vts_408_vol_spread_short_long_skew_21d},
    "vts_409_vol_spread_short_long_kurt_21d": {"inputs": ["close"], "func": vts_409_vol_spread_short_long_kurt_21d},
    "vts_410_vol_spread_short_long_skew_63d": {"inputs": ["close"], "func": vts_410_vol_spread_short_long_skew_63d},
    "vts_411_vol_spread_short_long_kurt_63d": {"inputs": ["close"], "func": vts_411_vol_spread_short_long_kurt_63d},
    "vts_412_vol_spread_short_long_skew_126d": {"inputs": ["close"], "func": vts_412_vol_spread_short_long_skew_126d},
    "vts_413_vol_spread_short_long_kurt_126d": {"inputs": ["close"], "func": vts_413_vol_spread_short_long_kurt_126d},
    "vts_414_vol_spread_short_long_skew_252d": {"inputs": ["close"], "func": vts_414_vol_spread_short_long_skew_252d},
    "vts_415_vol_spread_short_long_kurt_252d": {"inputs": ["close"], "func": vts_415_vol_spread_short_long_kurt_252d},
    "vts_416_vol_term_slope_skew_5d": {"inputs": ["close"], "func": vts_416_vol_term_slope_skew_5d},
    "vts_417_vol_term_slope_kurt_5d": {"inputs": ["close"], "func": vts_417_vol_term_slope_kurt_5d},
    "vts_418_vol_term_slope_skew_21d": {"inputs": ["close"], "func": vts_418_vol_term_slope_skew_21d},
    "vts_419_vol_term_slope_kurt_21d": {"inputs": ["close"], "func": vts_419_vol_term_slope_kurt_21d},
    "vts_420_vol_term_slope_skew_63d": {"inputs": ["close"], "func": vts_420_vol_term_slope_skew_63d},
    "vts_421_vol_term_slope_kurt_63d": {"inputs": ["close"], "func": vts_421_vol_term_slope_kurt_63d},
    "vts_422_vol_term_slope_skew_126d": {"inputs": ["close"], "func": vts_422_vol_term_slope_skew_126d},
    "vts_423_vol_term_slope_kurt_126d": {"inputs": ["close"], "func": vts_423_vol_term_slope_kurt_126d},
    "vts_424_vol_term_slope_skew_252d": {"inputs": ["close"], "func": vts_424_vol_term_slope_skew_252d},
    "vts_425_vol_term_slope_kurt_252d": {"inputs": ["close"], "func": vts_425_vol_term_slope_kurt_252d},
    "vts_426_vol_convexity_skew_5d": {"inputs": ["close"], "func": vts_426_vol_convexity_skew_5d},
    "vts_427_vol_convexity_kurt_5d": {"inputs": ["close"], "func": vts_427_vol_convexity_kurt_5d},
    "vts_428_vol_convexity_skew_21d": {"inputs": ["close"], "func": vts_428_vol_convexity_skew_21d},
    "vts_429_vol_convexity_kurt_21d": {"inputs": ["close"], "func": vts_429_vol_convexity_kurt_21d},
    "vts_430_vol_convexity_skew_63d": {"inputs": ["close"], "func": vts_430_vol_convexity_skew_63d},
    "vts_431_vol_convexity_kurt_63d": {"inputs": ["close"], "func": vts_431_vol_convexity_kurt_63d},
    "vts_432_vol_convexity_skew_126d": {"inputs": ["close"], "func": vts_432_vol_convexity_skew_126d},
    "vts_433_vol_convexity_kurt_126d": {"inputs": ["close"], "func": vts_433_vol_convexity_kurt_126d},
    "vts_434_vol_convexity_skew_252d": {"inputs": ["close"], "func": vts_434_vol_convexity_skew_252d},
    "vts_435_vol_convexity_kurt_252d": {"inputs": ["close"], "func": vts_435_vol_convexity_kurt_252d},
    "vts_436_vol_mean_reversion_speed_skew_5d": {"inputs": ["close"], "func": vts_436_vol_mean_reversion_speed_skew_5d},
    "vts_437_vol_mean_reversion_speed_kurt_5d": {"inputs": ["close"], "func": vts_437_vol_mean_reversion_speed_kurt_5d},
    "vts_438_vol_mean_reversion_speed_skew_21d": {"inputs": ["close"], "func": vts_438_vol_mean_reversion_speed_skew_21d},
    "vts_439_vol_mean_reversion_speed_kurt_21d": {"inputs": ["close"], "func": vts_439_vol_mean_reversion_speed_kurt_21d},
    "vts_440_vol_mean_reversion_speed_skew_63d": {"inputs": ["close"], "func": vts_440_vol_mean_reversion_speed_skew_63d},
    "vts_441_vol_mean_reversion_speed_kurt_63d": {"inputs": ["close"], "func": vts_441_vol_mean_reversion_speed_kurt_63d},
    "vts_442_vol_mean_reversion_speed_skew_126d": {"inputs": ["close"], "func": vts_442_vol_mean_reversion_speed_skew_126d},
    "vts_443_vol_mean_reversion_speed_kurt_126d": {"inputs": ["close"], "func": vts_443_vol_mean_reversion_speed_kurt_126d},
    "vts_444_vol_mean_reversion_speed_skew_252d": {"inputs": ["close"], "func": vts_444_vol_mean_reversion_speed_skew_252d},
    "vts_445_vol_mean_reversion_speed_kurt_252d": {"inputs": ["close"], "func": vts_445_vol_mean_reversion_speed_kurt_252d},
    "vts_446_vol_regime_z_skew_5d": {"inputs": ["close"], "func": vts_446_vol_regime_z_skew_5d},
    "vts_447_vol_regime_z_kurt_5d": {"inputs": ["close"], "func": vts_447_vol_regime_z_kurt_5d},
    "vts_448_vol_regime_z_skew_21d": {"inputs": ["close"], "func": vts_448_vol_regime_z_skew_21d},
    "vts_449_vol_regime_z_kurt_21d": {"inputs": ["close"], "func": vts_449_vol_regime_z_kurt_21d},
    "vts_450_vol_regime_z_skew_63d": {"inputs": ["close"], "func": vts_450_vol_regime_z_skew_63d},
    "vts_451_vol_regime_z_kurt_63d": {"inputs": ["close"], "func": vts_451_vol_regime_z_kurt_63d},
    "vts_452_vol_regime_z_skew_126d": {"inputs": ["close"], "func": vts_452_vol_regime_z_skew_126d},
    "vts_453_vol_regime_z_kurt_126d": {"inputs": ["close"], "func": vts_453_vol_regime_z_kurt_126d},
    "vts_454_vol_regime_z_skew_252d": {"inputs": ["close"], "func": vts_454_vol_regime_z_skew_252d},
    "vts_455_vol_regime_z_kurt_252d": {"inputs": ["close"], "func": vts_455_vol_regime_z_kurt_252d},
    "vts_456_vol_acceleration_skew_5d": {"inputs": ["close"], "func": vts_456_vol_acceleration_skew_5d},
    "vts_457_vol_acceleration_kurt_5d": {"inputs": ["close"], "func": vts_457_vol_acceleration_kurt_5d},
    "vts_458_vol_acceleration_skew_21d": {"inputs": ["close"], "func": vts_458_vol_acceleration_skew_21d},
    "vts_459_vol_acceleration_kurt_21d": {"inputs": ["close"], "func": vts_459_vol_acceleration_kurt_21d},
    "vts_460_vol_acceleration_skew_63d": {"inputs": ["close"], "func": vts_460_vol_acceleration_skew_63d},
    "vts_461_vol_acceleration_kurt_63d": {"inputs": ["close"], "func": vts_461_vol_acceleration_kurt_63d},
    "vts_462_vol_acceleration_skew_126d": {"inputs": ["close"], "func": vts_462_vol_acceleration_skew_126d},
    "vts_463_vol_acceleration_kurt_126d": {"inputs": ["close"], "func": vts_463_vol_acceleration_kurt_126d},
    "vts_464_vol_acceleration_skew_252d": {"inputs": ["close"], "func": vts_464_vol_acceleration_skew_252d},
    "vts_465_vol_acceleration_kurt_252d": {"inputs": ["close"], "func": vts_465_vol_acceleration_kurt_252d},
    "vts_466_vol_of_vol_skew_5d": {"inputs": ["close"], "func": vts_466_vol_of_vol_skew_5d},
    "vts_467_vol_of_vol_kurt_5d": {"inputs": ["close"], "func": vts_467_vol_of_vol_kurt_5d},
    "vts_468_vol_of_vol_skew_21d": {"inputs": ["close"], "func": vts_468_vol_of_vol_skew_21d},
    "vts_469_vol_of_vol_kurt_21d": {"inputs": ["close"], "func": vts_469_vol_of_vol_kurt_21d},
    "vts_470_vol_of_vol_skew_63d": {"inputs": ["close"], "func": vts_470_vol_of_vol_skew_63d},
    "vts_471_vol_of_vol_kurt_63d": {"inputs": ["close"], "func": vts_471_vol_of_vol_kurt_63d},
    "vts_472_vol_of_vol_skew_126d": {"inputs": ["close"], "func": vts_472_vol_of_vol_skew_126d},
    "vts_473_vol_of_vol_kurt_126d": {"inputs": ["close"], "func": vts_473_vol_of_vol_kurt_126d},
    "vts_474_vol_of_vol_skew_252d": {"inputs": ["close"], "func": vts_474_vol_of_vol_skew_252d},
    "vts_475_vol_of_vol_kurt_252d": {"inputs": ["close"], "func": vts_475_vol_of_vol_kurt_252d},
    "vts_476_vol_decay_skew_5d": {"inputs": ["close"], "func": vts_476_vol_decay_skew_5d},
    "vts_477_vol_decay_kurt_5d": {"inputs": ["close"], "func": vts_477_vol_decay_kurt_5d},
    "vts_478_vol_decay_skew_21d": {"inputs": ["close"], "func": vts_478_vol_decay_skew_21d},
    "vts_479_vol_decay_kurt_21d": {"inputs": ["close"], "func": vts_479_vol_decay_kurt_21d},
    "vts_480_vol_decay_skew_63d": {"inputs": ["close"], "func": vts_480_vol_decay_skew_63d},
    "vts_481_vol_decay_kurt_63d": {"inputs": ["close"], "func": vts_481_vol_decay_kurt_63d},
    "vts_482_vol_decay_skew_126d": {"inputs": ["close"], "func": vts_482_vol_decay_skew_126d},
    "vts_483_vol_decay_kurt_126d": {"inputs": ["close"], "func": vts_483_vol_decay_kurt_126d},
    "vts_484_vol_decay_skew_252d": {"inputs": ["close"], "func": vts_484_vol_decay_skew_252d},
    "vts_485_vol_decay_kurt_252d": {"inputs": ["close"], "func": vts_485_vol_decay_kurt_252d},
    "vts_486_vol_term_inversion_skew_5d": {"inputs": ["close"], "func": vts_486_vol_term_inversion_skew_5d},
    "vts_487_vol_term_inversion_kurt_5d": {"inputs": ["close"], "func": vts_487_vol_term_inversion_kurt_5d},
    "vts_488_vol_term_inversion_skew_21d": {"inputs": ["close"], "func": vts_488_vol_term_inversion_skew_21d},
    "vts_489_vol_term_inversion_kurt_21d": {"inputs": ["close"], "func": vts_489_vol_term_inversion_kurt_21d},
    "vts_490_vol_term_inversion_skew_63d": {"inputs": ["close"], "func": vts_490_vol_term_inversion_skew_63d},
    "vts_491_vol_term_inversion_kurt_63d": {"inputs": ["close"], "func": vts_491_vol_term_inversion_kurt_63d},
    "vts_492_vol_term_inversion_skew_126d": {"inputs": ["close"], "func": vts_492_vol_term_inversion_skew_126d},
    "vts_493_vol_term_inversion_kurt_126d": {"inputs": ["close"], "func": vts_493_vol_term_inversion_kurt_126d},
    "vts_494_vol_term_inversion_skew_252d": {"inputs": ["close"], "func": vts_494_vol_term_inversion_skew_252d},
    "vts_495_vol_term_inversion_kurt_252d": {"inputs": ["close"], "func": vts_495_vol_term_inversion_kurt_252d},
    "vts_496_vol_peak_dist_skew_5d": {"inputs": ["close"], "func": vts_496_vol_peak_dist_skew_5d},
    "vts_497_vol_peak_dist_kurt_5d": {"inputs": ["close"], "func": vts_497_vol_peak_dist_kurt_5d},
    "vts_498_vol_peak_dist_skew_21d": {"inputs": ["close"], "func": vts_498_vol_peak_dist_skew_21d},
    "vts_499_vol_peak_dist_kurt_21d": {"inputs": ["close"], "func": vts_499_vol_peak_dist_kurt_21d},
    "vts_500_vol_peak_dist_skew_63d": {"inputs": ["close"], "func": vts_500_vol_peak_dist_skew_63d},
    "vts_501_vol_peak_dist_kurt_63d": {"inputs": ["close"], "func": vts_501_vol_peak_dist_kurt_63d},
    "vts_502_vol_peak_dist_skew_126d": {"inputs": ["close"], "func": vts_502_vol_peak_dist_skew_126d},
    "vts_503_vol_peak_dist_kurt_126d": {"inputs": ["close"], "func": vts_503_vol_peak_dist_kurt_126d},
    "vts_504_vol_peak_dist_skew_252d": {"inputs": ["close"], "func": vts_504_vol_peak_dist_skew_252d},
    "vts_505_vol_peak_dist_kurt_252d": {"inputs": ["close"], "func": vts_505_vol_peak_dist_kurt_252d},
    "vts_506_vol_tail_spread_skew_5d": {"inputs": ["close"], "func": vts_506_vol_tail_spread_skew_5d},
    "vts_507_vol_tail_spread_kurt_5d": {"inputs": ["close"], "func": vts_507_vol_tail_spread_kurt_5d},
    "vts_508_vol_tail_spread_skew_21d": {"inputs": ["close"], "func": vts_508_vol_tail_spread_skew_21d},
    "vts_509_vol_tail_spread_kurt_21d": {"inputs": ["close"], "func": vts_509_vol_tail_spread_kurt_21d},
    "vts_510_vol_tail_spread_skew_63d": {"inputs": ["close"], "func": vts_510_vol_tail_spread_skew_63d},
    "vts_511_vol_tail_spread_kurt_63d": {"inputs": ["close"], "func": vts_511_vol_tail_spread_kurt_63d},
    "vts_512_vol_tail_spread_skew_126d": {"inputs": ["close"], "func": vts_512_vol_tail_spread_skew_126d},
    "vts_513_vol_tail_spread_kurt_126d": {"inputs": ["close"], "func": vts_513_vol_tail_spread_kurt_126d},
    "vts_514_vol_tail_spread_skew_252d": {"inputs": ["close"], "func": vts_514_vol_tail_spread_skew_252d},
    "vts_515_vol_tail_spread_kurt_252d": {"inputs": ["close"], "func": vts_515_vol_tail_spread_kurt_252d},
    "vts_516_vol_structural_stability_skew_5d": {"inputs": ["close"], "func": vts_516_vol_structural_stability_skew_5d},
    "vts_517_vol_structural_stability_kurt_5d": {"inputs": ["close"], "func": vts_517_vol_structural_stability_kurt_5d},
    "vts_518_vol_structural_stability_skew_21d": {"inputs": ["close"], "func": vts_518_vol_structural_stability_skew_21d},
    "vts_519_vol_structural_stability_kurt_21d": {"inputs": ["close"], "func": vts_519_vol_structural_stability_kurt_21d},
    "vts_520_vol_structural_stability_skew_63d": {"inputs": ["close"], "func": vts_520_vol_structural_stability_skew_63d},
    "vts_521_vol_structural_stability_kurt_63d": {"inputs": ["close"], "func": vts_521_vol_structural_stability_kurt_63d},
    "vts_522_vol_structural_stability_skew_126d": {"inputs": ["close"], "func": vts_522_vol_structural_stability_skew_126d},
    "vts_523_vol_structural_stability_kurt_126d": {"inputs": ["close"], "func": vts_523_vol_structural_stability_kurt_126d},
    "vts_524_vol_structural_stability_skew_252d": {"inputs": ["close"], "func": vts_524_vol_structural_stability_skew_252d},
    "vts_525_vol_structural_stability_kurt_252d": {"inputs": ["close"], "func": vts_525_vol_structural_stability_kurt_252d},
}
