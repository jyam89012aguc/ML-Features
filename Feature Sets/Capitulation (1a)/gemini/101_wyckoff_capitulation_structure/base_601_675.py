"""
101_101_wyckoff_capitulation_structure — Base Features 601-675
Domain: 101_wyckoff_capitulation_structure
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

def wyck_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(18)
    return _zscore_rolling(base, 5)

def wyck_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(18)
    return _zscore_rolling(base, 21)

def wyck_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(18)
    return _zscore_rolling(base, 63)

def wyck_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(18)
    return _zscore_rolling(base, 126)

def wyck_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(18)
    return _zscore_rolling(base, 252)

def wyck_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(18)
    return _rank_pct(base, 5)

def wyck_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(18)
    return _rank_pct(base, 21)

def wyck_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(18)
    return _rank_pct(base, 63)

def wyck_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(18)
    return _rank_pct(base, 126)

def wyck_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(18)
    return _rank_pct(base, 252)

def wyck_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(18)
    return _rolling_skew(base, 5)

def wyck_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(18)
    return _rolling_skew(base, 21)

def wyck_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(18)
    return _rolling_skew(base, 63)

def wyck_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(18)
    return _rolling_skew(base, 126)

def wyck_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(18)
    return _rolling_skew(base, 252)

def wyck_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(18)
    return _rolling_kurt(base, 5)

def wyck_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(18)
    return _rolling_kurt(base, 21)

def wyck_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(18)
    return _rolling_kurt(base, 63)

def wyck_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(18)
    return _rolling_kurt(base, 126)

def wyck_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(18)
    return _rolling_kurt(base, 252)

def wyck_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(18)
    return _safe_div(base, _rolling_std(base, 5))

def wyck_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(18)
    return _safe_div(base, _rolling_std(base, 21))

def wyck_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(18)
    return _safe_div(base, _rolling_std(base, 63))

def wyck_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(18)
    return _safe_div(base, _rolling_std(base, 126))

def wyck_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(18)
    return _safe_div(base, _rolling_std(base, 252))

def wyck_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(18)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wyck_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(18)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wyck_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(18)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wyck_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(18)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wyck_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(18)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wyck_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(19)
    return _rolling_mean(base, 5)

def wyck_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(19)
    return _rolling_mean(base, 21)

def wyck_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(19)
    return _rolling_mean(base, 63)

def wyck_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(19)
    return _rolling_mean(base, 126)

def wyck_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(19)
    return _rolling_mean(base, 252)

def wyck_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(19)
    return _zscore_rolling(base, 5)

def wyck_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(19)
    return _zscore_rolling(base, 21)

def wyck_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(19)
    return _zscore_rolling(base, 63)

def wyck_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(19)
    return _zscore_rolling(base, 126)

def wyck_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(19)
    return _zscore_rolling(base, 252)

def wyck_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(19)
    return _rank_pct(base, 5)

def wyck_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(19)
    return _rank_pct(base, 21)

def wyck_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(19)
    return _rank_pct(base, 63)

def wyck_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(19)
    return _rank_pct(base, 126)

def wyck_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(19)
    return _rank_pct(base, 252)

def wyck_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(19)
    return _rolling_skew(base, 5)

def wyck_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(19)
    return _rolling_skew(base, 21)

def wyck_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(19)
    return _rolling_skew(base, 63)

def wyck_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(19)
    return _rolling_skew(base, 126)

def wyck_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(19)
    return _rolling_skew(base, 252)

def wyck_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(19)
    return _rolling_kurt(base, 5)

def wyck_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(19)
    return _rolling_kurt(base, 21)

def wyck_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(19)
    return _rolling_kurt(base, 63)

def wyck_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(19)
    return _rolling_kurt(base, 126)

def wyck_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(19)
    return _rolling_kurt(base, 252)

def wyck_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(19)
    return _safe_div(base, _rolling_std(base, 5))

def wyck_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(19)
    return _safe_div(base, _rolling_std(base, 21))

def wyck_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(19)
    return _safe_div(base, _rolling_std(base, 63))

def wyck_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(19)
    return _safe_div(base, _rolling_std(base, 126))

def wyck_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(19)
    return _safe_div(base, _rolling_std(base, 252))

def wyck_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(19)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wyck_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(19)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wyck_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(19)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wyck_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(19)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wyck_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(19)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wyck_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(20)
    return _rolling_mean(base, 5)

def wyck_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(20)
    return _rolling_mean(base, 21)

def wyck_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(20)
    return _rolling_mean(base, 63)

def wyck_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(20)
    return _rolling_mean(base, 126)

def wyck_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(20)
    return _rolling_mean(base, 252)

def wyck_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(20)
    return _zscore_rolling(base, 5)

def wyck_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(20)
    return _zscore_rolling(base, 21)

def wyck_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(20)
    return _zscore_rolling(base, 63)

def wyck_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(20)
    return _zscore_rolling(base, 126)

def wyck_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(20)
    return _zscore_rolling(base, 252)
