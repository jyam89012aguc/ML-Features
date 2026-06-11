"""
109_return_autocorrelation — Statistical Moments
Domain: return_autocorrelation
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

def raut_376_lag1_autocorr_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_376_lag1_autocorr_skew_5d
    ECONOMIC RATIONALE: Skewness of lag1_autocorr over 5d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(5).skew()

def raut_377_lag1_autocorr_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_377_lag1_autocorr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of lag1_autocorr over 5d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(5).kurt()

def raut_378_lag1_autocorr_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_378_lag1_autocorr_skew_21d
    ECONOMIC RATIONALE: Skewness of lag1_autocorr over 21d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(21).skew()

def raut_379_lag1_autocorr_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_379_lag1_autocorr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of lag1_autocorr over 21d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(21).kurt()

def raut_380_lag1_autocorr_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_380_lag1_autocorr_skew_63d
    ECONOMIC RATIONALE: Skewness of lag1_autocorr over 63d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(63).skew()

def raut_381_lag1_autocorr_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_381_lag1_autocorr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of lag1_autocorr over 63d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(63).kurt()

def raut_382_lag1_autocorr_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_382_lag1_autocorr_skew_126d
    ECONOMIC RATIONALE: Skewness of lag1_autocorr over 126d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(126).skew()

def raut_383_lag1_autocorr_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_383_lag1_autocorr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of lag1_autocorr over 126d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(126).kurt()

def raut_384_lag1_autocorr_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_384_lag1_autocorr_skew_252d
    ECONOMIC RATIONALE: Skewness of lag1_autocorr over 252d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(252).skew()

def raut_385_lag1_autocorr_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_385_lag1_autocorr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of lag1_autocorr over 252d. 21-day serial correlation of returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(252).kurt()

def raut_386_lag5_autocorr_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_386_lag5_autocorr_skew_5d
    ECONOMIC RATIONALE: Skewness of lag5_autocorr over 5d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(5).skew()

def raut_387_lag5_autocorr_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_387_lag5_autocorr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of lag5_autocorr over 5d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(5).kurt()

def raut_388_lag5_autocorr_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_388_lag5_autocorr_skew_21d
    ECONOMIC RATIONALE: Skewness of lag5_autocorr over 21d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(21).skew()

def raut_389_lag5_autocorr_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_389_lag5_autocorr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of lag5_autocorr over 21d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(21).kurt()

def raut_390_lag5_autocorr_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_390_lag5_autocorr_skew_63d
    ECONOMIC RATIONALE: Skewness of lag5_autocorr over 63d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(63).skew()

def raut_391_lag5_autocorr_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_391_lag5_autocorr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of lag5_autocorr over 63d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(63).kurt()

def raut_392_lag5_autocorr_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_392_lag5_autocorr_skew_126d
    ECONOMIC RATIONALE: Skewness of lag5_autocorr over 126d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(126).skew()

def raut_393_lag5_autocorr_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_393_lag5_autocorr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of lag5_autocorr over 126d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(126).kurt()

def raut_394_lag5_autocorr_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_394_lag5_autocorr_skew_252d
    ECONOMIC RATIONALE: Skewness of lag5_autocorr over 252d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(252).skew()

def raut_395_lag5_autocorr_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_395_lag5_autocorr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of lag5_autocorr over 252d. 63-day correlation with weekly-lagged returns.
    """
    return (close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))).rolling(252).kurt()

def raut_396_autocorr_zscore_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_396_autocorr_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_zscore over 5d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).skew()

def raut_397_autocorr_zscore_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_397_autocorr_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_zscore over 5d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).kurt()

def raut_398_autocorr_zscore_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_398_autocorr_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_zscore over 21d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).skew()

def raut_399_autocorr_zscore_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_399_autocorr_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_zscore over 21d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).kurt()

def raut_400_autocorr_zscore_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_400_autocorr_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_zscore over 63d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).skew()

def raut_401_autocorr_zscore_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_401_autocorr_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_zscore over 63d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).kurt()

def raut_402_autocorr_zscore_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_402_autocorr_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_zscore over 126d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).skew()

def raut_403_autocorr_zscore_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_403_autocorr_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_zscore over 126d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).kurt()

def raut_404_autocorr_zscore_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_404_autocorr_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_zscore over 252d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).skew()

