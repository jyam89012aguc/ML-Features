"""
118_drawdown_recovery_asymmetry — Statistical Moments
Domain: drawdown_recovery_asymmetry
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

def dras_376_downside_speed_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_376_downside_speed_skew_5d
    ECONOMIC RATIONALE: Skewness of downside_speed over 5d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(5).skew()

def dras_377_downside_speed_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_377_downside_speed_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of downside_speed over 5d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(5).kurt()

def dras_378_downside_speed_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_378_downside_speed_skew_21d
    ECONOMIC RATIONALE: Skewness of downside_speed over 21d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(21).skew()

def dras_379_downside_speed_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_379_downside_speed_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of downside_speed over 21d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(21).kurt()

def dras_380_downside_speed_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_380_downside_speed_skew_63d
    ECONOMIC RATIONALE: Skewness of downside_speed over 63d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(63).skew()

def dras_381_downside_speed_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_381_downside_speed_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of downside_speed over 63d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(63).kurt()

def dras_382_downside_speed_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_382_downside_speed_skew_126d
    ECONOMIC RATIONALE: Skewness of downside_speed over 126d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(126).skew()

def dras_383_downside_speed_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_383_downside_speed_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of downside_speed over 126d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(126).kurt()

def dras_384_downside_speed_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_384_downside_speed_skew_252d
    ECONOMIC RATIONALE: Skewness of downside_speed over 252d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(252).skew()

def dras_385_downside_speed_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_385_downside_speed_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of downside_speed over 252d. Average speed of price drops.
    """
    return (close.diff(21).clip(upper=0).abs() / 21).rolling(252).kurt()

def dras_386_upside_speed_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_386_upside_speed_skew_5d
    ECONOMIC RATIONALE: Skewness of upside_speed over 5d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(5).skew()

def dras_387_upside_speed_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_387_upside_speed_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of upside_speed over 5d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(5).kurt()

def dras_388_upside_speed_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_388_upside_speed_skew_21d
    ECONOMIC RATIONALE: Skewness of upside_speed over 21d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(21).skew()

def dras_389_upside_speed_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_389_upside_speed_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of upside_speed over 21d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(21).kurt()

def dras_390_upside_speed_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_390_upside_speed_skew_63d
    ECONOMIC RATIONALE: Skewness of upside_speed over 63d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(63).skew()

def dras_391_upside_speed_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_391_upside_speed_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of upside_speed over 63d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(63).kurt()

def dras_392_upside_speed_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_392_upside_speed_skew_126d
    ECONOMIC RATIONALE: Skewness of upside_speed over 126d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(126).skew()

def dras_393_upside_speed_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_393_upside_speed_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of upside_speed over 126d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(126).kurt()

def dras_394_upside_speed_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_394_upside_speed_skew_252d
    ECONOMIC RATIONALE: Skewness of upside_speed over 252d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(252).skew()

def dras_395_upside_speed_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_395_upside_speed_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of upside_speed over 252d. Average speed of price rallies.
    """
    return (close.diff(21).clip(lower=0) / 21).rolling(252).kurt()

def dras_396_recovery_asymmetry_ratio_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_396_recovery_asymmetry_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of recovery_asymmetry_ratio over 5d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(5).skew()

def dras_397_recovery_asymmetry_ratio_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_397_recovery_asymmetry_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of recovery_asymmetry_ratio over 5d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(5).kurt()

def dras_398_recovery_asymmetry_ratio_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_398_recovery_asymmetry_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of recovery_asymmetry_ratio over 21d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(21).skew()

def dras_399_recovery_asymmetry_ratio_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_399_recovery_asymmetry_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of recovery_asymmetry_ratio over 21d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(21).kurt()

def dras_400_recovery_asymmetry_ratio_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_400_recovery_asymmetry_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of recovery_asymmetry_ratio over 63d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(63).skew()

def dras_401_recovery_asymmetry_ratio_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_401_recovery_asymmetry_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of recovery_asymmetry_ratio over 63d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(63).kurt()

def dras_402_recovery_asymmetry_ratio_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_402_recovery_asymmetry_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of recovery_asymmetry_ratio over 126d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(126).skew()

def dras_403_recovery_asymmetry_ratio_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_403_recovery_asymmetry_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of recovery_asymmetry_ratio over 126d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(126).kurt()

def dras_404_recovery_asymmetry_ratio_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_404_recovery_asymmetry_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of recovery_asymmetry_ratio over 252d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(252).skew()

def dras_405_recovery_asymmetry_ratio_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_405_recovery_asymmetry_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of recovery_asymmetry_ratio over 252d. Ratio of recovery speed to drawdown speed.
    """
    return ((close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)).rolling(252).kurt()

def dras_406_drawdown_recovery_lag_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_406_drawdown_recovery_lag_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_lag over 5d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(5).skew()

def dras_407_drawdown_recovery_lag_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_407_drawdown_recovery_lag_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_lag over 5d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(5).kurt()

def dras_408_drawdown_recovery_lag_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_408_drawdown_recovery_lag_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_lag over 21d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(21).skew()

def dras_409_drawdown_recovery_lag_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_409_drawdown_recovery_lag_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_lag over 21d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(21).kurt()

def dras_410_drawdown_recovery_lag_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_410_drawdown_recovery_lag_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_lag over 63d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(63).skew()

def dras_411_drawdown_recovery_lag_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_411_drawdown_recovery_lag_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_lag over 63d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(63).kurt()

def dras_412_drawdown_recovery_lag_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_412_drawdown_recovery_lag_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_lag over 126d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(126).skew()

def dras_413_drawdown_recovery_lag_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_413_drawdown_recovery_lag_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_lag over 126d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(126).kurt()

def dras_414_drawdown_recovery_lag_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_414_drawdown_recovery_lag_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_lag over 252d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(252).skew()

