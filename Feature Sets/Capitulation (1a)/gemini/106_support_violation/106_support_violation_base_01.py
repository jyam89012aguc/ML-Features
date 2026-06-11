"""
106_support_violation — Base Features Part 1
Domain: support_violation
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

def supv_001_support_252d_break_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_001_support_252d_break_lvl_5d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rolling_mean(base, 5)

def supv_002_support_252d_break_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_002_support_252d_break_zscore_5d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _zscore_rolling(base, 5)

def supv_003_support_252d_break_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_003_support_252d_break_rank_5d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rank_pct(base, 5)

def supv_004_support_252d_break_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_004_support_252d_break_lvl_21d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rolling_mean(base, 21)

def supv_005_support_252d_break_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_005_support_252d_break_zscore_21d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _zscore_rolling(base, 21)

def supv_006_support_252d_break_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_006_support_252d_break_rank_21d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rank_pct(base, 21)

def supv_007_support_252d_break_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_007_support_252d_break_lvl_63d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rolling_mean(base, 63)

def supv_008_support_252d_break_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_008_support_252d_break_zscore_63d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _zscore_rolling(base, 63)

def supv_009_support_252d_break_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_009_support_252d_break_rank_63d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rank_pct(base, 63)

def supv_010_support_252d_break_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_010_support_252d_break_lvl_126d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rolling_mean(base, 126)

def supv_011_support_252d_break_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_011_support_252d_break_zscore_126d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _zscore_rolling(base, 126)

def supv_012_support_252d_break_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_012_support_252d_break_rank_126d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rank_pct(base, 126)

def supv_013_support_252d_break_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_013_support_252d_break_lvl_252d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rolling_mean(base, 252)

def supv_014_support_252d_break_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_014_support_252d_break_zscore_252d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _zscore_rolling(base, 252)

def supv_015_support_252d_break_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_015_support_252d_break_rank_252d
    ECONOMIC RATIONALE: Violation of the 52-week low.
    """
    base = (low < low.rolling(252).min().shift(1)).astype(float)
    return _rank_pct(base, 252)

def supv_016_support_63d_break_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_016_support_63d_break_lvl_5d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 5)

def supv_017_support_63d_break_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_017_support_63d_break_zscore_5d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 5)

def supv_018_support_63d_break_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_018_support_63d_break_rank_5d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 5)

def supv_019_support_63d_break_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_019_support_63d_break_lvl_21d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 21)

def supv_020_support_63d_break_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_020_support_63d_break_zscore_21d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 21)

def supv_021_support_63d_break_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_021_support_63d_break_rank_21d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 21)

def supv_022_support_63d_break_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_022_support_63d_break_lvl_63d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 63)

def supv_023_support_63d_break_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_023_support_63d_break_zscore_63d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 63)

def supv_024_support_63d_break_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_024_support_63d_break_rank_63d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 63)

def supv_025_support_63d_break_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_025_support_63d_break_lvl_126d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 126)

def supv_026_support_63d_break_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_026_support_63d_break_zscore_126d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 126)

def supv_027_support_63d_break_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_027_support_63d_break_rank_126d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 126)

def supv_028_support_63d_break_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_028_support_63d_break_lvl_252d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 252)

def supv_029_support_63d_break_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_029_support_63d_break_zscore_252d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 252)

