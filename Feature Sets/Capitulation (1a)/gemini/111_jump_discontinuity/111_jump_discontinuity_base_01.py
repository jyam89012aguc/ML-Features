"""
111_jump_discontinuity — Base Features Part 1
Domain: jump_discontinuity
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

def jump_001_price_jump_magnitude_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_001_price_jump_magnitude_lvl_5d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rolling_mean(base, 5)

def jump_002_price_jump_magnitude_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_002_price_jump_magnitude_zscore_5d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 5)

def jump_003_price_jump_magnitude_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_003_price_jump_magnitude_rank_5d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rank_pct(base, 5)

def jump_004_price_jump_magnitude_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_004_price_jump_magnitude_lvl_21d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rolling_mean(base, 21)

def jump_005_price_jump_magnitude_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_005_price_jump_magnitude_zscore_21d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 21)

def jump_006_price_jump_magnitude_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_006_price_jump_magnitude_rank_21d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rank_pct(base, 21)

def jump_007_price_jump_magnitude_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_007_price_jump_magnitude_lvl_63d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rolling_mean(base, 63)

def jump_008_price_jump_magnitude_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_008_price_jump_magnitude_zscore_63d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 63)

def jump_009_price_jump_magnitude_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_009_price_jump_magnitude_rank_63d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rank_pct(base, 63)

def jump_010_price_jump_magnitude_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_010_price_jump_magnitude_lvl_126d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rolling_mean(base, 126)

def jump_011_price_jump_magnitude_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_011_price_jump_magnitude_zscore_126d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 126)

def jump_012_price_jump_magnitude_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_012_price_jump_magnitude_rank_126d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rank_pct(base, 126)

def jump_013_price_jump_magnitude_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_013_price_jump_magnitude_lvl_252d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rolling_mean(base, 252)

def jump_014_price_jump_magnitude_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_014_price_jump_magnitude_zscore_252d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 252)

def jump_015_price_jump_magnitude_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_015_price_jump_magnitude_rank_252d
    ECONOMIC RATIONALE: Size of daily price jumps relative to volatility.
    """
    base = close.diff(1).abs() / close.rolling(21).std()
    return _rank_pct(base, 252)

def jump_016_overnight_gap_jump_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_016_overnight_gap_jump_lvl_5d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rolling_mean(base, 5)

def jump_017_overnight_gap_jump_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_017_overnight_gap_jump_zscore_5d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 5)

def jump_018_overnight_gap_jump_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_018_overnight_gap_jump_rank_5d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rank_pct(base, 5)

def jump_019_overnight_gap_jump_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_019_overnight_gap_jump_lvl_21d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rolling_mean(base, 21)

def jump_020_overnight_gap_jump_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_020_overnight_gap_jump_zscore_21d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 21)

def jump_021_overnight_gap_jump_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_021_overnight_gap_jump_rank_21d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rank_pct(base, 21)

def jump_022_overnight_gap_jump_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_022_overnight_gap_jump_lvl_63d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rolling_mean(base, 63)

def jump_023_overnight_gap_jump_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_023_overnight_gap_jump_zscore_63d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 63)

def jump_024_overnight_gap_jump_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_024_overnight_gap_jump_rank_63d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rank_pct(base, 63)

def jump_025_overnight_gap_jump_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_025_overnight_gap_jump_lvl_126d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rolling_mean(base, 126)

def jump_026_overnight_gap_jump_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_026_overnight_gap_jump_zscore_126d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 126)

def jump_027_overnight_gap_jump_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_027_overnight_gap_jump_rank_126d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rank_pct(base, 126)

def jump_028_overnight_gap_jump_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_028_overnight_gap_jump_lvl_252d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rolling_mean(base, 252)

def jump_029_overnight_gap_jump_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_029_overnight_gap_jump_zscore_252d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _zscore_rolling(base, 252)

