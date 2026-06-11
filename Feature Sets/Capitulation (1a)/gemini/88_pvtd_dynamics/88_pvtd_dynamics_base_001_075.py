"""
88_pvtd_dynamics — Base Features 001-075
Domain: pvtd_dynamics
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

def pvtd_001_pvt_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_001_pvt_lvl_5d"""
    base = volume * (close.pct_change())
    return _rolling_mean(base, 5)

def pvtd_002_pvt_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_002_pvt_zscore_5d"""
    base = volume * (close.pct_change())
    return _zscore_rolling(base, 5)

def pvtd_003_pvt_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_003_pvt_rank_5d"""
    base = volume * (close.pct_change())
    return _rank_pct(base, 5)

def pvtd_004_pvt_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_004_pvt_lvl_21d"""
    base = volume * (close.pct_change())
    return _rolling_mean(base, 21)

def pvtd_005_pvt_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_005_pvt_zscore_21d"""
    base = volume * (close.pct_change())
    return _zscore_rolling(base, 21)

def pvtd_006_pvt_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_006_pvt_rank_21d"""
    base = volume * (close.pct_change())
    return _rank_pct(base, 21)

def pvtd_007_pvt_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_007_pvt_lvl_63d"""
    base = volume * (close.pct_change())
    return _rolling_mean(base, 63)

def pvtd_008_pvt_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_008_pvt_zscore_63d"""
    base = volume * (close.pct_change())
    return _zscore_rolling(base, 63)

def pvtd_009_pvt_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_009_pvt_rank_63d"""
    base = volume * (close.pct_change())
    return _rank_pct(base, 63)

def pvtd_010_pvt_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_010_pvt_lvl_126d"""
    base = volume * (close.pct_change())
    return _rolling_mean(base, 126)

def pvtd_011_pvt_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_011_pvt_zscore_126d"""
    base = volume * (close.pct_change())
    return _zscore_rolling(base, 126)

def pvtd_012_pvt_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_012_pvt_rank_126d"""
    base = volume * (close.pct_change())
    return _rank_pct(base, 126)

def pvtd_013_pvt_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_013_pvt_lvl_252d"""
    base = volume * (close.pct_change())
    return _rolling_mean(base, 252)

def pvtd_014_pvt_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_014_pvt_zscore_252d"""
    base = volume * (close.pct_change())
    return _zscore_rolling(base, 252)

def pvtd_015_pvt_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_015_pvt_rank_252d"""
    base = volume * (close.pct_change())
    return _rank_pct(base, 252)

def pvtd_016_pvt_cum_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_016_pvt_cum_lvl_5d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rolling_mean(base, 5)

def pvtd_017_pvt_cum_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_017_pvt_cum_zscore_5d"""
    base = (volume * (close.pct_change())).cumsum()
    return _zscore_rolling(base, 5)

def pvtd_018_pvt_cum_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_018_pvt_cum_rank_5d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rank_pct(base, 5)

def pvtd_019_pvt_cum_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_019_pvt_cum_lvl_21d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rolling_mean(base, 21)

def pvtd_020_pvt_cum_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_020_pvt_cum_zscore_21d"""
    base = (volume * (close.pct_change())).cumsum()
    return _zscore_rolling(base, 21)

def pvtd_021_pvt_cum_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_021_pvt_cum_rank_21d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rank_pct(base, 21)

def pvtd_022_pvt_cum_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_022_pvt_cum_lvl_63d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rolling_mean(base, 63)

def pvtd_023_pvt_cum_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_023_pvt_cum_zscore_63d"""
    base = (volume * (close.pct_change())).cumsum()
    return _zscore_rolling(base, 63)

def pvtd_024_pvt_cum_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_024_pvt_cum_rank_63d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rank_pct(base, 63)

def pvtd_025_pvt_cum_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_025_pvt_cum_lvl_126d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rolling_mean(base, 126)

def pvtd_026_pvt_cum_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_026_pvt_cum_zscore_126d"""
    base = (volume * (close.pct_change())).cumsum()
    return _zscore_rolling(base, 126)

