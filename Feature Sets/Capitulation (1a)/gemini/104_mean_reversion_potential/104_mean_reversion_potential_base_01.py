"""
104_mean_reversion_potential — Base Features Part 1
Domain: mean_reversion_potential
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

def mrpt_001_bollinger_pct_b_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_001_bollinger_pct_b_lvl_5d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def mrpt_002_bollinger_pct_b_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_002_bollinger_pct_b_zscore_5d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mrpt_003_bollinger_pct_b_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_003_bollinger_pct_b_rank_5d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def mrpt_004_bollinger_pct_b_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_004_bollinger_pct_b_lvl_21d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def mrpt_005_bollinger_pct_b_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_005_bollinger_pct_b_zscore_21d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mrpt_006_bollinger_pct_b_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_006_bollinger_pct_b_rank_21d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def mrpt_007_bollinger_pct_b_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_007_bollinger_pct_b_lvl_63d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def mrpt_008_bollinger_pct_b_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_008_bollinger_pct_b_zscore_63d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mrpt_009_bollinger_pct_b_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_009_bollinger_pct_b_rank_63d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def mrpt_010_bollinger_pct_b_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_010_bollinger_pct_b_lvl_126d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def mrpt_011_bollinger_pct_b_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_011_bollinger_pct_b_zscore_126d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mrpt_012_bollinger_pct_b_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_012_bollinger_pct_b_rank_126d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def mrpt_013_bollinger_pct_b_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_013_bollinger_pct_b_lvl_252d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def mrpt_014_bollinger_pct_b_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_014_bollinger_pct_b_zscore_252d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def mrpt_015_bollinger_pct_b_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_015_bollinger_pct_b_rank_252d
    ECONOMIC RATIONALE: Position within Bollinger Bands.
    """
    base = (close - (close.rolling(20).mean() - 2*close.rolling(20).std())) / (4*close.rolling(20).std()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def mrpt_016_distance_from_ma200_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_016_distance_from_ma200_lvl_5d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rolling_mean(base, 5)

def mrpt_017_distance_from_ma200_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_017_distance_from_ma200_zscore_5d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _zscore_rolling(base, 5)

def mrpt_018_distance_from_ma200_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_018_distance_from_ma200_rank_5d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rank_pct(base, 5)

def mrpt_019_distance_from_ma200_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_019_distance_from_ma200_lvl_21d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rolling_mean(base, 21)

def mrpt_020_distance_from_ma200_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_020_distance_from_ma200_zscore_21d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _zscore_rolling(base, 21)

def mrpt_021_distance_from_ma200_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_021_distance_from_ma200_rank_21d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rank_pct(base, 21)

def mrpt_022_distance_from_ma200_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_022_distance_from_ma200_lvl_63d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rolling_mean(base, 63)

def mrpt_023_distance_from_ma200_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_023_distance_from_ma200_zscore_63d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _zscore_rolling(base, 63)

def mrpt_024_distance_from_ma200_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_024_distance_from_ma200_rank_63d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rank_pct(base, 63)

def mrpt_025_distance_from_ma200_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_025_distance_from_ma200_lvl_126d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rolling_mean(base, 126)

def mrpt_026_distance_from_ma200_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_026_distance_from_ma200_zscore_126d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _zscore_rolling(base, 126)

def mrpt_027_distance_from_ma200_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_027_distance_from_ma200_rank_126d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rank_pct(base, 126)

def mrpt_028_distance_from_ma200_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_028_distance_from_ma200_lvl_252d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rolling_mean(base, 252)

def mrpt_029_distance_from_ma200_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_029_distance_from_ma200_zscore_252d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _zscore_rolling(base, 252)

def mrpt_030_distance_from_ma200_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_030_distance_from_ma200_rank_252d
    ECONOMIC RATIONALE: Percentage deviation from the 200-day moving average.
    """
    base = close / close.rolling(252).mean() - 1
    return _rank_pct(base, 252)

def mrpt_031_keltner_channel_lower_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_031_keltner_channel_lower_lvl_5d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rolling_mean(base, 5)

def mrpt_032_keltner_channel_lower_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_032_keltner_channel_lower_zscore_5d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _zscore_rolling(base, 5)

def mrpt_033_keltner_channel_lower_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_033_keltner_channel_lower_rank_5d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rank_pct(base, 5)

def mrpt_034_keltner_channel_lower_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_034_keltner_channel_lower_lvl_21d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rolling_mean(base, 21)

def mrpt_035_keltner_channel_lower_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_035_keltner_channel_lower_zscore_21d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _zscore_rolling(base, 21)

def mrpt_036_keltner_channel_lower_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_036_keltner_channel_lower_rank_21d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rank_pct(base, 21)

def mrpt_037_keltner_channel_lower_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_037_keltner_channel_lower_lvl_63d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rolling_mean(base, 63)

def mrpt_038_keltner_channel_lower_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_038_keltner_channel_lower_zscore_63d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _zscore_rolling(base, 63)

def mrpt_039_keltner_channel_lower_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_039_keltner_channel_lower_rank_63d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rank_pct(base, 63)

def mrpt_040_keltner_channel_lower_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_040_keltner_channel_lower_lvl_126d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rolling_mean(base, 126)

def mrpt_041_keltner_channel_lower_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_041_keltner_channel_lower_zscore_126d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _zscore_rolling(base, 126)

def mrpt_042_keltner_channel_lower_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_042_keltner_channel_lower_rank_126d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rank_pct(base, 126)

def mrpt_043_keltner_channel_lower_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_043_keltner_channel_lower_lvl_252d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rolling_mean(base, 252)

def mrpt_044_keltner_channel_lower_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_044_keltner_channel_lower_zscore_252d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _zscore_rolling(base, 252)

def mrpt_045_keltner_channel_lower_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_045_keltner_channel_lower_rank_252d
    ECONOMIC RATIONALE: Position relative to Keltner Channels.
    """
    base = close / (close.rolling(20).mean() - 2*(high-low).rolling(20).mean()) - 1
    return _rank_pct(base, 252)

def mrpt_046_mean_reversion_z_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_046_mean_reversion_z_lvl_5d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 5)

