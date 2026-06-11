"""
01_01_drawdown_depth — Base Features 001-075
Domain: 01_drawdown_depth
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

def dd_001_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 5)

def dd_002_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 21)

def dd_003_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 63)

def dd_004_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 126)

def dd_005_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_mean(base, 252)

def dd_006_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 5)

def dd_007_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 21)

def dd_008_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 63)

def dd_009_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 126)

def dd_010_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _zscore_rolling(base, 252)

def dd_011_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 5)

def dd_012_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 21)

def dd_013_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 63)

def dd_014_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 126)

def dd_015_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rank_pct(base, 252)

def dd_016_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 5)

def dd_017_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 21)

def dd_018_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 63)

def dd_019_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 126)

def dd_020_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_skew(base, 252)

def dd_021_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 5)

def dd_022_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 21)

def dd_023_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 63)

def dd_024_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 126)

def dd_025_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _rolling_kurt(base, 252)

def dd_026_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 5))

def dd_027_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 21))

def dd_028_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 63))

def dd_029_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 126))

def dd_030_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return _safe_div(base, _rolling_std(base, 252))

def dd_031_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dd_032_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dd_033_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dd_034_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dd_035_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dd_036_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 5)

def dd_037_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 21)

def dd_038_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 63)

def dd_039_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 126)

def dd_040_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_mean(base, 252)

def dd_041_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 5d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 5)

def dd_042_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 21d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 21)

def dd_043_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 63d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 63)

def dd_044_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 126d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 126)

def dd_045_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 252d mean.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _zscore_rolling(base, 252)

def dd_046_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 5)

def dd_047_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 21)

def dd_048_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 63)

def dd_049_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 126)

def dd_050_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rank_pct(base, 252)

def dd_051_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 5)

def dd_052_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 21)

def dd_053_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 63)

def dd_054_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 126)

def dd_055_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_skew(base, 252)

def dd_056_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 5)

def dd_057_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 21)

def dd_058_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 63)

def dd_059_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 126)

def dd_060_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _rolling_kurt(base, 252)

def dd_061_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 5))

def dd_062_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 21))

def dd_063_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 63))

def dd_064_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 126))

def dd_065_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return _safe_div(base, _rolling_std(base, 252))

def dd_066_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dd_067_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dd_068_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dd_069_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dd_070_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dd_071_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dd_072_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dd_073_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dd_074_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dd_075_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)
