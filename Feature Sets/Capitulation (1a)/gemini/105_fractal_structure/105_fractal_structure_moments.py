"""
105_fractal_structure — Statistical Moments
Domain: fractal_structure
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

def frac_376_hurst_exponent_proxy_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_376_hurst_exponent_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of hurst_exponent_proxy over 5d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(5).skew()

def frac_377_hurst_exponent_proxy_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_377_hurst_exponent_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of hurst_exponent_proxy over 5d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(5).kurt()

def frac_378_hurst_exponent_proxy_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_378_hurst_exponent_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of hurst_exponent_proxy over 21d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(21).skew()

def frac_379_hurst_exponent_proxy_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_379_hurst_exponent_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of hurst_exponent_proxy over 21d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(21).kurt()

def frac_380_hurst_exponent_proxy_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_380_hurst_exponent_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of hurst_exponent_proxy over 63d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(63).skew()

def frac_381_hurst_exponent_proxy_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_381_hurst_exponent_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of hurst_exponent_proxy over 63d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(63).kurt()

def frac_382_hurst_exponent_proxy_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_382_hurst_exponent_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of hurst_exponent_proxy over 126d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(126).skew()

def frac_383_hurst_exponent_proxy_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_383_hurst_exponent_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of hurst_exponent_proxy over 126d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(126).kurt()

def frac_384_hurst_exponent_proxy_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_384_hurst_exponent_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of hurst_exponent_proxy over 252d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(252).skew()

def frac_385_hurst_exponent_proxy_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_385_hurst_exponent_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of hurst_exponent_proxy over 252d. Simplified Hurst exponent for trend persistence.
    """
    return (np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)).rolling(252).kurt()

def frac_386_fractal_dimension_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_386_fractal_dimension_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_dimension over 5d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(5).skew()

def frac_387_fractal_dimension_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_387_fractal_dimension_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_dimension over 5d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(5).kurt()

def frac_388_fractal_dimension_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_388_fractal_dimension_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_dimension over 21d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(21).skew()

def frac_389_fractal_dimension_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_389_fractal_dimension_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_dimension over 21d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(21).kurt()

def frac_390_fractal_dimension_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_390_fractal_dimension_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_dimension over 63d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(63).skew()

def frac_391_fractal_dimension_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_391_fractal_dimension_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_dimension over 63d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(63).kurt()

def frac_392_fractal_dimension_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_392_fractal_dimension_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_dimension over 126d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(126).skew()

def frac_393_fractal_dimension_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_393_fractal_dimension_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_dimension over 126d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(126).kurt()

def frac_394_fractal_dimension_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_394_fractal_dimension_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_dimension over 252d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(252).skew()

def frac_395_fractal_dimension_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_395_fractal_dimension_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_dimension over 252d. Estimated fractal dimension.
    """
    return ((np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)).rolling(252).kurt()

def frac_396_efficiency_ratio_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_396_efficiency_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of efficiency_ratio over 5d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(5).skew()

def frac_397_efficiency_ratio_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_397_efficiency_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of efficiency_ratio over 5d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(5).kurt()

def frac_398_efficiency_ratio_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_398_efficiency_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of efficiency_ratio over 21d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(21).skew()

def frac_399_efficiency_ratio_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_399_efficiency_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of efficiency_ratio over 21d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(21).kurt()

def frac_400_efficiency_ratio_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_400_efficiency_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of efficiency_ratio over 63d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(63).skew()

def frac_401_efficiency_ratio_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_401_efficiency_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of efficiency_ratio over 63d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(63).kurt()

def frac_402_efficiency_ratio_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_402_efficiency_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of efficiency_ratio over 126d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(126).skew()

def frac_403_efficiency_ratio_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_403_efficiency_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of efficiency_ratio over 126d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(126).kurt()

def frac_404_efficiency_ratio_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_404_efficiency_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of efficiency_ratio over 252d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(252).skew()

def frac_405_efficiency_ratio_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_405_efficiency_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of efficiency_ratio over 252d. Kaufman's Efficiency Ratio.
    """
    return (abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)).rolling(252).kurt()

def frac_406_fractal_volatility_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_406_fractal_volatility_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_volatility over 5d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(5).skew()

def frac_407_fractal_volatility_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_407_fractal_volatility_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_volatility over 5d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(5).kurt()

def frac_408_fractal_volatility_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_408_fractal_volatility_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_volatility over 21d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(21).skew()

def frac_409_fractal_volatility_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_409_fractal_volatility_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_volatility over 21d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(21).kurt()