def mrpt_047_mean_reversion_z_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_047_mean_reversion_z_zscore_5d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 5)

def mrpt_048_mean_reversion_z_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_048_mean_reversion_z_rank_5d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 5)

def mrpt_049_mean_reversion_z_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_049_mean_reversion_z_lvl_21d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 21)

def mrpt_050_mean_reversion_z_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_050_mean_reversion_z_zscore_21d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 21)

def mrpt_051_mean_reversion_z_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_051_mean_reversion_z_rank_21d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 21)

def mrpt_052_mean_reversion_z_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_052_mean_reversion_z_lvl_63d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 63)

def mrpt_053_mean_reversion_z_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_053_mean_reversion_z_zscore_63d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 63)

def mrpt_054_mean_reversion_z_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_054_mean_reversion_z_rank_63d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 63)

def mrpt_055_mean_reversion_z_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_055_mean_reversion_z_lvl_126d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 126)

def mrpt_056_mean_reversion_z_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_056_mean_reversion_z_zscore_126d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 126)

def mrpt_057_mean_reversion_z_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_057_mean_reversion_z_rank_126d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 126)

def mrpt_058_mean_reversion_z_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_058_mean_reversion_z_lvl_252d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 252)

def mrpt_059_mean_reversion_z_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_059_mean_reversion_z_zscore_252d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 252)

def mrpt_060_mean_reversion_z_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_060_mean_reversion_z_rank_252d
    ECONOMIC RATIONALE: Z-score relative to 63-day price distribution.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 252)

def mrpt_061_extreme_stretch_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_061_extreme_stretch_lvl_5d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rolling_mean(base, 5)

def mrpt_062_extreme_stretch_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_062_extreme_stretch_zscore_5d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _zscore_rolling(base, 5)

def mrpt_063_extreme_stretch_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_063_extreme_stretch_rank_5d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rank_pct(base, 5)

def mrpt_064_extreme_stretch_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_064_extreme_stretch_lvl_21d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rolling_mean(base, 21)