def supv_030_support_63d_break_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_030_support_63d_break_rank_252d
    ECONOMIC RATIONALE: Violation of quarterly support.
    """
    base = (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 252)

def supv_031_volume_on_breakout_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_031_volume_on_breakout_lvl_5d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 5)

def supv_032_volume_on_breakout_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_032_volume_on_breakout_zscore_5d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 5)

def supv_033_volume_on_breakout_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_033_volume_on_breakout_rank_5d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 5)

def supv_034_volume_on_breakout_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_034_volume_on_breakout_lvl_21d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 21)

def supv_035_volume_on_breakout_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_035_volume_on_breakout_zscore_21d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 21)

def supv_036_volume_on_breakout_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_036_volume_on_breakout_rank_21d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 21)

def supv_037_volume_on_breakout_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_037_volume_on_breakout_lvl_63d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 63)

def supv_038_volume_on_breakout_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_038_volume_on_breakout_zscore_63d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 63)

def supv_039_volume_on_breakout_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_039_volume_on_breakout_rank_63d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 63)

def supv_040_volume_on_breakout_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_040_volume_on_breakout_lvl_126d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 126)

def supv_041_volume_on_breakout_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_041_volume_on_breakout_zscore_126d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 126)

def supv_042_volume_on_breakout_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_042_volume_on_breakout_rank_126d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 126)

def supv_043_volume_on_breakout_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_043_volume_on_breakout_lvl_252d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rolling_mean(base, 252)

def supv_044_volume_on_breakout_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_044_volume_on_breakout_zscore_252d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _zscore_rolling(base, 252)

def supv_045_volume_on_breakout_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_045_volume_on_breakout_rank_252d
    ECONOMIC RATIONALE: Volume intensity during support violation.
    """
    base = volume / volume.rolling(63).mean() * (low < low.rolling(63).min().shift(1)).astype(float)
    return _rank_pct(base, 252)

def supv_046_support_proximity_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_046_support_proximity_lvl_5d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rolling_mean(base, 5)

def supv_047_support_proximity_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_047_support_proximity_zscore_5d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _zscore_rolling(base, 5)

def supv_048_support_proximity_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_048_support_proximity_rank_5d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rank_pct(base, 5)

def supv_049_support_proximity_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_049_support_proximity_lvl_21d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rolling_mean(base, 21)

def supv_050_support_proximity_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_050_support_proximity_zscore_21d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _zscore_rolling(base, 21)

def supv_051_support_proximity_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_051_support_proximity_rank_21d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rank_pct(base, 21)

def supv_052_support_proximity_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_052_support_proximity_lvl_63d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rolling_mean(base, 63)

def supv_053_support_proximity_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_053_support_proximity_zscore_63d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _zscore_rolling(base, 63)

def supv_054_support_proximity_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_054_support_proximity_rank_63d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rank_pct(base, 63)

def supv_055_support_proximity_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_055_support_proximity_lvl_126d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rolling_mean(base, 126)

def supv_056_support_proximity_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_056_support_proximity_zscore_126d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _zscore_rolling(base, 126)

def supv_057_support_proximity_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_057_support_proximity_rank_126d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rank_pct(base, 126)

def supv_058_support_proximity_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_058_support_proximity_lvl_252d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rolling_mean(base, 252)

def supv_059_support_proximity_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_059_support_proximity_zscore_252d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _zscore_rolling(base, 252)

def supv_060_support_proximity_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_060_support_proximity_rank_252d
    ECONOMIC RATIONALE: Closeness to major support levels.
    """
    base = (close - low.rolling(63).min()) / close
    return _rank_pct(base, 252)

def supv_061_support_bounce_failure_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_061_support_bounce_failure_lvl_5d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rolling_mean(base, 5)

def supv_062_support_bounce_failure_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_062_support_bounce_failure_zscore_5d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _zscore_rolling(base, 5)

def supv_063_support_bounce_failure_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_063_support_bounce_failure_rank_5d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rank_pct(base, 5)

def supv_064_support_bounce_failure_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_064_support_bounce_failure_lvl_21d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rolling_mean(base, 21)

def supv_065_support_bounce_failure_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_065_support_bounce_failure_zscore_21d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _zscore_rolling(base, 21)

def supv_066_support_bounce_failure_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_066_support_bounce_failure_rank_21d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rank_pct(base, 21)

def supv_067_support_bounce_failure_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_067_support_bounce_failure_lvl_63d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rolling_mean(base, 63)

def supv_068_support_bounce_failure_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_068_support_bounce_failure_zscore_63d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _zscore_rolling(base, 63)

def supv_069_support_bounce_failure_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_069_support_bounce_failure_rank_63d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rank_pct(base, 63)

def supv_070_support_bounce_failure_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_070_support_bounce_failure_lvl_126d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rolling_mean(base, 126)

def supv_071_support_bounce_failure_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_071_support_bounce_failure_zscore_126d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _zscore_rolling(base, 126)

def supv_072_support_bounce_failure_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_072_support_bounce_failure_rank_126d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rank_pct(base, 126)

def supv_073_support_bounce_failure_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_073_support_bounce_failure_lvl_252d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rolling_mean(base, 252)

def supv_074_support_bounce_failure_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_074_support_bounce_failure_zscore_252d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _zscore_rolling(base, 252)

def supv_075_support_bounce_failure_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_075_support_bounce_failure_rank_252d
    ECONOMIC RATIONALE: Failure to rally significantly after hitting support.
    """
    base = (close / low.rolling(63).min() - 1) < 0.02
    return _rank_pct(base, 252)

