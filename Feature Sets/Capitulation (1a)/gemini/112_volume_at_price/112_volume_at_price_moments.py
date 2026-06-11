"""
112_volume_at_price — Statistical Moments
Domain: volume_at_price
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

def vapr_376_volume_poc_dist_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_376_volume_poc_dist_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_poc_dist over 5d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(5).skew()

def vapr_377_volume_poc_dist_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_377_volume_poc_dist_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_poc_dist over 5d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(5).kurt()

def vapr_378_volume_poc_dist_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_378_volume_poc_dist_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_poc_dist over 21d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(21).skew()

def vapr_379_volume_poc_dist_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_379_volume_poc_dist_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_poc_dist over 21d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(21).kurt()

def vapr_380_volume_poc_dist_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_380_volume_poc_dist_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_poc_dist over 63d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(63).skew()

def vapr_381_volume_poc_dist_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_381_volume_poc_dist_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_poc_dist over 63d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(63).kurt()

def vapr_382_volume_poc_dist_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_382_volume_poc_dist_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_poc_dist over 126d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(126).skew()

def vapr_383_volume_poc_dist_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_383_volume_poc_dist_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_poc_dist over 126d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(126).kurt()

def vapr_384_volume_poc_dist_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_384_volume_poc_dist_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_poc_dist over 252d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(252).skew()

def vapr_385_volume_poc_dist_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_385_volume_poc_dist_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_poc_dist over 252d. Distance from the volume-weighted Point of Control.
    """
    return (close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(252).kurt()

def vapr_386_value_area_high_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_386_value_area_high_skew_5d
    ECONOMIC RATIONALE: Skewness of value_area_high over 5d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(5).skew()

def vapr_387_value_area_high_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_387_value_area_high_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of value_area_high over 5d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(5).kurt()

def vapr_388_value_area_high_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_388_value_area_high_skew_21d
    ECONOMIC RATIONALE: Skewness of value_area_high over 21d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(21).skew()

def vapr_389_value_area_high_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_389_value_area_high_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of value_area_high over 21d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(21).kurt()

def vapr_390_value_area_high_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_390_value_area_high_skew_63d
    ECONOMIC RATIONALE: Skewness of value_area_high over 63d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(63).skew()

def vapr_391_value_area_high_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_391_value_area_high_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of value_area_high over 63d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(63).kurt()

def vapr_392_value_area_high_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_392_value_area_high_skew_126d
    ECONOMIC RATIONALE: Skewness of value_area_high over 126d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(126).skew()

def vapr_393_value_area_high_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_393_value_area_high_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of value_area_high over 126d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(126).kurt()

def vapr_394_value_area_high_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_394_value_area_high_skew_252d
    ECONOMIC RATIONALE: Skewness of value_area_high over 252d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(252).skew()

def vapr_395_value_area_high_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_395_value_area_high_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of value_area_high over 252d. Upper bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.7)).rolling(252).kurt()

def vapr_396_value_area_low_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_396_value_area_low_skew_5d
    ECONOMIC RATIONALE: Skewness of value_area_low over 5d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(5).skew()

def vapr_397_value_area_low_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_397_value_area_low_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of value_area_low over 5d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(5).kurt()

def vapr_398_value_area_low_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_398_value_area_low_skew_21d
    ECONOMIC RATIONALE: Skewness of value_area_low over 21d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(21).skew()

def vapr_399_value_area_low_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_399_value_area_low_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of value_area_low over 21d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(21).kurt()

def vapr_400_value_area_low_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_400_value_area_low_skew_63d
    ECONOMIC RATIONALE: Skewness of value_area_low over 63d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(63).skew()

def vapr_401_value_area_low_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_401_value_area_low_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of value_area_low over 63d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(63).kurt()

def vapr_402_value_area_low_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_402_value_area_low_skew_126d
    ECONOMIC RATIONALE: Skewness of value_area_low over 126d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(126).skew()

def vapr_403_value_area_low_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_403_value_area_low_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of value_area_low over 126d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(126).kurt()

def vapr_404_value_area_low_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_404_value_area_low_skew_252d
    ECONOMIC RATIONALE: Skewness of value_area_low over 252d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(252).skew()

