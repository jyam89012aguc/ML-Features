"""
112_volume_at_price — Base Features Part 1
Domain: volume_at_price
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

def vapr_001_volume_poc_dist_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_001_volume_poc_dist_lvl_5d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 5)

def vapr_002_volume_poc_dist_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_002_volume_poc_dist_zscore_5d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 5)

def vapr_003_volume_poc_dist_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_003_volume_poc_dist_rank_5d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 5)

def vapr_004_volume_poc_dist_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_004_volume_poc_dist_lvl_21d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 21)

def vapr_005_volume_poc_dist_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_005_volume_poc_dist_zscore_21d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 21)

def vapr_006_volume_poc_dist_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_006_volume_poc_dist_rank_21d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 21)

def vapr_007_volume_poc_dist_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_007_volume_poc_dist_lvl_63d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 63)

def vapr_008_volume_poc_dist_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_008_volume_poc_dist_zscore_63d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 63)

def vapr_009_volume_poc_dist_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_009_volume_poc_dist_rank_63d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 63)

def vapr_010_volume_poc_dist_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_010_volume_poc_dist_lvl_126d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 126)

def vapr_011_volume_poc_dist_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_011_volume_poc_dist_zscore_126d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 126)

def vapr_012_volume_poc_dist_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_012_volume_poc_dist_rank_126d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 126)

def vapr_013_volume_poc_dist_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_013_volume_poc_dist_lvl_252d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 252)

def vapr_014_volume_poc_dist_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_014_volume_poc_dist_zscore_252d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 252)

def vapr_015_volume_poc_dist_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_015_volume_poc_dist_rank_252d
    ECONOMIC RATIONALE: Distance from the volume-weighted Point of Control.
    """
    base = close - close.rolling(63).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 252)

def vapr_016_value_area_high_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_016_value_area_high_lvl_5d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rolling_mean(base, 5)

def vapr_017_value_area_high_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_017_value_area_high_zscore_5d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _zscore_rolling(base, 5)

def vapr_018_value_area_high_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_018_value_area_high_rank_5d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rank_pct(base, 5)

def vapr_019_value_area_high_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_019_value_area_high_lvl_21d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rolling_mean(base, 21)

def vapr_020_value_area_high_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_020_value_area_high_zscore_21d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _zscore_rolling(base, 21)

def vapr_021_value_area_high_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_021_value_area_high_rank_21d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rank_pct(base, 21)

def vapr_022_value_area_high_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_022_value_area_high_lvl_63d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rolling_mean(base, 63)

def vapr_023_value_area_high_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_023_value_area_high_zscore_63d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _zscore_rolling(base, 63)

def vapr_024_value_area_high_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_024_value_area_high_rank_63d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rank_pct(base, 63)

def vapr_025_value_area_high_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_025_value_area_high_lvl_126d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rolling_mean(base, 126)

def vapr_026_value_area_high_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_026_value_area_high_zscore_126d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _zscore_rolling(base, 126)

def vapr_027_value_area_high_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_027_value_area_high_rank_126d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rank_pct(base, 126)

def vapr_028_value_area_high_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_028_value_area_high_lvl_252d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rolling_mean(base, 252)

def vapr_029_value_area_high_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_029_value_area_high_zscore_252d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _zscore_rolling(base, 252)

def vapr_030_value_area_high_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_030_value_area_high_rank_252d
    ECONOMIC RATIONALE: Upper bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.7)
    return _rank_pct(base, 252)

def vapr_031_value_area_low_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_031_value_area_low_lvl_5d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rolling_mean(base, 5)

def vapr_032_value_area_low_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_032_value_area_low_zscore_5d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _zscore_rolling(base, 5)

def vapr_033_value_area_low_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_033_value_area_low_rank_5d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rank_pct(base, 5)

def vapr_034_value_area_low_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_034_value_area_low_lvl_21d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rolling_mean(base, 21)

def vapr_035_value_area_low_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_035_value_area_low_zscore_21d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _zscore_rolling(base, 21)

def vapr_036_value_area_low_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_036_value_area_low_rank_21d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rank_pct(base, 21)

def vapr_037_value_area_low_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_037_value_area_low_lvl_63d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rolling_mean(base, 63)

