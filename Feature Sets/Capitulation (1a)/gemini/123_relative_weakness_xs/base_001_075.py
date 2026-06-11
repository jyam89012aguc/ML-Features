"""
123_123_relative_weakness_xs — Base Features 001-075
Domain: 123_relative_weakness_xs
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

def rwxs_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_mean(base, 5)

def rwxs_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_mean(base, 21)

def rwxs_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_mean(base, 63)

def rwxs_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_mean(base, 126)

def rwxs_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_mean(base, 252)

def rwxs_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 252)
    return _zscore_rolling(base, 5)

def rwxs_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 252)
    return _zscore_rolling(base, 21)

def rwxs_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 252)
    return _zscore_rolling(base, 63)

def rwxs_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 252)
    return _zscore_rolling(base, 126)

def rwxs_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 252)
    return _zscore_rolling(base, 252)

def rwxs_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 252)
    return _rank_pct(base, 5)

def rwxs_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 252)
    return _rank_pct(base, 21)

def rwxs_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 252)
    return _rank_pct(base, 63)

def rwxs_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 252)
    return _rank_pct(base, 126)

def rwxs_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 252)
    return _rank_pct(base, 252)

def rwxs_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_skew(base, 5)

def rwxs_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_skew(base, 21)

def rwxs_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_skew(base, 63)

def rwxs_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_skew(base, 126)

def rwxs_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_skew(base, 252)

def rwxs_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_kurt(base, 5)

def rwxs_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_kurt(base, 21)

def rwxs_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_kurt(base, 63)

def rwxs_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_kurt(base, 126)

def rwxs_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 252)
    return _rolling_kurt(base, 252)

def rwxs_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 252)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 252)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 252)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 252)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 252)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 5)

def rwxs_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 21)

def rwxs_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 63)

def rwxs_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 126)

def rwxs_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(63)
    return _rolling_mean(base, 252)

def rwxs_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 5)

def rwxs_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 21)

def rwxs_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 63)

def rwxs_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 126)

def rwxs_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(63)
    return _zscore_rolling(base, 252)

def rwxs_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 5)

def rwxs_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 21)

def rwxs_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 63)

def rwxs_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 126)

def rwxs_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(63)
    return _rank_pct(base, 252)

def rwxs_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(63)
    return _rolling_skew(base, 5)

def rwxs_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(63)
    return _rolling_skew(base, 21)

def rwxs_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(63)
    return _rolling_skew(base, 63)

def rwxs_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(63)
    return _rolling_skew(base, 126)

def rwxs_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(63)
    return _rolling_skew(base, 252)

def rwxs_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(63)
    return _rolling_kurt(base, 5)

def rwxs_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(63)
    return _rolling_kurt(base, 21)

def rwxs_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(63)
    return _rolling_kurt(base, 63)

def rwxs_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(63)
    return _rolling_kurt(base, 126)

def rwxs_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(63)
    return _rolling_kurt(base, 252)

def rwxs_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(63)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(63)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(63)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(63)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(63)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(63)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(63)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(63)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(63)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(63)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_mean(base, 5)

def rwxs_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_mean(base, 21)

def rwxs_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_mean(base, 63)

def rwxs_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_mean(base, 126)

def rwxs_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_mean(base, 252)
