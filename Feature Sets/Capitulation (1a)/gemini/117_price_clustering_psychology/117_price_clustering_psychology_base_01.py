"""
117_price_clustering_psychology — Base Features Part 1
Domain: price_clustering_psychology
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

def ppsy_001_round_number_proximity_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_001_round_number_proximity_lvl_5d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rolling_mean(base, 5)

def ppsy_002_round_number_proximity_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_002_round_number_proximity_zscore_5d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _zscore_rolling(base, 5)

def ppsy_003_round_number_proximity_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_003_round_number_proximity_rank_5d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rank_pct(base, 5)

def ppsy_004_round_number_proximity_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_004_round_number_proximity_lvl_21d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rolling_mean(base, 21)

def ppsy_005_round_number_proximity_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_005_round_number_proximity_zscore_21d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _zscore_rolling(base, 21)

def ppsy_006_round_number_proximity_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_006_round_number_proximity_rank_21d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rank_pct(base, 21)

def ppsy_007_round_number_proximity_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_007_round_number_proximity_lvl_63d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rolling_mean(base, 63)

def ppsy_008_round_number_proximity_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_008_round_number_proximity_zscore_63d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _zscore_rolling(base, 63)

def ppsy_009_round_number_proximity_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_009_round_number_proximity_rank_63d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rank_pct(base, 63)

def ppsy_010_round_number_proximity_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_010_round_number_proximity_lvl_126d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rolling_mean(base, 126)

def ppsy_011_round_number_proximity_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_011_round_number_proximity_zscore_126d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _zscore_rolling(base, 126)

def ppsy_012_round_number_proximity_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_012_round_number_proximity_rank_126d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rank_pct(base, 126)

def ppsy_013_round_number_proximity_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_013_round_number_proximity_lvl_252d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rolling_mean(base, 252)

def ppsy_014_round_number_proximity_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_014_round_number_proximity_zscore_252d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _zscore_rolling(base, 252)

def ppsy_015_round_number_proximity_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_015_round_number_proximity_rank_252d
    ECONOMIC RATIONALE: Proximity to whole dollar amounts.
    """
    base = close % 1.0
    return _rank_pct(base, 252)

def ppsy_016_decade_number_proximity_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_016_decade_number_proximity_lvl_5d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rolling_mean(base, 5)

def ppsy_017_decade_number_proximity_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_017_decade_number_proximity_zscore_5d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _zscore_rolling(base, 5)

def ppsy_018_decade_number_proximity_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_018_decade_number_proximity_rank_5d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rank_pct(base, 5)

def ppsy_019_decade_number_proximity_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_019_decade_number_proximity_lvl_21d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rolling_mean(base, 21)

def ppsy_020_decade_number_proximity_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_020_decade_number_proximity_zscore_21d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _zscore_rolling(base, 21)

def ppsy_021_decade_number_proximity_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_021_decade_number_proximity_rank_21d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rank_pct(base, 21)

def ppsy_022_decade_number_proximity_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_022_decade_number_proximity_lvl_63d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rolling_mean(base, 63)

def ppsy_023_decade_number_proximity_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_023_decade_number_proximity_zscore_63d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _zscore_rolling(base, 63)

def ppsy_024_decade_number_proximity_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_024_decade_number_proximity_rank_63d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rank_pct(base, 63)

def ppsy_025_decade_number_proximity_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_025_decade_number_proximity_lvl_126d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rolling_mean(base, 126)

def ppsy_026_decade_number_proximity_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_026_decade_number_proximity_zscore_126d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _zscore_rolling(base, 126)

def ppsy_027_decade_number_proximity_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_027_decade_number_proximity_rank_126d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rank_pct(base, 126)

def ppsy_028_decade_number_proximity_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_028_decade_number_proximity_lvl_252d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rolling_mean(base, 252)

def ppsy_029_decade_number_proximity_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_029_decade_number_proximity_zscore_252d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _zscore_rolling(base, 252)

