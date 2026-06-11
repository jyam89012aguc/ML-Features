"""
106_106_support_violation — Base Features 001-075
Domain: 106_support_violation
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

def supv_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_mean(base, 5)

def supv_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_mean(base, 21)

def supv_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_mean(base, 63)

def supv_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_mean(base, 126)

def supv_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_mean(base, 252)

def supv_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _zscore_rolling(base, 5)

def supv_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _zscore_rolling(base, 21)

def supv_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _zscore_rolling(base, 63)

def supv_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _zscore_rolling(base, 126)

def supv_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _zscore_rolling(base, 252)

def supv_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rank_pct(base, 5)

def supv_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rank_pct(base, 21)

def supv_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rank_pct(base, 63)

def supv_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rank_pct(base, 126)

def supv_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rank_pct(base, 252)

def supv_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_skew(base, 5)

def supv_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_skew(base, 21)

def supv_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_skew(base, 63)

def supv_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_skew(base, 126)

def supv_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_skew(base, 252)

def supv_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_kurt(base, 5)

def supv_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_kurt(base, 21)

def supv_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_kurt(base, 63)

def supv_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_kurt(base, 126)

def supv_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _rolling_kurt(base, 252)

def supv_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 5))

def supv_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 21))

def supv_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 63))

def supv_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 126))

def supv_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 252))

def supv_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(63).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_mean(base, 5)

def supv_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_mean(base, 21)

def supv_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_mean(base, 63)

def supv_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_mean(base, 126)

def supv_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_mean(base, 252)

def supv_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(252).min() - 1
    return _zscore_rolling(base, 5)

def supv_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(252).min() - 1
    return _zscore_rolling(base, 21)

def supv_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(252).min() - 1
    return _zscore_rolling(base, 63)

def supv_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(252).min() - 1
    return _zscore_rolling(base, 126)

def supv_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(252).min() - 1
    return _zscore_rolling(base, 252)

def supv_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(252).min() - 1
    return _rank_pct(base, 5)

def supv_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(252).min() - 1
    return _rank_pct(base, 21)

def supv_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(252).min() - 1
    return _rank_pct(base, 63)

def supv_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(252).min() - 1
    return _rank_pct(base, 126)

def supv_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(252).min() - 1
    return _rank_pct(base, 252)

def supv_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_skew(base, 5)

def supv_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_skew(base, 21)

def supv_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_skew(base, 63)

def supv_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_skew(base, 126)

def supv_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_skew(base, 252)

def supv_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_kurt(base, 5)

def supv_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_kurt(base, 21)

def supv_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_kurt(base, 63)

def supv_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_kurt(base, 126)

def supv_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(252).min() - 1
    return _rolling_kurt(base, 252)

def supv_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(252).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(252).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(252).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(252).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(252).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(252).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(252).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(252).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(252).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(252).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_mean(base, 5)

def supv_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_mean(base, 21)

def supv_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_mean(base, 63)

def supv_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_mean(base, 126)

def supv_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_mean(base, 252)
