"""
68_68_asset_quality — Base Features 601-675
Domain: 68_asset_quality
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

def aqal_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 5)

def aqal_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 21)

def aqal_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 63)

def aqal_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 126)

def aqal_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(90)
    return _zscore_rolling(base, 252)

def aqal_606_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 5)

def aqal_607_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 21)

def aqal_608_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 63)

def aqal_609_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 126)

def aqal_610_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(90)
    return _rank_pct(base, 252)

def aqal_611_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 5)

def aqal_612_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 21)

def aqal_613_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 63)

def aqal_614_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 126)

def aqal_615_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(90)
    return _rolling_skew(base, 252)

def aqal_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 5)

def aqal_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 21)

def aqal_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 63)

def aqal_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 126)

def aqal_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(90)
    return _rolling_kurt(base, 252)

def aqal_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 5))

def aqal_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 21))

def aqal_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 63))

def aqal_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 126))

def aqal_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(90)
    return _safe_div(base, _rolling_std(base, 252))

def aqal_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def aqal_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def aqal_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def aqal_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def aqal_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(90)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def aqal_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 5)

def aqal_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 21)

def aqal_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 63)

def aqal_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 126)

def aqal_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(95)
    return _rolling_mean(base, 252)

def aqal_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 5)

def aqal_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 21)

def aqal_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 63)

def aqal_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 126)

def aqal_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(95)
    return _zscore_rolling(base, 252)

def aqal_641_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 5)

def aqal_642_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 21)

def aqal_643_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 63)

def aqal_644_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 126)

def aqal_645_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(95)
    return _rank_pct(base, 252)

def aqal_646_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 5)

def aqal_647_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 21)

def aqal_648_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 63)

def aqal_649_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 126)

def aqal_650_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(95)
    return _rolling_skew(base, 252)

def aqal_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 5)

def aqal_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 21)

def aqal_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 63)

def aqal_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 126)

def aqal_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(95)
    return _rolling_kurt(base, 252)

def aqal_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 5))

def aqal_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 21))

def aqal_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 63))

def aqal_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 126))

def aqal_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(95)
    return _safe_div(base, _rolling_std(base, 252))

def aqal_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def aqal_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def aqal_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def aqal_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def aqal_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def aqal_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 5)

def aqal_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 21)

def aqal_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 63)

def aqal_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 126)

def aqal_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(100)
    return _rolling_mean(base, 252)

def aqal_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 5)

def aqal_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 21)

def aqal_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 63)

def aqal_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 126)

def aqal_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(100)
    return _zscore_rolling(base, 252)
