"""
78_stoc_dynamics — Base Features 001-075
Domain: stoc_dynamics
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
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std().fillna(0)

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _rsi(s: pd.Series, w: int) -> pd.Series:
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w).mean()
    rs = _safe_div(gain, loss)
    return 100 - (100 / (1 + rs))

# ── Feature functions ────────────────────────────────────────────────────────

def stoc_001_stok_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_001_stok_lvl_5d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rolling_mean(base, 5)

def stoc_002_stok_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_002_stok_zscore_5d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _zscore_rolling(base, 5)

def stoc_003_stok_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_003_stok_rank_5d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rank_pct(base, 5)

def stoc_004_stok_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_004_stok_lvl_21d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rolling_mean(base, 21)

def stoc_005_stok_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_005_stok_zscore_21d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _zscore_rolling(base, 21)

def stoc_006_stok_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_006_stok_rank_21d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rank_pct(base, 21)

def stoc_007_stok_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_007_stok_lvl_63d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rolling_mean(base, 63)

def stoc_008_stok_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_008_stok_zscore_63d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _zscore_rolling(base, 63)

def stoc_009_stok_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_009_stok_rank_63d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rank_pct(base, 63)

def stoc_010_stok_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_010_stok_lvl_126d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rolling_mean(base, 126)

def stoc_011_stok_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_011_stok_zscore_126d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _zscore_rolling(base, 126)

def stoc_012_stok_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_012_stok_rank_126d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rank_pct(base, 126)

def stoc_013_stok_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_013_stok_lvl_252d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rolling_mean(base, 252)

def stoc_014_stok_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_014_stok_zscore_252d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _zscore_rolling(base, 252)

def stoc_015_stok_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_015_stok_rank_252d"""
    base = _safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100
    return _rank_pct(base, 252)

def stoc_016_stod_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_016_stod_lvl_5d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rolling_mean(base, 5)

def stoc_017_stod_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_017_stod_zscore_5d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _zscore_rolling(base, 5)

def stoc_018_stod_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_018_stod_rank_5d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rank_pct(base, 5)

def stoc_019_stod_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_019_stod_lvl_21d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rolling_mean(base, 21)

def stoc_020_stod_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_020_stod_zscore_21d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _zscore_rolling(base, 21)

def stoc_021_stod_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_021_stod_rank_21d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rank_pct(base, 21)

def stoc_022_stod_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_022_stod_lvl_63d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rolling_mean(base, 63)

def stoc_023_stod_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_023_stod_zscore_63d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _zscore_rolling(base, 63)

def stoc_024_stod_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_024_stod_rank_63d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rank_pct(base, 63)

def stoc_025_stod_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_025_stod_lvl_126d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rolling_mean(base, 126)

def stoc_026_stod_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_026_stod_zscore_126d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _zscore_rolling(base, 126)

def stoc_027_stod_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_027_stod_rank_126d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rank_pct(base, 126)

def stoc_028_stod_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_028_stod_lvl_252d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rolling_mean(base, 252)

def stoc_029_stod_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_029_stod_zscore_252d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _zscore_rolling(base, 252)

def stoc_030_stod_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_030_stod_rank_252d"""
    base = _rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3)
    return _rank_pct(base, 252)

def stoc_031_stod_slow_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_031_stod_slow_lvl_5d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rolling_mean(base, 5)

def stoc_032_stod_slow_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_032_stod_slow_zscore_5d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _zscore_rolling(base, 5)

def stoc_033_stod_slow_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_033_stod_slow_rank_5d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rank_pct(base, 5)

def stoc_034_stod_slow_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_034_stod_slow_lvl_21d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rolling_mean(base, 21)

def stoc_035_stod_slow_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_035_stod_slow_zscore_21d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _zscore_rolling(base, 21)

def stoc_036_stod_slow_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_036_stod_slow_rank_21d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rank_pct(base, 21)

def stoc_037_stod_slow_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_037_stod_slow_lvl_63d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rolling_mean(base, 63)

def stoc_038_stod_slow_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_038_stod_slow_zscore_63d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _zscore_rolling(base, 63)

def stoc_039_stod_slow_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_039_stod_slow_rank_63d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rank_pct(base, 63)

def stoc_040_stod_slow_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_040_stod_slow_lvl_126d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rolling_mean(base, 126)

def stoc_041_stod_slow_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_041_stod_slow_zscore_126d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _zscore_rolling(base, 126)

def stoc_042_stod_slow_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_042_stod_slow_rank_126d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rank_pct(base, 126)

def stoc_043_stod_slow_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_043_stod_slow_lvl_252d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rolling_mean(base, 252)

def stoc_044_stod_slow_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_044_stod_slow_zscore_252d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _zscore_rolling(base, 252)

def stoc_045_stod_slow_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_045_stod_slow_rank_252d"""
    base = _rolling_mean(_rolling_mean(_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100, 3), 3)
    return _rank_pct(base, 252)

