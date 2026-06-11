"""
105_fractal_structure — Base Features Part 1
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

def frac_001_hurst_exponent_proxy_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_001_hurst_exponent_proxy_lvl_5d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rolling_mean(base, 5)

def frac_002_hurst_exponent_proxy_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_002_hurst_exponent_proxy_zscore_5d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _zscore_rolling(base, 5)

def frac_003_hurst_exponent_proxy_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_003_hurst_exponent_proxy_rank_5d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rank_pct(base, 5)

def frac_004_hurst_exponent_proxy_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_004_hurst_exponent_proxy_lvl_21d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rolling_mean(base, 21)

def frac_005_hurst_exponent_proxy_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_005_hurst_exponent_proxy_zscore_21d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _zscore_rolling(base, 21)

def frac_006_hurst_exponent_proxy_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_006_hurst_exponent_proxy_rank_21d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rank_pct(base, 21)

def frac_007_hurst_exponent_proxy_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_007_hurst_exponent_proxy_lvl_63d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rolling_mean(base, 63)

def frac_008_hurst_exponent_proxy_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_008_hurst_exponent_proxy_zscore_63d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _zscore_rolling(base, 63)

def frac_009_hurst_exponent_proxy_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_009_hurst_exponent_proxy_rank_63d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rank_pct(base, 63)

def frac_010_hurst_exponent_proxy_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_010_hurst_exponent_proxy_lvl_126d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rolling_mean(base, 126)

def frac_011_hurst_exponent_proxy_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_011_hurst_exponent_proxy_zscore_126d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _zscore_rolling(base, 126)

def frac_012_hurst_exponent_proxy_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_012_hurst_exponent_proxy_rank_126d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rank_pct(base, 126)

def frac_013_hurst_exponent_proxy_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_013_hurst_exponent_proxy_lvl_252d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rolling_mean(base, 252)

def frac_014_hurst_exponent_proxy_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_014_hurst_exponent_proxy_zscore_252d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _zscore_rolling(base, 252)

def frac_015_hurst_exponent_proxy_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_015_hurst_exponent_proxy_rank_252d
    ECONOMIC RATIONALE: Simplified Hurst exponent for trend persistence.
    """
    base = np.log(high.rolling(21).max() - low.rolling(21).min()) / np.log(21)
    return _rank_pct(base, 252)

def frac_016_fractal_dimension_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_016_fractal_dimension_lvl_5d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rolling_mean(base, 5)

def frac_017_fractal_dimension_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_017_fractal_dimension_zscore_5d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _zscore_rolling(base, 5)

def frac_018_fractal_dimension_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_018_fractal_dimension_rank_5d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rank_pct(base, 5)

def frac_019_fractal_dimension_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_019_fractal_dimension_lvl_21d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rolling_mean(base, 21)

def frac_020_fractal_dimension_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_020_fractal_dimension_zscore_21d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _zscore_rolling(base, 21)

def frac_021_fractal_dimension_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_021_fractal_dimension_rank_21d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rank_pct(base, 21)

def frac_022_fractal_dimension_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_022_fractal_dimension_lvl_63d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rolling_mean(base, 63)

def frac_023_fractal_dimension_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_023_fractal_dimension_zscore_63d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _zscore_rolling(base, 63)

def frac_024_fractal_dimension_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_024_fractal_dimension_rank_63d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rank_pct(base, 63)

def frac_025_fractal_dimension_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_025_fractal_dimension_lvl_126d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rolling_mean(base, 126)

def frac_026_fractal_dimension_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_026_fractal_dimension_zscore_126d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _zscore_rolling(base, 126)

def frac_027_fractal_dimension_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_027_fractal_dimension_rank_126d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rank_pct(base, 126)

def frac_028_fractal_dimension_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_028_fractal_dimension_lvl_252d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rolling_mean(base, 252)

