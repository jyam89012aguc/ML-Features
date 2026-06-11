"""
42_42_volatility_of_volatility — Base Features 001-075
Domain: 42_volatility_of_volatility
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

def vov_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 5d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def vov_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 21d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def vov_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 63d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def vov_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 126d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def vov_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 252d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def vov_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 5d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def vov_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 21d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def vov_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 63d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def vov_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 126d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def vov_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 252d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def vov_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 5)

def vov_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 21)

def vov_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 63)

def vov_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 126)

def vov_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 252)

def vov_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def vov_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def vov_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def vov_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def vov_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def vov_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def vov_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def vov_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def vov_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def vov_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def vov_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def vov_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def vov_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def vov_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def vov_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def vov_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vov_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vov_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vov_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vov_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vov_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 5)

def vov_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 21)

def vov_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 63)

def vov_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 126)

def vov_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 252)

def vov_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 5)

def vov_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 21)

def vov_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 63)

def vov_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 126)

def vov_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 252)

def vov_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 5)

def vov_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 21)

def vov_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 63)

def vov_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 126)

def vov_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 252)

def vov_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 5)

def vov_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 21)

def vov_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 63)

def vov_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 126)

def vov_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 252)

def vov_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 5)

def vov_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 21)

def vov_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 63)

def vov_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 126)

def vov_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 252)

def vov_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def vov_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def vov_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def vov_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def vov_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def vov_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vov_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vov_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vov_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vov_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vov_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 5d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 5)

def vov_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 21d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 21)

def vov_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 63d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 63)

def vov_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 126d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 126)

def vov_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 252d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 252)
