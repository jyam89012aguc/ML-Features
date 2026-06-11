"""
10_10_trough_clustering — Base Features 001-075
Domain: 10_trough_clustering
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

def tcl_001_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 5)

def tcl_002_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 21)

def tcl_003_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 63)

def tcl_004_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 126)

def tcl_005_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 252)

def tcl_006_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 5)

def tcl_007_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 21)

def tcl_008_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 63)

def tcl_009_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 126)

def tcl_010_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 252)

def tcl_011_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 5)

def tcl_012_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 21)

def tcl_013_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 63)

def tcl_014_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 126)

def tcl_015_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 252)

def tcl_016_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 5)

def tcl_017_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 21)

def tcl_018_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 63)

def tcl_019_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 126)

def tcl_020_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 252)

def tcl_021_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 5)

def tcl_022_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 21)

def tcl_023_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 63)

def tcl_024_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 126)

def tcl_025_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 252)

def tcl_026_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 5))

def tcl_027_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 21))

def tcl_028_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 63))

def tcl_029_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 126))

def tcl_030_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 252))

def tcl_031_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tcl_032_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tcl_033_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tcl_034_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tcl_035_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tcl_036_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 5d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 5)

def tcl_037_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 21d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 21)

def tcl_038_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 63d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 63)

def tcl_039_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 126d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 126)

def tcl_040_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 252d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 252)

def tcl_041_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 5d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 5)

def tcl_042_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 21d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 21)

def tcl_043_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 63d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 63)

def tcl_044_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 126d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 126)

def tcl_045_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 10 trough clustering by measuring deviations from the 252d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 252)

def tcl_046_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 5)

def tcl_047_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 21)

def tcl_048_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 63)

def tcl_049_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 126)

def tcl_050_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 10 trough clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 252)

def tcl_051_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 5)

def tcl_052_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 21)

def tcl_053_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 63)

def tcl_054_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 126)

def tcl_055_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 10 trough clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 252)

def tcl_056_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 5)

def tcl_057_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 21)

def tcl_058_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 63)

def tcl_059_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 126)

def tcl_060_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 10 trough clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 252)

def tcl_061_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 5))

def tcl_062_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 21))

def tcl_063_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 63))

def tcl_064_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 126))

def tcl_065_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 10 trough clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 252))

def tcl_066_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tcl_067_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tcl_068_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tcl_069_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tcl_070_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 10 trough clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tcl_071_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 5d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def tcl_072_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 21d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def tcl_073_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 63d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def tcl_074_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 126d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def tcl_075_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 10 trough clustering over a 252d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)
