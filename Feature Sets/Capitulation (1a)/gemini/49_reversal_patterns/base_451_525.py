"""
49_49_reversal_patterns — Base Features 451-525
Domain: 49_reversal_patterns
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

def revp_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def revp_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def revp_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def revp_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def revp_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def revp_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 5)

def revp_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 21)

def revp_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 63)

def revp_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 126)

def revp_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 252)

def revp_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 5)

def revp_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 21)

def revp_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 63)

def revp_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 126)

def revp_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 252)

def revp_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 5)

def revp_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 21)

def revp_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 63)

def revp_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 126)

def revp_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 252)

def revp_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 5)

def revp_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 21)

def revp_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 63)

def revp_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 126)

def revp_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 252)

def revp_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 5)

def revp_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 21)

def revp_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 63)

def revp_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 126)

def revp_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 252)

def revp_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def revp_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def revp_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def revp_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def revp_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def revp_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def revp_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def revp_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def revp_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def revp_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def revp_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 5)

def revp_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 21)

def revp_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 63)

def revp_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 126)

def revp_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 49 reversal patterns over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 252)

def revp_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 5)

def revp_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 21)

def revp_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 63)

def revp_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 126)

def revp_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 49 reversal patterns by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 252)

def revp_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 5)

def revp_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 21)

def revp_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 63)

def revp_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 126)

def revp_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 49 reversal patterns to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 252)

def revp_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 5)

def revp_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 21)

def revp_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 63)

def revp_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 126)

def revp_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 49 reversal patterns distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 252)

def revp_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 5)

def revp_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 21)

def revp_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 63)

def revp_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 126)

def revp_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 49 reversal patterns over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 252)

def revp_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def revp_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def revp_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def revp_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def revp_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 49 reversal patterns for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def revp_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def revp_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def revp_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def revp_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def revp_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 49 reversal patterns over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
