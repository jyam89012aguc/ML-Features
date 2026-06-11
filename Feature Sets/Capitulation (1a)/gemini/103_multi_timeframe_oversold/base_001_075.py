"""
103_103_multi_timeframe_oversold — Base Features 001-075
Domain: 103_multi_timeframe_oversold
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

def mtfo_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_mean(base, 5)

def mtfo_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_mean(base, 21)

def mtfo_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_mean(base, 63)

def mtfo_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_mean(base, 126)

def mtfo_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_mean(base, 252)

def mtfo_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 21)
    return _zscore_rolling(base, 5)

def mtfo_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 21)
    return _zscore_rolling(base, 21)

def mtfo_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 21)
    return _zscore_rolling(base, 63)

def mtfo_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 21)
    return _zscore_rolling(base, 126)

def mtfo_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 21)
    return _zscore_rolling(base, 252)

def mtfo_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 21)
    return _rank_pct(base, 5)

def mtfo_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 21)
    return _rank_pct(base, 21)

def mtfo_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 21)
    return _rank_pct(base, 63)

def mtfo_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 21)
    return _rank_pct(base, 126)

def mtfo_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 21)
    return _rank_pct(base, 252)

def mtfo_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_skew(base, 5)

def mtfo_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_skew(base, 21)

def mtfo_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_skew(base, 63)

def mtfo_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_skew(base, 126)

def mtfo_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_skew(base, 252)

def mtfo_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_kurt(base, 5)

def mtfo_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_kurt(base, 21)

def mtfo_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_kurt(base, 63)

def mtfo_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_kurt(base, 126)

def mtfo_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 21)
    return _rolling_kurt(base, 252)

def mtfo_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 21)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 21)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 21)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 21)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 21)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 21)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 21)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 21)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 21)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 21)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 5)

def mtfo_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 21)

def mtfo_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 63)

def mtfo_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 126)

def mtfo_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_mean(base, 252)

def mtfo_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 5)

def mtfo_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 21)

def mtfo_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 63)

def mtfo_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 126)

def mtfo_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 63)
    return _zscore_rolling(base, 252)

def mtfo_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 5)

def mtfo_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 21)

def mtfo_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 63)

def mtfo_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 126)

def mtfo_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 63)
    return _rank_pct(base, 252)

def mtfo_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_skew(base, 5)

def mtfo_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_skew(base, 21)

def mtfo_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_skew(base, 63)

def mtfo_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_skew(base, 126)

def mtfo_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_skew(base, 252)

def mtfo_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_kurt(base, 5)

def mtfo_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_kurt(base, 21)

def mtfo_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_kurt(base, 63)

def mtfo_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_kurt(base, 126)

def mtfo_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 63)
    return _rolling_kurt(base, 252)

def mtfo_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 63)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 63)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 63)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 63)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 63)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 63)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 63)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 63)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 63)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 63)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 252)
    return _rolling_mean(base, 5)

def mtfo_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 252)
    return _rolling_mean(base, 21)

def mtfo_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 252)
    return _rolling_mean(base, 63)

def mtfo_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 252)
    return _rolling_mean(base, 126)

def mtfo_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 252)
    return _rolling_mean(base, 252)
