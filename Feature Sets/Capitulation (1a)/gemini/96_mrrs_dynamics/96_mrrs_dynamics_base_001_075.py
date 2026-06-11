"""
96_mrrs_dynamics — Base Features 001-075
Domain: mrrs_dynamics
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

def mrrs_001_rs_ratio_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_001_rs_ratio_lvl_5d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rolling_mean(base, 5)

def mrrs_002_rs_ratio_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_002_rs_ratio_zscore_5d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _zscore_rolling(base, 5)

def mrrs_003_rs_ratio_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_003_rs_ratio_rank_5d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rank_pct(base, 5)

def mrrs_004_rs_ratio_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_004_rs_ratio_lvl_21d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rolling_mean(base, 21)

def mrrs_005_rs_ratio_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_005_rs_ratio_zscore_21d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _zscore_rolling(base, 21)

def mrrs_006_rs_ratio_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_006_rs_ratio_rank_21d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rank_pct(base, 21)

def mrrs_007_rs_ratio_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_007_rs_ratio_lvl_63d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rolling_mean(base, 63)

def mrrs_008_rs_ratio_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_008_rs_ratio_zscore_63d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _zscore_rolling(base, 63)

def mrrs_009_rs_ratio_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_009_rs_ratio_rank_63d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rank_pct(base, 63)

def mrrs_010_rs_ratio_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_010_rs_ratio_lvl_126d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rolling_mean(base, 126)

def mrrs_011_rs_ratio_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_011_rs_ratio_zscore_126d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _zscore_rolling(base, 126)

def mrrs_012_rs_ratio_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_012_rs_ratio_rank_126d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rank_pct(base, 126)

def mrrs_013_rs_ratio_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_013_rs_ratio_lvl_252d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rolling_mean(base, 252)

def mrrs_014_rs_ratio_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_014_rs_ratio_zscore_252d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _zscore_rolling(base, 252)

def mrrs_015_rs_ratio_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_015_rs_ratio_rank_252d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 252), _rolling_std(_safe_div(close, mkt_close), 252))
    return _rank_pct(base, 252)

def mrrs_016_rs_mom_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_016_rs_mom_lvl_5d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rolling_mean(base, 5)

def mrrs_017_rs_mom_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_017_rs_mom_zscore_5d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _zscore_rolling(base, 5)

def mrrs_018_rs_mom_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_018_rs_mom_rank_5d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rank_pct(base, 5)

def mrrs_019_rs_mom_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_019_rs_mom_lvl_21d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rolling_mean(base, 21)

def mrrs_020_rs_mom_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_020_rs_mom_zscore_21d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _zscore_rolling(base, 21)

def mrrs_021_rs_mom_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_021_rs_mom_rank_21d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rank_pct(base, 21)

def mrrs_022_rs_mom_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_022_rs_mom_lvl_63d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rolling_mean(base, 63)

def mrrs_023_rs_mom_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_023_rs_mom_zscore_63d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _zscore_rolling(base, 63)

def mrrs_024_rs_mom_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_024_rs_mom_rank_63d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rank_pct(base, 63)

def mrrs_025_rs_mom_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_025_rs_mom_lvl_126d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rolling_mean(base, 126)

def mrrs_026_rs_mom_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_026_rs_mom_zscore_126d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _zscore_rolling(base, 126)

def mrrs_027_rs_mom_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_027_rs_mom_rank_126d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rank_pct(base, 126)

def mrrs_028_rs_mom_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_028_rs_mom_lvl_252d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rolling_mean(base, 252)

def mrrs_029_rs_mom_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_029_rs_mom_zscore_252d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _zscore_rolling(base, 252)

def mrrs_030_rs_mom_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_030_rs_mom_rank_252d"""
    base = 100 + _safe_div(_safe_div(close, mkt_close) - _rolling_mean(_safe_div(close, mkt_close), 21), _rolling_std(_safe_div(close, mkt_close), 21))
    return _rank_pct(base, 252)

def mrrs_031_rs_lvl_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_031_rs_lvl_lvl_5d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 5)

def mrrs_032_rs_lvl_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_032_rs_lvl_zscore_5d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 5)

def mrrs_033_rs_lvl_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_033_rs_lvl_rank_5d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 5)

def mrrs_034_rs_lvl_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_034_rs_lvl_lvl_21d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 21)

def mrrs_035_rs_lvl_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_035_rs_lvl_zscore_21d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 21)

def mrrs_036_rs_lvl_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_036_rs_lvl_rank_21d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 21)