def vapr_405_value_area_low_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_405_value_area_low_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of value_area_low over 252d. Lower bound of the 70% volume value area.
    """
    return (close.rolling(63).quantile(0.3)).rolling(252).kurt()

def vapr_406_high_volume_node_dist_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_406_high_volume_node_dist_skew_5d
    ECONOMIC RATIONALE: Skewness of high_volume_node_dist over 5d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(5).skew()

def vapr_407_high_volume_node_dist_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_407_high_volume_node_dist_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of high_volume_node_dist over 5d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(5).kurt()

def vapr_408_high_volume_node_dist_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_408_high_volume_node_dist_skew_21d
    ECONOMIC RATIONALE: Skewness of high_volume_node_dist over 21d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(21).skew()

def vapr_409_high_volume_node_dist_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_409_high_volume_node_dist_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of high_volume_node_dist over 21d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(21).kurt()

def vapr_410_high_volume_node_dist_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_410_high_volume_node_dist_skew_63d
    ECONOMIC RATIONALE: Skewness of high_volume_node_dist over 63d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(63).skew()

def vapr_411_high_volume_node_dist_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_411_high_volume_node_dist_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of high_volume_node_dist over 63d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(63).kurt()

def vapr_412_high_volume_node_dist_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_412_high_volume_node_dist_skew_126d
    ECONOMIC RATIONALE: Skewness of high_volume_node_dist over 126d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(126).skew()

def vapr_413_high_volume_node_dist_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_413_high_volume_node_dist_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of high_volume_node_dist over 126d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(126).kurt()

def vapr_414_high_volume_node_dist_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_414_high_volume_node_dist_skew_252d
    ECONOMIC RATIONALE: Skewness of high_volume_node_dist over 252d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(252).skew()

def vapr_415_high_volume_node_dist_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_415_high_volume_node_dist_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of high_volume_node_dist over 252d. Distance from long-term high volume nodes.
    """
    return (close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])).rolling(252).kurt()

def vapr_416_low_volume_node_flag_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_416_low_volume_node_flag_skew_5d
    ECONOMIC RATIONALE: Skewness of low_volume_node_flag over 5d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(5).skew()

def vapr_417_low_volume_node_flag_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_417_low_volume_node_flag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of low_volume_node_flag over 5d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(5).kurt()

def vapr_418_low_volume_node_flag_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_418_low_volume_node_flag_skew_21d
    ECONOMIC RATIONALE: Skewness of low_volume_node_flag over 21d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(21).skew()

def vapr_419_low_volume_node_flag_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_419_low_volume_node_flag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of low_volume_node_flag over 21d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(21).kurt()

def vapr_420_low_volume_node_flag_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_420_low_volume_node_flag_skew_63d
    ECONOMIC RATIONALE: Skewness of low_volume_node_flag over 63d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(63).skew()

def vapr_421_low_volume_node_flag_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_421_low_volume_node_flag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of low_volume_node_flag over 63d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(63).kurt()

def vapr_422_low_volume_node_flag_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_422_low_volume_node_flag_skew_126d
    ECONOMIC RATIONALE: Skewness of low_volume_node_flag over 126d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(126).skew()

def vapr_423_low_volume_node_flag_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_423_low_volume_node_flag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of low_volume_node_flag over 126d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(126).kurt()

def vapr_424_low_volume_node_flag_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_424_low_volume_node_flag_skew_252d
    ECONOMIC RATIONALE: Skewness of low_volume_node_flag over 252d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(252).skew()

def vapr_425_low_volume_node_flag_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_425_low_volume_node_flag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of low_volume_node_flag over 252d. Trading in low-volume price vacuum zones.
    """
    return (((volume < volume.rolling(63).mean()*0.5)).astype(float)).rolling(252).kurt()

def vapr_426_volume_skew_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_426_volume_skew_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_skew over 5d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(5).skew()

def vapr_427_volume_skew_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_427_volume_skew_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_skew over 5d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(5).kurt()

def vapr_428_volume_skew_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_428_volume_skew_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_skew over 21d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(21).skew()

def vapr_429_volume_skew_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_429_volume_skew_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_skew over 21d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(21).kurt()

def vapr_430_volume_skew_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_430_volume_skew_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_skew over 63d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(63).skew()

def vapr_431_volume_skew_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_431_volume_skew_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_skew over 63d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(63).kurt()

def vapr_432_volume_skew_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_432_volume_skew_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_skew over 126d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(126).skew()

def vapr_433_volume_skew_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_433_volume_skew_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_skew over 126d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(126).kurt()

def vapr_434_volume_skew_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_434_volume_skew_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_skew over 252d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(252).skew()

def vapr_435_volume_skew_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_435_volume_skew_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_skew over 252d. Asymmetry of volume distribution across price.
    """
    return (volume.rolling(63).skew()).rolling(252).kurt()

def vapr_436_vapr_zscore_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_436_vapr_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of vapr_zscore over 5d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(5).skew()

def vapr_437_vapr_zscore_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_437_vapr_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vapr_zscore over 5d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(5).kurt()

def vapr_438_vapr_zscore_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_438_vapr_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of vapr_zscore over 21d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(21).skew()

