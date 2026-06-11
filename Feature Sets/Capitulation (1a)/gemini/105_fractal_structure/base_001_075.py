"""
105_105_fractal_structure — Base Features 001-075
Domain: 105_fractal_structure
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

def frac_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_mean(base, 5)

def frac_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_mean(base, 21)

def frac_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_mean(base, 63)

def frac_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_mean(base, 126)

def frac_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_mean(base, 252)

def frac_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _zscore_rolling(base, 5)

def frac_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _zscore_rolling(base, 21)

def frac_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _zscore_rolling(base, 63)

def frac_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _zscore_rolling(base, 126)

def frac_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _zscore_rolling(base, 252)

def frac_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rank_pct(base, 5)

def frac_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rank_pct(base, 21)

def frac_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rank_pct(base, 63)

def frac_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rank_pct(base, 126)

def frac_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rank_pct(base, 252)

def frac_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_skew(base, 5)

def frac_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_skew(base, 21)

def frac_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_skew(base, 63)

def frac_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_skew(base, 126)

def frac_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_skew(base, 252)

def frac_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_kurt(base, 5)

def frac_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_kurt(base, 21)

def frac_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_kurt(base, 63)

def frac_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_kurt(base, 126)

def frac_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _rolling_kurt(base, 252)

def frac_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _safe_div(base, _rolling_std(base, 5))

def frac_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _safe_div(base, _rolling_std(base, 21))

def frac_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _safe_div(base, _rolling_std(base, 63))

def frac_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _safe_div(base, _rolling_std(base, 126))

def frac_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return _safe_div(base, _rolling_std(base, 252))

def frac_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.log(high.rolling(10).max() - low.rolling(10).min()) / np.log(10)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 5)

def frac_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 21)

def frac_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 63)

def frac_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 126)

def frac_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 252)

def frac_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 5)

def frac_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 21)

def frac_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 63)

def frac_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 126)

def frac_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _zscore_rolling(base, 252)

def frac_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 5)

def frac_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 21)

def frac_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 63)

def frac_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 126)

def frac_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rank_pct(base, 252)

def frac_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_skew(base, 5)

def frac_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_skew(base, 21)

def frac_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_skew(base, 63)

def frac_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_skew(base, 126)

def frac_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_skew(base, 252)

def frac_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_kurt(base, 5)

def frac_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_kurt(base, 21)

def frac_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_kurt(base, 63)

def frac_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_kurt(base, 126)

def frac_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_kurt(base, 252)

def frac_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _safe_div(base, _rolling_std(base, 5))

def frac_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _safe_div(base, _rolling_std(base, 21))

def frac_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _safe_div(base, _rolling_std(base, 63))

def frac_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _safe_div(base, _rolling_std(base, 126))

def frac_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _safe_div(base, _rolling_std(base, 252))

def frac_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = (high - low).rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 5)

def frac_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 21)

def frac_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 63)

def frac_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 126)

def frac_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(21).sum() / (high.rolling(21).max() - low.rolling(21).min())
    return _rolling_mean(base, 252)
