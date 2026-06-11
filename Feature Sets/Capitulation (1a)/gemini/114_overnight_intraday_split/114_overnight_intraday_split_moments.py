"""
114_overnight_intraday_split — Statistical Moments
Domain: overnight_intraday_split
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

def onid_376_overnight_return_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_376_overnight_return_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_return over 5d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(5).skew()

def onid_377_overnight_return_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_377_overnight_return_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_return over 5d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(5).kurt()

def onid_378_overnight_return_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_378_overnight_return_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_return over 21d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(21).skew()

def onid_379_overnight_return_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_379_overnight_return_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_return over 21d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(21).kurt()

def onid_380_overnight_return_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_380_overnight_return_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_return over 63d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(63).skew()

def onid_381_overnight_return_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_381_overnight_return_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_return over 63d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(63).kurt()

def onid_382_overnight_return_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_382_overnight_return_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_return over 126d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(126).skew()

def onid_383_overnight_return_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_383_overnight_return_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_return over 126d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(126).kurt()

def onid_384_overnight_return_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_384_overnight_return_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_return over 252d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(252).skew()

def onid_385_overnight_return_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_385_overnight_return_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_return over 252d. Returns from previous close to current open.
    """
    return (open / close.shift(1) - 1).rolling(252).kurt()

def onid_386_intraday_return_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_386_intraday_return_skew_5d
    ECONOMIC RATIONALE: Skewness of intraday_return over 5d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(5).skew()

def onid_387_intraday_return_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_387_intraday_return_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of intraday_return over 5d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(5).kurt()

def onid_388_intraday_return_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_388_intraday_return_skew_21d
    ECONOMIC RATIONALE: Skewness of intraday_return over 21d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(21).skew()

def onid_389_intraday_return_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_389_intraday_return_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of intraday_return over 21d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(21).kurt()

def onid_390_intraday_return_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_390_intraday_return_skew_63d
    ECONOMIC RATIONALE: Skewness of intraday_return over 63d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(63).skew()

def onid_391_intraday_return_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_391_intraday_return_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of intraday_return over 63d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(63).kurt()

def onid_392_intraday_return_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_392_intraday_return_skew_126d
    ECONOMIC RATIONALE: Skewness of intraday_return over 126d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(126).skew()

def onid_393_intraday_return_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_393_intraday_return_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of intraday_return over 126d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(126).kurt()

def onid_394_intraday_return_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_394_intraday_return_skew_252d
    ECONOMIC RATIONALE: Skewness of intraday_return over 252d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(252).skew()

def onid_395_intraday_return_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_395_intraday_return_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of intraday_return over 252d. Returns from current open to current close.
    """
    return (close / open - 1).rolling(252).kurt()

def onid_396_on_id_divergence_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_396_on_id_divergence_skew_5d
    ECONOMIC RATIONALE: Skewness of on_id_divergence over 5d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(5).skew()

def onid_397_on_id_divergence_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_397_on_id_divergence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of on_id_divergence over 5d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(5).kurt()

def onid_398_on_id_divergence_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_398_on_id_divergence_skew_21d
    ECONOMIC RATIONALE: Skewness of on_id_divergence over 21d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(21).skew()

def onid_399_on_id_divergence_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_399_on_id_divergence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of on_id_divergence over 21d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(21).kurt()

def onid_400_on_id_divergence_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_400_on_id_divergence_skew_63d
    ECONOMIC RATIONALE: Skewness of on_id_divergence over 63d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(63).skew()

def onid_401_on_id_divergence_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_401_on_id_divergence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of on_id_divergence over 63d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(63).kurt()

def onid_402_on_id_divergence_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_402_on_id_divergence_skew_126d
    ECONOMIC RATIONALE: Skewness of on_id_divergence over 126d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(126).skew()

def onid_403_on_id_divergence_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_403_on_id_divergence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of on_id_divergence over 126d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(126).kurt()

def onid_404_on_id_divergence_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_404_on_id_divergence_skew_252d
    ECONOMIC RATIONALE: Skewness of on_id_divergence over 252d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(252).skew()

def onid_405_on_id_divergence_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_405_on_id_divergence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of on_id_divergence over 252d. Divergence between overnight and intraday performance.
    """
    return ((open / close.shift(1) - 1) - (close / open - 1)).rolling(252).kurt()

def onid_406_overnight_vol_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_406_overnight_vol_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_vol over 5d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(5).skew()

def onid_407_overnight_vol_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_407_overnight_vol_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_vol over 5d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(5).kurt()

