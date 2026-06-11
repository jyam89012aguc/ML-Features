"""
82_82_valuation_vs_peers — Base Features 601-675
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

def vpee_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 5)

def vpee_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 21)

def vpee_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 63)

def vpee_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 126)

def vpee_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = _safe_div(revenue, assets)
    return _zscore_rolling(base, 252)

def vpee_606_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 5)

def vpee_607_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 21)

def vpee_608_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 63)

def vpee_609_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 126)

def vpee_610_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, assets)
    return _rank_pct(base, 252)

def vpee_611_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, assets)
    return _rolling_skew(base, 5)

def vpee_612_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, assets)
    return _rolling_skew(base, 21)

def vpee_613_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, assets)
    return _rolling_skew(base, 63)

def vpee_614_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, assets)
    return _rolling_skew(base, 126)

def vpee_615_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, assets)
    return _rolling_skew(base, 252)

def vpee_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, assets)
    return _rolling_kurt(base, 5)

def vpee_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, assets)
    return _rolling_kurt(base, 21)

def vpee_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, assets)
    return _rolling_kurt(base, 63)

def vpee_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, assets)
    return _rolling_kurt(base, 126)

def vpee_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, assets)
    return _rolling_kurt(base, 252)

def vpee_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, assets)
    return _safe_div(base, _rolling_std(base, 5))

def vpee_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, assets)
    return _safe_div(base, _rolling_std(base, 21))

def vpee_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, assets)
    return _safe_div(base, _rolling_std(base, 63))

def vpee_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, assets)
    return _safe_div(base, _rolling_std(base, 126))

def vpee_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, assets)
    return _safe_div(base, _rolling_std(base, 252))

def vpee_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, assets)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, assets)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, assets)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, assets)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, assets)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpee_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 5)

def vpee_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 21)

def vpee_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 63)

def vpee_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 126)

def vpee_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_mean(base, 252)

def vpee_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 5)

def vpee_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 21)

def vpee_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 63)

def vpee_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 126)

def vpee_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = _safe_div(marketcap, equity)
    return _zscore_rolling(base, 252)

def vpee_641_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 5)

def vpee_642_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 21)

def vpee_643_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 63)

def vpee_644_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 126)

def vpee_645_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 82 valuation vs peers to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(marketcap, equity)
    return _rank_pct(base, 252)

def vpee_646_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_skew(base, 5)

def vpee_647_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_skew(base, 21)

def vpee_648_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_skew(base, 63)

def vpee_649_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_skew(base, 126)

def vpee_650_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 82 valuation vs peers distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_skew(base, 252)

def vpee_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_kurt(base, 5)

def vpee_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_kurt(base, 21)

def vpee_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_kurt(base, 63)

def vpee_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_kurt(base, 126)

def vpee_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 82 valuation vs peers over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(marketcap, equity)
    return _rolling_kurt(base, 252)

def vpee_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(marketcap, equity)
    return _safe_div(base, _rolling_std(base, 5))

def vpee_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(marketcap, equity)
    return _safe_div(base, _rolling_std(base, 21))

def vpee_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(marketcap, equity)
    return _safe_div(base, _rolling_std(base, 63))

def vpee_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(marketcap, equity)
    return _safe_div(base, _rolling_std(base, 126))

def vpee_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 82 valuation vs peers for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(marketcap, equity)
    return _safe_div(base, _rolling_std(base, 252))

def vpee_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(marketcap, equity)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vpee_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(marketcap, equity)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vpee_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(marketcap, equity)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vpee_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(marketcap, equity)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vpee_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 82 valuation vs peers over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(marketcap, equity)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vpee_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_mean(base, 5)

def vpee_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_mean(base, 21)

def vpee_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_mean(base, 63)

def vpee_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_mean(base, 126)

def vpee_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 82 valuation vs peers over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(fcf, ocf)
    return _rolling_mean(base, 252)

def vpee_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 5d mean.
    """
    base = _safe_div(fcf, ocf)
    return _zscore_rolling(base, 5)

def vpee_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 21d mean.
    """
    base = _safe_div(fcf, ocf)
    return _zscore_rolling(base, 21)

def vpee_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 63d mean.
    """
    base = _safe_div(fcf, ocf)
    return _zscore_rolling(base, 63)

def vpee_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 126d mean.
    """
    base = _safe_div(fcf, ocf)
    return _zscore_rolling(base, 126)

def vpee_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 82 valuation vs peers by measuring deviations from the 252d mean.
    """
    base = _safe_div(fcf, ocf)
    return _zscore_rolling(base, 252)
