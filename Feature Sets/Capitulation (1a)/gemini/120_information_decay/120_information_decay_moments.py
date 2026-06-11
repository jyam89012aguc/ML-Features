"""
120_information_decay — Statistical Moments
Domain: information_decay
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

def idec_376_price_impact_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_376_price_impact_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of price_impact_decay over 5d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(5).skew()

def idec_377_price_impact_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_377_price_impact_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_impact_decay over 5d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(5).kurt()

def idec_378_price_impact_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_378_price_impact_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of price_impact_decay over 21d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(21).skew()

def idec_379_price_impact_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_379_price_impact_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_impact_decay over 21d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(21).kurt()

def idec_380_price_impact_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_380_price_impact_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of price_impact_decay over 63d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(63).skew()

def idec_381_price_impact_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_381_price_impact_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_impact_decay over 63d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(63).kurt()

def idec_382_price_impact_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_382_price_impact_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of price_impact_decay over 126d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(126).skew()

def idec_383_price_impact_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_383_price_impact_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_impact_decay over 126d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(126).kurt()

def idec_384_price_impact_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_384_price_impact_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of price_impact_decay over 252d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(252).skew()

def idec_385_price_impact_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_385_price_impact_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_impact_decay over 252d. Decaying magnitude of recent price impacts.
    """
    return (close.diff(1).abs().ewm(halflife=5).mean()).rolling(252).kurt()

def idec_386_volume_impact_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_386_volume_impact_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_impact_decay over 5d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(5).skew()

def idec_387_volume_impact_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_387_volume_impact_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_impact_decay over 5d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(5).kurt()

def idec_388_volume_impact_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_388_volume_impact_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_impact_decay over 21d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(21).skew()

def idec_389_volume_impact_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_389_volume_impact_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_impact_decay over 21d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(21).kurt()

def idec_390_volume_impact_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_390_volume_impact_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_impact_decay over 63d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(63).skew()

def idec_391_volume_impact_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_391_volume_impact_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_impact_decay over 63d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(63).kurt()

def idec_392_volume_impact_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_392_volume_impact_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_impact_decay over 126d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(126).skew()

def idec_393_volume_impact_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_393_volume_impact_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_impact_decay over 126d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(126).kurt()

def idec_394_volume_impact_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_394_volume_impact_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_impact_decay over 252d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(252).skew()

def idec_395_volume_impact_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_395_volume_impact_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_impact_decay over 252d. Decaying intensity of recent volume spikes.
    """
    return (volume.ewm(halflife=5).mean() / volume.rolling(63).mean()).rolling(252).kurt()

def idec_396_information_horizon_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_396_information_horizon_skew_5d
    ECONOMIC RATIONALE: Skewness of information_horizon over 5d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(5).skew()

def idec_397_information_horizon_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_397_information_horizon_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of information_horizon over 5d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(5).kurt()

def idec_398_information_horizon_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_398_information_horizon_skew_21d
    ECONOMIC RATIONALE: Skewness of information_horizon over 21d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(21).skew()

def idec_399_information_horizon_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_399_information_horizon_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of information_horizon over 21d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(21).kurt()

def idec_400_information_horizon_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_400_information_horizon_skew_63d
    ECONOMIC RATIONALE: Skewness of information_horizon over 63d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(63).skew()

def idec_401_information_horizon_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_401_information_horizon_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of information_horizon over 63d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(63).kurt()

def idec_402_information_horizon_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_402_information_horizon_skew_126d
    ECONOMIC RATIONALE: Skewness of information_horizon over 126d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(126).skew()

def idec_403_information_horizon_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_403_information_horizon_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of information_horizon over 126d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(126).kurt()

def idec_404_information_horizon_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_404_information_horizon_skew_252d
    ECONOMIC RATIONALE: Skewness of information_horizon over 252d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(252).skew()

def idec_405_information_horizon_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_405_information_horizon_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of information_horizon over 252d. Long-term memory of price levels.
    """
    return (close.rolling(21).corr(close.shift(21))).rolling(252).kurt()

def idec_406_news_response_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_406_news_response_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of news_response_decay over 5d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(5).skew()

def idec_407_news_response_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_407_news_response_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of news_response_decay over 5d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(5).kurt()

def idec_408_news_response_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_408_news_response_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of news_response_decay over 21d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(21).skew()

def idec_409_news_response_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_409_news_response_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of news_response_decay over 21d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(21).kurt()

def idec_410_news_response_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_410_news_response_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of news_response_decay over 63d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(63).skew()

def idec_411_news_response_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_411_news_response_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of news_response_decay over 63d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(63).kurt()

def idec_412_news_response_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_412_news_response_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of news_response_decay over 126d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(126).skew()

