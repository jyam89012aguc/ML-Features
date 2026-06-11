"""
116_extreme_day_density — Base Features Part 1
Domain: extreme_day_density
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

def exdd_001_extreme_down_day_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_001_extreme_down_day_lvl_5d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rolling_mean(base, 5)

def exdd_002_extreme_down_day_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_002_extreme_down_day_zscore_5d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _zscore_rolling(base, 5)

def exdd_003_extreme_down_day_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_003_extreme_down_day_rank_5d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rank_pct(base, 5)

def exdd_004_extreme_down_day_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_004_extreme_down_day_lvl_21d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rolling_mean(base, 21)

def exdd_005_extreme_down_day_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_005_extreme_down_day_zscore_21d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _zscore_rolling(base, 21)

def exdd_006_extreme_down_day_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_006_extreme_down_day_rank_21d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rank_pct(base, 21)

def exdd_007_extreme_down_day_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_007_extreme_down_day_lvl_63d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rolling_mean(base, 63)

def exdd_008_extreme_down_day_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_008_extreme_down_day_zscore_63d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _zscore_rolling(base, 63)

def exdd_009_extreme_down_day_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_009_extreme_down_day_rank_63d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rank_pct(base, 63)

def exdd_010_extreme_down_day_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_010_extreme_down_day_lvl_126d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rolling_mean(base, 126)

def exdd_011_extreme_down_day_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_011_extreme_down_day_zscore_126d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _zscore_rolling(base, 126)

def exdd_012_extreme_down_day_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_012_extreme_down_day_rank_126d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rank_pct(base, 126)

def exdd_013_extreme_down_day_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_013_extreme_down_day_lvl_252d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rolling_mean(base, 252)

def exdd_014_extreme_down_day_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_014_extreme_down_day_zscore_252d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _zscore_rolling(base, 252)

def exdd_015_extreme_down_day_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_015_extreme_down_day_rank_252d
    ECONOMIC RATIONALE: Frequency of days with >5% drops.
    """
    base = (close.pct_change(1) < -0.05).astype(float)
    return _rank_pct(base, 252)

def exdd_016_extreme_up_day_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_016_extreme_up_day_lvl_5d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rolling_mean(base, 5)

def exdd_017_extreme_up_day_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_017_extreme_up_day_zscore_5d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _zscore_rolling(base, 5)

def exdd_018_extreme_up_day_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_018_extreme_up_day_rank_5d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rank_pct(base, 5)

def exdd_019_extreme_up_day_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_019_extreme_up_day_lvl_21d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rolling_mean(base, 21)

def exdd_020_extreme_up_day_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_020_extreme_up_day_zscore_21d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _zscore_rolling(base, 21)

def exdd_021_extreme_up_day_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_021_extreme_up_day_rank_21d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rank_pct(base, 21)

def exdd_022_extreme_up_day_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_022_extreme_up_day_lvl_63d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rolling_mean(base, 63)

def exdd_023_extreme_up_day_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_023_extreme_up_day_zscore_63d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _zscore_rolling(base, 63)

def exdd_024_extreme_up_day_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_024_extreme_up_day_rank_63d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rank_pct(base, 63)

def exdd_025_extreme_up_day_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_025_extreme_up_day_lvl_126d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rolling_mean(base, 126)

def exdd_026_extreme_up_day_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_026_extreme_up_day_zscore_126d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _zscore_rolling(base, 126)

def exdd_027_extreme_up_day_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_027_extreme_up_day_rank_126d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rank_pct(base, 126)

def exdd_028_extreme_up_day_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_028_extreme_up_day_lvl_252d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rolling_mean(base, 252)

def exdd_029_extreme_up_day_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_029_extreme_up_day_zscore_252d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _zscore_rolling(base, 252)

