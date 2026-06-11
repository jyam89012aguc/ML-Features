"""
64_64_liquidity_distress — Base Features 451-525
Domain: 64_liquidity_distress
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

def ldis_451_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(65)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_452_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(65)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_453_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(65)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_454_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(65)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_455_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(65)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_456_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(70)
    return _rolling_mean(base, 5)

def ldis_457_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(70)
    return _rolling_mean(base, 21)

def ldis_458_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(70)
    return _rolling_mean(base, 63)

def ldis_459_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(70)
    return _rolling_mean(base, 126)

def ldis_460_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(70)
    return _rolling_mean(base, 252)

def ldis_461_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(70)
    return _zscore_rolling(base, 5)

def ldis_462_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(70)
    return _zscore_rolling(base, 21)

def ldis_463_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(70)
    return _zscore_rolling(base, 63)

def ldis_464_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(70)
    return _zscore_rolling(base, 126)

def ldis_465_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(70)
    return _zscore_rolling(base, 252)

def ldis_466_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(70)
    return _rank_pct(base, 5)

def ldis_467_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(70)
    return _rank_pct(base, 21)

def ldis_468_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(70)
    return _rank_pct(base, 63)

def ldis_469_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(70)
    return _rank_pct(base, 126)

def ldis_470_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(70)
    return _rank_pct(base, 252)

def ldis_471_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(70)
    return _rolling_skew(base, 5)

def ldis_472_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(70)
    return _rolling_skew(base, 21)

def ldis_473_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(70)
    return _rolling_skew(base, 63)

def ldis_474_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(70)
    return _rolling_skew(base, 126)

def ldis_475_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(70)
    return _rolling_skew(base, 252)

def ldis_476_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(70)
    return _rolling_kurt(base, 5)

def ldis_477_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(70)
    return _rolling_kurt(base, 21)

def ldis_478_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(70)
    return _rolling_kurt(base, 63)

def ldis_479_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(70)
    return _rolling_kurt(base, 126)

def ldis_480_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(70)
    return _rolling_kurt(base, 252)

def ldis_481_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(70)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_482_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(70)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_483_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(70)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_484_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(70)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_485_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(70)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_486_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(70)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_487_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(70)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_488_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(70)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_489_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(70)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_490_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(70)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_491_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(75)
    return _rolling_mean(base, 5)

def ldis_492_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(75)
    return _rolling_mean(base, 21)

def ldis_493_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(75)
    return _rolling_mean(base, 63)

def ldis_494_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(75)
    return _rolling_mean(base, 126)

def ldis_495_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(75)
    return _rolling_mean(base, 252)

def ldis_496_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(75)
    return _zscore_rolling(base, 5)

def ldis_497_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(75)
    return _zscore_rolling(base, 21)

def ldis_498_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(75)
    return _zscore_rolling(base, 63)

def ldis_499_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(75)
    return _zscore_rolling(base, 126)

def ldis_500_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(75)
    return _zscore_rolling(base, 252)

def ldis_501_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(75)
    return _rank_pct(base, 5)

def ldis_502_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(75)
    return _rank_pct(base, 21)

def ldis_503_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(75)
    return _rank_pct(base, 63)

def ldis_504_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(75)
    return _rank_pct(base, 126)

def ldis_505_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(75)
    return _rank_pct(base, 252)

def ldis_506_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(75)
    return _rolling_skew(base, 5)

def ldis_507_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(75)
    return _rolling_skew(base, 21)

def ldis_508_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(75)
    return _rolling_skew(base, 63)

def ldis_509_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(75)
    return _rolling_skew(base, 126)

def ldis_510_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(75)
    return _rolling_skew(base, 252)

def ldis_511_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(75)
    return _rolling_kurt(base, 5)

def ldis_512_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(75)
    return _rolling_kurt(base, 21)

def ldis_513_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(75)
    return _rolling_kurt(base, 63)

def ldis_514_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(75)
    return _rolling_kurt(base, 126)

def ldis_515_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(75)
    return _rolling_kurt(base, 252)

def ldis_516_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(75)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_517_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(75)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_518_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(75)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_519_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(75)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_520_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(75)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_521_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(75)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_522_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(75)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_523_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(75)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_524_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(75)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_525_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(75)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