def jump_030_overnight_gap_jump_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_030_overnight_gap_jump_rank_252d
    ECONOMIC RATIONALE: Magnitude of overnight gaps.
    """
    base = (open - close.shift(1)).abs() / close.rolling(21).std()
    return _rank_pct(base, 252)

def jump_031_jump_volume_intensity_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_031_jump_volume_intensity_lvl_5d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rolling_mean(base, 5)

def jump_032_jump_volume_intensity_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_032_jump_volume_intensity_zscore_5d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _zscore_rolling(base, 5)

def jump_033_jump_volume_intensity_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_033_jump_volume_intensity_rank_5d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rank_pct(base, 5)

def jump_034_jump_volume_intensity_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_034_jump_volume_intensity_lvl_21d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rolling_mean(base, 21)

def jump_035_jump_volume_intensity_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_035_jump_volume_intensity_zscore_21d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _zscore_rolling(base, 21)

def jump_036_jump_volume_intensity_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_036_jump_volume_intensity_rank_21d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rank_pct(base, 21)

def jump_037_jump_volume_intensity_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_037_jump_volume_intensity_lvl_63d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rolling_mean(base, 63)

def jump_038_jump_volume_intensity_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_038_jump_volume_intensity_zscore_63d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _zscore_rolling(base, 63)

def jump_039_jump_volume_intensity_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_039_jump_volume_intensity_rank_63d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rank_pct(base, 63)

def jump_040_jump_volume_intensity_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_040_jump_volume_intensity_lvl_126d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rolling_mean(base, 126)

def jump_041_jump_volume_intensity_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_041_jump_volume_intensity_zscore_126d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _zscore_rolling(base, 126)

def jump_042_jump_volume_intensity_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_042_jump_volume_intensity_rank_126d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rank_pct(base, 126)

def jump_043_jump_volume_intensity_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_043_jump_volume_intensity_lvl_252d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rolling_mean(base, 252)

def jump_044_jump_volume_intensity_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_044_jump_volume_intensity_zscore_252d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _zscore_rolling(base, 252)

def jump_045_jump_volume_intensity_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_045_jump_volume_intensity_rank_252d
    ECONOMIC RATIONALE: Volume-weighted jump magnitude.
    """
    base = volume * close.diff(1).abs()
    return _rank_pct(base, 252)

def jump_046_jump_frequency_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_046_jump_frequency_lvl_5d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rolling_mean(base, 5)

def jump_047_jump_frequency_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_047_jump_frequency_zscore_5d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _zscore_rolling(base, 5)

def jump_048_jump_frequency_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_048_jump_frequency_rank_5d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rank_pct(base, 5)

def jump_049_jump_frequency_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_049_jump_frequency_lvl_21d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rolling_mean(base, 21)

def jump_050_jump_frequency_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_050_jump_frequency_zscore_21d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _zscore_rolling(base, 21)

def jump_051_jump_frequency_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_051_jump_frequency_rank_21d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rank_pct(base, 21)

def jump_052_jump_frequency_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_052_jump_frequency_lvl_63d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rolling_mean(base, 63)

def jump_053_jump_frequency_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_053_jump_frequency_zscore_63d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _zscore_rolling(base, 63)

def jump_054_jump_frequency_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_054_jump_frequency_rank_63d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rank_pct(base, 63)

def jump_055_jump_frequency_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_055_jump_frequency_lvl_126d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rolling_mean(base, 126)

def jump_056_jump_frequency_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_056_jump_frequency_zscore_126d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _zscore_rolling(base, 126)

def jump_057_jump_frequency_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_057_jump_frequency_rank_126d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rank_pct(base, 126)

def jump_058_jump_frequency_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_058_jump_frequency_lvl_252d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rolling_mean(base, 252)

def jump_059_jump_frequency_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_059_jump_frequency_zscore_252d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _zscore_rolling(base, 252)

def jump_060_jump_frequency_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_060_jump_frequency_rank_252d
    ECONOMIC RATIONALE: Frequency of significant price discontinuities.
    """
    base = (close.diff(1).abs() > 2*close.rolling(252).std()).rolling(63).sum()
    return _rank_pct(base, 252)

def jump_061_jump_direction_bias_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_061_jump_direction_bias_lvl_5d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def jump_062_jump_direction_bias_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_062_jump_direction_bias_zscore_5d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def jump_063_jump_direction_bias_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_063_jump_direction_bias_rank_5d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rank_pct(base, 5)

def jump_064_jump_direction_bias_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_064_jump_direction_bias_lvl_21d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def jump_065_jump_direction_bias_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_065_jump_direction_bias_zscore_21d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def jump_066_jump_direction_bias_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_066_jump_direction_bias_rank_21d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rank_pct(base, 21)

def jump_067_jump_direction_bias_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_067_jump_direction_bias_lvl_63d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def jump_068_jump_direction_bias_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_068_jump_direction_bias_zscore_63d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def jump_069_jump_direction_bias_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_069_jump_direction_bias_rank_63d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rank_pct(base, 63)

def jump_070_jump_direction_bias_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_070_jump_direction_bias_lvl_126d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def jump_071_jump_direction_bias_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_071_jump_direction_bias_zscore_126d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def jump_072_jump_direction_bias_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_072_jump_direction_bias_rank_126d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rank_pct(base, 126)

def jump_073_jump_direction_bias_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_073_jump_direction_bias_lvl_252d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def jump_074_jump_direction_bias_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_074_jump_direction_bias_zscore_252d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def jump_075_jump_direction_bias_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_075_jump_direction_bias_rank_252d
    ECONOMIC RATIONALE: Predominance of jumps in one direction.
    """
    base = close.diff(1).rolling(21).sum() / close.diff(1).abs().rolling(21).sum().replace(0, 1e-9)
    return _rank_pct(base, 252)

