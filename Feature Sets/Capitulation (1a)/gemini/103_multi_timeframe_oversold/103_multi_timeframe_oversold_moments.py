"""
103_multi_timeframe_oversold — Statistical Moments
Domain: multi_timeframe_oversold
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

def mtfo_376_daily_rsi_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_376_daily_rsi_skew_5d
    ECONOMIC RATIONALE: Skewness of daily_rsi over 5d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).skew()

def mtfo_377_daily_rsi_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_377_daily_rsi_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of daily_rsi over 5d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).kurt()

def mtfo_378_daily_rsi_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_378_daily_rsi_skew_21d
    ECONOMIC RATIONALE: Skewness of daily_rsi over 21d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).skew()

def mtfo_379_daily_rsi_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_379_daily_rsi_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of daily_rsi over 21d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).kurt()

def mtfo_380_daily_rsi_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_380_daily_rsi_skew_63d
    ECONOMIC RATIONALE: Skewness of daily_rsi over 63d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).skew()

def mtfo_381_daily_rsi_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_381_daily_rsi_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of daily_rsi over 63d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).kurt()

def mtfo_382_daily_rsi_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_382_daily_rsi_skew_126d
    ECONOMIC RATIONALE: Skewness of daily_rsi over 126d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).skew()

def mtfo_383_daily_rsi_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_383_daily_rsi_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of daily_rsi over 126d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).kurt()

def mtfo_384_daily_rsi_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_384_daily_rsi_skew_252d
    ECONOMIC RATIONALE: Skewness of daily_rsi over 252d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).skew()

def mtfo_385_daily_rsi_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_385_daily_rsi_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of daily_rsi over 252d. 14-day Relative Strength Index.
    """
    return (100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).kurt()

def mtfo_386_weekly_rsi_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_386_weekly_rsi_skew_5d
    ECONOMIC RATIONALE: Skewness of weekly_rsi over 5d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).skew()

def mtfo_387_weekly_rsi_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_387_weekly_rsi_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of weekly_rsi over 5d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).kurt()

def mtfo_388_weekly_rsi_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_388_weekly_rsi_skew_21d
    ECONOMIC RATIONALE: Skewness of weekly_rsi over 21d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).skew()

def mtfo_389_weekly_rsi_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_389_weekly_rsi_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of weekly_rsi over 21d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).kurt()

def mtfo_390_weekly_rsi_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_390_weekly_rsi_skew_63d
    ECONOMIC RATIONALE: Skewness of weekly_rsi over 63d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).skew()

def mtfo_391_weekly_rsi_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_391_weekly_rsi_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of weekly_rsi over 63d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).kurt()

def mtfo_392_weekly_rsi_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_392_weekly_rsi_skew_126d
    ECONOMIC RATIONALE: Skewness of weekly_rsi over 126d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).skew()

def mtfo_393_weekly_rsi_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_393_weekly_rsi_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of weekly_rsi over 126d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).kurt()

def mtfo_394_weekly_rsi_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_394_weekly_rsi_skew_252d
    ECONOMIC RATIONALE: Skewness of weekly_rsi over 252d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).skew()

def mtfo_395_weekly_rsi_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_395_weekly_rsi_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of weekly_rsi over 252d. Weekly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).kurt()

def mtfo_396_monthly_rsi_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_396_monthly_rsi_skew_5d
    ECONOMIC RATIONALE: Skewness of monthly_rsi over 5d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).skew()

def mtfo_397_monthly_rsi_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_397_monthly_rsi_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of monthly_rsi over 5d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).kurt()

def mtfo_398_monthly_rsi_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_398_monthly_rsi_skew_21d
    ECONOMIC RATIONALE: Skewness of monthly_rsi over 21d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).skew()

def mtfo_399_monthly_rsi_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_399_monthly_rsi_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of monthly_rsi over 21d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).kurt()

def mtfo_400_monthly_rsi_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_400_monthly_rsi_skew_63d
    ECONOMIC RATIONALE: Skewness of monthly_rsi over 63d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).skew()

def mtfo_401_monthly_rsi_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_401_monthly_rsi_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of monthly_rsi over 63d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).kurt()

def mtfo_402_monthly_rsi_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_402_monthly_rsi_skew_126d
    ECONOMIC RATIONALE: Skewness of monthly_rsi over 126d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).skew()

def mtfo_403_monthly_rsi_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_403_monthly_rsi_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of monthly_rsi over 126d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).kurt()

def mtfo_404_monthly_rsi_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_404_monthly_rsi_skew_252d
    ECONOMIC RATIONALE: Skewness of monthly_rsi over 252d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).skew()

