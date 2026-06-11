"""
75_75_guidance_distress — Base Features 601-675
Domain: 75_guidance_distress
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

def guid_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 5)

def guid_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 21)

def guid_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 63)

def guid_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 126)

def guid_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 252)

def guid_606_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 5)

def guid_607_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 21)

def guid_608_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 63)

def guid_609_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 126)

def guid_610_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 252)

def guid_611_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 5)

def guid_612_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 21)

def guid_613_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 63)

def guid_614_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 126)

def guid_615_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 252)

def guid_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 5)

def guid_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 21)

def guid_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 63)

def guid_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 126)

def guid_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 252)

def guid_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 5))

def guid_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 21))

def guid_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 63))

def guid_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 126))

def guid_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 252))

def guid_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def guid_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def guid_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def guid_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def guid_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def guid_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 5)

def guid_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 21)

def guid_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 63)

def guid_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 126)

def guid_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 252)

def guid_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 5)

def guid_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 21)

def guid_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 63)

def guid_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 126)

def guid_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 252)

def guid_641_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 5)

def guid_642_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 21)

def guid_643_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 63)

def guid_644_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 126)

def guid_645_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 252)

def guid_646_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 5)

def guid_647_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 21)

def guid_648_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 63)

def guid_649_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 126)

def guid_650_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 252)

def guid_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 5)

def guid_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 21)

def guid_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 63)

def guid_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 126)

def guid_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 252)

def guid_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 5))

def guid_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 21))

def guid_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 63))

def guid_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 126))

def guid_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 252))

def guid_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def guid_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def guid_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def guid_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def guid_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def guid_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 5)

def guid_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 21)

def guid_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 63)

def guid_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 126)

def guid_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 252)

def guid_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 5)

def guid_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 21)

def guid_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 63)

def guid_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 126)

def guid_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 252)
