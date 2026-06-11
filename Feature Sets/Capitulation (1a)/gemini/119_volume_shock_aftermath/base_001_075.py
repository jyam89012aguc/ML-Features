"""
119_119_volume_shock_aftermath — Base Features 001-075
Domain: 119_volume_shock_aftermath
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

def vsha_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_mean(base, 5)

def vsha_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_mean(base, 21)

def vsha_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_mean(base, 63)

def vsha_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_mean(base, 126)

def vsha_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_mean(base, 252)

def vsha_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 21)
    return _zscore_rolling(base, 5)

def vsha_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 21)
    return _zscore_rolling(base, 21)

def vsha_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 21)
    return _zscore_rolling(base, 63)

def vsha_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 21)
    return _zscore_rolling(base, 126)

def vsha_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 21)
    return _zscore_rolling(base, 252)

def vsha_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rank_pct(base, 5)

def vsha_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rank_pct(base, 21)

def vsha_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rank_pct(base, 63)

def vsha_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rank_pct(base, 126)

def vsha_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rank_pct(base, 252)

def vsha_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_skew(base, 5)

def vsha_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_skew(base, 21)

def vsha_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_skew(base, 63)

def vsha_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_skew(base, 126)

def vsha_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_skew(base, 252)

def vsha_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_kurt(base, 5)

def vsha_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_kurt(base, 21)

def vsha_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_kurt(base, 63)

def vsha_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_kurt(base, 126)

def vsha_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 21)
    return _rolling_kurt(base, 252)

def vsha_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 21)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 21)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 21)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 21)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 21)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 21)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 21)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 21)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 21)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 21)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_mean(base, 5)

def vsha_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_mean(base, 21)

def vsha_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_mean(base, 63)

def vsha_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_mean(base, 126)

def vsha_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_mean(base, 252)

def vsha_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _zscore_rolling(base, 5)

def vsha_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _zscore_rolling(base, 21)

def vsha_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _zscore_rolling(base, 63)

def vsha_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _zscore_rolling(base, 126)

def vsha_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _zscore_rolling(base, 252)

def vsha_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rank_pct(base, 5)

def vsha_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rank_pct(base, 21)

def vsha_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rank_pct(base, 63)

def vsha_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rank_pct(base, 126)

def vsha_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rank_pct(base, 252)

def vsha_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_skew(base, 5)

def vsha_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_skew(base, 21)

def vsha_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_skew(base, 63)

def vsha_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_skew(base, 126)

def vsha_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_skew(base, 252)

def vsha_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_kurt(base, 5)

def vsha_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_kurt(base, 21)

def vsha_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_kurt(base, 63)

def vsha_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_kurt(base, 126)

def vsha_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _rolling_kurt(base, 252)

def vsha_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume / _rolling_mean(volume, 21)).diff(5)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)) * close.pct_change()
    return _rolling_mean(base, 5)

def vsha_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)) * close.pct_change()
    return _rolling_mean(base, 21)

def vsha_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)) * close.pct_change()
    return _rolling_mean(base, 63)

def vsha_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)) * close.pct_change()
    return _rolling_mean(base, 126)

def vsha_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = (volume / _rolling_mean(volume, 21)) * close.pct_change()
    return _rolling_mean(base, 252)
