"""
23_23_dollar_volume_shock — Base Features 601-675
Domain: 23_dollar_volume_shock
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

def dvsh_601_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def dvsh_602_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def dvsh_603_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def dvsh_604_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def dvsh_605_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def dvsh_606_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def dvsh_607_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def dvsh_608_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def dvsh_609_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def dvsh_610_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def dvsh_611_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def dvsh_612_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def dvsh_613_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def dvsh_614_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def dvsh_615_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def dvsh_616_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def dvsh_617_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def dvsh_618_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def dvsh_619_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def dvsh_620_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def dvsh_621_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvsh_622_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvsh_623_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvsh_624_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvsh_625_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvsh_626_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvsh_627_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvsh_628_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvsh_629_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvsh_630_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvsh_631_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def dvsh_632_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def dvsh_633_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def dvsh_634_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def dvsh_635_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def dvsh_636_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def dvsh_637_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def dvsh_638_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def dvsh_639_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def dvsh_640_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def dvsh_641_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def dvsh_642_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def dvsh_643_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def dvsh_644_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def dvsh_645_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def dvsh_646_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def dvsh_647_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def dvsh_648_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def dvsh_649_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def dvsh_650_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def dvsh_651_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def dvsh_652_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def dvsh_653_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def dvsh_654_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def dvsh_655_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def dvsh_656_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvsh_657_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvsh_658_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvsh_659_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvsh_660_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvsh_661_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvsh_662_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvsh_663_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvsh_664_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvsh_665_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvsh_666_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def dvsh_667_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def dvsh_668_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def dvsh_669_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def dvsh_670_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def dvsh_671_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def dvsh_672_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def dvsh_673_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def dvsh_674_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def dvsh_675_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