def supv_076_multiple_support_test_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_076_multiple_support_test_lvl_5d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rolling_mean(base, 5)

def supv_077_multiple_support_test_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_077_multiple_support_test_zscore_5d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _zscore_rolling(base, 5)

def supv_078_multiple_support_test_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_078_multiple_support_test_rank_5d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rank_pct(base, 5)

def supv_079_multiple_support_test_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_079_multiple_support_test_lvl_21d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rolling_mean(base, 21)

def supv_080_multiple_support_test_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_080_multiple_support_test_zscore_21d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _zscore_rolling(base, 21)

def supv_081_multiple_support_test_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_081_multiple_support_test_rank_21d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rank_pct(base, 21)

def supv_082_multiple_support_test_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_082_multiple_support_test_lvl_63d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rolling_mean(base, 63)

def supv_083_multiple_support_test_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_083_multiple_support_test_zscore_63d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _zscore_rolling(base, 63)

def supv_084_multiple_support_test_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_084_multiple_support_test_rank_63d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rank_pct(base, 63)

def supv_085_multiple_support_test_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_085_multiple_support_test_lvl_126d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rolling_mean(base, 126)

def supv_086_multiple_support_test_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_086_multiple_support_test_zscore_126d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _zscore_rolling(base, 126)

def supv_087_multiple_support_test_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_087_multiple_support_test_rank_126d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rank_pct(base, 126)

def supv_088_multiple_support_test_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_088_multiple_support_test_lvl_252d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rolling_mean(base, 252)

def supv_089_multiple_support_test_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_089_multiple_support_test_zscore_252d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _zscore_rolling(base, 252)

def supv_090_multiple_support_test_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_090_multiple_support_test_rank_252d
    ECONOMIC RATIONALE: Frequency of new lows being made.
    """
    base = ((low < low.rolling(21).min().shift(1)).rolling(63).sum())
    return _rank_pct(base, 252)

def supv_091_support_zone_density_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_091_support_zone_density_lvl_5d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rolling_mean(base, 5)

def supv_092_support_zone_density_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_092_support_zone_density_zscore_5d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _zscore_rolling(base, 5)

def supv_093_support_zone_density_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_093_support_zone_density_rank_5d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rank_pct(base, 5)

def supv_094_support_zone_density_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_094_support_zone_density_lvl_21d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rolling_mean(base, 21)

def supv_095_support_zone_density_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_095_support_zone_density_zscore_21d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _zscore_rolling(base, 21)

def supv_096_support_zone_density_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_096_support_zone_density_rank_21d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rank_pct(base, 21)

def supv_097_support_zone_density_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_097_support_zone_density_lvl_63d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rolling_mean(base, 63)

def supv_098_support_zone_density_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_098_support_zone_density_zscore_63d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _zscore_rolling(base, 63)

def supv_099_support_zone_density_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_099_support_zone_density_rank_63d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rank_pct(base, 63)

def supv_100_support_zone_density_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_100_support_zone_density_lvl_126d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rolling_mean(base, 126)

def supv_101_support_zone_density_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_101_support_zone_density_zscore_126d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _zscore_rolling(base, 126)

def supv_102_support_zone_density_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_102_support_zone_density_rank_126d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rank_pct(base, 126)

def supv_103_support_zone_density_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_103_support_zone_density_lvl_252d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rolling_mean(base, 252)

def supv_104_support_zone_density_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_104_support_zone_density_zscore_252d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _zscore_rolling(base, 252)

def supv_105_support_zone_density_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_105_support_zone_density_rank_252d
    ECONOMIC RATIONALE: Time spent near support zones.
    """
    base = ((low < low.rolling(63).min() * 1.02).rolling(21).sum())
    return _rank_pct(base, 252)

