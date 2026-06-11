"""
59_59_market_impact_proxy — Base Features 601-675
Domain: 59_market_impact_proxy
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

def mimp_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def mimp_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def mimp_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def mimp_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def mimp_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def mimp_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def mimp_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def mimp_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def mimp_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def mimp_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def mimp_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def mimp_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def mimp_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def mimp_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def mimp_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def mimp_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def mimp_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def mimp_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def mimp_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def mimp_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def mimp_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def mimp_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def mimp_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def mimp_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def mimp_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def mimp_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def mimp_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def mimp_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def mimp_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def mimp_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def mimp_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def mimp_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def mimp_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def mimp_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def mimp_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def mimp_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def mimp_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def mimp_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def mimp_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def mimp_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def mimp_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def mimp_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def mimp_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def mimp_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def mimp_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def mimp_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def mimp_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def mimp_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def mimp_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def mimp_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def mimp_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def mimp_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def mimp_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def mimp_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def mimp_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
