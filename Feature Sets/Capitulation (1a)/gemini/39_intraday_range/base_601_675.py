"""
39_39_intraday_range — Base Features 601-675
Domain: 39_intraday_range
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

def iran_601_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def iran_602_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def iran_603_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def iran_604_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def iran_605_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def iran_606_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def iran_607_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def iran_608_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def iran_609_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def iran_610_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def iran_611_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def iran_612_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def iran_613_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def iran_614_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def iran_615_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def iran_616_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def iran_617_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def iran_618_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def iran_619_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def iran_620_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def iran_621_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def iran_622_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def iran_623_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def iran_624_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def iran_625_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def iran_626_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def iran_627_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def iran_628_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def iran_629_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def iran_630_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def iran_631_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def iran_632_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def iran_633_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def iran_634_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def iran_635_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def iran_636_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def iran_637_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def iran_638_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def iran_639_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def iran_640_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def iran_641_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def iran_642_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def iran_643_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def iran_644_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def iran_645_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 39 intraday range to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def iran_646_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def iran_647_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def iran_648_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def iran_649_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def iran_650_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 39 intraday range distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def iran_651_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def iran_652_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def iran_653_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def iran_654_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def iran_655_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 39 intraday range over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def iran_656_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def iran_657_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def iran_658_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def iran_659_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def iran_660_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 39 intraday range for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def iran_661_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def iran_662_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def iran_663_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def iran_664_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def iran_665_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 39 intraday range over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def iran_666_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def iran_667_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def iran_668_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def iran_669_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def iran_670_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 39 intraday range over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def iran_671_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def iran_672_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def iran_673_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def iran_674_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def iran_675_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 39 intraday range by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