def vapr_038_value_area_low_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_038_value_area_low_zscore_63d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _zscore_rolling(base, 63)

def vapr_039_value_area_low_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_039_value_area_low_rank_63d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rank_pct(base, 63)

def vapr_040_value_area_low_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_040_value_area_low_lvl_126d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rolling_mean(base, 126)

def vapr_041_value_area_low_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_041_value_area_low_zscore_126d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _zscore_rolling(base, 126)

def vapr_042_value_area_low_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_042_value_area_low_rank_126d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rank_pct(base, 126)

def vapr_043_value_area_low_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_043_value_area_low_lvl_252d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rolling_mean(base, 252)

def vapr_044_value_area_low_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_044_value_area_low_zscore_252d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _zscore_rolling(base, 252)

def vapr_045_value_area_low_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_045_value_area_low_rank_252d
    ECONOMIC RATIONALE: Lower bound of the 70% volume value area.
    """
    base = close.rolling(63).quantile(0.3)
    return _rank_pct(base, 252)

def vapr_046_high_volume_node_dist_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_046_high_volume_node_dist_lvl_5d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 5)

def vapr_047_high_volume_node_dist_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_047_high_volume_node_dist_zscore_5d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 5)

def vapr_048_high_volume_node_dist_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_048_high_volume_node_dist_rank_5d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 5)

def vapr_049_high_volume_node_dist_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_049_high_volume_node_dist_lvl_21d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 21)

def vapr_050_high_volume_node_dist_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_050_high_volume_node_dist_zscore_21d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 21)

def vapr_051_high_volume_node_dist_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_051_high_volume_node_dist_rank_21d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 21)

def vapr_052_high_volume_node_dist_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_052_high_volume_node_dist_lvl_63d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 63)

def vapr_053_high_volume_node_dist_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_053_high_volume_node_dist_zscore_63d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 63)

def vapr_054_high_volume_node_dist_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_054_high_volume_node_dist_rank_63d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 63)

def vapr_055_high_volume_node_dist_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_055_high_volume_node_dist_lvl_126d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 126)

def vapr_056_high_volume_node_dist_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_056_high_volume_node_dist_zscore_126d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 126)

def vapr_057_high_volume_node_dist_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_057_high_volume_node_dist_rank_126d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 126)

def vapr_058_high_volume_node_dist_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_058_high_volume_node_dist_lvl_252d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rolling_mean(base, 252)

def vapr_059_high_volume_node_dist_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_059_high_volume_node_dist_zscore_252d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _zscore_rolling(base, 252)

def vapr_060_high_volume_node_dist_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_060_high_volume_node_dist_rank_252d
    ECONOMIC RATIONALE: Distance from long-term high volume nodes.
    """
    base = close - close.rolling(252).apply(lambda x: x[np.argmax(np.histogram(x, weights=volume.iloc[close.index.get_indexer(x.index)])[0])])
    return _rank_pct(base, 252)

def vapr_061_low_volume_node_flag_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_061_low_volume_node_flag_lvl_5d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rolling_mean(base, 5)

def vapr_062_low_volume_node_flag_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_062_low_volume_node_flag_zscore_5d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _zscore_rolling(base, 5)

def vapr_063_low_volume_node_flag_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_063_low_volume_node_flag_rank_5d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rank_pct(base, 5)

def vapr_064_low_volume_node_flag_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_064_low_volume_node_flag_lvl_21d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rolling_mean(base, 21)

def vapr_065_low_volume_node_flag_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_065_low_volume_node_flag_zscore_21d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _zscore_rolling(base, 21)

def vapr_066_low_volume_node_flag_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_066_low_volume_node_flag_rank_21d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rank_pct(base, 21)

def vapr_067_low_volume_node_flag_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_067_low_volume_node_flag_lvl_63d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rolling_mean(base, 63)

def vapr_068_low_volume_node_flag_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_068_low_volume_node_flag_zscore_63d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _zscore_rolling(base, 63)

def vapr_069_low_volume_node_flag_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_069_low_volume_node_flag_rank_63d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rank_pct(base, 63)

def vapr_070_low_volume_node_flag_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_070_low_volume_node_flag_lvl_126d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rolling_mean(base, 126)

