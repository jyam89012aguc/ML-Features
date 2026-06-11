"""
121_121_distress_score_ensemble — Base Features 076-150
Domain: 121_distress_score_ensemble
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

def dsen_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _zscore_rolling(base, 5)

def dsen_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _zscore_rolling(base, 21)

def dsen_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _zscore_rolling(base, 63)

def dsen_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _zscore_rolling(base, 126)

def dsen_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _zscore_rolling(base, 252)

def dsen_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rank_pct(base, 5)

def dsen_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rank_pct(base, 21)

def dsen_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rank_pct(base, 63)

def dsen_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rank_pct(base, 126)

def dsen_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rank_pct(base, 252)

def dsen_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_skew(base, 5)

def dsen_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_skew(base, 21)

def dsen_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_skew(base, 63)

def dsen_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_skew(base, 126)

def dsen_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_skew(base, 252)

def dsen_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_kurt(base, 5)

def dsen_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_kurt(base, 21)

def dsen_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_kurt(base, 63)

def dsen_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_kurt(base, 126)

def dsen_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _rolling_kurt(base, 252)

def dsen_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _safe_div(base, _rolling_std(base, 5))

def dsen_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _safe_div(base, _rolling_std(base, 21))

def dsen_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _safe_div(base, _rolling_std(base, 63))

def dsen_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _safe_div(base, _rolling_std(base, 126))

def dsen_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return _safe_div(base, _rolling_std(base, 252))

def dsen_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close.pct_change().rolling(21).std(), 63))
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_mean(base, 5)

def dsen_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_mean(base, 21)

def dsen_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_mean(base, 63)

def dsen_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_mean(base, 126)

def dsen_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_mean(base, 252)

def dsen_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _zscore_rolling(base, 5)

def dsen_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _zscore_rolling(base, 21)

def dsen_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _zscore_rolling(base, 63)

def dsen_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _zscore_rolling(base, 126)

def dsen_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _zscore_rolling(base, 252)

def dsen_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rank_pct(base, 5)

def dsen_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rank_pct(base, 21)

def dsen_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rank_pct(base, 63)

def dsen_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rank_pct(base, 126)

def dsen_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rank_pct(base, 252)

def dsen_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_skew(base, 5)

def dsen_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_skew(base, 21)

def dsen_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_skew(base, 63)

def dsen_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_skew(base, 126)

def dsen_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_skew(base, 252)

def dsen_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_kurt(base, 5)

def dsen_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_kurt(base, 21)

def dsen_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_kurt(base, 63)

def dsen_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_kurt(base, 126)

def dsen_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _rolling_kurt(base, 252)

def dsen_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 40) + _zscore_rolling(volume, 40)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_mean(base, 5)

def dsen_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_mean(base, 21)

def dsen_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_mean(base, 63)

def dsen_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_mean(base, 126)

def dsen_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_mean(base, 252)

def dsen_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _zscore_rolling(base, 5)

def dsen_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _zscore_rolling(base, 21)

def dsen_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _zscore_rolling(base, 63)

def dsen_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _zscore_rolling(base, 126)

def dsen_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _zscore_rolling(base, 252)