def vapr_439_vapr_zscore_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_439_vapr_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vapr_zscore over 21d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(21).kurt()

def vapr_440_vapr_zscore_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_440_vapr_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of vapr_zscore over 63d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(63).skew()

def vapr_441_vapr_zscore_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_441_vapr_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vapr_zscore over 63d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(63).kurt()

def vapr_442_vapr_zscore_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_442_vapr_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of vapr_zscore over 126d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(126).skew()

def vapr_443_vapr_zscore_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_443_vapr_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vapr_zscore over 126d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(126).kurt()

def vapr_444_vapr_zscore_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_444_vapr_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of vapr_zscore over 252d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(252).skew()

def vapr_445_vapr_zscore_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_445_vapr_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vapr_zscore over 252d. Abnormality of volume per price unit.
    """
    return (_zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)).rolling(252).kurt()

def vapr_446_volume_concentration_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_446_volume_concentration_skew_5d
    ECONOMIC RATIONALE: Skewness of volume_concentration over 5d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(5).skew()

def vapr_447_volume_concentration_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_447_volume_concentration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of volume_concentration over 5d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(5).kurt()

def vapr_448_volume_concentration_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_448_volume_concentration_skew_21d
    ECONOMIC RATIONALE: Skewness of volume_concentration over 21d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(21).skew()

def vapr_449_volume_concentration_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_449_volume_concentration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of volume_concentration over 21d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(21).kurt()

def vapr_450_volume_concentration_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_450_volume_concentration_skew_63d
    ECONOMIC RATIONALE: Skewness of volume_concentration over 63d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(63).skew()

def vapr_451_volume_concentration_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_451_volume_concentration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of volume_concentration over 63d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(63).kurt()

def vapr_452_volume_concentration_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_452_volume_concentration_skew_126d
    ECONOMIC RATIONALE: Skewness of volume_concentration over 126d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(126).skew()

def vapr_453_volume_concentration_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_453_volume_concentration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of volume_concentration over 126d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(126).kurt()

def vapr_454_volume_concentration_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_454_volume_concentration_skew_252d
    ECONOMIC RATIONALE: Skewness of volume_concentration over 252d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(252).skew()

def vapr_455_volume_concentration_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_455_volume_concentration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of volume_concentration over 252d. Concentration of volume at current price levels.
    """
    return (volume.rolling(21).sum() / volume.rolling(252).sum()).rolling(252).kurt()

def vapr_456_price_volume_overlap_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_456_price_volume_overlap_skew_5d
    ECONOMIC RATIONALE: Skewness of price_volume_overlap over 5d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(5).skew()

def vapr_457_price_volume_overlap_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_457_price_volume_overlap_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of price_volume_overlap over 5d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(5).kurt()

def vapr_458_price_volume_overlap_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_458_price_volume_overlap_skew_21d
    ECONOMIC RATIONALE: Skewness of price_volume_overlap over 21d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(21).skew()

def vapr_459_price_volume_overlap_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_459_price_volume_overlap_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of price_volume_overlap over 21d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(21).kurt()

def vapr_460_price_volume_overlap_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_460_price_volume_overlap_skew_63d
    ECONOMIC RATIONALE: Skewness of price_volume_overlap over 63d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(63).skew()

def vapr_461_price_volume_overlap_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_461_price_volume_overlap_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of price_volume_overlap over 63d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(63).kurt()

def vapr_462_price_volume_overlap_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_462_price_volume_overlap_skew_126d
    ECONOMIC RATIONALE: Skewness of price_volume_overlap over 126d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(126).skew()

def vapr_463_price_volume_overlap_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_463_price_volume_overlap_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of price_volume_overlap over 126d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(126).kurt()

def vapr_464_price_volume_overlap_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_464_price_volume_overlap_skew_252d
    ECONOMIC RATIONALE: Skewness of price_volume_overlap over 252d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(252).skew()

def vapr_465_price_volume_overlap_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_465_price_volume_overlap_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of price_volume_overlap over 252d. Diversity of price levels traded recently.
    """
    return (close.rolling(21).apply(lambda x: len(np.unique(np.round(x, 2))))).rolling(252).kurt()

def vapr_466_vapr_momentum_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_466_vapr_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of vapr_momentum over 5d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(5).skew()

def vapr_467_vapr_momentum_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_467_vapr_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vapr_momentum over 5d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(5).kurt()

def vapr_468_vapr_momentum_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_468_vapr_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of vapr_momentum over 21d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(21).skew()

def vapr_469_vapr_momentum_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_469_vapr_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vapr_momentum over 21d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(21).kurt()

def vapr_470_vapr_momentum_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_470_vapr_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of vapr_momentum over 63d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(63).skew()

def vapr_471_vapr_momentum_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_471_vapr_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vapr_momentum over 63d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(63).kurt()

def vapr_472_vapr_momentum_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_472_vapr_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of vapr_momentum over 126d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(126).skew()

def vapr_473_vapr_momentum_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_473_vapr_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vapr_momentum over 126d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(126).kurt()

def vapr_474_vapr_momentum_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_474_vapr_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of vapr_momentum over 252d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(252).skew()

def vapr_475_vapr_momentum_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_475_vapr_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vapr_momentum over 252d. Volume-weighted price momentum.
    """
    return (volume.rolling(21).mean() * close.pct_change(21)).rolling(252).kurt()

