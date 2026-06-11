"""
51_51_shadow_wick_analysis — Base Features 001-075
Domain: 51_shadow_wick_analysis
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

def swik_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def swik_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def swik_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def swik_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def swik_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def swik_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 5d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def swik_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 21d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def swik_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 63d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def swik_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 126d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def swik_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 252d mean.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def swik_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 5)

def swik_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 21)

def swik_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 63)

def swik_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 126)

def swik_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rank_pct(base, 252)

def swik_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def swik_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def swik_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def swik_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def swik_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def swik_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 5d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def swik_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 21d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def swik_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 63d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def swik_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 126d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def swik_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 252d to capture explosive breakdown or reversal points.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def swik_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def swik_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def swik_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def swik_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def swik_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def swik_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def swik_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def swik_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def swik_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def swik_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open - close.shift(1)) / close.shift(1).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def swik_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def swik_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def swik_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def swik_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def swik_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def swik_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 5d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def swik_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 21d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def swik_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 63d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def swik_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 126d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def swik_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 252d mean.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def swik_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def swik_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def swik_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def swik_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def swik_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def swik_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def swik_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def swik_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def swik_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def swik_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def swik_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 5d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def swik_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 21d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def swik_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 63d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def swik_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 126d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def swik_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 252d to capture explosive breakdown or reversal points.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def swik_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def swik_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def swik_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def swik_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def swik_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def swik_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def swik_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def swik_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def swik_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def swik_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close - open) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def swik_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def swik_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def swik_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def swik_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def swik_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)