def raut_405_autocorr_zscore_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_405_autocorr_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_zscore over 252d. Anomaly in return persistence.
    """
    return (_zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).kurt()

def raut_406_autocorr_trend_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_406_autocorr_trend_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_trend over 5d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(5).skew()

def raut_407_autocorr_trend_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_407_autocorr_trend_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_trend over 5d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(5).kurt()

def raut_408_autocorr_trend_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_408_autocorr_trend_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_trend over 21d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(21).skew()

def raut_409_autocorr_trend_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_409_autocorr_trend_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_trend over 21d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(21).kurt()

def raut_410_autocorr_trend_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_410_autocorr_trend_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_trend over 63d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(63).skew()

def raut_411_autocorr_trend_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_411_autocorr_trend_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_trend over 63d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(63).kurt()

def raut_412_autocorr_trend_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_412_autocorr_trend_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_trend over 126d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(126).skew()

def raut_413_autocorr_trend_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_413_autocorr_trend_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_trend over 126d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(126).kurt()

def raut_414_autocorr_trend_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_414_autocorr_trend_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_trend over 252d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(252).skew()

def raut_415_autocorr_trend_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_415_autocorr_trend_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_trend over 252d. Shift in return persistence trend.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)).rolling(252).kurt()

def raut_416_negative_autocorr_flag_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_416_negative_autocorr_flag_skew_5d
    ECONOMIC RATIONALE: Skewness of negative_autocorr_flag over 5d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(5).skew()

def raut_417_negative_autocorr_flag_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_417_negative_autocorr_flag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of negative_autocorr_flag over 5d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(5).kurt()

def raut_418_negative_autocorr_flag_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_418_negative_autocorr_flag_skew_21d
    ECONOMIC RATIONALE: Skewness of negative_autocorr_flag over 21d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(21).skew()

def raut_419_negative_autocorr_flag_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_419_negative_autocorr_flag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of negative_autocorr_flag over 21d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(21).kurt()

def raut_420_negative_autocorr_flag_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_420_negative_autocorr_flag_skew_63d
    ECONOMIC RATIONALE: Skewness of negative_autocorr_flag over 63d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(63).skew()

def raut_421_negative_autocorr_flag_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_421_negative_autocorr_flag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of negative_autocorr_flag over 63d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(63).kurt()

def raut_422_negative_autocorr_flag_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_422_negative_autocorr_flag_skew_126d
    ECONOMIC RATIONALE: Skewness of negative_autocorr_flag over 126d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(126).skew()

def raut_423_negative_autocorr_flag_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_423_negative_autocorr_flag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of negative_autocorr_flag over 126d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(126).kurt()

def raut_424_negative_autocorr_flag_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_424_negative_autocorr_flag_skew_252d
    ECONOMIC RATIONALE: Skewness of negative_autocorr_flag over 252d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(252).skew()

def raut_425_negative_autocorr_flag_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_425_negative_autocorr_flag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of negative_autocorr_flag over 252d. Indication of mean-reverting regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)).rolling(252).kurt()

def raut_426_positive_autocorr_flag_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_426_positive_autocorr_flag_skew_5d
    ECONOMIC RATIONALE: Skewness of positive_autocorr_flag over 5d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(5).skew()

def raut_427_positive_autocorr_flag_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_427_positive_autocorr_flag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of positive_autocorr_flag over 5d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(5).kurt()

def raut_428_positive_autocorr_flag_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_428_positive_autocorr_flag_skew_21d
    ECONOMIC RATIONALE: Skewness of positive_autocorr_flag over 21d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(21).skew()

def raut_429_positive_autocorr_flag_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_429_positive_autocorr_flag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of positive_autocorr_flag over 21d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(21).kurt()

def raut_430_positive_autocorr_flag_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_430_positive_autocorr_flag_skew_63d
    ECONOMIC RATIONALE: Skewness of positive_autocorr_flag over 63d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(63).skew()

def raut_431_positive_autocorr_flag_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_431_positive_autocorr_flag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of positive_autocorr_flag over 63d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(63).kurt()

def raut_432_positive_autocorr_flag_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_432_positive_autocorr_flag_skew_126d
    ECONOMIC RATIONALE: Skewness of positive_autocorr_flag over 126d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(126).skew()

def raut_433_positive_autocorr_flag_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_433_positive_autocorr_flag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of positive_autocorr_flag over 126d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(126).kurt()

def raut_434_positive_autocorr_flag_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_434_positive_autocorr_flag_skew_252d
    ECONOMIC RATIONALE: Skewness of positive_autocorr_flag over 252d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(252).skew()

def raut_435_positive_autocorr_flag_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_435_positive_autocorr_flag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of positive_autocorr_flag over 252d. Indication of trending regime.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)).rolling(252).kurt()

def raut_436_autocorr_vol_corr_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_436_autocorr_vol_corr_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_vol_corr over 5d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(5).skew()

def raut_437_autocorr_vol_corr_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_437_autocorr_vol_corr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_vol_corr over 5d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(5).kurt()

def raut_438_autocorr_vol_corr_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_438_autocorr_vol_corr_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_vol_corr over 21d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(21).skew()

def raut_439_autocorr_vol_corr_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_439_autocorr_vol_corr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_vol_corr over 21d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(21).kurt()

def raut_440_autocorr_vol_corr_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_440_autocorr_vol_corr_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_vol_corr over 63d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(63).skew()

def raut_441_autocorr_vol_corr_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_441_autocorr_vol_corr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_vol_corr over 63d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(63).kurt()

def raut_442_autocorr_vol_corr_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_442_autocorr_vol_corr_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_vol_corr over 126d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(126).skew()

def raut_443_autocorr_vol_corr_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_443_autocorr_vol_corr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_vol_corr over 126d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(126).kurt()

def raut_444_autocorr_vol_corr_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_444_autocorr_vol_corr_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_vol_corr over 252d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(252).skew()

def raut_445_autocorr_vol_corr_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_445_autocorr_vol_corr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_vol_corr over 252d. Relationship between persistence and volatility.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())).rolling(252).kurt()

def raut_446_multi_lag_autocorr_sum_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_446_multi_lag_autocorr_sum_skew_5d
    ECONOMIC RATIONALE: Skewness of multi_lag_autocorr_sum over 5d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(5).skew()

def raut_447_multi_lag_autocorr_sum_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_447_multi_lag_autocorr_sum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of multi_lag_autocorr_sum over 5d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(5).kurt()

def raut_448_multi_lag_autocorr_sum_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_448_multi_lag_autocorr_sum_skew_21d
    ECONOMIC RATIONALE: Skewness of multi_lag_autocorr_sum over 21d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(21).skew()

def raut_449_multi_lag_autocorr_sum_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_449_multi_lag_autocorr_sum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of multi_lag_autocorr_sum over 21d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(21).kurt()

def raut_450_multi_lag_autocorr_sum_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_450_multi_lag_autocorr_sum_skew_63d
    ECONOMIC RATIONALE: Skewness of multi_lag_autocorr_sum over 63d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(63).skew()

def raut_451_multi_lag_autocorr_sum_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_451_multi_lag_autocorr_sum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of multi_lag_autocorr_sum over 63d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(63).kurt()

def raut_452_multi_lag_autocorr_sum_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_452_multi_lag_autocorr_sum_skew_126d
    ECONOMIC RATIONALE: Skewness of multi_lag_autocorr_sum over 126d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(126).skew()

def raut_453_multi_lag_autocorr_sum_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_453_multi_lag_autocorr_sum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of multi_lag_autocorr_sum over 126d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(126).kurt()

def raut_454_multi_lag_autocorr_sum_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_454_multi_lag_autocorr_sum_skew_252d
    ECONOMIC RATIONALE: Skewness of multi_lag_autocorr_sum over 252d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(252).skew()

def raut_455_multi_lag_autocorr_sum_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_455_multi_lag_autocorr_sum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of multi_lag_autocorr_sum over 252d. Average persistence across multiple lags.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2).rolling(252).kurt()

def raut_456_autocorr_breakdown_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_456_autocorr_breakdown_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_breakdown over 5d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(5).skew()

def raut_457_autocorr_breakdown_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_457_autocorr_breakdown_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_breakdown over 5d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(5).kurt()

def raut_458_autocorr_breakdown_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_458_autocorr_breakdown_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_breakdown over 21d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(21).skew()

def raut_459_autocorr_breakdown_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_459_autocorr_breakdown_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_breakdown over 21d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(21).kurt()

def raut_460_autocorr_breakdown_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_460_autocorr_breakdown_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_breakdown over 63d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(63).skew()

def raut_461_autocorr_breakdown_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_461_autocorr_breakdown_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_breakdown over 63d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(63).kurt()

def raut_462_autocorr_breakdown_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_462_autocorr_breakdown_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_breakdown over 126d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(126).skew()

def raut_463_autocorr_breakdown_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_463_autocorr_breakdown_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_breakdown over 126d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(126).kurt()

def raut_464_autocorr_breakdown_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_464_autocorr_breakdown_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_breakdown over 252d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(252).skew()

def raut_465_autocorr_breakdown_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_465_autocorr_breakdown_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_breakdown over 252d. Sudden breakdown in return structure.
    """
    return ((close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(1).abs() > 0.2).astype(float)).rolling(252).kurt()

