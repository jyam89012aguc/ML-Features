"""
120_120_information_decay — Base Features 001-075
Domain: 120_information_decay
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

def idec_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_mean(base, 5)

def idec_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_mean(base, 21)

def idec_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_mean(base, 63)

def idec_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_mean(base, 126)

def idec_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_mean(base, 252)

def idec_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _zscore_rolling(base, 5)

def idec_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _zscore_rolling(base, 21)

def idec_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _zscore_rolling(base, 63)

def idec_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _zscore_rolling(base, 126)

def idec_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _zscore_rolling(base, 252)

def idec_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rank_pct(base, 5)

def idec_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rank_pct(base, 21)

def idec_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rank_pct(base, 63)

def idec_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rank_pct(base, 126)

def idec_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rank_pct(base, 252)

def idec_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_skew(base, 5)

def idec_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_skew(base, 21)

def idec_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_skew(base, 63)

def idec_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_skew(base, 126)

def idec_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_skew(base, 252)

def idec_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_kurt(base, 5)

def idec_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_kurt(base, 21)

def idec_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_kurt(base, 63)

def idec_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_kurt(base, 126)

def idec_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _rolling_kurt(base, 252)

def idec_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 5))

def idec_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 21))

def idec_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 63))

def idec_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 126))

def idec_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 252))

def idec_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(21).mean() / close.pct_change(21).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_mean(base, 5)

def idec_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_mean(base, 21)

def idec_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_mean(base, 63)

def idec_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_mean(base, 126)

def idec_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_mean(base, 252)

def idec_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 5)

def idec_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 21)

def idec_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 63)

def idec_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 126)

def idec_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _zscore_rolling(base, 252)

def idec_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rank_pct(base, 5)

def idec_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rank_pct(base, 21)

def idec_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rank_pct(base, 63)

def idec_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rank_pct(base, 126)

def idec_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rank_pct(base, 252)

def idec_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_skew(base, 5)

def idec_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_skew(base, 21)

def idec_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_skew(base, 63)

def idec_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_skew(base, 126)

def idec_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_skew(base, 252)

def idec_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_kurt(base, 5)

def idec_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_kurt(base, 21)

def idec_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_kurt(base, 63)

def idec_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_kurt(base, 126)

def idec_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _rolling_kurt(base, 252)

def idec_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 5))

def idec_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 21))

def idec_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 63))

def idec_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 126))

def idec_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return _safe_div(base, _rolling_std(base, 252))

def idec_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change().abs().rolling(21).mean() / volume.pct_change(21).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 5)

def idec_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 21)

def idec_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 63)

def idec_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 126)

def idec_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 252)