def frac_410_fractal_volatility_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_410_fractal_volatility_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_volatility over 63d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(63).skew()

def frac_411_fractal_volatility_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_411_fractal_volatility_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_volatility over 63d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(63).kurt()

def frac_412_fractal_volatility_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_412_fractal_volatility_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_volatility over 126d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(126).skew()

def frac_413_fractal_volatility_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_413_fractal_volatility_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_volatility over 126d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(126).kurt()

def frac_414_fractal_volatility_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_414_fractal_volatility_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_volatility over 252d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(252).skew()

def frac_415_fractal_volatility_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_415_fractal_volatility_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_volatility over 252d. Complexity of price path relative to range.
    """
    return (close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)).rolling(252).kurt()

def frac_416_self_similarity_score_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_416_self_similarity_score_skew_5d
    ECONOMIC RATIONALE: Skewness of self_similarity_score over 5d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(5).skew()

def frac_417_self_similarity_score_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_417_self_similarity_score_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of self_similarity_score over 5d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(5).kurt()

def frac_418_self_similarity_score_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_418_self_similarity_score_skew_21d
    ECONOMIC RATIONALE: Skewness of self_similarity_score over 21d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(21).skew()

def frac_419_self_similarity_score_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_419_self_similarity_score_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of self_similarity_score over 21d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(21).kurt()

def frac_420_self_similarity_score_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_420_self_similarity_score_skew_63d
    ECONOMIC RATIONALE: Skewness of self_similarity_score over 63d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(63).skew()

def frac_421_self_similarity_score_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_421_self_similarity_score_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of self_similarity_score over 63d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(63).kurt()

def frac_422_self_similarity_score_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_422_self_similarity_score_skew_126d
    ECONOMIC RATIONALE: Skewness of self_similarity_score over 126d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(126).skew()

def frac_423_self_similarity_score_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_423_self_similarity_score_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of self_similarity_score over 126d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(126).kurt()

def frac_424_self_similarity_score_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_424_self_similarity_score_skew_252d
    ECONOMIC RATIONALE: Skewness of self_similarity_score over 252d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(252).skew()

def frac_425_self_similarity_score_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_425_self_similarity_score_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of self_similarity_score over 252d. Correlation of returns with lagged returns.
    """
    return (close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))).rolling(252).kurt()

def frac_426_fractal_breakout_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_426_fractal_breakout_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_breakout over 5d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(5).skew()

def frac_427_fractal_breakout_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_427_fractal_breakout_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_breakout over 5d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(5).kurt()

def frac_428_fractal_breakout_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_428_fractal_breakout_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_breakout over 21d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(21).skew()

def frac_429_fractal_breakout_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_429_fractal_breakout_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_breakout over 21d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(21).kurt()

def frac_430_fractal_breakout_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_430_fractal_breakout_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_breakout over 63d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(63).skew()

def frac_431_fractal_breakout_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_431_fractal_breakout_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_breakout over 63d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(63).kurt()

def frac_432_fractal_breakout_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_432_fractal_breakout_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_breakout over 126d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(126).skew()

def frac_433_fractal_breakout_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_433_fractal_breakout_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_breakout over 126d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(126).kurt()

def frac_434_fractal_breakout_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_434_fractal_breakout_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_breakout over 252d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(252).skew()

def frac_435_fractal_breakout_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_435_fractal_breakout_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_breakout over 252d. Breakout of local fractal peaks.
    """
    return ((high > high.rolling(20).max().shift(1)).astype(float)).rolling(252).kurt()

def frac_436_fractal_support_violation_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_436_fractal_support_violation_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_support_violation over 5d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(5).skew()

def frac_437_fractal_support_violation_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_437_fractal_support_violation_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_support_violation over 5d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(5).kurt()

def frac_438_fractal_support_violation_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_438_fractal_support_violation_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_support_violation over 21d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(21).skew()

def frac_439_fractal_support_violation_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_439_fractal_support_violation_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_support_violation over 21d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(21).kurt()

def frac_440_fractal_support_violation_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_440_fractal_support_violation_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_support_violation over 63d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(63).skew()

def frac_441_fractal_support_violation_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_441_fractal_support_violation_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_support_violation over 63d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(63).kurt()

def frac_442_fractal_support_violation_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_442_fractal_support_violation_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_support_violation over 126d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(126).skew()

def frac_443_fractal_support_violation_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_443_fractal_support_violation_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_support_violation over 126d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(126).kurt()

def frac_444_fractal_support_violation_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_444_fractal_support_violation_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_support_violation over 252d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(252).skew()

def frac_445_fractal_support_violation_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_445_fractal_support_violation_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_support_violation over 252d. Breakdown of local fractal troughs.
    """
    return ((low < low.rolling(20).min().shift(1)).astype(float)).rolling(252).kurt()