def dras_415_drawdown_recovery_lag_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_415_drawdown_recovery_lag_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_lag over 252d. Time spent in drawdown vs time spent in recovery.
    """
    return ((close.rolling(252).max().shift(1) > close).rolling(252).sum()).rolling(252).kurt()

def dras_416_asymmetry_zscore_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_416_asymmetry_zscore_skew_5d
    ECONOMIC RATIONALE: Skewness of asymmetry_zscore over 5d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(5).skew()

def dras_417_asymmetry_zscore_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_417_asymmetry_zscore_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_zscore over 5d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(5).kurt()

def dras_418_asymmetry_zscore_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_418_asymmetry_zscore_skew_21d
    ECONOMIC RATIONALE: Skewness of asymmetry_zscore over 21d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(21).skew()

def dras_419_asymmetry_zscore_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_419_asymmetry_zscore_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_zscore over 21d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(21).kurt()

def dras_420_asymmetry_zscore_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_420_asymmetry_zscore_skew_63d
    ECONOMIC RATIONALE: Skewness of asymmetry_zscore over 63d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(63).skew()

def dras_421_asymmetry_zscore_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_421_asymmetry_zscore_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_zscore over 63d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(63).kurt()

def dras_422_asymmetry_zscore_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_422_asymmetry_zscore_skew_126d
    ECONOMIC RATIONALE: Skewness of asymmetry_zscore over 126d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(126).skew()

def dras_423_asymmetry_zscore_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_423_asymmetry_zscore_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_zscore over 126d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(126).kurt()

def dras_424_asymmetry_zscore_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_424_asymmetry_zscore_skew_252d
    ECONOMIC RATIONALE: Skewness of asymmetry_zscore over 252d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(252).skew()

def dras_425_asymmetry_zscore_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_425_asymmetry_zscore_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_zscore over 252d. Anomaly in return symmetry.
    """
    return (_zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)).rolling(252).kurt()

def dras_426_drawdown_severity_skew_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_426_drawdown_severity_skew_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_skew over 5d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(5).skew()

def dras_427_drawdown_severity_skew_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_427_drawdown_severity_skew_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_skew over 5d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(5).kurt()

def dras_428_drawdown_severity_skew_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_428_drawdown_severity_skew_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_skew over 21d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(21).skew()

def dras_429_drawdown_severity_skew_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_429_drawdown_severity_skew_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_skew over 21d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(21).kurt()

def dras_430_drawdown_severity_skew_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_430_drawdown_severity_skew_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_skew over 63d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(63).skew()

def dras_431_drawdown_severity_skew_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_431_drawdown_severity_skew_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_skew over 63d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(63).kurt()

def dras_432_drawdown_severity_skew_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_432_drawdown_severity_skew_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_skew over 126d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(126).skew()

def dras_433_drawdown_severity_skew_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_433_drawdown_severity_skew_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_skew over 126d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(126).kurt()

def dras_434_drawdown_severity_skew_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_434_drawdown_severity_skew_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_severity_skew over 252d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(252).skew()

def dras_435_drawdown_severity_skew_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_435_drawdown_severity_skew_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_severity_skew over 252d. Skewness of negative returns only.
    """
    return (close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())).rolling(252).kurt()

def dras_436_recovery_strength_index_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_436_recovery_strength_index_skew_5d
    ECONOMIC RATIONALE: Skewness of recovery_strength_index over 5d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(5).skew()

def dras_437_recovery_strength_index_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_437_recovery_strength_index_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of recovery_strength_index over 5d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(5).kurt()

def dras_438_recovery_strength_index_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_438_recovery_strength_index_skew_21d
    ECONOMIC RATIONALE: Skewness of recovery_strength_index over 21d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(21).skew()

def dras_439_recovery_strength_index_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_439_recovery_strength_index_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of recovery_strength_index over 21d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(21).kurt()

def dras_440_recovery_strength_index_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_440_recovery_strength_index_skew_63d
    ECONOMIC RATIONALE: Skewness of recovery_strength_index over 63d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(63).skew()

def dras_441_recovery_strength_index_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_441_recovery_strength_index_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of recovery_strength_index over 63d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(63).kurt()

def dras_442_recovery_strength_index_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_442_recovery_strength_index_skew_126d
    ECONOMIC RATIONALE: Skewness of recovery_strength_index over 126d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(126).skew()

def dras_443_recovery_strength_index_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_443_recovery_strength_index_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of recovery_strength_index over 126d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(126).kurt()

def dras_444_recovery_strength_index_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_444_recovery_strength_index_skew_252d
    ECONOMIC RATIONALE: Skewness of recovery_strength_index over 252d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(252).skew()

def dras_445_recovery_strength_index_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_445_recovery_strength_index_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of recovery_strength_index over 252d. Recent rally relative to annual range.
    """
    return (close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)).rolling(252).kurt()

def dras_446_asymmetry_momentum_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_446_asymmetry_momentum_skew_5d
    ECONOMIC RATIONALE: Skewness of asymmetry_momentum over 5d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(5).skew()

def dras_447_asymmetry_momentum_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_447_asymmetry_momentum_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_momentum over 5d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(5).kurt()

def dras_448_asymmetry_momentum_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_448_asymmetry_momentum_skew_21d
    ECONOMIC RATIONALE: Skewness of asymmetry_momentum over 21d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(21).skew()

def dras_449_asymmetry_momentum_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_449_asymmetry_momentum_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_momentum over 21d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(21).kurt()

def dras_450_asymmetry_momentum_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_450_asymmetry_momentum_skew_63d
    ECONOMIC RATIONALE: Skewness of asymmetry_momentum over 63d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(63).skew()

def dras_451_asymmetry_momentum_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_451_asymmetry_momentum_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_momentum over 63d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(63).kurt()

