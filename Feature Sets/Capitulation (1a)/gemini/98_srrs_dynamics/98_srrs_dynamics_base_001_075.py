"""
98_srrs_dynamics — Base Features 001-075
Domain: srrs_dynamics
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

def srrs_001_sec_rs_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_001_sec_rs_lvl_5d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 5)

def srrs_002_sec_rs_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_002_sec_rs_zscore_5d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 5)

def srrs_003_sec_rs_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_003_sec_rs_rank_5d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 5)

def srrs_004_sec_rs_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_004_sec_rs_lvl_21d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 21)

def srrs_005_sec_rs_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_005_sec_rs_zscore_21d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 21)

def srrs_006_sec_rs_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_006_sec_rs_rank_21d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 21)

def srrs_007_sec_rs_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_007_sec_rs_lvl_63d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 63)

def srrs_008_sec_rs_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_008_sec_rs_zscore_63d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 63)

def srrs_009_sec_rs_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_009_sec_rs_rank_63d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 63)

def srrs_010_sec_rs_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_010_sec_rs_lvl_126d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 126)

def srrs_011_sec_rs_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_011_sec_rs_zscore_126d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 126)

def srrs_012_sec_rs_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_012_sec_rs_rank_126d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 126)

def srrs_013_sec_rs_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_013_sec_rs_lvl_252d"""
    base = _safe_div(close, mkt_close)
    return _rolling_mean(base, 252)

def srrs_014_sec_rs_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_014_sec_rs_zscore_252d"""
    base = _safe_div(close, mkt_close)
    return _zscore_rolling(base, 252)

def srrs_015_sec_rs_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_015_sec_rs_rank_252d"""
    base = _safe_div(close, mkt_close)
    return _rank_pct(base, 252)

def srrs_016_sec_rs_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_016_sec_rs_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 5)

def srrs_017_sec_rs_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_017_sec_rs_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 5)

def srrs_018_sec_rs_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_018_sec_rs_z_rank_5d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 5)

def srrs_019_sec_rs_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_019_sec_rs_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 21)

def srrs_020_sec_rs_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_020_sec_rs_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 21)

def srrs_021_sec_rs_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_021_sec_rs_z_rank_21d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 21)

def srrs_022_sec_rs_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_022_sec_rs_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 63)

def srrs_023_sec_rs_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_023_sec_rs_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 63)

def srrs_024_sec_rs_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_024_sec_rs_z_rank_63d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 63)

def srrs_025_sec_rs_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_025_sec_rs_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 126)

def srrs_026_sec_rs_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_026_sec_rs_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 126)

def srrs_027_sec_rs_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_027_sec_rs_z_rank_126d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 126)

def srrs_028_sec_rs_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_028_sec_rs_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 252)

def srrs_029_sec_rs_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_029_sec_rs_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 252)

def srrs_030_sec_rs_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_030_sec_rs_z_rank_252d"""
    base = _zscore_rolling(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 252)

def srrs_031_sec_rs_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_031_sec_rs_roc_lvl_5d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 5)

def srrs_032_sec_rs_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_032_sec_rs_roc_zscore_5d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 5)

def srrs_033_sec_rs_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_033_sec_rs_roc_rank_5d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 5)

def srrs_034_sec_rs_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_034_sec_rs_roc_lvl_21d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 21)

def srrs_035_sec_rs_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_035_sec_rs_roc_zscore_21d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 21)

def srrs_036_sec_rs_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_036_sec_rs_roc_rank_21d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 21)

def srrs_037_sec_rs_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_037_sec_rs_roc_lvl_63d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 63)

def srrs_038_sec_rs_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_038_sec_rs_roc_zscore_63d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 63)

def srrs_039_sec_rs_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_039_sec_rs_roc_rank_63d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 63)

def srrs_040_sec_rs_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_040_sec_rs_roc_lvl_126d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 126)

def srrs_041_sec_rs_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_041_sec_rs_roc_zscore_126d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 126)

def srrs_042_sec_rs_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_042_sec_rs_roc_rank_126d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 126)

def srrs_043_sec_rs_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_043_sec_rs_roc_lvl_252d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rolling_mean(base, 252)

def srrs_044_sec_rs_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_044_sec_rs_roc_zscore_252d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _zscore_rolling(base, 252)

def srrs_045_sec_rs_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_045_sec_rs_roc_rank_252d"""
    base = _safe_div(close, mkt_close).pct_change(21)
    return _rank_pct(base, 252)

def srrs_046_sec_rs_mom_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_046_sec_rs_mom_lvl_5d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rolling_mean(base, 5)

def srrs_047_sec_rs_mom_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_047_sec_rs_mom_zscore_5d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _zscore_rolling(base, 5)

def srrs_048_sec_rs_mom_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_048_sec_rs_mom_rank_5d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rank_pct(base, 5)

def srrs_049_sec_rs_mom_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_049_sec_rs_mom_lvl_21d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rolling_mean(base, 21)

