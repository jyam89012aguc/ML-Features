"""
118_118_drawdown_recovery_asymmetry — Base Features 601-675
Domain: 118_drawdown_recovery_asymmetry
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

def dras_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(180).skew()
    return _zscore_rolling(base, 5)

def dras_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(180).skew()
    return _zscore_rolling(base, 21)

def dras_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(180).skew()
    return _zscore_rolling(base, 63)

def dras_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(180).skew()
    return _zscore_rolling(base, 126)

def dras_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(180).skew()
    return _zscore_rolling(base, 252)

def dras_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(180).skew()
    return _rank_pct(base, 5)

def dras_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(180).skew()
    return _rank_pct(base, 21)

def dras_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(180).skew()
    return _rank_pct(base, 63)

def dras_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(180).skew()
    return _rank_pct(base, 126)

def dras_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(180).skew()
    return _rank_pct(base, 252)

def dras_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_skew(base, 5)

def dras_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_skew(base, 21)

def dras_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_skew(base, 63)

def dras_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_skew(base, 126)

def dras_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_skew(base, 252)

def dras_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_kurt(base, 5)

def dras_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_kurt(base, 21)

def dras_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_kurt(base, 63)

def dras_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_kurt(base, 126)

def dras_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(180).skew()
    return _rolling_kurt(base, 252)

def dras_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(180).skew()
    return _safe_div(base, _rolling_std(base, 5))

def dras_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(180).skew()
    return _safe_div(base, _rolling_std(base, 21))

def dras_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(180).skew()
    return _safe_div(base, _rolling_std(base, 63))

def dras_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(180).skew()
    return _safe_div(base, _rolling_std(base, 126))

def dras_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(180).skew()
    return _safe_div(base, _rolling_std(base, 252))

def dras_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(180).skew()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(180).skew()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(180).skew()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(180).skew()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(180).skew()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_mean(base, 5)

def dras_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_mean(base, 21)

def dras_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_mean(base, 63)

def dras_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_mean(base, 126)

def dras_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_mean(base, 252)

def dras_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(190).skew()
    return _zscore_rolling(base, 5)

def dras_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(190).skew()
    return _zscore_rolling(base, 21)

def dras_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(190).skew()
    return _zscore_rolling(base, 63)

def dras_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(190).skew()
    return _zscore_rolling(base, 126)

def dras_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(190).skew()
    return _zscore_rolling(base, 252)

def dras_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(190).skew()
    return _rank_pct(base, 5)

def dras_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(190).skew()
    return _rank_pct(base, 21)

def dras_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(190).skew()
    return _rank_pct(base, 63)

def dras_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(190).skew()
    return _rank_pct(base, 126)

def dras_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(190).skew()
    return _rank_pct(base, 252)

def dras_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_skew(base, 5)

def dras_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_skew(base, 21)

def dras_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_skew(base, 63)

def dras_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_skew(base, 126)

def dras_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_skew(base, 252)

def dras_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_kurt(base, 5)

def dras_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_kurt(base, 21)

def dras_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_kurt(base, 63)

def dras_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_kurt(base, 126)

def dras_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(190).skew()
    return _rolling_kurt(base, 252)

def dras_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(190).skew()
    return _safe_div(base, _rolling_std(base, 5))

def dras_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(190).skew()
    return _safe_div(base, _rolling_std(base, 21))

def dras_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(190).skew()
    return _safe_div(base, _rolling_std(base, 63))

def dras_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(190).skew()
    return _safe_div(base, _rolling_std(base, 126))

def dras_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(190).skew()
    return _safe_div(base, _rolling_std(base, 252))

def dras_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(190).skew()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(190).skew()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(190).skew()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(190).skew()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(190).skew()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(200).skew()
    return _rolling_mean(base, 5)

def dras_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(200).skew()
    return _rolling_mean(base, 21)

def dras_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(200).skew()
    return _rolling_mean(base, 63)

def dras_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(200).skew()
    return _rolling_mean(base, 126)

def dras_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(200).skew()
    return _rolling_mean(base, 252)

def dras_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(200).skew()
    return _zscore_rolling(base, 5)

def dras_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(200).skew()
    return _zscore_rolling(base, 21)

def dras_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(200).skew()
    return _zscore_rolling(base, 63)

def dras_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(200).skew()
    return _zscore_rolling(base, 126)

def dras_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(200).skew()
    return _zscore_rolling(base, 252)
