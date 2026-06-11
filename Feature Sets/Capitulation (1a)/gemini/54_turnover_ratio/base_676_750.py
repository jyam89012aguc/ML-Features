"""
54_54_turnover_ratio — Base Features 676-750
Domain: 54_turnover_ratio
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

def turn_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def turn_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def turn_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def turn_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def turn_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def turn_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def turn_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def turn_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def turn_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def turn_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def turn_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def turn_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def turn_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def turn_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def turn_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def turn_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def turn_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def turn_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def turn_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def turn_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def turn_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def turn_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def turn_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def turn_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def turn_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def turn_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def turn_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def turn_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def turn_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def turn_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def turn_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def turn_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def turn_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def turn_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def turn_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def turn_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def turn_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def turn_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def turn_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def turn_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def turn_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def turn_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def turn_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def turn_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def turn_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def turn_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def turn_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def turn_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def turn_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def turn_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def turn_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def turn_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def turn_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def turn_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def turn_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def turn_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def turn_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def turn_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def turn_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def turn_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def turn_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def turn_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def turn_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def turn_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def turn_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def turn_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def turn_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def turn_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def turn_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def turn_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def turn_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def turn_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def turn_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def turn_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def turn_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
