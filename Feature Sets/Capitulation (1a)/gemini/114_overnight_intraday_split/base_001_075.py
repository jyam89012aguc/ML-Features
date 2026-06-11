"""
114_114_overnight_intraday_split — Base Features 001-075
Domain: 114_overnight_intraday_split
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

def onid_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 5)

def onid_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 21)

def onid_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 63)

def onid_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 126)

def onid_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 252)

def onid_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 5)

def onid_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 21)

def onid_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 63)

def onid_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 126)

def onid_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 252)

def onid_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 5)

def onid_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 21)

def onid_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 63)

def onid_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 126)

def onid_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 252)

def onid_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = open / close.shift(1) - 1
    return _rolling_skew(base, 5)

def onid_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = open / close.shift(1) - 1
    return _rolling_skew(base, 21)

def onid_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = open / close.shift(1) - 1
    return _rolling_skew(base, 63)

def onid_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = open / close.shift(1) - 1
    return _rolling_skew(base, 126)

def onid_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = open / close.shift(1) - 1
    return _rolling_skew(base, 252)

def onid_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = open / close.shift(1) - 1
    return _rolling_kurt(base, 5)

def onid_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = open / close.shift(1) - 1
    return _rolling_kurt(base, 21)

def onid_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = open / close.shift(1) - 1
    return _rolling_kurt(base, 63)

def onid_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = open / close.shift(1) - 1
    return _rolling_kurt(base, 126)

def onid_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = open / close.shift(1) - 1
    return _rolling_kurt(base, 252)

def onid_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = open / close.shift(1) - 1
    return _safe_div(base, _rolling_std(base, 5))

def onid_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = open / close.shift(1) - 1
    return _safe_div(base, _rolling_std(base, 21))

def onid_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = open / close.shift(1) - 1
    return _safe_div(base, _rolling_std(base, 63))

def onid_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = open / close.shift(1) - 1
    return _safe_div(base, _rolling_std(base, 126))

def onid_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = open / close.shift(1) - 1
    return _safe_div(base, _rolling_std(base, 252))

def onid_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = open / close.shift(1) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = open / close.shift(1) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = open / close.shift(1) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = open / close.shift(1) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = open / close.shift(1) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = close / open - 1
    return _rolling_mean(base, 5)

def onid_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = close / open - 1
    return _rolling_mean(base, 21)

def onid_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = close / open - 1
    return _rolling_mean(base, 63)

def onid_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = close / open - 1
    return _rolling_mean(base, 126)

def onid_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = close / open - 1
    return _rolling_mean(base, 252)

def onid_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = close / open - 1
    return _zscore_rolling(base, 5)

def onid_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = close / open - 1
    return _zscore_rolling(base, 21)

def onid_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = close / open - 1
    return _zscore_rolling(base, 63)

def onid_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = close / open - 1
    return _zscore_rolling(base, 126)

def onid_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = close / open - 1
    return _zscore_rolling(base, 252)

def onid_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / open - 1
    return _rank_pct(base, 5)

def onid_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / open - 1
    return _rank_pct(base, 21)

def onid_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / open - 1
    return _rank_pct(base, 63)

def onid_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / open - 1
    return _rank_pct(base, 126)

def onid_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / open - 1
    return _rank_pct(base, 252)

def onid_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / open - 1
    return _rolling_skew(base, 5)

def onid_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / open - 1
    return _rolling_skew(base, 21)

def onid_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / open - 1
    return _rolling_skew(base, 63)

def onid_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / open - 1
    return _rolling_skew(base, 126)

def onid_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / open - 1
    return _rolling_skew(base, 252)

def onid_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = close / open - 1
    return _rolling_kurt(base, 5)

def onid_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = close / open - 1
    return _rolling_kurt(base, 21)

def onid_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = close / open - 1
    return _rolling_kurt(base, 63)

def onid_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = close / open - 1
    return _rolling_kurt(base, 126)

def onid_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = close / open - 1
    return _rolling_kurt(base, 252)

def onid_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / open - 1
    return _safe_div(base, _rolling_std(base, 5))

def onid_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / open - 1
    return _safe_div(base, _rolling_std(base, 21))

def onid_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / open - 1
    return _safe_div(base, _rolling_std(base, 63))

def onid_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / open - 1
    return _safe_div(base, _rolling_std(base, 126))

def onid_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / open - 1
    return _safe_div(base, _rolling_std(base, 252))

def onid_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / open - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / open - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / open - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / open - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / open - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 5)

def onid_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 21)

def onid_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 63)

def onid_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 126)

def onid_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 252)
