"""
49_49_reversal_patterns — Base Features 001-075
Domain: 49_reversal_patterns
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).skew().fillna(0)

def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).kurt().fillna(0)

# ── Feature functions ────────────────────────────────────────────────────────

def revp_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 5d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def revp_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 21d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def revp_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 63d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def revp_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 126d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def revp_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 252d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def revp_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 5d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def revp_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 21d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def revp_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 63d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def revp_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 126d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def revp_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 252d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def revp_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 5)

def revp_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 21)

def revp_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 63)

def revp_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 126)

def revp_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 252)

def revp_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def revp_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def revp_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def revp_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def revp_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def revp_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 5d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def revp_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 21d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def revp_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 63d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def revp_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 126d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def revp_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 252d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def revp_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def revp_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def revp_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def revp_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def revp_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def revp_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def revp_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def revp_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def revp_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def revp_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def revp_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 5d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def revp_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 21d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def revp_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 63d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def revp_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 126d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def revp_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 252d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def revp_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 5d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def revp_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 21d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def revp_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 63d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def revp_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 126d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def revp_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 252d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def revp_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def revp_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def revp_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def revp_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def revp_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def revp_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def revp_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def revp_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def revp_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def revp_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def revp_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 5d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def revp_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 21d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def revp_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 63d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def revp_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 126d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def revp_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 252d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def revp_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def revp_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def revp_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def revp_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def revp_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def revp_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def revp_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def revp_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def revp_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def revp_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def revp_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 5d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def revp_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 21d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def revp_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 63d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def revp_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 126d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def revp_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 252d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)