def pvtd_027_pvt_cum_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_027_pvt_cum_rank_126d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rank_pct(base, 126)

def pvtd_028_pvt_cum_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_028_pvt_cum_lvl_252d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rolling_mean(base, 252)

def pvtd_029_pvt_cum_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_029_pvt_cum_zscore_252d"""
    base = (volume * (close.pct_change())).cumsum()
    return _zscore_rolling(base, 252)

def pvtd_030_pvt_cum_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_030_pvt_cum_rank_252d"""
    base = (volume * (close.pct_change())).cumsum()
    return _rank_pct(base, 252)

def pvtd_031_pvt_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_031_pvt_rat_lvl_5d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rolling_mean(base, 5)

def pvtd_032_pvt_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_032_pvt_rat_zscore_5d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _zscore_rolling(base, 5)

def pvtd_033_pvt_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_033_pvt_rat_rank_5d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rank_pct(base, 5)

def pvtd_034_pvt_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_034_pvt_rat_lvl_21d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rolling_mean(base, 21)

def pvtd_035_pvt_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_035_pvt_rat_zscore_21d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _zscore_rolling(base, 21)

def pvtd_036_pvt_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_036_pvt_rat_rank_21d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rank_pct(base, 21)

def pvtd_037_pvt_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_037_pvt_rat_lvl_63d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rolling_mean(base, 63)

def pvtd_038_pvt_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_038_pvt_rat_zscore_63d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _zscore_rolling(base, 63)

def pvtd_039_pvt_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_039_pvt_rat_rank_63d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rank_pct(base, 63)

def pvtd_040_pvt_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_040_pvt_rat_lvl_126d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rolling_mean(base, 126)

def pvtd_041_pvt_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_041_pvt_rat_zscore_126d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _zscore_rolling(base, 126)

def pvtd_042_pvt_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_042_pvt_rat_rank_126d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rank_pct(base, 126)

def pvtd_043_pvt_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_043_pvt_rat_lvl_252d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rolling_mean(base, 252)

def pvtd_044_pvt_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_044_pvt_rat_zscore_252d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _zscore_rolling(base, 252)

def pvtd_045_pvt_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_045_pvt_rat_rank_252d"""
    base = _safe_div(volume * (close.pct_change()), volume)
    return _rank_pct(base, 252)

def pvtd_046_pvt_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_046_pvt_roc_lvl_5d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rolling_mean(base, 5)

def pvtd_047_pvt_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_047_pvt_roc_zscore_5d"""
    base = (volume * (close.pct_change())).pct_change()
    return _zscore_rolling(base, 5)

def pvtd_048_pvt_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_048_pvt_roc_rank_5d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rank_pct(base, 5)

def pvtd_049_pvt_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_049_pvt_roc_lvl_21d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rolling_mean(base, 21)

def pvtd_050_pvt_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_050_pvt_roc_zscore_21d"""
    base = (volume * (close.pct_change())).pct_change()
    return _zscore_rolling(base, 21)

def pvtd_051_pvt_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_051_pvt_roc_rank_21d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rank_pct(base, 21)

def pvtd_052_pvt_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_052_pvt_roc_lvl_63d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rolling_mean(base, 63)

def pvtd_053_pvt_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_053_pvt_roc_zscore_63d"""
    base = (volume * (close.pct_change())).pct_change()
    return _zscore_rolling(base, 63)

def pvtd_054_pvt_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_054_pvt_roc_rank_63d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rank_pct(base, 63)

def pvtd_055_pvt_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_055_pvt_roc_lvl_126d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rolling_mean(base, 126)

def pvtd_056_pvt_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_056_pvt_roc_zscore_126d"""
    base = (volume * (close.pct_change())).pct_change()
    return _zscore_rolling(base, 126)

def pvtd_057_pvt_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_057_pvt_roc_rank_126d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rank_pct(base, 126)

def pvtd_058_pvt_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_058_pvt_roc_lvl_252d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rolling_mean(base, 252)

def pvtd_059_pvt_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_059_pvt_roc_zscore_252d"""
    base = (volume * (close.pct_change())).pct_change()
    return _zscore_rolling(base, 252)

