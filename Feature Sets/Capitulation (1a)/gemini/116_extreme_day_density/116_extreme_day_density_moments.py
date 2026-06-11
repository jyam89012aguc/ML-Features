"""
116_extreme_day_density — Statistical Moments
Domain: extreme_day_density
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

def exdd_376_extreme_down_day_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_376_extreme_down_day_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_down_day over 5d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(5).skew()

def exdd_377_extreme_down_day_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_377_extreme_down_day_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_down_day over 5d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(5).kurt()

def exdd_378_extreme_down_day_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_378_extreme_down_day_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_down_day over 21d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(21).skew()

def exdd_379_extreme_down_day_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_379_extreme_down_day_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_down_day over 21d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(21).kurt()

def exdd_380_extreme_down_day_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_380_extreme_down_day_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_down_day over 63d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(63).skew()

def exdd_381_extreme_down_day_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_381_extreme_down_day_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_down_day over 63d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(63).kurt()

def exdd_382_extreme_down_day_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_382_extreme_down_day_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_down_day over 126d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(126).skew()

def exdd_383_extreme_down_day_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_383_extreme_down_day_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_down_day over 126d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(126).kurt()

def exdd_384_extreme_down_day_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_384_extreme_down_day_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_down_day over 252d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(252).skew()

def exdd_385_extreme_down_day_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_385_extreme_down_day_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_down_day over 252d. Frequency of days with >5% drops.
    """
    return ((close.pct_change(1) < -0.05).astype(float)).rolling(252).kurt()

def exdd_386_extreme_up_day_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_386_extreme_up_day_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_up_day over 5d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(5).skew()

def exdd_387_extreme_up_day_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_387_extreme_up_day_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_up_day over 5d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(5).kurt()

def exdd_388_extreme_up_day_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_388_extreme_up_day_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_up_day over 21d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(21).skew()

def exdd_389_extreme_up_day_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_389_extreme_up_day_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_up_day over 21d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(21).kurt()

def exdd_390_extreme_up_day_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_390_extreme_up_day_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_up_day over 63d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(63).skew()

def exdd_391_extreme_up_day_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_391_extreme_up_day_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_up_day over 63d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(63).kurt()

def exdd_392_extreme_up_day_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_392_extreme_up_day_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_up_day over 126d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(126).skew()

def exdd_393_extreme_up_day_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_393_extreme_up_day_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_up_day over 126d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(126).kurt()

def exdd_394_extreme_up_day_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_394_extreme_up_day_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_up_day over 252d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(252).skew()

def exdd_395_extreme_up_day_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_395_extreme_up_day_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_up_day over 252d. Frequency of days with >5% gains.
    """
    return ((close.pct_change(1) > 0.05).astype(float)).rolling(252).kurt()

def exdd_396_extreme_vol_day_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_396_extreme_vol_day_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_vol_day over 5d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(5).skew()

def exdd_397_extreme_vol_day_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_397_extreme_vol_day_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_day over 5d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(5).kurt()

def exdd_398_extreme_vol_day_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_398_extreme_vol_day_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_vol_day over 21d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(21).skew()

def exdd_399_extreme_vol_day_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_399_extreme_vol_day_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_day over 21d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(21).kurt()

def exdd_400_extreme_vol_day_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_400_extreme_vol_day_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_vol_day over 63d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(63).skew()

def exdd_401_extreme_vol_day_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_401_extreme_vol_day_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_day over 63d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(63).kurt()

def exdd_402_extreme_vol_day_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_402_extreme_vol_day_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_vol_day over 126d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(126).skew()

def exdd_403_extreme_vol_day_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_403_extreme_vol_day_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_day over 126d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(126).kurt()

def exdd_404_extreme_vol_day_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_404_extreme_vol_day_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_vol_day over 252d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(252).skew()

def exdd_405_extreme_vol_day_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_405_extreme_vol_day_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_day over 252d. Frequency of days with >300% average volume.
    """
    return ((volume > volume.rolling(63).mean() * 3).astype(float)).rolling(252).kurt()

def exdd_406_extreme_day_cluster_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_406_extreme_day_cluster_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_cluster over 5d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(5).skew()

def exdd_407_extreme_day_cluster_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_407_extreme_day_cluster_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_cluster over 5d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(5).kurt()

def exdd_408_extreme_day_cluster_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_408_extreme_day_cluster_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_cluster over 21d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(21).skew()

