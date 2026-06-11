"""
95_vort_dynamics — Base Features 001-075
Domain: vort_dynamics
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

def vort_001_vi_plus_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_001_vi_plus_lvl_5d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 5)

def vort_002_vi_plus_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_002_vi_plus_zscore_5d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 5)

def vort_003_vi_plus_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_003_vi_plus_rank_5d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 5)

def vort_004_vi_plus_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_004_vi_plus_lvl_21d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 21)

def vort_005_vi_plus_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_005_vi_plus_zscore_21d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 21)

def vort_006_vi_plus_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_006_vi_plus_rank_21d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 21)

def vort_007_vi_plus_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_007_vi_plus_lvl_63d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 63)

def vort_008_vi_plus_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_008_vi_plus_zscore_63d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 63)

def vort_009_vi_plus_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_009_vi_plus_rank_63d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 63)

def vort_010_vi_plus_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_010_vi_plus_lvl_126d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 126)

def vort_011_vi_plus_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_011_vi_plus_zscore_126d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 126)

def vort_012_vi_plus_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_012_vi_plus_rank_126d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 126)

def vort_013_vi_plus_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_013_vi_plus_lvl_252d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 252)

def vort_014_vi_plus_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_014_vi_plus_zscore_252d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 252)

def vort_015_vi_plus_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_015_vi_plus_rank_252d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 252)

def vort_016_vi_minus_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_016_vi_minus_lvl_5d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 5)

def vort_017_vi_minus_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_017_vi_minus_zscore_5d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 5)

def vort_018_vi_minus_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_018_vi_minus_rank_5d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 5)

def vort_019_vi_minus_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_019_vi_minus_lvl_21d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 21)

def vort_020_vi_minus_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_020_vi_minus_zscore_21d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 21)

def vort_021_vi_minus_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_021_vi_minus_rank_21d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 21)

def vort_022_vi_minus_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_022_vi_minus_lvl_63d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 63)

def vort_023_vi_minus_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_023_vi_minus_zscore_63d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 63)

def vort_024_vi_minus_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_024_vi_minus_rank_63d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 63)

def vort_025_vi_minus_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_025_vi_minus_lvl_126d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 126)

def vort_026_vi_minus_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_026_vi_minus_zscore_126d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 126)

def vort_027_vi_minus_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_027_vi_minus_rank_126d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 126)

def vort_028_vi_minus_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_028_vi_minus_lvl_252d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 252)

def vort_029_vi_minus_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_029_vi_minus_zscore_252d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 252)

def vort_030_vi_minus_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_030_vi_minus_rank_252d"""
    base = _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 252)

def vort_031_vi_diff_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_031_vi_diff_lvl_5d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 5)

def vort_032_vi_diff_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_032_vi_diff_zscore_5d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 5)

def vort_033_vi_diff_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_033_vi_diff_rank_5d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 5)

def vort_034_vi_diff_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_034_vi_diff_lvl_21d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 21)

def vort_035_vi_diff_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_035_vi_diff_zscore_21d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 21)

def vort_036_vi_diff_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_036_vi_diff_rank_21d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 21)

def vort_037_vi_diff_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_037_vi_diff_lvl_63d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 63)

def vort_038_vi_diff_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_038_vi_diff_zscore_63d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 63)

def vort_039_vi_diff_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_039_vi_diff_rank_63d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 63)

def vort_040_vi_diff_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_040_vi_diff_lvl_126d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 126)

def vort_041_vi_diff_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_041_vi_diff_zscore_126d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 126)

def vort_042_vi_diff_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_042_vi_diff_rank_126d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 126)

def vort_043_vi_diff_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_043_vi_diff_lvl_252d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rolling_mean(base, 252)

def vort_044_vi_diff_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_044_vi_diff_zscore_252d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _zscore_rolling(base, 252)