def stoc_046_stoc_range_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_046_stoc_range_lvl_5d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 5)

def stoc_047_stoc_range_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_047_stoc_range_zscore_5d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 5)

def stoc_048_stoc_range_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_048_stoc_range_rank_5d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 5)

def stoc_049_stoc_range_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_049_stoc_range_lvl_21d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 21)

def stoc_050_stoc_range_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_050_stoc_range_zscore_21d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 21)

def stoc_051_stoc_range_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_051_stoc_range_rank_21d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 21)

def stoc_052_stoc_range_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_052_stoc_range_lvl_63d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 63)

def stoc_053_stoc_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_053_stoc_range_zscore_63d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 63)

def stoc_054_stoc_range_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_054_stoc_range_rank_63d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 63)

def stoc_055_stoc_range_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_055_stoc_range_lvl_126d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 126)

def stoc_056_stoc_range_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_056_stoc_range_zscore_126d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 126)

def stoc_057_stoc_range_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_057_stoc_range_rank_126d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 126)

def stoc_058_stoc_range_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_058_stoc_range_lvl_252d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rolling_mean(base, 252)

def stoc_059_stoc_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_059_stoc_range_zscore_252d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _zscore_rolling(base, 252)

def stoc_060_stoc_range_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_060_stoc_range_rank_252d"""
    base = _rolling_max(high, 14) - _rolling_min(low, 14)
    return _rank_pct(base, 252)

def stoc_061_stoc_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_061_stoc_dist_lvl_5d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rolling_mean(base, 5)

def stoc_062_stoc_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_062_stoc_dist_zscore_5d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _zscore_rolling(base, 5)

def stoc_063_stoc_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_063_stoc_dist_rank_5d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rank_pct(base, 5)

def stoc_064_stoc_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_064_stoc_dist_lvl_21d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rolling_mean(base, 21)

def stoc_065_stoc_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_065_stoc_dist_zscore_21d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _zscore_rolling(base, 21)

def stoc_066_stoc_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_066_stoc_dist_rank_21d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rank_pct(base, 21)

def stoc_067_stoc_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_067_stoc_dist_lvl_63d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rolling_mean(base, 63)

def stoc_068_stoc_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_068_stoc_dist_zscore_63d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _zscore_rolling(base, 63)

def stoc_069_stoc_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_069_stoc_dist_rank_63d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rank_pct(base, 63)

def stoc_070_stoc_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_070_stoc_dist_lvl_126d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rolling_mean(base, 126)

def stoc_071_stoc_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_071_stoc_dist_zscore_126d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _zscore_rolling(base, 126)

def stoc_072_stoc_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_072_stoc_dist_rank_126d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rank_pct(base, 126)

def stoc_073_stoc_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_073_stoc_dist_lvl_252d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rolling_mean(base, 252)

def stoc_074_stoc_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_074_stoc_dist_zscore_252d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _zscore_rolling(base, 252)

def stoc_075_stoc_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """stoc_075_stoc_dist_rank_252d"""
    base = (_safe_div(close - _rolling_min(low, 14), _rolling_max(high, 14) - _rolling_min(low, 14)) * 100) - 50
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V78_REGISTRY = {
    "stoc_001_stok_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_001_stok_lvl_5d},
    "stoc_002_stok_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_002_stok_zscore_5d},
    "stoc_003_stok_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_003_stok_rank_5d},
    "stoc_004_stok_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_004_stok_lvl_21d},
    "stoc_005_stok_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_005_stok_zscore_21d},
    "stoc_006_stok_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_006_stok_rank_21d},
    "stoc_007_stok_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_007_stok_lvl_63d},
    "stoc_008_stok_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_008_stok_zscore_63d},
    "stoc_009_stok_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_009_stok_rank_63d},
    "stoc_010_stok_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_010_stok_lvl_126d},
    "stoc_011_stok_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_011_stok_zscore_126d},
    "stoc_012_stok_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_012_stok_rank_126d},
    "stoc_013_stok_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_013_stok_lvl_252d},
    "stoc_014_stok_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_014_stok_zscore_252d},
    "stoc_015_stok_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_015_stok_rank_252d},
    "stoc_016_stod_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_016_stod_lvl_5d},
    "stoc_017_stod_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_017_stod_zscore_5d},
    "stoc_018_stod_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_018_stod_rank_5d},
    "stoc_019_stod_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_019_stod_lvl_21d},
    "stoc_020_stod_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_020_stod_zscore_21d},
    "stoc_021_stod_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_021_stod_rank_21d},
    "stoc_022_stod_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_022_stod_lvl_63d},
    "stoc_023_stod_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_023_stod_zscore_63d},
    "stoc_024_stod_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_024_stod_rank_63d},
    "stoc_025_stod_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_025_stod_lvl_126d},
    "stoc_026_stod_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_026_stod_zscore_126d},
    "stoc_027_stod_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_027_stod_rank_126d},
    "stoc_028_stod_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_028_stod_lvl_252d},
    "stoc_029_stod_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_029_stod_zscore_252d},
    "stoc_030_stod_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_030_stod_rank_252d},
    "stoc_031_stod_slow_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_031_stod_slow_lvl_5d},
    "stoc_032_stod_slow_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_032_stod_slow_zscore_5d},
    "stoc_033_stod_slow_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_033_stod_slow_rank_5d},
    "stoc_034_stod_slow_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_034_stod_slow_lvl_21d},
    "stoc_035_stod_slow_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_035_stod_slow_zscore_21d},
    "stoc_036_stod_slow_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_036_stod_slow_rank_21d},
    "stoc_037_stod_slow_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_037_stod_slow_lvl_63d},
    "stoc_038_stod_slow_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_038_stod_slow_zscore_63d},
    "stoc_039_stod_slow_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_039_stod_slow_rank_63d},
    "stoc_040_stod_slow_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_040_stod_slow_lvl_126d},
    "stoc_041_stod_slow_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_041_stod_slow_zscore_126d},
    "stoc_042_stod_slow_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_042_stod_slow_rank_126d},
    "stoc_043_stod_slow_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_043_stod_slow_lvl_252d},
    "stoc_044_stod_slow_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_044_stod_slow_zscore_252d},
    "stoc_045_stod_slow_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_045_stod_slow_rank_252d},
    "stoc_046_stoc_range_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_046_stoc_range_lvl_5d},
    "stoc_047_stoc_range_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_047_stoc_range_zscore_5d},
    "stoc_048_stoc_range_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_048_stoc_range_rank_5d},
    "stoc_049_stoc_range_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_049_stoc_range_lvl_21d},
    "stoc_050_stoc_range_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_050_stoc_range_zscore_21d},
    "stoc_051_stoc_range_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_051_stoc_range_rank_21d},
    "stoc_052_stoc_range_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_052_stoc_range_lvl_63d},
    "stoc_053_stoc_range_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_053_stoc_range_zscore_63d},
    "stoc_054_stoc_range_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_054_stoc_range_rank_63d},
    "stoc_055_stoc_range_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_055_stoc_range_lvl_126d},
    "stoc_056_stoc_range_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_056_stoc_range_zscore_126d},
    "stoc_057_stoc_range_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_057_stoc_range_rank_126d},
    "stoc_058_stoc_range_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_058_stoc_range_lvl_252d},
    "stoc_059_stoc_range_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_059_stoc_range_zscore_252d},
    "stoc_060_stoc_range_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_060_stoc_range_rank_252d},
    "stoc_061_stoc_dist_lvl_5d": {"inputs": ["high", "low", "close"], "func": stoc_061_stoc_dist_lvl_5d},
    "stoc_062_stoc_dist_zscore_5d": {"inputs": ["high", "low", "close"], "func": stoc_062_stoc_dist_zscore_5d},
    "stoc_063_stoc_dist_rank_5d": {"inputs": ["high", "low", "close"], "func": stoc_063_stoc_dist_rank_5d},
    "stoc_064_stoc_dist_lvl_21d": {"inputs": ["high", "low", "close"], "func": stoc_064_stoc_dist_lvl_21d},
    "stoc_065_stoc_dist_zscore_21d": {"inputs": ["high", "low", "close"], "func": stoc_065_stoc_dist_zscore_21d},
    "stoc_066_stoc_dist_rank_21d": {"inputs": ["high", "low", "close"], "func": stoc_066_stoc_dist_rank_21d},
    "stoc_067_stoc_dist_lvl_63d": {"inputs": ["high", "low", "close"], "func": stoc_067_stoc_dist_lvl_63d},
    "stoc_068_stoc_dist_zscore_63d": {"inputs": ["high", "low", "close"], "func": stoc_068_stoc_dist_zscore_63d},
    "stoc_069_stoc_dist_rank_63d": {"inputs": ["high", "low", "close"], "func": stoc_069_stoc_dist_rank_63d},
    "stoc_070_stoc_dist_lvl_126d": {"inputs": ["high", "low", "close"], "func": stoc_070_stoc_dist_lvl_126d},
    "stoc_071_stoc_dist_zscore_126d": {"inputs": ["high", "low", "close"], "func": stoc_071_stoc_dist_zscore_126d},
    "stoc_072_stoc_dist_rank_126d": {"inputs": ["high", "low", "close"], "func": stoc_072_stoc_dist_rank_126d},
    "stoc_073_stoc_dist_lvl_252d": {"inputs": ["high", "low", "close"], "func": stoc_073_stoc_dist_lvl_252d},
    "stoc_074_stoc_dist_zscore_252d": {"inputs": ["high", "low", "close"], "func": stoc_074_stoc_dist_zscore_252d},
    "stoc_075_stoc_dist_rank_252d": {"inputs": ["high", "low", "close"], "func": stoc_075_stoc_dist_rank_252d},
}