def onid_408_overnight_vol_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_408_overnight_vol_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_vol over 21d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(21).skew()

def onid_409_overnight_vol_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_409_overnight_vol_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_vol over 21d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(21).kurt()

def onid_410_overnight_vol_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_410_overnight_vol_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_vol over 63d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(63).skew()

def onid_411_overnight_vol_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_411_overnight_vol_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_vol over 63d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(63).kurt()

def onid_412_overnight_vol_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_412_overnight_vol_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_vol over 126d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(126).skew()

def onid_413_overnight_vol_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_413_overnight_vol_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_vol over 126d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(126).kurt()

def onid_414_overnight_vol_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_414_overnight_vol_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_vol over 252d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(252).skew()

def onid_415_overnight_vol_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_415_overnight_vol_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_vol over 252d. Volatility of overnight returns.
    """
    return ((open / close.shift(1) - 1).rolling(21).std()).rolling(252).kurt()

def onid_416_intraday_vol_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_416_intraday_vol_skew_5d
    ECONOMIC RATIONALE: Skewness of intraday_vol over 5d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(5).skew()

def onid_417_intraday_vol_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_417_intraday_vol_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of intraday_vol over 5d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(5).kurt()

def onid_418_intraday_vol_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_418_intraday_vol_skew_21d
    ECONOMIC RATIONALE: Skewness of intraday_vol over 21d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(21).skew()

def onid_419_intraday_vol_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_419_intraday_vol_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of intraday_vol over 21d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(21).kurt()

def onid_420_intraday_vol_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_420_intraday_vol_skew_63d
    ECONOMIC RATIONALE: Skewness of intraday_vol over 63d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(63).skew()

def onid_421_intraday_vol_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_421_intraday_vol_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of intraday_vol over 63d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(63).kurt()

def onid_422_intraday_vol_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_422_intraday_vol_skew_126d
    ECONOMIC RATIONALE: Skewness of intraday_vol over 126d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(126).skew()

def onid_423_intraday_vol_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_423_intraday_vol_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of intraday_vol over 126d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(126).kurt()

def onid_424_intraday_vol_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_424_intraday_vol_skew_252d
    ECONOMIC RATIONALE: Skewness of intraday_vol over 252d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(252).skew()

def onid_425_intraday_vol_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_425_intraday_vol_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of intraday_vol over 252d. Volatility of intraday returns.
    """
    return ((close / open - 1).rolling(21).std()).rolling(252).kurt()

def onid_426_on_id_vol_ratio_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_426_on_id_vol_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of on_id_vol_ratio over 5d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(5).skew()

def onid_427_on_id_vol_ratio_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_427_on_id_vol_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of on_id_vol_ratio over 5d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(5).kurt()

def onid_428_on_id_vol_ratio_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_428_on_id_vol_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of on_id_vol_ratio over 21d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(21).skew()

def onid_429_on_id_vol_ratio_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_429_on_id_vol_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of on_id_vol_ratio over 21d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(21).kurt()

def onid_430_on_id_vol_ratio_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_430_on_id_vol_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of on_id_vol_ratio over 63d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(63).skew()

def onid_431_on_id_vol_ratio_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_431_on_id_vol_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of on_id_vol_ratio over 63d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(63).kurt()

def onid_432_on_id_vol_ratio_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_432_on_id_vol_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of on_id_vol_ratio over 126d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(126).skew()

def onid_433_on_id_vol_ratio_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_433_on_id_vol_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of on_id_vol_ratio over 126d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(126).kurt()

def onid_434_on_id_vol_ratio_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_434_on_id_vol_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of on_id_vol_ratio over 252d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(252).skew()

def onid_435_on_id_vol_ratio_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_435_on_id_vol_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of on_id_vol_ratio over 252d. Ratio of overnight to intraday volatility.
    """
    return (((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)).rolling(252).kurt()

def onid_436_overnight_bias_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_436_overnight_bias_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_bias over 5d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(5).skew()

def onid_437_overnight_bias_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_437_overnight_bias_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_bias over 5d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(5).kurt()

def onid_438_overnight_bias_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_438_overnight_bias_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_bias over 21d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(21).skew()

def onid_439_overnight_bias_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_439_overnight_bias_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_bias over 21d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(21).kurt()

def onid_440_overnight_bias_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_440_overnight_bias_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_bias over 63d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(63).skew()

def onid_441_overnight_bias_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_441_overnight_bias_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_bias over 63d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(63).kurt()

def onid_442_overnight_bias_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_442_overnight_bias_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_bias over 126d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(126).skew()

def onid_443_overnight_bias_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_443_overnight_bias_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_bias over 126d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(126).kurt()

def onid_444_overnight_bias_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_444_overnight_bias_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_bias over 252d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(252).skew()

def onid_445_overnight_bias_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_445_overnight_bias_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_bias over 252d. Cumulative overnight return bias.
    """
    return ((open / close.shift(1) - 1).rolling(63).sum()).rolling(252).kurt()