def mrrs_037_rs_lvl_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_037_rs_lvl_lvl_63d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 63)

def mrrs_038_rs_lvl_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_038_rs_lvl_zscore_63d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 63)

def mrrs_039_rs_lvl_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_039_rs_lvl_rank_63d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 63)

def mrrs_040_rs_lvl_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_040_rs_lvl_lvl_126d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 126)

def mrrs_041_rs_lvl_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_041_rs_lvl_zscore_126d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 126)

def mrrs_042_rs_lvl_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_042_rs_lvl_rank_126d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 126)

def mrrs_043_rs_lvl_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_043_rs_lvl_lvl_252d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 252)

def mrrs_044_rs_lvl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_044_rs_lvl_zscore_252d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 252)

def mrrs_045_rs_lvl_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_045_rs_lvl_rank_252d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 252)

def mrrs_046_rs_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_046_rs_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 5)

def mrrs_047_rs_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_047_rs_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 5)

def mrrs_048_rs_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_048_rs_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 5)

def mrrs_049_rs_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_049_rs_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 21)

def mrrs_050_rs_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_050_rs_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 21)

def mrrs_051_rs_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_051_rs_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 21)

def mrrs_052_rs_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_052_rs_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 63)

def mrrs_053_rs_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_053_rs_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 63)

def mrrs_054_rs_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_054_rs_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 63)

def mrrs_055_rs_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_055_rs_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 126)

def mrrs_056_rs_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_056_rs_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 126)

def mrrs_057_rs_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_057_rs_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 126)

def mrrs_058_rs_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_058_rs_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 252)

def mrrs_059_rs_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_059_rs_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 252)

def mrrs_060_rs_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_060_rs_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 252)

def mrrs_061_rs_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_061_rs_roc_lvl_5d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 5)

def mrrs_062_rs_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_062_rs_roc_zscore_5d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 5)

def mrrs_063_rs_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_063_rs_roc_rank_5d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 5)

def mrrs_064_rs_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_064_rs_roc_lvl_21d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 21)

def mrrs_065_rs_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_065_rs_roc_zscore_21d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 21)

def mrrs_066_rs_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_066_rs_roc_rank_21d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 21)

def mrrs_067_rs_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_067_rs_roc_lvl_63d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 63)

def mrrs_068_rs_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_068_rs_roc_zscore_63d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 63)

def mrrs_069_rs_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_069_rs_roc_rank_63d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 63)

def mrrs_070_rs_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_070_rs_roc_lvl_126d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 126)

def mrrs_071_rs_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_071_rs_roc_zscore_126d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 126)

def mrrs_072_rs_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_072_rs_roc_rank_126d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 126)

def mrrs_073_rs_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_073_rs_roc_lvl_252d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 252)

def mrrs_074_rs_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_074_rs_roc_zscore_252d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 252)