def idec_413_news_response_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_413_news_response_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of news_response_decay over 126d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(126).kurt()

def idec_414_news_response_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_414_news_response_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of news_response_decay over 252d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(252).skew()

def idec_415_news_response_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_415_news_response_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of news_response_decay over 252d. Recent daily change relative to cumulative monthly change.
    """
    return (close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)).rolling(252).kurt()

def idec_416_autocorr_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_416_autocorr_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of autocorr_decay over 5d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(5).skew()

def idec_417_autocorr_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_417_autocorr_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of autocorr_decay over 5d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(5).kurt()

def idec_418_autocorr_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_418_autocorr_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of autocorr_decay over 21d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(21).skew()

def idec_419_autocorr_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_419_autocorr_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of autocorr_decay over 21d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(21).kurt()

def idec_420_autocorr_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_420_autocorr_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of autocorr_decay over 63d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(63).skew()

def idec_421_autocorr_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_421_autocorr_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of autocorr_decay over 63d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(63).kurt()

def idec_422_autocorr_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_422_autocorr_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of autocorr_decay over 126d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(126).skew()

def idec_423_autocorr_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_423_autocorr_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of autocorr_decay over 126d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(126).kurt()

def idec_424_autocorr_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_424_autocorr_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of autocorr_decay over 252d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(252).skew()

def idec_425_autocorr_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_425_autocorr_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of autocorr_decay over 252d. Decay in serial correlation across timeframes.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)).rolling(252).kurt()

def idec_426_volatility_mean_reversion_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_426_volatility_mean_reversion_skew_5d
    ECONOMIC RATIONALE: Skewness of volatility_mean_reversion over 5d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(5).skew()

def idec_427_volatility_mean_reversion_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_427_volatility_mean_reversion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volatility_mean_reversion over 5d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(5).kurt()

def idec_428_volatility_mean_reversion_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_428_volatility_mean_reversion_skew_21d
    ECONOMIC RATIONALE: Skewness of volatility_mean_reversion over 21d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(21).skew()

def idec_429_volatility_mean_reversion_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_429_volatility_mean_reversion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volatility_mean_reversion over 21d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(21).kurt()

def idec_430_volatility_mean_reversion_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_430_volatility_mean_reversion_skew_63d
    ECONOMIC RATIONALE: Skewness of volatility_mean_reversion over 63d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(63).skew()

def idec_431_volatility_mean_reversion_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_431_volatility_mean_reversion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volatility_mean_reversion over 63d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(63).kurt()

def idec_432_volatility_mean_reversion_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_432_volatility_mean_reversion_skew_126d
    ECONOMIC RATIONALE: Skewness of volatility_mean_reversion over 126d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(126).skew()

def idec_433_volatility_mean_reversion_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_433_volatility_mean_reversion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volatility_mean_reversion over 126d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(126).kurt()

def idec_434_volatility_mean_reversion_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_434_volatility_mean_reversion_skew_252d
    ECONOMIC RATIONALE: Skewness of volatility_mean_reversion over 252d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(252).skew()

def idec_435_volatility_mean_reversion_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_435_volatility_mean_reversion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volatility_mean_reversion over 252d. Rate at which short-term vol returns to the long-term mean.
    """
    return (close.rolling(21).std() / close.rolling(252).std()).rolling(252).kurt()

def idec_436_information_efficiency_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_436_information_efficiency_skew_5d
    ECONOMIC RATIONALE: Skewness of information_efficiency over 5d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(5).skew()

def idec_437_information_efficiency_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_437_information_efficiency_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of information_efficiency over 5d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(5).kurt()

def idec_438_information_efficiency_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_438_information_efficiency_skew_21d
    ECONOMIC RATIONALE: Skewness of information_efficiency over 21d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(21).skew()

def idec_439_information_efficiency_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_439_information_efficiency_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of information_efficiency over 21d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(21).kurt()

def idec_440_information_efficiency_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_440_information_efficiency_skew_63d
    ECONOMIC RATIONALE: Skewness of information_efficiency over 63d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(63).skew()

def idec_441_information_efficiency_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_441_information_efficiency_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of information_efficiency over 63d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(63).kurt()

def idec_442_information_efficiency_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_442_information_efficiency_skew_126d
    ECONOMIC RATIONALE: Skewness of information_efficiency over 126d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(126).skew()

def idec_443_information_efficiency_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_443_information_efficiency_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of information_efficiency over 126d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(126).kurt()

def idec_444_information_efficiency_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_444_information_efficiency_skew_252d
    ECONOMIC RATIONALE: Skewness of information_efficiency over 252d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(252).skew()

