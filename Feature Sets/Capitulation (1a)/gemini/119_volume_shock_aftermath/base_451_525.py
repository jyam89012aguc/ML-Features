"""
119_119_volume_shock_aftermath — Base Features 451-525
Domain: 119_volume_shock_aftermath
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

def vsha_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 130)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 130)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 130)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 130)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 130)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_mean(base, 5)

def vsha_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_mean(base, 21)

def vsha_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_mean(base, 63)

def vsha_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_mean(base, 126)

def vsha_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_mean(base, 252)

def vsha_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 140)
    return _zscore_rolling(base, 5)

def vsha_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 140)
    return _zscore_rolling(base, 21)

def vsha_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 140)
    return _zscore_rolling(base, 63)

def vsha_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 140)
    return _zscore_rolling(base, 126)

def vsha_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 140)
    return _zscore_rolling(base, 252)

def vsha_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rank_pct(base, 5)

def vsha_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rank_pct(base, 21)

def vsha_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rank_pct(base, 63)

def vsha_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rank_pct(base, 126)

def vsha_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rank_pct(base, 252)

def vsha_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_skew(base, 5)

def vsha_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_skew(base, 21)

def vsha_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_skew(base, 63)

def vsha_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_skew(base, 126)

def vsha_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_skew(base, 252)

def vsha_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_kurt(base, 5)

def vsha_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_kurt(base, 21)

def vsha_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_kurt(base, 63)

def vsha_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_kurt(base, 126)

def vsha_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 140)
    return _rolling_kurt(base, 252)

def vsha_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 140)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 140)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 140)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 140)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 140)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 140)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 140)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 140)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 140)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 140)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_mean(base, 5)

def vsha_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_mean(base, 21)

def vsha_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_mean(base, 63)

def vsha_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_mean(base, 126)

def vsha_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_mean(base, 252)

def vsha_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 150)
    return _zscore_rolling(base, 5)

def vsha_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 150)
    return _zscore_rolling(base, 21)

def vsha_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 150)
    return _zscore_rolling(base, 63)

def vsha_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 150)
    return _zscore_rolling(base, 126)

def vsha_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 150)
    return _zscore_rolling(base, 252)

def vsha_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rank_pct(base, 5)

def vsha_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rank_pct(base, 21)

def vsha_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rank_pct(base, 63)

def vsha_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rank_pct(base, 126)

def vsha_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rank_pct(base, 252)

def vsha_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_skew(base, 5)

def vsha_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_skew(base, 21)

def vsha_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_skew(base, 63)

def vsha_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_skew(base, 126)

def vsha_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_skew(base, 252)

def vsha_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_kurt(base, 5)

def vsha_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_kurt(base, 21)

def vsha_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_kurt(base, 63)

def vsha_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_kurt(base, 126)

def vsha_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 150)
    return _rolling_kurt(base, 252)

def vsha_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 150)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 150)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 150)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 150)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 150)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 150)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 150)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 150)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 150)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 150)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
