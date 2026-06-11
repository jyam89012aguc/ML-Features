"""
101_wyckoff_capitulation_structure — Base Features Part 1
Domain: wyckoff_capitulation_structure
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

def wyck_001_selling_climax_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_001_selling_climax_lvl_5d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rolling_mean(base, 5)

def wyck_002_selling_climax_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_002_selling_climax_zscore_5d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _zscore_rolling(base, 5)

def wyck_003_selling_climax_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_003_selling_climax_rank_5d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rank_pct(base, 5)

def wyck_004_selling_climax_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_004_selling_climax_lvl_21d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rolling_mean(base, 21)

def wyck_005_selling_climax_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_005_selling_climax_zscore_21d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _zscore_rolling(base, 21)

def wyck_006_selling_climax_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_006_selling_climax_rank_21d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rank_pct(base, 21)

def wyck_007_selling_climax_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_007_selling_climax_lvl_63d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rolling_mean(base, 63)

def wyck_008_selling_climax_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_008_selling_climax_zscore_63d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _zscore_rolling(base, 63)

def wyck_009_selling_climax_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_009_selling_climax_rank_63d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rank_pct(base, 63)

def wyck_010_selling_climax_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_010_selling_climax_lvl_126d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rolling_mean(base, 126)

def wyck_011_selling_climax_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_011_selling_climax_zscore_126d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _zscore_rolling(base, 126)

def wyck_012_selling_climax_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_012_selling_climax_rank_126d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rank_pct(base, 126)

def wyck_013_selling_climax_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_013_selling_climax_lvl_252d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rolling_mean(base, 252)

def wyck_014_selling_climax_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_014_selling_climax_zscore_252d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _zscore_rolling(base, 252)

def wyck_015_selling_climax_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_015_selling_climax_rank_252d
    ECONOMIC RATIONALE: High volume price collapse indicating a selling climax.
    """
    base = (volume > volume.rolling(63).mean()*2) * (close < low.shift(1))
    return _rank_pct(base, 252)

def wyck_016_automatic_rally_failure_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_016_automatic_rally_failure_lvl_5d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 5)

def wyck_017_automatic_rally_failure_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_017_automatic_rally_failure_zscore_5d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 5)

def wyck_018_automatic_rally_failure_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_018_automatic_rally_failure_rank_5d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 5)

def wyck_019_automatic_rally_failure_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_019_automatic_rally_failure_lvl_21d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 21)

def wyck_020_automatic_rally_failure_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_020_automatic_rally_failure_zscore_21d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 21)

def wyck_021_automatic_rally_failure_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_021_automatic_rally_failure_rank_21d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 21)

def wyck_022_automatic_rally_failure_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_022_automatic_rally_failure_lvl_63d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 63)

def wyck_023_automatic_rally_failure_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_023_automatic_rally_failure_zscore_63d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 63)

def wyck_024_automatic_rally_failure_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_024_automatic_rally_failure_rank_63d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 63)

def wyck_025_automatic_rally_failure_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_025_automatic_rally_failure_lvl_126d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 126)

def wyck_026_automatic_rally_failure_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_026_automatic_rally_failure_zscore_126d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 126)

def wyck_027_automatic_rally_failure_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_027_automatic_rally_failure_rank_126d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 126)

def wyck_028_automatic_rally_failure_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_028_automatic_rally_failure_lvl_252d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 252)

def wyck_029_automatic_rally_failure_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_029_automatic_rally_failure_zscore_252d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 252)

