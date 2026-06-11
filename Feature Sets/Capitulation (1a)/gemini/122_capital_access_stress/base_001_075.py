"""
122_122_capital_access_stress — Base Features 001-075
Domain: 122_capital_access_stress
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

def cast_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_mean(base, 5)

def cast_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_mean(base, 21)

def cast_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_mean(base, 63)

def cast_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_mean(base, 126)

def cast_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_mean(base, 252)

def cast_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _zscore_rolling(base, 5)

def cast_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _zscore_rolling(base, 21)

def cast_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _zscore_rolling(base, 63)

def cast_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _zscore_rolling(base, 126)

def cast_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _zscore_rolling(base, 252)

def cast_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rank_pct(base, 5)

def cast_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rank_pct(base, 21)

def cast_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rank_pct(base, 63)

def cast_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rank_pct(base, 126)

def cast_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rank_pct(base, 252)

def cast_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_skew(base, 5)

def cast_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_skew(base, 21)

def cast_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_skew(base, 63)

def cast_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_skew(base, 126)

def cast_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_skew(base, 252)

def cast_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_kurt(base, 5)

def cast_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_kurt(base, 21)

def cast_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_kurt(base, 63)

def cast_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_kurt(base, 126)

def cast_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _rolling_kurt(base, 252)

def cast_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std() * volume.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_mean(base, 5)

def cast_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_mean(base, 21)

def cast_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_mean(base, 63)

def cast_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_mean(base, 126)

def cast_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_mean(base, 252)

def cast_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _zscore_rolling(base, 5)

def cast_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _zscore_rolling(base, 21)

def cast_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _zscore_rolling(base, 63)

def cast_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _zscore_rolling(base, 126)

def cast_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _zscore_rolling(base, 252)

def cast_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rank_pct(base, 5)

def cast_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rank_pct(base, 21)

def cast_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rank_pct(base, 63)

def cast_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rank_pct(base, 126)

def cast_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rank_pct(base, 252)

def cast_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_skew(base, 5)

def cast_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_skew(base, 21)

def cast_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_skew(base, 63)

def cast_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_skew(base, 126)

def cast_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_skew(base, 252)

def cast_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_kurt(base, 5)

def cast_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_kurt(base, 21)

def cast_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_kurt(base, 63)

def cast_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_kurt(base, 126)

def cast_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _rolling_kurt(base, 252)

def cast_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _safe_div(base, _rolling_std(base, 5))

def cast_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _safe_div(base, _rolling_std(base, 21))

def cast_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _safe_div(base, _rolling_std(base, 63))

def cast_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _safe_div(base, _rolling_std(base, 126))

def cast_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return _safe_div(base, _rolling_std(base, 252))

def cast_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(close.pct_change().rolling(21).std(), volume.rolling(21).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_mean(base, 5)

def cast_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_mean(base, 21)

def cast_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_mean(base, 63)

def cast_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_mean(base, 126)

def cast_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_mean(base, 252)
