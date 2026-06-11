"""
93_ulto_dynamics — Base Features 001-075
Domain: ulto_dynamics
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

def ulto_001_bp_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_001_bp_lvl_5d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 5)

def ulto_002_bp_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_002_bp_zscore_5d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 5)

def ulto_003_bp_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_003_bp_rank_5d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 5)

def ulto_004_bp_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_004_bp_lvl_21d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 21)

def ulto_005_bp_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_005_bp_zscore_21d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 21)

def ulto_006_bp_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_006_bp_rank_21d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 21)

def ulto_007_bp_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_007_bp_lvl_63d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 63)

def ulto_008_bp_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_008_bp_zscore_63d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 63)

def ulto_009_bp_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_009_bp_rank_63d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 63)

def ulto_010_bp_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_010_bp_lvl_126d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 126)

def ulto_011_bp_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_011_bp_zscore_126d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 126)

def ulto_012_bp_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_012_bp_rank_126d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 126)

def ulto_013_bp_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_013_bp_lvl_252d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 252)

def ulto_014_bp_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_014_bp_zscore_252d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 252)

def ulto_015_bp_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_015_bp_rank_252d"""
    base = close - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 252)

def ulto_016_tr_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_016_tr_lvl_5d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 5)

def ulto_017_tr_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_017_tr_zscore_5d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 5)

def ulto_018_tr_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_018_tr_rank_5d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 5)

def ulto_019_tr_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_019_tr_lvl_21d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 21)

def ulto_020_tr_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_020_tr_zscore_21d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 21)

def ulto_021_tr_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_021_tr_rank_21d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 21)

def ulto_022_tr_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_022_tr_lvl_63d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 63)

def ulto_023_tr_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_023_tr_zscore_63d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 63)

def ulto_024_tr_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_024_tr_rank_63d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 63)

def ulto_025_tr_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_025_tr_lvl_126d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 126)

def ulto_026_tr_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_026_tr_zscore_126d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 126)

def ulto_027_tr_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_027_tr_rank_126d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 126)

def ulto_028_tr_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_028_tr_lvl_252d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rolling_mean(base, 252)

def ulto_029_tr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_029_tr_zscore_252d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _zscore_rolling(base, 252)

def ulto_030_tr_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_030_tr_rank_252d"""
    base = pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    return _rank_pct(base, 252)

def ulto_031_avg_7_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_031_avg_7_lvl_5d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rolling_mean(base, 5)

def ulto_032_avg_7_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_032_avg_7_zscore_5d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _zscore_rolling(base, 5)

def ulto_033_avg_7_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_033_avg_7_rank_5d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rank_pct(base, 5)

def ulto_034_avg_7_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_034_avg_7_lvl_21d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rolling_mean(base, 21)

def ulto_035_avg_7_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_035_avg_7_zscore_21d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _zscore_rolling(base, 21)

def ulto_036_avg_7_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_036_avg_7_rank_21d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rank_pct(base, 21)

def ulto_037_avg_7_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_037_avg_7_lvl_63d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rolling_mean(base, 63)

def ulto_038_avg_7_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_038_avg_7_zscore_63d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _zscore_rolling(base, 63)

def ulto_039_avg_7_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_039_avg_7_rank_63d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rank_pct(base, 63)

def ulto_040_avg_7_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_040_avg_7_lvl_126d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rolling_mean(base, 126)

def ulto_041_avg_7_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_041_avg_7_zscore_126d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _zscore_rolling(base, 126)

def ulto_042_avg_7_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_042_avg_7_rank_126d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rank_pct(base, 126)

def ulto_043_avg_7_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_043_avg_7_lvl_252d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rolling_mean(base, 252)

def ulto_044_avg_7_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_044_avg_7_zscore_252d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _zscore_rolling(base, 252)

def ulto_045_avg_7_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_045_avg_7_rank_252d"""
    base = _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7))
    return _rank_pct(base, 252)

def ulto_046_ult_osc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_046_ult_osc_lvl_5d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rolling_mean(base, 5)

def ulto_047_ult_osc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_047_ult_osc_zscore_5d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _zscore_rolling(base, 5)

def ulto_048_ult_osc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_048_ult_osc_rank_5d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rank_pct(base, 5)