def frac_446_chaos_theory_osc_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_446_chaos_theory_osc_skew_5d
    ECONOMIC RATIONALE: Skewness of chaos_theory_osc over 5d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(5).skew()

def frac_447_chaos_theory_osc_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_447_chaos_theory_osc_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of chaos_theory_osc over 5d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(5).kurt()

def frac_448_chaos_theory_osc_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_448_chaos_theory_osc_skew_21d
    ECONOMIC RATIONALE: Skewness of chaos_theory_osc over 21d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(21).skew()

def frac_449_chaos_theory_osc_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_449_chaos_theory_osc_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of chaos_theory_osc over 21d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(21).kurt()

def frac_450_chaos_theory_osc_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_450_chaos_theory_osc_skew_63d
    ECONOMIC RATIONALE: Skewness of chaos_theory_osc over 63d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(63).skew()

def frac_451_chaos_theory_osc_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_451_chaos_theory_osc_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of chaos_theory_osc over 63d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(63).kurt()

def frac_452_chaos_theory_osc_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_452_chaos_theory_osc_skew_126d
    ECONOMIC RATIONALE: Skewness of chaos_theory_osc over 126d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(126).skew()

def frac_453_chaos_theory_osc_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_453_chaos_theory_osc_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of chaos_theory_osc over 126d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(126).kurt()

def frac_454_chaos_theory_osc_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_454_chaos_theory_osc_skew_252d
    ECONOMIC RATIONALE: Skewness of chaos_theory_osc over 252d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(252).skew()

def frac_455_chaos_theory_osc_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_455_chaos_theory_osc_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of chaos_theory_osc over 252d. Noise-adjusted short-term momentum.
    """
    return (close.pct_change(1) / close.pct_change(5).rolling(21).std()).rolling(252).kurt()

def frac_456_entropy_proxy_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_456_entropy_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of entropy_proxy over 5d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(5).skew()

def frac_457_entropy_proxy_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_457_entropy_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of entropy_proxy over 5d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(5).kurt()

def frac_458_entropy_proxy_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_458_entropy_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of entropy_proxy over 21d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(21).skew()

def frac_459_entropy_proxy_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_459_entropy_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of entropy_proxy over 21d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(21).kurt()

def frac_460_entropy_proxy_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_460_entropy_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of entropy_proxy over 63d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(63).skew()

def frac_461_entropy_proxy_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_461_entropy_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of entropy_proxy over 63d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(63).kurt()

def frac_462_entropy_proxy_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_462_entropy_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of entropy_proxy over 126d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(126).skew()

def frac_463_entropy_proxy_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_463_entropy_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of entropy_proxy over 126d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(126).kurt()

def frac_464_entropy_proxy_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_464_entropy_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of entropy_proxy over 252d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(252).skew()

def frac_465_entropy_proxy_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_465_entropy_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of entropy_proxy over 252d. Approximate entropy of price distribution.
    """
    return (close.rolling(21).apply(lambda x: -np.sum(np.histogram(x, bins=10, density=True)[0] * np.log(np.histogram(x, bins=10, density=True)[0] + 1e-9)))).rolling(252).kurt()

def frac_466_fractal_energy_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_466_fractal_energy_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_energy over 5d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(5).skew()

def frac_467_fractal_energy_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_467_fractal_energy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_energy over 5d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(5).kurt()

def frac_468_fractal_energy_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_468_fractal_energy_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_energy over 21d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(21).skew()

def frac_469_fractal_energy_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_469_fractal_energy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_energy over 21d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(21).kurt()

def frac_470_fractal_energy_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_470_fractal_energy_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_energy over 63d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(63).skew()

def frac_471_fractal_energy_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_471_fractal_energy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_energy over 63d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(63).kurt()

def frac_472_fractal_energy_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_472_fractal_energy_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_energy over 126d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(126).skew()

def frac_473_fractal_energy_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_473_fractal_energy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_energy over 126d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(126).kurt()

def frac_474_fractal_energy_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_474_fractal_energy_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_energy over 252d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(252).skew()

