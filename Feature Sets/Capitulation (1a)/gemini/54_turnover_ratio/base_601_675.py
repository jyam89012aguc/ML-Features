"""
54_54_turnover_ratio — Base Features 601-675
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

def turn_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def turn_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def turn_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def turn_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def turn_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def turn_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def turn_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def turn_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def turn_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def turn_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def turn_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def turn_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def turn_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def turn_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def turn_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def turn_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def turn_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def turn_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def turn_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def turn_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def turn_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def turn_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def turn_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def turn_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def turn_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def turn_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def turn_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def turn_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def turn_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def turn_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def turn_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def turn_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def turn_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def turn_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def turn_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def turn_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def turn_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def turn_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def turn_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def turn_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def turn_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def turn_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def turn_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def turn_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def turn_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 54 turnover ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def turn_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def turn_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def turn_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def turn_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def turn_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 54 turnover ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def turn_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def turn_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def turn_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def turn_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def turn_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 54 turnover ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def turn_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def turn_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def turn_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def turn_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def turn_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 54 turnover ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def turn_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def turn_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def turn_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def turn_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def turn_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 54 turnover ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def turn_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def turn_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def turn_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def turn_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def turn_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 54 turnover ratio over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def turn_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def turn_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def turn_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def turn_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def turn_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 54 turnover ratio by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