def exdd_030_extreme_up_day_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_030_extreme_up_day_rank_252d
    ECONOMIC RATIONALE: Frequency of days with >5% gains.
    """
    base = (close.pct_change(1) > 0.05).astype(float)
    return _rank_pct(base, 252)

def exdd_031_extreme_vol_day_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_031_extreme_vol_day_lvl_5d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rolling_mean(base, 5)

def exdd_032_extreme_vol_day_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_032_extreme_vol_day_zscore_5d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _zscore_rolling(base, 5)

def exdd_033_extreme_vol_day_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_033_extreme_vol_day_rank_5d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rank_pct(base, 5)

def exdd_034_extreme_vol_day_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_034_extreme_vol_day_lvl_21d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rolling_mean(base, 21)

def exdd_035_extreme_vol_day_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_035_extreme_vol_day_zscore_21d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _zscore_rolling(base, 21)

def exdd_036_extreme_vol_day_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_036_extreme_vol_day_rank_21d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rank_pct(base, 21)

def exdd_037_extreme_vol_day_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_037_extreme_vol_day_lvl_63d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rolling_mean(base, 63)

def exdd_038_extreme_vol_day_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_038_extreme_vol_day_zscore_63d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _zscore_rolling(base, 63)

def exdd_039_extreme_vol_day_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_039_extreme_vol_day_rank_63d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rank_pct(base, 63)

def exdd_040_extreme_vol_day_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_040_extreme_vol_day_lvl_126d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rolling_mean(base, 126)

def exdd_041_extreme_vol_day_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_041_extreme_vol_day_zscore_126d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _zscore_rolling(base, 126)

def exdd_042_extreme_vol_day_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_042_extreme_vol_day_rank_126d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rank_pct(base, 126)

def exdd_043_extreme_vol_day_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_043_extreme_vol_day_lvl_252d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rolling_mean(base, 252)

def exdd_044_extreme_vol_day_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_044_extreme_vol_day_zscore_252d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _zscore_rolling(base, 252)

def exdd_045_extreme_vol_day_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_045_extreme_vol_day_rank_252d
    ECONOMIC RATIONALE: Frequency of days with >300% average volume.
    """
    base = (volume > volume.rolling(63).mean() * 3).astype(float)
    return _rank_pct(base, 252)

def exdd_046_extreme_day_cluster_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_046_extreme_day_cluster_lvl_5d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rolling_mean(base, 5)

def exdd_047_extreme_day_cluster_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_047_extreme_day_cluster_zscore_5d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _zscore_rolling(base, 5)

def exdd_048_extreme_day_cluster_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_048_extreme_day_cluster_rank_5d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rank_pct(base, 5)

def exdd_049_extreme_day_cluster_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_049_extreme_day_cluster_lvl_21d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rolling_mean(base, 21)

def exdd_050_extreme_day_cluster_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_050_extreme_day_cluster_zscore_21d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _zscore_rolling(base, 21)

def exdd_051_extreme_day_cluster_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_051_extreme_day_cluster_rank_21d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rank_pct(base, 21)

def exdd_052_extreme_day_cluster_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_052_extreme_day_cluster_lvl_63d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rolling_mean(base, 63)

def exdd_053_extreme_day_cluster_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_053_extreme_day_cluster_zscore_63d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _zscore_rolling(base, 63)

def exdd_054_extreme_day_cluster_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_054_extreme_day_cluster_rank_63d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rank_pct(base, 63)

def exdd_055_extreme_day_cluster_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_055_extreme_day_cluster_lvl_126d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rolling_mean(base, 126)

def exdd_056_extreme_day_cluster_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_056_extreme_day_cluster_zscore_126d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _zscore_rolling(base, 126)

def exdd_057_extreme_day_cluster_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_057_extreme_day_cluster_rank_126d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rank_pct(base, 126)

def exdd_058_extreme_day_cluster_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_058_extreme_day_cluster_lvl_252d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rolling_mean(base, 252)

def exdd_059_extreme_day_cluster_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_059_extreme_day_cluster_zscore_252d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _zscore_rolling(base, 252)

def exdd_060_extreme_day_cluster_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_060_extreme_day_cluster_rank_252d
    ECONOMIC RATIONALE: Clustering of high-magnitude price days.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum())
    return _rank_pct(base, 252)