def frac_475_fractal_energy_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_475_fractal_energy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_energy over 252d. Energy dissipated in price movement.
    """
    return (close.diff(1).pow(2).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min()).pow(2)).rolling(252).kurt()

def frac_476_multi_scale_vol_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_476_multi_scale_vol_skew_5d
    ECONOMIC RATIONALE: Skewness of multi_scale_vol over 5d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(5).skew()

def frac_477_multi_scale_vol_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_477_multi_scale_vol_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of multi_scale_vol over 5d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(5).kurt()

def frac_478_multi_scale_vol_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_478_multi_scale_vol_skew_21d
    ECONOMIC RATIONALE: Skewness of multi_scale_vol over 21d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(21).skew()

def frac_479_multi_scale_vol_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_479_multi_scale_vol_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of multi_scale_vol over 21d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(21).kurt()

def frac_480_multi_scale_vol_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_480_multi_scale_vol_skew_63d
    ECONOMIC RATIONALE: Skewness of multi_scale_vol over 63d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(63).skew()

def frac_481_multi_scale_vol_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_481_multi_scale_vol_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of multi_scale_vol over 63d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(63).kurt()

def frac_482_multi_scale_vol_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_482_multi_scale_vol_skew_126d
    ECONOMIC RATIONALE: Skewness of multi_scale_vol over 126d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(126).skew()

def frac_483_multi_scale_vol_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_483_multi_scale_vol_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of multi_scale_vol over 126d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(126).kurt()

def frac_484_multi_scale_vol_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_484_multi_scale_vol_skew_252d
    ECONOMIC RATIONALE: Skewness of multi_scale_vol over 252d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(252).skew()

def frac_485_multi_scale_vol_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_485_multi_scale_vol_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of multi_scale_vol over 252d. Ratio of short-term to long-term volatility structure.
    """
    return (close.rolling(5).std() / close.rolling(63).std()).rolling(252).kurt()

def frac_486_fractal_regime_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_486_fractal_regime_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_regime over 5d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(5).skew()

def frac_487_fractal_regime_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_487_fractal_regime_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_regime over 5d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(5).kurt()

def frac_488_fractal_regime_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_488_fractal_regime_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_regime over 21d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(21).skew()

def frac_489_fractal_regime_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_489_fractal_regime_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_regime over 21d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(21).kurt()

def frac_490_fractal_regime_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_490_fractal_regime_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_regime over 63d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(63).skew()

def frac_491_fractal_regime_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_491_fractal_regime_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_regime over 63d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(63).kurt()

def frac_492_fractal_regime_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_492_fractal_regime_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_regime over 126d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(126).skew()

def frac_493_fractal_regime_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_493_fractal_regime_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_regime over 126d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(126).kurt()

def frac_494_fractal_regime_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_494_fractal_regime_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_regime over 252d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(252).skew()

def frac_495_fractal_regime_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_495_fractal_regime_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_regime over 252d. Fractal trend of moving average changes.
    """
    return (close.rolling(21).mean().diff(5).rolling(63).mean()).rolling(252).kurt()

def frac_496_box_counting_proxy_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_496_box_counting_proxy_skew_5d
    ECONOMIC RATIONALE: Skewness of box_counting_proxy over 5d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(5).skew()

def frac_497_box_counting_proxy_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_497_box_counting_proxy_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of box_counting_proxy over 5d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(5).kurt()

def frac_498_box_counting_proxy_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_498_box_counting_proxy_skew_21d
    ECONOMIC RATIONALE: Skewness of box_counting_proxy over 21d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(21).skew()

def frac_499_box_counting_proxy_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_499_box_counting_proxy_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of box_counting_proxy over 21d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(21).kurt()

def frac_500_box_counting_proxy_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_500_box_counting_proxy_skew_63d
    ECONOMIC RATIONALE: Skewness of box_counting_proxy over 63d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(63).skew()

def frac_501_box_counting_proxy_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_501_box_counting_proxy_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of box_counting_proxy over 63d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(63).kurt()

def frac_502_box_counting_proxy_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_502_box_counting_proxy_skew_126d
    ECONOMIC RATIONALE: Skewness of box_counting_proxy over 126d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(126).skew()

def frac_503_box_counting_proxy_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_503_box_counting_proxy_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of box_counting_proxy over 126d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(126).kurt()

def frac_504_box_counting_proxy_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_504_box_counting_proxy_skew_252d
    ECONOMIC RATIONALE: Skewness of box_counting_proxy over 252d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(252).skew()

def frac_505_box_counting_proxy_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_505_box_counting_proxy_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of box_counting_proxy over 252d. Box-counting dimension approximation.
    """
    return (((high.rolling(10).max() - low.rolling(10).min()) + (high.rolling(10).max().shift(10) - low.rolling(10).min().shift(10))) / (high.rolling(20).max() - low.rolling(20).min())).rolling(252).kurt()