def idec_445_information_efficiency_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_445_information_efficiency_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of information_efficiency over 252d. Rate of information incorporation into price.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(252).kurt()

def idec_446_signal_noise_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_446_signal_noise_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of signal_noise_decay over 5d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(5).skew()

def idec_447_signal_noise_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_447_signal_noise_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of signal_noise_decay over 5d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(5).kurt()

def idec_448_signal_noise_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_448_signal_noise_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of signal_noise_decay over 21d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(21).skew()

def idec_449_signal_noise_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_449_signal_noise_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of signal_noise_decay over 21d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(21).kurt()

def idec_450_signal_noise_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_450_signal_noise_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of signal_noise_decay over 63d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(63).skew()

def idec_451_signal_noise_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_451_signal_noise_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of signal_noise_decay over 63d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(63).kurt()

def idec_452_signal_noise_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_452_signal_noise_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of signal_noise_decay over 126d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(126).skew()

def idec_453_signal_noise_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_453_signal_noise_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of signal_noise_decay over 126d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(126).kurt()

def idec_454_signal_noise_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_454_signal_noise_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of signal_noise_decay over 252d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(252).skew()

def idec_455_signal_noise_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_455_signal_noise_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of signal_noise_decay over 252d. Decay of signal strength relative to noise.
    """
    return (close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(252).kurt()

def idec_456_memory_length_proxy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_456_memory_length_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of memory_length_proxy over 5d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(5).skew()

def idec_457_memory_length_proxy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_457_memory_length_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of memory_length_proxy over 5d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(5).kurt()

def idec_458_memory_length_proxy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_458_memory_length_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of memory_length_proxy over 21d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(21).skew()

def idec_459_memory_length_proxy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_459_memory_length_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of memory_length_proxy over 21d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(21).kurt()

def idec_460_memory_length_proxy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_460_memory_length_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of memory_length_proxy over 63d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(63).skew()

def idec_461_memory_length_proxy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_461_memory_length_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of memory_length_proxy over 63d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(63).kurt()

def idec_462_memory_length_proxy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_462_memory_length_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of memory_length_proxy over 126d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(126).skew()

def idec_463_memory_length_proxy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_463_memory_length_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of memory_length_proxy over 126d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(126).kurt()

def idec_464_memory_length_proxy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_464_memory_length_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of memory_length_proxy over 252d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(252).skew()

def idec_465_memory_length_proxy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_465_memory_length_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of memory_length_proxy over 252d. Estimated length of price memory.
    """
    return (close.rolling(252).apply(lambda x: np.argmax(np.correlate(x-np.mean(x), x-np.mean(x), mode='full')[len(x):]))).rolling(252).kurt()

def idec_466_information_shock_persistence_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_466_information_shock_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of information_shock_persistence over 5d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(5).skew()

def idec_467_information_shock_persistence_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_467_information_shock_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of information_shock_persistence over 5d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(5).kurt()

def idec_468_information_shock_persistence_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_468_information_shock_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of information_shock_persistence over 21d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(21).skew()

def idec_469_information_shock_persistence_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_469_information_shock_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of information_shock_persistence over 21d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(21).kurt()

def idec_470_information_shock_persistence_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_470_information_shock_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of information_shock_persistence over 63d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(63).skew()

def idec_471_information_shock_persistence_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_471_information_shock_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of information_shock_persistence over 63d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(63).kurt()

def idec_472_information_shock_persistence_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_472_information_shock_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of information_shock_persistence over 126d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(126).skew()

def idec_473_information_shock_persistence_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_473_information_shock_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of information_shock_persistence over 126d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(126).kurt()

def idec_474_information_shock_persistence_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_474_information_shock_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of information_shock_persistence over 252d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(252).skew()

def idec_475_information_shock_persistence_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_475_information_shock_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of information_shock_persistence over 252d. Persistence of information-driven price volatility.
    """
    return (close.diff(1).abs().rolling(21).mean() / close.diff(1).abs().rolling(252).mean()).rolling(252).kurt()

def idec_476_drift_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_476_drift_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of drift_decay over 5d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(5).skew()

def idec_477_drift_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_477_drift_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drift_decay over 5d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(5).kurt()

def idec_478_drift_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_478_drift_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of drift_decay over 21d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(21).skew()

def idec_479_drift_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_479_drift_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drift_decay over 21d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(21).kurt()

def idec_480_drift_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_480_drift_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of drift_decay over 63d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(63).skew()

def idec_481_drift_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_481_drift_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drift_decay over 63d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(63).kurt()

def idec_482_drift_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_482_drift_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of drift_decay over 126d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(126).skew()

def idec_483_drift_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_483_drift_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drift_decay over 126d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(126).kurt()

def idec_484_drift_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_484_drift_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of drift_decay over 252d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(252).skew()

def idec_485_drift_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_485_drift_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drift_decay over 252d. Decay of short-term drift relative to quarterly trend.
    """
    return (close.pct_change(5).abs() / close.pct_change(63).abs().replace(0, 1e-9)).rolling(252).kurt()

