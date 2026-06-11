"""
79_79_ev_distortion — Base Features 451-525
Domain: 79_ev_distortion
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

def evds_451_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evds_452_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evds_453_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evds_454_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evds_455_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evds_456_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 5)

def evds_457_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 21)

def evds_458_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 63)

def evds_459_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 126)

def evds_460_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 252)

def evds_461_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 5)

def evds_462_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 21)

def evds_463_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 63)

def evds_464_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 126)

def evds_465_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 252)

def evds_466_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 5)

def evds_467_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 21)

def evds_468_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 63)

def evds_469_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 126)

def evds_470_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 252)

def evds_471_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 5)

def evds_472_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 21)

def evds_473_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 63)

def evds_474_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 126)

def evds_475_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 252)

def evds_476_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 5)

def evds_477_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 21)

def evds_478_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 63)

def evds_479_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 126)

def evds_480_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 252)

def evds_481_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 5))

def evds_482_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 21))

def evds_483_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 63))

def evds_484_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 126))

def evds_485_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 252))

def evds_486_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evds_487_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evds_488_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evds_489_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evds_490_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evds_491_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 5)

def evds_492_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 21)

def evds_493_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 63)

def evds_494_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 126)

def evds_495_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 252)

def evds_496_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 5)

def evds_497_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 21)

def evds_498_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 63)

def evds_499_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 126)

def evds_500_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 252)

def evds_501_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 5)

def evds_502_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 21)

def evds_503_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 63)

def evds_504_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 126)

def evds_505_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 252)

def evds_506_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 5)

def evds_507_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 21)

def evds_508_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 63)

def evds_509_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 126)

def evds_510_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 252)

def evds_511_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 5)

def evds_512_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 21)

def evds_513_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 63)

def evds_514_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 126)

def evds_515_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 252)

def evds_516_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 5))

def evds_517_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 21))

def evds_518_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 63))

def evds_519_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 126))

def evds_520_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 252))

def evds_521_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evds_522_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evds_523_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evds_524_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evds_525_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
