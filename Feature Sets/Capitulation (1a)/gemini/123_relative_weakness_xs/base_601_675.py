"""
123_123_relative_weakness_xs — Base Features 601-675
Domain: 123_relative_weakness_xs
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

def rwxs_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(360)
    return _zscore_rolling(base, 5)

def rwxs_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(360)
    return _zscore_rolling(base, 21)

def rwxs_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(360)
    return _zscore_rolling(base, 63)

def rwxs_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(360)
    return _zscore_rolling(base, 126)

def rwxs_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(360)
    return _zscore_rolling(base, 252)

def rwxs_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(360)
    return _rank_pct(base, 5)

def rwxs_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(360)
    return _rank_pct(base, 21)

def rwxs_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(360)
    return _rank_pct(base, 63)

def rwxs_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(360)
    return _rank_pct(base, 126)

def rwxs_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(360)
    return _rank_pct(base, 252)

def rwxs_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(360)
    return _rolling_skew(base, 5)

def rwxs_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(360)
    return _rolling_skew(base, 21)

def rwxs_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(360)
    return _rolling_skew(base, 63)

def rwxs_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(360)
    return _rolling_skew(base, 126)

def rwxs_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(360)
    return _rolling_skew(base, 252)

def rwxs_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(360)
    return _rolling_kurt(base, 5)

def rwxs_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(360)
    return _rolling_kurt(base, 21)

def rwxs_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(360)
    return _rolling_kurt(base, 63)

def rwxs_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(360)
    return _rolling_kurt(base, 126)

def rwxs_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(360)
    return _rolling_kurt(base, 252)

def rwxs_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(360)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(360)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(360)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(360)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(360)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(360)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(360)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(360)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(360)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(360)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(380)
    return _rolling_mean(base, 5)

def rwxs_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(380)
    return _rolling_mean(base, 21)

def rwxs_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(380)
    return _rolling_mean(base, 63)

def rwxs_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(380)
    return _rolling_mean(base, 126)

def rwxs_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(380)
    return _rolling_mean(base, 252)

def rwxs_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(380)
    return _zscore_rolling(base, 5)

def rwxs_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(380)
    return _zscore_rolling(base, 21)

def rwxs_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(380)
    return _zscore_rolling(base, 63)

def rwxs_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(380)
    return _zscore_rolling(base, 126)

def rwxs_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(380)
    return _zscore_rolling(base, 252)

def rwxs_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(380)
    return _rank_pct(base, 5)

def rwxs_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(380)
    return _rank_pct(base, 21)

def rwxs_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(380)
    return _rank_pct(base, 63)

def rwxs_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(380)
    return _rank_pct(base, 126)

def rwxs_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(380)
    return _rank_pct(base, 252)

def rwxs_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(380)
    return _rolling_skew(base, 5)

def rwxs_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(380)
    return _rolling_skew(base, 21)

def rwxs_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(380)
    return _rolling_skew(base, 63)

def rwxs_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(380)
    return _rolling_skew(base, 126)

def rwxs_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(380)
    return _rolling_skew(base, 252)

def rwxs_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(380)
    return _rolling_kurt(base, 5)

def rwxs_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(380)
    return _rolling_kurt(base, 21)

def rwxs_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(380)
    return _rolling_kurt(base, 63)

def rwxs_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(380)
    return _rolling_kurt(base, 126)

def rwxs_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(380)
    return _rolling_kurt(base, 252)

def rwxs_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(380)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(380)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(380)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(380)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(380)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(380)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(380)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(380)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(380)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(380)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(400)
    return _rolling_mean(base, 5)

def rwxs_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(400)
    return _rolling_mean(base, 21)

def rwxs_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(400)
    return _rolling_mean(base, 63)

def rwxs_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(400)
    return _rolling_mean(base, 126)

def rwxs_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(400)
    return _rolling_mean(base, 252)

def rwxs_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(400)
    return _zscore_rolling(base, 5)

def rwxs_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(400)
    return _zscore_rolling(base, 21)

def rwxs_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(400)
    return _zscore_rolling(base, 63)

def rwxs_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(400)
    return _zscore_rolling(base, 126)

def rwxs_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(400)
    return _zscore_rolling(base, 252)
