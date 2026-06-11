"""
124_124_cross_sectional_distress_rank — Base Features 001-075
Domain: 124_cross_sectional_distress_rank
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

def csdr_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_mean(base, 5)

def csdr_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_mean(base, 21)

def csdr_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_mean(base, 63)

def csdr_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_mean(base, 126)

def csdr_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_mean(base, 252)

def csdr_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _zscore_rolling(base, 5)

def csdr_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _zscore_rolling(base, 21)

def csdr_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _zscore_rolling(base, 63)

def csdr_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _zscore_rolling(base, 126)

def csdr_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _zscore_rolling(base, 252)

def csdr_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rank_pct(base, 5)

def csdr_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rank_pct(base, 21)

def csdr_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rank_pct(base, 63)

def csdr_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rank_pct(base, 126)

def csdr_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rank_pct(base, 252)

def csdr_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_skew(base, 5)

def csdr_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_skew(base, 21)

def csdr_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_skew(base, 63)

def csdr_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_skew(base, 126)

def csdr_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_skew(base, 252)

def csdr_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_kurt(base, 5)

def csdr_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_kurt(base, 21)

def csdr_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_kurt(base, 63)

def csdr_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_kurt(base, 126)

def csdr_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _rolling_kurt(base, 252)

def csdr_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(21), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_mean(base, 5)

def csdr_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_mean(base, 21)

def csdr_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_mean(base, 63)

def csdr_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_mean(base, 126)

def csdr_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_mean(base, 252)

def csdr_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _zscore_rolling(base, 5)

def csdr_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _zscore_rolling(base, 21)

def csdr_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _zscore_rolling(base, 63)

def csdr_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _zscore_rolling(base, 126)

def csdr_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _zscore_rolling(base, 252)

def csdr_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rank_pct(base, 5)

def csdr_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rank_pct(base, 21)

def csdr_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rank_pct(base, 63)

def csdr_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rank_pct(base, 126)

def csdr_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rank_pct(base, 252)

def csdr_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_skew(base, 5)

def csdr_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_skew(base, 21)

def csdr_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_skew(base, 63)

def csdr_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_skew(base, 126)

def csdr_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_skew(base, 252)

def csdr_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_kurt(base, 5)

def csdr_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_kurt(base, 21)

def csdr_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_kurt(base, 63)

def csdr_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_kurt(base, 126)

def csdr_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _rolling_kurt(base, 252)

def csdr_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(63), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_mean(base, 5)

def csdr_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_mean(base, 21)

def csdr_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_mean(base, 63)

def csdr_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_mean(base, 126)

def csdr_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_mean(base, 252)
