"""
117_117_price_clustering_psychology — Base Features 001-075
Domain: 117_price_clustering_psychology
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

def ppsy_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = close % 1
    return _rolling_mean(base, 5)

def ppsy_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = close % 1
    return _rolling_mean(base, 21)

def ppsy_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = close % 1
    return _rolling_mean(base, 63)

def ppsy_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = close % 1
    return _rolling_mean(base, 126)

def ppsy_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = close % 1
    return _rolling_mean(base, 252)

def ppsy_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 5d mean.
    """
    base = close % 1
    return _zscore_rolling(base, 5)

def ppsy_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 21d mean.
    """
    base = close % 1
    return _zscore_rolling(base, 21)

def ppsy_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 63d mean.
    """
    base = close % 1
    return _zscore_rolling(base, 63)

def ppsy_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 126d mean.
    """
    base = close % 1
    return _zscore_rolling(base, 126)

def ppsy_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 252d mean.
    """
    base = close % 1
    return _zscore_rolling(base, 252)

def ppsy_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close % 1
    return _rank_pct(base, 5)

def ppsy_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close % 1
    return _rank_pct(base, 21)

def ppsy_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close % 1
    return _rank_pct(base, 63)

def ppsy_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close % 1
    return _rank_pct(base, 126)

def ppsy_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close % 1
    return _rank_pct(base, 252)

def ppsy_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 5d to detect tail risk or exhaustion.
    """
    base = close % 1
    return _rolling_skew(base, 5)

def ppsy_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 21d to detect tail risk or exhaustion.
    """
    base = close % 1
    return _rolling_skew(base, 21)

def ppsy_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 63d to detect tail risk or exhaustion.
    """
    base = close % 1
    return _rolling_skew(base, 63)

def ppsy_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 126d to detect tail risk or exhaustion.
    """
    base = close % 1
    return _rolling_skew(base, 126)

def ppsy_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 252d to detect tail risk or exhaustion.
    """
    base = close % 1
    return _rolling_skew(base, 252)

def ppsy_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = close % 1
    return _rolling_kurt(base, 5)

def ppsy_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = close % 1
    return _rolling_kurt(base, 21)

def ppsy_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = close % 1
    return _rolling_kurt(base, 63)

def ppsy_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = close % 1
    return _rolling_kurt(base, 126)

def ppsy_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = close % 1
    return _rolling_kurt(base, 252)

def ppsy_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close % 1
    return _safe_div(base, _rolling_std(base, 5))

def ppsy_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close % 1
    return _safe_div(base, _rolling_std(base, 21))

def ppsy_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close % 1
    return _safe_div(base, _rolling_std(base, 63))

def ppsy_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close % 1
    return _safe_div(base, _rolling_std(base, 126))

def ppsy_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close % 1
    return _safe_div(base, _rolling_std(base, 252))

def ppsy_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = close % 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = close % 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = close % 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = close % 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = close % 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ppsy_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = close % 10
    return _rolling_mean(base, 5)

def ppsy_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = close % 10
    return _rolling_mean(base, 21)

def ppsy_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = close % 10
    return _rolling_mean(base, 63)

def ppsy_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = close % 10
    return _rolling_mean(base, 126)

def ppsy_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = close % 10
    return _rolling_mean(base, 252)

def ppsy_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 5d mean.
    """
    base = close % 10
    return _zscore_rolling(base, 5)

def ppsy_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 21d mean.
    """
    base = close % 10
    return _zscore_rolling(base, 21)

def ppsy_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 63d mean.
    """
    base = close % 10
    return _zscore_rolling(base, 63)

def ppsy_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 126d mean.
    """
    base = close % 10
    return _zscore_rolling(base, 126)

def ppsy_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 252d mean.
    """
    base = close % 10
    return _zscore_rolling(base, 252)

def ppsy_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close % 10
    return _rank_pct(base, 5)

def ppsy_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close % 10
    return _rank_pct(base, 21)

def ppsy_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close % 10
    return _rank_pct(base, 63)

def ppsy_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close % 10
    return _rank_pct(base, 126)

def ppsy_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close % 10
    return _rank_pct(base, 252)

def ppsy_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 5d to detect tail risk or exhaustion.
    """
    base = close % 10
    return _rolling_skew(base, 5)

def ppsy_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 21d to detect tail risk or exhaustion.
    """
    base = close % 10
    return _rolling_skew(base, 21)

def ppsy_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 63d to detect tail risk or exhaustion.
    """
    base = close % 10
    return _rolling_skew(base, 63)

def ppsy_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 126d to detect tail risk or exhaustion.
    """
    base = close % 10
    return _rolling_skew(base, 126)

def ppsy_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 252d to detect tail risk or exhaustion.
    """
    base = close % 10
    return _rolling_skew(base, 252)

def ppsy_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = close % 10
    return _rolling_kurt(base, 5)

def ppsy_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = close % 10
    return _rolling_kurt(base, 21)

def ppsy_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = close % 10
    return _rolling_kurt(base, 63)

def ppsy_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = close % 10
    return _rolling_kurt(base, 126)

def ppsy_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = close % 10
    return _rolling_kurt(base, 252)

def ppsy_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close % 10
    return _safe_div(base, _rolling_std(base, 5))

def ppsy_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close % 10
    return _safe_div(base, _rolling_std(base, 21))

def ppsy_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close % 10
    return _safe_div(base, _rolling_std(base, 63))

def ppsy_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close % 10
    return _safe_div(base, _rolling_std(base, 126))

def ppsy_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close % 10
    return _safe_div(base, _rolling_std(base, 252))

def ppsy_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = close % 10
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = close % 10
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = close % 10
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = close % 10
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = close % 10
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ppsy_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.round())
    return _rolling_mean(base, 5)

def ppsy_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.round())
    return _rolling_mean(base, 21)

def ppsy_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.round())
    return _rolling_mean(base, 63)

def ppsy_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.round())
    return _rolling_mean(base, 126)

def ppsy_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.round())
    return _rolling_mean(base, 252)