def vapr_476_vapr_exhaustion_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_476_vapr_exhaustion_skew_5d
    ECONOMIC RATIONALE: Skewness of vapr_exhaustion over 5d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(5).skew()

def vapr_477_vapr_exhaustion_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_477_vapr_exhaustion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vapr_exhaustion over 5d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(5).kurt()

def vapr_478_vapr_exhaustion_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_478_vapr_exhaustion_skew_21d
    ECONOMIC RATIONALE: Skewness of vapr_exhaustion over 21d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(21).skew()

def vapr_479_vapr_exhaustion_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_479_vapr_exhaustion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vapr_exhaustion over 21d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(21).kurt()

def vapr_480_vapr_exhaustion_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_480_vapr_exhaustion_skew_63d
    ECONOMIC RATIONALE: Skewness of vapr_exhaustion over 63d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(63).skew()

def vapr_481_vapr_exhaustion_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_481_vapr_exhaustion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vapr_exhaustion over 63d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(63).kurt()

def vapr_482_vapr_exhaustion_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_482_vapr_exhaustion_skew_126d
    ECONOMIC RATIONALE: Skewness of vapr_exhaustion over 126d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(126).skew()

def vapr_483_vapr_exhaustion_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_483_vapr_exhaustion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vapr_exhaustion over 126d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(126).kurt()

def vapr_484_vapr_exhaustion_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_484_vapr_exhaustion_skew_252d
    ECONOMIC RATIONALE: Skewness of vapr_exhaustion over 252d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(252).skew()

def vapr_485_vapr_exhaustion_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_485_vapr_exhaustion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vapr_exhaustion over 252d. High volume with little price movement (churn).
    """
    return ((volume.rolling(5).mean() > volume.rolling(63).mean()*2) & (close.pct_change(5).abs() < 0.02)).rolling(252).kurt()

def vapr_486_support_volume_strength_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_486_support_volume_strength_skew_5d
    ECONOMIC RATIONALE: Skewness of support_volume_strength over 5d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(5).skew()

def vapr_487_support_volume_strength_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_487_support_volume_strength_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of support_volume_strength over 5d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(5).kurt()

def vapr_488_support_volume_strength_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_488_support_volume_strength_skew_21d
    ECONOMIC RATIONALE: Skewness of support_volume_strength over 21d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(21).skew()

def vapr_489_support_volume_strength_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_489_support_volume_strength_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of support_volume_strength over 21d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(21).kurt()

def vapr_490_support_volume_strength_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_490_support_volume_strength_skew_63d
    ECONOMIC RATIONALE: Skewness of support_volume_strength over 63d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(63).skew()

def vapr_491_support_volume_strength_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_491_support_volume_strength_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of support_volume_strength over 63d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(63).kurt()

def vapr_492_support_volume_strength_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_492_support_volume_strength_skew_126d
    ECONOMIC RATIONALE: Skewness of support_volume_strength over 126d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(126).skew()

def vapr_493_support_volume_strength_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_493_support_volume_strength_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of support_volume_strength over 126d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(126).kurt()

def vapr_494_support_volume_strength_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_494_support_volume_strength_skew_252d
    ECONOMIC RATIONALE: Skewness of support_volume_strength over 252d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(252).skew()

def vapr_495_support_volume_strength_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_495_support_volume_strength_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of support_volume_strength over 252d. Volume traded near structural support.
    """
    return (volume * (close < low.rolling(63).min()*1.05)).rolling(252).kurt()

def vapr_496_resistance_volume_strength_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_496_resistance_volume_strength_skew_5d
    ECONOMIC RATIONALE: Skewness of resistance_volume_strength over 5d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(5).skew()

def vapr_497_resistance_volume_strength_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_497_resistance_volume_strength_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of resistance_volume_strength over 5d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(5).kurt()

def vapr_498_resistance_volume_strength_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_498_resistance_volume_strength_skew_21d
    ECONOMIC RATIONALE: Skewness of resistance_volume_strength over 21d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(21).skew()

