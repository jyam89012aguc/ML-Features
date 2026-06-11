"""
107_107_change_point_detection — Base Features 001-075
Domain: 107_change_point_detection
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

def cpdt_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_mean(base, 5)

def cpdt_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_mean(base, 21)

def cpdt_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_mean(base, 63)

def cpdt_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_mean(base, 126)

def cpdt_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_mean(base, 252)

def cpdt_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rank_pct(base, 5)

def cpdt_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rank_pct(base, 21)

def cpdt_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rank_pct(base, 63)

def cpdt_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rank_pct(base, 126)

def cpdt_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rank_pct(base, 252)

def cpdt_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_skew(base, 5)

def cpdt_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_skew(base, 21)

def cpdt_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_skew(base, 63)

def cpdt_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_skew(base, 126)

def cpdt_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_skew(base, 252)

def cpdt_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_mean(base, 5)

def cpdt_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_mean(base, 21)

def cpdt_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_mean(base, 63)

def cpdt_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_mean(base, 126)

def cpdt_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_mean(base, 252)

def cpdt_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.rolling(21).mean().diff().diff()
    return _zscore_rolling(base, 5)

def cpdt_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.rolling(21).mean().diff().diff()
    return _zscore_rolling(base, 21)

def cpdt_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.rolling(21).mean().diff().diff()
    return _zscore_rolling(base, 63)

def cpdt_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.rolling(21).mean().diff().diff()
    return _zscore_rolling(base, 126)

def cpdt_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.rolling(21).mean().diff().diff()
    return _zscore_rolling(base, 252)

def cpdt_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rank_pct(base, 5)

def cpdt_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rank_pct(base, 21)

def cpdt_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rank_pct(base, 63)

def cpdt_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rank_pct(base, 126)

def cpdt_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rank_pct(base, 252)

def cpdt_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_skew(base, 5)

def cpdt_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_skew(base, 21)

def cpdt_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_skew(base, 63)

def cpdt_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_skew(base, 126)

def cpdt_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_skew(base, 252)

def cpdt_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_kurt(base, 5)

def cpdt_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_kurt(base, 21)

def cpdt_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_kurt(base, 63)

def cpdt_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_kurt(base, 126)

def cpdt_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(21).mean().diff().diff()
    return _rolling_kurt(base, 252)

def cpdt_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(21).mean().diff().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(21).mean().diff().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(21).mean().diff().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(21).mean().diff().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(21).mean().diff().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(21).mean().diff().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(21).mean().diff().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(21).mean().diff().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(21).mean().diff().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(21).mean().diff().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).mean().diff()
    return _rolling_mean(base, 5)

def cpdt_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).mean().diff()
    return _rolling_mean(base, 21)

def cpdt_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).mean().diff()
    return _rolling_mean(base, 63)

def cpdt_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).mean().diff()
    return _rolling_mean(base, 126)

def cpdt_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).mean().diff()
    return _rolling_mean(base, 252)