def jump_076_jump_zscore_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_076_jump_zscore_lvl_5d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 5)

def jump_077_jump_zscore_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_077_jump_zscore_zscore_5d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 5)

def jump_078_jump_zscore_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_078_jump_zscore_rank_5d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 5)

def jump_079_jump_zscore_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_079_jump_zscore_lvl_21d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 21)

def jump_080_jump_zscore_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_080_jump_zscore_zscore_21d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 21)

def jump_081_jump_zscore_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_081_jump_zscore_rank_21d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 21)

def jump_082_jump_zscore_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_082_jump_zscore_lvl_63d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 63)

def jump_083_jump_zscore_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_083_jump_zscore_zscore_63d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 63)

def jump_084_jump_zscore_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_084_jump_zscore_rank_63d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 63)

def jump_085_jump_zscore_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_085_jump_zscore_lvl_126d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 126)

def jump_086_jump_zscore_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_086_jump_zscore_zscore_126d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 126)

def jump_087_jump_zscore_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_087_jump_zscore_rank_126d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 126)

def jump_088_jump_zscore_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_088_jump_zscore_lvl_252d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rolling_mean(base, 252)

def jump_089_jump_zscore_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_089_jump_zscore_zscore_252d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _zscore_rolling(base, 252)

def jump_090_jump_zscore_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_090_jump_zscore_rank_252d
    ECONOMIC RATIONALE: Statistical abnormality of current price jump.
    """
    base = _zscore_rolling(close.diff(1).abs(), 252)
    return _rank_pct(base, 252)

def jump_091_jump_reversal_rate_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_091_jump_reversal_rate_lvl_5d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rolling_mean(base, 5)

def jump_092_jump_reversal_rate_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_092_jump_reversal_rate_zscore_5d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _zscore_rolling(base, 5)

def jump_093_jump_reversal_rate_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_093_jump_reversal_rate_rank_5d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rank_pct(base, 5)

def jump_094_jump_reversal_rate_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_094_jump_reversal_rate_lvl_21d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rolling_mean(base, 21)

def jump_095_jump_reversal_rate_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_095_jump_reversal_rate_zscore_21d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _zscore_rolling(base, 21)

def jump_096_jump_reversal_rate_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_096_jump_reversal_rate_rank_21d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rank_pct(base, 21)

def jump_097_jump_reversal_rate_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_097_jump_reversal_rate_lvl_63d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rolling_mean(base, 63)

def jump_098_jump_reversal_rate_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_098_jump_reversal_rate_zscore_63d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _zscore_rolling(base, 63)

def jump_099_jump_reversal_rate_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_099_jump_reversal_rate_rank_63d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rank_pct(base, 63)

def jump_100_jump_reversal_rate_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_100_jump_reversal_rate_lvl_126d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rolling_mean(base, 126)

def jump_101_jump_reversal_rate_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_101_jump_reversal_rate_zscore_126d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _zscore_rolling(base, 126)

def jump_102_jump_reversal_rate_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_102_jump_reversal_rate_rank_126d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rank_pct(base, 126)

def jump_103_jump_reversal_rate_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_103_jump_reversal_rate_lvl_252d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rolling_mean(base, 252)

def jump_104_jump_reversal_rate_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_104_jump_reversal_rate_zscore_252d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _zscore_rolling(base, 252)

def jump_105_jump_reversal_rate_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_105_jump_reversal_rate_rank_252d
    ECONOMIC RATIONALE: Frequency of jump reversals.
    """
    base = close.diff(1).shift(1) * close.diff(1) < 0
    return _rank_pct(base, 252)

