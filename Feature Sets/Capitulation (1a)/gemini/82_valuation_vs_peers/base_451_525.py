"""
82_82_valuation_vs_peers — Base Features 451-525
Domain: 82_valuation_vs_peers
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

def vpee_451_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = pb
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_452_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = pb
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_453_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = pb
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_454_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = pb
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_455_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = pb
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpee_456_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 5)

def vpee_457_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 21)

def vpee_458_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 63)

def vpee_459_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 126)

def vpee_460_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, assets)
    return _rolling_mean(base, 252)

def vpee_461_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 5)

def vpee_462_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 21)

def vpee_463_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 63)

def vpee_464_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 126)

def vpee_465_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = _safe_div(ocf, assets)
    return _zscore_rolling(base, 252)

def vpee_466_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 5)

def vpee_467_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 21)

def vpee_468_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 63)

def vpee_469_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 126)

def vpee_470_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, assets)
    return _rank_pct(base, 252)

def vpee_471_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, assets)
    return _rolling_skew(base, 5)

def vpee_472_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, assets)
    return _rolling_skew(base, 21)

def vpee_473_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, assets)
    return _rolling_skew(base, 63)

def vpee_474_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, assets)
    return _rolling_skew(base, 126)

def vpee_475_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, assets)
    return _rolling_skew(base, 252)

def vpee_476_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, assets)
    return _rolling_kurt(base, 5)

def vpee_477_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, assets)
    return _rolling_kurt(base, 21)

def vpee_478_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, assets)
    return _rolling_kurt(base, 63)

def vpee_479_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, assets)
    return _rolling_kurt(base, 126)

def vpee_480_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, assets)
    return _rolling_kurt(base, 252)

def vpee_481_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, assets)
    return _safe_div(base, _rolling_std(base, 5))

def vpee_482_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, assets)
    return _safe_div(base, _rolling_std(base, 21))

def vpee_483_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, assets)
    return _safe_div(base, _rolling_std(base, 63))

def vpee_484_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, assets)
    return _safe_div(base, _rolling_std(base, 126))

def vpee_485_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, assets)
    return _safe_div(base, _rolling_std(base, 252))

def vpee_486_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, assets)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_487_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, assets)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_488_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, assets)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_489_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, assets)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_490_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, assets)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpee_491_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 5)

def vpee_492_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 21)

def vpee_493_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 63)

def vpee_494_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 126)

def vpee_495_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_mean(base, 252)

def vpee_496_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 5)

def vpee_497_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 21)

def vpee_498_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 63)

def vpee_499_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 126)

def vpee_500_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = _safe_div(netinc, revenue)
    return _zscore_rolling(base, 252)

def vpee_501_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 5)

def vpee_502_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 21)

def vpee_503_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 63)

def vpee_504_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 126)

def vpee_505_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, revenue)
    return _rank_pct(base, 252)

def vpee_506_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_skew(base, 5)

def vpee_507_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_skew(base, 21)

def vpee_508_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_skew(base, 63)

def vpee_509_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_skew(base, 126)

def vpee_510_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_skew(base, 252)

def vpee_511_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_kurt(base, 5)

def vpee_512_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_kurt(base, 21)

def vpee_513_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_kurt(base, 63)

def vpee_514_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_kurt(base, 126)

def vpee_515_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, revenue)
    return _rolling_kurt(base, 252)

def vpee_516_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, revenue)
    return _safe_div(base, _rolling_std(base, 5))

def vpee_517_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, revenue)
    return _safe_div(base, _rolling_std(base, 21))

def vpee_518_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, revenue)
    return _safe_div(base, _rolling_std(base, 63))

def vpee_519_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, revenue)
    return _safe_div(base, _rolling_std(base, 126))

def vpee_520_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, revenue)
    return _safe_div(base, _rolling_std(base, 252))

def vpee_521_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, revenue)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_522_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, revenue)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_523_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, revenue)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_524_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, revenue)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_525_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, revenue)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