def supv_106_breakdown_momentum_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_106_breakdown_momentum_lvl_5d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rolling_mean(base, 5)

def supv_107_breakdown_momentum_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_107_breakdown_momentum_zscore_5d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _zscore_rolling(base, 5)

def supv_108_breakdown_momentum_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_108_breakdown_momentum_rank_5d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rank_pct(base, 5)

def supv_109_breakdown_momentum_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_109_breakdown_momentum_lvl_21d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rolling_mean(base, 21)

def supv_110_breakdown_momentum_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_110_breakdown_momentum_zscore_21d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _zscore_rolling(base, 21)

def supv_111_breakdown_momentum_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_111_breakdown_momentum_rank_21d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rank_pct(base, 21)

def supv_112_breakdown_momentum_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_112_breakdown_momentum_lvl_63d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rolling_mean(base, 63)

def supv_113_breakdown_momentum_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_113_breakdown_momentum_zscore_63d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _zscore_rolling(base, 63)

def supv_114_breakdown_momentum_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_114_breakdown_momentum_rank_63d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rank_pct(base, 63)

def supv_115_breakdown_momentum_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_115_breakdown_momentum_lvl_126d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rolling_mean(base, 126)

def supv_116_breakdown_momentum_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_116_breakdown_momentum_zscore_126d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _zscore_rolling(base, 126)

def supv_117_breakdown_momentum_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_117_breakdown_momentum_rank_126d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rank_pct(base, 126)

def supv_118_breakdown_momentum_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_118_breakdown_momentum_lvl_252d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rolling_mean(base, 252)

def supv_119_breakdown_momentum_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_119_breakdown_momentum_zscore_252d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _zscore_rolling(base, 252)