def raut_466_return_clustering_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_466_return_clustering_skew_5d
    ECONOMIC RATIONALE: Skewness of return_clustering over 5d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(5).skew()

def raut_467_return_clustering_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_467_return_clustering_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of return_clustering over 5d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(5).kurt()

def raut_468_return_clustering_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_468_return_clustering_skew_21d
    ECONOMIC RATIONALE: Skewness of return_clustering over 21d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(21).skew()

def raut_469_return_clustering_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_469_return_clustering_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of return_clustering over 21d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(21).kurt()

def raut_470_return_clustering_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_470_return_clustering_skew_63d
    ECONOMIC RATIONALE: Skewness of return_clustering over 63d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(63).skew()

def raut_471_return_clustering_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_471_return_clustering_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of return_clustering over 63d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(63).kurt()

def raut_472_return_clustering_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_472_return_clustering_skew_126d
    ECONOMIC RATIONALE: Skewness of return_clustering over 126d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(126).skew()

def raut_473_return_clustering_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_473_return_clustering_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of return_clustering over 126d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(126).kurt()

def raut_474_return_clustering_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_474_return_clustering_skew_252d
    ECONOMIC RATIONALE: Skewness of return_clustering over 252d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(252).skew()

def raut_475_return_clustering_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_475_return_clustering_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of return_clustering over 252d. Autocorrelation of absolute returns (volatility clustering).
    """
    return (close.pct_change(1).abs().rolling(21).corr(close.pct_change(1).abs().shift(1))).rolling(252).kurt()

def raut_476_autocorr_regime_rank_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_476_autocorr_regime_rank_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_rank over 5d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).skew()

def raut_477_autocorr_regime_rank_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_477_autocorr_regime_rank_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_rank over 5d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(5).kurt()

def raut_478_autocorr_regime_rank_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_478_autocorr_regime_rank_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_rank over 21d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).skew()

def raut_479_autocorr_regime_rank_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_479_autocorr_regime_rank_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_rank over 21d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(21).kurt()

def raut_480_autocorr_regime_rank_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_480_autocorr_regime_rank_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_rank over 63d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).skew()

def raut_481_autocorr_regime_rank_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_481_autocorr_regime_rank_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_rank over 63d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(63).kurt()

def raut_482_autocorr_regime_rank_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_482_autocorr_regime_rank_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_rank over 126d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).skew()

def raut_483_autocorr_regime_rank_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_483_autocorr_regime_rank_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_rank over 126d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(126).kurt()

def raut_484_autocorr_regime_rank_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_484_autocorr_regime_rank_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_regime_rank over 252d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).skew()

def raut_485_autocorr_regime_rank_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_485_autocorr_regime_rank_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_regime_rank over 252d. Historical rank of current return persistence.
    """
    return (_rank_pct(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)).rolling(252).kurt()

def raut_486_autocorr_momentum_div_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_486_autocorr_momentum_div_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_momentum_div over 5d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(5).skew()

def raut_487_autocorr_momentum_div_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_487_autocorr_momentum_div_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_momentum_div over 5d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(5).kurt()

def raut_488_autocorr_momentum_div_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_488_autocorr_momentum_div_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_momentum_div over 21d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(21).skew()