def mrrs_075_rs_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """mrrs_075_rs_roc_rank_252d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V96_REGISTRY = {
    "mrrs_001_rs_ratio_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_001_rs_ratio_lvl_5d},
    "mrrs_002_rs_ratio_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_002_rs_ratio_zscore_5d},
    "mrrs_003_rs_ratio_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_003_rs_ratio_rank_5d},
    "mrrs_004_rs_ratio_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_004_rs_ratio_lvl_21d},
    "mrrs_005_rs_ratio_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_005_rs_ratio_zscore_21d},
    "mrrs_006_rs_ratio_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_006_rs_ratio_rank_21d},
    "mrrs_007_rs_ratio_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_007_rs_ratio_lvl_63d},
    "mrrs_008_rs_ratio_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_008_rs_ratio_zscore_63d},
    "mrrs_009_rs_ratio_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_009_rs_ratio_rank_63d},
    "mrrs_010_rs_ratio_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_010_rs_ratio_lvl_126d},
    "mrrs_011_rs_ratio_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_011_rs_ratio_zscore_126d},
    "mrrs_012_rs_ratio_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_012_rs_ratio_rank_126d},
    "mrrs_013_rs_ratio_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_013_rs_ratio_lvl_252d},
    "mrrs_014_rs_ratio_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_014_rs_ratio_zscore_252d},
    "mrrs_015_rs_ratio_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_015_rs_ratio_rank_252d},
    "mrrs_016_rs_mom_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_016_rs_mom_lvl_5d},
    "mrrs_017_rs_mom_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_017_rs_mom_zscore_5d},
    "mrrs_018_rs_mom_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_018_rs_mom_rank_5d},
    "mrrs_019_rs_mom_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_019_rs_mom_lvl_21d},
    "mrrs_020_rs_mom_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_020_rs_mom_zscore_21d},
    "mrrs_021_rs_mom_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_021_rs_mom_rank_21d},
    "mrrs_022_rs_mom_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_022_rs_mom_lvl_63d},
    "mrrs_023_rs_mom_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_023_rs_mom_zscore_63d},
    "mrrs_024_rs_mom_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_024_rs_mom_rank_63d},
    "mrrs_025_rs_mom_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_025_rs_mom_lvl_126d},
    "mrrs_026_rs_mom_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_026_rs_mom_zscore_126d},
    "mrrs_027_rs_mom_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_027_rs_mom_rank_126d},
    "mrrs_028_rs_mom_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_028_rs_mom_lvl_252d},
    "mrrs_029_rs_mom_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_029_rs_mom_zscore_252d},
    "mrrs_030_rs_mom_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_030_rs_mom_rank_252d},
    "mrrs_031_rs_lvl_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_031_rs_lvl_lvl_5d},
    "mrrs_032_rs_lvl_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_032_rs_lvl_zscore_5d},
    "mrrs_033_rs_lvl_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_033_rs_lvl_rank_5d},
    "mrrs_034_rs_lvl_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_034_rs_lvl_lvl_21d},
    "mrrs_035_rs_lvl_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_035_rs_lvl_zscore_21d},
    "mrrs_036_rs_lvl_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_036_rs_lvl_rank_21d},
    "mrrs_037_rs_lvl_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_037_rs_lvl_lvl_63d},
    "mrrs_038_rs_lvl_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_038_rs_lvl_zscore_63d},
    "mrrs_039_rs_lvl_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_039_rs_lvl_rank_63d},
    "mrrs_040_rs_lvl_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_040_rs_lvl_lvl_126d},
    "mrrs_041_rs_lvl_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_041_rs_lvl_zscore_126d},
    "mrrs_042_rs_lvl_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_042_rs_lvl_rank_126d},
    "mrrs_043_rs_lvl_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_043_rs_lvl_lvl_252d},
    "mrrs_044_rs_lvl_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_044_rs_lvl_zscore_252d},
    "mrrs_045_rs_lvl_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_045_rs_lvl_rank_252d},
    "mrrs_046_rs_z_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_046_rs_z_lvl_5d},
    "mrrs_047_rs_z_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_047_rs_z_zscore_5d},
    "mrrs_048_rs_z_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_048_rs_z_rank_5d},
    "mrrs_049_rs_z_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_049_rs_z_lvl_21d},
    "mrrs_050_rs_z_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_050_rs_z_zscore_21d},
    "mrrs_051_rs_z_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_051_rs_z_rank_21d},
    "mrrs_052_rs_z_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_052_rs_z_lvl_63d},
    "mrrs_053_rs_z_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_053_rs_z_zscore_63d},
    "mrrs_054_rs_z_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_054_rs_z_rank_63d},
    "mrrs_055_rs_z_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_055_rs_z_lvl_126d},
    "mrrs_056_rs_z_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_056_rs_z_zscore_126d},
    "mrrs_057_rs_z_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_057_rs_z_rank_126d},
    "mrrs_058_rs_z_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_058_rs_z_lvl_252d},
    "mrrs_059_rs_z_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_059_rs_z_zscore_252d},
    "mrrs_060_rs_z_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_060_rs_z_rank_252d},
    "mrrs_061_rs_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_061_rs_roc_lvl_5d},
    "mrrs_062_rs_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_062_rs_roc_zscore_5d},
    "mrrs_063_rs_roc_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_063_rs_roc_rank_5d},
    "mrrs_064_rs_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_064_rs_roc_lvl_21d},
    "mrrs_065_rs_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_065_rs_roc_zscore_21d},
    "mrrs_066_rs_roc_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_066_rs_roc_rank_21d},
    "mrrs_067_rs_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_067_rs_roc_lvl_63d},
    "mrrs_068_rs_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_068_rs_roc_zscore_63d},
    "mrrs_069_rs_roc_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_069_rs_roc_rank_63d},
    "mrrs_070_rs_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_070_rs_roc_lvl_126d},
    "mrrs_071_rs_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_071_rs_roc_zscore_126d},
    "mrrs_072_rs_roc_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_072_rs_roc_rank_126d},
    "mrrs_073_rs_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_073_rs_roc_lvl_252d},
    "mrrs_074_rs_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_074_rs_roc_zscore_252d},
    "mrrs_075_rs_roc_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": mrrs_075_rs_roc_rank_252d},
}
