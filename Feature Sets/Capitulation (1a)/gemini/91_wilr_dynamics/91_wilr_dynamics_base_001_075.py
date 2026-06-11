"""
91_wilr_dynamics — Base Features 001-075
Domain: wilr_dynamics
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

def wilr_001_williams_r_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_001_williams_r_lvl_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 5)

def wilr_002_williams_r_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_002_williams_r_zscore_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 5)

def wilr_003_williams_r_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_003_williams_r_rank_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 5)

def wilr_004_williams_r_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_004_williams_r_lvl_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 21)

def wilr_005_williams_r_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_005_williams_r_zscore_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 21)

def wilr_006_williams_r_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_006_williams_r_rank_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 21)

def wilr_007_williams_r_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_007_williams_r_lvl_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 63)

def wilr_008_williams_r_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_008_williams_r_zscore_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 63)

def wilr_009_williams_r_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_009_williams_r_rank_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 63)

def wilr_010_williams_r_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_010_williams_r_lvl_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 126)

def wilr_011_williams_r_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_011_williams_r_zscore_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 126)

def wilr_012_williams_r_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_012_williams_r_rank_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 126)

def wilr_013_williams_r_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_013_williams_r_lvl_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rolling_mean(base, 252)

def wilr_014_williams_r_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_014_williams_r_zscore_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _zscore_rolling(base, 252)

def wilr_015_williams_r_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_015_williams_r_rank_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14))
    return _rank_pct(base, 252)

def wilr_016_wilr_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_016_wilr_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rolling_mean(base, 5)

def wilr_017_wilr_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_017_wilr_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _zscore_rolling(base, 5)

def wilr_018_wilr_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_018_wilr_z_rank_5d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rank_pct(base, 5)

def wilr_019_wilr_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_019_wilr_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rolling_mean(base, 21)

def wilr_020_wilr_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_020_wilr_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _zscore_rolling(base, 21)

def wilr_021_wilr_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_021_wilr_z_rank_21d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rank_pct(base, 21)

def wilr_022_wilr_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_022_wilr_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rolling_mean(base, 63)

def wilr_023_wilr_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_023_wilr_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _zscore_rolling(base, 63)

def wilr_024_wilr_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_024_wilr_z_rank_63d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rank_pct(base, 63)

def wilr_025_wilr_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_025_wilr_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rolling_mean(base, 126)

def wilr_026_wilr_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_026_wilr_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _zscore_rolling(base, 126)

def wilr_027_wilr_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_027_wilr_z_rank_126d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rank_pct(base, 126)

def wilr_028_wilr_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_028_wilr_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rolling_mean(base, 252)

def wilr_029_wilr_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_029_wilr_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _zscore_rolling(base, 252)

def wilr_030_wilr_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_030_wilr_z_rank_252d"""
    base = _zscore_rolling(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 21)
    return _rank_pct(base, 252)

def wilr_031_wilr_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_031_wilr_roc_lvl_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rolling_mean(base, 5)

def wilr_032_wilr_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_032_wilr_roc_zscore_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _zscore_rolling(base, 5)

def wilr_033_wilr_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_033_wilr_roc_rank_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rank_pct(base, 5)

def wilr_034_wilr_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_034_wilr_roc_lvl_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rolling_mean(base, 21)

def wilr_035_wilr_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_035_wilr_roc_zscore_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _zscore_rolling(base, 21)

def wilr_036_wilr_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_036_wilr_roc_rank_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rank_pct(base, 21)

def wilr_037_wilr_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_037_wilr_roc_lvl_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rolling_mean(base, 63)

def wilr_038_wilr_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_038_wilr_roc_zscore_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _zscore_rolling(base, 63)

def wilr_039_wilr_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_039_wilr_roc_rank_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rank_pct(base, 63)

def wilr_040_wilr_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_040_wilr_roc_lvl_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rolling_mean(base, 126)

def wilr_041_wilr_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_041_wilr_roc_zscore_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _zscore_rolling(base, 126)

def wilr_042_wilr_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_042_wilr_roc_rank_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rank_pct(base, 126)

def wilr_043_wilr_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_043_wilr_roc_lvl_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rolling_mean(base, 252)

def wilr_044_wilr_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_044_wilr_roc_zscore_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _zscore_rolling(base, 252)

def wilr_045_wilr_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_045_wilr_roc_rank_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)).pct_change()
    return _rank_pct(base, 252)

def wilr_046_wilr_ma_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_046_wilr_ma_lvl_5d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rolling_mean(base, 5)

def wilr_047_wilr_ma_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_047_wilr_ma_zscore_5d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _zscore_rolling(base, 5)