def frac_029_fractal_dimension_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_029_fractal_dimension_zscore_252d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _zscore_rolling(base, 252)

def frac_030_fractal_dimension_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_030_fractal_dimension_rank_252d
    ECONOMIC RATIONALE: Estimated fractal dimension.
    """
    base = (np.log(high.rolling(21).max() - low.rolling(21).min()) - np.log(high.rolling(5).max() - low.rolling(5).min())) / np.log(21/5)
    return _rank_pct(base, 252)

def frac_031_efficiency_ratio_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_031_efficiency_ratio_lvl_5d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def frac_032_efficiency_ratio_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_032_efficiency_ratio_zscore_5d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def frac_033_efficiency_ratio_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_033_efficiency_ratio_rank_5d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def frac_034_efficiency_ratio_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_034_efficiency_ratio_lvl_21d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def frac_035_efficiency_ratio_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_035_efficiency_ratio_zscore_21d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def frac_036_efficiency_ratio_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_036_efficiency_ratio_rank_21d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def frac_037_efficiency_ratio_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_037_efficiency_ratio_lvl_63d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def frac_038_efficiency_ratio_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_038_efficiency_ratio_zscore_63d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def frac_039_efficiency_ratio_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_039_efficiency_ratio_rank_63d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def frac_040_efficiency_ratio_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_040_efficiency_ratio_lvl_126d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def frac_041_efficiency_ratio_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_041_efficiency_ratio_zscore_126d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def frac_042_efficiency_ratio_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_042_efficiency_ratio_rank_126d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def frac_043_efficiency_ratio_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_043_efficiency_ratio_lvl_252d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def frac_044_efficiency_ratio_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_044_efficiency_ratio_zscore_252d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def frac_045_efficiency_ratio_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_045_efficiency_ratio_rank_252d
    ECONOMIC RATIONALE: Kaufman's Efficiency Ratio.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def frac_046_fractal_volatility_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_046_fractal_volatility_lvl_5d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def frac_047_fractal_volatility_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_047_fractal_volatility_zscore_5d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def frac_048_fractal_volatility_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_048_fractal_volatility_rank_5d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def frac_049_fractal_volatility_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_049_fractal_volatility_lvl_21d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def frac_050_fractal_volatility_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_050_fractal_volatility_zscore_21d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def frac_051_fractal_volatility_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_051_fractal_volatility_rank_21d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def frac_052_fractal_volatility_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_052_fractal_volatility_lvl_63d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def frac_053_fractal_volatility_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_053_fractal_volatility_zscore_63d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def frac_054_fractal_volatility_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_054_fractal_volatility_rank_63d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def frac_055_fractal_volatility_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_055_fractal_volatility_lvl_126d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def frac_056_fractal_volatility_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_056_fractal_volatility_zscore_126d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def frac_057_fractal_volatility_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_057_fractal_volatility_rank_126d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def frac_058_fractal_volatility_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_058_fractal_volatility_lvl_252d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def frac_059_fractal_volatility_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_059_fractal_volatility_zscore_252d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def frac_060_fractal_volatility_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_060_fractal_volatility_rank_252d
    ECONOMIC RATIONALE: Complexity of price path relative to range.
    """
    base = close.diff(1).abs().rolling(63).sum() / (high.rolling(63).max() - low.rolling(63).min()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def frac_061_self_similarity_score_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_061_self_similarity_score_lvl_5d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rolling_mean(base, 5)

def frac_062_self_similarity_score_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_062_self_similarity_score_zscore_5d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _zscore_rolling(base, 5)

def frac_063_self_similarity_score_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_063_self_similarity_score_rank_5d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rank_pct(base, 5)

def frac_064_self_similarity_score_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_064_self_similarity_score_lvl_21d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rolling_mean(base, 21)

def frac_065_self_similarity_score_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_065_self_similarity_score_zscore_21d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _zscore_rolling(base, 21)

def frac_066_self_similarity_score_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_066_self_similarity_score_rank_21d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rank_pct(base, 21)

def frac_067_self_similarity_score_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_067_self_similarity_score_lvl_63d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rolling_mean(base, 63)

def frac_068_self_similarity_score_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_068_self_similarity_score_zscore_63d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _zscore_rolling(base, 63)

def frac_069_self_similarity_score_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_069_self_similarity_score_rank_63d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rank_pct(base, 63)

def frac_070_self_similarity_score_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_070_self_similarity_score_lvl_126d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rolling_mean(base, 126)

def frac_071_self_similarity_score_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_071_self_similarity_score_zscore_126d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _zscore_rolling(base, 126)

def frac_072_self_similarity_score_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_072_self_similarity_score_rank_126d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rank_pct(base, 126)

def frac_073_self_similarity_score_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_073_self_similarity_score_lvl_252d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rolling_mean(base, 252)

def frac_074_self_similarity_score_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_074_self_similarity_score_zscore_252d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _zscore_rolling(base, 252)

def frac_075_self_similarity_score_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_075_self_similarity_score_rank_252d
    ECONOMIC RATIONALE: Correlation of returns with lagged returns.
    """
    base = close.pct_change(5).rolling(21).corr(close.pct_change(5).shift(5))
    return _rank_pct(base, 252)

def frac_076_fractal_breakout_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_076_fractal_breakout_lvl_5d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rolling_mean(base, 5)

def frac_077_fractal_breakout_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_077_fractal_breakout_zscore_5d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _zscore_rolling(base, 5)

def frac_078_fractal_breakout_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_078_fractal_breakout_rank_5d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rank_pct(base, 5)

def frac_079_fractal_breakout_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_079_fractal_breakout_lvl_21d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rolling_mean(base, 21)

def frac_080_fractal_breakout_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_080_fractal_breakout_zscore_21d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _zscore_rolling(base, 21)

def frac_081_fractal_breakout_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_081_fractal_breakout_rank_21d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rank_pct(base, 21)

def frac_082_fractal_breakout_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_082_fractal_breakout_lvl_63d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rolling_mean(base, 63)

def frac_083_fractal_breakout_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_083_fractal_breakout_zscore_63d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _zscore_rolling(base, 63)

def frac_084_fractal_breakout_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_084_fractal_breakout_rank_63d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rank_pct(base, 63)

def frac_085_fractal_breakout_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_085_fractal_breakout_lvl_126d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rolling_mean(base, 126)

def frac_086_fractal_breakout_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_086_fractal_breakout_zscore_126d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _zscore_rolling(base, 126)

def frac_087_fractal_breakout_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_087_fractal_breakout_rank_126d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rank_pct(base, 126)

def frac_088_fractal_breakout_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_088_fractal_breakout_lvl_252d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rolling_mean(base, 252)

def frac_089_fractal_breakout_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_089_fractal_breakout_zscore_252d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _zscore_rolling(base, 252)

def frac_090_fractal_breakout_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_090_fractal_breakout_rank_252d
    ECONOMIC RATIONALE: Breakout of local fractal peaks.
    """
    base = (high > high.rolling(20).max().shift(1)).astype(float)
    return _rank_pct(base, 252)

def frac_091_fractal_support_violation_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_091_fractal_support_violation_lvl_5d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rolling_mean(base, 5)

def frac_092_fractal_support_violation_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_092_fractal_support_violation_zscore_5d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _zscore_rolling(base, 5)

def frac_093_fractal_support_violation_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_093_fractal_support_violation_rank_5d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rank_pct(base, 5)

def frac_094_fractal_support_violation_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_094_fractal_support_violation_lvl_21d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rolling_mean(base, 21)

def frac_095_fractal_support_violation_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_095_fractal_support_violation_zscore_21d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _zscore_rolling(base, 21)

def frac_096_fractal_support_violation_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_096_fractal_support_violation_rank_21d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rank_pct(base, 21)

def frac_097_fractal_support_violation_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_097_fractal_support_violation_lvl_63d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rolling_mean(base, 63)

def frac_098_fractal_support_violation_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_098_fractal_support_violation_zscore_63d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _zscore_rolling(base, 63)

def frac_099_fractal_support_violation_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_099_fractal_support_violation_rank_63d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rank_pct(base, 63)

def frac_100_fractal_support_violation_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_100_fractal_support_violation_lvl_126d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rolling_mean(base, 126)

def frac_101_fractal_support_violation_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_101_fractal_support_violation_zscore_126d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _zscore_rolling(base, 126)

def frac_102_fractal_support_violation_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_102_fractal_support_violation_rank_126d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rank_pct(base, 126)

def frac_103_fractal_support_violation_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_103_fractal_support_violation_lvl_252d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rolling_mean(base, 252)

def frac_104_fractal_support_violation_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_104_fractal_support_violation_zscore_252d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _zscore_rolling(base, 252)

def frac_105_fractal_support_violation_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_105_fractal_support_violation_rank_252d
    ECONOMIC RATIONALE: Breakdown of local fractal troughs.
    """
    base = (low < low.rolling(20).min().shift(1)).astype(float)
    return _rank_pct(base, 252)

def frac_106_chaos_theory_osc_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_106_chaos_theory_osc_lvl_5d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rolling_mean(base, 5)

def frac_107_chaos_theory_osc_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_107_chaos_theory_osc_zscore_5d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _zscore_rolling(base, 5)

def frac_108_chaos_theory_osc_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_108_chaos_theory_osc_rank_5d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rank_pct(base, 5)

def frac_109_chaos_theory_osc_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_109_chaos_theory_osc_lvl_21d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rolling_mean(base, 21)

def frac_110_chaos_theory_osc_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_110_chaos_theory_osc_zscore_21d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _zscore_rolling(base, 21)

def frac_111_chaos_theory_osc_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_111_chaos_theory_osc_rank_21d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rank_pct(base, 21)

def frac_112_chaos_theory_osc_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_112_chaos_theory_osc_lvl_63d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rolling_mean(base, 63)

def frac_113_chaos_theory_osc_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_113_chaos_theory_osc_zscore_63d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _zscore_rolling(base, 63)

def frac_114_chaos_theory_osc_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_114_chaos_theory_osc_rank_63d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rank_pct(base, 63)

def frac_115_chaos_theory_osc_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_115_chaos_theory_osc_lvl_126d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rolling_mean(base, 126)

def frac_116_chaos_theory_osc_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_116_chaos_theory_osc_zscore_126d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _zscore_rolling(base, 126)

def frac_117_chaos_theory_osc_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_117_chaos_theory_osc_rank_126d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rank_pct(base, 126)

def frac_118_chaos_theory_osc_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_118_chaos_theory_osc_lvl_252d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rolling_mean(base, 252)

def frac_119_chaos_theory_osc_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_119_chaos_theory_osc_zscore_252d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _zscore_rolling(base, 252)

def frac_120_chaos_theory_osc_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    frac_120_chaos_theory_osc_rank_252d
    ECONOMIC RATIONALE: Noise-adjusted short-term momentum.
    """
    base = close.pct_change(1) / close.pct_change(5).rolling(21).std()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V105_REGISTRY_1 = {
    "frac_001_hurst_exponent_proxy_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_001_hurst_exponent_proxy_lvl_5d},
    "frac_002_hurst_exponent_proxy_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_002_hurst_exponent_proxy_zscore_5d},
    "frac_003_hurst_exponent_proxy_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_003_hurst_exponent_proxy_rank_5d},
    "frac_004_hurst_exponent_proxy_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_004_hurst_exponent_proxy_lvl_21d},
    "frac_005_hurst_exponent_proxy_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_005_hurst_exponent_proxy_zscore_21d},
    "frac_006_hurst_exponent_proxy_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_006_hurst_exponent_proxy_rank_21d},
    "frac_007_hurst_exponent_proxy_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_007_hurst_exponent_proxy_lvl_63d},
    "frac_008_hurst_exponent_proxy_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_008_hurst_exponent_proxy_zscore_63d},
    "frac_009_hurst_exponent_proxy_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_009_hurst_exponent_proxy_rank_63d},
    "frac_010_hurst_exponent_proxy_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_010_hurst_exponent_proxy_lvl_126d},
    "frac_011_hurst_exponent_proxy_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_011_hurst_exponent_proxy_zscore_126d},
    "frac_012_hurst_exponent_proxy_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_012_hurst_exponent_proxy_rank_126d},
    "frac_013_hurst_exponent_proxy_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_013_hurst_exponent_proxy_lvl_252d},
    "frac_014_hurst_exponent_proxy_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_014_hurst_exponent_proxy_zscore_252d},
    "frac_015_hurst_exponent_proxy_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_015_hurst_exponent_proxy_rank_252d},
    "frac_016_fractal_dimension_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_016_fractal_dimension_lvl_5d},
    "frac_017_fractal_dimension_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_017_fractal_dimension_zscore_5d},
    "frac_018_fractal_dimension_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_018_fractal_dimension_rank_5d},
    "frac_019_fractal_dimension_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_019_fractal_dimension_lvl_21d},
    "frac_020_fractal_dimension_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_020_fractal_dimension_zscore_21d},
    "frac_021_fractal_dimension_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_021_fractal_dimension_rank_21d},
    "frac_022_fractal_dimension_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_022_fractal_dimension_lvl_63d},
    "frac_023_fractal_dimension_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_023_fractal_dimension_zscore_63d},
    "frac_024_fractal_dimension_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_024_fractal_dimension_rank_63d},
    "frac_025_fractal_dimension_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_025_fractal_dimension_lvl_126d},
    "frac_026_fractal_dimension_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_026_fractal_dimension_zscore_126d},
    "frac_027_fractal_dimension_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_027_fractal_dimension_rank_126d},
    "frac_028_fractal_dimension_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_028_fractal_dimension_lvl_252d},
    "frac_029_fractal_dimension_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_029_fractal_dimension_zscore_252d},
    "frac_030_fractal_dimension_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_030_fractal_dimension_rank_252d},
    "frac_031_efficiency_ratio_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_031_efficiency_ratio_lvl_5d},
    "frac_032_efficiency_ratio_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_032_efficiency_ratio_zscore_5d},
    "frac_033_efficiency_ratio_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_033_efficiency_ratio_rank_5d},
    "frac_034_efficiency_ratio_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_034_efficiency_ratio_lvl_21d},
    "frac_035_efficiency_ratio_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_035_efficiency_ratio_zscore_21d},
    "frac_036_efficiency_ratio_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_036_efficiency_ratio_rank_21d},
    "frac_037_efficiency_ratio_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_037_efficiency_ratio_lvl_63d},
    "frac_038_efficiency_ratio_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_038_efficiency_ratio_zscore_63d},
    "frac_039_efficiency_ratio_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_039_efficiency_ratio_rank_63d},
    "frac_040_efficiency_ratio_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_040_efficiency_ratio_lvl_126d},
    "frac_041_efficiency_ratio_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_041_efficiency_ratio_zscore_126d},
    "frac_042_efficiency_ratio_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_042_efficiency_ratio_rank_126d},
    "frac_043_efficiency_ratio_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_043_efficiency_ratio_lvl_252d},
    "frac_044_efficiency_ratio_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_044_efficiency_ratio_zscore_252d},
    "frac_045_efficiency_ratio_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_045_efficiency_ratio_rank_252d},
    "frac_046_fractal_volatility_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_046_fractal_volatility_lvl_5d},
    "frac_047_fractal_volatility_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_047_fractal_volatility_zscore_5d},
    "frac_048_fractal_volatility_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_048_fractal_volatility_rank_5d},
    "frac_049_fractal_volatility_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_049_fractal_volatility_lvl_21d},
    "frac_050_fractal_volatility_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_050_fractal_volatility_zscore_21d},
    "frac_051_fractal_volatility_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_051_fractal_volatility_rank_21d},
    "frac_052_fractal_volatility_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_052_fractal_volatility_lvl_63d},
    "frac_053_fractal_volatility_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_053_fractal_volatility_zscore_63d},
    "frac_054_fractal_volatility_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_054_fractal_volatility_rank_63d},
    "frac_055_fractal_volatility_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_055_fractal_volatility_lvl_126d},
    "frac_056_fractal_volatility_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_056_fractal_volatility_zscore_126d},
    "frac_057_fractal_volatility_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_057_fractal_volatility_rank_126d},
    "frac_058_fractal_volatility_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_058_fractal_volatility_lvl_252d},
    "frac_059_fractal_volatility_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_059_fractal_volatility_zscore_252d},
    "frac_060_fractal_volatility_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_060_fractal_volatility_rank_252d},
    "frac_061_self_similarity_score_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_061_self_similarity_score_lvl_5d},
    "frac_062_self_similarity_score_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_062_self_similarity_score_zscore_5d},
    "frac_063_self_similarity_score_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_063_self_similarity_score_rank_5d},
    "frac_064_self_similarity_score_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_064_self_similarity_score_lvl_21d},
    "frac_065_self_similarity_score_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_065_self_similarity_score_zscore_21d},
    "frac_066_self_similarity_score_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_066_self_similarity_score_rank_21d},
    "frac_067_self_similarity_score_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_067_self_similarity_score_lvl_63d},
    "frac_068_self_similarity_score_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_068_self_similarity_score_zscore_63d},
    "frac_069_self_similarity_score_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_069_self_similarity_score_rank_63d},
    "frac_070_self_similarity_score_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_070_self_similarity_score_lvl_126d},
    "frac_071_self_similarity_score_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_071_self_similarity_score_zscore_126d},
    "frac_072_self_similarity_score_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_072_self_similarity_score_rank_126d},
    "frac_073_self_similarity_score_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_073_self_similarity_score_lvl_252d},
    "frac_074_self_similarity_score_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_074_self_similarity_score_zscore_252d},
    "frac_075_self_similarity_score_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_075_self_similarity_score_rank_252d},
    "frac_076_fractal_breakout_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_076_fractal_breakout_lvl_5d},
    "frac_077_fractal_breakout_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_077_fractal_breakout_zscore_5d},
    "frac_078_fractal_breakout_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_078_fractal_breakout_rank_5d},
    "frac_079_fractal_breakout_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_079_fractal_breakout_lvl_21d},
    "frac_080_fractal_breakout_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_080_fractal_breakout_zscore_21d},
    "frac_081_fractal_breakout_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_081_fractal_breakout_rank_21d},
    "frac_082_fractal_breakout_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_082_fractal_breakout_lvl_63d},
    "frac_083_fractal_breakout_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_083_fractal_breakout_zscore_63d},
    "frac_084_fractal_breakout_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_084_fractal_breakout_rank_63d},
    "frac_085_fractal_breakout_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_085_fractal_breakout_lvl_126d},
    "frac_086_fractal_breakout_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_086_fractal_breakout_zscore_126d},
    "frac_087_fractal_breakout_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_087_fractal_breakout_rank_126d},
    "frac_088_fractal_breakout_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_088_fractal_breakout_lvl_252d},
    "frac_089_fractal_breakout_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_089_fractal_breakout_zscore_252d},
    "frac_090_fractal_breakout_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_090_fractal_breakout_rank_252d},
    "frac_091_fractal_support_violation_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_091_fractal_support_violation_lvl_5d},
    "frac_092_fractal_support_violation_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_092_fractal_support_violation_zscore_5d},
    "frac_093_fractal_support_violation_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_093_fractal_support_violation_rank_5d},
    "frac_094_fractal_support_violation_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_094_fractal_support_violation_lvl_21d},
    "frac_095_fractal_support_violation_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_095_fractal_support_violation_zscore_21d},
    "frac_096_fractal_support_violation_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_096_fractal_support_violation_rank_21d},
    "frac_097_fractal_support_violation_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_097_fractal_support_violation_lvl_63d},
    "frac_098_fractal_support_violation_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_098_fractal_support_violation_zscore_63d},
    "frac_099_fractal_support_violation_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_099_fractal_support_violation_rank_63d},
    "frac_100_fractal_support_violation_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_100_fractal_support_violation_lvl_126d},
    "frac_101_fractal_support_violation_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_101_fractal_support_violation_zscore_126d},
    "frac_102_fractal_support_violation_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_102_fractal_support_violation_rank_126d},
    "frac_103_fractal_support_violation_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_103_fractal_support_violation_lvl_252d},
    "frac_104_fractal_support_violation_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_104_fractal_support_violation_zscore_252d},
    "frac_105_fractal_support_violation_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_105_fractal_support_violation_rank_252d},
    "frac_106_chaos_theory_osc_lvl_5d": {"inputs": ["close", "high", "low"], "func": frac_106_chaos_theory_osc_lvl_5d},
    "frac_107_chaos_theory_osc_zscore_5d": {"inputs": ["close", "high", "low"], "func": frac_107_chaos_theory_osc_zscore_5d},
    "frac_108_chaos_theory_osc_rank_5d": {"inputs": ["close", "high", "low"], "func": frac_108_chaos_theory_osc_rank_5d},
    "frac_109_chaos_theory_osc_lvl_21d": {"inputs": ["close", "high", "low"], "func": frac_109_chaos_theory_osc_lvl_21d},
    "frac_110_chaos_theory_osc_zscore_21d": {"inputs": ["close", "high", "low"], "func": frac_110_chaos_theory_osc_zscore_21d},
    "frac_111_chaos_theory_osc_rank_21d": {"inputs": ["close", "high", "low"], "func": frac_111_chaos_theory_osc_rank_21d},
    "frac_112_chaos_theory_osc_lvl_63d": {"inputs": ["close", "high", "low"], "func": frac_112_chaos_theory_osc_lvl_63d},
    "frac_113_chaos_theory_osc_zscore_63d": {"inputs": ["close", "high", "low"], "func": frac_113_chaos_theory_osc_zscore_63d},
    "frac_114_chaos_theory_osc_rank_63d": {"inputs": ["close", "high", "low"], "func": frac_114_chaos_theory_osc_rank_63d},
    "frac_115_chaos_theory_osc_lvl_126d": {"inputs": ["close", "high", "low"], "func": frac_115_chaos_theory_osc_lvl_126d},
    "frac_116_chaos_theory_osc_zscore_126d": {"inputs": ["close", "high", "low"], "func": frac_116_chaos_theory_osc_zscore_126d},
    "frac_117_chaos_theory_osc_rank_126d": {"inputs": ["close", "high", "low"], "func": frac_117_chaos_theory_osc_rank_126d},
    "frac_118_chaos_theory_osc_lvl_252d": {"inputs": ["close", "high", "low"], "func": frac_118_chaos_theory_osc_lvl_252d},
    "frac_119_chaos_theory_osc_zscore_252d": {"inputs": ["close", "high", "low"], "func": frac_119_chaos_theory_osc_zscore_252d},
    "frac_120_chaos_theory_osc_rank_252d": {"inputs": ["close", "high", "low"], "func": frac_120_chaos_theory_osc_rank_252d},
}