def exdd_409_extreme_day_cluster_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_409_extreme_day_cluster_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_cluster over 21d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(21).kurt()

def exdd_410_extreme_day_cluster_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_410_extreme_day_cluster_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_cluster over 63d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(63).skew()

def exdd_411_extreme_day_cluster_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_411_extreme_day_cluster_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_cluster over 63d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(63).kurt()

def exdd_412_extreme_day_cluster_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_412_extreme_day_cluster_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_cluster over 126d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(126).skew()

def exdd_413_extreme_day_cluster_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_413_extreme_day_cluster_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_cluster over 126d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(126).kurt()

def exdd_414_extreme_day_cluster_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_414_extreme_day_cluster_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_cluster over 252d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(252).skew()

def exdd_415_extreme_day_cluster_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_415_extreme_day_cluster_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_cluster over 252d. Clustering of high-magnitude price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum())).rolling(252).kurt()

def exdd_416_extreme_day_bias_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_416_extreme_day_bias_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_bias over 5d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(5).skew()

def exdd_417_extreme_day_bias_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_417_extreme_day_bias_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_bias over 5d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(5).kurt()

def exdd_418_extreme_day_bias_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_418_extreme_day_bias_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_bias over 21d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(21).skew()

def exdd_419_extreme_day_bias_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_419_extreme_day_bias_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_bias over 21d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(21).kurt()

def exdd_420_extreme_day_bias_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_420_extreme_day_bias_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_bias over 63d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(63).skew()

def exdd_421_extreme_day_bias_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_421_extreme_day_bias_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_bias over 63d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(63).kurt()

def exdd_422_extreme_day_bias_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_422_extreme_day_bias_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_bias over 126d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(126).skew()

def exdd_423_extreme_day_bias_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_423_extreme_day_bias_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_bias over 126d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(126).kurt()

def exdd_424_extreme_day_bias_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_424_extreme_day_bias_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_bias over 252d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(252).skew()