def jump_106_vol_adjusted_jump_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_106_vol_adjusted_jump_lvl_5d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def jump_107_vol_adjusted_jump_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_107_vol_adjusted_jump_zscore_5d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def jump_108_vol_adjusted_jump_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_108_vol_adjusted_jump_rank_5d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def jump_109_vol_adjusted_jump_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_109_vol_adjusted_jump_lvl_21d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def jump_110_vol_adjusted_jump_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_110_vol_adjusted_jump_zscore_21d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def jump_111_vol_adjusted_jump_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_111_vol_adjusted_jump_rank_21d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def jump_112_vol_adjusted_jump_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_112_vol_adjusted_jump_lvl_63d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def jump_113_vol_adjusted_jump_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_113_vol_adjusted_jump_zscore_63d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def jump_114_vol_adjusted_jump_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_114_vol_adjusted_jump_rank_63d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def jump_115_vol_adjusted_jump_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_115_vol_adjusted_jump_lvl_126d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def jump_116_vol_adjusted_jump_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_116_vol_adjusted_jump_zscore_126d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def jump_117_vol_adjusted_jump_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_117_vol_adjusted_jump_rank_126d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def jump_118_vol_adjusted_jump_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_118_vol_adjusted_jump_lvl_252d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def jump_119_vol_adjusted_jump_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_119_vol_adjusted_jump_zscore_252d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def jump_120_vol_adjusted_jump_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    jump_120_vol_adjusted_jump_rank_252d
    ECONOMIC RATIONALE: Jump magnitude relative to volume effort.
    """
    base = close.diff(1).abs() / (volume / volume.rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V111_REGISTRY_1 = {
    "jump_001_price_jump_magnitude_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_001_price_jump_magnitude_lvl_5d},
    "jump_002_price_jump_magnitude_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_002_price_jump_magnitude_zscore_5d},
    "jump_003_price_jump_magnitude_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_003_price_jump_magnitude_rank_5d},
    "jump_004_price_jump_magnitude_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_004_price_jump_magnitude_lvl_21d},
    "jump_005_price_jump_magnitude_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_005_price_jump_magnitude_zscore_21d},
    "jump_006_price_jump_magnitude_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_006_price_jump_magnitude_rank_21d},
    "jump_007_price_jump_magnitude_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_007_price_jump_magnitude_lvl_63d},
    "jump_008_price_jump_magnitude_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_008_price_jump_magnitude_zscore_63d},
    "jump_009_price_jump_magnitude_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_009_price_jump_magnitude_rank_63d},
    "jump_010_price_jump_magnitude_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_010_price_jump_magnitude_lvl_126d},
    "jump_011_price_jump_magnitude_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_011_price_jump_magnitude_zscore_126d},
    "jump_012_price_jump_magnitude_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_012_price_jump_magnitude_rank_126d},
    "jump_013_price_jump_magnitude_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_013_price_jump_magnitude_lvl_252d},
    "jump_014_price_jump_magnitude_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_014_price_jump_magnitude_zscore_252d},
    "jump_015_price_jump_magnitude_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_015_price_jump_magnitude_rank_252d},
    "jump_016_overnight_gap_jump_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_016_overnight_gap_jump_lvl_5d},
    "jump_017_overnight_gap_jump_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_017_overnight_gap_jump_zscore_5d},
    "jump_018_overnight_gap_jump_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_018_overnight_gap_jump_rank_5d},
    "jump_019_overnight_gap_jump_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_019_overnight_gap_jump_lvl_21d},
    "jump_020_overnight_gap_jump_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_020_overnight_gap_jump_zscore_21d},
    "jump_021_overnight_gap_jump_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_021_overnight_gap_jump_rank_21d},
    "jump_022_overnight_gap_jump_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_022_overnight_gap_jump_lvl_63d},
    "jump_023_overnight_gap_jump_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_023_overnight_gap_jump_zscore_63d},
    "jump_024_overnight_gap_jump_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_024_overnight_gap_jump_rank_63d},
    "jump_025_overnight_gap_jump_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_025_overnight_gap_jump_lvl_126d},
    "jump_026_overnight_gap_jump_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_026_overnight_gap_jump_zscore_126d},
    "jump_027_overnight_gap_jump_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_027_overnight_gap_jump_rank_126d},
    "jump_028_overnight_gap_jump_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_028_overnight_gap_jump_lvl_252d},
    "jump_029_overnight_gap_jump_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_029_overnight_gap_jump_zscore_252d},
    "jump_030_overnight_gap_jump_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_030_overnight_gap_jump_rank_252d},
    "jump_031_jump_volume_intensity_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_031_jump_volume_intensity_lvl_5d},
    "jump_032_jump_volume_intensity_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_032_jump_volume_intensity_zscore_5d},
    "jump_033_jump_volume_intensity_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_033_jump_volume_intensity_rank_5d},
    "jump_034_jump_volume_intensity_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_034_jump_volume_intensity_lvl_21d},
    "jump_035_jump_volume_intensity_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_035_jump_volume_intensity_zscore_21d},
    "jump_036_jump_volume_intensity_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_036_jump_volume_intensity_rank_21d},
    "jump_037_jump_volume_intensity_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_037_jump_volume_intensity_lvl_63d},
    "jump_038_jump_volume_intensity_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_038_jump_volume_intensity_zscore_63d},
    "jump_039_jump_volume_intensity_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_039_jump_volume_intensity_rank_63d},
    "jump_040_jump_volume_intensity_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_040_jump_volume_intensity_lvl_126d},
    "jump_041_jump_volume_intensity_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_041_jump_volume_intensity_zscore_126d},
    "jump_042_jump_volume_intensity_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_042_jump_volume_intensity_rank_126d},
    "jump_043_jump_volume_intensity_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_043_jump_volume_intensity_lvl_252d},
    "jump_044_jump_volume_intensity_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_044_jump_volume_intensity_zscore_252d},
    "jump_045_jump_volume_intensity_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_045_jump_volume_intensity_rank_252d},
    "jump_046_jump_frequency_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_046_jump_frequency_lvl_5d},
    "jump_047_jump_frequency_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_047_jump_frequency_zscore_5d},
    "jump_048_jump_frequency_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_048_jump_frequency_rank_5d},
    "jump_049_jump_frequency_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_049_jump_frequency_lvl_21d},
    "jump_050_jump_frequency_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_050_jump_frequency_zscore_21d},
    "jump_051_jump_frequency_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_051_jump_frequency_rank_21d},
    "jump_052_jump_frequency_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_052_jump_frequency_lvl_63d},
    "jump_053_jump_frequency_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_053_jump_frequency_zscore_63d},
    "jump_054_jump_frequency_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_054_jump_frequency_rank_63d},
    "jump_055_jump_frequency_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_055_jump_frequency_lvl_126d},
    "jump_056_jump_frequency_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_056_jump_frequency_zscore_126d},
    "jump_057_jump_frequency_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_057_jump_frequency_rank_126d},
    "jump_058_jump_frequency_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_058_jump_frequency_lvl_252d},
    "jump_059_jump_frequency_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_059_jump_frequency_zscore_252d},
    "jump_060_jump_frequency_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_060_jump_frequency_rank_252d},
    "jump_061_jump_direction_bias_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_061_jump_direction_bias_lvl_5d},
    "jump_062_jump_direction_bias_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_062_jump_direction_bias_zscore_5d},
    "jump_063_jump_direction_bias_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_063_jump_direction_bias_rank_5d},
    "jump_064_jump_direction_bias_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_064_jump_direction_bias_lvl_21d},
    "jump_065_jump_direction_bias_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_065_jump_direction_bias_zscore_21d},
    "jump_066_jump_direction_bias_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_066_jump_direction_bias_rank_21d},
    "jump_067_jump_direction_bias_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_067_jump_direction_bias_lvl_63d},
    "jump_068_jump_direction_bias_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_068_jump_direction_bias_zscore_63d},
    "jump_069_jump_direction_bias_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_069_jump_direction_bias_rank_63d},
    "jump_070_jump_direction_bias_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_070_jump_direction_bias_lvl_126d},
    "jump_071_jump_direction_bias_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_071_jump_direction_bias_zscore_126d},
    "jump_072_jump_direction_bias_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_072_jump_direction_bias_rank_126d},
    "jump_073_jump_direction_bias_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_073_jump_direction_bias_lvl_252d},
    "jump_074_jump_direction_bias_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_074_jump_direction_bias_zscore_252d},
    "jump_075_jump_direction_bias_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_075_jump_direction_bias_rank_252d},
    "jump_076_jump_zscore_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_076_jump_zscore_lvl_5d},
    "jump_077_jump_zscore_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_077_jump_zscore_zscore_5d},
    "jump_078_jump_zscore_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_078_jump_zscore_rank_5d},
    "jump_079_jump_zscore_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_079_jump_zscore_lvl_21d},
    "jump_080_jump_zscore_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_080_jump_zscore_zscore_21d},
    "jump_081_jump_zscore_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_081_jump_zscore_rank_21d},
    "jump_082_jump_zscore_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_082_jump_zscore_lvl_63d},
    "jump_083_jump_zscore_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_083_jump_zscore_zscore_63d},
    "jump_084_jump_zscore_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_084_jump_zscore_rank_63d},
    "jump_085_jump_zscore_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_085_jump_zscore_lvl_126d},
    "jump_086_jump_zscore_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_086_jump_zscore_zscore_126d},
    "jump_087_jump_zscore_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_087_jump_zscore_rank_126d},
    "jump_088_jump_zscore_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_088_jump_zscore_lvl_252d},
    "jump_089_jump_zscore_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_089_jump_zscore_zscore_252d},
    "jump_090_jump_zscore_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_090_jump_zscore_rank_252d},
    "jump_091_jump_reversal_rate_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_091_jump_reversal_rate_lvl_5d},
    "jump_092_jump_reversal_rate_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_092_jump_reversal_rate_zscore_5d},
    "jump_093_jump_reversal_rate_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_093_jump_reversal_rate_rank_5d},
    "jump_094_jump_reversal_rate_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_094_jump_reversal_rate_lvl_21d},
    "jump_095_jump_reversal_rate_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_095_jump_reversal_rate_zscore_21d},
    "jump_096_jump_reversal_rate_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_096_jump_reversal_rate_rank_21d},
    "jump_097_jump_reversal_rate_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_097_jump_reversal_rate_lvl_63d},
    "jump_098_jump_reversal_rate_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_098_jump_reversal_rate_zscore_63d},
    "jump_099_jump_reversal_rate_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_099_jump_reversal_rate_rank_63d},
    "jump_100_jump_reversal_rate_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_100_jump_reversal_rate_lvl_126d},
    "jump_101_jump_reversal_rate_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_101_jump_reversal_rate_zscore_126d},
    "jump_102_jump_reversal_rate_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_102_jump_reversal_rate_rank_126d},
    "jump_103_jump_reversal_rate_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_103_jump_reversal_rate_lvl_252d},
    "jump_104_jump_reversal_rate_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_104_jump_reversal_rate_zscore_252d},
    "jump_105_jump_reversal_rate_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_105_jump_reversal_rate_rank_252d},
    "jump_106_vol_adjusted_jump_lvl_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_106_vol_adjusted_jump_lvl_5d},
    "jump_107_vol_adjusted_jump_zscore_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_107_vol_adjusted_jump_zscore_5d},
    "jump_108_vol_adjusted_jump_rank_5d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_108_vol_adjusted_jump_rank_5d},
    "jump_109_vol_adjusted_jump_lvl_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_109_vol_adjusted_jump_lvl_21d},
    "jump_110_vol_adjusted_jump_zscore_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_110_vol_adjusted_jump_zscore_21d},
    "jump_111_vol_adjusted_jump_rank_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_111_vol_adjusted_jump_rank_21d},
    "jump_112_vol_adjusted_jump_lvl_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_112_vol_adjusted_jump_lvl_63d},
    "jump_113_vol_adjusted_jump_zscore_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_113_vol_adjusted_jump_zscore_63d},
    "jump_114_vol_adjusted_jump_rank_63d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_114_vol_adjusted_jump_rank_63d},
    "jump_115_vol_adjusted_jump_lvl_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_115_vol_adjusted_jump_lvl_126d},
    "jump_116_vol_adjusted_jump_zscore_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_116_vol_adjusted_jump_zscore_126d},
    "jump_117_vol_adjusted_jump_rank_126d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_117_vol_adjusted_jump_rank_126d},
    "jump_118_vol_adjusted_jump_lvl_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_118_vol_adjusted_jump_lvl_252d},
    "jump_119_vol_adjusted_jump_zscore_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_119_vol_adjusted_jump_zscore_252d},
    "jump_120_vol_adjusted_jump_rank_252d": {"inputs": ["close", "high", "low", "open", "volume"], "func": jump_120_vol_adjusted_jump_rank_252d},
}