def ppsy_030_decade_number_proximity_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_030_decade_number_proximity_rank_252d
    ECONOMIC RATIONALE: Proximity to ten-dollar increments.
    """
    base = close % 10.0
    return _rank_pct(base, 252)

def ppsy_031_century_number_proximity_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_031_century_number_proximity_lvl_5d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rolling_mean(base, 5)

def ppsy_032_century_number_proximity_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_032_century_number_proximity_zscore_5d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _zscore_rolling(base, 5)

def ppsy_033_century_number_proximity_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_033_century_number_proximity_rank_5d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rank_pct(base, 5)

def ppsy_034_century_number_proximity_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_034_century_number_proximity_lvl_21d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rolling_mean(base, 21)

def ppsy_035_century_number_proximity_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_035_century_number_proximity_zscore_21d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _zscore_rolling(base, 21)

def ppsy_036_century_number_proximity_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_036_century_number_proximity_rank_21d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rank_pct(base, 21)

def ppsy_037_century_number_proximity_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_037_century_number_proximity_lvl_63d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rolling_mean(base, 63)

def ppsy_038_century_number_proximity_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_038_century_number_proximity_zscore_63d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _zscore_rolling(base, 63)

def ppsy_039_century_number_proximity_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_039_century_number_proximity_rank_63d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rank_pct(base, 63)

def ppsy_040_century_number_proximity_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_040_century_number_proximity_lvl_126d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rolling_mean(base, 126)

def ppsy_041_century_number_proximity_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_041_century_number_proximity_zscore_126d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _zscore_rolling(base, 126)

def ppsy_042_century_number_proximity_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_042_century_number_proximity_rank_126d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rank_pct(base, 126)

def ppsy_043_century_number_proximity_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_043_century_number_proximity_lvl_252d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rolling_mean(base, 252)

def ppsy_044_century_number_proximity_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_044_century_number_proximity_zscore_252d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _zscore_rolling(base, 252)

def ppsy_045_century_number_proximity_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_045_century_number_proximity_rank_252d
    ECONOMIC RATIONALE: Proximity to hundred-dollar increments.
    """
    base = close % 100.0
    return _rank_pct(base, 252)

def ppsy_046_price_level_clustering_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_046_price_level_clustering_lvl_5d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rolling_mean(base, 5)

def ppsy_047_price_level_clustering_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_047_price_level_clustering_zscore_5d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _zscore_rolling(base, 5)

def ppsy_048_price_level_clustering_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_048_price_level_clustering_rank_5d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rank_pct(base, 5)

def ppsy_049_price_level_clustering_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_049_price_level_clustering_lvl_21d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rolling_mean(base, 21)

def ppsy_050_price_level_clustering_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_050_price_level_clustering_zscore_21d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _zscore_rolling(base, 21)

def ppsy_051_price_level_clustering_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_051_price_level_clustering_rank_21d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rank_pct(base, 21)

def ppsy_052_price_level_clustering_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_052_price_level_clustering_lvl_63d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rolling_mean(base, 63)

def ppsy_053_price_level_clustering_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_053_price_level_clustering_zscore_63d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _zscore_rolling(base, 63)

def ppsy_054_price_level_clustering_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_054_price_level_clustering_rank_63d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rank_pct(base, 63)

def ppsy_055_price_level_clustering_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_055_price_level_clustering_lvl_126d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rolling_mean(base, 126)

def ppsy_056_price_level_clustering_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_056_price_level_clustering_zscore_126d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _zscore_rolling(base, 126)

def ppsy_057_price_level_clustering_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_057_price_level_clustering_rank_126d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rank_pct(base, 126)

def ppsy_058_price_level_clustering_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_058_price_level_clustering_lvl_252d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rolling_mean(base, 252)

def ppsy_059_price_level_clustering_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_059_price_level_clustering_zscore_252d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _zscore_rolling(base, 252)