def vapr_499_resistance_volume_strength_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_499_resistance_volume_strength_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of resistance_volume_strength over 21d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(21).kurt()

def vapr_500_resistance_volume_strength_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_500_resistance_volume_strength_skew_63d
    ECONOMIC RATIONALE: Skewness of resistance_volume_strength over 63d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(63).skew()

def vapr_501_resistance_volume_strength_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_501_resistance_volume_strength_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of resistance_volume_strength over 63d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(63).kurt()

def vapr_502_resistance_volume_strength_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_502_resistance_volume_strength_skew_126d
    ECONOMIC RATIONALE: Skewness of resistance_volume_strength over 126d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(126).skew()

def vapr_503_resistance_volume_strength_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_503_resistance_volume_strength_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of resistance_volume_strength over 126d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(126).kurt()

def vapr_504_resistance_volume_strength_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_504_resistance_volume_strength_skew_252d
    ECONOMIC RATIONALE: Skewness of resistance_volume_strength over 252d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(252).skew()

def vapr_505_resistance_volume_strength_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_505_resistance_volume_strength_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of resistance_volume_strength over 252d. Volume traded near structural resistance.
    """
    return (volume * (close > high.rolling(63).max()*0.95)).rolling(252).kurt()

def vapr_506_vapr_regime_shift_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_506_vapr_regime_shift_skew_5d
    ECONOMIC RATIONALE: Skewness of vapr_regime_shift over 5d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(5).skew()

def vapr_507_vapr_regime_shift_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_507_vapr_regime_shift_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vapr_regime_shift over 5d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(5).kurt()

def vapr_508_vapr_regime_shift_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_508_vapr_regime_shift_skew_21d
    ECONOMIC RATIONALE: Skewness of vapr_regime_shift over 21d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(21).skew()

def vapr_509_vapr_regime_shift_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_509_vapr_regime_shift_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vapr_regime_shift over 21d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(21).kurt()

def vapr_510_vapr_regime_shift_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_510_vapr_regime_shift_skew_63d
    ECONOMIC RATIONALE: Skewness of vapr_regime_shift over 63d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(63).skew()

def vapr_511_vapr_regime_shift_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_511_vapr_regime_shift_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vapr_regime_shift over 63d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(63).kurt()

def vapr_512_vapr_regime_shift_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_512_vapr_regime_shift_skew_126d
    ECONOMIC RATIONALE: Skewness of vapr_regime_shift over 126d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(126).skew()

def vapr_513_vapr_regime_shift_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_513_vapr_regime_shift_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vapr_regime_shift over 126d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(126).kurt()

def vapr_514_vapr_regime_shift_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_514_vapr_regime_shift_skew_252d
    ECONOMIC RATIONALE: Skewness of vapr_regime_shift over 252d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(252).skew()

def vapr_515_vapr_regime_shift_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_515_vapr_regime_shift_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vapr_regime_shift over 252d. Shift in the price-volume correlation regime.
    """
    return (volume.rolling(21).corr(close).diff(21)).rolling(252).kurt()

def vapr_516_vapr_tail_volume_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_516_vapr_tail_volume_skew_5d
    ECONOMIC RATIONALE: Skewness of vapr_tail_volume over 5d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(5).skew()

def vapr_517_vapr_tail_volume_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_517_vapr_tail_volume_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of vapr_tail_volume over 5d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(5).kurt()

def vapr_518_vapr_tail_volume_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_518_vapr_tail_volume_skew_21d
    ECONOMIC RATIONALE: Skewness of vapr_tail_volume over 21d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(21).skew()

def vapr_519_vapr_tail_volume_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_519_vapr_tail_volume_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of vapr_tail_volume over 21d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(21).kurt()

def vapr_520_vapr_tail_volume_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_520_vapr_tail_volume_skew_63d
    ECONOMIC RATIONALE: Skewness of vapr_tail_volume over 63d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(63).skew()

def vapr_521_vapr_tail_volume_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_521_vapr_tail_volume_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of vapr_tail_volume over 63d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(63).kurt()

def vapr_522_vapr_tail_volume_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_522_vapr_tail_volume_skew_126d
    ECONOMIC RATIONALE: Skewness of vapr_tail_volume over 126d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(126).skew()

def vapr_523_vapr_tail_volume_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_523_vapr_tail_volume_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of vapr_tail_volume over 126d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(126).kurt()

def vapr_524_vapr_tail_volume_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_524_vapr_tail_volume_skew_252d
    ECONOMIC RATIONALE: Skewness of vapr_tail_volume over 252d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(252).skew()

