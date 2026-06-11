"""
02_02_drawdown_duration — Base Features 601-675
Domain: 02_drawdown_duration
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

def ddur_601_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def ddur_602_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def ddur_603_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def ddur_604_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def ddur_605_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def ddur_606_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def ddur_607_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def ddur_608_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def ddur_609_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def ddur_610_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def ddur_611_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def ddur_612_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def ddur_613_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def ddur_614_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def ddur_615_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def ddur_616_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def ddur_617_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def ddur_618_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def ddur_619_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def ddur_620_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def ddur_621_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ddur_622_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ddur_623_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ddur_624_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ddur_625_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ddur_626_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ddur_627_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ddur_628_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ddur_629_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ddur_630_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ddur_631_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def ddur_632_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def ddur_633_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def ddur_634_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def ddur_635_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def ddur_636_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def ddur_637_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def ddur_638_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def ddur_639_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def ddur_640_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def ddur_641_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def ddur_642_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def ddur_643_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def ddur_644_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def ddur_645_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 02 drawdown duration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def ddur_646_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def ddur_647_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def ddur_648_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def ddur_649_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def ddur_650_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 02 drawdown duration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def ddur_651_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def ddur_652_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def ddur_653_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def ddur_654_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def ddur_655_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 02 drawdown duration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def ddur_656_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ddur_657_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ddur_658_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ddur_659_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ddur_660_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 02 drawdown duration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ddur_661_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ddur_662_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ddur_663_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ddur_664_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ddur_665_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 02 drawdown duration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ddur_666_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def ddur_667_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def ddur_668_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def ddur_669_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def ddur_670_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 02 drawdown duration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def ddur_671_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def ddur_672_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def ddur_673_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def ddur_674_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def ddur_675_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 02 drawdown duration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