def wyck_030_automatic_rally_failure_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_030_automatic_rally_failure_rank_252d
    ECONOMIC RATIONALE: Weakness of the initial bounce from lows.
    """
    base = (close - low.rolling(21).min()) / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 252)

def wyck_031_secondary_test_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_031_secondary_test_lvl_5d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rolling_mean(base, 5)

def wyck_032_secondary_test_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_032_secondary_test_zscore_5d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _zscore_rolling(base, 5)

def wyck_033_secondary_test_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_033_secondary_test_rank_5d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rank_pct(base, 5)

def wyck_034_secondary_test_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_034_secondary_test_lvl_21d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rolling_mean(base, 21)

def wyck_035_secondary_test_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_035_secondary_test_zscore_21d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _zscore_rolling(base, 21)

def wyck_036_secondary_test_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_036_secondary_test_rank_21d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rank_pct(base, 21)

def wyck_037_secondary_test_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_037_secondary_test_lvl_63d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rolling_mean(base, 63)

def wyck_038_secondary_test_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_038_secondary_test_zscore_63d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _zscore_rolling(base, 63)

def wyck_039_secondary_test_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_039_secondary_test_rank_63d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rank_pct(base, 63)

def wyck_040_secondary_test_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_040_secondary_test_lvl_126d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rolling_mean(base, 126)

def wyck_041_secondary_test_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_041_secondary_test_zscore_126d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _zscore_rolling(base, 126)

def wyck_042_secondary_test_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_042_secondary_test_rank_126d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rank_pct(base, 126)

def wyck_043_secondary_test_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_043_secondary_test_lvl_252d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rolling_mean(base, 252)

def wyck_044_secondary_test_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_044_secondary_test_zscore_252d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _zscore_rolling(base, 252)

def wyck_045_secondary_test_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_045_secondary_test_rank_252d
    ECONOMIC RATIONALE: Testing of previous lows on lower volume.
    """
    base = low / low.rolling(21).min().shift(5)
    return _rank_pct(base, 252)

def wyck_046_spring_detection_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_046_spring_detection_lvl_5d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rolling_mean(base, 5)

def wyck_047_spring_detection_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_047_spring_detection_zscore_5d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _zscore_rolling(base, 5)

def wyck_048_spring_detection_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_048_spring_detection_rank_5d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rank_pct(base, 5)

def wyck_049_spring_detection_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_049_spring_detection_lvl_21d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rolling_mean(base, 21)

def wyck_050_spring_detection_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_050_spring_detection_zscore_21d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _zscore_rolling(base, 21)

def wyck_051_spring_detection_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_051_spring_detection_rank_21d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rank_pct(base, 21)

def wyck_052_spring_detection_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_052_spring_detection_lvl_63d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rolling_mean(base, 63)

def wyck_053_spring_detection_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_053_spring_detection_zscore_63d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _zscore_rolling(base, 63)

def wyck_054_spring_detection_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_054_spring_detection_rank_63d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rank_pct(base, 63)

def wyck_055_spring_detection_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_055_spring_detection_lvl_126d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rolling_mean(base, 126)

def wyck_056_spring_detection_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_056_spring_detection_zscore_126d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _zscore_rolling(base, 126)

def wyck_057_spring_detection_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_057_spring_detection_rank_126d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rank_pct(base, 126)

def wyck_058_spring_detection_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_058_spring_detection_lvl_252d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rolling_mean(base, 252)

def wyck_059_spring_detection_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_059_spring_detection_zscore_252d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _zscore_rolling(base, 252)

def wyck_060_spring_detection_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_060_spring_detection_rank_252d
    ECONOMIC RATIONALE: False breakdown below support (spring).
    """
    base = (low < low.rolling(63).min().shift(1)) * (close > low.rolling(63).min().shift(1))
    return _rank_pct(base, 252)

def wyck_061_sign_of_weakness_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_061_sign_of_weakness_lvl_5d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rolling_mean(base, 5)

def wyck_062_sign_of_weakness_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_062_sign_of_weakness_zscore_5d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _zscore_rolling(base, 5)

def wyck_063_sign_of_weakness_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_063_sign_of_weakness_rank_5d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rank_pct(base, 5)

def wyck_064_sign_of_weakness_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_064_sign_of_weakness_lvl_21d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rolling_mean(base, 21)

def wyck_065_sign_of_weakness_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_065_sign_of_weakness_zscore_21d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _zscore_rolling(base, 21)

def wyck_066_sign_of_weakness_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_066_sign_of_weakness_rank_21d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rank_pct(base, 21)

def wyck_067_sign_of_weakness_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_067_sign_of_weakness_lvl_63d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rolling_mean(base, 63)

def wyck_068_sign_of_weakness_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_068_sign_of_weakness_zscore_63d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _zscore_rolling(base, 63)

def wyck_069_sign_of_weakness_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_069_sign_of_weakness_rank_63d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rank_pct(base, 63)

def wyck_070_sign_of_weakness_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_070_sign_of_weakness_lvl_126d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rolling_mean(base, 126)

def wyck_071_sign_of_weakness_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_071_sign_of_weakness_zscore_126d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _zscore_rolling(base, 126)

def wyck_072_sign_of_weakness_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_072_sign_of_weakness_rank_126d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rank_pct(base, 126)

def wyck_073_sign_of_weakness_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_073_sign_of_weakness_lvl_252d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rolling_mean(base, 252)

def wyck_074_sign_of_weakness_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_074_sign_of_weakness_zscore_252d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _zscore_rolling(base, 252)

def wyck_075_sign_of_weakness_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_075_sign_of_weakness_rank_252d
    ECONOMIC RATIONALE: Sharp drop after a period of consolidation.
    """
    base = close.pct_change(5) < -0.1
    return _rank_pct(base, 252)

