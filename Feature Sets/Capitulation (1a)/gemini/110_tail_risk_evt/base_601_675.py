"""
110_110_tail_risk_evt — Base Features 601-675
Domain: 110_tail_risk_evt
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

def trev_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rank_pct(base, 5)

def trev_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rank_pct(base, 21)

def trev_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rank_pct(base, 63)

def trev_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rank_pct(base, 126)

def trev_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rank_pct(base, 252)

def trev_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rank_pct(base, 5)

def trev_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rank_pct(base, 21)

def trev_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rank_pct(base, 63)

def trev_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rank_pct(base, 126)

def trev_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rank_pct(base, 252)

def trev_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(950).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(1000).quantile(0.01)
    return _zscore_rolling(base, 252)
