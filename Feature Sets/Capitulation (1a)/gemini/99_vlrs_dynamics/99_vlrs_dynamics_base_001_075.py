"""
99_vlrs_dynamics — Base Features 001-075
Domain: vlrs_dynamics
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

def vlrs_001_vol_rs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_001_vol_rs_lvl_5d"""
    base = _safe_div(volume, mkt_volume)
    return _rolling_mean(base, 5)

def vlrs_002_vol_rs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_002_vol_rs_zscore_5d"""
    base = _safe_div(volume, mkt_volume)
    return _zscore_rolling(base, 5)

def vlrs_003_vol_rs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_003_vol_rs_rank_5d"""
    base = _safe_div(volume, mkt_volume)
    return _rank_pct(base, 5)

def vlrs_004_vol_rs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_004_vol_rs_lvl_21d"""
    base = _safe_div(volume, mkt_volume)
    return _rolling_mean(base, 21)

def vlrs_005_vol_rs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_005_vol_rs_zscore_21d"""
    base = _safe_div(volume, mkt_volume)
    return _zscore_rolling(base, 21)

def vlrs_006_vol_rs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_006_vol_rs_rank_21d"""
    base = _safe_div(volume, mkt_volume)
    return _rank_pct(base, 21)

def vlrs_007_vol_rs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_007_vol_rs_lvl_63d"""
    base = _safe_div(volume, mkt_volume)
    return _rolling_mean(base, 63)

def vlrs_008_vol_rs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_008_vol_rs_zscore_63d"""
    base = _safe_div(volume, mkt_volume)
    return _zscore_rolling(base, 63)

def vlrs_009_vol_rs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_009_vol_rs_rank_63d"""
    base = _safe_div(volume, mkt_volume)
    return _rank_pct(base, 63)

def vlrs_010_vol_rs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_010_vol_rs_lvl_126d"""
    base = _safe_div(volume, mkt_volume)
    return _rolling_mean(base, 126)

def vlrs_011_vol_rs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_011_vol_rs_zscore_126d"""
    base = _safe_div(volume, mkt_volume)
    return _zscore_rolling(base, 126)

def vlrs_012_vol_rs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_012_vol_rs_rank_126d"""
    base = _safe_div(volume, mkt_volume)
    return _rank_pct(base, 126)

def vlrs_013_vol_rs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_013_vol_rs_lvl_252d"""
    base = _safe_div(volume, mkt_volume)
    return _rolling_mean(base, 252)

def vlrs_014_vol_rs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_014_vol_rs_zscore_252d"""
    base = _safe_div(volume, mkt_volume)
    return _zscore_rolling(base, 252)

def vlrs_015_vol_rs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_015_vol_rs_rank_252d"""
    base = _safe_div(volume, mkt_volume)
    return _rank_pct(base, 252)

def vlrs_016_vol_rs_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_016_vol_rs_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 5)

def vlrs_017_vol_rs_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_017_vol_rs_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 5)

def vlrs_018_vol_rs_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_018_vol_rs_z_rank_5d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 5)

def vlrs_019_vol_rs_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_019_vol_rs_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 21)

def vlrs_020_vol_rs_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_020_vol_rs_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 21)

def vlrs_021_vol_rs_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_021_vol_rs_z_rank_21d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 21)

def vlrs_022_vol_rs_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_022_vol_rs_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 63)

def vlrs_023_vol_rs_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_023_vol_rs_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 63)

def vlrs_024_vol_rs_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_024_vol_rs_z_rank_63d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 63)

def vlrs_025_vol_rs_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_025_vol_rs_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 126)

def vlrs_026_vol_rs_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_026_vol_rs_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 126)

def vlrs_027_vol_rs_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_027_vol_rs_z_rank_126d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 126)

def vlrs_028_vol_rs_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_028_vol_rs_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 252)

def vlrs_029_vol_rs_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_029_vol_rs_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 252)

