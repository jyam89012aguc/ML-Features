"""
108_108_drawdown_history_rank — Base Features 601-675
Domain: 108_drawdown_history_rank
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

def dhrk_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(360).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(360).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(360).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(360).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(360).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rank_pct(base, 5)

def dhrk_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rank_pct(base, 21)

def dhrk_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rank_pct(base, 63)

def dhrk_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rank_pct(base, 126)

def dhrk_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rank_pct(base, 252)

def dhrk_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(360).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(360).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(360).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(360).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(360).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(360).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(360).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(360).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(360).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(360).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(360).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(380).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(380).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(380).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(380).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(380).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rank_pct(base, 5)

def dhrk_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rank_pct(base, 21)

def dhrk_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rank_pct(base, 63)

def dhrk_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rank_pct(base, 126)

def dhrk_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rank_pct(base, 252)

def dhrk_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(380).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(380).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(380).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(380).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(380).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(380).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(380).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(380).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(380).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(380).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(380).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(400).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(400).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(400).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(400).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(400).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(400).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(400).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(400).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(400).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(400).max() - 1)
    return _zscore_rolling(base, 252)