def dras_452_asymmetry_momentum_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_452_asymmetry_momentum_skew_126d
    ECONOMIC RATIONALE: Skewness of asymmetry_momentum over 126d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(126).skew()

def dras_453_asymmetry_momentum_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_453_asymmetry_momentum_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_momentum over 126d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(126).kurt()

def dras_454_asymmetry_momentum_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_454_asymmetry_momentum_skew_252d
    ECONOMIC RATIONALE: Skewness of asymmetry_momentum over 252d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(252).skew()

def dras_455_asymmetry_momentum_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_455_asymmetry_momentum_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_momentum over 252d. Change in the recovery/drawdown balance.
    """
    return ((recovery_asymmetry_ratio).diff(21)).rolling(252).kurt()

def dras_456_drawdown_velocity_z_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_456_drawdown_velocity_z_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_velocity_z over 5d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(5).skew()

def dras_457_drawdown_velocity_z_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_457_drawdown_velocity_z_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_velocity_z over 5d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(5).kurt()

def dras_458_drawdown_velocity_z_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_458_drawdown_velocity_z_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_velocity_z over 21d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(21).skew()

def dras_459_drawdown_velocity_z_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_459_drawdown_velocity_z_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_velocity_z over 21d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(21).kurt()

def dras_460_drawdown_velocity_z_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_460_drawdown_velocity_z_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_velocity_z over 63d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(63).skew()

def dras_461_drawdown_velocity_z_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_461_drawdown_velocity_z_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_velocity_z over 63d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(63).kurt()

def dras_462_drawdown_velocity_z_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_462_drawdown_velocity_z_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_velocity_z over 126d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(126).skew()

def dras_463_drawdown_velocity_z_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_463_drawdown_velocity_z_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_velocity_z over 126d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(126).kurt()

def dras_464_drawdown_velocity_z_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_464_drawdown_velocity_z_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_velocity_z over 252d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(252).skew()

def dras_465_drawdown_velocity_z_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_465_drawdown_velocity_z_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_velocity_z over 252d. Severity of recent drop speed.
    """
    return (_zscore_rolling(close.diff(5).clip(upper=0).abs(), 252)).rolling(252).kurt()

def dras_466_recovery_efficiency_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_466_recovery_efficiency_skew_5d
    ECONOMIC RATIONALE: Skewness of recovery_efficiency over 5d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(5).skew()

def dras_467_recovery_efficiency_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_467_recovery_efficiency_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of recovery_efficiency over 5d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(5).kurt()

def dras_468_recovery_efficiency_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_468_recovery_efficiency_skew_21d
    ECONOMIC RATIONALE: Skewness of recovery_efficiency over 21d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(21).skew()

def dras_469_recovery_efficiency_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_469_recovery_efficiency_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of recovery_efficiency over 21d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(21).kurt()

def dras_470_recovery_efficiency_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_470_recovery_efficiency_skew_63d
    ECONOMIC RATIONALE: Skewness of recovery_efficiency over 63d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(63).skew()

def dras_471_recovery_efficiency_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_471_recovery_efficiency_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of recovery_efficiency over 63d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(63).kurt()

def dras_472_recovery_efficiency_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_472_recovery_efficiency_skew_126d
    ECONOMIC RATIONALE: Skewness of recovery_efficiency over 126d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(126).skew()

def dras_473_recovery_efficiency_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_473_recovery_efficiency_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of recovery_efficiency over 126d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(126).kurt()

def dras_474_recovery_efficiency_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_474_recovery_efficiency_skew_252d
    ECONOMIC RATIONALE: Skewness of recovery_efficiency over 252d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(252).skew()

def dras_475_recovery_efficiency_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_475_recovery_efficiency_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of recovery_efficiency over 252d. Upside move normalized by volatility.
    """
    return (close.diff(21).clip(lower=0) / close.rolling(21).std().replace(0, 1e-9)).rolling(252).kurt()

def dras_476_drawdown_efficiency_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_476_drawdown_efficiency_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_efficiency over 5d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(5).skew()

def dras_477_drawdown_efficiency_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_477_drawdown_efficiency_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_efficiency over 5d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(5).kurt()

def dras_478_drawdown_efficiency_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_478_drawdown_efficiency_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_efficiency over 21d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(21).skew()

def dras_479_drawdown_efficiency_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_479_drawdown_efficiency_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_efficiency over 21d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(21).kurt()

def dras_480_drawdown_efficiency_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_480_drawdown_efficiency_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_efficiency over 63d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(63).skew()

def dras_481_drawdown_efficiency_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_481_drawdown_efficiency_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_efficiency over 63d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(63).kurt()

def dras_482_drawdown_efficiency_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_482_drawdown_efficiency_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_efficiency over 126d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(126).skew()

def dras_483_drawdown_efficiency_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_483_drawdown_efficiency_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_efficiency over 126d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(126).kurt()

def dras_484_drawdown_efficiency_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_484_drawdown_efficiency_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_efficiency over 252d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(252).skew()

def dras_485_drawdown_efficiency_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_485_drawdown_efficiency_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_efficiency over 252d. Downside move normalized by volatility.
    """
    return (close.diff(21).clip(upper=0).abs() / close.rolling(21).std().replace(0, 1e-9)).rolling(252).kurt()

def dras_486_asymmetry_regime_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_486_asymmetry_regime_skew_5d
    ECONOMIC RATIONALE: Skewness of asymmetry_regime over 5d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(5).skew()

def dras_487_asymmetry_regime_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_487_asymmetry_regime_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_regime over 5d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(5).kurt()

def dras_488_asymmetry_regime_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_488_asymmetry_regime_skew_21d
    ECONOMIC RATIONALE: Skewness of asymmetry_regime over 21d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(21).skew()

def dras_489_asymmetry_regime_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_489_asymmetry_regime_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_regime over 21d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(21).kurt()

