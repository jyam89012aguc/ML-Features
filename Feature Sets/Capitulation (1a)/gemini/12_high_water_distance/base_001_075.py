"""
12_12_high_water_distance — Base Features 001-075
Domain: 12_high_water_distance
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

def hwd_001_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 5)

def hwd_002_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 21)

def hwd_003_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 63)

def hwd_004_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 126)

def hwd_005_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 252)

def hwd_006_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 5)

def hwd_007_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 21)

def hwd_008_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 63)

def hwd_009_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 126)

def hwd_010_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 252)

def hwd_011_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 5)

def hwd_012_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 21)

def hwd_013_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 63)

def hwd_014_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 126)

def hwd_015_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 252)

def hwd_016_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 5)

def hwd_017_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 21)

def hwd_018_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 63)

def hwd_019_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 126)

def hwd_020_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 252)

def hwd_021_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 5)

def hwd_022_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 21)

def hwd_023_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 63)

def hwd_024_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 126)

def hwd_025_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 252)

def hwd_026_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 5))

def hwd_027_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 21))

def hwd_028_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 63))

def hwd_029_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 126))

def hwd_030_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 252))

def hwd_031_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hwd_032_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hwd_033_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hwd_034_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hwd_035_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hwd_036_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 5d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 5)

def hwd_037_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 21d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 21)

def hwd_038_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 63d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 63)

def hwd_039_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 126d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 126)

def hwd_040_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 252d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 252)

def hwd_041_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 5d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 5)

def hwd_042_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 21d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 21)

def hwd_043_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 63d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 63)

def hwd_044_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 126d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 126)

def hwd_045_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 12 high water distance by measuring deviations from the 252d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 252)

def hwd_046_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 5)

def hwd_047_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 21)

def hwd_048_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 63)

def hwd_049_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 126)

def hwd_050_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 12 high water distance to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 252)

def hwd_051_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 5)

def hwd_052_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 21)

def hwd_053_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 63)

def hwd_054_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 126)

def hwd_055_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 12 high water distance distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 252)

def hwd_056_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 5)

def hwd_057_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 21)

def hwd_058_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 63)

def hwd_059_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 126)

def hwd_060_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 12 high water distance over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 252)

def hwd_061_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 5))

def hwd_062_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 21))

def hwd_063_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 63))

def hwd_064_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 126))

def hwd_065_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 12 high water distance for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 252))

def hwd_066_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hwd_067_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hwd_068_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hwd_069_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hwd_070_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 12 high water distance over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hwd_071_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 5d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def hwd_072_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 21d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def hwd_073_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 63d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def hwd_074_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 126d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def hwd_075_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 12 high water distance over a 252d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)