def wyck_076_supply_overcoming_demand_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_076_supply_overcoming_demand_lvl_5d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rolling_mean(base, 5)

def wyck_077_supply_overcoming_demand_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_077_supply_overcoming_demand_zscore_5d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _zscore_rolling(base, 5)

def wyck_078_supply_overcoming_demand_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_078_supply_overcoming_demand_rank_5d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rank_pct(base, 5)

def wyck_079_supply_overcoming_demand_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_079_supply_overcoming_demand_lvl_21d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rolling_mean(base, 21)

def wyck_080_supply_overcoming_demand_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_080_supply_overcoming_demand_zscore_21d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _zscore_rolling(base, 21)

def wyck_081_supply_overcoming_demand_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_081_supply_overcoming_demand_rank_21d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rank_pct(base, 21)

def wyck_082_supply_overcoming_demand_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_082_supply_overcoming_demand_lvl_63d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rolling_mean(base, 63)

def wyck_083_supply_overcoming_demand_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_083_supply_overcoming_demand_zscore_63d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _zscore_rolling(base, 63)

def wyck_084_supply_overcoming_demand_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_084_supply_overcoming_demand_rank_63d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rank_pct(base, 63)

def wyck_085_supply_overcoming_demand_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_085_supply_overcoming_demand_lvl_126d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rolling_mean(base, 126)

def wyck_086_supply_overcoming_demand_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_086_supply_overcoming_demand_zscore_126d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _zscore_rolling(base, 126)

def wyck_087_supply_overcoming_demand_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_087_supply_overcoming_demand_rank_126d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rank_pct(base, 126)

def wyck_088_supply_overcoming_demand_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_088_supply_overcoming_demand_lvl_252d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rolling_mean(base, 252)

def wyck_089_supply_overcoming_demand_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_089_supply_overcoming_demand_zscore_252d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _zscore_rolling(base, 252)

def wyck_090_supply_overcoming_demand_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_090_supply_overcoming_demand_rank_252d
    ECONOMIC RATIONALE: Volume-weighted negative price action.
    """
    base = volume * (close - open) < 0
    return _rank_pct(base, 252)

def wyck_091_trading_range_position_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_091_trading_range_position_lvl_5d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 5)

def wyck_092_trading_range_position_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_092_trading_range_position_zscore_5d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 5)

def wyck_093_trading_range_position_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_093_trading_range_position_rank_5d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 5)

def wyck_094_trading_range_position_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_094_trading_range_position_lvl_21d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 21)

def wyck_095_trading_range_position_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_095_trading_range_position_zscore_21d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 21)

def wyck_096_trading_range_position_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_096_trading_range_position_rank_21d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 21)

def wyck_097_trading_range_position_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_097_trading_range_position_lvl_63d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 63)

def wyck_098_trading_range_position_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_098_trading_range_position_zscore_63d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 63)

def wyck_099_trading_range_position_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_099_trading_range_position_rank_63d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 63)

def wyck_100_trading_range_position_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_100_trading_range_position_lvl_126d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 126)

def wyck_101_trading_range_position_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_101_trading_range_position_zscore_126d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 126)

def wyck_102_trading_range_position_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_102_trading_range_position_rank_126d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 126)

def wyck_103_trading_range_position_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_103_trading_range_position_lvl_252d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rolling_mean(base, 252)

def wyck_104_trading_range_position_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_104_trading_range_position_zscore_252d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _zscore_rolling(base, 252)

def wyck_105_trading_range_position_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_105_trading_range_position_rank_252d
    ECONOMIC RATIONALE: Position within the Wyckoff trading range.
    """
    base = (close - low.rolling(63).min()) / (high.rolling(63).max() - low.rolling(63).min())
    return _rank_pct(base, 252)