def exdd_425_extreme_day_bias_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_425_extreme_day_bias_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_bias over 252d. Net density of extreme down vs up days.
    """
    return (((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())).rolling(252).kurt()

def exdd_426_extreme_vol_price_sync_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_426_extreme_vol_price_sync_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_vol_price_sync over 5d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(5).skew()

def exdd_427_extreme_vol_price_sync_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_427_extreme_vol_price_sync_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_price_sync over 5d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(5).kurt()

def exdd_428_extreme_vol_price_sync_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_428_extreme_vol_price_sync_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_vol_price_sync over 21d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(21).skew()

def exdd_429_extreme_vol_price_sync_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_429_extreme_vol_price_sync_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_price_sync over 21d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(21).kurt()

def exdd_430_extreme_vol_price_sync_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_430_extreme_vol_price_sync_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_vol_price_sync over 63d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(63).skew()

def exdd_431_extreme_vol_price_sync_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_431_extreme_vol_price_sync_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_price_sync over 63d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(63).kurt()

def exdd_432_extreme_vol_price_sync_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_432_extreme_vol_price_sync_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_vol_price_sync over 126d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(126).skew()

def exdd_433_extreme_vol_price_sync_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_433_extreme_vol_price_sync_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_price_sync over 126d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(126).kurt()

def exdd_434_extreme_vol_price_sync_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_434_extreme_vol_price_sync_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_vol_price_sync over 252d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(252).skew()

def exdd_435_extreme_vol_price_sync_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_435_extreme_vol_price_sync_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_vol_price_sync over 252d. Co-occurrence of extreme drops and high volume.
    """
    return (((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()).rolling(252).kurt()

def exdd_436_extreme_day_z_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_436_extreme_day_z_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_z over 5d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(5).skew()

def exdd_437_extreme_day_z_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_437_extreme_day_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_z over 5d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(5).kurt()

def exdd_438_extreme_day_z_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_438_extreme_day_z_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_z over 21d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(21).skew()

def exdd_439_extreme_day_z_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_439_extreme_day_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_z over 21d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(21).kurt()

def exdd_440_extreme_day_z_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_440_extreme_day_z_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_z over 63d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(63).skew()

def exdd_441_extreme_day_z_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_441_extreme_day_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_z over 63d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(63).kurt()

def exdd_442_extreme_day_z_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_442_extreme_day_z_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_z over 126d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(126).skew()

def exdd_443_extreme_day_z_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_443_extreme_day_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_z over 126d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(126).kurt()

def exdd_444_extreme_day_z_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_444_extreme_day_z_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_z over 252d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(252).skew()

def exdd_445_extreme_day_z_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_445_extreme_day_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_z over 252d. Abnormality of current extreme day density.
    """
    return (_zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)).rolling(252).kurt()

def exdd_446_extreme_day_momentum_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_446_extreme_day_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_momentum over 5d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(5).skew()

def exdd_447_extreme_day_momentum_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_447_extreme_day_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_momentum over 5d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(5).kurt()

def exdd_448_extreme_day_momentum_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_448_extreme_day_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_momentum over 21d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(21).skew()

def exdd_449_extreme_day_momentum_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_449_extreme_day_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_momentum over 21d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(21).kurt()

def exdd_450_extreme_day_momentum_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_450_extreme_day_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_momentum over 63d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(63).skew()

def exdd_451_extreme_day_momentum_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_451_extreme_day_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_momentum over 63d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(63).kurt()

def exdd_452_extreme_day_momentum_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_452_extreme_day_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_momentum over 126d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(126).skew()

def exdd_453_extreme_day_momentum_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_453_extreme_day_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_momentum over 126d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(126).kurt()

def exdd_454_extreme_day_momentum_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_454_extreme_day_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_momentum over 252d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(252).skew()

def exdd_455_extreme_day_momentum_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_455_extreme_day_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_momentum over 252d. Change in extreme day frequency.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)).rolling(252).kurt()

def exdd_456_extreme_range_day_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_456_extreme_range_day_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_range_day over 5d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(5).skew()

def exdd_457_extreme_range_day_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_457_extreme_range_day_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_range_day over 5d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(5).kurt()

def exdd_458_extreme_range_day_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_458_extreme_range_day_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_range_day over 21d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(21).skew()

def exdd_459_extreme_range_day_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_459_extreme_range_day_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_range_day over 21d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(21).kurt()

def exdd_460_extreme_range_day_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_460_extreme_range_day_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_range_day over 63d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(63).skew()

def exdd_461_extreme_range_day_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_461_extreme_range_day_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_range_day over 63d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(63).kurt()

def exdd_462_extreme_range_day_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_462_extreme_range_day_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_range_day over 126d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(126).skew()

def exdd_463_extreme_range_day_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_463_extreme_range_day_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_range_day over 126d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(126).kurt()

def exdd_464_extreme_range_day_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_464_extreme_range_day_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_range_day over 252d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(252).skew()

def exdd_465_extreme_range_day_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_465_extreme_range_day_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_range_day over 252d. Frequency of days with >10% intraday ranges.
    """
    return (((high - low) / close > 0.1).astype(float)).rolling(252).kurt()

def exdd_466_extreme_gap_day_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_466_extreme_gap_day_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_gap_day over 5d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(5).skew()

def exdd_467_extreme_gap_day_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_467_extreme_gap_day_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_gap_day over 5d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(5).kurt()

def exdd_468_extreme_gap_day_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_468_extreme_gap_day_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_gap_day over 21d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(21).skew()

def exdd_469_extreme_gap_day_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_469_extreme_gap_day_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_gap_day over 21d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(21).kurt()

def exdd_470_extreme_gap_day_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_470_extreme_gap_day_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_gap_day over 63d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(63).skew()

def exdd_471_extreme_gap_day_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_471_extreme_gap_day_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_gap_day over 63d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(63).kurt()

def exdd_472_extreme_gap_day_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_472_extreme_gap_day_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_gap_day over 126d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(126).skew()

def exdd_473_extreme_gap_day_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_473_extreme_gap_day_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_gap_day over 126d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(126).kurt()

def exdd_474_extreme_gap_day_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_474_extreme_gap_day_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_gap_day over 252d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(252).skew()

def exdd_475_extreme_gap_day_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_475_extreme_gap_day_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_gap_day over 252d. Frequency of days with >3% overnight gaps.
    """
    return ((abs(open/close.shift(1)-1) > 0.03).astype(float)).rolling(252).kurt()

def exdd_476_extreme_day_persistence_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_476_extreme_day_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_persistence over 5d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(5).skew()

def exdd_477_extreme_day_persistence_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_477_extreme_day_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_persistence over 5d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(5).kurt()

def exdd_478_extreme_day_persistence_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_478_extreme_day_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_persistence over 21d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(21).skew()

def exdd_479_extreme_day_persistence_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_479_extreme_day_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_persistence over 21d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(21).kurt()

def exdd_480_extreme_day_persistence_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_480_extreme_day_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_persistence over 63d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(63).skew()

def exdd_481_extreme_day_persistence_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_481_extreme_day_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_persistence over 63d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(63).kurt()

def exdd_482_extreme_day_persistence_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_482_extreme_day_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_persistence over 126d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(126).skew()

def exdd_483_extreme_day_persistence_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_483_extreme_day_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_persistence over 126d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(126).kurt()

def exdd_484_extreme_day_persistence_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_484_extreme_day_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_persistence over 252d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(252).skew()

def exdd_485_extreme_day_persistence_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_485_extreme_day_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_persistence over 252d. Sequential extreme price days.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(5).sum() > 2).astype(float)).rolling(252).kurt()

def exdd_486_extreme_day_decay_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_486_extreme_day_decay_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_decay over 5d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(5).skew()

def exdd_487_extreme_day_decay_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_487_extreme_day_decay_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_decay over 5d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(5).kurt()

def exdd_488_extreme_day_decay_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_488_extreme_day_decay_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_decay over 21d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(21).skew()

def exdd_489_extreme_day_decay_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_489_extreme_day_decay_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_decay over 21d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(21).kurt()

def exdd_490_extreme_day_decay_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_490_extreme_day_decay_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_decay over 63d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(63).skew()

def exdd_491_extreme_day_decay_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_491_extreme_day_decay_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_decay over 63d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(63).kurt()

def exdd_492_extreme_day_decay_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_492_extreme_day_decay_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_decay over 126d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(126).skew()

def exdd_493_extreme_day_decay_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_493_extreme_day_decay_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_decay over 126d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(126).kurt()

def exdd_494_extreme_day_decay_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_494_extreme_day_decay_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_decay over 252d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(252).skew()

def exdd_495_extreme_day_decay_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_495_extreme_day_decay_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_decay over 252d. Time-weighted density of extreme events.
    """
    return (((close.pct_change(1).abs() > 0.05).astype(float)).ewm(span=63).mean()).rolling(252).kurt()

def exdd_496_extreme_day_vol_ratio_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_496_extreme_day_vol_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_vol_ratio over 5d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(5).skew()

def exdd_497_extreme_day_vol_ratio_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_497_extreme_day_vol_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_vol_ratio over 5d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(5).kurt()

def exdd_498_extreme_day_vol_ratio_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_498_extreme_day_vol_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_vol_ratio over 21d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(21).skew()

def exdd_499_extreme_day_vol_ratio_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_499_extreme_day_vol_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_vol_ratio over 21d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(21).kurt()

def exdd_500_extreme_day_vol_ratio_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_500_extreme_day_vol_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_vol_ratio over 63d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(63).skew()

def exdd_501_extreme_day_vol_ratio_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_501_extreme_day_vol_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_vol_ratio over 63d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(63).kurt()

def exdd_502_extreme_day_vol_ratio_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_502_extreme_day_vol_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_vol_ratio over 126d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(126).skew()

def exdd_503_extreme_day_vol_ratio_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_503_extreme_day_vol_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_vol_ratio over 126d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(126).kurt()

def exdd_504_extreme_day_vol_ratio_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_504_extreme_day_vol_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_vol_ratio over 252d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(252).skew()

def exdd_505_extreme_day_vol_ratio_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_505_extreme_day_vol_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_vol_ratio over 252d. Volume intensity on extreme days.
    """
    return (volume * (close.pct_change(1).abs() > 0.05) / volume.rolling(63).mean()).rolling(252).kurt()

def exdd_506_extreme_day_regime_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_506_extreme_day_regime_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_regime over 5d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(5).skew()

def exdd_507_extreme_day_regime_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_507_extreme_day_regime_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_regime over 5d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(5).kurt()

def exdd_508_extreme_day_regime_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_508_extreme_day_regime_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_regime over 21d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(21).skew()

def exdd_509_extreme_day_regime_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_509_extreme_day_regime_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_regime over 21d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(21).kurt()

def exdd_510_extreme_day_regime_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_510_extreme_day_regime_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_regime over 63d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(63).skew()

def exdd_511_extreme_day_regime_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_511_extreme_day_regime_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_regime over 63d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(63).kurt()

def exdd_512_extreme_day_regime_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_512_extreme_day_regime_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_regime over 126d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(126).skew()

def exdd_513_extreme_day_regime_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_513_extreme_day_regime_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_regime over 126d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(126).kurt()

def exdd_514_extreme_day_regime_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_514_extreme_day_regime_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_regime over 252d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(252).skew()

def exdd_515_extreme_day_regime_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_515_extreme_day_regime_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_regime over 252d. Proportion of days that are extreme.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(63).sum()) / 63).rolling(252).kurt()

def exdd_516_extreme_day_exhaustion_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_516_extreme_day_exhaustion_skew_5d
    ECONOMIC RATIONALE: Skewness of extreme_day_exhaustion over 5d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(5).skew()

def exdd_517_extreme_day_exhaustion_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_517_extreme_day_exhaustion_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_exhaustion over 5d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(5).kurt()

def exdd_518_extreme_day_exhaustion_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_518_extreme_day_exhaustion_skew_21d
    ECONOMIC RATIONALE: Skewness of extreme_day_exhaustion over 21d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(21).skew()

def exdd_519_extreme_day_exhaustion_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_519_extreme_day_exhaustion_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_exhaustion over 21d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(21).kurt()

def exdd_520_extreme_day_exhaustion_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_520_extreme_day_exhaustion_skew_63d
    ECONOMIC RATIONALE: Skewness of extreme_day_exhaustion over 63d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(63).skew()

def exdd_521_extreme_day_exhaustion_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_521_extreme_day_exhaustion_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_exhaustion over 63d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(63).kurt()

def exdd_522_extreme_day_exhaustion_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_522_extreme_day_exhaustion_skew_126d
    ECONOMIC RATIONALE: Skewness of extreme_day_exhaustion over 126d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(126).skew()

def exdd_523_extreme_day_exhaustion_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_523_extreme_day_exhaustion_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_exhaustion over 126d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(126).kurt()

def exdd_524_extreme_day_exhaustion_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_524_extreme_day_exhaustion_skew_252d
    ECONOMIC RATIONALE: Skewness of extreme_day_exhaustion over 252d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(252).skew()

def exdd_525_extreme_day_exhaustion_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_525_extreme_day_exhaustion_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of extreme_day_exhaustion over 252d. High density of extreme days followed by price stalling.
    """
    return (((close.pct_change(1).abs() > 0.05).rolling(21).sum() > 5) & (close.pct_change(5).abs() < 0.02)).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V116_REGISTRY_MOMENTS = {
    "exdd_376_extreme_down_day_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_376_extreme_down_day_skew_5d},
    "exdd_377_extreme_down_day_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_377_extreme_down_day_kurt_5d},
    "exdd_378_extreme_down_day_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_378_extreme_down_day_skew_21d},
    "exdd_379_extreme_down_day_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_379_extreme_down_day_kurt_21d},
    "exdd_380_extreme_down_day_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_380_extreme_down_day_skew_63d},
    "exdd_381_extreme_down_day_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_381_extreme_down_day_kurt_63d},
    "exdd_382_extreme_down_day_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_382_extreme_down_day_skew_126d},
    "exdd_383_extreme_down_day_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_383_extreme_down_day_kurt_126d},
    "exdd_384_extreme_down_day_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_384_extreme_down_day_skew_252d},
    "exdd_385_extreme_down_day_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_385_extreme_down_day_kurt_252d},
    "exdd_386_extreme_up_day_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_386_extreme_up_day_skew_5d},
    "exdd_387_extreme_up_day_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_387_extreme_up_day_kurt_5d},
    "exdd_388_extreme_up_day_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_388_extreme_up_day_skew_21d},
    "exdd_389_extreme_up_day_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_389_extreme_up_day_kurt_21d},
    "exdd_390_extreme_up_day_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_390_extreme_up_day_skew_63d},
    "exdd_391_extreme_up_day_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_391_extreme_up_day_kurt_63d},
    "exdd_392_extreme_up_day_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_392_extreme_up_day_skew_126d},
    "exdd_393_extreme_up_day_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_393_extreme_up_day_kurt_126d},
    "exdd_394_extreme_up_day_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_394_extreme_up_day_skew_252d},
    "exdd_395_extreme_up_day_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_395_extreme_up_day_kurt_252d},
    "exdd_396_extreme_vol_day_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_396_extreme_vol_day_skew_5d},
    "exdd_397_extreme_vol_day_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_397_extreme_vol_day_kurt_5d},
    "exdd_398_extreme_vol_day_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_398_extreme_vol_day_skew_21d},
    "exdd_399_extreme_vol_day_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_399_extreme_vol_day_kurt_21d},
    "exdd_400_extreme_vol_day_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_400_extreme_vol_day_skew_63d},
    "exdd_401_extreme_vol_day_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_401_extreme_vol_day_kurt_63d},
    "exdd_402_extreme_vol_day_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_402_extreme_vol_day_skew_126d},
    "exdd_403_extreme_vol_day_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_403_extreme_vol_day_kurt_126d},
    "exdd_404_extreme_vol_day_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_404_extreme_vol_day_skew_252d},
    "exdd_405_extreme_vol_day_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_405_extreme_vol_day_kurt_252d},
    "exdd_406_extreme_day_cluster_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_406_extreme_day_cluster_skew_5d},
    "exdd_407_extreme_day_cluster_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_407_extreme_day_cluster_kurt_5d},
    "exdd_408_extreme_day_cluster_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_408_extreme_day_cluster_skew_21d},
    "exdd_409_extreme_day_cluster_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_409_extreme_day_cluster_kurt_21d},
    "exdd_410_extreme_day_cluster_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_410_extreme_day_cluster_skew_63d},
    "exdd_411_extreme_day_cluster_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_411_extreme_day_cluster_kurt_63d},
    "exdd_412_extreme_day_cluster_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_412_extreme_day_cluster_skew_126d},
    "exdd_413_extreme_day_cluster_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_413_extreme_day_cluster_kurt_126d},
    "exdd_414_extreme_day_cluster_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_414_extreme_day_cluster_skew_252d},
    "exdd_415_extreme_day_cluster_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_415_extreme_day_cluster_kurt_252d},
    "exdd_416_extreme_day_bias_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_416_extreme_day_bias_skew_5d},
    "exdd_417_extreme_day_bias_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_417_extreme_day_bias_kurt_5d},
    "exdd_418_extreme_day_bias_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_418_extreme_day_bias_skew_21d},
    "exdd_419_extreme_day_bias_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_419_extreme_day_bias_kurt_21d},
    "exdd_420_extreme_day_bias_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_420_extreme_day_bias_skew_63d},
    "exdd_421_extreme_day_bias_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_421_extreme_day_bias_kurt_63d},
    "exdd_422_extreme_day_bias_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_422_extreme_day_bias_skew_126d},
    "exdd_423_extreme_day_bias_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_423_extreme_day_bias_kurt_126d},
    "exdd_424_extreme_day_bias_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_424_extreme_day_bias_skew_252d},
    "exdd_425_extreme_day_bias_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_425_extreme_day_bias_kurt_252d},
    "exdd_426_extreme_vol_price_sync_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_426_extreme_vol_price_sync_skew_5d},
    "exdd_427_extreme_vol_price_sync_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_427_extreme_vol_price_sync_kurt_5d},
    "exdd_428_extreme_vol_price_sync_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_428_extreme_vol_price_sync_skew_21d},
    "exdd_429_extreme_vol_price_sync_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_429_extreme_vol_price_sync_kurt_21d},
    "exdd_430_extreme_vol_price_sync_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_430_extreme_vol_price_sync_skew_63d},
    "exdd_431_extreme_vol_price_sync_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_431_extreme_vol_price_sync_kurt_63d},
    "exdd_432_extreme_vol_price_sync_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_432_extreme_vol_price_sync_skew_126d},
    "exdd_433_extreme_vol_price_sync_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_433_extreme_vol_price_sync_kurt_126d},
    "exdd_434_extreme_vol_price_sync_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_434_extreme_vol_price_sync_skew_252d},
    "exdd_435_extreme_vol_price_sync_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_435_extreme_vol_price_sync_kurt_252d},
    "exdd_436_extreme_day_z_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_436_extreme_day_z_skew_5d},
    "exdd_437_extreme_day_z_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_437_extreme_day_z_kurt_5d},
    "exdd_438_extreme_day_z_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_438_extreme_day_z_skew_21d},
    "exdd_439_extreme_day_z_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_439_extreme_day_z_kurt_21d},
    "exdd_440_extreme_day_z_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_440_extreme_day_z_skew_63d},
    "exdd_441_extreme_day_z_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_441_extreme_day_z_kurt_63d},
    "exdd_442_extreme_day_z_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_442_extreme_day_z_skew_126d},
    "exdd_443_extreme_day_z_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_443_extreme_day_z_kurt_126d},
    "exdd_444_extreme_day_z_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_444_extreme_day_z_skew_252d},
    "exdd_445_extreme_day_z_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_445_extreme_day_z_kurt_252d},
    "exdd_446_extreme_day_momentum_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_446_extreme_day_momentum_skew_5d},
    "exdd_447_extreme_day_momentum_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_447_extreme_day_momentum_kurt_5d},
    "exdd_448_extreme_day_momentum_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_448_extreme_day_momentum_skew_21d},
    "exdd_449_extreme_day_momentum_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_449_extreme_day_momentum_kurt_21d},
    "exdd_450_extreme_day_momentum_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_450_extreme_day_momentum_skew_63d},
    "exdd_451_extreme_day_momentum_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_451_extreme_day_momentum_kurt_63d},
    "exdd_452_extreme_day_momentum_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_452_extreme_day_momentum_skew_126d},
    "exdd_453_extreme_day_momentum_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_453_extreme_day_momentum_kurt_126d},
    "exdd_454_extreme_day_momentum_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_454_extreme_day_momentum_skew_252d},
    "exdd_455_extreme_day_momentum_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_455_extreme_day_momentum_kurt_252d},
    "exdd_456_extreme_range_day_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_456_extreme_range_day_skew_5d},
    "exdd_457_extreme_range_day_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_457_extreme_range_day_kurt_5d},
    "exdd_458_extreme_range_day_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_458_extreme_range_day_skew_21d},
    "exdd_459_extreme_range_day_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_459_extreme_range_day_kurt_21d},
    "exdd_460_extreme_range_day_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_460_extreme_range_day_skew_63d},
    "exdd_461_extreme_range_day_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_461_extreme_range_day_kurt_63d},
    "exdd_462_extreme_range_day_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_462_extreme_range_day_skew_126d},
    "exdd_463_extreme_range_day_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_463_extreme_range_day_kurt_126d},
    "exdd_464_extreme_range_day_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_464_extreme_range_day_skew_252d},
    "exdd_465_extreme_range_day_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_465_extreme_range_day_kurt_252d},
    "exdd_466_extreme_gap_day_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_466_extreme_gap_day_skew_5d},
    "exdd_467_extreme_gap_day_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_467_extreme_gap_day_kurt_5d},
    "exdd_468_extreme_gap_day_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_468_extreme_gap_day_skew_21d},
    "exdd_469_extreme_gap_day_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_469_extreme_gap_day_kurt_21d},
    "exdd_470_extreme_gap_day_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_470_extreme_gap_day_skew_63d},
    "exdd_471_extreme_gap_day_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_471_extreme_gap_day_kurt_63d},
    "exdd_472_extreme_gap_day_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_472_extreme_gap_day_skew_126d},
    "exdd_473_extreme_gap_day_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_473_extreme_gap_day_kurt_126d},
    "exdd_474_extreme_gap_day_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_474_extreme_gap_day_skew_252d},
    "exdd_475_extreme_gap_day_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_475_extreme_gap_day_kurt_252d},
    "exdd_476_extreme_day_persistence_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_476_extreme_day_persistence_skew_5d},
    "exdd_477_extreme_day_persistence_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_477_extreme_day_persistence_kurt_5d},
    "exdd_478_extreme_day_persistence_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_478_extreme_day_persistence_skew_21d},
    "exdd_479_extreme_day_persistence_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_479_extreme_day_persistence_kurt_21d},
    "exdd_480_extreme_day_persistence_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_480_extreme_day_persistence_skew_63d},
    "exdd_481_extreme_day_persistence_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_481_extreme_day_persistence_kurt_63d},
    "exdd_482_extreme_day_persistence_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_482_extreme_day_persistence_skew_126d},
    "exdd_483_extreme_day_persistence_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_483_extreme_day_persistence_kurt_126d},
    "exdd_484_extreme_day_persistence_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_484_extreme_day_persistence_skew_252d},
    "exdd_485_extreme_day_persistence_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_485_extreme_day_persistence_kurt_252d},
    "exdd_486_extreme_day_decay_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_486_extreme_day_decay_skew_5d},
    "exdd_487_extreme_day_decay_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_487_extreme_day_decay_kurt_5d},
    "exdd_488_extreme_day_decay_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_488_extreme_day_decay_skew_21d},
    "exdd_489_extreme_day_decay_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_489_extreme_day_decay_kurt_21d},
    "exdd_490_extreme_day_decay_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_490_extreme_day_decay_skew_63d},
    "exdd_491_extreme_day_decay_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_491_extreme_day_decay_kurt_63d},
    "exdd_492_extreme_day_decay_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_492_extreme_day_decay_skew_126d},
    "exdd_493_extreme_day_decay_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_493_extreme_day_decay_kurt_126d},
    "exdd_494_extreme_day_decay_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_494_extreme_day_decay_skew_252d},
    "exdd_495_extreme_day_decay_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_495_extreme_day_decay_kurt_252d},
    "exdd_496_extreme_day_vol_ratio_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_496_extreme_day_vol_ratio_skew_5d},
    "exdd_497_extreme_day_vol_ratio_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_497_extreme_day_vol_ratio_kurt_5d},
    "exdd_498_extreme_day_vol_ratio_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_498_extreme_day_vol_ratio_skew_21d},
    "exdd_499_extreme_day_vol_ratio_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_499_extreme_day_vol_ratio_kurt_21d},
    "exdd_500_extreme_day_vol_ratio_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_500_extreme_day_vol_ratio_skew_63d},
    "exdd_501_extreme_day_vol_ratio_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_501_extreme_day_vol_ratio_kurt_63d},
    "exdd_502_extreme_day_vol_ratio_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_502_extreme_day_vol_ratio_skew_126d},
    "exdd_503_extreme_day_vol_ratio_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_503_extreme_day_vol_ratio_kurt_126d},
    "exdd_504_extreme_day_vol_ratio_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_504_extreme_day_vol_ratio_skew_252d},
    "exdd_505_extreme_day_vol_ratio_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_505_extreme_day_vol_ratio_kurt_252d},
    "exdd_506_extreme_day_regime_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_506_extreme_day_regime_skew_5d},
    "exdd_507_extreme_day_regime_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_507_extreme_day_regime_kurt_5d},
    "exdd_508_extreme_day_regime_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_508_extreme_day_regime_skew_21d},
    "exdd_509_extreme_day_regime_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_509_extreme_day_regime_kurt_21d},
    "exdd_510_extreme_day_regime_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_510_extreme_day_regime_skew_63d},
    "exdd_511_extreme_day_regime_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_511_extreme_day_regime_kurt_63d},
    "exdd_512_extreme_day_regime_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_512_extreme_day_regime_skew_126d},
    "exdd_513_extreme_day_regime_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_513_extreme_day_regime_kurt_126d},
    "exdd_514_extreme_day_regime_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_514_extreme_day_regime_skew_252d},
    "exdd_515_extreme_day_regime_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_515_extreme_day_regime_kurt_252d},
    "exdd_516_extreme_day_exhaustion_skew_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_516_extreme_day_exhaustion_skew_5d},
    "exdd_517_extreme_day_exhaustion_kurt_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_517_extreme_day_exhaustion_kurt_5d},
    "exdd_518_extreme_day_exhaustion_skew_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_518_extreme_day_exhaustion_skew_21d},
    "exdd_519_extreme_day_exhaustion_kurt_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_519_extreme_day_exhaustion_kurt_21d},
    "exdd_520_extreme_day_exhaustion_skew_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_520_extreme_day_exhaustion_skew_63d},
    "exdd_521_extreme_day_exhaustion_kurt_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_521_extreme_day_exhaustion_kurt_63d},
    "exdd_522_extreme_day_exhaustion_skew_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_522_extreme_day_exhaustion_skew_126d},
    "exdd_523_extreme_day_exhaustion_kurt_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_523_extreme_day_exhaustion_kurt_126d},
    "exdd_524_extreme_day_exhaustion_skew_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_524_extreme_day_exhaustion_skew_252d},
    "exdd_525_extreme_day_exhaustion_kurt_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_525_extreme_day_exhaustion_kurt_252d},
}