def frac_506_fractal_trend_index_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_506_fractal_trend_index_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_trend_index over 5d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(5).skew()

def frac_507_fractal_trend_index_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_507_fractal_trend_index_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_trend_index over 5d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(5).kurt()

def frac_508_fractal_trend_index_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_508_fractal_trend_index_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_trend_index over 21d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(21).skew()

def frac_509_fractal_trend_index_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_509_fractal_trend_index_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_trend_index over 21d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(21).kurt()

def frac_510_fractal_trend_index_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_510_fractal_trend_index_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_trend_index over 63d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(63).skew()

def frac_511_fractal_trend_index_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_511_fractal_trend_index_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_trend_index over 63d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(63).kurt()

def frac_512_fractal_trend_index_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_512_fractal_trend_index_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_trend_index over 126d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(126).skew()

def frac_513_fractal_trend_index_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_513_fractal_trend_index_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_trend_index over 126d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(126).kurt()

def frac_514_fractal_trend_index_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_514_fractal_trend_index_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_trend_index over 252d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(252).skew()

def frac_515_fractal_trend_index_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_515_fractal_trend_index_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_trend_index over 252d. Trend magnitude relative to structural range.
    """
    return (close.diff(63) / (high.rolling(63).max() - low.rolling(63).min())).rolling(252).kurt()

def frac_516_fractal_noise_ratio_skew_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_516_fractal_noise_ratio_skew_5d
    ECONOMIC RATIONALE: Skewness of fractal_noise_ratio over 5d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(5).skew()

def frac_517_fractal_noise_ratio_kurt_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_517_fractal_noise_ratio_kurt_5d
    ECONOMIC RATIONALE: Kurtosis of fractal_noise_ratio over 5d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(5).kurt()

def frac_518_fractal_noise_ratio_skew_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_518_fractal_noise_ratio_skew_21d
    ECONOMIC RATIONALE: Skewness of fractal_noise_ratio over 21d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(21).skew()

def frac_519_fractal_noise_ratio_kurt_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_519_fractal_noise_ratio_kurt_21d
    ECONOMIC RATIONALE: Kurtosis of fractal_noise_ratio over 21d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(21).kurt()

def frac_520_fractal_noise_ratio_skew_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_520_fractal_noise_ratio_skew_63d
    ECONOMIC RATIONALE: Skewness of fractal_noise_ratio over 63d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(63).skew()

def frac_521_fractal_noise_ratio_kurt_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_521_fractal_noise_ratio_kurt_63d
    ECONOMIC RATIONALE: Kurtosis of fractal_noise_ratio over 63d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(63).kurt()

def frac_522_fractal_noise_ratio_skew_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_522_fractal_noise_ratio_skew_126d
    ECONOMIC RATIONALE: Skewness of fractal_noise_ratio over 126d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(126).skew()

def frac_523_fractal_noise_ratio_kurt_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_523_fractal_noise_ratio_kurt_126d
    ECONOMIC RATIONALE: Kurtosis of fractal_noise_ratio over 126d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(126).kurt()

def frac_524_fractal_noise_ratio_skew_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_524_fractal_noise_ratio_skew_252d
    ECONOMIC RATIONALE: Skewness of fractal_noise_ratio over 252d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(252).skew()

def frac_525_fractal_noise_ratio_kurt_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_525_fractal_noise_ratio_kurt_252d
    ECONOMIC RATIONALE: Kurtosis of fractal_noise_ratio over 252d. Proportion of price movement attributed to noise.
    """
    return (1 - efficiency_ratio).rolling(252).kurt()