def supv_120_breakdown_momentum_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    supv_120_breakdown_momentum_rank_252d
    ECONOMIC RATIONALE: Speed of price drop following support break.
    """
    base = close.pct_change(5) * (low < low.rolling(21).min().shift(1)).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V106_REGISTRY_1 = {
    "supv_001_support_252d_break_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_001_support_252d_break_lvl_5d},
    "supv_002_support_252d_break_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_002_support_252d_break_zscore_5d},
    "supv_003_support_252d_break_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_003_support_252d_break_rank_5d},
    "supv_004_support_252d_break_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_004_support_252d_break_lvl_21d},
    "supv_005_support_252d_break_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_005_support_252d_break_zscore_21d},
    "supv_006_support_252d_break_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_006_support_252d_break_rank_21d},
    "supv_007_support_252d_break_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_007_support_252d_break_lvl_63d},
    "supv_008_support_252d_break_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_008_support_252d_break_zscore_63d},
    "supv_009_support_252d_break_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_009_support_252d_break_rank_63d},
    "supv_010_support_252d_break_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_010_support_252d_break_lvl_126d},
    "supv_011_support_252d_break_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_011_support_252d_break_zscore_126d},
    "supv_012_support_252d_break_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_012_support_252d_break_rank_126d},
    "supv_013_support_252d_break_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_013_support_252d_break_lvl_252d},
    "supv_014_support_252d_break_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_014_support_252d_break_zscore_252d},
    "supv_015_support_252d_break_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_015_support_252d_break_rank_252d},
    "supv_016_support_63d_break_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_016_support_63d_break_lvl_5d},
    "supv_017_support_63d_break_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_017_support_63d_break_zscore_5d},
    "supv_018_support_63d_break_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_018_support_63d_break_rank_5d},
    "supv_019_support_63d_break_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_019_support_63d_break_lvl_21d},
    "supv_020_support_63d_break_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_020_support_63d_break_zscore_21d},
    "supv_021_support_63d_break_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_021_support_63d_break_rank_21d},
    "supv_022_support_63d_break_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_022_support_63d_break_lvl_63d},
    "supv_023_support_63d_break_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_023_support_63d_break_zscore_63d},
    "supv_024_support_63d_break_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_024_support_63d_break_rank_63d},
    "supv_025_support_63d_break_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_025_support_63d_break_lvl_126d},
    "supv_026_support_63d_break_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_026_support_63d_break_zscore_126d},
    "supv_027_support_63d_break_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_027_support_63d_break_rank_126d},
    "supv_028_support_63d_break_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_028_support_63d_break_lvl_252d},
    "supv_029_support_63d_break_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_029_support_63d_break_zscore_252d},
    "supv_030_support_63d_break_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_030_support_63d_break_rank_252d},
    "supv_031_volume_on_breakout_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_031_volume_on_breakout_lvl_5d},
    "supv_032_volume_on_breakout_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_032_volume_on_breakout_zscore_5d},
    "supv_033_volume_on_breakout_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_033_volume_on_breakout_rank_5d},
    "supv_034_volume_on_breakout_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_034_volume_on_breakout_lvl_21d},
    "supv_035_volume_on_breakout_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_035_volume_on_breakout_zscore_21d},
    "supv_036_volume_on_breakout_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_036_volume_on_breakout_rank_21d},
    "supv_037_volume_on_breakout_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_037_volume_on_breakout_lvl_63d},
    "supv_038_volume_on_breakout_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_038_volume_on_breakout_zscore_63d},
    "supv_039_volume_on_breakout_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_039_volume_on_breakout_rank_63d},
    "supv_040_volume_on_breakout_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_040_volume_on_breakout_lvl_126d},
    "supv_041_volume_on_breakout_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_041_volume_on_breakout_zscore_126d},
    "supv_042_volume_on_breakout_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_042_volume_on_breakout_rank_126d},
    "supv_043_volume_on_breakout_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_043_volume_on_breakout_lvl_252d},
    "supv_044_volume_on_breakout_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_044_volume_on_breakout_zscore_252d},
    "supv_045_volume_on_breakout_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_045_volume_on_breakout_rank_252d},
    "supv_046_support_proximity_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_046_support_proximity_lvl_5d},
    "supv_047_support_proximity_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_047_support_proximity_zscore_5d},
    "supv_048_support_proximity_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_048_support_proximity_rank_5d},
    "supv_049_support_proximity_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_049_support_proximity_lvl_21d},
    "supv_050_support_proximity_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_050_support_proximity_zscore_21d},
    "supv_051_support_proximity_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_051_support_proximity_rank_21d},
    "supv_052_support_proximity_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_052_support_proximity_lvl_63d},
    "supv_053_support_proximity_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_053_support_proximity_zscore_63d},
    "supv_054_support_proximity_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_054_support_proximity_rank_63d},
    "supv_055_support_proximity_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_055_support_proximity_lvl_126d},
    "supv_056_support_proximity_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_056_support_proximity_zscore_126d},
    "supv_057_support_proximity_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_057_support_proximity_rank_126d},
    "supv_058_support_proximity_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_058_support_proximity_lvl_252d},
    "supv_059_support_proximity_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_059_support_proximity_zscore_252d},
    "supv_060_support_proximity_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_060_support_proximity_rank_252d},
    "supv_061_support_bounce_failure_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_061_support_bounce_failure_lvl_5d},
    "supv_062_support_bounce_failure_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_062_support_bounce_failure_zscore_5d},
    "supv_063_support_bounce_failure_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_063_support_bounce_failure_rank_5d},
    "supv_064_support_bounce_failure_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_064_support_bounce_failure_lvl_21d},
    "supv_065_support_bounce_failure_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_065_support_bounce_failure_zscore_21d},
    "supv_066_support_bounce_failure_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_066_support_bounce_failure_rank_21d},
    "supv_067_support_bounce_failure_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_067_support_bounce_failure_lvl_63d},
    "supv_068_support_bounce_failure_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_068_support_bounce_failure_zscore_63d},
    "supv_069_support_bounce_failure_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_069_support_bounce_failure_rank_63d},
    "supv_070_support_bounce_failure_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_070_support_bounce_failure_lvl_126d},
    "supv_071_support_bounce_failure_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_071_support_bounce_failure_zscore_126d},
    "supv_072_support_bounce_failure_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_072_support_bounce_failure_rank_126d},
    "supv_073_support_bounce_failure_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_073_support_bounce_failure_lvl_252d},
    "supv_074_support_bounce_failure_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_074_support_bounce_failure_zscore_252d},
    "supv_075_support_bounce_failure_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_075_support_bounce_failure_rank_252d},
    "supv_076_multiple_support_test_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_076_multiple_support_test_lvl_5d},
    "supv_077_multiple_support_test_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_077_multiple_support_test_zscore_5d},
    "supv_078_multiple_support_test_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_078_multiple_support_test_rank_5d},
    "supv_079_multiple_support_test_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_079_multiple_support_test_lvl_21d},
    "supv_080_multiple_support_test_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_080_multiple_support_test_zscore_21d},
    "supv_081_multiple_support_test_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_081_multiple_support_test_rank_21d},
    "supv_082_multiple_support_test_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_082_multiple_support_test_lvl_63d},
    "supv_083_multiple_support_test_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_083_multiple_support_test_zscore_63d},
    "supv_084_multiple_support_test_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_084_multiple_support_test_rank_63d},
    "supv_085_multiple_support_test_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_085_multiple_support_test_lvl_126d},
    "supv_086_multiple_support_test_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_086_multiple_support_test_zscore_126d},
    "supv_087_multiple_support_test_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_087_multiple_support_test_rank_126d},
    "supv_088_multiple_support_test_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_088_multiple_support_test_lvl_252d},
    "supv_089_multiple_support_test_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_089_multiple_support_test_zscore_252d},
    "supv_090_multiple_support_test_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_090_multiple_support_test_rank_252d},
    "supv_091_support_zone_density_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_091_support_zone_density_lvl_5d},
    "supv_092_support_zone_density_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_092_support_zone_density_zscore_5d},
    "supv_093_support_zone_density_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_093_support_zone_density_rank_5d},
    "supv_094_support_zone_density_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_094_support_zone_density_lvl_21d},
    "supv_095_support_zone_density_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_095_support_zone_density_zscore_21d},
    "supv_096_support_zone_density_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_096_support_zone_density_rank_21d},
    "supv_097_support_zone_density_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_097_support_zone_density_lvl_63d},
    "supv_098_support_zone_density_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_098_support_zone_density_zscore_63d},
    "supv_099_support_zone_density_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_099_support_zone_density_rank_63d},
    "supv_100_support_zone_density_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_100_support_zone_density_lvl_126d},
    "supv_101_support_zone_density_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_101_support_zone_density_zscore_126d},
    "supv_102_support_zone_density_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_102_support_zone_density_rank_126d},
    "supv_103_support_zone_density_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_103_support_zone_density_lvl_252d},
    "supv_104_support_zone_density_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_104_support_zone_density_zscore_252d},
    "supv_105_support_zone_density_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_105_support_zone_density_rank_252d},
    "supv_106_breakdown_momentum_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_106_breakdown_momentum_lvl_5d},
    "supv_107_breakdown_momentum_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_107_breakdown_momentum_zscore_5d},
    "supv_108_breakdown_momentum_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_108_breakdown_momentum_rank_5d},
    "supv_109_breakdown_momentum_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_109_breakdown_momentum_lvl_21d},
    "supv_110_breakdown_momentum_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_110_breakdown_momentum_zscore_21d},
    "supv_111_breakdown_momentum_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_111_breakdown_momentum_rank_21d},
    "supv_112_breakdown_momentum_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_112_breakdown_momentum_lvl_63d},
    "supv_113_breakdown_momentum_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_113_breakdown_momentum_zscore_63d},
    "supv_114_breakdown_momentum_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_114_breakdown_momentum_rank_63d},
    "supv_115_breakdown_momentum_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_115_breakdown_momentum_lvl_126d},
    "supv_116_breakdown_momentum_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_116_breakdown_momentum_zscore_126d},
    "supv_117_breakdown_momentum_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_117_breakdown_momentum_rank_126d},
    "supv_118_breakdown_momentum_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_118_breakdown_momentum_lvl_252d},
    "supv_119_breakdown_momentum_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_119_breakdown_momentum_zscore_252d},
    "supv_120_breakdown_momentum_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": supv_120_breakdown_momentum_rank_252d},
}