def dras_490_asymmetry_regime_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_490_asymmetry_regime_skew_63d
    ECONOMIC RATIONALE: Skewness of asymmetry_regime over 63d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(63).skew()

def dras_491_asymmetry_regime_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_491_asymmetry_regime_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_regime over 63d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(63).kurt()

def dras_492_asymmetry_regime_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_492_asymmetry_regime_skew_126d
    ECONOMIC RATIONALE: Skewness of asymmetry_regime over 126d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(126).skew()

def dras_493_asymmetry_regime_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_493_asymmetry_regime_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_regime over 126d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(126).kurt()

def dras_494_asymmetry_regime_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_494_asymmetry_regime_skew_252d
    ECONOMIC RATIONALE: Skewness of asymmetry_regime over 252d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(252).skew()

def dras_495_asymmetry_regime_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_495_asymmetry_regime_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of asymmetry_regime over 252d. Deviation from historical asymmetry.
    """
    return (recovery_asymmetry_ratio - recovery_asymmetry_ratio.rolling(252).mean()).rolling(252).kurt()

def dras_496_sequential_drop_count_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_496_sequential_drop_count_skew_5d
    ECONOMIC RATIONALE: Skewness of sequential_drop_count over 5d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(5).skew()

def dras_497_sequential_drop_count_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_497_sequential_drop_count_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of sequential_drop_count over 5d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(5).kurt()

def dras_498_sequential_drop_count_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_498_sequential_drop_count_skew_21d
    ECONOMIC RATIONALE: Skewness of sequential_drop_count over 21d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(21).skew()

def dras_499_sequential_drop_count_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_499_sequential_drop_count_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of sequential_drop_count over 21d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(21).kurt()

def dras_500_sequential_drop_count_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_500_sequential_drop_count_skew_63d
    ECONOMIC RATIONALE: Skewness of sequential_drop_count over 63d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(63).skew()

def dras_501_sequential_drop_count_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_501_sequential_drop_count_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of sequential_drop_count over 63d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(63).kurt()

def dras_502_sequential_drop_count_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_502_sequential_drop_count_skew_126d
    ECONOMIC RATIONALE: Skewness of sequential_drop_count over 126d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(126).skew()

def dras_503_sequential_drop_count_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_503_sequential_drop_count_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of sequential_drop_count over 126d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(126).kurt()

def dras_504_sequential_drop_count_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_504_sequential_drop_count_skew_252d
    ECONOMIC RATIONALE: Skewness of sequential_drop_count over 252d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(252).skew()

def dras_505_sequential_drop_count_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_505_sequential_drop_count_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of sequential_drop_count over 252d. Number of consecutive down days.
    """
    return ((close.diff(1) < 0).rolling(10).sum()).rolling(252).kurt()

def dras_506_sequential_rally_count_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_506_sequential_rally_count_skew_5d
    ECONOMIC RATIONALE: Skewness of sequential_rally_count over 5d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(5).skew()

def dras_507_sequential_rally_count_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_507_sequential_rally_count_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of sequential_rally_count over 5d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(5).kurt()

def dras_508_sequential_rally_count_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_508_sequential_rally_count_skew_21d
    ECONOMIC RATIONALE: Skewness of sequential_rally_count over 21d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(21).skew()

def dras_509_sequential_rally_count_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_509_sequential_rally_count_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of sequential_rally_count over 21d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(21).kurt()

def dras_510_sequential_rally_count_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_510_sequential_rally_count_skew_63d
    ECONOMIC RATIONALE: Skewness of sequential_rally_count over 63d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(63).skew()

def dras_511_sequential_rally_count_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_511_sequential_rally_count_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of sequential_rally_count over 63d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(63).kurt()

def dras_512_sequential_rally_count_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_512_sequential_rally_count_skew_126d
    ECONOMIC RATIONALE: Skewness of sequential_rally_count over 126d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(126).skew()

def dras_513_sequential_rally_count_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_513_sequential_rally_count_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of sequential_rally_count over 126d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(126).kurt()

def dras_514_sequential_rally_count_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_514_sequential_rally_count_skew_252d
    ECONOMIC RATIONALE: Skewness of sequential_rally_count over 252d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(252).skew()

def dras_515_sequential_rally_count_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_515_sequential_rally_count_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of sequential_rally_count over 252d. Number of consecutive up days.
    """
    return ((close.diff(1) > 0).rolling(10).sum()).rolling(252).kurt()

def dras_516_drawdown_recovery_gap_skew_5d(close: pd.Series) -> pd.Series:
    """
    dras_516_drawdown_recovery_gap_skew_5d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_gap over 5d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(5).skew()

def dras_517_drawdown_recovery_gap_kurt_5d(close: pd.Series) -> pd.Series:
    """
    dras_517_drawdown_recovery_gap_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_gap over 5d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(5).kurt()

def dras_518_drawdown_recovery_gap_skew_21d(close: pd.Series) -> pd.Series:
    """
    dras_518_drawdown_recovery_gap_skew_21d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_gap over 21d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(21).skew()

def dras_519_drawdown_recovery_gap_kurt_21d(close: pd.Series) -> pd.Series:
    """
    dras_519_drawdown_recovery_gap_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_gap over 21d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(21).kurt()

def dras_520_drawdown_recovery_gap_skew_63d(close: pd.Series) -> pd.Series:
    """
    dras_520_drawdown_recovery_gap_skew_63d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_gap over 63d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(63).skew()

def dras_521_drawdown_recovery_gap_kurt_63d(close: pd.Series) -> pd.Series:
    """
    dras_521_drawdown_recovery_gap_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_gap over 63d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(63).kurt()

def dras_522_drawdown_recovery_gap_skew_126d(close: pd.Series) -> pd.Series:
    """
    dras_522_drawdown_recovery_gap_skew_126d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_gap over 126d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(126).skew()