def vort_045_vi_diff_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_045_vi_diff_rank_252d"""
    base = _safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))
    return _rank_pct(base, 252)

def vort_046_vi_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_046_vi_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rolling_mean(base, 5)

def vort_047_vi_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_047_vi_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _zscore_rolling(base, 5)

def vort_048_vi_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_048_vi_z_rank_5d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rank_pct(base, 5)

def vort_049_vi_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_049_vi_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rolling_mean(base, 21)

def vort_050_vi_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_050_vi_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _zscore_rolling(base, 21)

def vort_051_vi_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_051_vi_z_rank_21d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rank_pct(base, 21)

def vort_052_vi_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_052_vi_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rolling_mean(base, 63)

def vort_053_vi_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_053_vi_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _zscore_rolling(base, 63)

def vort_054_vi_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_054_vi_z_rank_63d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rank_pct(base, 63)

def vort_055_vi_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_055_vi_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rolling_mean(base, 126)

def vort_056_vi_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_056_vi_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _zscore_rolling(base, 126)

def vort_057_vi_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_057_vi_z_rank_126d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rank_pct(base, 126)

def vort_058_vi_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_058_vi_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rolling_mean(base, 252)

def vort_059_vi_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_059_vi_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _zscore_rolling(base, 252)

def vort_060_vi_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_060_vi_z_rank_252d"""
    base = _zscore_rolling(_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)), 63)
    return _rank_pct(base, 252)

def vort_061_vi_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_061_vi_roc_lvl_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 5)

def vort_062_vi_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_062_vi_roc_zscore_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 5)

def vort_063_vi_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_063_vi_roc_rank_5d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 5)

def vort_064_vi_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_064_vi_roc_lvl_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 21)

def vort_065_vi_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_065_vi_roc_zscore_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 21)

def vort_066_vi_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_066_vi_roc_rank_21d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 21)

def vort_067_vi_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_067_vi_roc_lvl_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 63)

def vort_068_vi_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_068_vi_roc_zscore_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 63)

def vort_069_vi_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_069_vi_roc_rank_63d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 63)

def vort_070_vi_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_070_vi_roc_lvl_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 126)

def vort_071_vi_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_071_vi_roc_zscore_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 126)

def vort_072_vi_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_072_vi_roc_rank_126d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 126)

def vort_073_vi_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_073_vi_roc_lvl_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rolling_mean(base, 252)

def vort_074_vi_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_074_vi_roc_zscore_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _zscore_rolling(base, 252)