def vapr_525_vapr_tail_volume_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_525_vapr_tail_volume_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of vapr_tail_volume over 252d. Volume associated with extreme low prices.
    """
    return (volume * (close < close.rolling(252).quantile(0.05))).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V112_REGISTRY_MOMENTS = {
    "vapr_376_volume_poc_dist_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_376_volume_poc_dist_skew_5d},
    "vapr_377_volume_poc_dist_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_377_volume_poc_dist_kurt_5d},
    "vapr_378_volume_poc_dist_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_378_volume_poc_dist_skew_21d},
    "vapr_379_volume_poc_dist_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_379_volume_poc_dist_kurt_21d},
    "vapr_380_volume_poc_dist_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_380_volume_poc_dist_skew_63d},
    "vapr_381_volume_poc_dist_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_381_volume_poc_dist_kurt_63d},
    "vapr_382_volume_poc_dist_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_382_volume_poc_dist_skew_126d},
    "vapr_383_volume_poc_dist_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_383_volume_poc_dist_kurt_126d},
    "vapr_384_volume_poc_dist_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_384_volume_poc_dist_skew_252d},
    "vapr_385_volume_poc_dist_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_385_volume_poc_dist_kurt_252d},
    "vapr_386_value_area_high_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_386_value_area_high_skew_5d},
    "vapr_387_value_area_high_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_387_value_area_high_kurt_5d},
    "vapr_388_value_area_high_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_388_value_area_high_skew_21d},
    "vapr_389_value_area_high_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_389_value_area_high_kurt_21d},
    "vapr_390_value_area_high_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_390_value_area_high_skew_63d},
    "vapr_391_value_area_high_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_391_value_area_high_kurt_63d},
    "vapr_392_value_area_high_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_392_value_area_high_skew_126d},
    "vapr_393_value_area_high_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_393_value_area_high_kurt_126d},
    "vapr_394_value_area_high_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_394_value_area_high_skew_252d},
    "vapr_395_value_area_high_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_395_value_area_high_kurt_252d},
    "vapr_396_value_area_low_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_396_value_area_low_skew_5d},
    "vapr_397_value_area_low_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_397_value_area_low_kurt_5d},
    "vapr_398_value_area_low_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_398_value_area_low_skew_21d},
    "vapr_399_value_area_low_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_399_value_area_low_kurt_21d},
    "vapr_400_value_area_low_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_400_value_area_low_skew_63d},
    "vapr_401_value_area_low_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_401_value_area_low_kurt_63d},
    "vapr_402_value_area_low_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_402_value_area_low_skew_126d},
    "vapr_403_value_area_low_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_403_value_area_low_kurt_126d},
    "vapr_404_value_area_low_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_404_value_area_low_skew_252d},
    "vapr_405_value_area_low_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_405_value_area_low_kurt_252d},
    "vapr_406_high_volume_node_dist_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_406_high_volume_node_dist_skew_5d},
    "vapr_407_high_volume_node_dist_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_407_high_volume_node_dist_kurt_5d},
    "vapr_408_high_volume_node_dist_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_408_high_volume_node_dist_skew_21d},
    "vapr_409_high_volume_node_dist_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_409_high_volume_node_dist_kurt_21d},
    "vapr_410_high_volume_node_dist_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_410_high_volume_node_dist_skew_63d},
    "vapr_411_high_volume_node_dist_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_411_high_volume_node_dist_kurt_63d},
    "vapr_412_high_volume_node_dist_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_412_high_volume_node_dist_skew_126d},
    "vapr_413_high_volume_node_dist_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_413_high_volume_node_dist_kurt_126d},
    "vapr_414_high_volume_node_dist_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_414_high_volume_node_dist_skew_252d},
    "vapr_415_high_volume_node_dist_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_415_high_volume_node_dist_kurt_252d},
    "vapr_416_low_volume_node_flag_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_416_low_volume_node_flag_skew_5d},
    "vapr_417_low_volume_node_flag_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_417_low_volume_node_flag_kurt_5d},
    "vapr_418_low_volume_node_flag_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_418_low_volume_node_flag_skew_21d},
    "vapr_419_low_volume_node_flag_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_419_low_volume_node_flag_kurt_21d},
    "vapr_420_low_volume_node_flag_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_420_low_volume_node_flag_skew_63d},
    "vapr_421_low_volume_node_flag_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_421_low_volume_node_flag_kurt_63d},
    "vapr_422_low_volume_node_flag_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_422_low_volume_node_flag_skew_126d},
    "vapr_423_low_volume_node_flag_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_423_low_volume_node_flag_kurt_126d},
    "vapr_424_low_volume_node_flag_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_424_low_volume_node_flag_skew_252d},
    "vapr_425_low_volume_node_flag_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_425_low_volume_node_flag_kurt_252d},
    "vapr_426_volume_skew_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_426_volume_skew_skew_5d},
    "vapr_427_volume_skew_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_427_volume_skew_kurt_5d},
    "vapr_428_volume_skew_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_428_volume_skew_skew_21d},
    "vapr_429_volume_skew_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_429_volume_skew_kurt_21d},
    "vapr_430_volume_skew_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_430_volume_skew_skew_63d},
    "vapr_431_volume_skew_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_431_volume_skew_kurt_63d},
    "vapr_432_volume_skew_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_432_volume_skew_skew_126d},
    "vapr_433_volume_skew_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_433_volume_skew_kurt_126d},
    "vapr_434_volume_skew_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_434_volume_skew_skew_252d},
    "vapr_435_volume_skew_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_435_volume_skew_kurt_252d},
    "vapr_436_vapr_zscore_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_436_vapr_zscore_skew_5d},
    "vapr_437_vapr_zscore_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_437_vapr_zscore_kurt_5d},
    "vapr_438_vapr_zscore_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_438_vapr_zscore_skew_21d},
    "vapr_439_vapr_zscore_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_439_vapr_zscore_kurt_21d},
    "vapr_440_vapr_zscore_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_440_vapr_zscore_skew_63d},
    "vapr_441_vapr_zscore_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_441_vapr_zscore_kurt_63d},
    "vapr_442_vapr_zscore_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_442_vapr_zscore_skew_126d},
    "vapr_443_vapr_zscore_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_443_vapr_zscore_kurt_126d},
    "vapr_444_vapr_zscore_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_444_vapr_zscore_skew_252d},
    "vapr_445_vapr_zscore_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_445_vapr_zscore_kurt_252d},
    "vapr_446_volume_concentration_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_446_volume_concentration_skew_5d},
    "vapr_447_volume_concentration_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_447_volume_concentration_kurt_5d},
    "vapr_448_volume_concentration_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_448_volume_concentration_skew_21d},
    "vapr_449_volume_concentration_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_449_volume_concentration_kurt_21d},
    "vapr_450_volume_concentration_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_450_volume_concentration_skew_63d},
    "vapr_451_volume_concentration_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_451_volume_concentration_kurt_63d},
    "vapr_452_volume_concentration_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_452_volume_concentration_skew_126d},
    "vapr_453_volume_concentration_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_453_volume_concentration_kurt_126d},
    "vapr_454_volume_concentration_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_454_volume_concentration_skew_252d},
    "vapr_455_volume_concentration_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_455_volume_concentration_kurt_252d},
    "vapr_456_price_volume_overlap_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_456_price_volume_overlap_skew_5d},
    "vapr_457_price_volume_overlap_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_457_price_volume_overlap_kurt_5d},
    "vapr_458_price_volume_overlap_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_458_price_volume_overlap_skew_21d},
    "vapr_459_price_volume_overlap_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_459_price_volume_overlap_kurt_21d},
    "vapr_460_price_volume_overlap_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_460_price_volume_overlap_skew_63d},
    "vapr_461_price_volume_overlap_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_461_price_volume_overlap_kurt_63d},
    "vapr_462_price_volume_overlap_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_462_price_volume_overlap_skew_126d},
    "vapr_463_price_volume_overlap_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_463_price_volume_overlap_kurt_126d},
    "vapr_464_price_volume_overlap_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_464_price_volume_overlap_skew_252d},
    "vapr_465_price_volume_overlap_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_465_price_volume_overlap_kurt_252d},
    "vapr_466_vapr_momentum_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_466_vapr_momentum_skew_5d},
    "vapr_467_vapr_momentum_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_467_vapr_momentum_kurt_5d},
    "vapr_468_vapr_momentum_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_468_vapr_momentum_skew_21d},
    "vapr_469_vapr_momentum_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_469_vapr_momentum_kurt_21d},
    "vapr_470_vapr_momentum_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_470_vapr_momentum_skew_63d},
    "vapr_471_vapr_momentum_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_471_vapr_momentum_kurt_63d},
    "vapr_472_vapr_momentum_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_472_vapr_momentum_skew_126d},
    "vapr_473_vapr_momentum_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_473_vapr_momentum_kurt_126d},
    "vapr_474_vapr_momentum_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_474_vapr_momentum_skew_252d},
    "vapr_475_vapr_momentum_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_475_vapr_momentum_kurt_252d},
    "vapr_476_vapr_exhaustion_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_476_vapr_exhaustion_skew_5d},
    "vapr_477_vapr_exhaustion_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_477_vapr_exhaustion_kurt_5d},
    "vapr_478_vapr_exhaustion_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_478_vapr_exhaustion_skew_21d},
    "vapr_479_vapr_exhaustion_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_479_vapr_exhaustion_kurt_21d},
    "vapr_480_vapr_exhaustion_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_480_vapr_exhaustion_skew_63d},
    "vapr_481_vapr_exhaustion_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_481_vapr_exhaustion_kurt_63d},
    "vapr_482_vapr_exhaustion_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_482_vapr_exhaustion_skew_126d},
    "vapr_483_vapr_exhaustion_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_483_vapr_exhaustion_kurt_126d},
    "vapr_484_vapr_exhaustion_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_484_vapr_exhaustion_skew_252d},
    "vapr_485_vapr_exhaustion_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_485_vapr_exhaustion_kurt_252d},
    "vapr_486_support_volume_strength_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_486_support_volume_strength_skew_5d},
    "vapr_487_support_volume_strength_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_487_support_volume_strength_kurt_5d},
    "vapr_488_support_volume_strength_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_488_support_volume_strength_skew_21d},
    "vapr_489_support_volume_strength_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_489_support_volume_strength_kurt_21d},
    "vapr_490_support_volume_strength_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_490_support_volume_strength_skew_63d},
    "vapr_491_support_volume_strength_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_491_support_volume_strength_kurt_63d},
    "vapr_492_support_volume_strength_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_492_support_volume_strength_skew_126d},
    "vapr_493_support_volume_strength_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_493_support_volume_strength_kurt_126d},
    "vapr_494_support_volume_strength_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_494_support_volume_strength_skew_252d},
    "vapr_495_support_volume_strength_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_495_support_volume_strength_kurt_252d},
    "vapr_496_resistance_volume_strength_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_496_resistance_volume_strength_skew_5d},
    "vapr_497_resistance_volume_strength_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_497_resistance_volume_strength_kurt_5d},
    "vapr_498_resistance_volume_strength_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_498_resistance_volume_strength_skew_21d},
    "vapr_499_resistance_volume_strength_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_499_resistance_volume_strength_kurt_21d},
    "vapr_500_resistance_volume_strength_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_500_resistance_volume_strength_skew_63d},
    "vapr_501_resistance_volume_strength_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_501_resistance_volume_strength_kurt_63d},
    "vapr_502_resistance_volume_strength_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_502_resistance_volume_strength_skew_126d},
    "vapr_503_resistance_volume_strength_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_503_resistance_volume_strength_kurt_126d},
    "vapr_504_resistance_volume_strength_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_504_resistance_volume_strength_skew_252d},
    "vapr_505_resistance_volume_strength_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_505_resistance_volume_strength_kurt_252d},
    "vapr_506_vapr_regime_shift_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_506_vapr_regime_shift_skew_5d},
    "vapr_507_vapr_regime_shift_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_507_vapr_regime_shift_kurt_5d},
    "vapr_508_vapr_regime_shift_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_508_vapr_regime_shift_skew_21d},
    "vapr_509_vapr_regime_shift_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_509_vapr_regime_shift_kurt_21d},
    "vapr_510_vapr_regime_shift_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_510_vapr_regime_shift_skew_63d},
    "vapr_511_vapr_regime_shift_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_511_vapr_regime_shift_kurt_63d},
    "vapr_512_vapr_regime_shift_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_512_vapr_regime_shift_skew_126d},
    "vapr_513_vapr_regime_shift_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_513_vapr_regime_shift_kurt_126d},
    "vapr_514_vapr_regime_shift_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_514_vapr_regime_shift_skew_252d},
    "vapr_515_vapr_regime_shift_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_515_vapr_regime_shift_kurt_252d},
    "vapr_516_vapr_tail_volume_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_516_vapr_tail_volume_skew_5d},
    "vapr_517_vapr_tail_volume_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_517_vapr_tail_volume_kurt_5d},
    "vapr_518_vapr_tail_volume_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_518_vapr_tail_volume_skew_21d},
    "vapr_519_vapr_tail_volume_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_519_vapr_tail_volume_kurt_21d},
    "vapr_520_vapr_tail_volume_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_520_vapr_tail_volume_skew_63d},
    "vapr_521_vapr_tail_volume_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_521_vapr_tail_volume_kurt_63d},
    "vapr_522_vapr_tail_volume_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_522_vapr_tail_volume_skew_126d},
    "vapr_523_vapr_tail_volume_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_523_vapr_tail_volume_kurt_126d},
    "vapr_524_vapr_tail_volume_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_524_vapr_tail_volume_skew_252d},
    "vapr_525_vapr_tail_volume_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_525_vapr_tail_volume_kurt_252d},
}