def pvtd_060_pvt_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_060_pvt_roc_rank_252d"""
    base = (volume * (close.pct_change())).pct_change()
    return _rank_pct(base, 252)

def pvtd_061_pvt_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_061_pvt_z_lvl_5d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rolling_mean(base, 5)

def pvtd_062_pvt_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_062_pvt_z_zscore_5d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _zscore_rolling(base, 5)

def pvtd_063_pvt_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_063_pvt_z_rank_5d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rank_pct(base, 5)

def pvtd_064_pvt_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_064_pvt_z_lvl_21d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rolling_mean(base, 21)

def pvtd_065_pvt_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_065_pvt_z_zscore_21d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _zscore_rolling(base, 21)

def pvtd_066_pvt_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_066_pvt_z_rank_21d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rank_pct(base, 21)

def pvtd_067_pvt_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_067_pvt_z_lvl_63d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rolling_mean(base, 63)

def pvtd_068_pvt_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_068_pvt_z_zscore_63d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _zscore_rolling(base, 63)

def pvtd_069_pvt_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_069_pvt_z_rank_63d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rank_pct(base, 63)

def pvtd_070_pvt_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_070_pvt_z_lvl_126d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rolling_mean(base, 126)

def pvtd_071_pvt_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_071_pvt_z_zscore_126d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _zscore_rolling(base, 126)

def pvtd_072_pvt_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_072_pvt_z_rank_126d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rank_pct(base, 126)

def pvtd_073_pvt_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_073_pvt_z_lvl_252d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rolling_mean(base, 252)

def pvtd_074_pvt_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_074_pvt_z_zscore_252d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _zscore_rolling(base, 252)

def pvtd_075_pvt_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """pvtd_075_pvt_z_rank_252d"""
    base = _zscore_rolling(volume * (close.pct_change()), 21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V88_REGISTRY = {
    "pvtd_001_pvt_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_001_pvt_lvl_5d},
    "pvtd_002_pvt_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_002_pvt_zscore_5d},
    "pvtd_003_pvt_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_003_pvt_rank_5d},
    "pvtd_004_pvt_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_004_pvt_lvl_21d},
    "pvtd_005_pvt_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_005_pvt_zscore_21d},
    "pvtd_006_pvt_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_006_pvt_rank_21d},
    "pvtd_007_pvt_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_007_pvt_lvl_63d},
    "pvtd_008_pvt_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_008_pvt_zscore_63d},
    "pvtd_009_pvt_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_009_pvt_rank_63d},
    "pvtd_010_pvt_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_010_pvt_lvl_126d},
    "pvtd_011_pvt_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_011_pvt_zscore_126d},
    "pvtd_012_pvt_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_012_pvt_rank_126d},
    "pvtd_013_pvt_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_013_pvt_lvl_252d},
    "pvtd_014_pvt_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_014_pvt_zscore_252d},
    "pvtd_015_pvt_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_015_pvt_rank_252d},
    "pvtd_016_pvt_cum_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_016_pvt_cum_lvl_5d},
    "pvtd_017_pvt_cum_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_017_pvt_cum_zscore_5d},
    "pvtd_018_pvt_cum_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_018_pvt_cum_rank_5d},
    "pvtd_019_pvt_cum_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_019_pvt_cum_lvl_21d},
    "pvtd_020_pvt_cum_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_020_pvt_cum_zscore_21d},
    "pvtd_021_pvt_cum_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_021_pvt_cum_rank_21d},
    "pvtd_022_pvt_cum_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_022_pvt_cum_lvl_63d},
    "pvtd_023_pvt_cum_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_023_pvt_cum_zscore_63d},
    "pvtd_024_pvt_cum_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_024_pvt_cum_rank_63d},
    "pvtd_025_pvt_cum_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_025_pvt_cum_lvl_126d},
    "pvtd_026_pvt_cum_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_026_pvt_cum_zscore_126d},
    "pvtd_027_pvt_cum_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_027_pvt_cum_rank_126d},
    "pvtd_028_pvt_cum_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_028_pvt_cum_lvl_252d},
    "pvtd_029_pvt_cum_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_029_pvt_cum_zscore_252d},
    "pvtd_030_pvt_cum_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_030_pvt_cum_rank_252d},
    "pvtd_031_pvt_rat_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_031_pvt_rat_lvl_5d},
    "pvtd_032_pvt_rat_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_032_pvt_rat_zscore_5d},
    "pvtd_033_pvt_rat_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_033_pvt_rat_rank_5d},
    "pvtd_034_pvt_rat_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_034_pvt_rat_lvl_21d},
    "pvtd_035_pvt_rat_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_035_pvt_rat_zscore_21d},
    "pvtd_036_pvt_rat_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_036_pvt_rat_rank_21d},
    "pvtd_037_pvt_rat_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_037_pvt_rat_lvl_63d},
    "pvtd_038_pvt_rat_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_038_pvt_rat_zscore_63d},
    "pvtd_039_pvt_rat_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_039_pvt_rat_rank_63d},
    "pvtd_040_pvt_rat_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_040_pvt_rat_lvl_126d},
    "pvtd_041_pvt_rat_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_041_pvt_rat_zscore_126d},
    "pvtd_042_pvt_rat_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_042_pvt_rat_rank_126d},
    "pvtd_043_pvt_rat_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_043_pvt_rat_lvl_252d},
    "pvtd_044_pvt_rat_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_044_pvt_rat_zscore_252d},
    "pvtd_045_pvt_rat_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_045_pvt_rat_rank_252d},
    "pvtd_046_pvt_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_046_pvt_roc_lvl_5d},
    "pvtd_047_pvt_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_047_pvt_roc_zscore_5d},
    "pvtd_048_pvt_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_048_pvt_roc_rank_5d},
    "pvtd_049_pvt_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_049_pvt_roc_lvl_21d},
    "pvtd_050_pvt_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_050_pvt_roc_zscore_21d},
    "pvtd_051_pvt_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_051_pvt_roc_rank_21d},
    "pvtd_052_pvt_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_052_pvt_roc_lvl_63d},
    "pvtd_053_pvt_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_053_pvt_roc_zscore_63d},
    "pvtd_054_pvt_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_054_pvt_roc_rank_63d},
    "pvtd_055_pvt_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_055_pvt_roc_lvl_126d},
    "pvtd_056_pvt_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_056_pvt_roc_zscore_126d},
    "pvtd_057_pvt_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_057_pvt_roc_rank_126d},
    "pvtd_058_pvt_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_058_pvt_roc_lvl_252d},
    "pvtd_059_pvt_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_059_pvt_roc_zscore_252d},
    "pvtd_060_pvt_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_060_pvt_roc_rank_252d},
    "pvtd_061_pvt_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_061_pvt_z_lvl_5d},
    "pvtd_062_pvt_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_062_pvt_z_zscore_5d},
    "pvtd_063_pvt_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_063_pvt_z_rank_5d},
    "pvtd_064_pvt_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_064_pvt_z_lvl_21d},
    "pvtd_065_pvt_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_065_pvt_z_zscore_21d},
    "pvtd_066_pvt_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_066_pvt_z_rank_21d},
    "pvtd_067_pvt_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_067_pvt_z_lvl_63d},
    "pvtd_068_pvt_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_068_pvt_z_zscore_63d},
    "pvtd_069_pvt_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_069_pvt_z_rank_63d},
    "pvtd_070_pvt_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_070_pvt_z_lvl_126d},
    "pvtd_071_pvt_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_071_pvt_z_zscore_126d},
    "pvtd_072_pvt_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_072_pvt_z_rank_126d},
    "pvtd_073_pvt_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_073_pvt_z_lvl_252d},
    "pvtd_074_pvt_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_074_pvt_z_zscore_252d},
    "pvtd_075_pvt_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": pvtd_075_pvt_z_rank_252d},
}
