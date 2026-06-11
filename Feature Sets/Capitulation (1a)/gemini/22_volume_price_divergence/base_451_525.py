"""
22_22_volume_price_divergence — Base Features 451-525
Domain: 22_volume_price_divergence
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

def vpd_451_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpd_452_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpd_453_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpd_454_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpd_455_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpd_456_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def vpd_457_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def vpd_458_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def vpd_459_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def vpd_460_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def vpd_461_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def vpd_462_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def vpd_463_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def vpd_464_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def vpd_465_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def vpd_466_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def vpd_467_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def vpd_468_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def vpd_469_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def vpd_470_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def vpd_471_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def vpd_472_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def vpd_473_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def vpd_474_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def vpd_475_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def vpd_476_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def vpd_477_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def vpd_478_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def vpd_479_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def vpd_480_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def vpd_481_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vpd_482_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vpd_483_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vpd_484_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vpd_485_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vpd_486_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpd_487_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpd_488_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpd_489_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpd_490_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpd_491_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def vpd_492_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def vpd_493_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def vpd_494_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def vpd_495_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 22 volume price divergence over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def vpd_496_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def vpd_497_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def vpd_498_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def vpd_499_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def vpd_500_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 22 volume price divergence by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def vpd_501_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def vpd_502_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def vpd_503_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def vpd_504_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def vpd_505_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 22 volume price divergence to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def vpd_506_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def vpd_507_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def vpd_508_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def vpd_509_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def vpd_510_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 22 volume price divergence distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def vpd_511_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def vpd_512_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def vpd_513_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def vpd_514_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def vpd_515_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 22 volume price divergence over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def vpd_516_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vpd_517_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vpd_518_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vpd_519_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vpd_520_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 22 volume price divergence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vpd_521_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpd_522_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpd_523_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpd_524_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpd_525_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 22 volume price divergence over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