def mtfo_405_monthly_rsi_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_405_monthly_rsi_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of monthly_rsi over 252d. Monthly-equivalent RSI.
    """
    return (100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).kurt()

def mtfo_406_stoch_k_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_406_stoch_k_skew_5d
    ECONOMIC RATIONALE: Skewness of stoch_k over 5d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(5).skew()

def mtfo_407_stoch_k_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_407_stoch_k_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of stoch_k over 5d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(5).kurt()

def mtfo_408_stoch_k_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_408_stoch_k_skew_21d
    ECONOMIC RATIONALE: Skewness of stoch_k over 21d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(21).skew()

def mtfo_409_stoch_k_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_409_stoch_k_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of stoch_k over 21d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(21).kurt()

def mtfo_410_stoch_k_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_410_stoch_k_skew_63d
    ECONOMIC RATIONALE: Skewness of stoch_k over 63d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(63).skew()

def mtfo_411_stoch_k_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_411_stoch_k_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of stoch_k over 63d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(63).kurt()

def mtfo_412_stoch_k_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_412_stoch_k_skew_126d
    ECONOMIC RATIONALE: Skewness of stoch_k over 126d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(126).skew()

def mtfo_413_stoch_k_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_413_stoch_k_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of stoch_k over 126d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(126).kurt()

def mtfo_414_stoch_k_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_414_stoch_k_skew_252d
    ECONOMIC RATIONALE: Skewness of stoch_k over 252d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(252).skew()

def mtfo_415_stoch_k_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_415_stoch_k_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of stoch_k over 252d. Fast Stochastic %K.
    """
    return (100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)).rolling(252).kurt()

def mtfo_416_stoch_d_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_416_stoch_d_skew_5d
    ECONOMIC RATIONALE: Skewness of stoch_d over 5d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(5).skew()

def mtfo_417_stoch_d_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_417_stoch_d_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of stoch_d over 5d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(5).kurt()

def mtfo_418_stoch_d_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_418_stoch_d_skew_21d
    ECONOMIC RATIONALE: Skewness of stoch_d over 21d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(21).skew()

def mtfo_419_stoch_d_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_419_stoch_d_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of stoch_d over 21d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(21).kurt()

def mtfo_420_stoch_d_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_420_stoch_d_skew_63d
    ECONOMIC RATIONALE: Skewness of stoch_d over 63d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(63).skew()

def mtfo_421_stoch_d_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_421_stoch_d_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of stoch_d over 63d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(63).kurt()

def mtfo_422_stoch_d_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_422_stoch_d_skew_126d
    ECONOMIC RATIONALE: Skewness of stoch_d over 126d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(126).skew()

def mtfo_423_stoch_d_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_423_stoch_d_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of stoch_d over 126d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(126).kurt()

def mtfo_424_stoch_d_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_424_stoch_d_skew_252d
    ECONOMIC RATIONALE: Skewness of stoch_d over 252d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(252).skew()