def idec_486_information_entropy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_486_information_entropy_skew_5d
    ECONOMIC RATIONALE: Skewness of information_entropy over 5d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(5).skew()

def idec_487_information_entropy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_487_information_entropy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of information_entropy over 5d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(5).kurt()

def idec_488_information_entropy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_488_information_entropy_skew_21d
    ECONOMIC RATIONALE: Skewness of information_entropy over 21d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(21).skew()

def idec_489_information_entropy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_489_information_entropy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of information_entropy over 21d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(21).kurt()

def idec_490_information_entropy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_490_information_entropy_skew_63d
    ECONOMIC RATIONALE: Skewness of information_entropy over 63d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(63).skew()

def idec_491_information_entropy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_491_information_entropy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of information_entropy over 63d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(63).kurt()

def idec_492_information_entropy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_492_information_entropy_skew_126d
    ECONOMIC RATIONALE: Skewness of information_entropy over 126d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(126).skew()

def idec_493_information_entropy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_493_information_entropy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of information_entropy over 126d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(126).kurt()

def idec_494_information_entropy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_494_information_entropy_skew_252d
    ECONOMIC RATIONALE: Skewness of information_entropy over 252d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(252).skew()

def idec_495_information_entropy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_495_information_entropy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of information_entropy over 252d. Uncertainty or decay of information in price returns.
    """
    return (close.pct_change(1).rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))).rolling(252).kurt()

def idec_496_volume_memory_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_496_volume_memory_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_memory_decay over 5d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(5).skew()

def idec_497_volume_memory_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_497_volume_memory_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_memory_decay over 5d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(5).kurt()

def idec_498_volume_memory_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_498_volume_memory_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_memory_decay over 21d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(21).skew()

def idec_499_volume_memory_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_499_volume_memory_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_memory_decay over 21d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(21).kurt()

def idec_500_volume_memory_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_500_volume_memory_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_memory_decay over 63d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(63).skew()

def idec_501_volume_memory_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_501_volume_memory_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_memory_decay over 63d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(63).kurt()

def idec_502_volume_memory_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_502_volume_memory_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_memory_decay over 126d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(126).skew()

def idec_503_volume_memory_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_503_volume_memory_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_memory_decay over 126d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(126).kurt()

def idec_504_volume_memory_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_504_volume_memory_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_memory_decay over 252d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(252).skew()

def idec_505_volume_memory_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_505_volume_memory_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_memory_decay over 252d. Persistence of volume regimes.
    """
    return (volume.rolling(21).corr(volume.shift(21))).rolling(252).kurt()

def idec_506_price_stickiness_decay_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_506_price_stickiness_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of price_stickiness_decay over 5d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(5).skew()

def idec_507_price_stickiness_decay_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_507_price_stickiness_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness_decay over 5d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(5).kurt()

def idec_508_price_stickiness_decay_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_508_price_stickiness_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of price_stickiness_decay over 21d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(21).skew()

def idec_509_price_stickiness_decay_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_509_price_stickiness_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness_decay over 21d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(21).kurt()

def idec_510_price_stickiness_decay_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_510_price_stickiness_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of price_stickiness_decay over 63d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(63).skew()

def idec_511_price_stickiness_decay_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_511_price_stickiness_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness_decay over 63d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(63).kurt()

def idec_512_price_stickiness_decay_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_512_price_stickiness_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of price_stickiness_decay over 126d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(126).skew()

def idec_513_price_stickiness_decay_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_513_price_stickiness_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness_decay over 126d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(126).kurt()

def idec_514_price_stickiness_decay_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_514_price_stickiness_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of price_stickiness_decay over 252d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(252).skew()