def exdd_061_extreme_day_bias_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_061_extreme_day_bias_lvl_5d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rolling_mean(base, 5)

def exdd_062_extreme_day_bias_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_062_extreme_day_bias_zscore_5d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _zscore_rolling(base, 5)

def exdd_063_extreme_day_bias_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_063_extreme_day_bias_rank_5d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rank_pct(base, 5)

def exdd_064_extreme_day_bias_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_064_extreme_day_bias_lvl_21d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rolling_mean(base, 21)

def exdd_065_extreme_day_bias_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_065_extreme_day_bias_zscore_21d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _zscore_rolling(base, 21)

def exdd_066_extreme_day_bias_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_066_extreme_day_bias_rank_21d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rank_pct(base, 21)

def exdd_067_extreme_day_bias_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_067_extreme_day_bias_lvl_63d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rolling_mean(base, 63)

def exdd_068_extreme_day_bias_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_068_extreme_day_bias_zscore_63d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _zscore_rolling(base, 63)

def exdd_069_extreme_day_bias_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_069_extreme_day_bias_rank_63d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rank_pct(base, 63)

def exdd_070_extreme_day_bias_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_070_extreme_day_bias_lvl_126d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rolling_mean(base, 126)

def exdd_071_extreme_day_bias_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_071_extreme_day_bias_zscore_126d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _zscore_rolling(base, 126)

def exdd_072_extreme_day_bias_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_072_extreme_day_bias_rank_126d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rank_pct(base, 126)

def exdd_073_extreme_day_bias_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_073_extreme_day_bias_lvl_252d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rolling_mean(base, 252)

def exdd_074_extreme_day_bias_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_074_extreme_day_bias_zscore_252d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _zscore_rolling(base, 252)

def exdd_075_extreme_day_bias_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_075_extreme_day_bias_rank_252d
    ECONOMIC RATIONALE: Net density of extreme down vs up days.
    """
    base = ((close.pct_change(1) < -0.05).rolling(63).sum()) - ((close.pct_change(1) > 0.05).rolling(63).sum())
    return _rank_pct(base, 252)

def exdd_076_extreme_vol_price_sync_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_076_extreme_vol_price_sync_lvl_5d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rolling_mean(base, 5)

def exdd_077_extreme_vol_price_sync_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_077_extreme_vol_price_sync_zscore_5d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _zscore_rolling(base, 5)

def exdd_078_extreme_vol_price_sync_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_078_extreme_vol_price_sync_rank_5d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rank_pct(base, 5)

def exdd_079_extreme_vol_price_sync_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_079_extreme_vol_price_sync_lvl_21d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rolling_mean(base, 21)

def exdd_080_extreme_vol_price_sync_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_080_extreme_vol_price_sync_zscore_21d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _zscore_rolling(base, 21)

def exdd_081_extreme_vol_price_sync_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_081_extreme_vol_price_sync_rank_21d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rank_pct(base, 21)

def exdd_082_extreme_vol_price_sync_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_082_extreme_vol_price_sync_lvl_63d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rolling_mean(base, 63)

def exdd_083_extreme_vol_price_sync_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_083_extreme_vol_price_sync_zscore_63d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _zscore_rolling(base, 63)

def exdd_084_extreme_vol_price_sync_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_084_extreme_vol_price_sync_rank_63d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rank_pct(base, 63)

def exdd_085_extreme_vol_price_sync_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_085_extreme_vol_price_sync_lvl_126d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rolling_mean(base, 126)

def exdd_086_extreme_vol_price_sync_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_086_extreme_vol_price_sync_zscore_126d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _zscore_rolling(base, 126)

def exdd_087_extreme_vol_price_sync_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_087_extreme_vol_price_sync_rank_126d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rank_pct(base, 126)

def exdd_088_extreme_vol_price_sync_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_088_extreme_vol_price_sync_lvl_252d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rolling_mean(base, 252)

def exdd_089_extreme_vol_price_sync_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_089_extreme_vol_price_sync_zscore_252d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _zscore_rolling(base, 252)

def exdd_090_extreme_vol_price_sync_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_090_extreme_vol_price_sync_rank_252d
    ECONOMIC RATIONALE: Co-occurrence of extreme drops and high volume.
    """
    base = ((close.pct_change(1) < -0.05) & (volume > volume.rolling(63).mean()*2)).rolling(63).sum()
    return _rank_pct(base, 252)