def vlrs_030_vol_rs_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_030_vol_rs_z_rank_252d"""
    base = _zscore_rolling(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 252)

def vlrs_031_vol_rs_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_031_vol_rs_roc_lvl_5d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rolling_mean(base, 5)

def vlrs_032_vol_rs_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_032_vol_rs_roc_zscore_5d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _zscore_rolling(base, 5)

def vlrs_033_vol_rs_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_033_vol_rs_roc_rank_5d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rank_pct(base, 5)

def vlrs_034_vol_rs_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_034_vol_rs_roc_lvl_21d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rolling_mean(base, 21)

def vlrs_035_vol_rs_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_035_vol_rs_roc_zscore_21d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _zscore_rolling(base, 21)

def vlrs_036_vol_rs_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_036_vol_rs_roc_rank_21d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rank_pct(base, 21)

def vlrs_037_vol_rs_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_037_vol_rs_roc_lvl_63d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rolling_mean(base, 63)

def vlrs_038_vol_rs_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_038_vol_rs_roc_zscore_63d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _zscore_rolling(base, 63)

def vlrs_039_vol_rs_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_039_vol_rs_roc_rank_63d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rank_pct(base, 63)

def vlrs_040_vol_rs_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_040_vol_rs_roc_lvl_126d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rolling_mean(base, 126)

def vlrs_041_vol_rs_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_041_vol_rs_roc_zscore_126d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _zscore_rolling(base, 126)

def vlrs_042_vol_rs_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_042_vol_rs_roc_rank_126d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rank_pct(base, 126)

def vlrs_043_vol_rs_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_043_vol_rs_roc_lvl_252d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rolling_mean(base, 252)

def vlrs_044_vol_rs_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_044_vol_rs_roc_zscore_252d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _zscore_rolling(base, 252)

def vlrs_045_vol_rs_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_045_vol_rs_roc_rank_252d"""
    base = _safe_div(volume, mkt_volume).pct_change(21)
    return _rank_pct(base, 252)

def vlrs_046_vol_rs_sma_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_046_vol_rs_sma_lvl_5d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rolling_mean(base, 5)

def vlrs_047_vol_rs_sma_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_047_vol_rs_sma_zscore_5d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _zscore_rolling(base, 5)

def vlrs_048_vol_rs_sma_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_048_vol_rs_sma_rank_5d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rank_pct(base, 5)

def vlrs_049_vol_rs_sma_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_049_vol_rs_sma_lvl_21d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rolling_mean(base, 21)

def vlrs_050_vol_rs_sma_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_050_vol_rs_sma_zscore_21d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _zscore_rolling(base, 21)

def vlrs_051_vol_rs_sma_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_051_vol_rs_sma_rank_21d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rank_pct(base, 21)

def vlrs_052_vol_rs_sma_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_052_vol_rs_sma_lvl_63d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rolling_mean(base, 63)

def vlrs_053_vol_rs_sma_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_053_vol_rs_sma_zscore_63d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _zscore_rolling(base, 63)

def vlrs_054_vol_rs_sma_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_054_vol_rs_sma_rank_63d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rank_pct(base, 63)

def vlrs_055_vol_rs_sma_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_055_vol_rs_sma_lvl_126d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rolling_mean(base, 126)

def vlrs_056_vol_rs_sma_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_056_vol_rs_sma_zscore_126d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _zscore_rolling(base, 126)

def vlrs_057_vol_rs_sma_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_057_vol_rs_sma_rank_126d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rank_pct(base, 126)

def vlrs_058_vol_rs_sma_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_058_vol_rs_sma_lvl_252d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rolling_mean(base, 252)

def vlrs_059_vol_rs_sma_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_059_vol_rs_sma_zscore_252d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _zscore_rolling(base, 252)

