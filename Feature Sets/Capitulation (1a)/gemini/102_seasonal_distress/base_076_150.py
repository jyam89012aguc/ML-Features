"""
102_102_seasonal_distress — Base Features 076-150
Domain: 102_seasonal_distress
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

def seas_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(252)
    return _zscore_rolling(base, 5)

def seas_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(252)
    return _zscore_rolling(base, 21)

def seas_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(252)
    return _zscore_rolling(base, 63)

def seas_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(252)
    return _zscore_rolling(base, 126)

def seas_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(252)
    return _zscore_rolling(base, 252)

def seas_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(252)
    return _rank_pct(base, 5)

def seas_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(252)
    return _rank_pct(base, 21)

def seas_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(252)
    return _rank_pct(base, 63)

def seas_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(252)
    return _rank_pct(base, 126)

def seas_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(252)
    return _rank_pct(base, 252)

def seas_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(252)
    return _rolling_skew(base, 5)

def seas_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(252)
    return _rolling_skew(base, 21)

def seas_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(252)
    return _rolling_skew(base, 63)

def seas_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(252)
    return _rolling_skew(base, 126)

def seas_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(252)
    return _rolling_skew(base, 252)

def seas_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(252)
    return _rolling_kurt(base, 5)

def seas_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(252)
    return _rolling_kurt(base, 21)

def seas_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(252)
    return _rolling_kurt(base, 63)

def seas_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(252)
    return _rolling_kurt(base, 126)

def seas_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(252)
    return _rolling_kurt(base, 252)

def seas_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(252)
    return _safe_div(base, _rolling_std(base, 5))

def seas_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(252)
    return _safe_div(base, _rolling_std(base, 21))

def seas_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(252)
    return _safe_div(base, _rolling_std(base, 63))

def seas_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(252)
    return _safe_div(base, _rolling_std(base, 126))

def seas_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(252)
    return _safe_div(base, _rolling_std(base, 252))

def seas_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = volume.pct_change(252)
    return _rolling_mean(base, 5)

def seas_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = volume.pct_change(252)
    return _rolling_mean(base, 21)

def seas_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = volume.pct_change(252)
    return _rolling_mean(base, 63)

def seas_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = volume.pct_change(252)
    return _rolling_mean(base, 126)

def seas_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = volume.pct_change(252)
    return _rolling_mean(base, 252)

def seas_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = volume.pct_change(252)
    return _zscore_rolling(base, 5)

def seas_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = volume.pct_change(252)
    return _zscore_rolling(base, 21)

def seas_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = volume.pct_change(252)
    return _zscore_rolling(base, 63)

def seas_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = volume.pct_change(252)
    return _zscore_rolling(base, 126)

def seas_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = volume.pct_change(252)
    return _zscore_rolling(base, 252)

def seas_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume.pct_change(252)
    return _rank_pct(base, 5)

def seas_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume.pct_change(252)
    return _rank_pct(base, 21)

def seas_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume.pct_change(252)
    return _rank_pct(base, 63)

def seas_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume.pct_change(252)
    return _rank_pct(base, 126)

def seas_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume.pct_change(252)
    return _rank_pct(base, 252)

def seas_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume.pct_change(252)
    return _rolling_skew(base, 5)

def seas_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume.pct_change(252)
    return _rolling_skew(base, 21)

def seas_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume.pct_change(252)
    return _rolling_skew(base, 63)

def seas_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume.pct_change(252)
    return _rolling_skew(base, 126)

def seas_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume.pct_change(252)
    return _rolling_skew(base, 252)

def seas_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change(252)
    return _rolling_kurt(base, 5)

def seas_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change(252)
    return _rolling_kurt(base, 21)

def seas_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change(252)
    return _rolling_kurt(base, 63)

def seas_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change(252)
    return _rolling_kurt(base, 126)

def seas_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = volume.pct_change(252)
    return _rolling_kurt(base, 252)

def seas_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change(252)
    return _safe_div(base, _rolling_std(base, 5))

def seas_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change(252)
    return _safe_div(base, _rolling_std(base, 21))

def seas_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change(252)
    return _safe_div(base, _rolling_std(base, 63))

def seas_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change(252)
    return _safe_div(base, _rolling_std(base, 126))

def seas_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume.pct_change(252)
    return _safe_div(base, _rolling_std(base, 252))

def seas_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change(252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change(252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change(252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change(252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume.pct_change(252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(25)
    return _rolling_mean(base, 5)

def seas_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(25)
    return _rolling_mean(base, 21)

def seas_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(25)
    return _rolling_mean(base, 63)

def seas_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(25)
    return _rolling_mean(base, 126)

def seas_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(25)
    return _rolling_mean(base, 252)

def seas_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(25)
    return _zscore_rolling(base, 5)

def seas_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(25)
    return _zscore_rolling(base, 21)

def seas_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(25)
    return _zscore_rolling(base, 63)

def seas_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(25)
    return _zscore_rolling(base, 126)

def seas_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(25)
    return _zscore_rolling(base, 252)