def ppsy_060_price_level_clustering_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_060_price_level_clustering_rank_252d
    ECONOMIC RATIONALE: Number of distinct price clusters recently visited.
    """
    base = close.rolling(21).apply(lambda x: len(np.histogram(x, bins=10)[0][np.histogram(x, bins=10)[0] > 0]))
    return _rank_pct(base, 252)

def ppsy_061_clustering_entropy_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_061_clustering_entropy_lvl_5d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 5)

def ppsy_062_clustering_entropy_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_062_clustering_entropy_zscore_5d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 5)

def ppsy_063_clustering_entropy_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_063_clustering_entropy_rank_5d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 5)

def ppsy_064_clustering_entropy_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_064_clustering_entropy_lvl_21d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 21)

def ppsy_065_clustering_entropy_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_065_clustering_entropy_zscore_21d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 21)

def ppsy_066_clustering_entropy_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_066_clustering_entropy_rank_21d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 21)

def ppsy_067_clustering_entropy_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_067_clustering_entropy_lvl_63d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 63)

def ppsy_068_clustering_entropy_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_068_clustering_entropy_zscore_63d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 63)

def ppsy_069_clustering_entropy_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_069_clustering_entropy_rank_63d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 63)

def ppsy_070_clustering_entropy_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_070_clustering_entropy_lvl_126d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 126)

def ppsy_071_clustering_entropy_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_071_clustering_entropy_zscore_126d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 126)

def ppsy_072_clustering_entropy_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_072_clustering_entropy_rank_126d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 126)

def ppsy_073_clustering_entropy_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_073_clustering_entropy_lvl_252d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rolling_mean(base, 252)

def ppsy_074_clustering_entropy_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_074_clustering_entropy_zscore_252d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _zscore_rolling(base, 252)

def ppsy_075_clustering_entropy_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_075_clustering_entropy_rank_252d
    ECONOMIC RATIONALE: Entropy of price distribution across bins.
    """
    base = close.rolling(21).apply(lambda x: -np.sum(np.histogram(x)[0]*np.log(np.histogram(x)[0]+1e-9)))
    return _rank_pct(base, 252)

def ppsy_076_price_support_psych_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_076_price_support_psych_lvl_5d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rolling_mean(base, 5)

def ppsy_077_price_support_psych_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_077_price_support_psych_zscore_5d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _zscore_rolling(base, 5)

def ppsy_078_price_support_psych_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_078_price_support_psych_rank_5d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rank_pct(base, 5)

def ppsy_079_price_support_psych_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_079_price_support_psych_lvl_21d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rolling_mean(base, 21)

def ppsy_080_price_support_psych_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_080_price_support_psych_zscore_21d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _zscore_rolling(base, 21)

def ppsy_081_price_support_psych_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_081_price_support_psych_rank_21d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rank_pct(base, 21)

def ppsy_082_price_support_psych_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_082_price_support_psych_lvl_63d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rolling_mean(base, 63)

def ppsy_083_price_support_psych_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_083_price_support_psych_zscore_63d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _zscore_rolling(base, 63)

def ppsy_084_price_support_psych_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_084_price_support_psych_rank_63d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rank_pct(base, 63)

def ppsy_085_price_support_psych_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_085_price_support_psych_lvl_126d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rolling_mean(base, 126)

def ppsy_086_price_support_psych_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_086_price_support_psych_zscore_126d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _zscore_rolling(base, 126)

def ppsy_087_price_support_psych_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_087_price_support_psych_rank_126d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rank_pct(base, 126)

def ppsy_088_price_support_psych_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_088_price_support_psych_lvl_252d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rolling_mean(base, 252)

def ppsy_089_price_support_psych_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_089_price_support_psych_zscore_252d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _zscore_rolling(base, 252)