def srrs_050_sec_rs_mom_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_050_sec_rs_mom_zscore_21d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _zscore_rolling(base, 21)

def srrs_051_sec_rs_mom_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_051_sec_rs_mom_rank_21d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rank_pct(base, 21)

def srrs_052_sec_rs_mom_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_052_sec_rs_mom_lvl_63d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rolling_mean(base, 63)

def srrs_053_sec_rs_mom_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_053_sec_rs_mom_zscore_63d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _zscore_rolling(base, 63)

def srrs_054_sec_rs_mom_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_054_sec_rs_mom_rank_63d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rank_pct(base, 63)

def srrs_055_sec_rs_mom_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_055_sec_rs_mom_lvl_126d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rolling_mean(base, 126)

def srrs_056_sec_rs_mom_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_056_sec_rs_mom_zscore_126d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _zscore_rolling(base, 126)

def srrs_057_sec_rs_mom_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_057_sec_rs_mom_rank_126d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rank_pct(base, 126)

def srrs_058_sec_rs_mom_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_058_sec_rs_mom_lvl_252d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rolling_mean(base, 252)

def srrs_059_sec_rs_mom_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_059_sec_rs_mom_zscore_252d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _zscore_rolling(base, 252)

def srrs_060_sec_rs_mom_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_060_sec_rs_mom_rank_252d"""
    base = _safe_div(_safe_div(close, mkt_close).pct_change(21), _rolling_std(_safe_div(close, mkt_close).pct_change(1), 21))
    return _rank_pct(base, 252)

def srrs_061_sec_rs_rank_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_061_sec_rs_rank_lvl_5d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 5)

def srrs_062_sec_rs_rank_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_062_sec_rs_rank_zscore_5d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 5)

def srrs_063_sec_rs_rank_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_063_sec_rs_rank_rank_5d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 5)

def srrs_064_sec_rs_rank_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_064_sec_rs_rank_lvl_21d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 21)

def srrs_065_sec_rs_rank_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_065_sec_rs_rank_zscore_21d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 21)

def srrs_066_sec_rs_rank_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_066_sec_rs_rank_rank_21d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 21)

def srrs_067_sec_rs_rank_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_067_sec_rs_rank_lvl_63d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 63)

def srrs_068_sec_rs_rank_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_068_sec_rs_rank_zscore_63d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 63)

def srrs_069_sec_rs_rank_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_069_sec_rs_rank_rank_63d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 63)

def srrs_070_sec_rs_rank_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_070_sec_rs_rank_lvl_126d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 126)

def srrs_071_sec_rs_rank_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_071_sec_rs_rank_zscore_126d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 126)

def srrs_072_sec_rs_rank_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_072_sec_rs_rank_rank_126d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 126)

def srrs_073_sec_rs_rank_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_073_sec_rs_rank_lvl_252d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rolling_mean(base, 252)

def srrs_074_sec_rs_rank_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_074_sec_rs_rank_zscore_252d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _zscore_rolling(base, 252)

def srrs_075_sec_rs_rank_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """srrs_075_sec_rs_rank_rank_252d"""
    base = _rank_pct(_safe_div(close, mkt_close), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V98_REGISTRY = {
    "srrs_001_sec_rs_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_001_sec_rs_lvl_5d},
    "srrs_002_sec_rs_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_002_sec_rs_zscore_5d},
    "srrs_003_sec_rs_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_003_sec_rs_rank_5d},
    "srrs_004_sec_rs_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_004_sec_rs_lvl_21d},
    "srrs_005_sec_rs_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_005_sec_rs_zscore_21d},
    "srrs_006_sec_rs_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_006_sec_rs_rank_21d},
    "srrs_007_sec_rs_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_007_sec_rs_lvl_63d},
    "srrs_008_sec_rs_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_008_sec_rs_zscore_63d},
    "srrs_009_sec_rs_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_009_sec_rs_rank_63d},
    "srrs_010_sec_rs_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_010_sec_rs_lvl_126d},
    "srrs_011_sec_rs_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_011_sec_rs_zscore_126d},
    "srrs_012_sec_rs_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_012_sec_rs_rank_126d},
    "srrs_013_sec_rs_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_013_sec_rs_lvl_252d},
    "srrs_014_sec_rs_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_014_sec_rs_zscore_252d},
    "srrs_015_sec_rs_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_015_sec_rs_rank_252d},
    "srrs_016_sec_rs_z_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_016_sec_rs_z_lvl_5d},
    "srrs_017_sec_rs_z_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_017_sec_rs_z_zscore_5d},
    "srrs_018_sec_rs_z_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_018_sec_rs_z_rank_5d},
    "srrs_019_sec_rs_z_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_019_sec_rs_z_lvl_21d},
    "srrs_020_sec_rs_z_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_020_sec_rs_z_zscore_21d},
    "srrs_021_sec_rs_z_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_021_sec_rs_z_rank_21d},
    "srrs_022_sec_rs_z_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_022_sec_rs_z_lvl_63d},
    "srrs_023_sec_rs_z_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_023_sec_rs_z_zscore_63d},
    "srrs_024_sec_rs_z_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_024_sec_rs_z_rank_63d},
    "srrs_025_sec_rs_z_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_025_sec_rs_z_lvl_126d},
    "srrs_026_sec_rs_z_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_026_sec_rs_z_zscore_126d},
    "srrs_027_sec_rs_z_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_027_sec_rs_z_rank_126d},
    "srrs_028_sec_rs_z_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_028_sec_rs_z_lvl_252d},
    "srrs_029_sec_rs_z_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_029_sec_rs_z_zscore_252d},
    "srrs_030_sec_rs_z_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_030_sec_rs_z_rank_252d},
    "srrs_031_sec_rs_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_031_sec_rs_roc_lvl_5d},
    "srrs_032_sec_rs_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_032_sec_rs_roc_zscore_5d},
    "srrs_033_sec_rs_roc_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_033_sec_rs_roc_rank_5d},
    "srrs_034_sec_rs_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_034_sec_rs_roc_lvl_21d},
    "srrs_035_sec_rs_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_035_sec_rs_roc_zscore_21d},
    "srrs_036_sec_rs_roc_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_036_sec_rs_roc_rank_21d},
    "srrs_037_sec_rs_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_037_sec_rs_roc_lvl_63d},
    "srrs_038_sec_rs_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_038_sec_rs_roc_zscore_63d},
    "srrs_039_sec_rs_roc_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_039_sec_rs_roc_rank_63d},
    "srrs_040_sec_rs_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_040_sec_rs_roc_lvl_126d},
    "srrs_041_sec_rs_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_041_sec_rs_roc_zscore_126d},
    "srrs_042_sec_rs_roc_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_042_sec_rs_roc_rank_126d},
    "srrs_043_sec_rs_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_043_sec_rs_roc_lvl_252d},
    "srrs_044_sec_rs_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_044_sec_rs_roc_zscore_252d},
    "srrs_045_sec_rs_roc_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_045_sec_rs_roc_rank_252d},
    "srrs_046_sec_rs_mom_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_046_sec_rs_mom_lvl_5d},
    "srrs_047_sec_rs_mom_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_047_sec_rs_mom_zscore_5d},
    "srrs_048_sec_rs_mom_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_048_sec_rs_mom_rank_5d},
    "srrs_049_sec_rs_mom_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_049_sec_rs_mom_lvl_21d},
    "srrs_050_sec_rs_mom_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_050_sec_rs_mom_zscore_21d},
    "srrs_051_sec_rs_mom_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_051_sec_rs_mom_rank_21d},
    "srrs_052_sec_rs_mom_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_052_sec_rs_mom_lvl_63d},
    "srrs_053_sec_rs_mom_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_053_sec_rs_mom_zscore_63d},
    "srrs_054_sec_rs_mom_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_054_sec_rs_mom_rank_63d},
    "srrs_055_sec_rs_mom_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_055_sec_rs_mom_lvl_126d},
    "srrs_056_sec_rs_mom_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_056_sec_rs_mom_zscore_126d},
    "srrs_057_sec_rs_mom_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_057_sec_rs_mom_rank_126d},
    "srrs_058_sec_rs_mom_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_058_sec_rs_mom_lvl_252d},
    "srrs_059_sec_rs_mom_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_059_sec_rs_mom_zscore_252d},
    "srrs_060_sec_rs_mom_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_060_sec_rs_mom_rank_252d},
    "srrs_061_sec_rs_rank_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_061_sec_rs_rank_lvl_5d},
    "srrs_062_sec_rs_rank_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_062_sec_rs_rank_zscore_5d},
    "srrs_063_sec_rs_rank_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_063_sec_rs_rank_rank_5d},
    "srrs_064_sec_rs_rank_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_064_sec_rs_rank_lvl_21d},
    "srrs_065_sec_rs_rank_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_065_sec_rs_rank_zscore_21d},
    "srrs_066_sec_rs_rank_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_066_sec_rs_rank_rank_21d},
    "srrs_067_sec_rs_rank_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_067_sec_rs_rank_lvl_63d},
    "srrs_068_sec_rs_rank_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_068_sec_rs_rank_zscore_63d},
    "srrs_069_sec_rs_rank_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_069_sec_rs_rank_rank_63d},
    "srrs_070_sec_rs_rank_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_070_sec_rs_rank_lvl_126d},
    "srrs_071_sec_rs_rank_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_071_sec_rs_rank_zscore_126d},
    "srrs_072_sec_rs_rank_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_072_sec_rs_rank_rank_126d},
    "srrs_073_sec_rs_rank_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_073_sec_rs_rank_lvl_252d},
    "srrs_074_sec_rs_rank_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_074_sec_rs_rank_zscore_252d},
    "srrs_075_sec_rs_rank_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": srrs_075_sec_rs_rank_rank_252d},
}
