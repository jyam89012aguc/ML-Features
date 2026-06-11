"""
111_111_jump_discontinuity — Base Features 001-075
Domain: 111_jump_discontinuity
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

def jump_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_mean(base, 5)

def jump_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_mean(base, 21)

def jump_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_mean(base, 63)

def jump_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_mean(base, 126)

def jump_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_mean(base, 252)

def jump_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 5)

def jump_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 21)

def jump_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 63)

def jump_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 126)

def jump_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 252)

def jump_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 5)

def jump_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 21)

def jump_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 63)

def jump_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 126)

def jump_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 252)

def jump_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 5)

def jump_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 21)

def jump_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 63)

def jump_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 126)

def jump_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 252)

def jump_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 5)

def jump_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 21)

def jump_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 63)

def jump_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 126)

def jump_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 252)

def jump_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def jump_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def jump_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def jump_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def jump_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def jump_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def jump_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def jump_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def jump_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def jump_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def jump_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 5d horizon to identify extreme regimes.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def jump_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 21d horizon to identify extreme regimes.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def jump_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 63d horizon to identify extreme regimes.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def jump_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 126d horizon to identify extreme regimes.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def jump_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 252d horizon to identify extreme regimes.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def jump_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 5d mean.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def jump_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 21d mean.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def jump_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 63d mean.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def jump_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 126d mean.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def jump_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 252d mean.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def jump_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def jump_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def jump_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def jump_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def jump_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def jump_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def jump_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def jump_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def jump_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def jump_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def jump_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 5d to capture explosive breakdown or reversal points.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def jump_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 21d to capture explosive breakdown or reversal points.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def jump_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 63d to capture explosive breakdown or reversal points.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def jump_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 126d to capture explosive breakdown or reversal points.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def jump_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 252d to capture explosive breakdown or reversal points.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def jump_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def jump_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def jump_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def jump_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def jump_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def jump_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def jump_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def jump_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def jump_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def jump_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close - open).abs() / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def jump_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).max()
    return _rolling_mean(base, 5)

def jump_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).max()
    return _rolling_mean(base, 21)

def jump_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).max()
    return _rolling_mean(base, 63)

def jump_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).max()
    return _rolling_mean(base, 126)

def jump_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).max()
    return _rolling_mean(base, 252)