def ppsy_090_price_support_psych_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_090_price_support_psych_rank_252d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week lows.
    """
    base = close / close.rolling(252).min() - 1 < 0.05
    return _rank_pct(base, 252)

def ppsy_091_price_resistance_psych_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_091_price_resistance_psych_lvl_5d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rolling_mean(base, 5)

def ppsy_092_price_resistance_psych_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_092_price_resistance_psych_zscore_5d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _zscore_rolling(base, 5)

def ppsy_093_price_resistance_psych_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_093_price_resistance_psych_rank_5d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rank_pct(base, 5)

def ppsy_094_price_resistance_psych_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_094_price_resistance_psych_lvl_21d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rolling_mean(base, 21)

def ppsy_095_price_resistance_psych_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_095_price_resistance_psych_zscore_21d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _zscore_rolling(base, 21)

def ppsy_096_price_resistance_psych_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_096_price_resistance_psych_rank_21d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rank_pct(base, 21)

def ppsy_097_price_resistance_psych_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_097_price_resistance_psych_lvl_63d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rolling_mean(base, 63)

def ppsy_098_price_resistance_psych_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_098_price_resistance_psych_zscore_63d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _zscore_rolling(base, 63)

def ppsy_099_price_resistance_psych_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_099_price_resistance_psych_rank_63d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rank_pct(base, 63)

def ppsy_100_price_resistance_psych_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_100_price_resistance_psych_lvl_126d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rolling_mean(base, 126)

def ppsy_101_price_resistance_psych_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_101_price_resistance_psych_zscore_126d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _zscore_rolling(base, 126)

def ppsy_102_price_resistance_psych_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_102_price_resistance_psych_rank_126d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rank_pct(base, 126)

def ppsy_103_price_resistance_psych_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_103_price_resistance_psych_lvl_252d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rolling_mean(base, 252)

def ppsy_104_price_resistance_psych_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_104_price_resistance_psych_zscore_252d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _zscore_rolling(base, 252)

def ppsy_105_price_resistance_psych_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_105_price_resistance_psych_rank_252d
    ECONOMIC RATIONALE: Psychological anchoring to 52-week highs.
    """
    base = close / close.rolling(252).max() - 1 > -0.05
    return _rank_pct(base, 252)

def ppsy_106_clustering_zscore_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_106_clustering_zscore_lvl_5d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rolling_mean(base, 5)

def ppsy_107_clustering_zscore_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_107_clustering_zscore_zscore_5d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _zscore_rolling(base, 5)

def ppsy_108_clustering_zscore_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_108_clustering_zscore_rank_5d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rank_pct(base, 5)

def ppsy_109_clustering_zscore_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_109_clustering_zscore_lvl_21d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rolling_mean(base, 21)

def ppsy_110_clustering_zscore_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_110_clustering_zscore_zscore_21d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _zscore_rolling(base, 21)

def ppsy_111_clustering_zscore_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_111_clustering_zscore_rank_21d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rank_pct(base, 21)

def ppsy_112_clustering_zscore_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_112_clustering_zscore_lvl_63d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rolling_mean(base, 63)

def ppsy_113_clustering_zscore_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_113_clustering_zscore_zscore_63d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _zscore_rolling(base, 63)

def ppsy_114_clustering_zscore_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_114_clustering_zscore_rank_63d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rank_pct(base, 63)

def ppsy_115_clustering_zscore_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_115_clustering_zscore_lvl_126d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rolling_mean(base, 126)

def ppsy_116_clustering_zscore_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_116_clustering_zscore_zscore_126d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _zscore_rolling(base, 126)

def ppsy_117_clustering_zscore_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_117_clustering_zscore_rank_126d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rank_pct(base, 126)

def ppsy_118_clustering_zscore_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_118_clustering_zscore_lvl_252d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rolling_mean(base, 252)

def ppsy_119_clustering_zscore_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_119_clustering_zscore_zscore_252d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _zscore_rolling(base, 252)

