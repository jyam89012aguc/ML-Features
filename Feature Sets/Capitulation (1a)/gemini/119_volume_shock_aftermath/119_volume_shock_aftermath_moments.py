"""
119_volume_shock_aftermath — Statistical Moments
Domain: volume_shock_aftermath
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

def vsha_376_volume_shock_mag_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_376_volume_shock_mag_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_shock_mag over 5d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(5).skew()

def vsha_377_volume_shock_mag_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_377_volume_shock_mag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_mag over 5d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(5).kurt()

def vsha_378_volume_shock_mag_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_378_volume_shock_mag_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_shock_mag over 21d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(21).skew()

def vsha_379_volume_shock_mag_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_379_volume_shock_mag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_mag over 21d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(21).kurt()

def vsha_380_volume_shock_mag_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_380_volume_shock_mag_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_shock_mag over 63d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(63).skew()

def vsha_381_volume_shock_mag_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_381_volume_shock_mag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_mag over 63d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(63).kurt()

def vsha_382_volume_shock_mag_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_382_volume_shock_mag_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_shock_mag over 126d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(126).skew()

def vsha_383_volume_shock_mag_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_383_volume_shock_mag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_mag over 126d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(126).kurt()

def vsha_384_volume_shock_mag_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_384_volume_shock_mag_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_shock_mag over 252d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(252).skew()

def vsha_385_volume_shock_mag_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_385_volume_shock_mag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_mag over 252d. Magnitude of the current volume shock.
    """
    return (volume / volume.rolling(63).mean()).rolling(252).kurt()

def vsha_386_post_shock_drift_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_386_post_shock_drift_skew_5d
    ECONOMIC RATIONALE: Skewness of post_shock_drift over 5d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(5).skew()

def vsha_387_post_shock_drift_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_387_post_shock_drift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of post_shock_drift over 5d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(5).kurt()

def vsha_388_post_shock_drift_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_388_post_shock_drift_skew_21d
    ECONOMIC RATIONALE: Skewness of post_shock_drift over 21d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(21).skew()

def vsha_389_post_shock_drift_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_389_post_shock_drift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of post_shock_drift over 21d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(21).kurt()

def vsha_390_post_shock_drift_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_390_post_shock_drift_skew_63d
    ECONOMIC RATIONALE: Skewness of post_shock_drift over 63d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(63).skew()

def vsha_391_post_shock_drift_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_391_post_shock_drift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of post_shock_drift over 63d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(63).kurt()

def vsha_392_post_shock_drift_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_392_post_shock_drift_skew_126d
    ECONOMIC RATIONALE: Skewness of post_shock_drift over 126d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(126).skew()

def vsha_393_post_shock_drift_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_393_post_shock_drift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of post_shock_drift over 126d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(126).kurt()

def vsha_394_post_shock_drift_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_394_post_shock_drift_skew_252d
    ECONOMIC RATIONALE: Skewness of post_shock_drift over 252d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(252).skew()

