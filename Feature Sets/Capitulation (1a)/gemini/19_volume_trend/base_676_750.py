"""
19_19_volume_trend — Base Features 676-750
Domain: 19_volume_trend
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

def vtr_676_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def vtr_677_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def vtr_678_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def vtr_679_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def vtr_680_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def vtr_681_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def vtr_682_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def vtr_683_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def vtr_684_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def vtr_685_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def vtr_686_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def vtr_687_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def vtr_688_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def vtr_689_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def vtr_690_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def vtr_691_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vtr_692_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vtr_693_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vtr_694_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vtr_695_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vtr_696_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vtr_697_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vtr_698_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vtr_699_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vtr_700_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vtr_701_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def vtr_702_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def vtr_703_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def vtr_704_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def vtr_705_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def vtr_706_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def vtr_707_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def vtr_708_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def vtr_709_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def vtr_710_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def vtr_711_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def vtr_712_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def vtr_713_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def vtr_714_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def vtr_715_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def vtr_716_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def vtr_717_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def vtr_718_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def vtr_719_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def vtr_720_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 19 volume trend distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def vtr_721_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def vtr_722_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def vtr_723_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def vtr_724_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def vtr_725_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 19 volume trend over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def vtr_726_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vtr_727_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vtr_728_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vtr_729_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vtr_730_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 19 volume trend for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vtr_731_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vtr_732_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vtr_733_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vtr_734_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vtr_735_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 19 volume trend over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vtr_736_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def vtr_737_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def vtr_738_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def vtr_739_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def vtr_740_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 19 volume trend over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def vtr_741_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def vtr_742_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def vtr_743_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def vtr_744_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def vtr_745_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 19 volume trend by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def vtr_746_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def vtr_747_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def vtr_748_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def vtr_749_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def vtr_750_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 19 volume trend to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
