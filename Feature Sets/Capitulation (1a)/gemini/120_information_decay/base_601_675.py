"""
120_120_information_decay — Base Features 601-675
Domain: 120_information_decay
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

def idec_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(90).sum()
    return _zscore_rolling(base, 5)

def idec_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(90).sum()
    return _zscore_rolling(base, 21)

def idec_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(90).sum()
    return _zscore_rolling(base, 63)

def idec_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(90).sum()
    return _zscore_rolling(base, 126)

def idec_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(90).sum()
    return _zscore_rolling(base, 252)

def idec_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rank_pct(base, 5)

def idec_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rank_pct(base, 21)

def idec_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rank_pct(base, 63)

def idec_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rank_pct(base, 126)

def idec_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rank_pct(base, 252)

def idec_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_skew(base, 5)

def idec_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_skew(base, 21)

def idec_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_skew(base, 63)

def idec_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_skew(base, 126)

def idec_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_skew(base, 252)

def idec_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_kurt(base, 5)

def idec_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_kurt(base, 21)

def idec_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_kurt(base, 63)

def idec_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_kurt(base, 126)

def idec_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_kurt(base, 252)

def idec_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(90).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(90).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(90).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(90).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(90).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(90).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(90).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(90).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(90).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(90).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_mean(base, 5)

def idec_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_mean(base, 21)

def idec_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_mean(base, 63)

def idec_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_mean(base, 126)

def idec_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_mean(base, 252)

def idec_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(95).sum()
    return _zscore_rolling(base, 5)

def idec_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(95).sum()
    return _zscore_rolling(base, 21)

def idec_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(95).sum()
    return _zscore_rolling(base, 63)

def idec_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(95).sum()
    return _zscore_rolling(base, 126)

def idec_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(95).sum()
    return _zscore_rolling(base, 252)

def idec_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rank_pct(base, 5)

def idec_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rank_pct(base, 21)

def idec_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rank_pct(base, 63)

def idec_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rank_pct(base, 126)

def idec_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rank_pct(base, 252)

def idec_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_skew(base, 5)

def idec_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_skew(base, 21)

def idec_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_skew(base, 63)

def idec_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_skew(base, 126)

def idec_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_skew(base, 252)

def idec_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_kurt(base, 5)

def idec_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_kurt(base, 21)

def idec_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_kurt(base, 63)

def idec_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_kurt(base, 126)

def idec_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(95).sum()
    return _rolling_kurt(base, 252)

def idec_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(95).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(95).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(95).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(95).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(95).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(95).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(95).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(95).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(95).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(95).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(100).sum()
    return _rolling_mean(base, 5)

def idec_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(100).sum()
    return _rolling_mean(base, 21)

def idec_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(100).sum()
    return _rolling_mean(base, 63)

def idec_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(100).sum()
    return _rolling_mean(base, 126)

def idec_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(100).sum()
    return _rolling_mean(base, 252)

def idec_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(100).sum()
    return _zscore_rolling(base, 5)

def idec_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(100).sum()
    return _zscore_rolling(base, 21)

def idec_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(100).sum()
    return _zscore_rolling(base, 63)

def idec_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(100).sum()
    return _zscore_rolling(base, 126)

def idec_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(100).sum()
    return _zscore_rolling(base, 252)