def vsha_395_post_shock_drift_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_395_post_shock_drift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of post_shock_drift over 252d. Price drift following major volume shocks.
    """
    return (close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)).rolling(252).kurt()

def vsha_396_shock_volatility_expansion_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_396_shock_volatility_expansion_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_volatility_expansion over 5d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(5).skew()

def vsha_397_shock_volatility_expansion_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_397_shock_volatility_expansion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_volatility_expansion over 5d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(5).kurt()

def vsha_398_shock_volatility_expansion_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_398_shock_volatility_expansion_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_volatility_expansion over 21d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(21).skew()

def vsha_399_shock_volatility_expansion_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_399_shock_volatility_expansion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_volatility_expansion over 21d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(21).kurt()

def vsha_400_shock_volatility_expansion_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_400_shock_volatility_expansion_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_volatility_expansion over 63d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(63).skew()

def vsha_401_shock_volatility_expansion_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_401_shock_volatility_expansion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_volatility_expansion over 63d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(63).kurt()

def vsha_402_shock_volatility_expansion_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_402_shock_volatility_expansion_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_volatility_expansion over 126d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(126).skew()

def vsha_403_shock_volatility_expansion_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_403_shock_volatility_expansion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_volatility_expansion over 126d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(126).kurt()

def vsha_404_shock_volatility_expansion_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_404_shock_volatility_expansion_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_volatility_expansion over 252d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(252).skew()

def vsha_405_shock_volatility_expansion_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_405_shock_volatility_expansion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_volatility_expansion over 252d. Volatility expansion associated with volume shocks.
    """
    return (close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(252).kurt()

def vsha_406_volume_shock_reversal_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_406_volume_shock_reversal_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_shock_reversal over 5d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(5).skew()

def vsha_407_volume_shock_reversal_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_407_volume_shock_reversal_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_reversal over 5d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(5).kurt()

def vsha_408_volume_shock_reversal_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_408_volume_shock_reversal_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_shock_reversal over 21d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(21).skew()

def vsha_409_volume_shock_reversal_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_409_volume_shock_reversal_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_reversal over 21d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(21).kurt()

def vsha_410_volume_shock_reversal_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_410_volume_shock_reversal_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_shock_reversal over 63d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(63).skew()

def vsha_411_volume_shock_reversal_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_411_volume_shock_reversal_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_reversal over 63d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(63).kurt()

def vsha_412_volume_shock_reversal_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_412_volume_shock_reversal_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_shock_reversal over 126d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(126).skew()

def vsha_413_volume_shock_reversal_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_413_volume_shock_reversal_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_reversal over 126d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(126).kurt()

def vsha_414_volume_shock_reversal_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_414_volume_shock_reversal_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_shock_reversal over 252d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(252).skew()

def vsha_415_volume_shock_reversal_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_415_volume_shock_reversal_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_reversal over 252d. Reversal of price direction after a volume shock.
    """
    return ((close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)).rolling(252).kurt()

def vsha_416_shock_persistence_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_416_shock_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_persistence over 5d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(5).skew()

def vsha_417_shock_persistence_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_417_shock_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_persistence over 5d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(5).kurt()

def vsha_418_shock_persistence_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_418_shock_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_persistence over 21d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(21).skew()

def vsha_419_shock_persistence_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_419_shock_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_persistence over 21d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(21).kurt()

def vsha_420_shock_persistence_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_420_shock_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_persistence over 63d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(63).skew()

def vsha_421_shock_persistence_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_421_shock_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_persistence over 63d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(63).kurt()

def vsha_422_shock_persistence_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_422_shock_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_persistence over 126d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(126).skew()

def vsha_423_shock_persistence_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_423_shock_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_persistence over 126d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(126).kurt()

def vsha_424_shock_persistence_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_424_shock_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_persistence over 252d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(252).skew()

def vsha_425_shock_persistence_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_425_shock_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_persistence over 252d. Duration of a high-volume regime.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(10).sum()).rolling(252).kurt()

def vsha_426_volume_shock_z_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_426_volume_shock_z_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_shock_z over 5d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(5).skew()

def vsha_427_volume_shock_z_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_427_volume_shock_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_z over 5d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(5).kurt()

def vsha_428_volume_shock_z_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_428_volume_shock_z_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_shock_z over 21d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(21).skew()

def vsha_429_volume_shock_z_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_429_volume_shock_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_z over 21d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(21).kurt()

def vsha_430_volume_shock_z_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_430_volume_shock_z_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_shock_z over 63d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(63).skew()

def vsha_431_volume_shock_z_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_431_volume_shock_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_z over 63d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(63).kurt()

def vsha_432_volume_shock_z_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_432_volume_shock_z_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_shock_z over 126d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(126).skew()

def vsha_433_volume_shock_z_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_433_volume_shock_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_z over 126d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(126).kurt()

def vsha_434_volume_shock_z_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_434_volume_shock_z_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_shock_z over 252d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(252).skew()

def vsha_435_volume_shock_z_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_435_volume_shock_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_z over 252d. Z-score of volume relative to annual history.
    """
    return (_zscore_rolling(volume, 252)).rolling(252).kurt()

def vsha_436_shock_price_impact_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_436_shock_price_impact_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_price_impact over 5d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(5).skew()

def vsha_437_shock_price_impact_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_437_shock_price_impact_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_price_impact over 5d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(5).kurt()

def vsha_438_shock_price_impact_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_438_shock_price_impact_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_price_impact over 21d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(21).skew()

def vsha_439_shock_price_impact_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_439_shock_price_impact_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_price_impact over 21d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(21).kurt()

def vsha_440_shock_price_impact_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_440_shock_price_impact_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_price_impact over 63d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(63).skew()

def vsha_441_shock_price_impact_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_441_shock_price_impact_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_price_impact over 63d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(63).kurt()

def vsha_442_shock_price_impact_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_442_shock_price_impact_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_price_impact over 126d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(126).skew()

def vsha_443_shock_price_impact_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_443_shock_price_impact_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_price_impact over 126d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(126).kurt()

def vsha_444_shock_price_impact_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_444_shock_price_impact_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_price_impact over 252d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(252).skew()

def vsha_445_shock_price_impact_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_445_shock_price_impact_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_price_impact over 252d. Price change weighted by the volume shock magnitude.
    """
    return (close.diff(1) * (volume / volume.rolling(63).mean())).rolling(252).kurt()

def vsha_446_post_shock_liquidity_drain_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_446_post_shock_liquidity_drain_skew_5d
    ECONOMIC RATIONALE: Skewness of post_shock_liquidity_drain over 5d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(5).skew()

def vsha_447_post_shock_liquidity_drain_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_447_post_shock_liquidity_drain_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of post_shock_liquidity_drain over 5d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(5).kurt()

def vsha_448_post_shock_liquidity_drain_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_448_post_shock_liquidity_drain_skew_21d
    ECONOMIC RATIONALE: Skewness of post_shock_liquidity_drain over 21d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(21).skew()

def vsha_449_post_shock_liquidity_drain_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_449_post_shock_liquidity_drain_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of post_shock_liquidity_drain over 21d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(21).kurt()

def vsha_450_post_shock_liquidity_drain_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_450_post_shock_liquidity_drain_skew_63d
    ECONOMIC RATIONALE: Skewness of post_shock_liquidity_drain over 63d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(63).skew()

def vsha_451_post_shock_liquidity_drain_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_451_post_shock_liquidity_drain_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of post_shock_liquidity_drain over 63d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(63).kurt()

def vsha_452_post_shock_liquidity_drain_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_452_post_shock_liquidity_drain_skew_126d
    ECONOMIC RATIONALE: Skewness of post_shock_liquidity_drain over 126d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(126).skew()

def vsha_453_post_shock_liquidity_drain_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_453_post_shock_liquidity_drain_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of post_shock_liquidity_drain over 126d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(126).kurt()

def vsha_454_post_shock_liquidity_drain_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_454_post_shock_liquidity_drain_skew_252d
    ECONOMIC RATIONALE: Skewness of post_shock_liquidity_drain over 252d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(252).skew()

def vsha_455_post_shock_liquidity_drain_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_455_post_shock_liquidity_drain_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of post_shock_liquidity_drain over 252d. Liquidity dry-up following a massive shock.
    """
    return ((volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)).rolling(252).kurt()

def vsha_456_shock_clustering_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_456_shock_clustering_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_clustering over 5d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(5).skew()

def vsha_457_shock_clustering_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_457_shock_clustering_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_clustering over 5d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(5).kurt()

def vsha_458_shock_clustering_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_458_shock_clustering_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_clustering over 21d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(21).skew()

def vsha_459_shock_clustering_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_459_shock_clustering_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_clustering over 21d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(21).kurt()

def vsha_460_shock_clustering_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_460_shock_clustering_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_clustering over 63d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(63).skew()

def vsha_461_shock_clustering_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_461_shock_clustering_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_clustering over 63d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(63).kurt()

def vsha_462_shock_clustering_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_462_shock_clustering_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_clustering over 126d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(126).skew()

def vsha_463_shock_clustering_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_463_shock_clustering_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_clustering over 126d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(126).kurt()

def vsha_464_shock_clustering_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_464_shock_clustering_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_clustering over 252d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(252).skew()

def vsha_465_shock_clustering_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_465_shock_clustering_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_clustering over 252d. Frequency of volume shocks in the last quarter.
    """
    return ((volume > volume.rolling(63).mean()*2).rolling(63).sum()).rolling(252).kurt()

def vsha_466_volume_shock_entropy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_466_volume_shock_entropy_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_shock_entropy over 5d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(5).skew()

def vsha_467_volume_shock_entropy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_467_volume_shock_entropy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_entropy over 5d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(5).kurt()

def vsha_468_volume_shock_entropy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_468_volume_shock_entropy_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_shock_entropy over 21d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(21).skew()

def vsha_469_volume_shock_entropy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_469_volume_shock_entropy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_entropy over 21d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(21).kurt()

def vsha_470_volume_shock_entropy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_470_volume_shock_entropy_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_shock_entropy over 63d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(63).skew()

def vsha_471_volume_shock_entropy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_471_volume_shock_entropy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_entropy over 63d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(63).kurt()

def vsha_472_volume_shock_entropy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_472_volume_shock_entropy_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_shock_entropy over 126d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(126).skew()

def vsha_473_volume_shock_entropy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_473_volume_shock_entropy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_entropy over 126d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(126).kurt()

def vsha_474_volume_shock_entropy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_474_volume_shock_entropy_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_shock_entropy over 252d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(252).skew()

def vsha_475_volume_shock_entropy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_475_volume_shock_entropy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_entropy over 252d. Unpredictability of volume during shocks.
    """
    return (volume.rolling(21).apply(lambda x: -np.sum(x/np.sum(x)*np.log(x/np.sum(x)+1e-9)))).rolling(252).kurt()

def vsha_476_shock_exhaustion_proxy_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_476_shock_exhaustion_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_exhaustion_proxy over 5d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(5).skew()

def vsha_477_shock_exhaustion_proxy_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_477_shock_exhaustion_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_exhaustion_proxy over 5d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(5).kurt()

def vsha_478_shock_exhaustion_proxy_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_478_shock_exhaustion_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_exhaustion_proxy over 21d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(21).skew()

def vsha_479_shock_exhaustion_proxy_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_479_shock_exhaustion_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_exhaustion_proxy over 21d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(21).kurt()

def vsha_480_shock_exhaustion_proxy_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_480_shock_exhaustion_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_exhaustion_proxy over 63d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(63).skew()

def vsha_481_shock_exhaustion_proxy_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_481_shock_exhaustion_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_exhaustion_proxy over 63d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(63).kurt()

def vsha_482_shock_exhaustion_proxy_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_482_shock_exhaustion_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_exhaustion_proxy over 126d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(126).skew()

def vsha_483_shock_exhaustion_proxy_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_483_shock_exhaustion_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_exhaustion_proxy over 126d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(126).kurt()

def vsha_484_shock_exhaustion_proxy_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_484_shock_exhaustion_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_exhaustion_proxy over 252d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(252).skew()

def vsha_485_shock_exhaustion_proxy_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_485_shock_exhaustion_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_exhaustion_proxy over 252d. Large volume shock with minimal price impact.
    """
    return ((volume > volume.rolling(63).mean()*3) & (close.diff(1).abs() < close.rolling(21).std()*0.5)).rolling(252).kurt()

def vsha_486_shock_recovery_rate_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_486_shock_recovery_rate_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_recovery_rate over 5d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(5).skew()

def vsha_487_shock_recovery_rate_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_487_shock_recovery_rate_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_recovery_rate over 5d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(5).kurt()

def vsha_488_shock_recovery_rate_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_488_shock_recovery_rate_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_recovery_rate over 21d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(21).skew()

def vsha_489_shock_recovery_rate_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_489_shock_recovery_rate_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_recovery_rate over 21d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(21).kurt()

def vsha_490_shock_recovery_rate_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_490_shock_recovery_rate_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_recovery_rate over 63d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(63).skew()

def vsha_491_shock_recovery_rate_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_491_shock_recovery_rate_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_recovery_rate over 63d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(63).kurt()

def vsha_492_shock_recovery_rate_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_492_shock_recovery_rate_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_recovery_rate over 126d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(126).skew()

def vsha_493_shock_recovery_rate_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_493_shock_recovery_rate_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_recovery_rate over 126d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(126).kurt()

def vsha_494_shock_recovery_rate_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_494_shock_recovery_rate_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_recovery_rate over 252d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(252).skew()

def vsha_495_shock_recovery_rate_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_495_shock_recovery_rate_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_recovery_rate over 252d. Recovery relative to the price at the last volume peak.
    """
    return (close / close.shift(volume.rolling(63).apply(lambda x: np.argmax(x)))).rolling(252).kurt()

def vsha_496_volume_shock_momentum_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_496_volume_shock_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_shock_momentum over 5d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(5).skew()

def vsha_497_volume_shock_momentum_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_497_volume_shock_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_momentum over 5d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(5).kurt()

def vsha_498_volume_shock_momentum_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_498_volume_shock_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_shock_momentum over 21d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(21).skew()

def vsha_499_volume_shock_momentum_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_499_volume_shock_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_momentum over 21d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(21).kurt()

def vsha_500_volume_shock_momentum_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_500_volume_shock_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_shock_momentum over 63d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(63).skew()

def vsha_501_volume_shock_momentum_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_501_volume_shock_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_momentum over 63d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(63).kurt()

def vsha_502_volume_shock_momentum_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_502_volume_shock_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_shock_momentum over 126d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(126).skew()

def vsha_503_volume_shock_momentum_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_503_volume_shock_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_momentum over 126d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(126).kurt()

def vsha_504_volume_shock_momentum_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_504_volume_shock_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_shock_momentum over 252d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(252).skew()

def vsha_505_volume_shock_momentum_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_505_volume_shock_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_momentum over 252d. Synchronized volume and price momentum.
    """
    return (volume.pct_change(5) * close.pct_change(5)).rolling(252).kurt()

def vsha_506_shock_regime_shift_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_506_shock_regime_shift_skew_5d
    ECONOMIC RATIONALE: Skewness of shock_regime_shift over 5d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(5).skew()

def vsha_507_shock_regime_shift_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_507_shock_regime_shift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of shock_regime_shift over 5d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(5).kurt()

def vsha_508_shock_regime_shift_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_508_shock_regime_shift_skew_21d
    ECONOMIC RATIONALE: Skewness of shock_regime_shift over 21d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(21).skew()

def vsha_509_shock_regime_shift_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_509_shock_regime_shift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of shock_regime_shift over 21d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(21).kurt()

def vsha_510_shock_regime_shift_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_510_shock_regime_shift_skew_63d
    ECONOMIC RATIONALE: Skewness of shock_regime_shift over 63d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(63).skew()

def vsha_511_shock_regime_shift_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_511_shock_regime_shift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of shock_regime_shift over 63d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(63).kurt()

def vsha_512_shock_regime_shift_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_512_shock_regime_shift_skew_126d
    ECONOMIC RATIONALE: Skewness of shock_regime_shift over 126d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(126).skew()

def vsha_513_shock_regime_shift_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_513_shock_regime_shift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of shock_regime_shift over 126d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(126).kurt()

def vsha_514_shock_regime_shift_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_514_shock_regime_shift_skew_252d
    ECONOMIC RATIONALE: Skewness of shock_regime_shift over 252d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(252).skew()

def vsha_515_shock_regime_shift_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_515_shock_regime_shift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of shock_regime_shift over 252d. Structural shift in average volume levels.
    """
    return (volume.rolling(21).mean().diff(21) / volume.rolling(252).std()).rolling(252).kurt()

def vsha_516_volume_shock_tail_corr_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_516_volume_shock_tail_corr_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_shock_tail_corr over 5d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(5).skew()

def vsha_517_volume_shock_tail_corr_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_517_volume_shock_tail_corr_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_tail_corr over 5d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(5).kurt()

def vsha_518_volume_shock_tail_corr_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_518_volume_shock_tail_corr_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_shock_tail_corr over 21d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(21).skew()

def vsha_519_volume_shock_tail_corr_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_519_volume_shock_tail_corr_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_tail_corr over 21d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(21).kurt()

def vsha_520_volume_shock_tail_corr_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_520_volume_shock_tail_corr_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_shock_tail_corr over 63d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(63).skew()

def vsha_521_volume_shock_tail_corr_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_521_volume_shock_tail_corr_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_tail_corr over 63d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(63).kurt()

def vsha_522_volume_shock_tail_corr_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_522_volume_shock_tail_corr_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_shock_tail_corr over 126d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(126).skew()

def vsha_523_volume_shock_tail_corr_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_523_volume_shock_tail_corr_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_tail_corr over 126d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(126).kurt()

def vsha_524_volume_shock_tail_corr_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_524_volume_shock_tail_corr_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_shock_tail_corr over 252d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(252).skew()

def vsha_525_volume_shock_tail_corr_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_525_volume_shock_tail_corr_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_shock_tail_corr over 252d. Correlation between volume shocks and price magnitude.
    """
    return (volume.rolling(21).corr(close.pct_change(1).abs())).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V119_REGISTRY_MOMENTS = {
    "vsha_376_volume_shock_mag_skew_5d": {"inputs": ["close", "volume"], "func": vsha_376_volume_shock_mag_skew_5d},
    "vsha_377_volume_shock_mag_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_377_volume_shock_mag_kurt_5d},
    "vsha_378_volume_shock_mag_skew_21d": {"inputs": ["close", "volume"], "func": vsha_378_volume_shock_mag_skew_21d},
    "vsha_379_volume_shock_mag_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_379_volume_shock_mag_kurt_21d},
    "vsha_380_volume_shock_mag_skew_63d": {"inputs": ["close", "volume"], "func": vsha_380_volume_shock_mag_skew_63d},
    "vsha_381_volume_shock_mag_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_381_volume_shock_mag_kurt_63d},
    "vsha_382_volume_shock_mag_skew_126d": {"inputs": ["close", "volume"], "func": vsha_382_volume_shock_mag_skew_126d},
    "vsha_383_volume_shock_mag_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_383_volume_shock_mag_kurt_126d},
    "vsha_384_volume_shock_mag_skew_252d": {"inputs": ["close", "volume"], "func": vsha_384_volume_shock_mag_skew_252d},
    "vsha_385_volume_shock_mag_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_385_volume_shock_mag_kurt_252d},
    "vsha_386_post_shock_drift_skew_5d": {"inputs": ["close", "volume"], "func": vsha_386_post_shock_drift_skew_5d},
    "vsha_387_post_shock_drift_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_387_post_shock_drift_kurt_5d},
    "vsha_388_post_shock_drift_skew_21d": {"inputs": ["close", "volume"], "func": vsha_388_post_shock_drift_skew_21d},
    "vsha_389_post_shock_drift_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_389_post_shock_drift_kurt_21d},
    "vsha_390_post_shock_drift_skew_63d": {"inputs": ["close", "volume"], "func": vsha_390_post_shock_drift_skew_63d},
    "vsha_391_post_shock_drift_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_391_post_shock_drift_kurt_63d},
    "vsha_392_post_shock_drift_skew_126d": {"inputs": ["close", "volume"], "func": vsha_392_post_shock_drift_skew_126d},
    "vsha_393_post_shock_drift_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_393_post_shock_drift_kurt_126d},
    "vsha_394_post_shock_drift_skew_252d": {"inputs": ["close", "volume"], "func": vsha_394_post_shock_drift_skew_252d},
    "vsha_395_post_shock_drift_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_395_post_shock_drift_kurt_252d},
    "vsha_396_shock_volatility_expansion_skew_5d": {"inputs": ["close", "volume"], "func": vsha_396_shock_volatility_expansion_skew_5d},
    "vsha_397_shock_volatility_expansion_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_397_shock_volatility_expansion_kurt_5d},
    "vsha_398_shock_volatility_expansion_skew_21d": {"inputs": ["close", "volume"], "func": vsha_398_shock_volatility_expansion_skew_21d},
    "vsha_399_shock_volatility_expansion_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_399_shock_volatility_expansion_kurt_21d},
    "vsha_400_shock_volatility_expansion_skew_63d": {"inputs": ["close", "volume"], "func": vsha_400_shock_volatility_expansion_skew_63d},
    "vsha_401_shock_volatility_expansion_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_401_shock_volatility_expansion_kurt_63d},
    "vsha_402_shock_volatility_expansion_skew_126d": {"inputs": ["close", "volume"], "func": vsha_402_shock_volatility_expansion_skew_126d},
    "vsha_403_shock_volatility_expansion_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_403_shock_volatility_expansion_kurt_126d},
    "vsha_404_shock_volatility_expansion_skew_252d": {"inputs": ["close", "volume"], "func": vsha_404_shock_volatility_expansion_skew_252d},
    "vsha_405_shock_volatility_expansion_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_405_shock_volatility_expansion_kurt_252d},
    "vsha_406_volume_shock_reversal_skew_5d": {"inputs": ["close", "volume"], "func": vsha_406_volume_shock_reversal_skew_5d},
    "vsha_407_volume_shock_reversal_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_407_volume_shock_reversal_kurt_5d},
    "vsha_408_volume_shock_reversal_skew_21d": {"inputs": ["close", "volume"], "func": vsha_408_volume_shock_reversal_skew_21d},
    "vsha_409_volume_shock_reversal_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_409_volume_shock_reversal_kurt_21d},
    "vsha_410_volume_shock_reversal_skew_63d": {"inputs": ["close", "volume"], "func": vsha_410_volume_shock_reversal_skew_63d},
    "vsha_411_volume_shock_reversal_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_411_volume_shock_reversal_kurt_63d},
    "vsha_412_volume_shock_reversal_skew_126d": {"inputs": ["close", "volume"], "func": vsha_412_volume_shock_reversal_skew_126d},
    "vsha_413_volume_shock_reversal_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_413_volume_shock_reversal_kurt_126d},
    "vsha_414_volume_shock_reversal_skew_252d": {"inputs": ["close", "volume"], "func": vsha_414_volume_shock_reversal_skew_252d},
    "vsha_415_volume_shock_reversal_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_415_volume_shock_reversal_kurt_252d},
    "vsha_416_shock_persistence_skew_5d": {"inputs": ["close", "volume"], "func": vsha_416_shock_persistence_skew_5d},
    "vsha_417_shock_persistence_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_417_shock_persistence_kurt_5d},
    "vsha_418_shock_persistence_skew_21d": {"inputs": ["close", "volume"], "func": vsha_418_shock_persistence_skew_21d},
    "vsha_419_shock_persistence_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_419_shock_persistence_kurt_21d},
    "vsha_420_shock_persistence_skew_63d": {"inputs": ["close", "volume"], "func": vsha_420_shock_persistence_skew_63d},
    "vsha_421_shock_persistence_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_421_shock_persistence_kurt_63d},
    "vsha_422_shock_persistence_skew_126d": {"inputs": ["close", "volume"], "func": vsha_422_shock_persistence_skew_126d},
    "vsha_423_shock_persistence_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_423_shock_persistence_kurt_126d},
    "vsha_424_shock_persistence_skew_252d": {"inputs": ["close", "volume"], "func": vsha_424_shock_persistence_skew_252d},
    "vsha_425_shock_persistence_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_425_shock_persistence_kurt_252d},
    "vsha_426_volume_shock_z_skew_5d": {"inputs": ["close", "volume"], "func": vsha_426_volume_shock_z_skew_5d},
    "vsha_427_volume_shock_z_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_427_volume_shock_z_kurt_5d},
    "vsha_428_volume_shock_z_skew_21d": {"inputs": ["close", "volume"], "func": vsha_428_volume_shock_z_skew_21d},
    "vsha_429_volume_shock_z_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_429_volume_shock_z_kurt_21d},
    "vsha_430_volume_shock_z_skew_63d": {"inputs": ["close", "volume"], "func": vsha_430_volume_shock_z_skew_63d},
    "vsha_431_volume_shock_z_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_431_volume_shock_z_kurt_63d},
    "vsha_432_volume_shock_z_skew_126d": {"inputs": ["close", "volume"], "func": vsha_432_volume_shock_z_skew_126d},
    "vsha_433_volume_shock_z_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_433_volume_shock_z_kurt_126d},
    "vsha_434_volume_shock_z_skew_252d": {"inputs": ["close", "volume"], "func": vsha_434_volume_shock_z_skew_252d},
    "vsha_435_volume_shock_z_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_435_volume_shock_z_kurt_252d},
    "vsha_436_shock_price_impact_skew_5d": {"inputs": ["close", "volume"], "func": vsha_436_shock_price_impact_skew_5d},
    "vsha_437_shock_price_impact_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_437_shock_price_impact_kurt_5d},
    "vsha_438_shock_price_impact_skew_21d": {"inputs": ["close", "volume"], "func": vsha_438_shock_price_impact_skew_21d},
    "vsha_439_shock_price_impact_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_439_shock_price_impact_kurt_21d},
    "vsha_440_shock_price_impact_skew_63d": {"inputs": ["close", "volume"], "func": vsha_440_shock_price_impact_skew_63d},
    "vsha_441_shock_price_impact_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_441_shock_price_impact_kurt_63d},
    "vsha_442_shock_price_impact_skew_126d": {"inputs": ["close", "volume"], "func": vsha_442_shock_price_impact_skew_126d},
    "vsha_443_shock_price_impact_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_443_shock_price_impact_kurt_126d},
    "vsha_444_shock_price_impact_skew_252d": {"inputs": ["close", "volume"], "func": vsha_444_shock_price_impact_skew_252d},
    "vsha_445_shock_price_impact_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_445_shock_price_impact_kurt_252d},
    "vsha_446_post_shock_liquidity_drain_skew_5d": {"inputs": ["close", "volume"], "func": vsha_446_post_shock_liquidity_drain_skew_5d},
    "vsha_447_post_shock_liquidity_drain_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_447_post_shock_liquidity_drain_kurt_5d},
    "vsha_448_post_shock_liquidity_drain_skew_21d": {"inputs": ["close", "volume"], "func": vsha_448_post_shock_liquidity_drain_skew_21d},
    "vsha_449_post_shock_liquidity_drain_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_449_post_shock_liquidity_drain_kurt_21d},
    "vsha_450_post_shock_liquidity_drain_skew_63d": {"inputs": ["close", "volume"], "func": vsha_450_post_shock_liquidity_drain_skew_63d},
    "vsha_451_post_shock_liquidity_drain_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_451_post_shock_liquidity_drain_kurt_63d},
    "vsha_452_post_shock_liquidity_drain_skew_126d": {"inputs": ["close", "volume"], "func": vsha_452_post_shock_liquidity_drain_skew_126d},
    "vsha_453_post_shock_liquidity_drain_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_453_post_shock_liquidity_drain_kurt_126d},
    "vsha_454_post_shock_liquidity_drain_skew_252d": {"inputs": ["close", "volume"], "func": vsha_454_post_shock_liquidity_drain_skew_252d},
    "vsha_455_post_shock_liquidity_drain_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_455_post_shock_liquidity_drain_kurt_252d},
    "vsha_456_shock_clustering_skew_5d": {"inputs": ["close", "volume"], "func": vsha_456_shock_clustering_skew_5d},
    "vsha_457_shock_clustering_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_457_shock_clustering_kurt_5d},
    "vsha_458_shock_clustering_skew_21d": {"inputs": ["close", "volume"], "func": vsha_458_shock_clustering_skew_21d},
    "vsha_459_shock_clustering_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_459_shock_clustering_kurt_21d},
    "vsha_460_shock_clustering_skew_63d": {"inputs": ["close", "volume"], "func": vsha_460_shock_clustering_skew_63d},
    "vsha_461_shock_clustering_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_461_shock_clustering_kurt_63d},
    "vsha_462_shock_clustering_skew_126d": {"inputs": ["close", "volume"], "func": vsha_462_shock_clustering_skew_126d},
    "vsha_463_shock_clustering_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_463_shock_clustering_kurt_126d},
    "vsha_464_shock_clustering_skew_252d": {"inputs": ["close", "volume"], "func": vsha_464_shock_clustering_skew_252d},
    "vsha_465_shock_clustering_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_465_shock_clustering_kurt_252d},
    "vsha_466_volume_shock_entropy_skew_5d": {"inputs": ["close", "volume"], "func": vsha_466_volume_shock_entropy_skew_5d},
    "vsha_467_volume_shock_entropy_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_467_volume_shock_entropy_kurt_5d},
    "vsha_468_volume_shock_entropy_skew_21d": {"inputs": ["close", "volume"], "func": vsha_468_volume_shock_entropy_skew_21d},
    "vsha_469_volume_shock_entropy_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_469_volume_shock_entropy_kurt_21d},
    "vsha_470_volume_shock_entropy_skew_63d": {"inputs": ["close", "volume"], "func": vsha_470_volume_shock_entropy_skew_63d},
    "vsha_471_volume_shock_entropy_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_471_volume_shock_entropy_kurt_63d},
    "vsha_472_volume_shock_entropy_skew_126d": {"inputs": ["close", "volume"], "func": vsha_472_volume_shock_entropy_skew_126d},
    "vsha_473_volume_shock_entropy_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_473_volume_shock_entropy_kurt_126d},
    "vsha_474_volume_shock_entropy_skew_252d": {"inputs": ["close", "volume"], "func": vsha_474_volume_shock_entropy_skew_252d},
    "vsha_475_volume_shock_entropy_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_475_volume_shock_entropy_kurt_252d},
    "vsha_476_shock_exhaustion_proxy_skew_5d": {"inputs": ["close", "volume"], "func": vsha_476_shock_exhaustion_proxy_skew_5d},
    "vsha_477_shock_exhaustion_proxy_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_477_shock_exhaustion_proxy_kurt_5d},
    "vsha_478_shock_exhaustion_proxy_skew_21d": {"inputs": ["close", "volume"], "func": vsha_478_shock_exhaustion_proxy_skew_21d},
    "vsha_479_shock_exhaustion_proxy_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_479_shock_exhaustion_proxy_kurt_21d},
    "vsha_480_shock_exhaustion_proxy_skew_63d": {"inputs": ["close", "volume"], "func": vsha_480_shock_exhaustion_proxy_skew_63d},
    "vsha_481_shock_exhaustion_proxy_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_481_shock_exhaustion_proxy_kurt_63d},
    "vsha_482_shock_exhaustion_proxy_skew_126d": {"inputs": ["close", "volume"], "func": vsha_482_shock_exhaustion_proxy_skew_126d},
    "vsha_483_shock_exhaustion_proxy_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_483_shock_exhaustion_proxy_kurt_126d},
    "vsha_484_shock_exhaustion_proxy_skew_252d": {"inputs": ["close", "volume"], "func": vsha_484_shock_exhaustion_proxy_skew_252d},
    "vsha_485_shock_exhaustion_proxy_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_485_shock_exhaustion_proxy_kurt_252d},
    "vsha_486_shock_recovery_rate_skew_5d": {"inputs": ["close", "volume"], "func": vsha_486_shock_recovery_rate_skew_5d},
    "vsha_487_shock_recovery_rate_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_487_shock_recovery_rate_kurt_5d},
    "vsha_488_shock_recovery_rate_skew_21d": {"inputs": ["close", "volume"], "func": vsha_488_shock_recovery_rate_skew_21d},
    "vsha_489_shock_recovery_rate_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_489_shock_recovery_rate_kurt_21d},
    "vsha_490_shock_recovery_rate_skew_63d": {"inputs": ["close", "volume"], "func": vsha_490_shock_recovery_rate_skew_63d},
    "vsha_491_shock_recovery_rate_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_491_shock_recovery_rate_kurt_63d},
    "vsha_492_shock_recovery_rate_skew_126d": {"inputs": ["close", "volume"], "func": vsha_492_shock_recovery_rate_skew_126d},
    "vsha_493_shock_recovery_rate_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_493_shock_recovery_rate_kurt_126d},
    "vsha_494_shock_recovery_rate_skew_252d": {"inputs": ["close", "volume"], "func": vsha_494_shock_recovery_rate_skew_252d},
    "vsha_495_shock_recovery_rate_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_495_shock_recovery_rate_kurt_252d},
    "vsha_496_volume_shock_momentum_skew_5d": {"inputs": ["close", "volume"], "func": vsha_496_volume_shock_momentum_skew_5d},
    "vsha_497_volume_shock_momentum_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_497_volume_shock_momentum_kurt_5d},
    "vsha_498_volume_shock_momentum_skew_21d": {"inputs": ["close", "volume"], "func": vsha_498_volume_shock_momentum_skew_21d},
    "vsha_499_volume_shock_momentum_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_499_volume_shock_momentum_kurt_21d},
    "vsha_500_volume_shock_momentum_skew_63d": {"inputs": ["close", "volume"], "func": vsha_500_volume_shock_momentum_skew_63d},
    "vsha_501_volume_shock_momentum_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_501_volume_shock_momentum_kurt_63d},
    "vsha_502_volume_shock_momentum_skew_126d": {"inputs": ["close", "volume"], "func": vsha_502_volume_shock_momentum_skew_126d},
    "vsha_503_volume_shock_momentum_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_503_volume_shock_momentum_kurt_126d},
    "vsha_504_volume_shock_momentum_skew_252d": {"inputs": ["close", "volume"], "func": vsha_504_volume_shock_momentum_skew_252d},
    "vsha_505_volume_shock_momentum_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_505_volume_shock_momentum_kurt_252d},
    "vsha_506_shock_regime_shift_skew_5d": {"inputs": ["close", "volume"], "func": vsha_506_shock_regime_shift_skew_5d},
    "vsha_507_shock_regime_shift_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_507_shock_regime_shift_kurt_5d},
    "vsha_508_shock_regime_shift_skew_21d": {"inputs": ["close", "volume"], "func": vsha_508_shock_regime_shift_skew_21d},
    "vsha_509_shock_regime_shift_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_509_shock_regime_shift_kurt_21d},
    "vsha_510_shock_regime_shift_skew_63d": {"inputs": ["close", "volume"], "func": vsha_510_shock_regime_shift_skew_63d},
    "vsha_511_shock_regime_shift_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_511_shock_regime_shift_kurt_63d},
    "vsha_512_shock_regime_shift_skew_126d": {"inputs": ["close", "volume"], "func": vsha_512_shock_regime_shift_skew_126d},
    "vsha_513_shock_regime_shift_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_513_shock_regime_shift_kurt_126d},
    "vsha_514_shock_regime_shift_skew_252d": {"inputs": ["close", "volume"], "func": vsha_514_shock_regime_shift_skew_252d},
    "vsha_515_shock_regime_shift_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_515_shock_regime_shift_kurt_252d},
    "vsha_516_volume_shock_tail_corr_skew_5d": {"inputs": ["close", "volume"], "func": vsha_516_volume_shock_tail_corr_skew_5d},
    "vsha_517_volume_shock_tail_corr_kurt_5d": {"inputs": ["close", "volume"], "func": vsha_517_volume_shock_tail_corr_kurt_5d},
    "vsha_518_volume_shock_tail_corr_skew_21d": {"inputs": ["close", "volume"], "func": vsha_518_volume_shock_tail_corr_skew_21d},
    "vsha_519_volume_shock_tail_corr_kurt_21d": {"inputs": ["close", "volume"], "func": vsha_519_volume_shock_tail_corr_kurt_21d},
    "vsha_520_volume_shock_tail_corr_skew_63d": {"inputs": ["close", "volume"], "func": vsha_520_volume_shock_tail_corr_skew_63d},
    "vsha_521_volume_shock_tail_corr_kurt_63d": {"inputs": ["close", "volume"], "func": vsha_521_volume_shock_tail_corr_kurt_63d},
    "vsha_522_volume_shock_tail_corr_skew_126d": {"inputs": ["close", "volume"], "func": vsha_522_volume_shock_tail_corr_skew_126d},
    "vsha_523_volume_shock_tail_corr_kurt_126d": {"inputs": ["close", "volume"], "func": vsha_523_volume_shock_tail_corr_kurt_126d},
    "vsha_524_volume_shock_tail_corr_skew_252d": {"inputs": ["close", "volume"], "func": vsha_524_volume_shock_tail_corr_skew_252d},
    "vsha_525_volume_shock_tail_corr_kurt_252d": {"inputs": ["close", "volume"], "func": vsha_525_volume_shock_tail_corr_kurt_252d},
}