def wyck_106_volume_dry_up_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_106_volume_dry_up_lvl_5d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 5)

def wyck_107_volume_dry_up_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_107_volume_dry_up_zscore_5d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 5)

def wyck_108_volume_dry_up_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_108_volume_dry_up_rank_5d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 5)

def wyck_109_volume_dry_up_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_109_volume_dry_up_lvl_21d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 21)

def wyck_110_volume_dry_up_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_110_volume_dry_up_zscore_21d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 21)

def wyck_111_volume_dry_up_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_111_volume_dry_up_rank_21d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 21)

def wyck_112_volume_dry_up_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_112_volume_dry_up_lvl_63d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 63)

def wyck_113_volume_dry_up_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_113_volume_dry_up_zscore_63d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 63)

def wyck_114_volume_dry_up_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_114_volume_dry_up_rank_63d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 63)

def wyck_115_volume_dry_up_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_115_volume_dry_up_lvl_126d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 126)

def wyck_116_volume_dry_up_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_116_volume_dry_up_zscore_126d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 126)

def wyck_117_volume_dry_up_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_117_volume_dry_up_rank_126d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 126)

def wyck_118_volume_dry_up_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_118_volume_dry_up_lvl_252d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 252)

def wyck_119_volume_dry_up_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_119_volume_dry_up_zscore_252d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 252)

