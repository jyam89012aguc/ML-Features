"""
80_80_yield_distress — Base Features 451-525
Domain: 80_yield_distress
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

def yldd_451_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def yldd_452_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def yldd_453_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def yldd_454_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def yldd_455_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(65)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def yldd_456_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 5)

def yldd_457_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 21)

def yldd_458_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 63)

def yldd_459_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 126)

def yldd_460_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(70)
    return _rolling_mean(base, 252)

def yldd_461_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 5)

def yldd_462_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 21)

def yldd_463_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 63)

def yldd_464_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 126)

def yldd_465_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(70)
    return _zscore_rolling(base, 252)

def yldd_466_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 5)

def yldd_467_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 21)

def yldd_468_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 63)

def yldd_469_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 126)

def yldd_470_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(70)
    return _rank_pct(base, 252)

def yldd_471_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 5)

def yldd_472_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 21)

def yldd_473_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 63)

def yldd_474_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 126)

def yldd_475_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(70)
    return _rolling_skew(base, 252)

def yldd_476_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 5)

def yldd_477_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 21)

def yldd_478_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 63)

def yldd_479_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 126)

def yldd_480_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(70)
    return _rolling_kurt(base, 252)

def yldd_481_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 5))

def yldd_482_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 21))

def yldd_483_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 63))

def yldd_484_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 126))

def yldd_485_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(70)
    return _safe_div(base, _rolling_std(base, 252))

def yldd_486_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def yldd_487_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def yldd_488_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def yldd_489_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def yldd_490_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(70)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def yldd_491_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 5)

def yldd_492_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 21)

def yldd_493_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 63)

def yldd_494_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 126)

def yldd_495_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(75)
    return _rolling_mean(base, 252)

def yldd_496_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 5)

def yldd_497_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 21)

def yldd_498_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 63)

def yldd_499_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 126)

def yldd_500_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(75)
    return _zscore_rolling(base, 252)

def yldd_501_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 5)

def yldd_502_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 21)

def yldd_503_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 63)

def yldd_504_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 126)

def yldd_505_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(75)
    return _rank_pct(base, 252)

def yldd_506_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 5)

def yldd_507_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 21)

def yldd_508_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 63)

def yldd_509_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 126)

def yldd_510_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(75)
    return _rolling_skew(base, 252)

def yldd_511_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 5)

def yldd_512_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 21)

def yldd_513_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 63)

def yldd_514_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 126)

def yldd_515_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(75)
    return _rolling_kurt(base, 252)

def yldd_516_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 5))

def yldd_517_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 21))

def yldd_518_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 63))

def yldd_519_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 126))

def yldd_520_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(75)
    return _safe_div(base, _rolling_std(base, 252))

def yldd_521_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def yldd_522_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def yldd_523_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def yldd_524_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def yldd_525_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(75)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
