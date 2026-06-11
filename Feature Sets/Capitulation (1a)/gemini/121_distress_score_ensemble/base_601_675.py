"""
121_121_distress_score_ensemble — Base Features 601-675
Domain: 121_distress_score_ensemble
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

def dsen_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _zscore_rolling(base, 5)

def dsen_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _zscore_rolling(base, 21)

def dsen_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _zscore_rolling(base, 63)

def dsen_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _zscore_rolling(base, 126)

def dsen_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _zscore_rolling(base, 252)

def dsen_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rank_pct(base, 5)

def dsen_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rank_pct(base, 21)

def dsen_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rank_pct(base, 63)

def dsen_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rank_pct(base, 126)

def dsen_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rank_pct(base, 252)

def dsen_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_skew(base, 5)

def dsen_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_skew(base, 21)

def dsen_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_skew(base, 63)

def dsen_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_skew(base, 126)

def dsen_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_skew(base, 252)

def dsen_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_kurt(base, 5)

def dsen_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_kurt(base, 21)

def dsen_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_kurt(base, 63)

def dsen_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_kurt(base, 126)

def dsen_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_kurt(base, 252)

def dsen_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_mean(base, 5)

def dsen_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_mean(base, 21)

def dsen_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_mean(base, 63)

def dsen_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_mean(base, 126)

def dsen_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_mean(base, 252)

def dsen_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _zscore_rolling(base, 5)

def dsen_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _zscore_rolling(base, 21)

def dsen_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _zscore_rolling(base, 63)

def dsen_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _zscore_rolling(base, 126)

def dsen_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _zscore_rolling(base, 252)

def dsen_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rank_pct(base, 5)

def dsen_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rank_pct(base, 21)

def dsen_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rank_pct(base, 63)

def dsen_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rank_pct(base, 126)

def dsen_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rank_pct(base, 252)

def dsen_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_skew(base, 5)

def dsen_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_skew(base, 21)

def dsen_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_skew(base, 63)

def dsen_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_skew(base, 126)

def dsen_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_skew(base, 252)

def dsen_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_kurt(base, 5)

def dsen_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_kurt(base, 21)

def dsen_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_kurt(base, 63)

def dsen_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_kurt(base, 126)

def dsen_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _rolling_kurt(base, 252)

def dsen_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 190) + _zscore_rolling(volume, 190)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _rolling_mean(base, 5)

def dsen_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _rolling_mean(base, 21)

def dsen_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _rolling_mean(base, 63)

def dsen_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _rolling_mean(base, 126)

def dsen_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _rolling_mean(base, 252)

def dsen_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _zscore_rolling(base, 5)

def dsen_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _zscore_rolling(base, 21)

def dsen_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _zscore_rolling(base, 63)

def dsen_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _zscore_rolling(base, 126)

def dsen_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 200) + _zscore_rolling(volume, 200)) / 2
    return _zscore_rolling(base, 252)