def vort_075_vi_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vort_075_vi_roc_rank_252d"""
    base = (_safe_div(_rolling_mean((high - low.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14)) - _safe_div(_rolling_mean((low - high.shift(1)).abs(), 14), _rolling_mean(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), 14))).pct_change()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V95_REGISTRY = {
    "vort_001_vi_plus_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_001_vi_plus_lvl_5d},
    "vort_002_vi_plus_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_002_vi_plus_zscore_5d},
    "vort_003_vi_plus_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_003_vi_plus_rank_5d},
    "vort_004_vi_plus_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_004_vi_plus_lvl_21d},
    "vort_005_vi_plus_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_005_vi_plus_zscore_21d},
    "vort_006_vi_plus_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_006_vi_plus_rank_21d},
    "vort_007_vi_plus_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_007_vi_plus_lvl_63d},
    "vort_008_vi_plus_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_008_vi_plus_zscore_63d},
    "vort_009_vi_plus_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_009_vi_plus_rank_63d},
    "vort_010_vi_plus_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_010_vi_plus_lvl_126d},
    "vort_011_vi_plus_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_011_vi_plus_zscore_126d},
    "vort_012_vi_plus_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_012_vi_plus_rank_126d},
    "vort_013_vi_plus_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_013_vi_plus_lvl_252d},
    "vort_014_vi_plus_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_014_vi_plus_zscore_252d},
    "vort_015_vi_plus_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_015_vi_plus_rank_252d},
    "vort_016_vi_minus_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_016_vi_minus_lvl_5d},
    "vort_017_vi_minus_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_017_vi_minus_zscore_5d},
    "vort_018_vi_minus_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_018_vi_minus_rank_5d},
    "vort_019_vi_minus_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_019_vi_minus_lvl_21d},
    "vort_020_vi_minus_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_020_vi_minus_zscore_21d},
    "vort_021_vi_minus_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_021_vi_minus_rank_21d},
    "vort_022_vi_minus_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_022_vi_minus_lvl_63d},
    "vort_023_vi_minus_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_023_vi_minus_zscore_63d},
    "vort_024_vi_minus_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_024_vi_minus_rank_63d},
    "vort_025_vi_minus_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_025_vi_minus_lvl_126d},
    "vort_026_vi_minus_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_026_vi_minus_zscore_126d},
    "vort_027_vi_minus_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_027_vi_minus_rank_126d},
    "vort_028_vi_minus_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_028_vi_minus_lvl_252d},
    "vort_029_vi_minus_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_029_vi_minus_zscore_252d},
    "vort_030_vi_minus_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_030_vi_minus_rank_252d},
    "vort_031_vi_diff_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_031_vi_diff_lvl_5d},
    "vort_032_vi_diff_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_032_vi_diff_zscore_5d},
    "vort_033_vi_diff_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_033_vi_diff_rank_5d},
    "vort_034_vi_diff_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_034_vi_diff_lvl_21d},
    "vort_035_vi_diff_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_035_vi_diff_zscore_21d},
    "vort_036_vi_diff_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_036_vi_diff_rank_21d},
    "vort_037_vi_diff_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_037_vi_diff_lvl_63d},
    "vort_038_vi_diff_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_038_vi_diff_zscore_63d},
    "vort_039_vi_diff_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_039_vi_diff_rank_63d},
    "vort_040_vi_diff_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_040_vi_diff_lvl_126d},
    "vort_041_vi_diff_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_041_vi_diff_zscore_126d},
    "vort_042_vi_diff_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_042_vi_diff_rank_126d},
    "vort_043_vi_diff_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_043_vi_diff_lvl_252d},
    "vort_044_vi_diff_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_044_vi_diff_zscore_252d},
    "vort_045_vi_diff_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_045_vi_diff_rank_252d},
    "vort_046_vi_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_046_vi_z_lvl_5d},
    "vort_047_vi_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_047_vi_z_zscore_5d},
    "vort_048_vi_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_048_vi_z_rank_5d},
    "vort_049_vi_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_049_vi_z_lvl_21d},
    "vort_050_vi_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_050_vi_z_zscore_21d},
    "vort_051_vi_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_051_vi_z_rank_21d},
    "vort_052_vi_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_052_vi_z_lvl_63d},
    "vort_053_vi_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_053_vi_z_zscore_63d},
    "vort_054_vi_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_054_vi_z_rank_63d},
    "vort_055_vi_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_055_vi_z_lvl_126d},
    "vort_056_vi_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_056_vi_z_zscore_126d},
    "vort_057_vi_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_057_vi_z_rank_126d},
    "vort_058_vi_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_058_vi_z_lvl_252d},
    "vort_059_vi_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_059_vi_z_zscore_252d},
    "vort_060_vi_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_060_vi_z_rank_252d},
    "vort_061_vi_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_061_vi_roc_lvl_5d},
    "vort_062_vi_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_062_vi_roc_zscore_5d},
    "vort_063_vi_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": vort_063_vi_roc_rank_5d},
    "vort_064_vi_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_064_vi_roc_lvl_21d},
    "vort_065_vi_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_065_vi_roc_zscore_21d},
    "vort_066_vi_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": vort_066_vi_roc_rank_21d},
    "vort_067_vi_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_067_vi_roc_lvl_63d},
    "vort_068_vi_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_068_vi_roc_zscore_63d},
    "vort_069_vi_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": vort_069_vi_roc_rank_63d},
    "vort_070_vi_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_070_vi_roc_lvl_126d},
    "vort_071_vi_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_071_vi_roc_zscore_126d},
    "vort_072_vi_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": vort_072_vi_roc_rank_126d},
    "vort_073_vi_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_073_vi_roc_lvl_252d},
    "vort_074_vi_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_074_vi_roc_zscore_252d},
    "vort_075_vi_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": vort_075_vi_roc_rank_252d},
}
