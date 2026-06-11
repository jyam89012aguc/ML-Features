"""
58_58_trading_intensity — Base Features 001-075
Domain: 58_trading_intensity
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

def tint_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def tint_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def tint_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def tint_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def tint_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def tint_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def tint_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def tint_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def tint_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def tint_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def tint_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rank_pct(base, 5)

def tint_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rank_pct(base, 21)

def tint_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rank_pct(base, 63)

def tint_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rank_pct(base, 126)

def tint_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rank_pct(base, 252)

def tint_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def tint_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def tint_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def tint_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def tint_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def tint_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def tint_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def tint_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def tint_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def tint_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def tint_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def tint_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def tint_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def tint_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def tint_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def tint_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tint_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_mean(base, 5)

def tint_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_mean(base, 21)

def tint_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_mean(base, 63)

def tint_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_mean(base, 126)

def tint_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_mean(base, 252)

def tint_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _zscore_rolling(base, 5)

def tint_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _zscore_rolling(base, 21)

def tint_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _zscore_rolling(base, 63)

def tint_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _zscore_rolling(base, 126)

def tint_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _zscore_rolling(base, 252)

def tint_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rank_pct(base, 5)

def tint_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rank_pct(base, 21)

def tint_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rank_pct(base, 63)

def tint_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rank_pct(base, 126)

def tint_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rank_pct(base, 252)

def tint_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_skew(base, 5)

def tint_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_skew(base, 21)

def tint_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_skew(base, 63)

def tint_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_skew(base, 126)

def tint_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_skew(base, 252)

def tint_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_kurt(base, 5)

def tint_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_kurt(base, 21)

def tint_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_kurt(base, 63)

def tint_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_kurt(base, 126)

def tint_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _rolling_kurt(base, 252)

def tint_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 5))

def tint_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 21))

def tint_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 63))

def tint_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 126))

def tint_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 252))

def tint_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.diff().abs() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tint_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def tint_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def tint_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def tint_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def tint_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_mean(base, 252)
