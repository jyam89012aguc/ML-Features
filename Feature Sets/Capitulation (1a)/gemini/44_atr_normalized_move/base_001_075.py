"""
44_44_atr_normalized_move — Base Features 001-075
Domain: 44_atr_normalized_move
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

def atrn_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 5d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def atrn_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 21d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def atrn_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 63d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def atrn_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 126d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def atrn_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 252d horizon to identify extreme regimes.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def atrn_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 5d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def atrn_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 21d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def atrn_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 63d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def atrn_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 126d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def atrn_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 252d mean.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def atrn_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 5)

def atrn_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 21)

def atrn_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 63)

def atrn_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 126)

def atrn_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rank_pct(base, 252)

def atrn_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 5d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def atrn_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 21d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def atrn_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 63d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def atrn_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 126d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def atrn_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 252d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def atrn_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 5d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def atrn_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 21d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def atrn_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 63d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def atrn_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 126d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def atrn_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 252d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def atrn_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def atrn_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def atrn_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def atrn_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def atrn_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def atrn_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 5d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def atrn_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 21d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def atrn_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 63d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def atrn_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 126d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def atrn_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 252d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def atrn_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 5)

def atrn_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 21)

def atrn_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 63)

def atrn_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 126)

def atrn_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_mean(base, 252)

def atrn_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 5)

def atrn_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 21)

def atrn_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 63)

def atrn_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 126)

def atrn_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 44 atr normalized move by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 252)

def atrn_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 5)

def atrn_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 21)

def atrn_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 63)

def atrn_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 126)

def atrn_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 44 atr normalized move to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).std()
    return _rank_pct(base, 252)

def atrn_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 5)

def atrn_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 21)

def atrn_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 63)

def atrn_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 126)

def atrn_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 44 atr normalized move distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_skew(base, 252)

def atrn_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 5)

def atrn_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 21)

def atrn_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 63)

def atrn_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 126)

def atrn_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 44 atr normalized move over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 252)

def atrn_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def atrn_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def atrn_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def atrn_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def atrn_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 44 atr normalized move for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def atrn_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def atrn_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def atrn_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def atrn_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def atrn_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 44 atr normalized move over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def atrn_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 5d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 5)

def atrn_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 21d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 21)

def atrn_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 63d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 63)

def atrn_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 126d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 126)

def atrn_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 44 atr normalized move over a 252d horizon to identify extreme regimes.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_mean(base, 252)