def mtfo_425_stoch_d_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_425_stoch_d_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of stoch_d over 252d. Slow Stochastic %D.
    """
    return (100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)).rolling(252).kurt()

def mtfo_426_multi_tf_oversold_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_426_multi_tf_oversold_skew_5d
    ECONOMIC RATIONALE: Skewness of multi_tf_oversold over 5d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(5).skew()

def mtfo_427_multi_tf_oversold_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_427_multi_tf_oversold_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of multi_tf_oversold over 5d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(5).kurt()

def mtfo_428_multi_tf_oversold_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_428_multi_tf_oversold_skew_21d
    ECONOMIC RATIONALE: Skewness of multi_tf_oversold over 21d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(21).skew()

def mtfo_429_multi_tf_oversold_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_429_multi_tf_oversold_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of multi_tf_oversold over 21d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(21).kurt()

def mtfo_430_multi_tf_oversold_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_430_multi_tf_oversold_skew_63d
    ECONOMIC RATIONALE: Skewness of multi_tf_oversold over 63d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(63).skew()

def mtfo_431_multi_tf_oversold_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_431_multi_tf_oversold_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of multi_tf_oversold over 63d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(63).kurt()

def mtfo_432_multi_tf_oversold_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_432_multi_tf_oversold_skew_126d
    ECONOMIC RATIONALE: Skewness of multi_tf_oversold over 126d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(126).skew()

def mtfo_433_multi_tf_oversold_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_433_multi_tf_oversold_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of multi_tf_oversold over 126d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(126).kurt()

def mtfo_434_multi_tf_oversold_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_434_multi_tf_oversold_skew_252d
    ECONOMIC RATIONALE: Skewness of multi_tf_oversold over 252d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(252).skew()

def mtfo_435_multi_tf_oversold_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_435_multi_tf_oversold_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of multi_tf_oversold over 252d. Convergence of oversold signals across timeframes.
    """
    return (((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)).rolling(252).kurt()

def mtfo_436_rsi_divergence_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_436_rsi_divergence_skew_5d
    ECONOMIC RATIONALE: Skewness of rsi_divergence over 5d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(5).skew()

def mtfo_437_rsi_divergence_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_437_rsi_divergence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of rsi_divergence over 5d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(5).kurt()

def mtfo_438_rsi_divergence_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_438_rsi_divergence_skew_21d
    ECONOMIC RATIONALE: Skewness of rsi_divergence over 21d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(21).skew()

def mtfo_439_rsi_divergence_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_439_rsi_divergence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of rsi_divergence over 21d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(21).kurt()

def mtfo_440_rsi_divergence_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_440_rsi_divergence_skew_63d
    ECONOMIC RATIONALE: Skewness of rsi_divergence over 63d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(63).skew()

def mtfo_441_rsi_divergence_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_441_rsi_divergence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of rsi_divergence over 63d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(63).kurt()

def mtfo_442_rsi_divergence_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_442_rsi_divergence_skew_126d
    ECONOMIC RATIONALE: Skewness of rsi_divergence over 126d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(126).skew()

def mtfo_443_rsi_divergence_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_443_rsi_divergence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of rsi_divergence over 126d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(126).kurt()

def mtfo_444_rsi_divergence_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_444_rsi_divergence_skew_252d
    ECONOMIC RATIONALE: Skewness of rsi_divergence over 252d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(252).skew()

def mtfo_445_rsi_divergence_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_445_rsi_divergence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of rsi_divergence over 252d. Divergence between short and long term momentum.
    """
    return (daily_rsi - weekly_rsi).rolling(252).kurt()

def mtfo_446_oversold_persistence_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_446_oversold_persistence_skew_5d
    ECONOMIC RATIONALE: Skewness of oversold_persistence over 5d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(5).skew()

def mtfo_447_oversold_persistence_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_447_oversold_persistence_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of oversold_persistence over 5d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(5).kurt()

def mtfo_448_oversold_persistence_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_448_oversold_persistence_skew_21d
    ECONOMIC RATIONALE: Skewness of oversold_persistence over 21d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(21).skew()

def mtfo_449_oversold_persistence_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_449_oversold_persistence_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of oversold_persistence over 21d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(21).kurt()

def mtfo_450_oversold_persistence_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_450_oversold_persistence_skew_63d
    ECONOMIC RATIONALE: Skewness of oversold_persistence over 63d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(63).skew()

def mtfo_451_oversold_persistence_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_451_oversold_persistence_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of oversold_persistence over 63d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(63).kurt()

def mtfo_452_oversold_persistence_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_452_oversold_persistence_skew_126d
    ECONOMIC RATIONALE: Skewness of oversold_persistence over 126d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(126).skew()

def mtfo_453_oversold_persistence_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_453_oversold_persistence_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of oversold_persistence over 126d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(126).kurt()

def mtfo_454_oversold_persistence_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_454_oversold_persistence_skew_252d
    ECONOMIC RATIONALE: Skewness of oversold_persistence over 252d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(252).skew()

def mtfo_455_oversold_persistence_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_455_oversold_persistence_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of oversold_persistence over 252d. Duration of extremely oversold conditions.
    """
    return ((daily_rsi < 30).rolling(10).sum()).rolling(252).kurt()

def mtfo_456_stoch_rsi_hybrid_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_456_stoch_rsi_hybrid_skew_5d
    ECONOMIC RATIONALE: Skewness of stoch_rsi_hybrid over 5d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(5).skew()

def mtfo_457_stoch_rsi_hybrid_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_457_stoch_rsi_hybrid_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of stoch_rsi_hybrid over 5d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(5).kurt()

def mtfo_458_stoch_rsi_hybrid_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_458_stoch_rsi_hybrid_skew_21d
    ECONOMIC RATIONALE: Skewness of stoch_rsi_hybrid over 21d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(21).skew()

def mtfo_459_stoch_rsi_hybrid_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_459_stoch_rsi_hybrid_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of stoch_rsi_hybrid over 21d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(21).kurt()

def mtfo_460_stoch_rsi_hybrid_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_460_stoch_rsi_hybrid_skew_63d
    ECONOMIC RATIONALE: Skewness of stoch_rsi_hybrid over 63d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(63).skew()

def mtfo_461_stoch_rsi_hybrid_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_461_stoch_rsi_hybrid_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of stoch_rsi_hybrid over 63d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(63).kurt()

def mtfo_462_stoch_rsi_hybrid_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_462_stoch_rsi_hybrid_skew_126d
    ECONOMIC RATIONALE: Skewness of stoch_rsi_hybrid over 126d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(126).skew()

def mtfo_463_stoch_rsi_hybrid_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_463_stoch_rsi_hybrid_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of stoch_rsi_hybrid over 126d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(126).kurt()

def mtfo_464_stoch_rsi_hybrid_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_464_stoch_rsi_hybrid_skew_252d
    ECONOMIC RATIONALE: Skewness of stoch_rsi_hybrid over 252d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(252).skew()

def mtfo_465_stoch_rsi_hybrid_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_465_stoch_rsi_hybrid_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of stoch_rsi_hybrid over 252d. Composite momentum oscillator.
    """
    return ((stoch_k + daily_rsi) / 2).rolling(252).kurt()

def mtfo_466_williams_r_multi_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_466_williams_r_multi_skew_5d
    ECONOMIC RATIONALE: Skewness of williams_r_multi over 5d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(5).skew()

def mtfo_467_williams_r_multi_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_467_williams_r_multi_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of williams_r_multi over 5d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(5).kurt()

def mtfo_468_williams_r_multi_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_468_williams_r_multi_skew_21d
    ECONOMIC RATIONALE: Skewness of williams_r_multi over 21d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(21).skew()

def mtfo_469_williams_r_multi_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_469_williams_r_multi_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of williams_r_multi over 21d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(21).kurt()

def mtfo_470_williams_r_multi_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_470_williams_r_multi_skew_63d
    ECONOMIC RATIONALE: Skewness of williams_r_multi over 63d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(63).skew()

def mtfo_471_williams_r_multi_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_471_williams_r_multi_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of williams_r_multi over 63d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(63).kurt()

def mtfo_472_williams_r_multi_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_472_williams_r_multi_skew_126d
    ECONOMIC RATIONALE: Skewness of williams_r_multi over 126d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(126).skew()

def mtfo_473_williams_r_multi_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_473_williams_r_multi_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of williams_r_multi over 126d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(126).kurt()

def mtfo_474_williams_r_multi_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_474_williams_r_multi_skew_252d
    ECONOMIC RATIONALE: Skewness of williams_r_multi over 252d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(252).skew()

def mtfo_475_williams_r_multi_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_475_williams_r_multi_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of williams_r_multi over 252d. 21-day Williams %R.
    """
    return ((high.rolling(21).max() - close) / (high.rolling(21).max() - low.rolling(21).min()).replace(0, 1e-9)).rolling(252).kurt()

def mtfo_476_rsi_acceleration_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_476_rsi_acceleration_skew_5d
    ECONOMIC RATIONALE: Skewness of rsi_acceleration over 5d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(5).skew()

def mtfo_477_rsi_acceleration_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_477_rsi_acceleration_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of rsi_acceleration over 5d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(5).kurt()

def mtfo_478_rsi_acceleration_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_478_rsi_acceleration_skew_21d
    ECONOMIC RATIONALE: Skewness of rsi_acceleration over 21d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(21).skew()

def mtfo_479_rsi_acceleration_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_479_rsi_acceleration_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of rsi_acceleration over 21d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(21).kurt()

def mtfo_480_rsi_acceleration_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_480_rsi_acceleration_skew_63d
    ECONOMIC RATIONALE: Skewness of rsi_acceleration over 63d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(63).skew()

def mtfo_481_rsi_acceleration_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_481_rsi_acceleration_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of rsi_acceleration over 63d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(63).kurt()

def mtfo_482_rsi_acceleration_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_482_rsi_acceleration_skew_126d
    ECONOMIC RATIONALE: Skewness of rsi_acceleration over 126d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(126).skew()

def mtfo_483_rsi_acceleration_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_483_rsi_acceleration_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of rsi_acceleration over 126d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(126).kurt()

def mtfo_484_rsi_acceleration_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_484_rsi_acceleration_skew_252d
    ECONOMIC RATIONALE: Skewness of rsi_acceleration over 252d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(252).skew()

def mtfo_485_rsi_acceleration_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_485_rsi_acceleration_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of rsi_acceleration over 252d. Speed of change in RSI levels.
    """
    return (daily_rsi.diff(5)).rolling(252).kurt()

def mtfo_486_cci_oversold_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_486_cci_oversold_skew_5d
    ECONOMIC RATIONALE: Skewness of cci_oversold over 5d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(5).skew()

def mtfo_487_cci_oversold_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_487_cci_oversold_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of cci_oversold over 5d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(5).kurt()

def mtfo_488_cci_oversold_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_488_cci_oversold_skew_21d
    ECONOMIC RATIONALE: Skewness of cci_oversold over 21d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(21).skew()

def mtfo_489_cci_oversold_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_489_cci_oversold_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of cci_oversold over 21d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(21).kurt()

def mtfo_490_cci_oversold_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_490_cci_oversold_skew_63d
    ECONOMIC RATIONALE: Skewness of cci_oversold over 63d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(63).skew()

def mtfo_491_cci_oversold_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_491_cci_oversold_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of cci_oversold over 63d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(63).kurt()

def mtfo_492_cci_oversold_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_492_cci_oversold_skew_126d
    ECONOMIC RATIONALE: Skewness of cci_oversold over 126d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(126).skew()

def mtfo_493_cci_oversold_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_493_cci_oversold_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of cci_oversold over 126d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(126).kurt()

def mtfo_494_cci_oversold_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_494_cci_oversold_skew_252d
    ECONOMIC RATIONALE: Skewness of cci_oversold over 252d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(252).skew()

def mtfo_495_cci_oversold_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_495_cci_oversold_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of cci_oversold over 252d. Commodity Channel Index.
    """
    return ((close - close.rolling(20).mean()) / (0.015 * close.rolling(20).apply(lambda x: np.mean(np.abs(x - np.mean(x)))))).rolling(252).kurt()

def mtfo_496_ultimate_osc_proxy_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_496_ultimate_osc_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of ultimate_osc_proxy over 5d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(5).skew()

def mtfo_497_ultimate_osc_proxy_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_497_ultimate_osc_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of ultimate_osc_proxy over 5d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(5).kurt()

def mtfo_498_ultimate_osc_proxy_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_498_ultimate_osc_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of ultimate_osc_proxy over 21d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(21).skew()

def mtfo_499_ultimate_osc_proxy_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_499_ultimate_osc_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of ultimate_osc_proxy over 21d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(21).kurt()

def mtfo_500_ultimate_osc_proxy_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_500_ultimate_osc_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of ultimate_osc_proxy over 63d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(63).skew()

def mtfo_501_ultimate_osc_proxy_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_501_ultimate_osc_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of ultimate_osc_proxy over 63d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(63).kurt()

def mtfo_502_ultimate_osc_proxy_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_502_ultimate_osc_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of ultimate_osc_proxy over 126d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(126).skew()

def mtfo_503_ultimate_osc_proxy_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_503_ultimate_osc_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of ultimate_osc_proxy over 126d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(126).kurt()

def mtfo_504_ultimate_osc_proxy_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_504_ultimate_osc_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of ultimate_osc_proxy over 252d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(252).skew()

def mtfo_505_ultimate_osc_proxy_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_505_ultimate_osc_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of ultimate_osc_proxy over 252d. Simplified Ultimate Oscillator.
    """
    return (((close - low.rolling(7).min()) + (close - low.rolling(14).min()) + (close - low.rolling(28).min())) / 3).rolling(252).kurt()

def mtfo_506_mfi_oversold_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_506_mfi_oversold_skew_5d
    ECONOMIC RATIONALE: Skewness of mfi_oversold over 5d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).skew()

def mtfo_507_mfi_oversold_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_507_mfi_oversold_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of mfi_oversold over 5d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(5).kurt()

def mtfo_508_mfi_oversold_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_508_mfi_oversold_skew_21d
    ECONOMIC RATIONALE: Skewness of mfi_oversold over 21d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).skew()

def mtfo_509_mfi_oversold_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_509_mfi_oversold_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of mfi_oversold over 21d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(21).kurt()

def mtfo_510_mfi_oversold_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_510_mfi_oversold_skew_63d
    ECONOMIC RATIONALE: Skewness of mfi_oversold over 63d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).skew()

def mtfo_511_mfi_oversold_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_511_mfi_oversold_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of mfi_oversold over 63d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(63).kurt()

def mtfo_512_mfi_oversold_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_512_mfi_oversold_skew_126d
    ECONOMIC RATIONALE: Skewness of mfi_oversold over 126d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).skew()

def mtfo_513_mfi_oversold_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_513_mfi_oversold_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of mfi_oversold over 126d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(126).kurt()

def mtfo_514_mfi_oversold_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_514_mfi_oversold_skew_252d
    ECONOMIC RATIONALE: Skewness of mfi_oversold over 252d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).skew()

def mtfo_515_mfi_oversold_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_515_mfi_oversold_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of mfi_oversold over 252d. Money Flow Index.
    """
    return (100 - (100 / (1 + (volume * close).diff(1).clip(lower=0).rolling(14).mean() / (volume * close).diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))).rolling(252).kurt()

def mtfo_516_tf_regime_spread_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_516_tf_regime_spread_skew_5d
    ECONOMIC RATIONALE: Skewness of tf_regime_spread over 5d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(5).skew()

def mtfo_517_tf_regime_spread_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_517_tf_regime_spread_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of tf_regime_spread over 5d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(5).kurt()

def mtfo_518_tf_regime_spread_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_518_tf_regime_spread_skew_21d
    ECONOMIC RATIONALE: Skewness of tf_regime_spread over 21d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(21).skew()

def mtfo_519_tf_regime_spread_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_519_tf_regime_spread_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of tf_regime_spread over 21d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(21).kurt()

def mtfo_520_tf_regime_spread_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_520_tf_regime_spread_skew_63d
    ECONOMIC RATIONALE: Skewness of tf_regime_spread over 63d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(63).skew()

def mtfo_521_tf_regime_spread_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_521_tf_regime_spread_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of tf_regime_spread over 63d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(63).kurt()

def mtfo_522_tf_regime_spread_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_522_tf_regime_spread_skew_126d
    ECONOMIC RATIONALE: Skewness of tf_regime_spread over 126d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(126).skew()

def mtfo_523_tf_regime_spread_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_523_tf_regime_spread_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of tf_regime_spread over 126d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(126).kurt()

def mtfo_524_tf_regime_spread_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_524_tf_regime_spread_skew_252d
    ECONOMIC RATIONALE: Skewness of tf_regime_spread over 252d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(252).skew()

def mtfo_525_tf_regime_spread_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_525_tf_regime_spread_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of tf_regime_spread over 252d. Spread between short and medium term averages.
    """
    return (close.rolling(5).mean() / close.rolling(63).mean()).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V103_REGISTRY_MOMENTS = {
    "mtfo_376_daily_rsi_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_376_daily_rsi_skew_5d},
    "mtfo_377_daily_rsi_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_377_daily_rsi_kurt_5d},
    "mtfo_378_daily_rsi_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_378_daily_rsi_skew_21d},
    "mtfo_379_daily_rsi_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_379_daily_rsi_kurt_21d},
    "mtfo_380_daily_rsi_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_380_daily_rsi_skew_63d},
    "mtfo_381_daily_rsi_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_381_daily_rsi_kurt_63d},
    "mtfo_382_daily_rsi_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_382_daily_rsi_skew_126d},
    "mtfo_383_daily_rsi_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_383_daily_rsi_kurt_126d},
    "mtfo_384_daily_rsi_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_384_daily_rsi_skew_252d},
    "mtfo_385_daily_rsi_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_385_daily_rsi_kurt_252d},
    "mtfo_386_weekly_rsi_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_386_weekly_rsi_skew_5d},
    "mtfo_387_weekly_rsi_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_387_weekly_rsi_kurt_5d},
    "mtfo_388_weekly_rsi_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_388_weekly_rsi_skew_21d},
    "mtfo_389_weekly_rsi_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_389_weekly_rsi_kurt_21d},
    "mtfo_390_weekly_rsi_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_390_weekly_rsi_skew_63d},
    "mtfo_391_weekly_rsi_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_391_weekly_rsi_kurt_63d},
    "mtfo_392_weekly_rsi_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_392_weekly_rsi_skew_126d},
    "mtfo_393_weekly_rsi_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_393_weekly_rsi_kurt_126d},
    "mtfo_394_weekly_rsi_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_394_weekly_rsi_skew_252d},
    "mtfo_395_weekly_rsi_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_395_weekly_rsi_kurt_252d},
    "mtfo_396_monthly_rsi_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_396_monthly_rsi_skew_5d},
    "mtfo_397_monthly_rsi_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_397_monthly_rsi_kurt_5d},
    "mtfo_398_monthly_rsi_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_398_monthly_rsi_skew_21d},
    "mtfo_399_monthly_rsi_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_399_monthly_rsi_kurt_21d},
    "mtfo_400_monthly_rsi_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_400_monthly_rsi_skew_63d},
    "mtfo_401_monthly_rsi_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_401_monthly_rsi_kurt_63d},
    "mtfo_402_monthly_rsi_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_402_monthly_rsi_skew_126d},
    "mtfo_403_monthly_rsi_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_403_monthly_rsi_kurt_126d},
    "mtfo_404_monthly_rsi_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_404_monthly_rsi_skew_252d},
    "mtfo_405_monthly_rsi_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_405_monthly_rsi_kurt_252d},
    "mtfo_406_stoch_k_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_406_stoch_k_skew_5d},
    "mtfo_407_stoch_k_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_407_stoch_k_kurt_5d},
    "mtfo_408_stoch_k_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_408_stoch_k_skew_21d},
    "mtfo_409_stoch_k_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_409_stoch_k_kurt_21d},
    "mtfo_410_stoch_k_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_410_stoch_k_skew_63d},
    "mtfo_411_stoch_k_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_411_stoch_k_kurt_63d},
    "mtfo_412_stoch_k_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_412_stoch_k_skew_126d},
    "mtfo_413_stoch_k_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_413_stoch_k_kurt_126d},
    "mtfo_414_stoch_k_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_414_stoch_k_skew_252d},
    "mtfo_415_stoch_k_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_415_stoch_k_kurt_252d},
    "mtfo_416_stoch_d_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_416_stoch_d_skew_5d},
    "mtfo_417_stoch_d_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_417_stoch_d_kurt_5d},
    "mtfo_418_stoch_d_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_418_stoch_d_skew_21d},
    "mtfo_419_stoch_d_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_419_stoch_d_kurt_21d},
    "mtfo_420_stoch_d_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_420_stoch_d_skew_63d},
    "mtfo_421_stoch_d_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_421_stoch_d_kurt_63d},
    "mtfo_422_stoch_d_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_422_stoch_d_skew_126d},
    "mtfo_423_stoch_d_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_423_stoch_d_kurt_126d},
    "mtfo_424_stoch_d_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_424_stoch_d_skew_252d},
    "mtfo_425_stoch_d_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_425_stoch_d_kurt_252d},
    "mtfo_426_multi_tf_oversold_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_426_multi_tf_oversold_skew_5d},
    "mtfo_427_multi_tf_oversold_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_427_multi_tf_oversold_kurt_5d},
    "mtfo_428_multi_tf_oversold_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_428_multi_tf_oversold_skew_21d},
    "mtfo_429_multi_tf_oversold_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_429_multi_tf_oversold_kurt_21d},
    "mtfo_430_multi_tf_oversold_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_430_multi_tf_oversold_skew_63d},
    "mtfo_431_multi_tf_oversold_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_431_multi_tf_oversold_kurt_63d},
    "mtfo_432_multi_tf_oversold_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_432_multi_tf_oversold_skew_126d},
    "mtfo_433_multi_tf_oversold_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_433_multi_tf_oversold_kurt_126d},
    "mtfo_434_multi_tf_oversold_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_434_multi_tf_oversold_skew_252d},
    "mtfo_435_multi_tf_oversold_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_435_multi_tf_oversold_kurt_252d},
    "mtfo_436_rsi_divergence_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_436_rsi_divergence_skew_5d},
    "mtfo_437_rsi_divergence_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_437_rsi_divergence_kurt_5d},
    "mtfo_438_rsi_divergence_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_438_rsi_divergence_skew_21d},
    "mtfo_439_rsi_divergence_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_439_rsi_divergence_kurt_21d},
    "mtfo_440_rsi_divergence_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_440_rsi_divergence_skew_63d},
    "mtfo_441_rsi_divergence_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_441_rsi_divergence_kurt_63d},
    "mtfo_442_rsi_divergence_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_442_rsi_divergence_skew_126d},
    "mtfo_443_rsi_divergence_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_443_rsi_divergence_kurt_126d},
    "mtfo_444_rsi_divergence_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_444_rsi_divergence_skew_252d},
    "mtfo_445_rsi_divergence_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_445_rsi_divergence_kurt_252d},
    "mtfo_446_oversold_persistence_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_446_oversold_persistence_skew_5d},
    "mtfo_447_oversold_persistence_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_447_oversold_persistence_kurt_5d},
    "mtfo_448_oversold_persistence_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_448_oversold_persistence_skew_21d},
    "mtfo_449_oversold_persistence_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_449_oversold_persistence_kurt_21d},
    "mtfo_450_oversold_persistence_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_450_oversold_persistence_skew_63d},
    "mtfo_451_oversold_persistence_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_451_oversold_persistence_kurt_63d},
    "mtfo_452_oversold_persistence_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_452_oversold_persistence_skew_126d},
    "mtfo_453_oversold_persistence_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_453_oversold_persistence_kurt_126d},
    "mtfo_454_oversold_persistence_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_454_oversold_persistence_skew_252d},
    "mtfo_455_oversold_persistence_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_455_oversold_persistence_kurt_252d},
    "mtfo_456_stoch_rsi_hybrid_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_456_stoch_rsi_hybrid_skew_5d},
    "mtfo_457_stoch_rsi_hybrid_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_457_stoch_rsi_hybrid_kurt_5d},
    "mtfo_458_stoch_rsi_hybrid_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_458_stoch_rsi_hybrid_skew_21d},
    "mtfo_459_stoch_rsi_hybrid_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_459_stoch_rsi_hybrid_kurt_21d},
    "mtfo_460_stoch_rsi_hybrid_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_460_stoch_rsi_hybrid_skew_63d},
    "mtfo_461_stoch_rsi_hybrid_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_461_stoch_rsi_hybrid_kurt_63d},
    "mtfo_462_stoch_rsi_hybrid_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_462_stoch_rsi_hybrid_skew_126d},
    "mtfo_463_stoch_rsi_hybrid_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_463_stoch_rsi_hybrid_kurt_126d},
    "mtfo_464_stoch_rsi_hybrid_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_464_stoch_rsi_hybrid_skew_252d},
    "mtfo_465_stoch_rsi_hybrid_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_465_stoch_rsi_hybrid_kurt_252d},
    "mtfo_466_williams_r_multi_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_466_williams_r_multi_skew_5d},
    "mtfo_467_williams_r_multi_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_467_williams_r_multi_kurt_5d},
    "mtfo_468_williams_r_multi_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_468_williams_r_multi_skew_21d},
    "mtfo_469_williams_r_multi_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_469_williams_r_multi_kurt_21d},
    "mtfo_470_williams_r_multi_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_470_williams_r_multi_skew_63d},
    "mtfo_471_williams_r_multi_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_471_williams_r_multi_kurt_63d},
    "mtfo_472_williams_r_multi_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_472_williams_r_multi_skew_126d},
    "mtfo_473_williams_r_multi_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_473_williams_r_multi_kurt_126d},
    "mtfo_474_williams_r_multi_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_474_williams_r_multi_skew_252d},
    "mtfo_475_williams_r_multi_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_475_williams_r_multi_kurt_252d},
    "mtfo_476_rsi_acceleration_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_476_rsi_acceleration_skew_5d},
    "mtfo_477_rsi_acceleration_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_477_rsi_acceleration_kurt_5d},
    "mtfo_478_rsi_acceleration_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_478_rsi_acceleration_skew_21d},
    "mtfo_479_rsi_acceleration_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_479_rsi_acceleration_kurt_21d},
    "mtfo_480_rsi_acceleration_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_480_rsi_acceleration_skew_63d},
    "mtfo_481_rsi_acceleration_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_481_rsi_acceleration_kurt_63d},
    "mtfo_482_rsi_acceleration_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_482_rsi_acceleration_skew_126d},
    "mtfo_483_rsi_acceleration_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_483_rsi_acceleration_kurt_126d},
    "mtfo_484_rsi_acceleration_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_484_rsi_acceleration_skew_252d},
    "mtfo_485_rsi_acceleration_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_485_rsi_acceleration_kurt_252d},
    "mtfo_486_cci_oversold_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_486_cci_oversold_skew_5d},
    "mtfo_487_cci_oversold_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_487_cci_oversold_kurt_5d},
    "mtfo_488_cci_oversold_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_488_cci_oversold_skew_21d},
    "mtfo_489_cci_oversold_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_489_cci_oversold_kurt_21d},
    "mtfo_490_cci_oversold_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_490_cci_oversold_skew_63d},
    "mtfo_491_cci_oversold_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_491_cci_oversold_kurt_63d},
    "mtfo_492_cci_oversold_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_492_cci_oversold_skew_126d},
    "mtfo_493_cci_oversold_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_493_cci_oversold_kurt_126d},
    "mtfo_494_cci_oversold_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_494_cci_oversold_skew_252d},
    "mtfo_495_cci_oversold_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_495_cci_oversold_kurt_252d},
    "mtfo_496_ultimate_osc_proxy_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_496_ultimate_osc_proxy_skew_5d},
    "mtfo_497_ultimate_osc_proxy_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_497_ultimate_osc_proxy_kurt_5d},
    "mtfo_498_ultimate_osc_proxy_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_498_ultimate_osc_proxy_skew_21d},
    "mtfo_499_ultimate_osc_proxy_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_499_ultimate_osc_proxy_kurt_21d},
    "mtfo_500_ultimate_osc_proxy_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_500_ultimate_osc_proxy_skew_63d},
    "mtfo_501_ultimate_osc_proxy_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_501_ultimate_osc_proxy_kurt_63d},
    "mtfo_502_ultimate_osc_proxy_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_502_ultimate_osc_proxy_skew_126d},
    "mtfo_503_ultimate_osc_proxy_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_503_ultimate_osc_proxy_kurt_126d},
    "mtfo_504_ultimate_osc_proxy_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_504_ultimate_osc_proxy_skew_252d},
    "mtfo_505_ultimate_osc_proxy_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_505_ultimate_osc_proxy_kurt_252d},
    "mtfo_506_mfi_oversold_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_506_mfi_oversold_skew_5d},
    "mtfo_507_mfi_oversold_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_507_mfi_oversold_kurt_5d},
    "mtfo_508_mfi_oversold_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_508_mfi_oversold_skew_21d},
    "mtfo_509_mfi_oversold_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_509_mfi_oversold_kurt_21d},
    "mtfo_510_mfi_oversold_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_510_mfi_oversold_skew_63d},
    "mtfo_511_mfi_oversold_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_511_mfi_oversold_kurt_63d},
    "mtfo_512_mfi_oversold_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_512_mfi_oversold_skew_126d},
    "mtfo_513_mfi_oversold_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_513_mfi_oversold_kurt_126d},
    "mtfo_514_mfi_oversold_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_514_mfi_oversold_skew_252d},
    "mtfo_515_mfi_oversold_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_515_mfi_oversold_kurt_252d},
    "mtfo_516_tf_regime_spread_skew_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_516_tf_regime_spread_skew_5d},
    "mtfo_517_tf_regime_spread_kurt_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_517_tf_regime_spread_kurt_5d},
    "mtfo_518_tf_regime_spread_skew_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_518_tf_regime_spread_skew_21d},
    "mtfo_519_tf_regime_spread_kurt_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_519_tf_regime_spread_kurt_21d},
    "mtfo_520_tf_regime_spread_skew_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_520_tf_regime_spread_skew_63d},
    "mtfo_521_tf_regime_spread_kurt_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_521_tf_regime_spread_kurt_63d},
    "mtfo_522_tf_regime_spread_skew_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_522_tf_regime_spread_skew_126d},
    "mtfo_523_tf_regime_spread_kurt_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_523_tf_regime_spread_kurt_126d},
    "mtfo_524_tf_regime_spread_skew_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_524_tf_regime_spread_skew_252d},
    "mtfo_525_tf_regime_spread_kurt_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_525_tf_regime_spread_kurt_252d},
}
