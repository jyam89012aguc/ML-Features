"""
124_124_cross_sectional_distress_rank — Base Features 601-675
Domain: 124_cross_sectional_distress_rank
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

def csdr_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _zscore_rolling(base, 5)

def csdr_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _zscore_rolling(base, 21)

def csdr_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _zscore_rolling(base, 63)

def csdr_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _zscore_rolling(base, 126)

def csdr_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _zscore_rolling(base, 252)

def csdr_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rank_pct(base, 5)

def csdr_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rank_pct(base, 21)

def csdr_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rank_pct(base, 63)

def csdr_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rank_pct(base, 126)

def csdr_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rank_pct(base, 252)

def csdr_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_skew(base, 5)

def csdr_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_skew(base, 21)

def csdr_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_skew(base, 63)

def csdr_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_skew(base, 126)

def csdr_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_skew(base, 252)

def csdr_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_kurt(base, 5)

def csdr_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_kurt(base, 21)

def csdr_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_kurt(base, 63)

def csdr_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_kurt(base, 126)

def csdr_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _rolling_kurt(base, 252)

def csdr_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(180), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_mean(base, 5)

def csdr_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_mean(base, 21)

def csdr_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_mean(base, 63)

def csdr_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_mean(base, 126)

def csdr_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_mean(base, 252)

def csdr_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _zscore_rolling(base, 5)

def csdr_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _zscore_rolling(base, 21)

def csdr_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _zscore_rolling(base, 63)

def csdr_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _zscore_rolling(base, 126)

def csdr_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _zscore_rolling(base, 252)

def csdr_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rank_pct(base, 5)

def csdr_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rank_pct(base, 21)

def csdr_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rank_pct(base, 63)

def csdr_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rank_pct(base, 126)

def csdr_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rank_pct(base, 252)

def csdr_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_skew(base, 5)

def csdr_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_skew(base, 21)

def csdr_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_skew(base, 63)

def csdr_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_skew(base, 126)

def csdr_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_skew(base, 252)

def csdr_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_kurt(base, 5)

def csdr_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_kurt(base, 21)

def csdr_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_kurt(base, 63)

def csdr_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_kurt(base, 126)

def csdr_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _rolling_kurt(base, 252)

def csdr_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(190), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_mean(base, 5)

def csdr_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_mean(base, 21)

def csdr_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_mean(base, 63)

def csdr_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_mean(base, 126)

def csdr_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_mean(base, 252)

def csdr_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _zscore_rolling(base, 5)

def csdr_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _zscore_rolling(base, 21)

def csdr_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _zscore_rolling(base, 63)

def csdr_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _zscore_rolling(base, 126)

def csdr_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _zscore_rolling(base, 252)