def ulto_049_ult_osc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_049_ult_osc_lvl_21d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rolling_mean(base, 21)

def ulto_050_ult_osc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_050_ult_osc_zscore_21d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _zscore_rolling(base, 21)

def ulto_051_ult_osc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_051_ult_osc_rank_21d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rank_pct(base, 21)

def ulto_052_ult_osc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_052_ult_osc_lvl_63d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rolling_mean(base, 63)

def ulto_053_ult_osc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_053_ult_osc_zscore_63d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _zscore_rolling(base, 63)

def ulto_054_ult_osc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_054_ult_osc_rank_63d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rank_pct(base, 63)

def ulto_055_ult_osc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_055_ult_osc_lvl_126d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rolling_mean(base, 126)

def ulto_056_ult_osc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_056_ult_osc_zscore_126d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _zscore_rolling(base, 126)

def ulto_057_ult_osc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_057_ult_osc_rank_126d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rank_pct(base, 126)

def ulto_058_ult_osc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_058_ult_osc_lvl_252d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rolling_mean(base, 252)

def ulto_059_ult_osc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_059_ult_osc_zscore_252d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _zscore_rolling(base, 252)

def ulto_060_ult_osc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_060_ult_osc_rank_252d"""
    base = 100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7
    return _rank_pct(base, 252)

def ulto_061_ult_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_061_ult_z_lvl_5d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rolling_mean(base, 5)

def ulto_062_ult_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_062_ult_z_zscore_5d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _zscore_rolling(base, 5)

def ulto_063_ult_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_063_ult_z_rank_5d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rank_pct(base, 5)

def ulto_064_ult_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_064_ult_z_lvl_21d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rolling_mean(base, 21)

def ulto_065_ult_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_065_ult_z_zscore_21d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _zscore_rolling(base, 21)

def ulto_066_ult_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_066_ult_z_rank_21d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rank_pct(base, 21)

def ulto_067_ult_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_067_ult_z_lvl_63d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rolling_mean(base, 63)

def ulto_068_ult_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_068_ult_z_zscore_63d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _zscore_rolling(base, 63)

def ulto_069_ult_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_069_ult_z_rank_63d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rank_pct(base, 63)

def ulto_070_ult_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_070_ult_z_lvl_126d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rolling_mean(base, 126)

def ulto_071_ult_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_071_ult_z_zscore_126d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _zscore_rolling(base, 126)

def ulto_072_ult_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_072_ult_z_rank_126d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rank_pct(base, 126)

def ulto_073_ult_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_073_ult_z_lvl_252d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rolling_mean(base, 252)

def ulto_074_ult_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_074_ult_z_zscore_252d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _zscore_rolling(base, 252)

def ulto_075_ult_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ulto_075_ult_z_rank_252d"""
    base = _zscore_rolling(100 * (4*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 7)) + 2*_safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 14)) + _safe_div(_rolling_mean(close - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28), _rolling_mean(pd.concat([high, close.shift(1)], axis=1).max(axis=1) - pd.concat([low, close.shift(1)], axis=1).min(axis=1), 28))) / 7, 21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V93_REGISTRY = {
    "ulto_001_bp_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_001_bp_lvl_5d},
    "ulto_002_bp_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_002_bp_zscore_5d},
    "ulto_003_bp_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_003_bp_rank_5d},
    "ulto_004_bp_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_004_bp_lvl_21d},
    "ulto_005_bp_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_005_bp_zscore_21d},
    "ulto_006_bp_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_006_bp_rank_21d},
    "ulto_007_bp_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_007_bp_lvl_63d},
    "ulto_008_bp_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_008_bp_zscore_63d},
    "ulto_009_bp_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_009_bp_rank_63d},
    "ulto_010_bp_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_010_bp_lvl_126d},
    "ulto_011_bp_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_011_bp_zscore_126d},
    "ulto_012_bp_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_012_bp_rank_126d},
    "ulto_013_bp_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_013_bp_lvl_252d},
    "ulto_014_bp_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_014_bp_zscore_252d},
    "ulto_015_bp_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_015_bp_rank_252d},
    "ulto_016_tr_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_016_tr_lvl_5d},
    "ulto_017_tr_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_017_tr_zscore_5d},
    "ulto_018_tr_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_018_tr_rank_5d},
    "ulto_019_tr_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_019_tr_lvl_21d},
    "ulto_020_tr_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_020_tr_zscore_21d},
    "ulto_021_tr_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_021_tr_rank_21d},
    "ulto_022_tr_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_022_tr_lvl_63d},
    "ulto_023_tr_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_023_tr_zscore_63d},
    "ulto_024_tr_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_024_tr_rank_63d},
    "ulto_025_tr_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_025_tr_lvl_126d},
    "ulto_026_tr_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_026_tr_zscore_126d},
    "ulto_027_tr_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_027_tr_rank_126d},
    "ulto_028_tr_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_028_tr_lvl_252d},
    "ulto_029_tr_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_029_tr_zscore_252d},
    "ulto_030_tr_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_030_tr_rank_252d},
    "ulto_031_avg_7_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_031_avg_7_lvl_5d},
    "ulto_032_avg_7_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_032_avg_7_zscore_5d},
    "ulto_033_avg_7_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_033_avg_7_rank_5d},
    "ulto_034_avg_7_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_034_avg_7_lvl_21d},
    "ulto_035_avg_7_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_035_avg_7_zscore_21d},
    "ulto_036_avg_7_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_036_avg_7_rank_21d},
    "ulto_037_avg_7_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_037_avg_7_lvl_63d},
    "ulto_038_avg_7_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_038_avg_7_zscore_63d},
    "ulto_039_avg_7_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_039_avg_7_rank_63d},
    "ulto_040_avg_7_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_040_avg_7_lvl_126d},
    "ulto_041_avg_7_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_041_avg_7_zscore_126d},
    "ulto_042_avg_7_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_042_avg_7_rank_126d},
    "ulto_043_avg_7_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_043_avg_7_lvl_252d},
    "ulto_044_avg_7_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_044_avg_7_zscore_252d},
    "ulto_045_avg_7_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_045_avg_7_rank_252d},
    "ulto_046_ult_osc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_046_ult_osc_lvl_5d},
    "ulto_047_ult_osc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_047_ult_osc_zscore_5d},
    "ulto_048_ult_osc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_048_ult_osc_rank_5d},
    "ulto_049_ult_osc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_049_ult_osc_lvl_21d},
    "ulto_050_ult_osc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_050_ult_osc_zscore_21d},
    "ulto_051_ult_osc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_051_ult_osc_rank_21d},
    "ulto_052_ult_osc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_052_ult_osc_lvl_63d},
    "ulto_053_ult_osc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_053_ult_osc_zscore_63d},
    "ulto_054_ult_osc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_054_ult_osc_rank_63d},
    "ulto_055_ult_osc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_055_ult_osc_lvl_126d},
    "ulto_056_ult_osc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_056_ult_osc_zscore_126d},
    "ulto_057_ult_osc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_057_ult_osc_rank_126d},
    "ulto_058_ult_osc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_058_ult_osc_lvl_252d},
    "ulto_059_ult_osc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_059_ult_osc_zscore_252d},
    "ulto_060_ult_osc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_060_ult_osc_rank_252d},
    "ulto_061_ult_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_061_ult_z_lvl_5d},
    "ulto_062_ult_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_062_ult_z_zscore_5d},
    "ulto_063_ult_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_063_ult_z_rank_5d},
    "ulto_064_ult_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_064_ult_z_lvl_21d},
    "ulto_065_ult_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_065_ult_z_zscore_21d},
    "ulto_066_ult_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_066_ult_z_rank_21d},
    "ulto_067_ult_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_067_ult_z_lvl_63d},
    "ulto_068_ult_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_068_ult_z_zscore_63d},
    "ulto_069_ult_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_069_ult_z_rank_63d},
    "ulto_070_ult_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_070_ult_z_lvl_126d},
    "ulto_071_ult_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_071_ult_z_zscore_126d},
    "ulto_072_ult_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_072_ult_z_rank_126d},
    "ulto_073_ult_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_073_ult_z_lvl_252d},
    "ulto_074_ult_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_074_ult_z_zscore_252d},
    "ulto_075_ult_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": ulto_075_ult_z_rank_252d},
}
