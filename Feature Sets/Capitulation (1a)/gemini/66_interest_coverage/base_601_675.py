"""
66_66_interest_coverage — Base Features 601-675
Domain: 66_interest_coverage
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

def icov_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 5)

def icov_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 21)

def icov_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 63)

def icov_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 126)

def icov_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 252)

def icov_606_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 5)

def icov_607_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 21)

def icov_608_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 63)

def icov_609_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 126)

def icov_610_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 252)

def icov_611_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 5)

def icov_612_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 21)

def icov_613_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 63)

def icov_614_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 126)

def icov_615_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 252)

def icov_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 5)

def icov_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 21)

def icov_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 63)

def icov_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 126)

def icov_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 252)

def icov_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 5))

def icov_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 21))

def icov_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 63))

def icov_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 126))

def icov_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 252))

def icov_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 5)

def icov_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 21)

def icov_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 63)

def icov_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 126)

def icov_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 252)

def icov_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 5)

def icov_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 21)

def icov_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 63)

def icov_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 126)

def icov_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 252)

def icov_641_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 5)

def icov_642_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 21)

def icov_643_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 63)

def icov_644_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 126)

def icov_645_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 252)

def icov_646_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 5)

def icov_647_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 21)

def icov_648_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 63)

def icov_649_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 126)

def icov_650_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 252)

def icov_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 5)

def icov_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 21)

def icov_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 63)

def icov_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 126)

def icov_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 252)

def icov_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 5))

def icov_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 21))

def icov_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 63))

def icov_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 126))

def icov_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 252))

def icov_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 5)

def icov_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 21)

def icov_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 63)

def icov_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 126)

def icov_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 252)

def icov_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 5)

def icov_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 21)

def icov_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 63)

def icov_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 126)

def icov_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 252)