def wilr_048_wilr_ma_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_048_wilr_ma_rank_5d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rank_pct(base, 5)

def wilr_049_wilr_ma_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_049_wilr_ma_lvl_21d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rolling_mean(base, 21)

def wilr_050_wilr_ma_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_050_wilr_ma_zscore_21d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _zscore_rolling(base, 21)

def wilr_051_wilr_ma_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_051_wilr_ma_rank_21d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rank_pct(base, 21)

def wilr_052_wilr_ma_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_052_wilr_ma_lvl_63d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rolling_mean(base, 63)

def wilr_053_wilr_ma_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_053_wilr_ma_zscore_63d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _zscore_rolling(base, 63)

def wilr_054_wilr_ma_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_054_wilr_ma_rank_63d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rank_pct(base, 63)

def wilr_055_wilr_ma_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_055_wilr_ma_lvl_126d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rolling_mean(base, 126)

def wilr_056_wilr_ma_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_056_wilr_ma_zscore_126d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _zscore_rolling(base, 126)

def wilr_057_wilr_ma_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_057_wilr_ma_rank_126d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rank_pct(base, 126)

def wilr_058_wilr_ma_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_058_wilr_ma_lvl_252d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rolling_mean(base, 252)

def wilr_059_wilr_ma_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_059_wilr_ma_zscore_252d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _zscore_rolling(base, 252)