def dras_523_drawdown_recovery_gap_kurt_126d(close: pd.Series) -> pd.Series:
    """
    dras_523_drawdown_recovery_gap_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_gap over 126d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(126).kurt()

def dras_524_drawdown_recovery_gap_skew_252d(close: pd.Series) -> pd.Series:
    """
    dras_524_drawdown_recovery_gap_skew_252d
    ECONOMIC RATIONALE: Skewness of drawdown_recovery_gap over 252d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(252).skew()

def dras_525_drawdown_recovery_gap_kurt_252d(close: pd.Series) -> pd.Series:
    """
    dras_525_drawdown_recovery_gap_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of drawdown_recovery_gap over 252d. Distance from peak vs distance from trough.
    """
    return ((close.rolling(252).max() - close) - (close - close.rolling(252).min())).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V118_REGISTRY_MOMENTS = {
    "dras_376_downside_speed_skew_5d": {"inputs": ["close"], "func": dras_376_downside_speed_skew_5d},
    "dras_377_downside_speed_kurt_5d": {"inputs": ["close"], "func": dras_377_downside_speed_kurt_5d},
    "dras_378_downside_speed_skew_21d": {"inputs": ["close"], "func": dras_378_downside_speed_skew_21d},
    "dras_379_downside_speed_kurt_21d": {"inputs": ["close"], "func": dras_379_downside_speed_kurt_21d},
    "dras_380_downside_speed_skew_63d": {"inputs": ["close"], "func": dras_380_downside_speed_skew_63d},
    "dras_381_downside_speed_kurt_63d": {"inputs": ["close"], "func": dras_381_downside_speed_kurt_63d},
    "dras_382_downside_speed_skew_126d": {"inputs": ["close"], "func": dras_382_downside_speed_skew_126d},
    "dras_383_downside_speed_kurt_126d": {"inputs": ["close"], "func": dras_383_downside_speed_kurt_126d},
    "dras_384_downside_speed_skew_252d": {"inputs": ["close"], "func": dras_384_downside_speed_skew_252d},
    "dras_385_downside_speed_kurt_252d": {"inputs": ["close"], "func": dras_385_downside_speed_kurt_252d},
    "dras_386_upside_speed_skew_5d": {"inputs": ["close"], "func": dras_386_upside_speed_skew_5d},
    "dras_387_upside_speed_kurt_5d": {"inputs": ["close"], "func": dras_387_upside_speed_kurt_5d},
    "dras_388_upside_speed_skew_21d": {"inputs": ["close"], "func": dras_388_upside_speed_skew_21d},
    "dras_389_upside_speed_kurt_21d": {"inputs": ["close"], "func": dras_389_upside_speed_kurt_21d},
    "dras_390_upside_speed_skew_63d": {"inputs": ["close"], "func": dras_390_upside_speed_skew_63d},
    "dras_391_upside_speed_kurt_63d": {"inputs": ["close"], "func": dras_391_upside_speed_kurt_63d},
    "dras_392_upside_speed_skew_126d": {"inputs": ["close"], "func": dras_392_upside_speed_skew_126d},
    "dras_393_upside_speed_kurt_126d": {"inputs": ["close"], "func": dras_393_upside_speed_kurt_126d},
    "dras_394_upside_speed_skew_252d": {"inputs": ["close"], "func": dras_394_upside_speed_skew_252d},
    "dras_395_upside_speed_kurt_252d": {"inputs": ["close"], "func": dras_395_upside_speed_kurt_252d},
    "dras_396_recovery_asymmetry_ratio_skew_5d": {"inputs": ["close"], "func": dras_396_recovery_asymmetry_ratio_skew_5d},
    "dras_397_recovery_asymmetry_ratio_kurt_5d": {"inputs": ["close"], "func": dras_397_recovery_asymmetry_ratio_kurt_5d},
    "dras_398_recovery_asymmetry_ratio_skew_21d": {"inputs": ["close"], "func": dras_398_recovery_asymmetry_ratio_skew_21d},
    "dras_399_recovery_asymmetry_ratio_kurt_21d": {"inputs": ["close"], "func": dras_399_recovery_asymmetry_ratio_kurt_21d},
    "dras_400_recovery_asymmetry_ratio_skew_63d": {"inputs": ["close"], "func": dras_400_recovery_asymmetry_ratio_skew_63d},
    "dras_401_recovery_asymmetry_ratio_kurt_63d": {"inputs": ["close"], "func": dras_401_recovery_asymmetry_ratio_kurt_63d},
    "dras_402_recovery_asymmetry_ratio_skew_126d": {"inputs": ["close"], "func": dras_402_recovery_asymmetry_ratio_skew_126d},
    "dras_403_recovery_asymmetry_ratio_kurt_126d": {"inputs": ["close"], "func": dras_403_recovery_asymmetry_ratio_kurt_126d},
    "dras_404_recovery_asymmetry_ratio_skew_252d": {"inputs": ["close"], "func": dras_404_recovery_asymmetry_ratio_skew_252d},
    "dras_405_recovery_asymmetry_ratio_kurt_252d": {"inputs": ["close"], "func": dras_405_recovery_asymmetry_ratio_kurt_252d},
    "dras_406_drawdown_recovery_lag_skew_5d": {"inputs": ["close"], "func": dras_406_drawdown_recovery_lag_skew_5d},
    "dras_407_drawdown_recovery_lag_kurt_5d": {"inputs": ["close"], "func": dras_407_drawdown_recovery_lag_kurt_5d},
    "dras_408_drawdown_recovery_lag_skew_21d": {"inputs": ["close"], "func": dras_408_drawdown_recovery_lag_skew_21d},
    "dras_409_drawdown_recovery_lag_kurt_21d": {"inputs": ["close"], "func": dras_409_drawdown_recovery_lag_kurt_21d},
    "dras_410_drawdown_recovery_lag_skew_63d": {"inputs": ["close"], "func": dras_410_drawdown_recovery_lag_skew_63d},
    "dras_411_drawdown_recovery_lag_kurt_63d": {"inputs": ["close"], "func": dras_411_drawdown_recovery_lag_kurt_63d},
    "dras_412_drawdown_recovery_lag_skew_126d": {"inputs": ["close"], "func": dras_412_drawdown_recovery_lag_skew_126d},
    "dras_413_drawdown_recovery_lag_kurt_126d": {"inputs": ["close"], "func": dras_413_drawdown_recovery_lag_kurt_126d},
    "dras_414_drawdown_recovery_lag_skew_252d": {"inputs": ["close"], "func": dras_414_drawdown_recovery_lag_skew_252d},
    "dras_415_drawdown_recovery_lag_kurt_252d": {"inputs": ["close"], "func": dras_415_drawdown_recovery_lag_kurt_252d},
    "dras_416_asymmetry_zscore_skew_5d": {"inputs": ["close"], "func": dras_416_asymmetry_zscore_skew_5d},
    "dras_417_asymmetry_zscore_kurt_5d": {"inputs": ["close"], "func": dras_417_asymmetry_zscore_kurt_5d},
    "dras_418_asymmetry_zscore_skew_21d": {"inputs": ["close"], "func": dras_418_asymmetry_zscore_skew_21d},
    "dras_419_asymmetry_zscore_kurt_21d": {"inputs": ["close"], "func": dras_419_asymmetry_zscore_kurt_21d},
    "dras_420_asymmetry_zscore_skew_63d": {"inputs": ["close"], "func": dras_420_asymmetry_zscore_skew_63d},
    "dras_421_asymmetry_zscore_kurt_63d": {"inputs": ["close"], "func": dras_421_asymmetry_zscore_kurt_63d},
    "dras_422_asymmetry_zscore_skew_126d": {"inputs": ["close"], "func": dras_422_asymmetry_zscore_skew_126d},
    "dras_423_asymmetry_zscore_kurt_126d": {"inputs": ["close"], "func": dras_423_asymmetry_zscore_kurt_126d},
    "dras_424_asymmetry_zscore_skew_252d": {"inputs": ["close"], "func": dras_424_asymmetry_zscore_skew_252d},
    "dras_425_asymmetry_zscore_kurt_252d": {"inputs": ["close"], "func": dras_425_asymmetry_zscore_kurt_252d},
    "dras_426_drawdown_severity_skew_skew_5d": {"inputs": ["close"], "func": dras_426_drawdown_severity_skew_skew_5d},
    "dras_427_drawdown_severity_skew_kurt_5d": {"inputs": ["close"], "func": dras_427_drawdown_severity_skew_kurt_5d},
    "dras_428_drawdown_severity_skew_skew_21d": {"inputs": ["close"], "func": dras_428_drawdown_severity_skew_skew_21d},
    "dras_429_drawdown_severity_skew_kurt_21d": {"inputs": ["close"], "func": dras_429_drawdown_severity_skew_kurt_21d},
    "dras_430_drawdown_severity_skew_skew_63d": {"inputs": ["close"], "func": dras_430_drawdown_severity_skew_skew_63d},
    "dras_431_drawdown_severity_skew_kurt_63d": {"inputs": ["close"], "func": dras_431_drawdown_severity_skew_kurt_63d},
    "dras_432_drawdown_severity_skew_skew_126d": {"inputs": ["close"], "func": dras_432_drawdown_severity_skew_skew_126d},
    "dras_433_drawdown_severity_skew_kurt_126d": {"inputs": ["close"], "func": dras_433_drawdown_severity_skew_kurt_126d},
    "dras_434_drawdown_severity_skew_skew_252d": {"inputs": ["close"], "func": dras_434_drawdown_severity_skew_skew_252d},
    "dras_435_drawdown_severity_skew_kurt_252d": {"inputs": ["close"], "func": dras_435_drawdown_severity_skew_kurt_252d},
    "dras_436_recovery_strength_index_skew_5d": {"inputs": ["close"], "func": dras_436_recovery_strength_index_skew_5d},
    "dras_437_recovery_strength_index_kurt_5d": {"inputs": ["close"], "func": dras_437_recovery_strength_index_kurt_5d},
    "dras_438_recovery_strength_index_skew_21d": {"inputs": ["close"], "func": dras_438_recovery_strength_index_skew_21d},
    "dras_439_recovery_strength_index_kurt_21d": {"inputs": ["close"], "func": dras_439_recovery_strength_index_kurt_21d},
    "dras_440_recovery_strength_index_skew_63d": {"inputs": ["close"], "func": dras_440_recovery_strength_index_skew_63d},
    "dras_441_recovery_strength_index_kurt_63d": {"inputs": ["close"], "func": dras_441_recovery_strength_index_kurt_63d},
    "dras_442_recovery_strength_index_skew_126d": {"inputs": ["close"], "func": dras_442_recovery_strength_index_skew_126d},
    "dras_443_recovery_strength_index_kurt_126d": {"inputs": ["close"], "func": dras_443_recovery_strength_index_kurt_126d},
    "dras_444_recovery_strength_index_skew_252d": {"inputs": ["close"], "func": dras_444_recovery_strength_index_skew_252d},
    "dras_445_recovery_strength_index_kurt_252d": {"inputs": ["close"], "func": dras_445_recovery_strength_index_kurt_252d},
    "dras_446_asymmetry_momentum_skew_5d": {"inputs": ["close"], "func": dras_446_asymmetry_momentum_skew_5d},
    "dras_447_asymmetry_momentum_kurt_5d": {"inputs": ["close"], "func": dras_447_asymmetry_momentum_kurt_5d},
    "dras_448_asymmetry_momentum_skew_21d": {"inputs": ["close"], "func": dras_448_asymmetry_momentum_skew_21d},
    "dras_449_asymmetry_momentum_kurt_21d": {"inputs": ["close"], "func": dras_449_asymmetry_momentum_kurt_21d},
    "dras_450_asymmetry_momentum_skew_63d": {"inputs": ["close"], "func": dras_450_asymmetry_momentum_skew_63d},
    "dras_451_asymmetry_momentum_kurt_63d": {"inputs": ["close"], "func": dras_451_asymmetry_momentum_kurt_63d},
    "dras_452_asymmetry_momentum_skew_126d": {"inputs": ["close"], "func": dras_452_asymmetry_momentum_skew_126d},
    "dras_453_asymmetry_momentum_kurt_126d": {"inputs": ["close"], "func": dras_453_asymmetry_momentum_kurt_126d},
    "dras_454_asymmetry_momentum_skew_252d": {"inputs": ["close"], "func": dras_454_asymmetry_momentum_skew_252d},
    "dras_455_asymmetry_momentum_kurt_252d": {"inputs": ["close"], "func": dras_455_asymmetry_momentum_kurt_252d},
    "dras_456_drawdown_velocity_z_skew_5d": {"inputs": ["close"], "func": dras_456_drawdown_velocity_z_skew_5d},
    "dras_457_drawdown_velocity_z_kurt_5d": {"inputs": ["close"], "func": dras_457_drawdown_velocity_z_kurt_5d},
    "dras_458_drawdown_velocity_z_skew_21d": {"inputs": ["close"], "func": dras_458_drawdown_velocity_z_skew_21d},
    "dras_459_drawdown_velocity_z_kurt_21d": {"inputs": ["close"], "func": dras_459_drawdown_velocity_z_kurt_21d},
    "dras_460_drawdown_velocity_z_skew_63d": {"inputs": ["close"], "func": dras_460_drawdown_velocity_z_skew_63d},
    "dras_461_drawdown_velocity_z_kurt_63d": {"inputs": ["close"], "func": dras_461_drawdown_velocity_z_kurt_63d},
    "dras_462_drawdown_velocity_z_skew_126d": {"inputs": ["close"], "func": dras_462_drawdown_velocity_z_skew_126d},
    "dras_463_drawdown_velocity_z_kurt_126d": {"inputs": ["close"], "func": dras_463_drawdown_velocity_z_kurt_126d},
    "dras_464_drawdown_velocity_z_skew_252d": {"inputs": ["close"], "func": dras_464_drawdown_velocity_z_skew_252d},
    "dras_465_drawdown_velocity_z_kurt_252d": {"inputs": ["close"], "func": dras_465_drawdown_velocity_z_kurt_252d},
    "dras_466_recovery_efficiency_skew_5d": {"inputs": ["close"], "func": dras_466_recovery_efficiency_skew_5d},
    "dras_467_recovery_efficiency_kurt_5d": {"inputs": ["close"], "func": dras_467_recovery_efficiency_kurt_5d},
    "dras_468_recovery_efficiency_skew_21d": {"inputs": ["close"], "func": dras_468_recovery_efficiency_skew_21d},
    "dras_469_recovery_efficiency_kurt_21d": {"inputs": ["close"], "func": dras_469_recovery_efficiency_kurt_21d},
    "dras_470_recovery_efficiency_skew_63d": {"inputs": ["close"], "func": dras_470_recovery_efficiency_skew_63d},
    "dras_471_recovery_efficiency_kurt_63d": {"inputs": ["close"], "func": dras_471_recovery_efficiency_kurt_63d},
    "dras_472_recovery_efficiency_skew_126d": {"inputs": ["close"], "func": dras_472_recovery_efficiency_skew_126d},
    "dras_473_recovery_efficiency_kurt_126d": {"inputs": ["close"], "func": dras_473_recovery_efficiency_kurt_126d},
    "dras_474_recovery_efficiency_skew_252d": {"inputs": ["close"], "func": dras_474_recovery_efficiency_skew_252d},
    "dras_475_recovery_efficiency_kurt_252d": {"inputs": ["close"], "func": dras_475_recovery_efficiency_kurt_252d},
    "dras_476_drawdown_efficiency_skew_5d": {"inputs": ["close"], "func": dras_476_drawdown_efficiency_skew_5d},
    "dras_477_drawdown_efficiency_kurt_5d": {"inputs": ["close"], "func": dras_477_drawdown_efficiency_kurt_5d},
    "dras_478_drawdown_efficiency_skew_21d": {"inputs": ["close"], "func": dras_478_drawdown_efficiency_skew_21d},
    "dras_479_drawdown_efficiency_kurt_21d": {"inputs": ["close"], "func": dras_479_drawdown_efficiency_kurt_21d},
    "dras_480_drawdown_efficiency_skew_63d": {"inputs": ["close"], "func": dras_480_drawdown_efficiency_skew_63d},
    "dras_481_drawdown_efficiency_kurt_63d": {"inputs": ["close"], "func": dras_481_drawdown_efficiency_kurt_63d},
    "dras_482_drawdown_efficiency_skew_126d": {"inputs": ["close"], "func": dras_482_drawdown_efficiency_skew_126d},
    "dras_483_drawdown_efficiency_kurt_126d": {"inputs": ["close"], "func": dras_483_drawdown_efficiency_kurt_126d},
    "dras_484_drawdown_efficiency_skew_252d": {"inputs": ["close"], "func": dras_484_drawdown_efficiency_skew_252d},
    "dras_485_drawdown_efficiency_kurt_252d": {"inputs": ["close"], "func": dras_485_drawdown_efficiency_kurt_252d},
    "dras_486_asymmetry_regime_skew_5d": {"inputs": ["close"], "func": dras_486_asymmetry_regime_skew_5d},
    "dras_487_asymmetry_regime_kurt_5d": {"inputs": ["close"], "func": dras_487_asymmetry_regime_kurt_5d},
    "dras_488_asymmetry_regime_skew_21d": {"inputs": ["close"], "func": dras_488_asymmetry_regime_skew_21d},
    "dras_489_asymmetry_regime_kurt_21d": {"inputs": ["close"], "func": dras_489_asymmetry_regime_kurt_21d},
    "dras_490_asymmetry_regime_skew_63d": {"inputs": ["close"], "func": dras_490_asymmetry_regime_skew_63d},
    "dras_491_asymmetry_regime_kurt_63d": {"inputs": ["close"], "func": dras_491_asymmetry_regime_kurt_63d},
    "dras_492_asymmetry_regime_skew_126d": {"inputs": ["close"], "func": dras_492_asymmetry_regime_skew_126d},
    "dras_493_asymmetry_regime_kurt_126d": {"inputs": ["close"], "func": dras_493_asymmetry_regime_kurt_126d},
    "dras_494_asymmetry_regime_skew_252d": {"inputs": ["close"], "func": dras_494_asymmetry_regime_skew_252d},
    "dras_495_asymmetry_regime_kurt_252d": {"inputs": ["close"], "func": dras_495_asymmetry_regime_kurt_252d},
    "dras_496_sequential_drop_count_skew_5d": {"inputs": ["close"], "func": dras_496_sequential_drop_count_skew_5d},
    "dras_497_sequential_drop_count_kurt_5d": {"inputs": ["close"], "func": dras_497_sequential_drop_count_kurt_5d},
    "dras_498_sequential_drop_count_skew_21d": {"inputs": ["close"], "func": dras_498_sequential_drop_count_skew_21d},
    "dras_499_sequential_drop_count_kurt_21d": {"inputs": ["close"], "func": dras_499_sequential_drop_count_kurt_21d},
    "dras_500_sequential_drop_count_skew_63d": {"inputs": ["close"], "func": dras_500_sequential_drop_count_skew_63d},
    "dras_501_sequential_drop_count_kurt_63d": {"inputs": ["close"], "func": dras_501_sequential_drop_count_kurt_63d},
    "dras_502_sequential_drop_count_skew_126d": {"inputs": ["close"], "func": dras_502_sequential_drop_count_skew_126d},
    "dras_503_sequential_drop_count_kurt_126d": {"inputs": ["close"], "func": dras_503_sequential_drop_count_kurt_126d},
    "dras_504_sequential_drop_count_skew_252d": {"inputs": ["close"], "func": dras_504_sequential_drop_count_skew_252d},
    "dras_505_sequential_drop_count_kurt_252d": {"inputs": ["close"], "func": dras_505_sequential_drop_count_kurt_252d},
    "dras_506_sequential_rally_count_skew_5d": {"inputs": ["close"], "func": dras_506_sequential_rally_count_skew_5d},
    "dras_507_sequential_rally_count_kurt_5d": {"inputs": ["close"], "func": dras_507_sequential_rally_count_kurt_5d},
    "dras_508_sequential_rally_count_skew_21d": {"inputs": ["close"], "func": dras_508_sequential_rally_count_skew_21d},
    "dras_509_sequential_rally_count_kurt_21d": {"inputs": ["close"], "func": dras_509_sequential_rally_count_kurt_21d},
    "dras_510_sequential_rally_count_skew_63d": {"inputs": ["close"], "func": dras_510_sequential_rally_count_skew_63d},
    "dras_511_sequential_rally_count_kurt_63d": {"inputs": ["close"], "func": dras_511_sequential_rally_count_kurt_63d},
    "dras_512_sequential_rally_count_skew_126d": {"inputs": ["close"], "func": dras_512_sequential_rally_count_skew_126d},
    "dras_513_sequential_rally_count_kurt_126d": {"inputs": ["close"], "func": dras_513_sequential_rally_count_kurt_126d},
    "dras_514_sequential_rally_count_skew_252d": {"inputs": ["close"], "func": dras_514_sequential_rally_count_skew_252d},
    "dras_515_sequential_rally_count_kurt_252d": {"inputs": ["close"], "func": dras_515_sequential_rally_count_kurt_252d},
    "dras_516_drawdown_recovery_gap_skew_5d": {"inputs": ["close"], "func": dras_516_drawdown_recovery_gap_skew_5d},
    "dras_517_drawdown_recovery_gap_kurt_5d": {"inputs": ["close"], "func": dras_517_drawdown_recovery_gap_kurt_5d},
    "dras_518_drawdown_recovery_gap_skew_21d": {"inputs": ["close"], "func": dras_518_drawdown_recovery_gap_skew_21d},
    "dras_519_drawdown_recovery_gap_kurt_21d": {"inputs": ["close"], "func": dras_519_drawdown_recovery_gap_kurt_21d},
    "dras_520_drawdown_recovery_gap_skew_63d": {"inputs": ["close"], "func": dras_520_drawdown_recovery_gap_skew_63d},
    "dras_521_drawdown_recovery_gap_kurt_63d": {"inputs": ["close"], "func": dras_521_drawdown_recovery_gap_kurt_63d},
    "dras_522_drawdown_recovery_gap_skew_126d": {"inputs": ["close"], "func": dras_522_drawdown_recovery_gap_skew_126d},
    "dras_523_drawdown_recovery_gap_kurt_126d": {"inputs": ["close"], "func": dras_523_drawdown_recovery_gap_kurt_126d},
    "dras_524_drawdown_recovery_gap_skew_252d": {"inputs": ["close"], "func": dras_524_drawdown_recovery_gap_skew_252d},
    "dras_525_drawdown_recovery_gap_kurt_252d": {"inputs": ["close"], "func": dras_525_drawdown_recovery_gap_kurt_252d},
}