def vapr_071_low_volume_node_flag_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_071_low_volume_node_flag_zscore_126d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _zscore_rolling(base, 126)

def vapr_072_low_volume_node_flag_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_072_low_volume_node_flag_rank_126d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rank_pct(base, 126)

def vapr_073_low_volume_node_flag_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_073_low_volume_node_flag_lvl_252d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rolling_mean(base, 252)

def vapr_074_low_volume_node_flag_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_074_low_volume_node_flag_zscore_252d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _zscore_rolling(base, 252)

def vapr_075_low_volume_node_flag_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_075_low_volume_node_flag_rank_252d
    ECONOMIC RATIONALE: Trading in low-volume price vacuum zones.
    """
    base = ((volume < volume.rolling(63).mean()*0.5)).astype(float)
    return _rank_pct(base, 252)

def vapr_076_volume_skew_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_076_volume_skew_lvl_5d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rolling_mean(base, 5)

def vapr_077_volume_skew_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_077_volume_skew_zscore_5d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _zscore_rolling(base, 5)

def vapr_078_volume_skew_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_078_volume_skew_rank_5d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rank_pct(base, 5)

def vapr_079_volume_skew_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_079_volume_skew_lvl_21d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rolling_mean(base, 21)

def vapr_080_volume_skew_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_080_volume_skew_zscore_21d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _zscore_rolling(base, 21)

def vapr_081_volume_skew_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_081_volume_skew_rank_21d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rank_pct(base, 21)

def vapr_082_volume_skew_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_082_volume_skew_lvl_63d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rolling_mean(base, 63)

def vapr_083_volume_skew_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_083_volume_skew_zscore_63d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _zscore_rolling(base, 63)

def vapr_084_volume_skew_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_084_volume_skew_rank_63d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rank_pct(base, 63)

def vapr_085_volume_skew_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_085_volume_skew_lvl_126d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rolling_mean(base, 126)

def vapr_086_volume_skew_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_086_volume_skew_zscore_126d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _zscore_rolling(base, 126)

def vapr_087_volume_skew_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_087_volume_skew_rank_126d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rank_pct(base, 126)

def vapr_088_volume_skew_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_088_volume_skew_lvl_252d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rolling_mean(base, 252)

def vapr_089_volume_skew_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_089_volume_skew_zscore_252d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _zscore_rolling(base, 252)

def vapr_090_volume_skew_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_090_volume_skew_rank_252d
    ECONOMIC RATIONALE: Asymmetry of volume distribution across price.
    """
    base = volume.rolling(63).skew()
    return _rank_pct(base, 252)

def vapr_091_vapr_zscore_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_091_vapr_zscore_lvl_5d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rolling_mean(base, 5)

def vapr_092_vapr_zscore_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_092_vapr_zscore_zscore_5d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 5)

def vapr_093_vapr_zscore_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_093_vapr_zscore_rank_5d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rank_pct(base, 5)

def vapr_094_vapr_zscore_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_094_vapr_zscore_lvl_21d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rolling_mean(base, 21)

def vapr_095_vapr_zscore_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_095_vapr_zscore_zscore_21d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 21)

def vapr_096_vapr_zscore_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_096_vapr_zscore_rank_21d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rank_pct(base, 21)

def vapr_097_vapr_zscore_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_097_vapr_zscore_lvl_63d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rolling_mean(base, 63)

def vapr_098_vapr_zscore_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_098_vapr_zscore_zscore_63d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 63)

def vapr_099_vapr_zscore_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_099_vapr_zscore_rank_63d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rank_pct(base, 63)

def vapr_100_vapr_zscore_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_100_vapr_zscore_lvl_126d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rolling_mean(base, 126)

def vapr_101_vapr_zscore_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_101_vapr_zscore_zscore_126d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 126)

def vapr_102_vapr_zscore_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_102_vapr_zscore_rank_126d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rank_pct(base, 126)

def vapr_103_vapr_zscore_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_103_vapr_zscore_lvl_252d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rolling_mean(base, 252)

def vapr_104_vapr_zscore_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_104_vapr_zscore_zscore_252d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _zscore_rolling(base, 252)