def vlrs_060_vol_rs_sma_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_060_vol_rs_sma_rank_252d"""
    base = _safe_div(_safe_div(volume, mkt_volume), _rolling_mean(_safe_div(volume, mkt_volume), 21))
    return _rank_pct(base, 252)

def vlrs_061_vol_rs_rank_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_061_vol_rs_rank_lvl_5d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 5)

def vlrs_062_vol_rs_rank_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_062_vol_rs_rank_zscore_5d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 5)

def vlrs_063_vol_rs_rank_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_063_vol_rs_rank_rank_5d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 5)

def vlrs_064_vol_rs_rank_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_064_vol_rs_rank_lvl_21d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 21)

def vlrs_065_vol_rs_rank_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_065_vol_rs_rank_zscore_21d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 21)

def vlrs_066_vol_rs_rank_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_066_vol_rs_rank_rank_21d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 21)

def vlrs_067_vol_rs_rank_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_067_vol_rs_rank_lvl_63d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 63)

def vlrs_068_vol_rs_rank_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_068_vol_rs_rank_zscore_63d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 63)

def vlrs_069_vol_rs_rank_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_069_vol_rs_rank_rank_63d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 63)

def vlrs_070_vol_rs_rank_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_070_vol_rs_rank_lvl_126d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 126)

def vlrs_071_vol_rs_rank_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_071_vol_rs_rank_zscore_126d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 126)

def vlrs_072_vol_rs_rank_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_072_vol_rs_rank_rank_126d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 126)

def vlrs_073_vol_rs_rank_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_073_vol_rs_rank_lvl_252d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rolling_mean(base, 252)

def vlrs_074_vol_rs_rank_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_074_vol_rs_rank_zscore_252d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _zscore_rolling(base, 252)

def vlrs_075_vol_rs_rank_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """vlrs_075_vol_rs_rank_rank_252d"""
    base = _rank_pct(_safe_div(volume, mkt_volume), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V99_REGISTRY = {
    "vlrs_001_vol_rs_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_001_vol_rs_lvl_5d},
    "vlrs_002_vol_rs_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_002_vol_rs_zscore_5d},
    "vlrs_003_vol_rs_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_003_vol_rs_rank_5d},
    "vlrs_004_vol_rs_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_004_vol_rs_lvl_21d},
    "vlrs_005_vol_rs_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_005_vol_rs_zscore_21d},
    "vlrs_006_vol_rs_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_006_vol_rs_rank_21d},
    "vlrs_007_vol_rs_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_007_vol_rs_lvl_63d},
    "vlrs_008_vol_rs_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_008_vol_rs_zscore_63d},
    "vlrs_009_vol_rs_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_009_vol_rs_rank_63d},
    "vlrs_010_vol_rs_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_010_vol_rs_lvl_126d},
    "vlrs_011_vol_rs_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_011_vol_rs_zscore_126d},
    "vlrs_012_vol_rs_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_012_vol_rs_rank_126d},
    "vlrs_013_vol_rs_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_013_vol_rs_lvl_252d},
    "vlrs_014_vol_rs_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_014_vol_rs_zscore_252d},
    "vlrs_015_vol_rs_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_015_vol_rs_rank_252d},
    "vlrs_016_vol_rs_z_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_016_vol_rs_z_lvl_5d},
    "vlrs_017_vol_rs_z_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_017_vol_rs_z_zscore_5d},
    "vlrs_018_vol_rs_z_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_018_vol_rs_z_rank_5d},
    "vlrs_019_vol_rs_z_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_019_vol_rs_z_lvl_21d},
    "vlrs_020_vol_rs_z_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_020_vol_rs_z_zscore_21d},
    "vlrs_021_vol_rs_z_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_021_vol_rs_z_rank_21d},
    "vlrs_022_vol_rs_z_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_022_vol_rs_z_lvl_63d},
    "vlrs_023_vol_rs_z_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_023_vol_rs_z_zscore_63d},
    "vlrs_024_vol_rs_z_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_024_vol_rs_z_rank_63d},
    "vlrs_025_vol_rs_z_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_025_vol_rs_z_lvl_126d},
    "vlrs_026_vol_rs_z_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_026_vol_rs_z_zscore_126d},
    "vlrs_027_vol_rs_z_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_027_vol_rs_z_rank_126d},
    "vlrs_028_vol_rs_z_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_028_vol_rs_z_lvl_252d},
    "vlrs_029_vol_rs_z_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_029_vol_rs_z_zscore_252d},
    "vlrs_030_vol_rs_z_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_030_vol_rs_z_rank_252d},
    "vlrs_031_vol_rs_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_031_vol_rs_roc_lvl_5d},
    "vlrs_032_vol_rs_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_032_vol_rs_roc_zscore_5d},
    "vlrs_033_vol_rs_roc_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_033_vol_rs_roc_rank_5d},
    "vlrs_034_vol_rs_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_034_vol_rs_roc_lvl_21d},
    "vlrs_035_vol_rs_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_035_vol_rs_roc_zscore_21d},
    "vlrs_036_vol_rs_roc_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_036_vol_rs_roc_rank_21d},
    "vlrs_037_vol_rs_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_037_vol_rs_roc_lvl_63d},
    "vlrs_038_vol_rs_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_038_vol_rs_roc_zscore_63d},
    "vlrs_039_vol_rs_roc_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_039_vol_rs_roc_rank_63d},
    "vlrs_040_vol_rs_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_040_vol_rs_roc_lvl_126d},
    "vlrs_041_vol_rs_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_041_vol_rs_roc_zscore_126d},
    "vlrs_042_vol_rs_roc_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_042_vol_rs_roc_rank_126d},
    "vlrs_043_vol_rs_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_043_vol_rs_roc_lvl_252d},
    "vlrs_044_vol_rs_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_044_vol_rs_roc_zscore_252d},
    "vlrs_045_vol_rs_roc_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_045_vol_rs_roc_rank_252d},
    "vlrs_046_vol_rs_sma_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_046_vol_rs_sma_lvl_5d},
    "vlrs_047_vol_rs_sma_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_047_vol_rs_sma_zscore_5d},
    "vlrs_048_vol_rs_sma_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_048_vol_rs_sma_rank_5d},
    "vlrs_049_vol_rs_sma_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_049_vol_rs_sma_lvl_21d},
    "vlrs_050_vol_rs_sma_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_050_vol_rs_sma_zscore_21d},
    "vlrs_051_vol_rs_sma_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_051_vol_rs_sma_rank_21d},
    "vlrs_052_vol_rs_sma_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_052_vol_rs_sma_lvl_63d},
    "vlrs_053_vol_rs_sma_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_053_vol_rs_sma_zscore_63d},
    "vlrs_054_vol_rs_sma_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_054_vol_rs_sma_rank_63d},
    "vlrs_055_vol_rs_sma_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_055_vol_rs_sma_lvl_126d},
    "vlrs_056_vol_rs_sma_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_056_vol_rs_sma_zscore_126d},
    "vlrs_057_vol_rs_sma_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_057_vol_rs_sma_rank_126d},
    "vlrs_058_vol_rs_sma_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_058_vol_rs_sma_lvl_252d},
    "vlrs_059_vol_rs_sma_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_059_vol_rs_sma_zscore_252d},
    "vlrs_060_vol_rs_sma_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_060_vol_rs_sma_rank_252d},
    "vlrs_061_vol_rs_rank_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_061_vol_rs_rank_lvl_5d},
    "vlrs_062_vol_rs_rank_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_062_vol_rs_rank_zscore_5d},
    "vlrs_063_vol_rs_rank_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_063_vol_rs_rank_rank_5d},
    "vlrs_064_vol_rs_rank_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_064_vol_rs_rank_lvl_21d},
    "vlrs_065_vol_rs_rank_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_065_vol_rs_rank_zscore_21d},
    "vlrs_066_vol_rs_rank_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_066_vol_rs_rank_rank_21d},
    "vlrs_067_vol_rs_rank_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_067_vol_rs_rank_lvl_63d},
    "vlrs_068_vol_rs_rank_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_068_vol_rs_rank_zscore_63d},
    "vlrs_069_vol_rs_rank_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_069_vol_rs_rank_rank_63d},
    "vlrs_070_vol_rs_rank_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_070_vol_rs_rank_lvl_126d},
    "vlrs_071_vol_rs_rank_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_071_vol_rs_rank_zscore_126d},
    "vlrs_072_vol_rs_rank_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_072_vol_rs_rank_rank_126d},
    "vlrs_073_vol_rs_rank_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_073_vol_rs_rank_lvl_252d},
    "vlrs_074_vol_rs_rank_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_074_vol_rs_rank_zscore_252d},
    "vlrs_075_vol_rs_rank_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": vlrs_075_vol_rs_rank_rank_252d},
}