def wyck_120_volume_dry_up_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    wyck_120_volume_dry_up_rank_252d
    ECONOMIC RATIONALE: Reduction in volume suggesting supply exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V101_REGISTRY_1 = {
    "wyck_001_selling_climax_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_001_selling_climax_lvl_5d},
    "wyck_002_selling_climax_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_002_selling_climax_zscore_5d},
    "wyck_003_selling_climax_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_003_selling_climax_rank_5d},
    "wyck_004_selling_climax_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_004_selling_climax_lvl_21d},
    "wyck_005_selling_climax_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_005_selling_climax_zscore_21d},
    "wyck_006_selling_climax_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_006_selling_climax_rank_21d},
    "wyck_007_selling_climax_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_007_selling_climax_lvl_63d},
    "wyck_008_selling_climax_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_008_selling_climax_zscore_63d},
    "wyck_009_selling_climax_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_009_selling_climax_rank_63d},
    "wyck_010_selling_climax_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_010_selling_climax_lvl_126d},
    "wyck_011_selling_climax_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_011_selling_climax_zscore_126d},
    "wyck_012_selling_climax_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_012_selling_climax_rank_126d},
    "wyck_013_selling_climax_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_013_selling_climax_lvl_252d},
    "wyck_014_selling_climax_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_014_selling_climax_zscore_252d},
    "wyck_015_selling_climax_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_015_selling_climax_rank_252d},
    "wyck_016_automatic_rally_failure_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_016_automatic_rally_failure_lvl_5d},
    "wyck_017_automatic_rally_failure_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_017_automatic_rally_failure_zscore_5d},
    "wyck_018_automatic_rally_failure_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_018_automatic_rally_failure_rank_5d},
    "wyck_019_automatic_rally_failure_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_019_automatic_rally_failure_lvl_21d},
    "wyck_020_automatic_rally_failure_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_020_automatic_rally_failure_zscore_21d},
    "wyck_021_automatic_rally_failure_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_021_automatic_rally_failure_rank_21d},
    "wyck_022_automatic_rally_failure_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_022_automatic_rally_failure_lvl_63d},
    "wyck_023_automatic_rally_failure_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_023_automatic_rally_failure_zscore_63d},
    "wyck_024_automatic_rally_failure_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_024_automatic_rally_failure_rank_63d},
    "wyck_025_automatic_rally_failure_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_025_automatic_rally_failure_lvl_126d},
    "wyck_026_automatic_rally_failure_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_026_automatic_rally_failure_zscore_126d},
    "wyck_027_automatic_rally_failure_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_027_automatic_rally_failure_rank_126d},
    "wyck_028_automatic_rally_failure_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_028_automatic_rally_failure_lvl_252d},
    "wyck_029_automatic_rally_failure_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_029_automatic_rally_failure_zscore_252d},
    "wyck_030_automatic_rally_failure_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_030_automatic_rally_failure_rank_252d},
    "wyck_031_secondary_test_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_031_secondary_test_lvl_5d},
    "wyck_032_secondary_test_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_032_secondary_test_zscore_5d},
    "wyck_033_secondary_test_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_033_secondary_test_rank_5d},
    "wyck_034_secondary_test_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_034_secondary_test_lvl_21d},
    "wyck_035_secondary_test_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_035_secondary_test_zscore_21d},
    "wyck_036_secondary_test_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_036_secondary_test_rank_21d},
    "wyck_037_secondary_test_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_037_secondary_test_lvl_63d},
    "wyck_038_secondary_test_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_038_secondary_test_zscore_63d},
    "wyck_039_secondary_test_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_039_secondary_test_rank_63d},
    "wyck_040_secondary_test_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_040_secondary_test_lvl_126d},
    "wyck_041_secondary_test_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_041_secondary_test_zscore_126d},
    "wyck_042_secondary_test_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_042_secondary_test_rank_126d},
    "wyck_043_secondary_test_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_043_secondary_test_lvl_252d},
    "wyck_044_secondary_test_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_044_secondary_test_zscore_252d},
    "wyck_045_secondary_test_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_045_secondary_test_rank_252d},
    "wyck_046_spring_detection_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_046_spring_detection_lvl_5d},
    "wyck_047_spring_detection_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_047_spring_detection_zscore_5d},
    "wyck_048_spring_detection_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_048_spring_detection_rank_5d},
    "wyck_049_spring_detection_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_049_spring_detection_lvl_21d},
    "wyck_050_spring_detection_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_050_spring_detection_zscore_21d},
    "wyck_051_spring_detection_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_051_spring_detection_rank_21d},
    "wyck_052_spring_detection_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_052_spring_detection_lvl_63d},
    "wyck_053_spring_detection_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_053_spring_detection_zscore_63d},
    "wyck_054_spring_detection_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_054_spring_detection_rank_63d},
    "wyck_055_spring_detection_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_055_spring_detection_lvl_126d},
    "wyck_056_spring_detection_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_056_spring_detection_zscore_126d},
    "wyck_057_spring_detection_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_057_spring_detection_rank_126d},
    "wyck_058_spring_detection_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_058_spring_detection_lvl_252d},
    "wyck_059_spring_detection_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_059_spring_detection_zscore_252d},
    "wyck_060_spring_detection_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_060_spring_detection_rank_252d},
    "wyck_061_sign_of_weakness_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_061_sign_of_weakness_lvl_5d},
    "wyck_062_sign_of_weakness_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_062_sign_of_weakness_zscore_5d},
    "wyck_063_sign_of_weakness_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_063_sign_of_weakness_rank_5d},
    "wyck_064_sign_of_weakness_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_064_sign_of_weakness_lvl_21d},
    "wyck_065_sign_of_weakness_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_065_sign_of_weakness_zscore_21d},
    "wyck_066_sign_of_weakness_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_066_sign_of_weakness_rank_21d},
    "wyck_067_sign_of_weakness_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_067_sign_of_weakness_lvl_63d},
    "wyck_068_sign_of_weakness_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_068_sign_of_weakness_zscore_63d},
    "wyck_069_sign_of_weakness_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_069_sign_of_weakness_rank_63d},
    "wyck_070_sign_of_weakness_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_070_sign_of_weakness_lvl_126d},
    "wyck_071_sign_of_weakness_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_071_sign_of_weakness_zscore_126d},
    "wyck_072_sign_of_weakness_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_072_sign_of_weakness_rank_126d},
    "wyck_073_sign_of_weakness_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_073_sign_of_weakness_lvl_252d},
    "wyck_074_sign_of_weakness_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_074_sign_of_weakness_zscore_252d},
    "wyck_075_sign_of_weakness_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_075_sign_of_weakness_rank_252d},
    "wyck_076_supply_overcoming_demand_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_076_supply_overcoming_demand_lvl_5d},
    "wyck_077_supply_overcoming_demand_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_077_supply_overcoming_demand_zscore_5d},
    "wyck_078_supply_overcoming_demand_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_078_supply_overcoming_demand_rank_5d},
    "wyck_079_supply_overcoming_demand_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_079_supply_overcoming_demand_lvl_21d},
    "wyck_080_supply_overcoming_demand_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_080_supply_overcoming_demand_zscore_21d},
    "wyck_081_supply_overcoming_demand_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_081_supply_overcoming_demand_rank_21d},
    "wyck_082_supply_overcoming_demand_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_082_supply_overcoming_demand_lvl_63d},
    "wyck_083_supply_overcoming_demand_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_083_supply_overcoming_demand_zscore_63d},
    "wyck_084_supply_overcoming_demand_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_084_supply_overcoming_demand_rank_63d},
    "wyck_085_supply_overcoming_demand_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_085_supply_overcoming_demand_lvl_126d},
    "wyck_086_supply_overcoming_demand_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_086_supply_overcoming_demand_zscore_126d},
    "wyck_087_supply_overcoming_demand_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_087_supply_overcoming_demand_rank_126d},
    "wyck_088_supply_overcoming_demand_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_088_supply_overcoming_demand_lvl_252d},
    "wyck_089_supply_overcoming_demand_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_089_supply_overcoming_demand_zscore_252d},
    "wyck_090_supply_overcoming_demand_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_090_supply_overcoming_demand_rank_252d},
    "wyck_091_trading_range_position_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_091_trading_range_position_lvl_5d},
    "wyck_092_trading_range_position_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_092_trading_range_position_zscore_5d},
    "wyck_093_trading_range_position_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_093_trading_range_position_rank_5d},
    "wyck_094_trading_range_position_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_094_trading_range_position_lvl_21d},
    "wyck_095_trading_range_position_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_095_trading_range_position_zscore_21d},
    "wyck_096_trading_range_position_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_096_trading_range_position_rank_21d},
    "wyck_097_trading_range_position_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_097_trading_range_position_lvl_63d},
    "wyck_098_trading_range_position_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_098_trading_range_position_zscore_63d},
    "wyck_099_trading_range_position_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_099_trading_range_position_rank_63d},
    "wyck_100_trading_range_position_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_100_trading_range_position_lvl_126d},
    "wyck_101_trading_range_position_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_101_trading_range_position_zscore_126d},
    "wyck_102_trading_range_position_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_102_trading_range_position_rank_126d},
    "wyck_103_trading_range_position_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_103_trading_range_position_lvl_252d},
    "wyck_104_trading_range_position_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_104_trading_range_position_zscore_252d},
    "wyck_105_trading_range_position_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_105_trading_range_position_rank_252d},
    "wyck_106_volume_dry_up_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_106_volume_dry_up_lvl_5d},
    "wyck_107_volume_dry_up_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_107_volume_dry_up_zscore_5d},
    "wyck_108_volume_dry_up_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_108_volume_dry_up_rank_5d},
    "wyck_109_volume_dry_up_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_109_volume_dry_up_lvl_21d},
    "wyck_110_volume_dry_up_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_110_volume_dry_up_zscore_21d},
    "wyck_111_volume_dry_up_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_111_volume_dry_up_rank_21d},
    "wyck_112_volume_dry_up_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_112_volume_dry_up_lvl_63d},
    "wyck_113_volume_dry_up_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_113_volume_dry_up_zscore_63d},
    "wyck_114_volume_dry_up_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_114_volume_dry_up_rank_63d},
    "wyck_115_volume_dry_up_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_115_volume_dry_up_lvl_126d},
    "wyck_116_volume_dry_up_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_116_volume_dry_up_zscore_126d},
    "wyck_117_volume_dry_up_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_117_volume_dry_up_rank_126d},
    "wyck_118_volume_dry_up_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_118_volume_dry_up_lvl_252d},
    "wyck_119_volume_dry_up_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_119_volume_dry_up_zscore_252d},
    "wyck_120_volume_dry_up_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": wyck_120_volume_dry_up_rank_252d},
}
