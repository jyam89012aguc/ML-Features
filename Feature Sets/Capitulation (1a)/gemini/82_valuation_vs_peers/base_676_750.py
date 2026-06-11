"""
82_82_valuation_vs_peers — Base Features 676-750
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

def vpee_676_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, ocf)
    return _rank_pct(base, 5)

def vpee_677_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, ocf)
    return _rank_pct(base, 21)

def vpee_678_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, ocf)
    return _rank_pct(base, 63)

def vpee_679_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, ocf)
    return _rank_pct(base, 126)

def vpee_680_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, ocf)
    return _rank_pct(base, 252)

def vpee_681_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_skew(base, 5)

def vpee_682_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_skew(base, 21)

def vpee_683_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_skew(base, 63)

def vpee_684_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_skew(base, 126)

def vpee_685_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_skew(base, 252)

def vpee_686_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_kurt(base, 5)

def vpee_687_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_kurt(base, 21)

def vpee_688_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_kurt(base, 63)

def vpee_689_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_kurt(base, 126)

def vpee_690_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_kurt(base, 252)

def vpee_691_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, ocf)
    return _safe_div(base, _rolling_std(base, 5))

def vpee_692_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, ocf)
    return _safe_div(base, _rolling_std(base, 21))

def vpee_693_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, ocf)
    return _safe_div(base, _rolling_std(base, 63))

def vpee_694_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, ocf)
    return _safe_div(base, _rolling_std(base, 126))

def vpee_695_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, ocf)
    return _safe_div(base, _rolling_std(base, 252))

def vpee_696_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, ocf)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_697_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, ocf)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_698_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, ocf)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_699_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, ocf)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_700_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, ocf)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpee_701_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 5)

def vpee_702_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 21)

def vpee_703_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 63)

def vpee_704_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 126)

def vpee_705_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_mean(base, 252)

def vpee_706_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 5)

def vpee_707_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 21)

def vpee_708_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 63)

def vpee_709_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 126)

def vpee_710_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = _safe_div(fcf, marketcap)
    return _zscore_rolling(base, 252)

def vpee_711_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 5)

def vpee_712_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 21)

def vpee_713_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 63)

def vpee_714_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 126)

def vpee_715_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, marketcap)
    return _rank_pct(base, 252)

def vpee_716_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_skew(base, 5)

def vpee_717_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_skew(base, 21)

def vpee_718_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_skew(base, 63)

def vpee_719_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_skew(base, 126)

def vpee_720_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_skew(base, 252)

def vpee_721_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_kurt(base, 5)

def vpee_722_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_kurt(base, 21)

def vpee_723_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_kurt(base, 63)

def vpee_724_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_kurt(base, 126)

def vpee_725_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, marketcap)
    return _rolling_kurt(base, 252)

def vpee_726_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, marketcap)
    return _safe_div(base, _rolling_std(base, 5))

def vpee_727_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, marketcap)
    return _safe_div(base, _rolling_std(base, 21))

def vpee_728_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, marketcap)
    return _safe_div(base, _rolling_std(base, 63))

def vpee_729_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, marketcap)
    return _safe_div(base, _rolling_std(base, 126))

def vpee_730_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, marketcap)
    return _safe_div(base, _rolling_std(base, 252))

def vpee_731_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, marketcap)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_732_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, marketcap)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_733_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, marketcap)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_734_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, marketcap)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_735_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, marketcap)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpee_736_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 5d horizon to identify extreme regimes.
    """
    base = ps
    return _rolling_mean(base, 5)

def vpee_737_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 21d horizon to identify extreme regimes.
    """
    base = ps
    return _rolling_mean(base, 21)

def vpee_738_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 63d horizon to identify extreme regimes.
    """
    base = ps
    return _rolling_mean(base, 63)

def vpee_739_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 126d horizon to identify extreme regimes.
    """
    base = ps
    return _rolling_mean(base, 126)

def vpee_740_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 252d horizon to identify extreme regimes.
    """
    base = ps
    return _rolling_mean(base, 252)

def vpee_741_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = ps
    return _zscore_rolling(base, 5)

def vpee_742_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = ps
    return _zscore_rolling(base, 21)

def vpee_743_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = ps
    return _zscore_rolling(base, 63)

def vpee_744_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = ps
    return _zscore_rolling(base, 126)

def vpee_745_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = ps
    return _zscore_rolling(base, 252)

def vpee_746_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ps
    return _rank_pct(base, 5)

def vpee_747_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ps
    return _rank_pct(base, 21)

def vpee_748_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ps
    return _rank_pct(base, 63)

def vpee_749_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ps
    return _rank_pct(base, 126)

def vpee_750_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ps
    return _rank_pct(base, 252)
