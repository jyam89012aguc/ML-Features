"""
123_123_relative_weakness_xs — Base Features 076-150
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

def rwxs_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _zscore_rolling(base, 5)

def rwxs_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _zscore_rolling(base, 21)

def rwxs_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _zscore_rolling(base, 63)

def rwxs_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _zscore_rolling(base, 126)

def rwxs_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _zscore_rolling(base, 252)

def rwxs_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rank_pct(base, 5)

def rwxs_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rank_pct(base, 21)

def rwxs_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rank_pct(base, 63)

def rwxs_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rank_pct(base, 126)

def rwxs_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rank_pct(base, 252)

def rwxs_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_skew(base, 5)

def rwxs_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_skew(base, 21)

def rwxs_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_skew(base, 63)

def rwxs_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_skew(base, 126)

def rwxs_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_skew(base, 252)

def rwxs_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_kurt(base, 5)

def rwxs_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_kurt(base, 21)

def rwxs_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_kurt(base, 63)

def rwxs_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_kurt(base, 126)

def rwxs_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _rolling_kurt(base, 252)

def rwxs_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close / _rolling_mean(close, 252), 63)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 5)

def rwxs_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 21)

def rwxs_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 63)

def rwxs_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 126)

def rwxs_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 252)

def rwxs_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 5)

def rwxs_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 21)

def rwxs_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 63)

def rwxs_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 126)

def rwxs_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 252)

def rwxs_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 5)

def rwxs_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 21)

def rwxs_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 63)

def rwxs_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 126)

def rwxs_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 252)

def rwxs_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 5)

def rwxs_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 21)

def rwxs_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 63)

def rwxs_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 126)

def rwxs_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 252)

def rwxs_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 5)

def rwxs_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 21)

def rwxs_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 63)

def rwxs_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 126)

def rwxs_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 252)

def rwxs_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 5)

def rwxs_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 21)

def rwxs_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 63)

def rwxs_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 126)

def rwxs_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(100)
    return _rolling_mean(base, 252)

def rwxs_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 5)

def rwxs_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 21)

def rwxs_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 63)

def rwxs_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 126)

def rwxs_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(100)
    return _zscore_rolling(base, 252)
