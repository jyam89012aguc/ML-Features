"""
31_31_oscillator_extremes — Base Features 676-750
Domain: 31_oscillator_extremes
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

def osce_676_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def osce_677_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def osce_678_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def osce_679_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def osce_680_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def osce_681_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def osce_682_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def osce_683_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def osce_684_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def osce_685_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def osce_686_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def osce_687_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def osce_688_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def osce_689_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def osce_690_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def osce_691_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def osce_692_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def osce_693_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def osce_694_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def osce_695_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def osce_696_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def osce_697_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def osce_698_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def osce_699_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def osce_700_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def osce_701_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def osce_702_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def osce_703_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def osce_704_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def osce_705_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def osce_706_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def osce_707_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def osce_708_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def osce_709_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def osce_710_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def osce_711_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def osce_712_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def osce_713_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def osce_714_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def osce_715_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def osce_716_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def osce_717_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def osce_718_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def osce_719_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def osce_720_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 31 oscillator extremes distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def osce_721_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def osce_722_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def osce_723_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def osce_724_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def osce_725_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 31 oscillator extremes over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def osce_726_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def osce_727_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def osce_728_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def osce_729_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def osce_730_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 31 oscillator extremes for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def osce_731_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def osce_732_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def osce_733_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def osce_734_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def osce_735_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 31 oscillator extremes over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def osce_736_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def osce_737_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def osce_738_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def osce_739_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def osce_740_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 31 oscillator extremes over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def osce_741_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def osce_742_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def osce_743_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def osce_744_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def osce_745_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 31 oscillator extremes by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def osce_746_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def osce_747_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def osce_748_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def osce_749_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def osce_750_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 31 oscillator extremes to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
