"""
76_76_balance_sheet_decay — Base Features 601-675
Domain: 76_balance_sheet_decay
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

def bdec_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 5)

def bdec_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 21)

def bdec_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 63)

def bdec_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 126)

def bdec_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(90)
    return _zscore_rolling(base, 252)

def bdec_606_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 5)

def bdec_607_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 21)

def bdec_608_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 63)

def bdec_609_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 126)

def bdec_610_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(90)
    return _rank_pct(base, 252)

def bdec_611_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 5)

def bdec_612_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 21)

def bdec_613_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 63)

def bdec_614_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 126)

def bdec_615_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(90)
    return _rolling_skew(base, 252)

def bdec_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 5)

def bdec_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 21)

def bdec_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 63)

def bdec_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 126)

def bdec_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(90)
    return _rolling_kurt(base, 252)

def bdec_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(90)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(90)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 5)

def bdec_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 21)

def bdec_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 63)

def bdec_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 126)

def bdec_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(95)
    return _rolling_mean(base, 252)

def bdec_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 5)

def bdec_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 21)

def bdec_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 63)

def bdec_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 126)

def bdec_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(95)
    return _zscore_rolling(base, 252)

def bdec_641_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 5)

def bdec_642_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 21)

def bdec_643_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 63)

def bdec_644_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 126)

def bdec_645_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(95)
    return _rank_pct(base, 252)

def bdec_646_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 5)

def bdec_647_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 21)

def bdec_648_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 63)

def bdec_649_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 126)

def bdec_650_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(95)
    return _rolling_skew(base, 252)

def bdec_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 5)

def bdec_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 21)

def bdec_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 63)

def bdec_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 126)

def bdec_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(95)
    return _rolling_kurt(base, 252)

def bdec_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(95)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 5)

def bdec_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 21)

def bdec_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 63)

def bdec_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 126)

def bdec_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(100)
    return _rolling_mean(base, 252)

def bdec_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 5)

def bdec_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 21)

def bdec_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 63)

def bdec_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 126)

def bdec_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(100)
    return _zscore_rolling(base, 252)
