"""
102_102_seasonal_distress — Base Features 601-675
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

def seas_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(90)
    return _zscore_rolling(base, 5)

def seas_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(90)
    return _zscore_rolling(base, 21)

def seas_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(90)
    return _zscore_rolling(base, 63)

def seas_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(90)
    return _zscore_rolling(base, 126)

def seas_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(90)
    return _zscore_rolling(base, 252)

def seas_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(90)
    return _rank_pct(base, 5)

def seas_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(90)
    return _rank_pct(base, 21)

def seas_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(90)
    return _rank_pct(base, 63)

def seas_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(90)
    return _rank_pct(base, 126)

def seas_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(90)
    return _rank_pct(base, 252)

def seas_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(90)
    return _rolling_skew(base, 5)

def seas_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(90)
    return _rolling_skew(base, 21)

def seas_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(90)
    return _rolling_skew(base, 63)

def seas_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(90)
    return _rolling_skew(base, 126)

def seas_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(90)
    return _rolling_skew(base, 252)

def seas_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(90)
    return _rolling_kurt(base, 5)

def seas_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(90)
    return _rolling_kurt(base, 21)

def seas_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(90)
    return _rolling_kurt(base, 63)

def seas_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(90)
    return _rolling_kurt(base, 126)

def seas_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(90)
    return _rolling_kurt(base, 252)

def seas_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(90)
    return _safe_div(base, _rolling_std(base, 5))

def seas_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(90)
    return _safe_div(base, _rolling_std(base, 21))

def seas_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(90)
    return _safe_div(base, _rolling_std(base, 63))

def seas_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(90)
    return _safe_div(base, _rolling_std(base, 126))

def seas_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(90)
    return _safe_div(base, _rolling_std(base, 252))

def seas_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(90)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(90)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(90)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(90)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(90)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(95)
    return _rolling_mean(base, 5)

def seas_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(95)
    return _rolling_mean(base, 21)

def seas_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(95)
    return _rolling_mean(base, 63)

def seas_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(95)
    return _rolling_mean(base, 126)

def seas_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(95)
    return _rolling_mean(base, 252)

def seas_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(95)
    return _zscore_rolling(base, 5)

def seas_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(95)
    return _zscore_rolling(base, 21)

def seas_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(95)
    return _zscore_rolling(base, 63)

def seas_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(95)
    return _zscore_rolling(base, 126)

def seas_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(95)
    return _zscore_rolling(base, 252)

def seas_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(95)
    return _rank_pct(base, 5)

def seas_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(95)
    return _rank_pct(base, 21)

def seas_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(95)
    return _rank_pct(base, 63)

def seas_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(95)
    return _rank_pct(base, 126)

def seas_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(95)
    return _rank_pct(base, 252)

def seas_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(95)
    return _rolling_skew(base, 5)

def seas_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(95)
    return _rolling_skew(base, 21)

def seas_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(95)
    return _rolling_skew(base, 63)

def seas_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(95)
    return _rolling_skew(base, 126)

def seas_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(95)
    return _rolling_skew(base, 252)

def seas_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(95)
    return _rolling_kurt(base, 5)

def seas_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(95)
    return _rolling_kurt(base, 21)

def seas_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(95)
    return _rolling_kurt(base, 63)

def seas_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(95)
    return _rolling_kurt(base, 126)

def seas_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(95)
    return _rolling_kurt(base, 252)

def seas_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(95)
    return _safe_div(base, _rolling_std(base, 5))

def seas_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(95)
    return _safe_div(base, _rolling_std(base, 21))

def seas_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(95)
    return _safe_div(base, _rolling_std(base, 63))

def seas_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(95)
    return _safe_div(base, _rolling_std(base, 126))

def seas_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(95)
    return _safe_div(base, _rolling_std(base, 252))

def seas_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 5)

def seas_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 21)

def seas_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 63)

def seas_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 126)

def seas_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 252)

def seas_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 5)

def seas_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 21)

def seas_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 63)

def seas_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 126)

def seas_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 252)