def exdd_091_extreme_day_z_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_091_extreme_day_z_lvl_5d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rolling_mean(base, 5)

def exdd_092_extreme_day_z_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_092_extreme_day_z_zscore_5d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _zscore_rolling(base, 5)

def exdd_093_extreme_day_z_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_093_extreme_day_z_rank_5d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rank_pct(base, 5)

def exdd_094_extreme_day_z_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_094_extreme_day_z_lvl_21d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rolling_mean(base, 21)

def exdd_095_extreme_day_z_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_095_extreme_day_z_zscore_21d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _zscore_rolling(base, 21)

def exdd_096_extreme_day_z_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_096_extreme_day_z_rank_21d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rank_pct(base, 21)

def exdd_097_extreme_day_z_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_097_extreme_day_z_lvl_63d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rolling_mean(base, 63)

def exdd_098_extreme_day_z_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_098_extreme_day_z_zscore_63d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _zscore_rolling(base, 63)

def exdd_099_extreme_day_z_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_099_extreme_day_z_rank_63d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rank_pct(base, 63)

def exdd_100_extreme_day_z_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_100_extreme_day_z_lvl_126d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rolling_mean(base, 126)

def exdd_101_extreme_day_z_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_101_extreme_day_z_zscore_126d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _zscore_rolling(base, 126)

def exdd_102_extreme_day_z_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_102_extreme_day_z_rank_126d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rank_pct(base, 126)

def exdd_103_extreme_day_z_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_103_extreme_day_z_lvl_252d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rolling_mean(base, 252)

def exdd_104_extreme_day_z_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_104_extreme_day_z_zscore_252d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _zscore_rolling(base, 252)