def raut_489_autocorr_momentum_div_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_489_autocorr_momentum_div_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_momentum_div over 21d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(21).kurt()

def raut_490_autocorr_momentum_div_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_490_autocorr_momentum_div_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_momentum_div over 63d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(63).skew()

def raut_491_autocorr_momentum_div_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_491_autocorr_momentum_div_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_momentum_div over 63d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(63).kurt()

def raut_492_autocorr_momentum_div_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_492_autocorr_momentum_div_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_momentum_div over 126d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(126).skew()

def raut_493_autocorr_momentum_div_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_493_autocorr_momentum_div_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_momentum_div over 126d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(126).kurt()

def raut_494_autocorr_momentum_div_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_494_autocorr_momentum_div_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_momentum_div over 252d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(252).skew()

def raut_495_autocorr_momentum_div_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_495_autocorr_momentum_div_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_momentum_div over 252d. Momentum weighted by its own persistence.
    """
    return (close.pct_change(21) * close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))).rolling(252).kurt()

def raut_496_mean_reversion_edge_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_496_mean_reversion_edge_skew_5d
    ECONOMIC RATIONALE: Skewness of mean_reversion_edge over 5d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(5).skew()

def raut_497_mean_reversion_edge_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_497_mean_reversion_edge_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_edge over 5d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(5).kurt()

def raut_498_mean_reversion_edge_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_498_mean_reversion_edge_skew_21d
    ECONOMIC RATIONALE: Skewness of mean_reversion_edge over 21d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(21).skew()

def raut_499_mean_reversion_edge_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_499_mean_reversion_edge_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_edge over 21d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(21).kurt()

def raut_500_mean_reversion_edge_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_500_mean_reversion_edge_skew_63d
    ECONOMIC RATIONALE: Skewness of mean_reversion_edge over 63d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(63).skew()

def raut_501_mean_reversion_edge_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_501_mean_reversion_edge_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_edge over 63d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(63).kurt()

def raut_502_mean_reversion_edge_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_502_mean_reversion_edge_skew_126d
    ECONOMIC RATIONALE: Skewness of mean_reversion_edge over 126d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(126).skew()

def raut_503_mean_reversion_edge_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_503_mean_reversion_edge_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_edge over 126d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(126).kurt()

def raut_504_mean_reversion_edge_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_504_mean_reversion_edge_skew_252d
    ECONOMIC RATIONALE: Skewness of mean_reversion_edge over 252d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(252).skew()

def raut_505_mean_reversion_edge_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_505_mean_reversion_edge_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of mean_reversion_edge over 252d. Short-term mean reversion signal.
    """
    return (close.pct_change(1).rolling(10).apply(lambda x: x.autocorr(1)) < 0).rolling(252).kurt()

def raut_506_autocorr_stability_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_506_autocorr_stability_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_stability over 5d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(5).skew()

def raut_507_autocorr_stability_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_507_autocorr_stability_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_stability over 5d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(5).kurt()

def raut_508_autocorr_stability_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_508_autocorr_stability_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_stability over 21d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(21).skew()

def raut_509_autocorr_stability_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_509_autocorr_stability_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_stability over 21d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(21).kurt()

def raut_510_autocorr_stability_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_510_autocorr_stability_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_stability over 63d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(63).skew()

def raut_511_autocorr_stability_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_511_autocorr_stability_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_stability over 63d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(63).kurt()

def raut_512_autocorr_stability_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_512_autocorr_stability_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_stability over 126d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(126).skew()

def raut_513_autocorr_stability_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_513_autocorr_stability_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_stability over 126d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(126).kurt()

def raut_514_autocorr_stability_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_514_autocorr_stability_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_stability over 252d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(252).skew()

def raut_515_autocorr_stability_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_515_autocorr_stability_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_stability over 252d. Stability of the return persistence regime.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).std()).rolling(252).kurt()

def raut_516_autocorr_acceleration_skew_5d(close: pd.Series) -> pd.Series:
    """
    raut_516_autocorr_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_acceleration over 5d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(5).skew()

def raut_517_autocorr_acceleration_kurt_5d(close: pd.Series) -> pd.Series:
    """
    raut_517_autocorr_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_acceleration over 5d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(5).kurt()

def raut_518_autocorr_acceleration_skew_21d(close: pd.Series) -> pd.Series:
    """
    raut_518_autocorr_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_acceleration over 21d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(21).skew()

def raut_519_autocorr_acceleration_kurt_21d(close: pd.Series) -> pd.Series:
    """
    raut_519_autocorr_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_acceleration over 21d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(21).kurt()

def raut_520_autocorr_acceleration_skew_63d(close: pd.Series) -> pd.Series:
    """
    raut_520_autocorr_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_acceleration over 63d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(63).skew()

def raut_521_autocorr_acceleration_kurt_63d(close: pd.Series) -> pd.Series:
    """
    raut_521_autocorr_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_acceleration over 63d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(63).kurt()

def raut_522_autocorr_acceleration_skew_126d(close: pd.Series) -> pd.Series:
    """
    raut_522_autocorr_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_acceleration over 126d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(126).skew()

def raut_523_autocorr_acceleration_kurt_126d(close: pd.Series) -> pd.Series:
    """
    raut_523_autocorr_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_acceleration over 126d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(126).kurt()

