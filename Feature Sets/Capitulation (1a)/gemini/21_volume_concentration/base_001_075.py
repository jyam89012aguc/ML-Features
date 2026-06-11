"""
21_21_volume_concentration — Base Features 001-075
Domain: 21_volume_concentration
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

def vcc_001_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 5d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 5)

def vcc_002_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 21d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 21)

def vcc_003_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 63d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 63)

def vcc_004_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 126d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 126)

def vcc_005_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 252d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_mean(base, 252)

def vcc_006_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 5d mean.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 5)

def vcc_007_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 21d mean.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 21)

def vcc_008_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 63d mean.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 63)

def vcc_009_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 126d mean.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 126)

def vcc_010_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 252d mean.
    """
    base = volume / volume.rolling(252).mean()
    return _zscore_rolling(base, 252)

def vcc_011_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 5)

def vcc_012_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 21)

def vcc_013_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 63)

def vcc_014_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 126)

def vcc_015_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(252).mean()
    return _rank_pct(base, 252)

def vcc_016_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_skew(base, 5)

def vcc_017_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_skew(base, 21)

def vcc_018_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_skew(base, 63)

def vcc_019_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_skew(base, 126)

def vcc_020_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_skew(base, 252)

def vcc_021_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_kurt(base, 5)

def vcc_022_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_kurt(base, 21)

def vcc_023_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_kurt(base, 63)

def vcc_024_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_kurt(base, 126)

def vcc_025_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(252).mean()
    return _rolling_kurt(base, 252)

def vcc_026_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean()
    return _safe_div(base, _rolling_std(base, 5))

def vcc_027_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean()
    return _safe_div(base, _rolling_std(base, 21))

def vcc_028_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean()
    return _safe_div(base, _rolling_std(base, 63))

def vcc_029_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean()
    return _safe_div(base, _rolling_std(base, 126))

def vcc_030_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(252).mean()
    return _safe_div(base, _rolling_std(base, 252))

def vcc_031_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vcc_032_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vcc_033_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vcc_034_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vcc_035_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(252).mean()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vcc_036_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_mean(base, 5)

def vcc_037_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_mean(base, 21)

def vcc_038_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_mean(base, 63)

def vcc_039_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_mean(base, 126)

def vcc_040_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_mean(base, 252)

def vcc_041_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _zscore_rolling(base, 5)

def vcc_042_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _zscore_rolling(base, 21)

def vcc_043_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _zscore_rolling(base, 63)

def vcc_044_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _zscore_rolling(base, 126)

def vcc_045_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 21 volume concentration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _zscore_rolling(base, 252)

def vcc_046_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rank_pct(base, 5)

def vcc_047_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rank_pct(base, 21)

def vcc_048_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rank_pct(base, 63)

def vcc_049_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rank_pct(base, 126)

def vcc_050_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 21 volume concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rank_pct(base, 252)

def vcc_051_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_skew(base, 5)

def vcc_052_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_skew(base, 21)

def vcc_053_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_skew(base, 63)

def vcc_054_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_skew(base, 126)

def vcc_055_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 21 volume concentration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_skew(base, 252)

def vcc_056_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_kurt(base, 5)

def vcc_057_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_kurt(base, 21)

def vcc_058_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_kurt(base, 63)

def vcc_059_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_kurt(base, 126)

def vcc_060_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 21 volume concentration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _rolling_kurt(base, 252)

def vcc_061_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 5))

def vcc_062_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 21))

def vcc_063_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 63))

def vcc_064_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 126))

def vcc_065_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 21 volume concentration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 252))

def vcc_066_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vcc_067_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vcc_068_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vcc_069_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vcc_070_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 21 volume concentration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() * volume).rolling(21).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vcc_071_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 5d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 5)

def vcc_072_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 21d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 21)

def vcc_073_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 63d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 63)

def vcc_074_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 126d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 126)

def vcc_075_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 21 volume concentration over a 252d horizon to identify extreme regimes.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_mean(base, 252)