def onid_446_intraday_bias_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_446_intraday_bias_skew_5d
    ECONOMIC RATIONALE: Skewness of intraday_bias over 5d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(5).skew()

def onid_447_intraday_bias_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_447_intraday_bias_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of intraday_bias over 5d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(5).kurt()

def onid_448_intraday_bias_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_448_intraday_bias_skew_21d
    ECONOMIC RATIONALE: Skewness of intraday_bias over 21d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(21).skew()

def onid_449_intraday_bias_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_449_intraday_bias_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of intraday_bias over 21d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(21).kurt()

def onid_450_intraday_bias_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_450_intraday_bias_skew_63d
    ECONOMIC RATIONALE: Skewness of intraday_bias over 63d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(63).skew()

def onid_451_intraday_bias_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_451_intraday_bias_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of intraday_bias over 63d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(63).kurt()

def onid_452_intraday_bias_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_452_intraday_bias_skew_126d
    ECONOMIC RATIONALE: Skewness of intraday_bias over 126d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(126).skew()

def onid_453_intraday_bias_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_453_intraday_bias_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of intraday_bias over 126d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(126).kurt()

def onid_454_intraday_bias_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_454_intraday_bias_skew_252d
    ECONOMIC RATIONALE: Skewness of intraday_bias over 252d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(252).skew()

def onid_455_intraday_bias_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_455_intraday_bias_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of intraday_bias over 252d. Cumulative intraday return bias.
    """
    return ((close / open - 1).rolling(63).sum()).rolling(252).kurt()

def onid_456_gap_fade_potential_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_456_gap_fade_potential_skew_5d
    ECONOMIC RATIONALE: Skewness of gap_fade_potential over 5d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(5).skew()

def onid_457_gap_fade_potential_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_457_gap_fade_potential_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of gap_fade_potential over 5d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(5).kurt()

def onid_458_gap_fade_potential_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_458_gap_fade_potential_skew_21d
    ECONOMIC RATIONALE: Skewness of gap_fade_potential over 21d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(21).skew()

def onid_459_gap_fade_potential_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_459_gap_fade_potential_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of gap_fade_potential over 21d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(21).kurt()

def onid_460_gap_fade_potential_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_460_gap_fade_potential_skew_63d
    ECONOMIC RATIONALE: Skewness of gap_fade_potential over 63d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(63).skew()

def onid_461_gap_fade_potential_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_461_gap_fade_potential_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of gap_fade_potential over 63d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(63).kurt()

def onid_462_gap_fade_potential_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_462_gap_fade_potential_skew_126d
    ECONOMIC RATIONALE: Skewness of gap_fade_potential over 126d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(126).skew()

def onid_463_gap_fade_potential_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_463_gap_fade_potential_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of gap_fade_potential over 126d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(126).kurt()

def onid_464_gap_fade_potential_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_464_gap_fade_potential_skew_252d
    ECONOMIC RATIONALE: Skewness of gap_fade_potential over 252d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(252).skew()

def onid_465_gap_fade_potential_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_465_gap_fade_potential_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of gap_fade_potential over 252d. Potential for intraday fading of overnight gaps.
    """
    return ((open / close.shift(1) - 1).abs() * (close / open - 1).corr(open / close.shift(1) - 1)).rolling(252).kurt()

def onid_466_overnight_gap_z_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_466_overnight_gap_z_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_gap_z over 5d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(5).skew()

def onid_467_overnight_gap_z_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_467_overnight_gap_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_z over 5d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(5).kurt()

def onid_468_overnight_gap_z_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_468_overnight_gap_z_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_gap_z over 21d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(21).skew()

def onid_469_overnight_gap_z_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_469_overnight_gap_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_z over 21d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(21).kurt()

def onid_470_overnight_gap_z_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_470_overnight_gap_z_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_gap_z over 63d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(63).skew()

def onid_471_overnight_gap_z_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_471_overnight_gap_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_z over 63d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(63).kurt()

