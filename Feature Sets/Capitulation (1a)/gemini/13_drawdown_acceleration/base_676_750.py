"""
13_13_drawdown_acceleration — Base Features 676-750
Domain: 13_drawdown_acceleration
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

def dacc_676_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def dacc_677_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def dacc_678_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def dacc_679_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def dacc_680_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def dacc_681_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def dacc_682_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def dacc_683_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def dacc_684_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def dacc_685_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def dacc_686_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def dacc_687_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def dacc_688_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def dacc_689_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def dacc_690_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def dacc_691_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dacc_692_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dacc_693_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dacc_694_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dacc_695_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dacc_696_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dacc_697_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dacc_698_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dacc_699_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dacc_700_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dacc_701_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def dacc_702_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def dacc_703_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def dacc_704_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def dacc_705_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def dacc_706_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def dacc_707_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def dacc_708_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def dacc_709_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def dacc_710_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def dacc_711_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def dacc_712_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def dacc_713_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def dacc_714_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def dacc_715_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def dacc_716_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def dacc_717_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def dacc_718_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def dacc_719_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def dacc_720_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def dacc_721_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def dacc_722_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def dacc_723_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def dacc_724_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def dacc_725_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def dacc_726_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dacc_727_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dacc_728_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dacc_729_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dacc_730_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dacc_731_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dacc_732_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dacc_733_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dacc_734_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dacc_735_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dacc_736_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def dacc_737_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def dacc_738_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def dacc_739_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def dacc_740_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def dacc_741_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def dacc_742_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def dacc_743_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def dacc_744_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def dacc_745_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def dacc_746_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def dacc_747_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def dacc_748_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def dacc_749_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def dacc_750_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
