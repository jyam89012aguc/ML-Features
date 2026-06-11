"""
104_104_mean_reversion_potential — Base Features 601-675
Domain: 104_mean_reversion_potential
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

def mrpt_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _zscore_rolling(base, 5)

def mrpt_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _zscore_rolling(base, 21)

def mrpt_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _zscore_rolling(base, 63)

def mrpt_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _zscore_rolling(base, 126)

def mrpt_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _zscore_rolling(base, 252)

def mrpt_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rank_pct(base, 5)

def mrpt_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rank_pct(base, 21)

def mrpt_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rank_pct(base, 63)

def mrpt_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rank_pct(base, 126)

def mrpt_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rank_pct(base, 252)

def mrpt_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_skew(base, 5)

def mrpt_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_skew(base, 21)

def mrpt_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_skew(base, 63)

def mrpt_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_skew(base, 126)

def mrpt_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_skew(base, 252)

def mrpt_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_kurt(base, 5)

def mrpt_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_kurt(base, 21)

def mrpt_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_kurt(base, 63)

def mrpt_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_kurt(base, 126)

def mrpt_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_kurt(base, 252)

def mrpt_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 345) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 345) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 345) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 345) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 345) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_mean(base, 5)

def mrpt_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_mean(base, 21)

def mrpt_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_mean(base, 63)

def mrpt_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_mean(base, 126)

def mrpt_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_mean(base, 252)

def mrpt_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _zscore_rolling(base, 5)

def mrpt_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _zscore_rolling(base, 21)

def mrpt_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _zscore_rolling(base, 63)

def mrpt_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _zscore_rolling(base, 126)

def mrpt_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _zscore_rolling(base, 252)

def mrpt_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rank_pct(base, 5)

def mrpt_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rank_pct(base, 21)

def mrpt_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rank_pct(base, 63)

def mrpt_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rank_pct(base, 126)

def mrpt_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rank_pct(base, 252)

def mrpt_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_skew(base, 5)

def mrpt_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_skew(base, 21)

def mrpt_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_skew(base, 63)

def mrpt_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_skew(base, 126)

def mrpt_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_skew(base, 252)

def mrpt_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_kurt(base, 5)

def mrpt_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_kurt(base, 21)

def mrpt_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_kurt(base, 63)

def mrpt_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_kurt(base, 126)

def mrpt_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _rolling_kurt(base, 252)

def mrpt_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 365) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 365) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 365) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 365) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 365) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 365) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_mean(base, 5)

def mrpt_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_mean(base, 21)

def mrpt_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_mean(base, 63)

def mrpt_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_mean(base, 126)

def mrpt_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_mean(base, 252)

def mrpt_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _zscore_rolling(base, 5)

def mrpt_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _zscore_rolling(base, 21)

def mrpt_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _zscore_rolling(base, 63)

def mrpt_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _zscore_rolling(base, 126)

def mrpt_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _zscore_rolling(base, 252)
