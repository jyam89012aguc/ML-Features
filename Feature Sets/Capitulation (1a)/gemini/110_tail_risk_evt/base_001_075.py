"""
110_110_tail_risk_evt — Base Features 001-075
Domain: 110_tail_risk_evt
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

def trev_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rank_pct(base, 5)

def trev_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rank_pct(base, 21)

def trev_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rank_pct(base, 63)

def trev_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rank_pct(base, 126)

def trev_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rank_pct(base, 252)

def trev_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_mean(base, 5)

def trev_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_mean(base, 21)

def trev_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_mean(base, 63)

def trev_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_mean(base, 126)

def trev_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_mean(base, 252)

def trev_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _zscore_rolling(base, 5)

def trev_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _zscore_rolling(base, 21)

def trev_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _zscore_rolling(base, 63)

def trev_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _zscore_rolling(base, 126)

def trev_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _zscore_rolling(base, 252)

def trev_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rank_pct(base, 5)

def trev_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rank_pct(base, 21)

def trev_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rank_pct(base, 63)

def trev_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rank_pct(base, 126)

def trev_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rank_pct(base, 252)

def trev_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_skew(base, 5)

def trev_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_skew(base, 21)

def trev_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_skew(base, 63)

def trev_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_skew(base, 126)

def trev_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_skew(base, 252)

def trev_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_kurt(base, 5)

def trev_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_kurt(base, 21)

def trev_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_kurt(base, 63)

def trev_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_kurt(base, 126)

def trev_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _rolling_kurt(base, 252)

def trev_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _safe_div(base, _rolling_std(base, 5))

def trev_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _safe_div(base, _rolling_std(base, 21))

def trev_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _safe_div(base, _rolling_std(base, 63))

def trev_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _safe_div(base, _rolling_std(base, 126))

def trev_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return _safe_div(base, _rolling_std(base, 252))

def trev_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(252).quantile(0.05)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change() / close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change() / close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change() / close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change() / close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change() / close.pct_change().rolling(252).quantile(0.01)
    return _rolling_mean(base, 252)