def exdd_105_extreme_day_z_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_105_extreme_day_z_rank_252d
    ECONOMIC RATIONALE: Abnormality of current extreme day density.
    """
    base = _zscore_rolling((close.pct_change(1).abs() > 0.05).rolling(63).sum(), 252)
    return _rank_pct(base, 252)

def exdd_106_extreme_day_momentum_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_106_extreme_day_momentum_lvl_5d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rolling_mean(base, 5)

def exdd_107_extreme_day_momentum_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_107_extreme_day_momentum_zscore_5d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _zscore_rolling(base, 5)

def exdd_108_extreme_day_momentum_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_108_extreme_day_momentum_rank_5d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rank_pct(base, 5)

def exdd_109_extreme_day_momentum_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_109_extreme_day_momentum_lvl_21d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rolling_mean(base, 21)

def exdd_110_extreme_day_momentum_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_110_extreme_day_momentum_zscore_21d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _zscore_rolling(base, 21)

def exdd_111_extreme_day_momentum_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_111_extreme_day_momentum_rank_21d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rank_pct(base, 21)

def exdd_112_extreme_day_momentum_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_112_extreme_day_momentum_lvl_63d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rolling_mean(base, 63)

def exdd_113_extreme_day_momentum_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_113_extreme_day_momentum_zscore_63d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _zscore_rolling(base, 63)

def exdd_114_extreme_day_momentum_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_114_extreme_day_momentum_rank_63d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rank_pct(base, 63)

def exdd_115_extreme_day_momentum_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_115_extreme_day_momentum_lvl_126d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rolling_mean(base, 126)

def exdd_116_extreme_day_momentum_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_116_extreme_day_momentum_zscore_126d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _zscore_rolling(base, 126)

def exdd_117_extreme_day_momentum_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_117_extreme_day_momentum_rank_126d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rank_pct(base, 126)

def exdd_118_extreme_day_momentum_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_118_extreme_day_momentum_lvl_252d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rolling_mean(base, 252)

def exdd_119_extreme_day_momentum_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_119_extreme_day_momentum_zscore_252d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _zscore_rolling(base, 252)

def exdd_120_extreme_day_momentum_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    exdd_120_extreme_day_momentum_rank_252d
    ECONOMIC RATIONALE: Change in extreme day frequency.
    """
    base = ((close.pct_change(1).abs() > 0.05).rolling(21).sum()).diff(21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V116_REGISTRY_1 = {
    "exdd_001_extreme_down_day_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_001_extreme_down_day_lvl_5d},
    "exdd_002_extreme_down_day_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_002_extreme_down_day_zscore_5d},
    "exdd_003_extreme_down_day_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_003_extreme_down_day_rank_5d},
    "exdd_004_extreme_down_day_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_004_extreme_down_day_lvl_21d},
    "exdd_005_extreme_down_day_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_005_extreme_down_day_zscore_21d},
    "exdd_006_extreme_down_day_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_006_extreme_down_day_rank_21d},
    "exdd_007_extreme_down_day_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_007_extreme_down_day_lvl_63d},
    "exdd_008_extreme_down_day_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_008_extreme_down_day_zscore_63d},
    "exdd_009_extreme_down_day_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_009_extreme_down_day_rank_63d},
    "exdd_010_extreme_down_day_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_010_extreme_down_day_lvl_126d},
    "exdd_011_extreme_down_day_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_011_extreme_down_day_zscore_126d},
    "exdd_012_extreme_down_day_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_012_extreme_down_day_rank_126d},
    "exdd_013_extreme_down_day_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_013_extreme_down_day_lvl_252d},
    "exdd_014_extreme_down_day_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_014_extreme_down_day_zscore_252d},
    "exdd_015_extreme_down_day_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_015_extreme_down_day_rank_252d},
    "exdd_016_extreme_up_day_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_016_extreme_up_day_lvl_5d},
    "exdd_017_extreme_up_day_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_017_extreme_up_day_zscore_5d},
    "exdd_018_extreme_up_day_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_018_extreme_up_day_rank_5d},
    "exdd_019_extreme_up_day_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_019_extreme_up_day_lvl_21d},
    "exdd_020_extreme_up_day_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_020_extreme_up_day_zscore_21d},
    "exdd_021_extreme_up_day_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_021_extreme_up_day_rank_21d},
    "exdd_022_extreme_up_day_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_022_extreme_up_day_lvl_63d},
    "exdd_023_extreme_up_day_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_023_extreme_up_day_zscore_63d},
    "exdd_024_extreme_up_day_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_024_extreme_up_day_rank_63d},
    "exdd_025_extreme_up_day_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_025_extreme_up_day_lvl_126d},
    "exdd_026_extreme_up_day_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_026_extreme_up_day_zscore_126d},
    "exdd_027_extreme_up_day_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_027_extreme_up_day_rank_126d},
    "exdd_028_extreme_up_day_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_028_extreme_up_day_lvl_252d},
    "exdd_029_extreme_up_day_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_029_extreme_up_day_zscore_252d},
    "exdd_030_extreme_up_day_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_030_extreme_up_day_rank_252d},
    "exdd_031_extreme_vol_day_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_031_extreme_vol_day_lvl_5d},
    "exdd_032_extreme_vol_day_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_032_extreme_vol_day_zscore_5d},
    "exdd_033_extreme_vol_day_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_033_extreme_vol_day_rank_5d},
    "exdd_034_extreme_vol_day_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_034_extreme_vol_day_lvl_21d},
    "exdd_035_extreme_vol_day_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_035_extreme_vol_day_zscore_21d},
    "exdd_036_extreme_vol_day_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_036_extreme_vol_day_rank_21d},
    "exdd_037_extreme_vol_day_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_037_extreme_vol_day_lvl_63d},
    "exdd_038_extreme_vol_day_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_038_extreme_vol_day_zscore_63d},
    "exdd_039_extreme_vol_day_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_039_extreme_vol_day_rank_63d},
    "exdd_040_extreme_vol_day_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_040_extreme_vol_day_lvl_126d},
    "exdd_041_extreme_vol_day_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_041_extreme_vol_day_zscore_126d},
    "exdd_042_extreme_vol_day_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_042_extreme_vol_day_rank_126d},
    "exdd_043_extreme_vol_day_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_043_extreme_vol_day_lvl_252d},
    "exdd_044_extreme_vol_day_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_044_extreme_vol_day_zscore_252d},
    "exdd_045_extreme_vol_day_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_045_extreme_vol_day_rank_252d},
    "exdd_046_extreme_day_cluster_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_046_extreme_day_cluster_lvl_5d},
    "exdd_047_extreme_day_cluster_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_047_extreme_day_cluster_zscore_5d},
    "exdd_048_extreme_day_cluster_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_048_extreme_day_cluster_rank_5d},
    "exdd_049_extreme_day_cluster_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_049_extreme_day_cluster_lvl_21d},
    "exdd_050_extreme_day_cluster_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_050_extreme_day_cluster_zscore_21d},
    "exdd_051_extreme_day_cluster_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_051_extreme_day_cluster_rank_21d},
    "exdd_052_extreme_day_cluster_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_052_extreme_day_cluster_lvl_63d},
    "exdd_053_extreme_day_cluster_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_053_extreme_day_cluster_zscore_63d},
    "exdd_054_extreme_day_cluster_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_054_extreme_day_cluster_rank_63d},
    "exdd_055_extreme_day_cluster_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_055_extreme_day_cluster_lvl_126d},
    "exdd_056_extreme_day_cluster_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_056_extreme_day_cluster_zscore_126d},
    "exdd_057_extreme_day_cluster_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_057_extreme_day_cluster_rank_126d},
    "exdd_058_extreme_day_cluster_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_058_extreme_day_cluster_lvl_252d},
    "exdd_059_extreme_day_cluster_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_059_extreme_day_cluster_zscore_252d},
    "exdd_060_extreme_day_cluster_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_060_extreme_day_cluster_rank_252d},
    "exdd_061_extreme_day_bias_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_061_extreme_day_bias_lvl_5d},
    "exdd_062_extreme_day_bias_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_062_extreme_day_bias_zscore_5d},
    "exdd_063_extreme_day_bias_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_063_extreme_day_bias_rank_5d},
    "exdd_064_extreme_day_bias_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_064_extreme_day_bias_lvl_21d},
    "exdd_065_extreme_day_bias_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_065_extreme_day_bias_zscore_21d},
    "exdd_066_extreme_day_bias_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_066_extreme_day_bias_rank_21d},
    "exdd_067_extreme_day_bias_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_067_extreme_day_bias_lvl_63d},
    "exdd_068_extreme_day_bias_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_068_extreme_day_bias_zscore_63d},
    "exdd_069_extreme_day_bias_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_069_extreme_day_bias_rank_63d},
    "exdd_070_extreme_day_bias_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_070_extreme_day_bias_lvl_126d},
    "exdd_071_extreme_day_bias_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_071_extreme_day_bias_zscore_126d},
    "exdd_072_extreme_day_bias_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_072_extreme_day_bias_rank_126d},
    "exdd_073_extreme_day_bias_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_073_extreme_day_bias_lvl_252d},
    "exdd_074_extreme_day_bias_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_074_extreme_day_bias_zscore_252d},
    "exdd_075_extreme_day_bias_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_075_extreme_day_bias_rank_252d},
    "exdd_076_extreme_vol_price_sync_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_076_extreme_vol_price_sync_lvl_5d},
    "exdd_077_extreme_vol_price_sync_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_077_extreme_vol_price_sync_zscore_5d},
    "exdd_078_extreme_vol_price_sync_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_078_extreme_vol_price_sync_rank_5d},
    "exdd_079_extreme_vol_price_sync_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_079_extreme_vol_price_sync_lvl_21d},
    "exdd_080_extreme_vol_price_sync_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_080_extreme_vol_price_sync_zscore_21d},
    "exdd_081_extreme_vol_price_sync_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_081_extreme_vol_price_sync_rank_21d},
    "exdd_082_extreme_vol_price_sync_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_082_extreme_vol_price_sync_lvl_63d},
    "exdd_083_extreme_vol_price_sync_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_083_extreme_vol_price_sync_zscore_63d},
    "exdd_084_extreme_vol_price_sync_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_084_extreme_vol_price_sync_rank_63d},
    "exdd_085_extreme_vol_price_sync_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_085_extreme_vol_price_sync_lvl_126d},
    "exdd_086_extreme_vol_price_sync_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_086_extreme_vol_price_sync_zscore_126d},
    "exdd_087_extreme_vol_price_sync_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_087_extreme_vol_price_sync_rank_126d},
    "exdd_088_extreme_vol_price_sync_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_088_extreme_vol_price_sync_lvl_252d},
    "exdd_089_extreme_vol_price_sync_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_089_extreme_vol_price_sync_zscore_252d},
    "exdd_090_extreme_vol_price_sync_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_090_extreme_vol_price_sync_rank_252d},
    "exdd_091_extreme_day_z_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_091_extreme_day_z_lvl_5d},
    "exdd_092_extreme_day_z_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_092_extreme_day_z_zscore_5d},
    "exdd_093_extreme_day_z_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_093_extreme_day_z_rank_5d},
    "exdd_094_extreme_day_z_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_094_extreme_day_z_lvl_21d},
    "exdd_095_extreme_day_z_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_095_extreme_day_z_zscore_21d},
    "exdd_096_extreme_day_z_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_096_extreme_day_z_rank_21d},
    "exdd_097_extreme_day_z_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_097_extreme_day_z_lvl_63d},
    "exdd_098_extreme_day_z_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_098_extreme_day_z_zscore_63d},
    "exdd_099_extreme_day_z_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_099_extreme_day_z_rank_63d},
    "exdd_100_extreme_day_z_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_100_extreme_day_z_lvl_126d},
    "exdd_101_extreme_day_z_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_101_extreme_day_z_zscore_126d},
    "exdd_102_extreme_day_z_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_102_extreme_day_z_rank_126d},
    "exdd_103_extreme_day_z_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_103_extreme_day_z_lvl_252d},
    "exdd_104_extreme_day_z_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_104_extreme_day_z_zscore_252d},
    "exdd_105_extreme_day_z_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_105_extreme_day_z_rank_252d},
    "exdd_106_extreme_day_momentum_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_106_extreme_day_momentum_lvl_5d},
    "exdd_107_extreme_day_momentum_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_107_extreme_day_momentum_zscore_5d},
    "exdd_108_extreme_day_momentum_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_108_extreme_day_momentum_rank_5d},
    "exdd_109_extreme_day_momentum_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_109_extreme_day_momentum_lvl_21d},
    "exdd_110_extreme_day_momentum_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_110_extreme_day_momentum_zscore_21d},
    "exdd_111_extreme_day_momentum_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_111_extreme_day_momentum_rank_21d},
    "exdd_112_extreme_day_momentum_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_112_extreme_day_momentum_lvl_63d},
    "exdd_113_extreme_day_momentum_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_113_extreme_day_momentum_zscore_63d},
    "exdd_114_extreme_day_momentum_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_114_extreme_day_momentum_rank_63d},
    "exdd_115_extreme_day_momentum_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_115_extreme_day_momentum_lvl_126d},
    "exdd_116_extreme_day_momentum_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_116_extreme_day_momentum_zscore_126d},
    "exdd_117_extreme_day_momentum_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_117_extreme_day_momentum_rank_126d},
    "exdd_118_extreme_day_momentum_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_118_extreme_day_momentum_lvl_252d},
    "exdd_119_extreme_day_momentum_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_119_extreme_day_momentum_zscore_252d},
    "exdd_120_extreme_day_momentum_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": exdd_120_extreme_day_momentum_rank_252d},
}
