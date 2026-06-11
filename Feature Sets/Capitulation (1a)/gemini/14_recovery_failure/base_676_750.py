"""
14_14_recovery_failure — Base Features 676-750
Domain: 14_recovery_failure
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

def rfl_676_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def rfl_677_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def rfl_678_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def rfl_679_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def rfl_680_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def rfl_681_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def rfl_682_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def rfl_683_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def rfl_684_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def rfl_685_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def rfl_686_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def rfl_687_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def rfl_688_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def rfl_689_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def rfl_690_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def rfl_691_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rfl_692_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rfl_693_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rfl_694_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rfl_695_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rfl_696_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rfl_697_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rfl_698_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rfl_699_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rfl_700_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rfl_701_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def rfl_702_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def rfl_703_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def rfl_704_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def rfl_705_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def rfl_706_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def rfl_707_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def rfl_708_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def rfl_709_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def rfl_710_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def rfl_711_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def rfl_712_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def rfl_713_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def rfl_714_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def rfl_715_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def rfl_716_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def rfl_717_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def rfl_718_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def rfl_719_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def rfl_720_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 14 recovery failure distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def rfl_721_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def rfl_722_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def rfl_723_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def rfl_724_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def rfl_725_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 14 recovery failure over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def rfl_726_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rfl_727_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rfl_728_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rfl_729_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rfl_730_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 14 recovery failure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rfl_731_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rfl_732_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rfl_733_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rfl_734_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rfl_735_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 14 recovery failure over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rfl_736_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def rfl_737_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def rfl_738_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def rfl_739_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def rfl_740_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 14 recovery failure over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def rfl_741_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def rfl_742_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def rfl_743_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def rfl_744_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def rfl_745_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 14 recovery failure by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def rfl_746_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def rfl_747_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def rfl_748_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def rfl_749_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def rfl_750_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 14 recovery failure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