def mrpt_065_extreme_stretch_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_065_extreme_stretch_zscore_21d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _zscore_rolling(base, 21)

def mrpt_066_extreme_stretch_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_066_extreme_stretch_rank_21d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rank_pct(base, 21)

def mrpt_067_extreme_stretch_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_067_extreme_stretch_lvl_63d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rolling_mean(base, 63)

def mrpt_068_extreme_stretch_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_068_extreme_stretch_zscore_63d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _zscore_rolling(base, 63)

def mrpt_069_extreme_stretch_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_069_extreme_stretch_rank_63d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rank_pct(base, 63)

def mrpt_070_extreme_stretch_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_070_extreme_stretch_lvl_126d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rolling_mean(base, 126)

def mrpt_071_extreme_stretch_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_071_extreme_stretch_zscore_126d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _zscore_rolling(base, 126)

def mrpt_072_extreme_stretch_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_072_extreme_stretch_rank_126d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rank_pct(base, 126)

def mrpt_073_extreme_stretch_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_073_extreme_stretch_lvl_252d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rolling_mean(base, 252)

def mrpt_074_extreme_stretch_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_074_extreme_stretch_zscore_252d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _zscore_rolling(base, 252)

def mrpt_075_extreme_stretch_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_075_extreme_stretch_rank_252d
    ECONOMIC RATIONALE: Short-term price stretch from the mean.
    """
    base = close / close.rolling(5).mean() - 1
    return _rank_pct(base, 252)

def mrpt_076_reversion_velocity_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_076_reversion_velocity_lvl_5d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rolling_mean(base, 5)

def mrpt_077_reversion_velocity_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_077_reversion_velocity_zscore_5d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _zscore_rolling(base, 5)

def mrpt_078_reversion_velocity_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_078_reversion_velocity_rank_5d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rank_pct(base, 5)

def mrpt_079_reversion_velocity_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_079_reversion_velocity_lvl_21d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rolling_mean(base, 21)

def mrpt_080_reversion_velocity_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_080_reversion_velocity_zscore_21d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _zscore_rolling(base, 21)

def mrpt_081_reversion_velocity_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_081_reversion_velocity_rank_21d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rank_pct(base, 21)

def mrpt_082_reversion_velocity_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_082_reversion_velocity_lvl_63d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rolling_mean(base, 63)

def mrpt_083_reversion_velocity_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_083_reversion_velocity_zscore_63d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _zscore_rolling(base, 63)

def mrpt_084_reversion_velocity_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_084_reversion_velocity_rank_63d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rank_pct(base, 63)

def mrpt_085_reversion_velocity_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_085_reversion_velocity_lvl_126d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rolling_mean(base, 126)

def mrpt_086_reversion_velocity_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_086_reversion_velocity_zscore_126d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _zscore_rolling(base, 126)

def mrpt_087_reversion_velocity_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_087_reversion_velocity_rank_126d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rank_pct(base, 126)

def mrpt_088_reversion_velocity_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_088_reversion_velocity_lvl_252d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rolling_mean(base, 252)

def mrpt_089_reversion_velocity_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_089_reversion_velocity_zscore_252d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _zscore_rolling(base, 252)

def mrpt_090_reversion_velocity_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_090_reversion_velocity_rank_252d
    ECONOMIC RATIONALE: Price change normalized by volatility.
    """
    base = close.diff(5) / close.rolling(21).std()
    return _rank_pct(base, 252)

def mrpt_091_ma_cross_intensity_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_091_ma_cross_intensity_lvl_5d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rolling_mean(base, 5)

def mrpt_092_ma_cross_intensity_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_092_ma_cross_intensity_zscore_5d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _zscore_rolling(base, 5)

def mrpt_093_ma_cross_intensity_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_093_ma_cross_intensity_rank_5d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rank_pct(base, 5)

def mrpt_094_ma_cross_intensity_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_094_ma_cross_intensity_lvl_21d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rolling_mean(base, 21)

def mrpt_095_ma_cross_intensity_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_095_ma_cross_intensity_zscore_21d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _zscore_rolling(base, 21)