# ── Registry ──────────────────────────────────────────────────────────────────
V105_REGISTRY_MOMENTS = {
    "frac_376_hurst_exponent_proxy_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_376_hurst_exponent_proxy_skew_5d},
    "frac_377_hurst_exponent_proxy_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_377_hurst_exponent_proxy_kurt_5d},
    "frac_378_hurst_exponent_proxy_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_378_hurst_exponent_proxy_skew_21d},
    "frac_379_hurst_exponent_proxy_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_379_hurst_exponent_proxy_kurt_21d},
    "frac_380_hurst_exponent_proxy_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_380_hurst_exponent_proxy_skew_63d},
    "frac_381_hurst_exponent_proxy_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_381_hurst_exponent_proxy_kurt_63d},
    "frac_382_hurst_exponent_proxy_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_382_hurst_exponent_proxy_skew_126d},
    "frac_383_hurst_exponent_proxy_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_383_hurst_exponent_proxy_kurt_126d},
    "frac_384_hurst_exponent_proxy_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_384_hurst_exponent_proxy_skew_252d},
    "frac_385_hurst_exponent_proxy_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_385_hurst_exponent_proxy_kurt_252d},
    "frac_386_fractal_dimension_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_386_fractal_dimension_skew_5d},
    "frac_387_fractal_dimension_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_387_fractal_dimension_kurt_5d},
    "frac_388_fractal_dimension_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_388_fractal_dimension_skew_21d},
    "frac_389_fractal_dimension_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_389_fractal_dimension_kurt_21d},
    "frac_390_fractal_dimension_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_390_fractal_dimension_skew_63d},
    "frac_391_fractal_dimension_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_391_fractal_dimension_kurt_63d},
    "frac_392_fractal_dimension_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_392_fractal_dimension_skew_126d},
    "frac_393_fractal_dimension_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_393_fractal_dimension_kurt_126d},
    "frac_394_fractal_dimension_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_394_fractal_dimension_skew_252d},
    "frac_395_fractal_dimension_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_395_fractal_dimension_kurt_252d},
    "frac_396_efficiency_ratio_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_396_efficiency_ratio_skew_5d},
    "frac_397_efficiency_ratio_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_397_efficiency_ratio_kurt_5d},
    "frac_398_efficiency_ratio_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_398_efficiency_ratio_skew_21d},
    "frac_399_efficiency_ratio_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_399_efficiency_ratio_kurt_21d},
    "frac_400_efficiency_ratio_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_400_efficiency_ratio_skew_63d},
    "frac_401_efficiency_ratio_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_401_efficiency_ratio_kurt_63d},
    "frac_402_efficiency_ratio_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_402_efficiency_ratio_skew_126d},
    "frac_403_efficiency_ratio_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_403_efficiency_ratio_kurt_126d},
    "frac_404_efficiency_ratio_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_404_efficiency_ratio_skew_252d},
    "frac_405_efficiency_ratio_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_405_efficiency_ratio_kurt_252d},
    "frac_406_fractal_volatility_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_406_fractal_volatility_skew_5d},
    "frac_407_fractal_volatility_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_407_fractal_volatility_kurt_5d},
    "frac_408_fractal_volatility_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_408_fractal_volatility_skew_21d},
    "frac_409_fractal_volatility_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_409_fractal_volatility_kurt_21d},
    "frac_410_fractal_volatility_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_410_fractal_volatility_skew_63d},
    "frac_411_fractal_volatility_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_411_fractal_volatility_kurt_63d},
    "frac_412_fractal_volatility_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_412_fractal_volatility_skew_126d},
    "frac_413_fractal_volatility_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_413_fractal_volatility_kurt_126d},
    "frac_414_fractal_volatility_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_414_fractal_volatility_skew_252d},
    "frac_415_fractal_volatility_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_415_fractal_volatility_kurt_252d},
    "frac_416_self_similarity_score_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_416_self_similarity_score_skew_5d},
    "frac_417_self_similarity_score_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_417_self_similarity_score_kurt_5d},
    "frac_418_self_similarity_score_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_418_self_similarity_score_skew_21d},
    "frac_419_self_similarity_score_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_419_self_similarity_score_kurt_21d},
    "frac_420_self_similarity_score_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_420_self_similarity_score_skew_63d},
    "frac_421_self_similarity_score_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_421_self_similarity_score_kurt_63d},
    "frac_422_self_similarity_score_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_422_self_similarity_score_skew_126d},
    "frac_423_self_similarity_score_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_423_self_similarity_score_kurt_126d},
    "frac_424_self_similarity_score_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_424_self_similarity_score_skew_252d},
    "frac_425_self_similarity_score_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_425_self_similarity_score_kurt_252d},
    "frac_426_fractal_breakout_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_426_fractal_breakout_skew_5d},
    "frac_427_fractal_breakout_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_427_fractal_breakout_kurt_5d},
    "frac_428_fractal_breakout_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_428_fractal_breakout_skew_21d},
    "frac_429_fractal_breakout_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_429_fractal_breakout_kurt_21d},
    "frac_430_fractal_breakout_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_430_fractal_breakout_skew_63d},
    "frac_431_fractal_breakout_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_431_fractal_breakout_kurt_63d},
    "frac_432_fractal_breakout_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_432_fractal_breakout_skew_126d},
    "frac_433_fractal_breakout_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_433_fractal_breakout_kurt_126d},
    "frac_434_fractal_breakout_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_434_fractal_breakout_skew_252d},
    "frac_435_fractal_breakout_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_435_fractal_breakout_kurt_252d},
    "frac_436_fractal_support_violation_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_436_fractal_support_violation_skew_5d},
    "frac_437_fractal_support_violation_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_437_fractal_support_violation_kurt_5d},
    "frac_438_fractal_support_violation_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_438_fractal_support_violation_skew_21d},
    "frac_439_fractal_support_violation_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_439_fractal_support_violation_kurt_21d},
    "frac_440_fractal_support_violation_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_440_fractal_support_violation_skew_63d},
    "frac_441_fractal_support_violation_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_441_fractal_support_violation_kurt_63d},
    "frac_442_fractal_support_violation_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_442_fractal_support_violation_skew_126d},
    "frac_443_fractal_support_violation_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_443_fractal_support_violation_kurt_126d},
    "frac_444_fractal_support_violation_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_444_fractal_support_violation_skew_252d},
    "frac_445_fractal_support_violation_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_445_fractal_support_violation_kurt_252d},
    "frac_446_chaos_theory_osc_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_446_chaos_theory_osc_skew_5d},
    "frac_447_chaos_theory_osc_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_447_chaos_theory_osc_kurt_5d},
    "frac_448_chaos_theory_osc_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_448_chaos_theory_osc_skew_21d},
    "frac_449_chaos_theory_osc_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_449_chaos_theory_osc_kurt_21d},
    "frac_450_chaos_theory_osc_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_450_chaos_theory_osc_skew_63d},
    "frac_451_chaos_theory_osc_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_451_chaos_theory_osc_kurt_63d},
    "frac_452_chaos_theory_osc_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_452_chaos_theory_osc_skew_126d},
    "frac_453_chaos_theory_osc_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_453_chaos_theory_osc_kurt_126d},
    "frac_454_chaos_theory_osc_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_454_chaos_theory_osc_skew_252d},
    "frac_455_chaos_theory_osc_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_455_chaos_theory_osc_kurt_252d},
    "frac_456_entropy_proxy_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_456_entropy_proxy_skew_5d},
    "frac_457_entropy_proxy_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_457_entropy_proxy_kurt_5d},
    "frac_458_entropy_proxy_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_458_entropy_proxy_skew_21d},
    "frac_459_entropy_proxy_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_459_entropy_proxy_kurt_21d},
    "frac_460_entropy_proxy_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_460_entropy_proxy_skew_63d},
    "frac_461_entropy_proxy_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_461_entropy_proxy_kurt_63d},
    "frac_462_entropy_proxy_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_462_entropy_proxy_skew_126d},
    "frac_463_entropy_proxy_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_463_entropy_proxy_kurt_126d},
    "frac_464_entropy_proxy_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_464_entropy_proxy_skew_252d},
    "frac_465_entropy_proxy_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_465_entropy_proxy_kurt_252d},
    "frac_466_fractal_energy_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_466_fractal_energy_skew_5d},
    "frac_467_fractal_energy_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_467_fractal_energy_kurt_5d},
    "frac_468_fractal_energy_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_468_fractal_energy_skew_21d},
    "frac_469_fractal_energy_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_469_fractal_energy_kurt_21d},
    "frac_470_fractal_energy_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_470_fractal_energy_skew_63d},
    "frac_471_fractal_energy_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_471_fractal_energy_kurt_63d},
    "frac_472_fractal_energy_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_472_fractal_energy_skew_126d},
    "frac_473_fractal_energy_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_473_fractal_energy_kurt_126d},
    "frac_474_fractal_energy_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_474_fractal_energy_skew_252d},
    "frac_475_fractal_energy_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_475_fractal_energy_kurt_252d},
    "frac_476_multi_scale_vol_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_476_multi_scale_vol_skew_5d},
    "frac_477_multi_scale_vol_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_477_multi_scale_vol_kurt_5d},
    "frac_478_multi_scale_vol_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_478_multi_scale_vol_skew_21d},
    "frac_479_multi_scale_vol_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_479_multi_scale_vol_kurt_21d},
    "frac_480_multi_scale_vol_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_480_multi_scale_vol_skew_63d},
    "frac_481_multi_scale_vol_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_481_multi_scale_vol_kurt_63d},
    "frac_482_multi_scale_vol_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_482_multi_scale_vol_skew_126d},
    "frac_483_multi_scale_vol_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_483_multi_scale_vol_kurt_126d},
    "frac_484_multi_scale_vol_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_484_multi_scale_vol_skew_252d},
    "frac_485_multi_scale_vol_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_485_multi_scale_vol_kurt_252d},
    "frac_486_fractal_regime_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_486_fractal_regime_skew_5d},
    "frac_487_fractal_regime_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_487_fractal_regime_kurt_5d},
    "frac_488_fractal_regime_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_488_fractal_regime_skew_21d},
    "frac_489_fractal_regime_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_489_fractal_regime_kurt_21d},
    "frac_490_fractal_regime_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_490_fractal_regime_skew_63d},
    "frac_491_fractal_regime_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_491_fractal_regime_kurt_63d},
    "frac_492_fractal_regime_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_492_fractal_regime_skew_126d},
    "frac_493_fractal_regime_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_493_fractal_regime_kurt_126d},
    "frac_494_fractal_regime_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_494_fractal_regime_skew_252d},
    "frac_495_fractal_regime_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_495_fractal_regime_kurt_252d},
    "frac_496_box_counting_proxy_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_496_box_counting_proxy_skew_5d},
    "frac_497_box_counting_proxy_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_497_box_counting_proxy_kurt_5d},
    "frac_498_box_counting_proxy_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_498_box_counting_proxy_skew_21d},
    "frac_499_box_counting_proxy_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_499_box_counting_proxy_kurt_21d},
    "frac_500_box_counting_proxy_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_500_box_counting_proxy_skew_63d},
    "frac_501_box_counting_proxy_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_501_box_counting_proxy_kurt_63d},
    "frac_502_box_counting_proxy_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_502_box_counting_proxy_skew_126d},
    "frac_503_box_counting_proxy_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_503_box_counting_proxy_kurt_126d},
    "frac_504_box_counting_proxy_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_504_box_counting_proxy_skew_252d},
    "frac_505_box_counting_proxy_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_505_box_counting_proxy_kurt_252d},
    "frac_506_fractal_trend_index_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_506_fractal_trend_index_skew_5d},
    "frac_507_fractal_trend_index_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_507_fractal_trend_index_kurt_5d},
    "frac_508_fractal_trend_index_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_508_fractal_trend_index_skew_21d},
    "frac_509_fractal_trend_index_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_509_fractal_trend_index_kurt_21d},
    "frac_510_fractal_trend_index_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_510_fractal_trend_index_skew_63d},
    "frac_511_fractal_trend_index_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_511_fractal_trend_index_kurt_63d},
    "frac_512_fractal_trend_index_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_512_fractal_trend_index_skew_126d},
    "frac_513_fractal_trend_index_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_513_fractal_trend_index_kurt_126d},
    "frac_514_fractal_trend_index_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_514_fractal_trend_index_skew_252d},
    "frac_515_fractal_trend_index_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_515_fractal_trend_index_kurt_252d},
    "frac_516_fractal_noise_ratio_skew_5d": {"inputs": ["close", "high", "low"], "func": frac_516_fractal_noise_ratio_skew_5d},
    "frac_517_fractal_noise_ratio_kurt_5d": {"inputs": ["close", "high", "low"], "func": frac_517_fractal_noise_ratio_kurt_5d},
    "frac_518_fractal_noise_ratio_skew_21d": {"inputs": ["close", "high", "low"], "func": frac_518_fractal_noise_ratio_skew_21d},
    "frac_519_fractal_noise_ratio_kurt_21d": {"inputs": ["close", "high", "low"], "func": frac_519_fractal_noise_ratio_kurt_21d},
    "frac_520_fractal_noise_ratio_skew_63d": {"inputs": ["close", "high", "low"], "func": frac_520_fractal_noise_ratio_skew_63d},
    "frac_521_fractal_noise_ratio_kurt_63d": {"inputs": ["close", "high", "low"], "func": frac_521_fractal_noise_ratio_kurt_63d},
    "frac_522_fractal_noise_ratio_skew_126d": {"inputs": ["close", "high", "low"], "func": frac_522_fractal_noise_ratio_skew_126d},
    "frac_523_fractal_noise_ratio_kurt_126d": {"inputs": ["close", "high", "low"], "func": frac_523_fractal_noise_ratio_kurt_126d},
    "frac_524_fractal_noise_ratio_skew_252d": {"inputs": ["close", "high", "low"], "func": frac_524_fractal_noise_ratio_skew_252d},
    "frac_525_fractal_noise_ratio_kurt_252d": {"inputs": ["close", "high", "low"], "func": frac_525_fractal_noise_ratio_kurt_252d},
}