def idec_515_price_stickiness_decay_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_515_price_stickiness_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_stickiness_decay over 252d. Change in the rate of price stagnation.
    """
    return ((close.diff(1).abs() < 0.01).rolling(21).mean().diff(21)).rolling(252).kurt()

def idec_516_information_flow_acceleration_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_516_information_flow_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of information_flow_acceleration over 5d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(5).skew()

def idec_517_information_flow_acceleration_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_517_information_flow_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of information_flow_acceleration over 5d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(5).kurt()

def idec_518_information_flow_acceleration_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_518_information_flow_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of information_flow_acceleration over 21d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(21).skew()

def idec_519_information_flow_acceleration_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_519_information_flow_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of information_flow_acceleration over 21d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(21).kurt()

def idec_520_information_flow_acceleration_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_520_information_flow_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of information_flow_acceleration over 63d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(63).skew()

def idec_521_information_flow_acceleration_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_521_information_flow_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of information_flow_acceleration over 63d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(63).kurt()

def idec_522_information_flow_acceleration_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_522_information_flow_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of information_flow_acceleration over 126d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(126).skew()

def idec_523_information_flow_acceleration_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_523_information_flow_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of information_flow_acceleration over 126d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(126).kurt()

def idec_524_information_flow_acceleration_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_524_information_flow_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of information_flow_acceleration over 252d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(252).skew()

def idec_525_information_flow_acceleration_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_525_information_flow_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of information_flow_acceleration over 252d. Acceleration of information flow into price.
    """
    return (close.diff(1).abs().ewm(span=5).mean() / close.diff(1).abs().ewm(span=63).mean()).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V120_REGISTRY_MOMENTS = {
    "idec_376_price_impact_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_376_price_impact_decay_skew_5d},
    "idec_377_price_impact_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_377_price_impact_decay_kurt_5d},
    "idec_378_price_impact_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_378_price_impact_decay_skew_21d},
    "idec_379_price_impact_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_379_price_impact_decay_kurt_21d},
    "idec_380_price_impact_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_380_price_impact_decay_skew_63d},
    "idec_381_price_impact_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_381_price_impact_decay_kurt_63d},
    "idec_382_price_impact_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_382_price_impact_decay_skew_126d},
    "idec_383_price_impact_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_383_price_impact_decay_kurt_126d},
    "idec_384_price_impact_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_384_price_impact_decay_skew_252d},
    "idec_385_price_impact_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_385_price_impact_decay_kurt_252d},
    "idec_386_volume_impact_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_386_volume_impact_decay_skew_5d},
    "idec_387_volume_impact_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_387_volume_impact_decay_kurt_5d},
    "idec_388_volume_impact_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_388_volume_impact_decay_skew_21d},
    "idec_389_volume_impact_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_389_volume_impact_decay_kurt_21d},
    "idec_390_volume_impact_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_390_volume_impact_decay_skew_63d},
    "idec_391_volume_impact_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_391_volume_impact_decay_kurt_63d},
    "idec_392_volume_impact_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_392_volume_impact_decay_skew_126d},
    "idec_393_volume_impact_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_393_volume_impact_decay_kurt_126d},
    "idec_394_volume_impact_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_394_volume_impact_decay_skew_252d},
    "idec_395_volume_impact_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_395_volume_impact_decay_kurt_252d},
    "idec_396_information_horizon_skew_5d": {"inputs": ["close", "volume"], "func": idec_396_information_horizon_skew_5d},
    "idec_397_information_horizon_kurt_5d": {"inputs": ["close", "volume"], "func": idec_397_information_horizon_kurt_5d},
    "idec_398_information_horizon_skew_21d": {"inputs": ["close", "volume"], "func": idec_398_information_horizon_skew_21d},
    "idec_399_information_horizon_kurt_21d": {"inputs": ["close", "volume"], "func": idec_399_information_horizon_kurt_21d},
    "idec_400_information_horizon_skew_63d": {"inputs": ["close", "volume"], "func": idec_400_information_horizon_skew_63d},
    "idec_401_information_horizon_kurt_63d": {"inputs": ["close", "volume"], "func": idec_401_information_horizon_kurt_63d},
    "idec_402_information_horizon_skew_126d": {"inputs": ["close", "volume"], "func": idec_402_information_horizon_skew_126d},
    "idec_403_information_horizon_kurt_126d": {"inputs": ["close", "volume"], "func": idec_403_information_horizon_kurt_126d},
    "idec_404_information_horizon_skew_252d": {"inputs": ["close", "volume"], "func": idec_404_information_horizon_skew_252d},
    "idec_405_information_horizon_kurt_252d": {"inputs": ["close", "volume"], "func": idec_405_information_horizon_kurt_252d},
    "idec_406_news_response_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_406_news_response_decay_skew_5d},
    "idec_407_news_response_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_407_news_response_decay_kurt_5d},
    "idec_408_news_response_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_408_news_response_decay_skew_21d},
    "idec_409_news_response_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_409_news_response_decay_kurt_21d},
    "idec_410_news_response_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_410_news_response_decay_skew_63d},
    "idec_411_news_response_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_411_news_response_decay_kurt_63d},
    "idec_412_news_response_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_412_news_response_decay_skew_126d},
    "idec_413_news_response_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_413_news_response_decay_kurt_126d},
    "idec_414_news_response_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_414_news_response_decay_skew_252d},
    "idec_415_news_response_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_415_news_response_decay_kurt_252d},
    "idec_416_autocorr_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_416_autocorr_decay_skew_5d},
    "idec_417_autocorr_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_417_autocorr_decay_kurt_5d},
    "idec_418_autocorr_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_418_autocorr_decay_skew_21d},
    "idec_419_autocorr_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_419_autocorr_decay_kurt_21d},
    "idec_420_autocorr_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_420_autocorr_decay_skew_63d},
    "idec_421_autocorr_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_421_autocorr_decay_kurt_63d},
    "idec_422_autocorr_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_422_autocorr_decay_skew_126d},
    "idec_423_autocorr_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_423_autocorr_decay_kurt_126d},
    "idec_424_autocorr_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_424_autocorr_decay_skew_252d},
    "idec_425_autocorr_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_425_autocorr_decay_kurt_252d},
    "idec_426_volatility_mean_reversion_skew_5d": {"inputs": ["close", "volume"], "func": idec_426_volatility_mean_reversion_skew_5d},
    "idec_427_volatility_mean_reversion_kurt_5d": {"inputs": ["close", "volume"], "func": idec_427_volatility_mean_reversion_kurt_5d},
    "idec_428_volatility_mean_reversion_skew_21d": {"inputs": ["close", "volume"], "func": idec_428_volatility_mean_reversion_skew_21d},
    "idec_429_volatility_mean_reversion_kurt_21d": {"inputs": ["close", "volume"], "func": idec_429_volatility_mean_reversion_kurt_21d},
    "idec_430_volatility_mean_reversion_skew_63d": {"inputs": ["close", "volume"], "func": idec_430_volatility_mean_reversion_skew_63d},
    "idec_431_volatility_mean_reversion_kurt_63d": {"inputs": ["close", "volume"], "func": idec_431_volatility_mean_reversion_kurt_63d},
    "idec_432_volatility_mean_reversion_skew_126d": {"inputs": ["close", "volume"], "func": idec_432_volatility_mean_reversion_skew_126d},
    "idec_433_volatility_mean_reversion_kurt_126d": {"inputs": ["close", "volume"], "func": idec_433_volatility_mean_reversion_kurt_126d},
    "idec_434_volatility_mean_reversion_skew_252d": {"inputs": ["close", "volume"], "func": idec_434_volatility_mean_reversion_skew_252d},
    "idec_435_volatility_mean_reversion_kurt_252d": {"inputs": ["close", "volume"], "func": idec_435_volatility_mean_reversion_kurt_252d},
    "idec_436_information_efficiency_skew_5d": {"inputs": ["close", "volume"], "func": idec_436_information_efficiency_skew_5d},
    "idec_437_information_efficiency_kurt_5d": {"inputs": ["close", "volume"], "func": idec_437_information_efficiency_kurt_5d},
    "idec_438_information_efficiency_skew_21d": {"inputs": ["close", "volume"], "func": idec_438_information_efficiency_skew_21d},
    "idec_439_information_efficiency_kurt_21d": {"inputs": ["close", "volume"], "func": idec_439_information_efficiency_kurt_21d},
    "idec_440_information_efficiency_skew_63d": {"inputs": ["close", "volume"], "func": idec_440_information_efficiency_skew_63d},
    "idec_441_information_efficiency_kurt_63d": {"inputs": ["close", "volume"], "func": idec_441_information_efficiency_kurt_63d},
    "idec_442_information_efficiency_skew_126d": {"inputs": ["close", "volume"], "func": idec_442_information_efficiency_skew_126d},
    "idec_443_information_efficiency_kurt_126d": {"inputs": ["close", "volume"], "func": idec_443_information_efficiency_kurt_126d},
    "idec_444_information_efficiency_skew_252d": {"inputs": ["close", "volume"], "func": idec_444_information_efficiency_skew_252d},
    "idec_445_information_efficiency_kurt_252d": {"inputs": ["close", "volume"], "func": idec_445_information_efficiency_kurt_252d},
    "idec_446_signal_noise_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_446_signal_noise_decay_skew_5d},
    "idec_447_signal_noise_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_447_signal_noise_decay_kurt_5d},
    "idec_448_signal_noise_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_448_signal_noise_decay_skew_21d},
    "idec_449_signal_noise_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_449_signal_noise_decay_kurt_21d},
    "idec_450_signal_noise_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_450_signal_noise_decay_skew_63d},
    "idec_451_signal_noise_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_451_signal_noise_decay_kurt_63d},
    "idec_452_signal_noise_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_452_signal_noise_decay_skew_126d},
    "idec_453_signal_noise_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_453_signal_noise_decay_kurt_126d},
    "idec_454_signal_noise_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_454_signal_noise_decay_skew_252d},
    "idec_455_signal_noise_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_455_signal_noise_decay_kurt_252d},
    "idec_456_memory_length_proxy_skew_5d": {"inputs": ["close", "volume"], "func": idec_456_memory_length_proxy_skew_5d},
    "idec_457_memory_length_proxy_kurt_5d": {"inputs": ["close", "volume"], "func": idec_457_memory_length_proxy_kurt_5d},
    "idec_458_memory_length_proxy_skew_21d": {"inputs": ["close", "volume"], "func": idec_458_memory_length_proxy_skew_21d},
    "idec_459_memory_length_proxy_kurt_21d": {"inputs": ["close", "volume"], "func": idec_459_memory_length_proxy_kurt_21d},
    "idec_460_memory_length_proxy_skew_63d": {"inputs": ["close", "volume"], "func": idec_460_memory_length_proxy_skew_63d},
    "idec_461_memory_length_proxy_kurt_63d": {"inputs": ["close", "volume"], "func": idec_461_memory_length_proxy_kurt_63d},
    "idec_462_memory_length_proxy_skew_126d": {"inputs": ["close", "volume"], "func": idec_462_memory_length_proxy_skew_126d},
    "idec_463_memory_length_proxy_kurt_126d": {"inputs": ["close", "volume"], "func": idec_463_memory_length_proxy_kurt_126d},
    "idec_464_memory_length_proxy_skew_252d": {"inputs": ["close", "volume"], "func": idec_464_memory_length_proxy_skew_252d},
    "idec_465_memory_length_proxy_kurt_252d": {"inputs": ["close", "volume"], "func": idec_465_memory_length_proxy_kurt_252d},
    "idec_466_information_shock_persistence_skew_5d": {"inputs": ["close", "volume"], "func": idec_466_information_shock_persistence_skew_5d},
    "idec_467_information_shock_persistence_kurt_5d": {"inputs": ["close", "volume"], "func": idec_467_information_shock_persistence_kurt_5d},
    "idec_468_information_shock_persistence_skew_21d": {"inputs": ["close", "volume"], "func": idec_468_information_shock_persistence_skew_21d},
    "idec_469_information_shock_persistence_kurt_21d": {"inputs": ["close", "volume"], "func": idec_469_information_shock_persistence_kurt_21d},
    "idec_470_information_shock_persistence_skew_63d": {"inputs": ["close", "volume"], "func": idec_470_information_shock_persistence_skew_63d},
    "idec_471_information_shock_persistence_kurt_63d": {"inputs": ["close", "volume"], "func": idec_471_information_shock_persistence_kurt_63d},
    "idec_472_information_shock_persistence_skew_126d": {"inputs": ["close", "volume"], "func": idec_472_information_shock_persistence_skew_126d},
    "idec_473_information_shock_persistence_kurt_126d": {"inputs": ["close", "volume"], "func": idec_473_information_shock_persistence_kurt_126d},
    "idec_474_information_shock_persistence_skew_252d": {"inputs": ["close", "volume"], "func": idec_474_information_shock_persistence_skew_252d},
    "idec_475_information_shock_persistence_kurt_252d": {"inputs": ["close", "volume"], "func": idec_475_information_shock_persistence_kurt_252d},
    "idec_476_drift_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_476_drift_decay_skew_5d},
    "idec_477_drift_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_477_drift_decay_kurt_5d},
    "idec_478_drift_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_478_drift_decay_skew_21d},
    "idec_479_drift_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_479_drift_decay_kurt_21d},
    "idec_480_drift_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_480_drift_decay_skew_63d},
    "idec_481_drift_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_481_drift_decay_kurt_63d},
    "idec_482_drift_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_482_drift_decay_skew_126d},
    "idec_483_drift_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_483_drift_decay_kurt_126d},
    "idec_484_drift_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_484_drift_decay_skew_252d},
    "idec_485_drift_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_485_drift_decay_kurt_252d},
    "idec_486_information_entropy_skew_5d": {"inputs": ["close", "volume"], "func": idec_486_information_entropy_skew_5d},
    "idec_487_information_entropy_kurt_5d": {"inputs": ["close", "volume"], "func": idec_487_information_entropy_kurt_5d},
    "idec_488_information_entropy_skew_21d": {"inputs": ["close", "volume"], "func": idec_488_information_entropy_skew_21d},
    "idec_489_information_entropy_kurt_21d": {"inputs": ["close", "volume"], "func": idec_489_information_entropy_kurt_21d},
    "idec_490_information_entropy_skew_63d": {"inputs": ["close", "volume"], "func": idec_490_information_entropy_skew_63d},
    "idec_491_information_entropy_kurt_63d": {"inputs": ["close", "volume"], "func": idec_491_information_entropy_kurt_63d},
    "idec_492_information_entropy_skew_126d": {"inputs": ["close", "volume"], "func": idec_492_information_entropy_skew_126d},
    "idec_493_information_entropy_kurt_126d": {"inputs": ["close", "volume"], "func": idec_493_information_entropy_kurt_126d},
    "idec_494_information_entropy_skew_252d": {"inputs": ["close", "volume"], "func": idec_494_information_entropy_skew_252d},
    "idec_495_information_entropy_kurt_252d": {"inputs": ["close", "volume"], "func": idec_495_information_entropy_kurt_252d},
    "idec_496_volume_memory_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_496_volume_memory_decay_skew_5d},
    "idec_497_volume_memory_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_497_volume_memory_decay_kurt_5d},
    "idec_498_volume_memory_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_498_volume_memory_decay_skew_21d},
    "idec_499_volume_memory_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_499_volume_memory_decay_kurt_21d},
    "idec_500_volume_memory_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_500_volume_memory_decay_skew_63d},
    "idec_501_volume_memory_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_501_volume_memory_decay_kurt_63d},
    "idec_502_volume_memory_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_502_volume_memory_decay_skew_126d},
    "idec_503_volume_memory_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_503_volume_memory_decay_kurt_126d},
    "idec_504_volume_memory_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_504_volume_memory_decay_skew_252d},
    "idec_505_volume_memory_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_505_volume_memory_decay_kurt_252d},
    "idec_506_price_stickiness_decay_skew_5d": {"inputs": ["close", "volume"], "func": idec_506_price_stickiness_decay_skew_5d},
    "idec_507_price_stickiness_decay_kurt_5d": {"inputs": ["close", "volume"], "func": idec_507_price_stickiness_decay_kurt_5d},
    "idec_508_price_stickiness_decay_skew_21d": {"inputs": ["close", "volume"], "func": idec_508_price_stickiness_decay_skew_21d},
    "idec_509_price_stickiness_decay_kurt_21d": {"inputs": ["close", "volume"], "func": idec_509_price_stickiness_decay_kurt_21d},
    "idec_510_price_stickiness_decay_skew_63d": {"inputs": ["close", "volume"], "func": idec_510_price_stickiness_decay_skew_63d},
    "idec_511_price_stickiness_decay_kurt_63d": {"inputs": ["close", "volume"], "func": idec_511_price_stickiness_decay_kurt_63d},
    "idec_512_price_stickiness_decay_skew_126d": {"inputs": ["close", "volume"], "func": idec_512_price_stickiness_decay_skew_126d},
    "idec_513_price_stickiness_decay_kurt_126d": {"inputs": ["close", "volume"], "func": idec_513_price_stickiness_decay_kurt_126d},
    "idec_514_price_stickiness_decay_skew_252d": {"inputs": ["close", "volume"], "func": idec_514_price_stickiness_decay_skew_252d},
    "idec_515_price_stickiness_decay_kurt_252d": {"inputs": ["close", "volume"], "func": idec_515_price_stickiness_decay_kurt_252d},
    "idec_516_information_flow_acceleration_skew_5d": {"inputs": ["close", "volume"], "func": idec_516_information_flow_acceleration_skew_5d},
    "idec_517_information_flow_acceleration_kurt_5d": {"inputs": ["close", "volume"], "func": idec_517_information_flow_acceleration_kurt_5d},
    "idec_518_information_flow_acceleration_skew_21d": {"inputs": ["close", "volume"], "func": idec_518_information_flow_acceleration_skew_21d},
    "idec_519_information_flow_acceleration_kurt_21d": {"inputs": ["close", "volume"], "func": idec_519_information_flow_acceleration_kurt_21d},
    "idec_520_information_flow_acceleration_skew_63d": {"inputs": ["close", "volume"], "func": idec_520_information_flow_acceleration_skew_63d},
    "idec_521_information_flow_acceleration_kurt_63d": {"inputs": ["close", "volume"], "func": idec_521_information_flow_acceleration_kurt_63d},
    "idec_522_information_flow_acceleration_skew_126d": {"inputs": ["close", "volume"], "func": idec_522_information_flow_acceleration_skew_126d},
    "idec_523_information_flow_acceleration_kurt_126d": {"inputs": ["close", "volume"], "func": idec_523_information_flow_acceleration_kurt_126d},
    "idec_524_information_flow_acceleration_skew_252d": {"inputs": ["close", "volume"], "func": idec_524_information_flow_acceleration_skew_252d},
    "idec_525_information_flow_acceleration_kurt_252d": {"inputs": ["close", "volume"], "func": idec_525_information_flow_acceleration_kurt_252d},
}