def mrpt_096_ma_cross_intensity_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_096_ma_cross_intensity_rank_21d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rank_pct(base, 21)

def mrpt_097_ma_cross_intensity_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_097_ma_cross_intensity_lvl_63d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rolling_mean(base, 63)

def mrpt_098_ma_cross_intensity_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_098_ma_cross_intensity_zscore_63d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _zscore_rolling(base, 63)

def mrpt_099_ma_cross_intensity_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_099_ma_cross_intensity_rank_63d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rank_pct(base, 63)

def mrpt_100_ma_cross_intensity_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_100_ma_cross_intensity_lvl_126d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rolling_mean(base, 126)

def mrpt_101_ma_cross_intensity_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_101_ma_cross_intensity_zscore_126d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _zscore_rolling(base, 126)

def mrpt_102_ma_cross_intensity_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_102_ma_cross_intensity_rank_126d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rank_pct(base, 126)

def mrpt_103_ma_cross_intensity_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_103_ma_cross_intensity_lvl_252d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rolling_mean(base, 252)

def mrpt_104_ma_cross_intensity_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_104_ma_cross_intensity_zscore_252d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _zscore_rolling(base, 252)

def mrpt_105_ma_cross_intensity_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_105_ma_cross_intensity_rank_252d
    ECONOMIC RATIONALE: Intensity of short-term MA crossover.
    """
    base = (close.rolling(5).mean() - close.rolling(21).mean()) / close.rolling(21).std()
    return _rank_pct(base, 252)

def mrpt_106_overshot_magnitude_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_106_overshot_magnitude_lvl_5d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rolling_mean(base, 5)

def mrpt_107_overshot_magnitude_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_107_overshot_magnitude_zscore_5d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _zscore_rolling(base, 5)

def mrpt_108_overshot_magnitude_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_108_overshot_magnitude_rank_5d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rank_pct(base, 5)

def mrpt_109_overshot_magnitude_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_109_overshot_magnitude_lvl_21d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rolling_mean(base, 21)

def mrpt_110_overshot_magnitude_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_110_overshot_magnitude_zscore_21d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _zscore_rolling(base, 21)

def mrpt_111_overshot_magnitude_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_111_overshot_magnitude_rank_21d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rank_pct(base, 21)

def mrpt_112_overshot_magnitude_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_112_overshot_magnitude_lvl_63d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rolling_mean(base, 63)

def mrpt_113_overshot_magnitude_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_113_overshot_magnitude_zscore_63d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _zscore_rolling(base, 63)

def mrpt_114_overshot_magnitude_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_114_overshot_magnitude_rank_63d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rank_pct(base, 63)

def mrpt_115_overshot_magnitude_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_115_overshot_magnitude_lvl_126d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rolling_mean(base, 126)

def mrpt_116_overshot_magnitude_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_116_overshot_magnitude_zscore_126d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _zscore_rolling(base, 126)

def mrpt_117_overshot_magnitude_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_117_overshot_magnitude_rank_126d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rank_pct(base, 126)

def mrpt_118_overshot_magnitude_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_118_overshot_magnitude_lvl_252d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rolling_mean(base, 252)

def mrpt_119_overshot_magnitude_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_119_overshot_magnitude_zscore_252d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _zscore_rolling(base, 252)

def mrpt_120_overshot_magnitude_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    mrpt_120_overshot_magnitude_rank_252d
    ECONOMIC RATIONALE: Intraday low's distance from the mean.
    """
    base = low / close.rolling(20).mean() - 1
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V104_REGISTRY_1 = {
    "mrpt_001_bollinger_pct_b_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_001_bollinger_pct_b_lvl_5d},
    "mrpt_002_bollinger_pct_b_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_002_bollinger_pct_b_zscore_5d},
    "mrpt_003_bollinger_pct_b_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_003_bollinger_pct_b_rank_5d},
    "mrpt_004_bollinger_pct_b_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_004_bollinger_pct_b_lvl_21d},
    "mrpt_005_bollinger_pct_b_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_005_bollinger_pct_b_zscore_21d},
    "mrpt_006_bollinger_pct_b_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_006_bollinger_pct_b_rank_21d},
    "mrpt_007_bollinger_pct_b_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_007_bollinger_pct_b_lvl_63d},
    "mrpt_008_bollinger_pct_b_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_008_bollinger_pct_b_zscore_63d},
    "mrpt_009_bollinger_pct_b_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_009_bollinger_pct_b_rank_63d},
    "mrpt_010_bollinger_pct_b_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_010_bollinger_pct_b_lvl_126d},
    "mrpt_011_bollinger_pct_b_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_011_bollinger_pct_b_zscore_126d},
    "mrpt_012_bollinger_pct_b_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_012_bollinger_pct_b_rank_126d},
    "mrpt_013_bollinger_pct_b_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_013_bollinger_pct_b_lvl_252d},
    "mrpt_014_bollinger_pct_b_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_014_bollinger_pct_b_zscore_252d},
    "mrpt_015_bollinger_pct_b_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_015_bollinger_pct_b_rank_252d},
    "mrpt_016_distance_from_ma200_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_016_distance_from_ma200_lvl_5d},
    "mrpt_017_distance_from_ma200_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_017_distance_from_ma200_zscore_5d},
    "mrpt_018_distance_from_ma200_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_018_distance_from_ma200_rank_5d},
    "mrpt_019_distance_from_ma200_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_019_distance_from_ma200_lvl_21d},
    "mrpt_020_distance_from_ma200_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_020_distance_from_ma200_zscore_21d},
    "mrpt_021_distance_from_ma200_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_021_distance_from_ma200_rank_21d},
    "mrpt_022_distance_from_ma200_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_022_distance_from_ma200_lvl_63d},
    "mrpt_023_distance_from_ma200_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_023_distance_from_ma200_zscore_63d},
    "mrpt_024_distance_from_ma200_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_024_distance_from_ma200_rank_63d},
    "mrpt_025_distance_from_ma200_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_025_distance_from_ma200_lvl_126d},
    "mrpt_026_distance_from_ma200_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_026_distance_from_ma200_zscore_126d},
    "mrpt_027_distance_from_ma200_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_027_distance_from_ma200_rank_126d},
    "mrpt_028_distance_from_ma200_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_028_distance_from_ma200_lvl_252d},
    "mrpt_029_distance_from_ma200_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_029_distance_from_ma200_zscore_252d},
    "mrpt_030_distance_from_ma200_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_030_distance_from_ma200_rank_252d},
    "mrpt_031_keltner_channel_lower_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_031_keltner_channel_lower_lvl_5d},
    "mrpt_032_keltner_channel_lower_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_032_keltner_channel_lower_zscore_5d},
    "mrpt_033_keltner_channel_lower_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_033_keltner_channel_lower_rank_5d},
    "mrpt_034_keltner_channel_lower_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_034_keltner_channel_lower_lvl_21d},
    "mrpt_035_keltner_channel_lower_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_035_keltner_channel_lower_zscore_21d},
    "mrpt_036_keltner_channel_lower_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_036_keltner_channel_lower_rank_21d},
    "mrpt_037_keltner_channel_lower_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_037_keltner_channel_lower_lvl_63d},
    "mrpt_038_keltner_channel_lower_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_038_keltner_channel_lower_zscore_63d},
    "mrpt_039_keltner_channel_lower_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_039_keltner_channel_lower_rank_63d},
    "mrpt_040_keltner_channel_lower_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_040_keltner_channel_lower_lvl_126d},
    "mrpt_041_keltner_channel_lower_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_041_keltner_channel_lower_zscore_126d},
    "mrpt_042_keltner_channel_lower_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_042_keltner_channel_lower_rank_126d},
    "mrpt_043_keltner_channel_lower_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_043_keltner_channel_lower_lvl_252d},
    "mrpt_044_keltner_channel_lower_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_044_keltner_channel_lower_zscore_252d},
    "mrpt_045_keltner_channel_lower_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_045_keltner_channel_lower_rank_252d},
    "mrpt_046_mean_reversion_z_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_046_mean_reversion_z_lvl_5d},
    "mrpt_047_mean_reversion_z_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_047_mean_reversion_z_zscore_5d},
    "mrpt_048_mean_reversion_z_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_048_mean_reversion_z_rank_5d},
    "mrpt_049_mean_reversion_z_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_049_mean_reversion_z_lvl_21d},
    "mrpt_050_mean_reversion_z_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_050_mean_reversion_z_zscore_21d},
    "mrpt_051_mean_reversion_z_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_051_mean_reversion_z_rank_21d},
    "mrpt_052_mean_reversion_z_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_052_mean_reversion_z_lvl_63d},
    "mrpt_053_mean_reversion_z_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_053_mean_reversion_z_zscore_63d},
    "mrpt_054_mean_reversion_z_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_054_mean_reversion_z_rank_63d},
    "mrpt_055_mean_reversion_z_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_055_mean_reversion_z_lvl_126d},
    "mrpt_056_mean_reversion_z_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_056_mean_reversion_z_zscore_126d},
    "mrpt_057_mean_reversion_z_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_057_mean_reversion_z_rank_126d},
    "mrpt_058_mean_reversion_z_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_058_mean_reversion_z_lvl_252d},
    "mrpt_059_mean_reversion_z_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_059_mean_reversion_z_zscore_252d},
    "mrpt_060_mean_reversion_z_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_060_mean_reversion_z_rank_252d},
    "mrpt_061_extreme_stretch_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_061_extreme_stretch_lvl_5d},
    "mrpt_062_extreme_stretch_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_062_extreme_stretch_zscore_5d},
    "mrpt_063_extreme_stretch_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_063_extreme_stretch_rank_5d},
    "mrpt_064_extreme_stretch_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_064_extreme_stretch_lvl_21d},
    "mrpt_065_extreme_stretch_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_065_extreme_stretch_zscore_21d},
    "mrpt_066_extreme_stretch_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_066_extreme_stretch_rank_21d},
    "mrpt_067_extreme_stretch_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_067_extreme_stretch_lvl_63d},
    "mrpt_068_extreme_stretch_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_068_extreme_stretch_zscore_63d},
    "mrpt_069_extreme_stretch_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_069_extreme_stretch_rank_63d},
    "mrpt_070_extreme_stretch_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_070_extreme_stretch_lvl_126d},
    "mrpt_071_extreme_stretch_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_071_extreme_stretch_zscore_126d},
    "mrpt_072_extreme_stretch_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_072_extreme_stretch_rank_126d},
    "mrpt_073_extreme_stretch_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_073_extreme_stretch_lvl_252d},
    "mrpt_074_extreme_stretch_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_074_extreme_stretch_zscore_252d},
    "mrpt_075_extreme_stretch_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_075_extreme_stretch_rank_252d},
    "mrpt_076_reversion_velocity_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_076_reversion_velocity_lvl_5d},
    "mrpt_077_reversion_velocity_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_077_reversion_velocity_zscore_5d},
    "mrpt_078_reversion_velocity_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_078_reversion_velocity_rank_5d},
    "mrpt_079_reversion_velocity_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_079_reversion_velocity_lvl_21d},
    "mrpt_080_reversion_velocity_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_080_reversion_velocity_zscore_21d},
    "mrpt_081_reversion_velocity_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_081_reversion_velocity_rank_21d},
    "mrpt_082_reversion_velocity_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_082_reversion_velocity_lvl_63d},
    "mrpt_083_reversion_velocity_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_083_reversion_velocity_zscore_63d},
    "mrpt_084_reversion_velocity_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_084_reversion_velocity_rank_63d},
    "mrpt_085_reversion_velocity_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_085_reversion_velocity_lvl_126d},
    "mrpt_086_reversion_velocity_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_086_reversion_velocity_zscore_126d},
    "mrpt_087_reversion_velocity_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_087_reversion_velocity_rank_126d},
    "mrpt_088_reversion_velocity_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_088_reversion_velocity_lvl_252d},
    "mrpt_089_reversion_velocity_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_089_reversion_velocity_zscore_252d},
    "mrpt_090_reversion_velocity_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_090_reversion_velocity_rank_252d},
    "mrpt_091_ma_cross_intensity_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_091_ma_cross_intensity_lvl_5d},
    "mrpt_092_ma_cross_intensity_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_092_ma_cross_intensity_zscore_5d},
    "mrpt_093_ma_cross_intensity_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_093_ma_cross_intensity_rank_5d},
    "mrpt_094_ma_cross_intensity_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_094_ma_cross_intensity_lvl_21d},
    "mrpt_095_ma_cross_intensity_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_095_ma_cross_intensity_zscore_21d},
    "mrpt_096_ma_cross_intensity_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_096_ma_cross_intensity_rank_21d},
    "mrpt_097_ma_cross_intensity_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_097_ma_cross_intensity_lvl_63d},
    "mrpt_098_ma_cross_intensity_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_098_ma_cross_intensity_zscore_63d},
    "mrpt_099_ma_cross_intensity_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_099_ma_cross_intensity_rank_63d},
    "mrpt_100_ma_cross_intensity_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_100_ma_cross_intensity_lvl_126d},
    "mrpt_101_ma_cross_intensity_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_101_ma_cross_intensity_zscore_126d},
    "mrpt_102_ma_cross_intensity_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_102_ma_cross_intensity_rank_126d},
    "mrpt_103_ma_cross_intensity_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_103_ma_cross_intensity_lvl_252d},
    "mrpt_104_ma_cross_intensity_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_104_ma_cross_intensity_zscore_252d},
    "mrpt_105_ma_cross_intensity_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_105_ma_cross_intensity_rank_252d},
    "mrpt_106_overshot_magnitude_lvl_5d": {"inputs": ["close", "high", "low"], "func": mrpt_106_overshot_magnitude_lvl_5d},
    "mrpt_107_overshot_magnitude_zscore_5d": {"inputs": ["close", "high", "low"], "func": mrpt_107_overshot_magnitude_zscore_5d},
    "mrpt_108_overshot_magnitude_rank_5d": {"inputs": ["close", "high", "low"], "func": mrpt_108_overshot_magnitude_rank_5d},
    "mrpt_109_overshot_magnitude_lvl_21d": {"inputs": ["close", "high", "low"], "func": mrpt_109_overshot_magnitude_lvl_21d},
    "mrpt_110_overshot_magnitude_zscore_21d": {"inputs": ["close", "high", "low"], "func": mrpt_110_overshot_magnitude_zscore_21d},
    "mrpt_111_overshot_magnitude_rank_21d": {"inputs": ["close", "high", "low"], "func": mrpt_111_overshot_magnitude_rank_21d},
    "mrpt_112_overshot_magnitude_lvl_63d": {"inputs": ["close", "high", "low"], "func": mrpt_112_overshot_magnitude_lvl_63d},
    "mrpt_113_overshot_magnitude_zscore_63d": {"inputs": ["close", "high", "low"], "func": mrpt_113_overshot_magnitude_zscore_63d},
    "mrpt_114_overshot_magnitude_rank_63d": {"inputs": ["close", "high", "low"], "func": mrpt_114_overshot_magnitude_rank_63d},
    "mrpt_115_overshot_magnitude_lvl_126d": {"inputs": ["close", "high", "low"], "func": mrpt_115_overshot_magnitude_lvl_126d},
    "mrpt_116_overshot_magnitude_zscore_126d": {"inputs": ["close", "high", "low"], "func": mrpt_116_overshot_magnitude_zscore_126d},
    "mrpt_117_overshot_magnitude_rank_126d": {"inputs": ["close", "high", "low"], "func": mrpt_117_overshot_magnitude_rank_126d},
    "mrpt_118_overshot_magnitude_lvl_252d": {"inputs": ["close", "high", "low"], "func": mrpt_118_overshot_magnitude_lvl_252d},
    "mrpt_119_overshot_magnitude_zscore_252d": {"inputs": ["close", "high", "low"], "func": mrpt_119_overshot_magnitude_zscore_252d},
    "mrpt_120_overshot_magnitude_rank_252d": {"inputs": ["close", "high", "low"], "func": mrpt_120_overshot_magnitude_rank_252d},
}