def vapr_105_vapr_zscore_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_105_vapr_zscore_rank_252d
    ECONOMIC RATIONALE: Abnormality of volume per price unit.
    """
    base = _zscore_rolling(volume / (high - low).replace(0, 1e-9), 252)
    return _rank_pct(base, 252)

def vapr_106_volume_concentration_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_106_volume_concentration_lvl_5d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rolling_mean(base, 5)

def vapr_107_volume_concentration_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_107_volume_concentration_zscore_5d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _zscore_rolling(base, 5)

def vapr_108_volume_concentration_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_108_volume_concentration_rank_5d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rank_pct(base, 5)

def vapr_109_volume_concentration_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_109_volume_concentration_lvl_21d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rolling_mean(base, 21)

def vapr_110_volume_concentration_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_110_volume_concentration_zscore_21d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _zscore_rolling(base, 21)

def vapr_111_volume_concentration_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_111_volume_concentration_rank_21d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rank_pct(base, 21)

def vapr_112_volume_concentration_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_112_volume_concentration_lvl_63d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rolling_mean(base, 63)

def vapr_113_volume_concentration_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_113_volume_concentration_zscore_63d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _zscore_rolling(base, 63)

def vapr_114_volume_concentration_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_114_volume_concentration_rank_63d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rank_pct(base, 63)

def vapr_115_volume_concentration_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_115_volume_concentration_lvl_126d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rolling_mean(base, 126)

def vapr_116_volume_concentration_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_116_volume_concentration_zscore_126d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _zscore_rolling(base, 126)

def vapr_117_volume_concentration_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_117_volume_concentration_rank_126d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rank_pct(base, 126)

def vapr_118_volume_concentration_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_118_volume_concentration_lvl_252d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rolling_mean(base, 252)

def vapr_119_volume_concentration_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_119_volume_concentration_zscore_252d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _zscore_rolling(base, 252)

def vapr_120_volume_concentration_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vapr_120_volume_concentration_rank_252d
    ECONOMIC RATIONALE: Concentration of volume at current price levels.
    """
    base = volume.rolling(21).sum() / volume.rolling(252).sum()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V112_REGISTRY_1 = {
    "vapr_001_volume_poc_dist_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_001_volume_poc_dist_lvl_5d},
    "vapr_002_volume_poc_dist_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_002_volume_poc_dist_zscore_5d},
    "vapr_003_volume_poc_dist_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_003_volume_poc_dist_rank_5d},
    "vapr_004_volume_poc_dist_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_004_volume_poc_dist_lvl_21d},
    "vapr_005_volume_poc_dist_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_005_volume_poc_dist_zscore_21d},
    "vapr_006_volume_poc_dist_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_006_volume_poc_dist_rank_21d},
    "vapr_007_volume_poc_dist_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_007_volume_poc_dist_lvl_63d},
    "vapr_008_volume_poc_dist_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_008_volume_poc_dist_zscore_63d},
    "vapr_009_volume_poc_dist_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_009_volume_poc_dist_rank_63d},
    "vapr_010_volume_poc_dist_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_010_volume_poc_dist_lvl_126d},
    "vapr_011_volume_poc_dist_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_011_volume_poc_dist_zscore_126d},
    "vapr_012_volume_poc_dist_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_012_volume_poc_dist_rank_126d},
    "vapr_013_volume_poc_dist_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_013_volume_poc_dist_lvl_252d},
    "vapr_014_volume_poc_dist_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_014_volume_poc_dist_zscore_252d},
    "vapr_015_volume_poc_dist_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_015_volume_poc_dist_rank_252d},
    "vapr_016_value_area_high_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_016_value_area_high_lvl_5d},
    "vapr_017_value_area_high_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_017_value_area_high_zscore_5d},
    "vapr_018_value_area_high_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_018_value_area_high_rank_5d},
    "vapr_019_value_area_high_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_019_value_area_high_lvl_21d},
    "vapr_020_value_area_high_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_020_value_area_high_zscore_21d},
    "vapr_021_value_area_high_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_021_value_area_high_rank_21d},
    "vapr_022_value_area_high_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_022_value_area_high_lvl_63d},
    "vapr_023_value_area_high_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_023_value_area_high_zscore_63d},
    "vapr_024_value_area_high_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_024_value_area_high_rank_63d},
    "vapr_025_value_area_high_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_025_value_area_high_lvl_126d},
    "vapr_026_value_area_high_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_026_value_area_high_zscore_126d},
    "vapr_027_value_area_high_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_027_value_area_high_rank_126d},
    "vapr_028_value_area_high_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_028_value_area_high_lvl_252d},
    "vapr_029_value_area_high_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_029_value_area_high_zscore_252d},
    "vapr_030_value_area_high_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_030_value_area_high_rank_252d},
    "vapr_031_value_area_low_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_031_value_area_low_lvl_5d},
    "vapr_032_value_area_low_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_032_value_area_low_zscore_5d},
    "vapr_033_value_area_low_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_033_value_area_low_rank_5d},
    "vapr_034_value_area_low_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_034_value_area_low_lvl_21d},
    "vapr_035_value_area_low_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_035_value_area_low_zscore_21d},
    "vapr_036_value_area_low_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_036_value_area_low_rank_21d},
    "vapr_037_value_area_low_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_037_value_area_low_lvl_63d},
    "vapr_038_value_area_low_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_038_value_area_low_zscore_63d},
    "vapr_039_value_area_low_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_039_value_area_low_rank_63d},
    "vapr_040_value_area_low_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_040_value_area_low_lvl_126d},
    "vapr_041_value_area_low_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_041_value_area_low_zscore_126d},
    "vapr_042_value_area_low_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_042_value_area_low_rank_126d},
    "vapr_043_value_area_low_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_043_value_area_low_lvl_252d},
    "vapr_044_value_area_low_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_044_value_area_low_zscore_252d},
    "vapr_045_value_area_low_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_045_value_area_low_rank_252d},
    "vapr_046_high_volume_node_dist_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_046_high_volume_node_dist_lvl_5d},
    "vapr_047_high_volume_node_dist_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_047_high_volume_node_dist_zscore_5d},
    "vapr_048_high_volume_node_dist_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_048_high_volume_node_dist_rank_5d},
    "vapr_049_high_volume_node_dist_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_049_high_volume_node_dist_lvl_21d},
    "vapr_050_high_volume_node_dist_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_050_high_volume_node_dist_zscore_21d},
    "vapr_051_high_volume_node_dist_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_051_high_volume_node_dist_rank_21d},
    "vapr_052_high_volume_node_dist_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_052_high_volume_node_dist_lvl_63d},
    "vapr_053_high_volume_node_dist_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_053_high_volume_node_dist_zscore_63d},
    "vapr_054_high_volume_node_dist_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_054_high_volume_node_dist_rank_63d},
    "vapr_055_high_volume_node_dist_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_055_high_volume_node_dist_lvl_126d},
    "vapr_056_high_volume_node_dist_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_056_high_volume_node_dist_zscore_126d},
    "vapr_057_high_volume_node_dist_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_057_high_volume_node_dist_rank_126d},
    "vapr_058_high_volume_node_dist_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_058_high_volume_node_dist_lvl_252d},
    "vapr_059_high_volume_node_dist_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_059_high_volume_node_dist_zscore_252d},
    "vapr_060_high_volume_node_dist_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_060_high_volume_node_dist_rank_252d},
    "vapr_061_low_volume_node_flag_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_061_low_volume_node_flag_lvl_5d},
    "vapr_062_low_volume_node_flag_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_062_low_volume_node_flag_zscore_5d},
    "vapr_063_low_volume_node_flag_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_063_low_volume_node_flag_rank_5d},
    "vapr_064_low_volume_node_flag_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_064_low_volume_node_flag_lvl_21d},
    "vapr_065_low_volume_node_flag_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_065_low_volume_node_flag_zscore_21d},
    "vapr_066_low_volume_node_flag_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_066_low_volume_node_flag_rank_21d},
    "vapr_067_low_volume_node_flag_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_067_low_volume_node_flag_lvl_63d},
    "vapr_068_low_volume_node_flag_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_068_low_volume_node_flag_zscore_63d},
    "vapr_069_low_volume_node_flag_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_069_low_volume_node_flag_rank_63d},
    "vapr_070_low_volume_node_flag_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_070_low_volume_node_flag_lvl_126d},
    "vapr_071_low_volume_node_flag_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_071_low_volume_node_flag_zscore_126d},
    "vapr_072_low_volume_node_flag_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_072_low_volume_node_flag_rank_126d},
    "vapr_073_low_volume_node_flag_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_073_low_volume_node_flag_lvl_252d},
    "vapr_074_low_volume_node_flag_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_074_low_volume_node_flag_zscore_252d},
    "vapr_075_low_volume_node_flag_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_075_low_volume_node_flag_rank_252d},
    "vapr_076_volume_skew_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_076_volume_skew_lvl_5d},
    "vapr_077_volume_skew_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_077_volume_skew_zscore_5d},
    "vapr_078_volume_skew_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_078_volume_skew_rank_5d},
    "vapr_079_volume_skew_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_079_volume_skew_lvl_21d},
    "vapr_080_volume_skew_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_080_volume_skew_zscore_21d},
    "vapr_081_volume_skew_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_081_volume_skew_rank_21d},
    "vapr_082_volume_skew_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_082_volume_skew_lvl_63d},
    "vapr_083_volume_skew_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_083_volume_skew_zscore_63d},
    "vapr_084_volume_skew_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_084_volume_skew_rank_63d},
    "vapr_085_volume_skew_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_085_volume_skew_lvl_126d},
    "vapr_086_volume_skew_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_086_volume_skew_zscore_126d},
    "vapr_087_volume_skew_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_087_volume_skew_rank_126d},
    "vapr_088_volume_skew_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_088_volume_skew_lvl_252d},
    "vapr_089_volume_skew_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_089_volume_skew_zscore_252d},
    "vapr_090_volume_skew_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_090_volume_skew_rank_252d},
    "vapr_091_vapr_zscore_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_091_vapr_zscore_lvl_5d},
    "vapr_092_vapr_zscore_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_092_vapr_zscore_zscore_5d},
    "vapr_093_vapr_zscore_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_093_vapr_zscore_rank_5d},
    "vapr_094_vapr_zscore_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_094_vapr_zscore_lvl_21d},
    "vapr_095_vapr_zscore_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_095_vapr_zscore_zscore_21d},
    "vapr_096_vapr_zscore_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_096_vapr_zscore_rank_21d},
    "vapr_097_vapr_zscore_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_097_vapr_zscore_lvl_63d},
    "vapr_098_vapr_zscore_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_098_vapr_zscore_zscore_63d},
    "vapr_099_vapr_zscore_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_099_vapr_zscore_rank_63d},
    "vapr_100_vapr_zscore_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_100_vapr_zscore_lvl_126d},
    "vapr_101_vapr_zscore_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_101_vapr_zscore_zscore_126d},
    "vapr_102_vapr_zscore_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_102_vapr_zscore_rank_126d},
    "vapr_103_vapr_zscore_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_103_vapr_zscore_lvl_252d},
    "vapr_104_vapr_zscore_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_104_vapr_zscore_zscore_252d},
    "vapr_105_vapr_zscore_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_105_vapr_zscore_rank_252d},
    "vapr_106_volume_concentration_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_106_volume_concentration_lvl_5d},
    "vapr_107_volume_concentration_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_107_volume_concentration_zscore_5d},
    "vapr_108_volume_concentration_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_108_volume_concentration_rank_5d},
    "vapr_109_volume_concentration_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_109_volume_concentration_lvl_21d},
    "vapr_110_volume_concentration_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_110_volume_concentration_zscore_21d},
    "vapr_111_volume_concentration_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_111_volume_concentration_rank_21d},
    "vapr_112_volume_concentration_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_112_volume_concentration_lvl_63d},
    "vapr_113_volume_concentration_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_113_volume_concentration_zscore_63d},
    "vapr_114_volume_concentration_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_114_volume_concentration_rank_63d},
    "vapr_115_volume_concentration_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_115_volume_concentration_lvl_126d},
    "vapr_116_volume_concentration_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_116_volume_concentration_zscore_126d},
    "vapr_117_volume_concentration_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_117_volume_concentration_rank_126d},
    "vapr_118_volume_concentration_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_118_volume_concentration_lvl_252d},
    "vapr_119_volume_concentration_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_119_volume_concentration_zscore_252d},
    "vapr_120_volume_concentration_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": vapr_120_volume_concentration_rank_252d},
}
