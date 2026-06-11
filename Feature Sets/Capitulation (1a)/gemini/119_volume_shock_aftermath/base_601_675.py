"""
119_119_volume_shock_aftermath — Base Features 601-675
Domain: 119_volume_shock_aftermath
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

def vsha_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 180)
    return _zscore_rolling(base, 5)

def vsha_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 180)
    return _zscore_rolling(base, 21)

def vsha_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 180)
    return _zscore_rolling(base, 63)

def vsha_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 180)
    return _zscore_rolling(base, 126)

def vsha_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 180)
    return _zscore_rolling(base, 252)

def vsha_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rank_pct(base, 5)

def vsha_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rank_pct(base, 21)

def vsha_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rank_pct(base, 63)

def vsha_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rank_pct(base, 126)

def vsha_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rank_pct(base, 252)

def vsha_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_skew(base, 5)

def vsha_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_skew(base, 21)

def vsha_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_skew(base, 63)

def vsha_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_skew(base, 126)

def vsha_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_skew(base, 252)

def vsha_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_kurt(base, 5)

def vsha_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_kurt(base, 21)

def vsha_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_kurt(base, 63)

def vsha_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_kurt(base, 126)

def vsha_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_kurt(base, 252)

def vsha_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 180)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 180)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 180)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 180)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 180)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 180)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 180)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 180)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 180)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 180)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_mean(base, 5)

def vsha_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_mean(base, 21)

def vsha_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_mean(base, 63)

def vsha_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_mean(base, 126)

def vsha_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_mean(base, 252)

def vsha_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 190)
    return _zscore_rolling(base, 5)

def vsha_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 190)
    return _zscore_rolling(base, 21)

def vsha_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 190)
    return _zscore_rolling(base, 63)

def vsha_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 190)
    return _zscore_rolling(base, 126)

def vsha_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 190)
    return _zscore_rolling(base, 252)

def vsha_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rank_pct(base, 5)

def vsha_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rank_pct(base, 21)

def vsha_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rank_pct(base, 63)

def vsha_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rank_pct(base, 126)

def vsha_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rank_pct(base, 252)

def vsha_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_skew(base, 5)

def vsha_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_skew(base, 21)

def vsha_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_skew(base, 63)

def vsha_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_skew(base, 126)

def vsha_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_skew(base, 252)

def vsha_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_kurt(base, 5)

def vsha_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_kurt(base, 21)

def vsha_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_kurt(base, 63)

def vsha_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_kurt(base, 126)

def vsha_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 190)
    return _rolling_kurt(base, 252)

def vsha_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 190)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 190)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 190)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 190)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 190)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 190)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 190)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 190)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 190)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 190)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 200)
    return _rolling_mean(base, 5)

def vsha_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 200)
    return _rolling_mean(base, 21)

def vsha_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 200)
    return _rolling_mean(base, 63)

def vsha_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 200)
    return _rolling_mean(base, 126)

def vsha_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 200)
    return _rolling_mean(base, 252)

def vsha_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 200)
    return _zscore_rolling(base, 5)

def vsha_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 200)
    return _zscore_rolling(base, 21)

def vsha_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 200)
    return _zscore_rolling(base, 63)

def vsha_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 200)
    return _zscore_rolling(base, 126)

def vsha_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 200)
    return _zscore_rolling(base, 252)
