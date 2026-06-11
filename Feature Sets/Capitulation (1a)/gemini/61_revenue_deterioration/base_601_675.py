"""
61_61_revenue_deterioration — Base Features 601-675
Domain: 61_revenue_deterioration
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

def rdet_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(90)
    return _zscore_rolling(base, 5)

def rdet_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(90)
    return _zscore_rolling(base, 21)

def rdet_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(90)
    return _zscore_rolling(base, 63)

def rdet_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(90)
    return _zscore_rolling(base, 126)

def rdet_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(90)
    return _zscore_rolling(base, 252)

def rdet_606_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(90)
    return _rank_pct(base, 5)

def rdet_607_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(90)
    return _rank_pct(base, 21)

def rdet_608_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(90)
    return _rank_pct(base, 63)

def rdet_609_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(90)
    return _rank_pct(base, 126)

def rdet_610_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(90)
    return _rank_pct(base, 252)

def rdet_611_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(90)
    return _rolling_skew(base, 5)

def rdet_612_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(90)
    return _rolling_skew(base, 21)

def rdet_613_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(90)
    return _rolling_skew(base, 63)

def rdet_614_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(90)
    return _rolling_skew(base, 126)

def rdet_615_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(90)
    return _rolling_skew(base, 252)

def rdet_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(90)
    return _rolling_kurt(base, 5)

def rdet_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(90)
    return _rolling_kurt(base, 21)

def rdet_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(90)
    return _rolling_kurt(base, 63)

def rdet_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(90)
    return _rolling_kurt(base, 126)

def rdet_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(90)
    return _rolling_kurt(base, 252)

def rdet_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(90)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(90)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(90)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(90)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(90)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(90)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(90)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(90)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(90)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(90)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(95)
    return _rolling_mean(base, 5)

def rdet_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(95)
    return _rolling_mean(base, 21)

def rdet_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(95)
    return _rolling_mean(base, 63)

def rdet_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(95)
    return _rolling_mean(base, 126)

def rdet_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(95)
    return _rolling_mean(base, 252)

def rdet_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(95)
    return _zscore_rolling(base, 5)

def rdet_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(95)
    return _zscore_rolling(base, 21)

def rdet_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(95)
    return _zscore_rolling(base, 63)

def rdet_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(95)
    return _zscore_rolling(base, 126)

def rdet_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(95)
    return _zscore_rolling(base, 252)

def rdet_641_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(95)
    return _rank_pct(base, 5)

def rdet_642_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(95)
    return _rank_pct(base, 21)

def rdet_643_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(95)
    return _rank_pct(base, 63)

def rdet_644_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(95)
    return _rank_pct(base, 126)

def rdet_645_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(95)
    return _rank_pct(base, 252)

def rdet_646_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(95)
    return _rolling_skew(base, 5)

def rdet_647_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(95)
    return _rolling_skew(base, 21)

def rdet_648_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(95)
    return _rolling_skew(base, 63)

def rdet_649_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(95)
    return _rolling_skew(base, 126)

def rdet_650_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(95)
    return _rolling_skew(base, 252)

def rdet_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(95)
    return _rolling_kurt(base, 5)

def rdet_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(95)
    return _rolling_kurt(base, 21)

def rdet_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(95)
    return _rolling_kurt(base, 63)

def rdet_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(95)
    return _rolling_kurt(base, 126)

def rdet_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(95)
    return _rolling_kurt(base, 252)

def rdet_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(95)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(95)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(95)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(95)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(95)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(100)
    return _rolling_mean(base, 5)

def rdet_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(100)
    return _rolling_mean(base, 21)

def rdet_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(100)
    return _rolling_mean(base, 63)

def rdet_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(100)
    return _rolling_mean(base, 126)

def rdet_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(100)
    return _rolling_mean(base, 252)

def rdet_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(100)
    return _zscore_rolling(base, 5)

def rdet_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(100)
    return _zscore_rolling(base, 21)

def rdet_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(100)
    return _zscore_rolling(base, 63)

def rdet_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(100)
    return _zscore_rolling(base, 126)

def rdet_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(100)
    return _zscore_rolling(base, 252)