def onid_472_overnight_gap_z_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_472_overnight_gap_z_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_gap_z over 126d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(126).skew()

def onid_473_overnight_gap_z_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_473_overnight_gap_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_z over 126d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(126).kurt()

def onid_474_overnight_gap_z_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_474_overnight_gap_z_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_gap_z over 252d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(252).skew()

def onid_475_overnight_gap_z_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_475_overnight_gap_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_gap_z over 252d. Z-score of current overnight gap.
    """
    return (_zscore_rolling(open / close.shift(1) - 1, 252)).rolling(252).kurt()

def onid_476_intraday_range_pos_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_476_intraday_range_pos_skew_5d
    ECONOMIC RATIONALE: Skewness of intraday_range_pos over 5d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(5).skew()

def onid_477_intraday_range_pos_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_477_intraday_range_pos_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of intraday_range_pos over 5d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(5).kurt()

def onid_478_intraday_range_pos_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_478_intraday_range_pos_skew_21d
    ECONOMIC RATIONALE: Skewness of intraday_range_pos over 21d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(21).skew()

def onid_479_intraday_range_pos_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_479_intraday_range_pos_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of intraday_range_pos over 21d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(21).kurt()

def onid_480_intraday_range_pos_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_480_intraday_range_pos_skew_63d
    ECONOMIC RATIONALE: Skewness of intraday_range_pos over 63d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(63).skew()

def onid_481_intraday_range_pos_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_481_intraday_range_pos_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of intraday_range_pos over 63d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(63).kurt()

def onid_482_intraday_range_pos_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_482_intraday_range_pos_skew_126d
    ECONOMIC RATIONALE: Skewness of intraday_range_pos over 126d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(126).skew()

def onid_483_intraday_range_pos_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_483_intraday_range_pos_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of intraday_range_pos over 126d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(126).kurt()

def onid_484_intraday_range_pos_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_484_intraday_range_pos_skew_252d
    ECONOMIC RATIONALE: Skewness of intraday_range_pos over 252d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(252).skew()

def onid_485_intraday_range_pos_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_485_intraday_range_pos_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of intraday_range_pos over 252d. Closing position within the intraday range.
    """
    return ((close - low) / (high - low).replace(0, 1e-9)).rolling(252).kurt()

def onid_486_overnight_momentum_lead_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_486_overnight_momentum_lead_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_momentum_lead over 5d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(5).skew()

def onid_487_overnight_momentum_lead_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_487_overnight_momentum_lead_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_momentum_lead over 5d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(5).kurt()

def onid_488_overnight_momentum_lead_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_488_overnight_momentum_lead_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_momentum_lead over 21d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(21).skew()

def onid_489_overnight_momentum_lead_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_489_overnight_momentum_lead_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_momentum_lead over 21d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(21).kurt()

def onid_490_overnight_momentum_lead_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_490_overnight_momentum_lead_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_momentum_lead over 63d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(63).skew()

def onid_491_overnight_momentum_lead_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_491_overnight_momentum_lead_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_momentum_lead over 63d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(63).kurt()

def onid_492_overnight_momentum_lead_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_492_overnight_momentum_lead_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_momentum_lead over 126d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(126).skew()

def onid_493_overnight_momentum_lead_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_493_overnight_momentum_lead_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_momentum_lead over 126d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(126).kurt()

def onid_494_overnight_momentum_lead_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_494_overnight_momentum_lead_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_momentum_lead over 252d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(252).skew()

