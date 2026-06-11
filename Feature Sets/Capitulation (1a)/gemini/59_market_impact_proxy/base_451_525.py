"""
59_59_market_impact_proxy — Base Features 451-525
Domain: 59_market_impact_proxy
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

def mimp_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def mimp_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def mimp_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def mimp_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def mimp_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def mimp_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def mimp_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def mimp_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def mimp_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def mimp_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def mimp_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def mimp_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def mimp_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def mimp_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def mimp_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def mimp_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def mimp_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def mimp_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def mimp_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def mimp_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def mimp_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def mimp_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def mimp_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def mimp_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def mimp_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def mimp_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def mimp_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def mimp_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def mimp_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def mimp_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def mimp_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def mimp_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def mimp_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def mimp_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def mimp_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def mimp_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def mimp_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def mimp_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def mimp_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def mimp_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def mimp_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def mimp_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def mimp_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def mimp_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def mimp_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def mimp_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def mimp_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def mimp_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def mimp_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def mimp_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def mimp_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