def raut_524_autocorr_acceleration_skew_252d(close: pd.Series) -> pd.Series:
    """
    raut_524_autocorr_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_acceleration over 252d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(252).skew()

def raut_525_autocorr_acceleration_kurt_252d(close: pd.Series) -> pd.Series:
    """
    raut_525_autocorr_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_acceleration over 252d. Short-term change in return persistence.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(5)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V109_REGISTRY_MOMENTS = {
    "raut_376_lag1_autocorr_skew_5d": {"inputs": ["close"], "func": raut_376_lag1_autocorr_skew_5d},
    "raut_377_lag1_autocorr_kurt_5d": {"inputs": ["close"], "func": raut_377_lag1_autocorr_kurt_5d},
    "raut_378_lag1_autocorr_skew_21d": {"inputs": ["close"], "func": raut_378_lag1_autocorr_skew_21d},
    "raut_379_lag1_autocorr_kurt_21d": {"inputs": ["close"], "func": raut_379_lag1_autocorr_kurt_21d},
    "raut_380_lag1_autocorr_skew_63d": {"inputs": ["close"], "func": raut_380_lag1_autocorr_skew_63d},
    "raut_381_lag1_autocorr_kurt_63d": {"inputs": ["close"], "func": raut_381_lag1_autocorr_kurt_63d},
    "raut_382_lag1_autocorr_skew_126d": {"inputs": ["close"], "func": raut_382_lag1_autocorr_skew_126d},
    "raut_383_lag1_autocorr_kurt_126d": {"inputs": ["close"], "func": raut_383_lag1_autocorr_kurt_126d},
    "raut_384_lag1_autocorr_skew_252d": {"inputs": ["close"], "func": raut_384_lag1_autocorr_skew_252d},
    "raut_385_lag1_autocorr_kurt_252d": {"inputs": ["close"], "func": raut_385_lag1_autocorr_kurt_252d},
    "raut_386_lag5_autocorr_skew_5d": {"inputs": ["close"], "func": raut_386_lag5_autocorr_skew_5d},
    "raut_387_lag5_autocorr_kurt_5d": {"inputs": ["close"], "func": raut_387_lag5_autocorr_kurt_5d},
    "raut_388_lag5_autocorr_skew_21d": {"inputs": ["close"], "func": raut_388_lag5_autocorr_skew_21d},
    "raut_389_lag5_autocorr_kurt_21d": {"inputs": ["close"], "func": raut_389_lag5_autocorr_kurt_21d},
    "raut_390_lag5_autocorr_skew_63d": {"inputs": ["close"], "func": raut_390_lag5_autocorr_skew_63d},
    "raut_391_lag5_autocorr_kurt_63d": {"inputs": ["close"], "func": raut_391_lag5_autocorr_kurt_63d},
    "raut_392_lag5_autocorr_skew_126d": {"inputs": ["close"], "func": raut_392_lag5_autocorr_skew_126d},
    "raut_393_lag5_autocorr_kurt_126d": {"inputs": ["close"], "func": raut_393_lag5_autocorr_kurt_126d},
    "raut_394_lag5_autocorr_skew_252d": {"inputs": ["close"], "func": raut_394_lag5_autocorr_skew_252d},
    "raut_395_lag5_autocorr_kurt_252d": {"inputs": ["close"], "func": raut_395_lag5_autocorr_kurt_252d},
    "raut_396_autocorr_zscore_skew_5d": {"inputs": ["close"], "func": raut_396_autocorr_zscore_skew_5d},
    "raut_397_autocorr_zscore_kurt_5d": {"inputs": ["close"], "func": raut_397_autocorr_zscore_kurt_5d},
    "raut_398_autocorr_zscore_skew_21d": {"inputs": ["close"], "func": raut_398_autocorr_zscore_skew_21d},
    "raut_399_autocorr_zscore_kurt_21d": {"inputs": ["close"], "func": raut_399_autocorr_zscore_kurt_21d},
    "raut_400_autocorr_zscore_skew_63d": {"inputs": ["close"], "func": raut_400_autocorr_zscore_skew_63d},
    "raut_401_autocorr_zscore_kurt_63d": {"inputs": ["close"], "func": raut_401_autocorr_zscore_kurt_63d},
    "raut_402_autocorr_zscore_skew_126d": {"inputs": ["close"], "func": raut_402_autocorr_zscore_skew_126d},
    "raut_403_autocorr_zscore_kurt_126d": {"inputs": ["close"], "func": raut_403_autocorr_zscore_kurt_126d},
    "raut_404_autocorr_zscore_skew_252d": {"inputs": ["close"], "func": raut_404_autocorr_zscore_skew_252d},
    "raut_405_autocorr_zscore_kurt_252d": {"inputs": ["close"], "func": raut_405_autocorr_zscore_kurt_252d},
    "raut_406_autocorr_trend_skew_5d": {"inputs": ["close"], "func": raut_406_autocorr_trend_skew_5d},
    "raut_407_autocorr_trend_kurt_5d": {"inputs": ["close"], "func": raut_407_autocorr_trend_kurt_5d},
    "raut_408_autocorr_trend_skew_21d": {"inputs": ["close"], "func": raut_408_autocorr_trend_skew_21d},
    "raut_409_autocorr_trend_kurt_21d": {"inputs": ["close"], "func": raut_409_autocorr_trend_kurt_21d},
    "raut_410_autocorr_trend_skew_63d": {"inputs": ["close"], "func": raut_410_autocorr_trend_skew_63d},
    "raut_411_autocorr_trend_kurt_63d": {"inputs": ["close"], "func": raut_411_autocorr_trend_kurt_63d},
    "raut_412_autocorr_trend_skew_126d": {"inputs": ["close"], "func": raut_412_autocorr_trend_skew_126d},
    "raut_413_autocorr_trend_kurt_126d": {"inputs": ["close"], "func": raut_413_autocorr_trend_kurt_126d},
    "raut_414_autocorr_trend_skew_252d": {"inputs": ["close"], "func": raut_414_autocorr_trend_skew_252d},
    "raut_415_autocorr_trend_kurt_252d": {"inputs": ["close"], "func": raut_415_autocorr_trend_kurt_252d},
    "raut_416_negative_autocorr_flag_skew_5d": {"inputs": ["close"], "func": raut_416_negative_autocorr_flag_skew_5d},
    "raut_417_negative_autocorr_flag_kurt_5d": {"inputs": ["close"], "func": raut_417_negative_autocorr_flag_kurt_5d},
    "raut_418_negative_autocorr_flag_skew_21d": {"inputs": ["close"], "func": raut_418_negative_autocorr_flag_skew_21d},
    "raut_419_negative_autocorr_flag_kurt_21d": {"inputs": ["close"], "func": raut_419_negative_autocorr_flag_kurt_21d},
    "raut_420_negative_autocorr_flag_skew_63d": {"inputs": ["close"], "func": raut_420_negative_autocorr_flag_skew_63d},
    "raut_421_negative_autocorr_flag_kurt_63d": {"inputs": ["close"], "func": raut_421_negative_autocorr_flag_kurt_63d},
    "raut_422_negative_autocorr_flag_skew_126d": {"inputs": ["close"], "func": raut_422_negative_autocorr_flag_skew_126d},
    "raut_423_negative_autocorr_flag_kurt_126d": {"inputs": ["close"], "func": raut_423_negative_autocorr_flag_kurt_126d},
    "raut_424_negative_autocorr_flag_skew_252d": {"inputs": ["close"], "func": raut_424_negative_autocorr_flag_skew_252d},
    "raut_425_negative_autocorr_flag_kurt_252d": {"inputs": ["close"], "func": raut_425_negative_autocorr_flag_kurt_252d},
    "raut_426_positive_autocorr_flag_skew_5d": {"inputs": ["close"], "func": raut_426_positive_autocorr_flag_skew_5d},
    "raut_427_positive_autocorr_flag_kurt_5d": {"inputs": ["close"], "func": raut_427_positive_autocorr_flag_kurt_5d},
    "raut_428_positive_autocorr_flag_skew_21d": {"inputs": ["close"], "func": raut_428_positive_autocorr_flag_skew_21d},
    "raut_429_positive_autocorr_flag_kurt_21d": {"inputs": ["close"], "func": raut_429_positive_autocorr_flag_kurt_21d},
    "raut_430_positive_autocorr_flag_skew_63d": {"inputs": ["close"], "func": raut_430_positive_autocorr_flag_skew_63d},
    "raut_431_positive_autocorr_flag_kurt_63d": {"inputs": ["close"], "func": raut_431_positive_autocorr_flag_kurt_63d},
    "raut_432_positive_autocorr_flag_skew_126d": {"inputs": ["close"], "func": raut_432_positive_autocorr_flag_skew_126d},
    "raut_433_positive_autocorr_flag_kurt_126d": {"inputs": ["close"], "func": raut_433_positive_autocorr_flag_kurt_126d},
    "raut_434_positive_autocorr_flag_skew_252d": {"inputs": ["close"], "func": raut_434_positive_autocorr_flag_skew_252d},
    "raut_435_positive_autocorr_flag_kurt_252d": {"inputs": ["close"], "func": raut_435_positive_autocorr_flag_kurt_252d},
    "raut_436_autocorr_vol_corr_skew_5d": {"inputs": ["close"], "func": raut_436_autocorr_vol_corr_skew_5d},
    "raut_437_autocorr_vol_corr_kurt_5d": {"inputs": ["close"], "func": raut_437_autocorr_vol_corr_kurt_5d},
    "raut_438_autocorr_vol_corr_skew_21d": {"inputs": ["close"], "func": raut_438_autocorr_vol_corr_skew_21d},
    "raut_439_autocorr_vol_corr_kurt_21d": {"inputs": ["close"], "func": raut_439_autocorr_vol_corr_kurt_21d},
    "raut_440_autocorr_vol_corr_skew_63d": {"inputs": ["close"], "func": raut_440_autocorr_vol_corr_skew_63d},
    "raut_441_autocorr_vol_corr_kurt_63d": {"inputs": ["close"], "func": raut_441_autocorr_vol_corr_kurt_63d},
    "raut_442_autocorr_vol_corr_skew_126d": {"inputs": ["close"], "func": raut_442_autocorr_vol_corr_skew_126d},
    "raut_443_autocorr_vol_corr_kurt_126d": {"inputs": ["close"], "func": raut_443_autocorr_vol_corr_kurt_126d},
    "raut_444_autocorr_vol_corr_skew_252d": {"inputs": ["close"], "func": raut_444_autocorr_vol_corr_skew_252d},
    "raut_445_autocorr_vol_corr_kurt_252d": {"inputs": ["close"], "func": raut_445_autocorr_vol_corr_kurt_252d},
    "raut_446_multi_lag_autocorr_sum_skew_5d": {"inputs": ["close"], "func": raut_446_multi_lag_autocorr_sum_skew_5d},
    "raut_447_multi_lag_autocorr_sum_kurt_5d": {"inputs": ["close"], "func": raut_447_multi_lag_autocorr_sum_kurt_5d},
    "raut_448_multi_lag_autocorr_sum_skew_21d": {"inputs": ["close"], "func": raut_448_multi_lag_autocorr_sum_skew_21d},
    "raut_449_multi_lag_autocorr_sum_kurt_21d": {"inputs": ["close"], "func": raut_449_multi_lag_autocorr_sum_kurt_21d},
    "raut_450_multi_lag_autocorr_sum_skew_63d": {"inputs": ["close"], "func": raut_450_multi_lag_autocorr_sum_skew_63d},
    "raut_451_multi_lag_autocorr_sum_kurt_63d": {"inputs": ["close"], "func": raut_451_multi_lag_autocorr_sum_kurt_63d},
    "raut_452_multi_lag_autocorr_sum_skew_126d": {"inputs": ["close"], "func": raut_452_multi_lag_autocorr_sum_skew_126d},
    "raut_453_multi_lag_autocorr_sum_kurt_126d": {"inputs": ["close"], "func": raut_453_multi_lag_autocorr_sum_kurt_126d},
    "raut_454_multi_lag_autocorr_sum_skew_252d": {"inputs": ["close"], "func": raut_454_multi_lag_autocorr_sum_skew_252d},
    "raut_455_multi_lag_autocorr_sum_kurt_252d": {"inputs": ["close"], "func": raut_455_multi_lag_autocorr_sum_kurt_252d},
    "raut_456_autocorr_breakdown_skew_5d": {"inputs": ["close"], "func": raut_456_autocorr_breakdown_skew_5d},
    "raut_457_autocorr_breakdown_kurt_5d": {"inputs": ["close"], "func": raut_457_autocorr_breakdown_kurt_5d},
    "raut_458_autocorr_breakdown_skew_21d": {"inputs": ["close"], "func": raut_458_autocorr_breakdown_skew_21d},
    "raut_459_autocorr_breakdown_kurt_21d": {"inputs": ["close"], "func": raut_459_autocorr_breakdown_kurt_21d},
    "raut_460_autocorr_breakdown_skew_63d": {"inputs": ["close"], "func": raut_460_autocorr_breakdown_skew_63d},
    "raut_461_autocorr_breakdown_kurt_63d": {"inputs": ["close"], "func": raut_461_autocorr_breakdown_kurt_63d},
    "raut_462_autocorr_breakdown_skew_126d": {"inputs": ["close"], "func": raut_462_autocorr_breakdown_skew_126d},
    "raut_463_autocorr_breakdown_kurt_126d": {"inputs": ["close"], "func": raut_463_autocorr_breakdown_kurt_126d},
    "raut_464_autocorr_breakdown_skew_252d": {"inputs": ["close"], "func": raut_464_autocorr_breakdown_skew_252d},
    "raut_465_autocorr_breakdown_kurt_252d": {"inputs": ["close"], "func": raut_465_autocorr_breakdown_kurt_252d},
    "raut_466_return_clustering_skew_5d": {"inputs": ["close"], "func": raut_466_return_clustering_skew_5d},
    "raut_467_return_clustering_kurt_5d": {"inputs": ["close"], "func": raut_467_return_clustering_kurt_5d},
    "raut_468_return_clustering_skew_21d": {"inputs": ["close"], "func": raut_468_return_clustering_skew_21d},
    "raut_469_return_clustering_kurt_21d": {"inputs": ["close"], "func": raut_469_return_clustering_kurt_21d},
    "raut_470_return_clustering_skew_63d": {"inputs": ["close"], "func": raut_470_return_clustering_skew_63d},
    "raut_471_return_clustering_kurt_63d": {"inputs": ["close"], "func": raut_471_return_clustering_kurt_63d},
    "raut_472_return_clustering_skew_126d": {"inputs": ["close"], "func": raut_472_return_clustering_skew_126d},
    "raut_473_return_clustering_kurt_126d": {"inputs": ["close"], "func": raut_473_return_clustering_kurt_126d},
    "raut_474_return_clustering_skew_252d": {"inputs": ["close"], "func": raut_474_return_clustering_skew_252d},
    "raut_475_return_clustering_kurt_252d": {"inputs": ["close"], "func": raut_475_return_clustering_kurt_252d},
    "raut_476_autocorr_regime_rank_skew_5d": {"inputs": ["close"], "func": raut_476_autocorr_regime_rank_skew_5d},
    "raut_477_autocorr_regime_rank_kurt_5d": {"inputs": ["close"], "func": raut_477_autocorr_regime_rank_kurt_5d},
    "raut_478_autocorr_regime_rank_skew_21d": {"inputs": ["close"], "func": raut_478_autocorr_regime_rank_skew_21d},
    "raut_479_autocorr_regime_rank_kurt_21d": {"inputs": ["close"], "func": raut_479_autocorr_regime_rank_kurt_21d},
    "raut_480_autocorr_regime_rank_skew_63d": {"inputs": ["close"], "func": raut_480_autocorr_regime_rank_skew_63d},
    "raut_481_autocorr_regime_rank_kurt_63d": {"inputs": ["close"], "func": raut_481_autocorr_regime_rank_kurt_63d},
    "raut_482_autocorr_regime_rank_skew_126d": {"inputs": ["close"], "func": raut_482_autocorr_regime_rank_skew_126d},
    "raut_483_autocorr_regime_rank_kurt_126d": {"inputs": ["close"], "func": raut_483_autocorr_regime_rank_kurt_126d},
    "raut_484_autocorr_regime_rank_skew_252d": {"inputs": ["close"], "func": raut_484_autocorr_regime_rank_skew_252d},
    "raut_485_autocorr_regime_rank_kurt_252d": {"inputs": ["close"], "func": raut_485_autocorr_regime_rank_kurt_252d},
    "raut_486_autocorr_momentum_div_skew_5d": {"inputs": ["close"], "func": raut_486_autocorr_momentum_div_skew_5d},
    "raut_487_autocorr_momentum_div_kurt_5d": {"inputs": ["close"], "func": raut_487_autocorr_momentum_div_kurt_5d},
    "raut_488_autocorr_momentum_div_skew_21d": {"inputs": ["close"], "func": raut_488_autocorr_momentum_div_skew_21d},
    "raut_489_autocorr_momentum_div_kurt_21d": {"inputs": ["close"], "func": raut_489_autocorr_momentum_div_kurt_21d},
    "raut_490_autocorr_momentum_div_skew_63d": {"inputs": ["close"], "func": raut_490_autocorr_momentum_div_skew_63d},
    "raut_491_autocorr_momentum_div_kurt_63d": {"inputs": ["close"], "func": raut_491_autocorr_momentum_div_kurt_63d},
    "raut_492_autocorr_momentum_div_skew_126d": {"inputs": ["close"], "func": raut_492_autocorr_momentum_div_skew_126d},
    "raut_493_autocorr_momentum_div_kurt_126d": {"inputs": ["close"], "func": raut_493_autocorr_momentum_div_kurt_126d},
    "raut_494_autocorr_momentum_div_skew_252d": {"inputs": ["close"], "func": raut_494_autocorr_momentum_div_skew_252d},
    "raut_495_autocorr_momentum_div_kurt_252d": {"inputs": ["close"], "func": raut_495_autocorr_momentum_div_kurt_252d},
    "raut_496_mean_reversion_edge_skew_5d": {"inputs": ["close"], "func": raut_496_mean_reversion_edge_skew_5d},
    "raut_497_mean_reversion_edge_kurt_5d": {"inputs": ["close"], "func": raut_497_mean_reversion_edge_kurt_5d},
    "raut_498_mean_reversion_edge_skew_21d": {"inputs": ["close"], "func": raut_498_mean_reversion_edge_skew_21d},
    "raut_499_mean_reversion_edge_kurt_21d": {"inputs": ["close"], "func": raut_499_mean_reversion_edge_kurt_21d},
    "raut_500_mean_reversion_edge_skew_63d": {"inputs": ["close"], "func": raut_500_mean_reversion_edge_skew_63d},
    "raut_501_mean_reversion_edge_kurt_63d": {"inputs": ["close"], "func": raut_501_mean_reversion_edge_kurt_63d},
    "raut_502_mean_reversion_edge_skew_126d": {"inputs": ["close"], "func": raut_502_mean_reversion_edge_skew_126d},
    "raut_503_mean_reversion_edge_kurt_126d": {"inputs": ["close"], "func": raut_503_mean_reversion_edge_kurt_126d},
    "raut_504_mean_reversion_edge_skew_252d": {"inputs": ["close"], "func": raut_504_mean_reversion_edge_skew_252d},
    "raut_505_mean_reversion_edge_kurt_252d": {"inputs": ["close"], "func": raut_505_mean_reversion_edge_kurt_252d},
    "raut_506_autocorr_stability_skew_5d": {"inputs": ["close"], "func": raut_506_autocorr_stability_skew_5d},
    "raut_507_autocorr_stability_kurt_5d": {"inputs": ["close"], "func": raut_507_autocorr_stability_kurt_5d},
    "raut_508_autocorr_stability_skew_21d": {"inputs": ["close"], "func": raut_508_autocorr_stability_skew_21d},
    "raut_509_autocorr_stability_kurt_21d": {"inputs": ["close"], "func": raut_509_autocorr_stability_kurt_21d},
    "raut_510_autocorr_stability_skew_63d": {"inputs": ["close"], "func": raut_510_autocorr_stability_skew_63d},
    "raut_511_autocorr_stability_kurt_63d": {"inputs": ["close"], "func": raut_511_autocorr_stability_kurt_63d},
    "raut_512_autocorr_stability_skew_126d": {"inputs": ["close"], "func": raut_512_autocorr_stability_skew_126d},
    "raut_513_autocorr_stability_kurt_126d": {"inputs": ["close"], "func": raut_513_autocorr_stability_kurt_126d},
    "raut_514_autocorr_stability_skew_252d": {"inputs": ["close"], "func": raut_514_autocorr_stability_skew_252d},
    "raut_515_autocorr_stability_kurt_252d": {"inputs": ["close"], "func": raut_515_autocorr_stability_kurt_252d},
    "raut_516_autocorr_acceleration_skew_5d": {"inputs": ["close"], "func": raut_516_autocorr_acceleration_skew_5d},
    "raut_517_autocorr_acceleration_kurt_5d": {"inputs": ["close"], "func": raut_517_autocorr_acceleration_kurt_5d},
    "raut_518_autocorr_acceleration_skew_21d": {"inputs": ["close"], "func": raut_518_autocorr_acceleration_skew_21d},
    "raut_519_autocorr_acceleration_kurt_21d": {"inputs": ["close"], "func": raut_519_autocorr_acceleration_kurt_21d},
    "raut_520_autocorr_acceleration_skew_63d": {"inputs": ["close"], "func": raut_520_autocorr_acceleration_skew_63d},
    "raut_521_autocorr_acceleration_kurt_63d": {"inputs": ["close"], "func": raut_521_autocorr_acceleration_kurt_63d},
    "raut_522_autocorr_acceleration_skew_126d": {"inputs": ["close"], "func": raut_522_autocorr_acceleration_skew_126d},
    "raut_523_autocorr_acceleration_kurt_126d": {"inputs": ["close"], "func": raut_523_autocorr_acceleration_kurt_126d},
    "raut_524_autocorr_acceleration_skew_252d": {"inputs": ["close"], "func": raut_524_autocorr_acceleration_skew_252d},
    "raut_525_autocorr_acceleration_kurt_252d": {"inputs": ["close"], "func": raut_525_autocorr_acceleration_kurt_252d},
}