def onid_495_overnight_momentum_lead_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_495_overnight_momentum_lead_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_momentum_lead over 252d. Lead of overnight momentum over intraday.
    """
    return ((open / close.shift(1) - 1).rolling(5).mean() / (close / open - 1).rolling(5).mean().replace(0, 1e-9)).rolling(252).kurt()

def onid_496_id_reversal_strength_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_496_id_reversal_strength_skew_5d
    ECONOMIC RATIONALE: Skewness of id_reversal_strength over 5d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(5).skew()

def onid_497_id_reversal_strength_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_497_id_reversal_strength_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of id_reversal_strength over 5d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(5).kurt()

def onid_498_id_reversal_strength_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_498_id_reversal_strength_skew_21d
    ECONOMIC RATIONALE: Skewness of id_reversal_strength over 21d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(21).skew()

def onid_499_id_reversal_strength_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_499_id_reversal_strength_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of id_reversal_strength over 21d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(21).kurt()

def onid_500_id_reversal_strength_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_500_id_reversal_strength_skew_63d
    ECONOMIC RATIONALE: Skewness of id_reversal_strength over 63d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(63).skew()

def onid_501_id_reversal_strength_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_501_id_reversal_strength_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of id_reversal_strength over 63d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(63).kurt()

def onid_502_id_reversal_strength_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_502_id_reversal_strength_skew_126d
    ECONOMIC RATIONALE: Skewness of id_reversal_strength over 126d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(126).skew()

def onid_503_id_reversal_strength_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_503_id_reversal_strength_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of id_reversal_strength over 126d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(126).kurt()

def onid_504_id_reversal_strength_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_504_id_reversal_strength_skew_252d
    ECONOMIC RATIONALE: Skewness of id_reversal_strength over 252d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(252).skew()

def onid_505_id_reversal_strength_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_505_id_reversal_strength_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of id_reversal_strength over 252d. Frequency of intraday reversals of overnight moves.
    """
    return (((close - open) * (open - close.shift(1)) < 0).rolling(21).mean()).rolling(252).kurt()

def onid_506_on_id_correlation_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_506_on_id_correlation_skew_5d
    ECONOMIC RATIONALE: Skewness of on_id_correlation over 5d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(5).skew()

def onid_507_on_id_correlation_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_507_on_id_correlation_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of on_id_correlation over 5d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(5).kurt()

def onid_508_on_id_correlation_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_508_on_id_correlation_skew_21d
    ECONOMIC RATIONALE: Skewness of on_id_correlation over 21d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(21).skew()

def onid_509_on_id_correlation_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_509_on_id_correlation_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of on_id_correlation over 21d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(21).kurt()

def onid_510_on_id_correlation_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_510_on_id_correlation_skew_63d
    ECONOMIC RATIONALE: Skewness of on_id_correlation over 63d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(63).skew()

def onid_511_on_id_correlation_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_511_on_id_correlation_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of on_id_correlation over 63d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(63).kurt()

def onid_512_on_id_correlation_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_512_on_id_correlation_skew_126d
    ECONOMIC RATIONALE: Skewness of on_id_correlation over 126d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(126).skew()

def onid_513_on_id_correlation_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_513_on_id_correlation_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of on_id_correlation over 126d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(126).kurt()

def onid_514_on_id_correlation_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_514_on_id_correlation_skew_252d
    ECONOMIC RATIONALE: Skewness of on_id_correlation over 252d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(252).skew()