def wilr_060_wilr_ma_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_060_wilr_ma_rank_252d"""
    base = _rolling_mean(_safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)), 5)
    return _rank_pct(base, 252)

def wilr_061_wilr_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_061_wilr_dist_lvl_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rolling_mean(base, 5)

def wilr_062_wilr_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_062_wilr_dist_zscore_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _zscore_rolling(base, 5)

def wilr_063_wilr_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_063_wilr_dist_rank_5d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rank_pct(base, 5)

def wilr_064_wilr_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_064_wilr_dist_lvl_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rolling_mean(base, 21)

def wilr_065_wilr_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_065_wilr_dist_zscore_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _zscore_rolling(base, 21)

def wilr_066_wilr_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_066_wilr_dist_rank_21d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rank_pct(base, 21)

def wilr_067_wilr_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_067_wilr_dist_lvl_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rolling_mean(base, 63)

def wilr_068_wilr_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_068_wilr_dist_zscore_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _zscore_rolling(base, 63)

def wilr_069_wilr_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_069_wilr_dist_rank_63d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rank_pct(base, 63)

def wilr_070_wilr_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_070_wilr_dist_lvl_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rolling_mean(base, 126)

def wilr_071_wilr_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_071_wilr_dist_zscore_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _zscore_rolling(base, 126)

def wilr_072_wilr_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_072_wilr_dist_rank_126d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rank_pct(base, 126)

def wilr_073_wilr_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_073_wilr_dist_lvl_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rolling_mean(base, 252)

def wilr_074_wilr_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_074_wilr_dist_zscore_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _zscore_rolling(base, 252)

def wilr_075_wilr_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """wilr_075_wilr_dist_rank_252d"""
    base = _safe_div(_rolling_max(high, 14) - close, _rolling_max(high, 14) - _rolling_min(low, 14)) - 0.5
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V91_REGISTRY = {
    "wilr_001_williams_r_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_001_williams_r_lvl_5d},
    "wilr_002_williams_r_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_002_williams_r_zscore_5d},
    "wilr_003_williams_r_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_003_williams_r_rank_5d},
    "wilr_004_williams_r_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_004_williams_r_lvl_21d},
    "wilr_005_williams_r_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_005_williams_r_zscore_21d},
    "wilr_006_williams_r_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_006_williams_r_rank_21d},
    "wilr_007_williams_r_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_007_williams_r_lvl_63d},
    "wilr_008_williams_r_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_008_williams_r_zscore_63d},
    "wilr_009_williams_r_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_009_williams_r_rank_63d},
    "wilr_010_williams_r_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_010_williams_r_lvl_126d},
    "wilr_011_williams_r_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_011_williams_r_zscore_126d},
    "wilr_012_williams_r_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_012_williams_r_rank_126d},
    "wilr_013_williams_r_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_013_williams_r_lvl_252d},
    "wilr_014_williams_r_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_014_williams_r_zscore_252d},
    "wilr_015_williams_r_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_015_williams_r_rank_252d},
    "wilr_016_wilr_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_016_wilr_z_lvl_5d},
    "wilr_017_wilr_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_017_wilr_z_zscore_5d},
    "wilr_018_wilr_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_018_wilr_z_rank_5d},
    "wilr_019_wilr_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_019_wilr_z_lvl_21d},
    "wilr_020_wilr_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_020_wilr_z_zscore_21d},
    "wilr_021_wilr_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_021_wilr_z_rank_21d},
    "wilr_022_wilr_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_022_wilr_z_lvl_63d},
    "wilr_023_wilr_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_023_wilr_z_zscore_63d},
    "wilr_024_wilr_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_024_wilr_z_rank_63d},
    "wilr_025_wilr_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_025_wilr_z_lvl_126d},
    "wilr_026_wilr_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_026_wilr_z_zscore_126d},
    "wilr_027_wilr_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_027_wilr_z_rank_126d},
    "wilr_028_wilr_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_028_wilr_z_lvl_252d},
    "wilr_029_wilr_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_029_wilr_z_zscore_252d},
    "wilr_030_wilr_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_030_wilr_z_rank_252d},
    "wilr_031_wilr_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_031_wilr_roc_lvl_5d},
    "wilr_032_wilr_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_032_wilr_roc_zscore_5d},
    "wilr_033_wilr_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_033_wilr_roc_rank_5d},
    "wilr_034_wilr_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_034_wilr_roc_lvl_21d},
    "wilr_035_wilr_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_035_wilr_roc_zscore_21d},
    "wilr_036_wilr_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_036_wilr_roc_rank_21d},
    "wilr_037_wilr_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_037_wilr_roc_lvl_63d},
    "wilr_038_wilr_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_038_wilr_roc_zscore_63d},
    "wilr_039_wilr_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_039_wilr_roc_rank_63d},
    "wilr_040_wilr_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_040_wilr_roc_lvl_126d},
    "wilr_041_wilr_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_041_wilr_roc_zscore_126d},
    "wilr_042_wilr_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_042_wilr_roc_rank_126d},
    "wilr_043_wilr_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_043_wilr_roc_lvl_252d},
    "wilr_044_wilr_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_044_wilr_roc_zscore_252d},
    "wilr_045_wilr_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_045_wilr_roc_rank_252d},
    "wilr_046_wilr_ma_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_046_wilr_ma_lvl_5d},
    "wilr_047_wilr_ma_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_047_wilr_ma_zscore_5d},
    "wilr_048_wilr_ma_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_048_wilr_ma_rank_5d},
    "wilr_049_wilr_ma_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_049_wilr_ma_lvl_21d},
    "wilr_050_wilr_ma_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_050_wilr_ma_zscore_21d},
    "wilr_051_wilr_ma_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_051_wilr_ma_rank_21d},
    "wilr_052_wilr_ma_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_052_wilr_ma_lvl_63d},
    "wilr_053_wilr_ma_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_053_wilr_ma_zscore_63d},
    "wilr_054_wilr_ma_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_054_wilr_ma_rank_63d},
    "wilr_055_wilr_ma_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_055_wilr_ma_lvl_126d},
    "wilr_056_wilr_ma_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_056_wilr_ma_zscore_126d},
    "wilr_057_wilr_ma_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_057_wilr_ma_rank_126d},
    "wilr_058_wilr_ma_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_058_wilr_ma_lvl_252d},
    "wilr_059_wilr_ma_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_059_wilr_ma_zscore_252d},
    "wilr_060_wilr_ma_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_060_wilr_ma_rank_252d},
    "wilr_061_wilr_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_061_wilr_dist_lvl_5d},
    "wilr_062_wilr_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_062_wilr_dist_zscore_5d},
    "wilr_063_wilr_dist_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_063_wilr_dist_rank_5d},
    "wilr_064_wilr_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_064_wilr_dist_lvl_21d},
    "wilr_065_wilr_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_065_wilr_dist_zscore_21d},
    "wilr_066_wilr_dist_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_066_wilr_dist_rank_21d},
    "wilr_067_wilr_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_067_wilr_dist_lvl_63d},
    "wilr_068_wilr_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_068_wilr_dist_zscore_63d},
    "wilr_069_wilr_dist_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_069_wilr_dist_rank_63d},
    "wilr_070_wilr_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_070_wilr_dist_lvl_126d},
    "wilr_071_wilr_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_071_wilr_dist_zscore_126d},
    "wilr_072_wilr_dist_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_072_wilr_dist_rank_126d},
    "wilr_073_wilr_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_073_wilr_dist_lvl_252d},
    "wilr_074_wilr_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_074_wilr_dist_zscore_252d},
    "wilr_075_wilr_dist_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": wilr_075_wilr_dist_rank_252d},
}
