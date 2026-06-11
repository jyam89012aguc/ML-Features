"""
102_102_seasonal_distress — Base Features 676-750
Domain: 102_seasonal_distress
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

def seas_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(100)
    return _rank_pct(base, 5)

def seas_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(100)
    return _rank_pct(base, 21)

def seas_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(100)
    return _rank_pct(base, 63)

def seas_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(100)
    return _rank_pct(base, 126)

def seas_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(100)
    return _rank_pct(base, 252)

def seas_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(100)
    return _rolling_skew(base, 5)

def seas_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(100)
    return _rolling_skew(base, 21)

def seas_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(100)
    return _rolling_skew(base, 63)

def seas_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(100)
    return _rolling_skew(base, 126)

def seas_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(100)
    return _rolling_skew(base, 252)

def seas_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(100)
    return _rolling_kurt(base, 5)

def seas_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(100)
    return _rolling_kurt(base, 21)

def seas_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(100)
    return _rolling_kurt(base, 63)

def seas_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(100)
    return _rolling_kurt(base, 126)

def seas_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(100)
    return _rolling_kurt(base, 252)

def seas_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(100)
    return _safe_div(base, _rolling_std(base, 5))

def seas_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(100)
    return _safe_div(base, _rolling_std(base, 21))

def seas_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(100)
    return _safe_div(base, _rolling_std(base, 63))

def seas_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(100)
    return _safe_div(base, _rolling_std(base, 126))

def seas_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(100)
    return _safe_div(base, _rolling_std(base, 252))

def seas_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(100)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(100)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(100)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(100)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(100)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(105)
    return _rolling_mean(base, 5)

def seas_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(105)
    return _rolling_mean(base, 21)

def seas_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(105)
    return _rolling_mean(base, 63)

def seas_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(105)
    return _rolling_mean(base, 126)

def seas_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(105)
    return _rolling_mean(base, 252)

def seas_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(105)
    return _zscore_rolling(base, 5)

def seas_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(105)
    return _zscore_rolling(base, 21)

def seas_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(105)
    return _zscore_rolling(base, 63)

def seas_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(105)
    return _zscore_rolling(base, 126)

def seas_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(105)
    return _zscore_rolling(base, 252)

def seas_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(105)
    return _rank_pct(base, 5)

def seas_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(105)
    return _rank_pct(base, 21)

def seas_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(105)
    return _rank_pct(base, 63)

def seas_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(105)
    return _rank_pct(base, 126)

def seas_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(105)
    return _rank_pct(base, 252)

def seas_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(105)
    return _rolling_skew(base, 5)

def seas_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(105)
    return _rolling_skew(base, 21)

def seas_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(105)
    return _rolling_skew(base, 63)

def seas_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(105)
    return _rolling_skew(base, 126)

def seas_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(105)
    return _rolling_skew(base, 252)

def seas_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(105)
    return _rolling_kurt(base, 5)

def seas_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(105)
    return _rolling_kurt(base, 21)

def seas_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(105)
    return _rolling_kurt(base, 63)

def seas_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(105)
    return _rolling_kurt(base, 126)

def seas_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(105)
    return _rolling_kurt(base, 252)

def seas_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(105)
    return _safe_div(base, _rolling_std(base, 5))

def seas_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(105)
    return _safe_div(base, _rolling_std(base, 21))

def seas_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(105)
    return _safe_div(base, _rolling_std(base, 63))

def seas_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(105)
    return _safe_div(base, _rolling_std(base, 126))

def seas_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(105)
    return _safe_div(base, _rolling_std(base, 252))

def seas_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(105)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(105)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(105)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(105)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(105)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(110)
    return _rolling_mean(base, 5)

def seas_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(110)
    return _rolling_mean(base, 21)

def seas_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(110)
    return _rolling_mean(base, 63)

def seas_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(110)
    return _rolling_mean(base, 126)

def seas_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(110)
    return _rolling_mean(base, 252)

def seas_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(110)
    return _zscore_rolling(base, 5)

def seas_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(110)
    return _zscore_rolling(base, 21)

def seas_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(110)
    return _zscore_rolling(base, 63)

def seas_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(110)
    return _zscore_rolling(base, 126)

def seas_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(110)
    return _zscore_rolling(base, 252)

def seas_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(110)
    return _rank_pct(base, 5)

def seas_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(110)
    return _rank_pct(base, 21)

def seas_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(110)
    return _rank_pct(base, 63)

def seas_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(110)
    return _rank_pct(base, 126)

def seas_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(110)
    return _rank_pct(base, 252)