def onid_515_on_id_correlation_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_515_on_id_correlation_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of on_id_correlation over 252d. Correlation between overnight and intraday returns.
    """
    return ((open / close.shift(1) - 1).rolling(63).corr(close / open - 1)).rolling(252).kurt()

def onid_516_overnight_shock_flag_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_516_overnight_shock_flag_skew_5d
    ECONOMIC RATIONALE: Skewness of overnight_shock_flag over 5d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(5).skew()

def onid_517_overnight_shock_flag_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_517_overnight_shock_flag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of overnight_shock_flag over 5d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(5).kurt()

def onid_518_overnight_shock_flag_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_518_overnight_shock_flag_skew_21d
    ECONOMIC RATIONALE: Skewness of overnight_shock_flag over 21d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(21).skew()

def onid_519_overnight_shock_flag_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_519_overnight_shock_flag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of overnight_shock_flag over 21d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(21).kurt()

def onid_520_overnight_shock_flag_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_520_overnight_shock_flag_skew_63d
    ECONOMIC RATIONALE: Skewness of overnight_shock_flag over 63d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(63).skew()

def onid_521_overnight_shock_flag_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_521_overnight_shock_flag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of overnight_shock_flag over 63d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(63).kurt()

def onid_522_overnight_shock_flag_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_522_overnight_shock_flag_skew_126d
    ECONOMIC RATIONALE: Skewness of overnight_shock_flag over 126d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(126).skew()

def onid_523_overnight_shock_flag_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_523_overnight_shock_flag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of overnight_shock_flag over 126d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(126).kurt()

def onid_524_overnight_shock_flag_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_524_overnight_shock_flag_skew_252d
    ECONOMIC RATIONALE: Skewness of overnight_shock_flag over 252d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(252).skew()

def onid_525_overnight_shock_flag_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_525_overnight_shock_flag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of overnight_shock_flag over 252d. Binary indicator of extreme overnight price shocks.
    """
    return ((abs(open / close.shift(1) - 1) > 2*(open / close.shift(1) - 1).rolling(252).std()).astype(float)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V114_REGISTRY_MOMENTS = {
    "onid_376_overnight_return_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_376_overnight_return_skew_5d},
    "onid_377_overnight_return_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_377_overnight_return_kurt_5d},
    "onid_378_overnight_return_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_378_overnight_return_skew_21d},
    "onid_379_overnight_return_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_379_overnight_return_kurt_21d},
    "onid_380_overnight_return_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_380_overnight_return_skew_63d},
    "onid_381_overnight_return_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_381_overnight_return_kurt_63d},
    "onid_382_overnight_return_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_382_overnight_return_skew_126d},
    "onid_383_overnight_return_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_383_overnight_return_kurt_126d},
    "onid_384_overnight_return_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_384_overnight_return_skew_252d},
    "onid_385_overnight_return_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_385_overnight_return_kurt_252d},
    "onid_386_intraday_return_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_386_intraday_return_skew_5d},
    "onid_387_intraday_return_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_387_intraday_return_kurt_5d},
    "onid_388_intraday_return_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_388_intraday_return_skew_21d},
    "onid_389_intraday_return_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_389_intraday_return_kurt_21d},
    "onid_390_intraday_return_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_390_intraday_return_skew_63d},
    "onid_391_intraday_return_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_391_intraday_return_kurt_63d},
    "onid_392_intraday_return_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_392_intraday_return_skew_126d},
    "onid_393_intraday_return_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_393_intraday_return_kurt_126d},
    "onid_394_intraday_return_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_394_intraday_return_skew_252d},
    "onid_395_intraday_return_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_395_intraday_return_kurt_252d},
    "onid_396_on_id_divergence_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_396_on_id_divergence_skew_5d},
    "onid_397_on_id_divergence_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_397_on_id_divergence_kurt_5d},
    "onid_398_on_id_divergence_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_398_on_id_divergence_skew_21d},
    "onid_399_on_id_divergence_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_399_on_id_divergence_kurt_21d},
    "onid_400_on_id_divergence_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_400_on_id_divergence_skew_63d},
    "onid_401_on_id_divergence_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_401_on_id_divergence_kurt_63d},
    "onid_402_on_id_divergence_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_402_on_id_divergence_skew_126d},
    "onid_403_on_id_divergence_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_403_on_id_divergence_kurt_126d},
    "onid_404_on_id_divergence_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_404_on_id_divergence_skew_252d},
    "onid_405_on_id_divergence_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_405_on_id_divergence_kurt_252d},
    "onid_406_overnight_vol_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_406_overnight_vol_skew_5d},
    "onid_407_overnight_vol_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_407_overnight_vol_kurt_5d},
    "onid_408_overnight_vol_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_408_overnight_vol_skew_21d},
    "onid_409_overnight_vol_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_409_overnight_vol_kurt_21d},
    "onid_410_overnight_vol_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_410_overnight_vol_skew_63d},
    "onid_411_overnight_vol_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_411_overnight_vol_kurt_63d},
    "onid_412_overnight_vol_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_412_overnight_vol_skew_126d},
    "onid_413_overnight_vol_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_413_overnight_vol_kurt_126d},
    "onid_414_overnight_vol_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_414_overnight_vol_skew_252d},
    "onid_415_overnight_vol_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_415_overnight_vol_kurt_252d},
    "onid_416_intraday_vol_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_416_intraday_vol_skew_5d},
    "onid_417_intraday_vol_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_417_intraday_vol_kurt_5d},
    "onid_418_intraday_vol_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_418_intraday_vol_skew_21d},
    "onid_419_intraday_vol_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_419_intraday_vol_kurt_21d},
    "onid_420_intraday_vol_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_420_intraday_vol_skew_63d},
    "onid_421_intraday_vol_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_421_intraday_vol_kurt_63d},
    "onid_422_intraday_vol_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_422_intraday_vol_skew_126d},
    "onid_423_intraday_vol_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_423_intraday_vol_kurt_126d},
    "onid_424_intraday_vol_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_424_intraday_vol_skew_252d},
    "onid_425_intraday_vol_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_425_intraday_vol_kurt_252d},
    "onid_426_on_id_vol_ratio_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_426_on_id_vol_ratio_skew_5d},
    "onid_427_on_id_vol_ratio_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_427_on_id_vol_ratio_kurt_5d},
    "onid_428_on_id_vol_ratio_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_428_on_id_vol_ratio_skew_21d},
    "onid_429_on_id_vol_ratio_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_429_on_id_vol_ratio_kurt_21d},
    "onid_430_on_id_vol_ratio_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_430_on_id_vol_ratio_skew_63d},
    "onid_431_on_id_vol_ratio_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_431_on_id_vol_ratio_kurt_63d},
    "onid_432_on_id_vol_ratio_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_432_on_id_vol_ratio_skew_126d},
    "onid_433_on_id_vol_ratio_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_433_on_id_vol_ratio_kurt_126d},
    "onid_434_on_id_vol_ratio_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_434_on_id_vol_ratio_skew_252d},
    "onid_435_on_id_vol_ratio_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_435_on_id_vol_ratio_kurt_252d},
    "onid_436_overnight_bias_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_436_overnight_bias_skew_5d},
    "onid_437_overnight_bias_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_437_overnight_bias_kurt_5d},
    "onid_438_overnight_bias_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_438_overnight_bias_skew_21d},
    "onid_439_overnight_bias_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_439_overnight_bias_kurt_21d},
    "onid_440_overnight_bias_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_440_overnight_bias_skew_63d},
    "onid_441_overnight_bias_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_441_overnight_bias_kurt_63d},
    "onid_442_overnight_bias_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_442_overnight_bias_skew_126d},
    "onid_443_overnight_bias_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_443_overnight_bias_kurt_126d},
    "onid_444_overnight_bias_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_444_overnight_bias_skew_252d},
    "onid_445_overnight_bias_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_445_overnight_bias_kurt_252d},
    "onid_446_intraday_bias_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_446_intraday_bias_skew_5d},
    "onid_447_intraday_bias_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_447_intraday_bias_kurt_5d},
    "onid_448_intraday_bias_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_448_intraday_bias_skew_21d},
    "onid_449_intraday_bias_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_449_intraday_bias_kurt_21d},
    "onid_450_intraday_bias_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_450_intraday_bias_skew_63d},
    "onid_451_intraday_bias_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_451_intraday_bias_kurt_63d},
    "onid_452_intraday_bias_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_452_intraday_bias_skew_126d},
    "onid_453_intraday_bias_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_453_intraday_bias_kurt_126d},
    "onid_454_intraday_bias_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_454_intraday_bias_skew_252d},
    "onid_455_intraday_bias_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_455_intraday_bias_kurt_252d},
    "onid_456_gap_fade_potential_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_456_gap_fade_potential_skew_5d},
    "onid_457_gap_fade_potential_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_457_gap_fade_potential_kurt_5d},
    "onid_458_gap_fade_potential_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_458_gap_fade_potential_skew_21d},
    "onid_459_gap_fade_potential_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_459_gap_fade_potential_kurt_21d},
    "onid_460_gap_fade_potential_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_460_gap_fade_potential_skew_63d},
    "onid_461_gap_fade_potential_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_461_gap_fade_potential_kurt_63d},
    "onid_462_gap_fade_potential_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_462_gap_fade_potential_skew_126d},
    "onid_463_gap_fade_potential_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_463_gap_fade_potential_kurt_126d},
    "onid_464_gap_fade_potential_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_464_gap_fade_potential_skew_252d},
    "onid_465_gap_fade_potential_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_465_gap_fade_potential_kurt_252d},
    "onid_466_overnight_gap_z_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_466_overnight_gap_z_skew_5d},
    "onid_467_overnight_gap_z_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_467_overnight_gap_z_kurt_5d},
    "onid_468_overnight_gap_z_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_468_overnight_gap_z_skew_21d},
    "onid_469_overnight_gap_z_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_469_overnight_gap_z_kurt_21d},
    "onid_470_overnight_gap_z_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_470_overnight_gap_z_skew_63d},
    "onid_471_overnight_gap_z_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_471_overnight_gap_z_kurt_63d},
    "onid_472_overnight_gap_z_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_472_overnight_gap_z_skew_126d},
    "onid_473_overnight_gap_z_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_473_overnight_gap_z_kurt_126d},
    "onid_474_overnight_gap_z_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_474_overnight_gap_z_skew_252d},
    "onid_475_overnight_gap_z_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_475_overnight_gap_z_kurt_252d},
    "onid_476_intraday_range_pos_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_476_intraday_range_pos_skew_5d},
    "onid_477_intraday_range_pos_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_477_intraday_range_pos_kurt_5d},
    "onid_478_intraday_range_pos_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_478_intraday_range_pos_skew_21d},
    "onid_479_intraday_range_pos_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_479_intraday_range_pos_kurt_21d},
    "onid_480_intraday_range_pos_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_480_intraday_range_pos_skew_63d},
    "onid_481_intraday_range_pos_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_481_intraday_range_pos_kurt_63d},
    "onid_482_intraday_range_pos_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_482_intraday_range_pos_skew_126d},
    "onid_483_intraday_range_pos_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_483_intraday_range_pos_kurt_126d},
    "onid_484_intraday_range_pos_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_484_intraday_range_pos_skew_252d},
    "onid_485_intraday_range_pos_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_485_intraday_range_pos_kurt_252d},
    "onid_486_overnight_momentum_lead_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_486_overnight_momentum_lead_skew_5d},
    "onid_487_overnight_momentum_lead_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_487_overnight_momentum_lead_kurt_5d},
    "onid_488_overnight_momentum_lead_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_488_overnight_momentum_lead_skew_21d},
    "onid_489_overnight_momentum_lead_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_489_overnight_momentum_lead_kurt_21d},
    "onid_490_overnight_momentum_lead_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_490_overnight_momentum_lead_skew_63d},
    "onid_491_overnight_momentum_lead_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_491_overnight_momentum_lead_kurt_63d},
    "onid_492_overnight_momentum_lead_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_492_overnight_momentum_lead_skew_126d},
    "onid_493_overnight_momentum_lead_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_493_overnight_momentum_lead_kurt_126d},
    "onid_494_overnight_momentum_lead_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_494_overnight_momentum_lead_skew_252d},
    "onid_495_overnight_momentum_lead_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_495_overnight_momentum_lead_kurt_252d},
    "onid_496_id_reversal_strength_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_496_id_reversal_strength_skew_5d},
    "onid_497_id_reversal_strength_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_497_id_reversal_strength_kurt_5d},
    "onid_498_id_reversal_strength_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_498_id_reversal_strength_skew_21d},
    "onid_499_id_reversal_strength_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_499_id_reversal_strength_kurt_21d},
    "onid_500_id_reversal_strength_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_500_id_reversal_strength_skew_63d},
    "onid_501_id_reversal_strength_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_501_id_reversal_strength_kurt_63d},
    "onid_502_id_reversal_strength_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_502_id_reversal_strength_skew_126d},
    "onid_503_id_reversal_strength_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_503_id_reversal_strength_kurt_126d},
    "onid_504_id_reversal_strength_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_504_id_reversal_strength_skew_252d},
    "onid_505_id_reversal_strength_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_505_id_reversal_strength_kurt_252d},
    "onid_506_on_id_correlation_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_506_on_id_correlation_skew_5d},
    "onid_507_on_id_correlation_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_507_on_id_correlation_kurt_5d},
    "onid_508_on_id_correlation_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_508_on_id_correlation_skew_21d},
    "onid_509_on_id_correlation_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_509_on_id_correlation_kurt_21d},
    "onid_510_on_id_correlation_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_510_on_id_correlation_skew_63d},
    "onid_511_on_id_correlation_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_511_on_id_correlation_kurt_63d},
    "onid_512_on_id_correlation_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_512_on_id_correlation_skew_126d},
    "onid_513_on_id_correlation_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_513_on_id_correlation_kurt_126d},
    "onid_514_on_id_correlation_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_514_on_id_correlation_skew_252d},
    "onid_515_on_id_correlation_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_515_on_id_correlation_kurt_252d},
    "onid_516_overnight_shock_flag_skew_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_516_overnight_shock_flag_skew_5d},
    "onid_517_overnight_shock_flag_kurt_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_517_overnight_shock_flag_kurt_5d},
    "onid_518_overnight_shock_flag_skew_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_518_overnight_shock_flag_skew_21d},
    "onid_519_overnight_shock_flag_kurt_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_519_overnight_shock_flag_kurt_21d},
    "onid_520_overnight_shock_flag_skew_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_520_overnight_shock_flag_skew_63d},
    "onid_521_overnight_shock_flag_kurt_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_521_overnight_shock_flag_kurt_63d},
    "onid_522_overnight_shock_flag_skew_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_522_overnight_shock_flag_skew_126d},
    "onid_523_overnight_shock_flag_kurt_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_523_overnight_shock_flag_kurt_126d},
    "onid_524_overnight_shock_flag_skew_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_524_overnight_shock_flag_skew_252d},
    "onid_525_overnight_shock_flag_kurt_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_525_overnight_shock_flag_kurt_252d},
}