def ppsy_120_clustering_zscore_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    ppsy_120_clustering_zscore_rank_252d
    ECONOMIC RATIONALE: Anomaly in price digit distribution.
    """
    base = _zscore_rolling(close % 1.0, 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V117_REGISTRY_1 = {
    "ppsy_001_round_number_proximity_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_001_round_number_proximity_lvl_5d},
    "ppsy_002_round_number_proximity_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_002_round_number_proximity_zscore_5d},
    "ppsy_003_round_number_proximity_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_003_round_number_proximity_rank_5d},
    "ppsy_004_round_number_proximity_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_004_round_number_proximity_lvl_21d},
    "ppsy_005_round_number_proximity_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_005_round_number_proximity_zscore_21d},
    "ppsy_006_round_number_proximity_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_006_round_number_proximity_rank_21d},
    "ppsy_007_round_number_proximity_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_007_round_number_proximity_lvl_63d},
    "ppsy_008_round_number_proximity_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_008_round_number_proximity_zscore_63d},
    "ppsy_009_round_number_proximity_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_009_round_number_proximity_rank_63d},
    "ppsy_010_round_number_proximity_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_010_round_number_proximity_lvl_126d},
    "ppsy_011_round_number_proximity_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_011_round_number_proximity_zscore_126d},
    "ppsy_012_round_number_proximity_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_012_round_number_proximity_rank_126d},
    "ppsy_013_round_number_proximity_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_013_round_number_proximity_lvl_252d},
    "ppsy_014_round_number_proximity_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_014_round_number_proximity_zscore_252d},
    "ppsy_015_round_number_proximity_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_015_round_number_proximity_rank_252d},
    "ppsy_016_decade_number_proximity_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_016_decade_number_proximity_lvl_5d},
    "ppsy_017_decade_number_proximity_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_017_decade_number_proximity_zscore_5d},
    "ppsy_018_decade_number_proximity_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_018_decade_number_proximity_rank_5d},
    "ppsy_019_decade_number_proximity_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_019_decade_number_proximity_lvl_21d},
    "ppsy_020_decade_number_proximity_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_020_decade_number_proximity_zscore_21d},
    "ppsy_021_decade_number_proximity_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_021_decade_number_proximity_rank_21d},
    "ppsy_022_decade_number_proximity_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_022_decade_number_proximity_lvl_63d},
    "ppsy_023_decade_number_proximity_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_023_decade_number_proximity_zscore_63d},
    "ppsy_024_decade_number_proximity_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_024_decade_number_proximity_rank_63d},
    "ppsy_025_decade_number_proximity_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_025_decade_number_proximity_lvl_126d},
    "ppsy_026_decade_number_proximity_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_026_decade_number_proximity_zscore_126d},
    "ppsy_027_decade_number_proximity_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_027_decade_number_proximity_rank_126d},
    "ppsy_028_decade_number_proximity_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_028_decade_number_proximity_lvl_252d},
    "ppsy_029_decade_number_proximity_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_029_decade_number_proximity_zscore_252d},
    "ppsy_030_decade_number_proximity_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_030_decade_number_proximity_rank_252d},
    "ppsy_031_century_number_proximity_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_031_century_number_proximity_lvl_5d},
    "ppsy_032_century_number_proximity_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_032_century_number_proximity_zscore_5d},
    "ppsy_033_century_number_proximity_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_033_century_number_proximity_rank_5d},
    "ppsy_034_century_number_proximity_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_034_century_number_proximity_lvl_21d},
    "ppsy_035_century_number_proximity_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_035_century_number_proximity_zscore_21d},
    "ppsy_036_century_number_proximity_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_036_century_number_proximity_rank_21d},
    "ppsy_037_century_number_proximity_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_037_century_number_proximity_lvl_63d},
    "ppsy_038_century_number_proximity_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_038_century_number_proximity_zscore_63d},
    "ppsy_039_century_number_proximity_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_039_century_number_proximity_rank_63d},
    "ppsy_040_century_number_proximity_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_040_century_number_proximity_lvl_126d},
    "ppsy_041_century_number_proximity_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_041_century_number_proximity_zscore_126d},
    "ppsy_042_century_number_proximity_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_042_century_number_proximity_rank_126d},
    "ppsy_043_century_number_proximity_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_043_century_number_proximity_lvl_252d},
    "ppsy_044_century_number_proximity_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_044_century_number_proximity_zscore_252d},
    "ppsy_045_century_number_proximity_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_045_century_number_proximity_rank_252d},
    "ppsy_046_price_level_clustering_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_046_price_level_clustering_lvl_5d},
    "ppsy_047_price_level_clustering_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_047_price_level_clustering_zscore_5d},
    "ppsy_048_price_level_clustering_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_048_price_level_clustering_rank_5d},
    "ppsy_049_price_level_clustering_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_049_price_level_clustering_lvl_21d},
    "ppsy_050_price_level_clustering_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_050_price_level_clustering_zscore_21d},
    "ppsy_051_price_level_clustering_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_051_price_level_clustering_rank_21d},
    "ppsy_052_price_level_clustering_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_052_price_level_clustering_lvl_63d},
    "ppsy_053_price_level_clustering_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_053_price_level_clustering_zscore_63d},
    "ppsy_054_price_level_clustering_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_054_price_level_clustering_rank_63d},
    "ppsy_055_price_level_clustering_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_055_price_level_clustering_lvl_126d},
    "ppsy_056_price_level_clustering_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_056_price_level_clustering_zscore_126d},
    "ppsy_057_price_level_clustering_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_057_price_level_clustering_rank_126d},
    "ppsy_058_price_level_clustering_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_058_price_level_clustering_lvl_252d},
    "ppsy_059_price_level_clustering_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_059_price_level_clustering_zscore_252d},
    "ppsy_060_price_level_clustering_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_060_price_level_clustering_rank_252d},
    "ppsy_061_clustering_entropy_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_061_clustering_entropy_lvl_5d},
    "ppsy_062_clustering_entropy_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_062_clustering_entropy_zscore_5d},
    "ppsy_063_clustering_entropy_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_063_clustering_entropy_rank_5d},
    "ppsy_064_clustering_entropy_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_064_clustering_entropy_lvl_21d},
    "ppsy_065_clustering_entropy_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_065_clustering_entropy_zscore_21d},
    "ppsy_066_clustering_entropy_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_066_clustering_entropy_rank_21d},
    "ppsy_067_clustering_entropy_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_067_clustering_entropy_lvl_63d},
    "ppsy_068_clustering_entropy_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_068_clustering_entropy_zscore_63d},
    "ppsy_069_clustering_entropy_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_069_clustering_entropy_rank_63d},
    "ppsy_070_clustering_entropy_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_070_clustering_entropy_lvl_126d},
    "ppsy_071_clustering_entropy_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_071_clustering_entropy_zscore_126d},
    "ppsy_072_clustering_entropy_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_072_clustering_entropy_rank_126d},
    "ppsy_073_clustering_entropy_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_073_clustering_entropy_lvl_252d},
    "ppsy_074_clustering_entropy_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_074_clustering_entropy_zscore_252d},
    "ppsy_075_clustering_entropy_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_075_clustering_entropy_rank_252d},
    "ppsy_076_price_support_psych_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_076_price_support_psych_lvl_5d},
    "ppsy_077_price_support_psych_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_077_price_support_psych_zscore_5d},
    "ppsy_078_price_support_psych_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_078_price_support_psych_rank_5d},
    "ppsy_079_price_support_psych_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_079_price_support_psych_lvl_21d},
    "ppsy_080_price_support_psych_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_080_price_support_psych_zscore_21d},
    "ppsy_081_price_support_psych_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_081_price_support_psych_rank_21d},
    "ppsy_082_price_support_psych_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_082_price_support_psych_lvl_63d},
    "ppsy_083_price_support_psych_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_083_price_support_psych_zscore_63d},
    "ppsy_084_price_support_psych_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_084_price_support_psych_rank_63d},
    "ppsy_085_price_support_psych_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_085_price_support_psych_lvl_126d},
    "ppsy_086_price_support_psych_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_086_price_support_psych_zscore_126d},
    "ppsy_087_price_support_psych_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_087_price_support_psych_rank_126d},
    "ppsy_088_price_support_psych_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_088_price_support_psych_lvl_252d},
    "ppsy_089_price_support_psych_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_089_price_support_psych_zscore_252d},
    "ppsy_090_price_support_psych_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_090_price_support_psych_rank_252d},
    "ppsy_091_price_resistance_psych_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_091_price_resistance_psych_lvl_5d},
    "ppsy_092_price_resistance_psych_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_092_price_resistance_psych_zscore_5d},
    "ppsy_093_price_resistance_psych_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_093_price_resistance_psych_rank_5d},
    "ppsy_094_price_resistance_psych_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_094_price_resistance_psych_lvl_21d},
    "ppsy_095_price_resistance_psych_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_095_price_resistance_psych_zscore_21d},
    "ppsy_096_price_resistance_psych_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_096_price_resistance_psych_rank_21d},
    "ppsy_097_price_resistance_psych_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_097_price_resistance_psych_lvl_63d},
    "ppsy_098_price_resistance_psych_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_098_price_resistance_psych_zscore_63d},
    "ppsy_099_price_resistance_psych_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_099_price_resistance_psych_rank_63d},
    "ppsy_100_price_resistance_psych_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_100_price_resistance_psych_lvl_126d},
    "ppsy_101_price_resistance_psych_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_101_price_resistance_psych_zscore_126d},
    "ppsy_102_price_resistance_psych_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_102_price_resistance_psych_rank_126d},
    "ppsy_103_price_resistance_psych_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_103_price_resistance_psych_lvl_252d},
    "ppsy_104_price_resistance_psych_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_104_price_resistance_psych_zscore_252d},
    "ppsy_105_price_resistance_psych_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_105_price_resistance_psych_rank_252d},
    "ppsy_106_clustering_zscore_lvl_5d": {"inputs": ["close", "volume"], "func": ppsy_106_clustering_zscore_lvl_5d},
    "ppsy_107_clustering_zscore_zscore_5d": {"inputs": ["close", "volume"], "func": ppsy_107_clustering_zscore_zscore_5d},
    "ppsy_108_clustering_zscore_rank_5d": {"inputs": ["close", "volume"], "func": ppsy_108_clustering_zscore_rank_5d},
    "ppsy_109_clustering_zscore_lvl_21d": {"inputs": ["close", "volume"], "func": ppsy_109_clustering_zscore_lvl_21d},
    "ppsy_110_clustering_zscore_zscore_21d": {"inputs": ["close", "volume"], "func": ppsy_110_clustering_zscore_zscore_21d},
    "ppsy_111_clustering_zscore_rank_21d": {"inputs": ["close", "volume"], "func": ppsy_111_clustering_zscore_rank_21d},
    "ppsy_112_clustering_zscore_lvl_63d": {"inputs": ["close", "volume"], "func": ppsy_112_clustering_zscore_lvl_63d},
    "ppsy_113_clustering_zscore_zscore_63d": {"inputs": ["close", "volume"], "func": ppsy_113_clustering_zscore_zscore_63d},
    "ppsy_114_clustering_zscore_rank_63d": {"inputs": ["close", "volume"], "func": ppsy_114_clustering_zscore_rank_63d},
    "ppsy_115_clustering_zscore_lvl_126d": {"inputs": ["close", "volume"], "func": ppsy_115_clustering_zscore_lvl_126d},
    "ppsy_116_clustering_zscore_zscore_126d": {"inputs": ["close", "volume"], "func": ppsy_116_clustering_zscore_zscore_126d},
    "ppsy_117_clustering_zscore_rank_126d": {"inputs": ["close", "volume"], "func": ppsy_117_clustering_zscore_rank_126d},
    "ppsy_118_clustering_zscore_lvl_252d": {"inputs": ["close", "volume"], "func": ppsy_118_clustering_zscore_lvl_252d},
    "ppsy_119_clustering_zscore_zscore_252d": {"inputs": ["close", "volume"], "func": ppsy_119_clustering_zscore_zscore_252d},
    "ppsy_120_clustering_zscore_rank_252d": {"inputs": ["close", "volume"], "func": ppsy_120_clustering_zscore_rank_252d},
}
