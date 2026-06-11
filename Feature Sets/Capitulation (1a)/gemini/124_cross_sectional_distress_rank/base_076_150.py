"""
124_124_cross_sectional_distress_rank — Base Features 076-150
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

def csdr_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _zscore_rolling(base, 5)

def csdr_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _zscore_rolling(base, 21)

def csdr_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _zscore_rolling(base, 63)

def csdr_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _zscore_rolling(base, 126)

def csdr_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _zscore_rolling(base, 252)

def csdr_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rank_pct(base, 5)

def csdr_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rank_pct(base, 21)

def csdr_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rank_pct(base, 63)

def csdr_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rank_pct(base, 126)

def csdr_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rank_pct(base, 252)

def csdr_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_skew(base, 5)

def csdr_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_skew(base, 21)

def csdr_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_skew(base, 63)

def csdr_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_skew(base, 126)

def csdr_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_skew(base, 252)

def csdr_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_kurt(base, 5)

def csdr_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_kurt(base, 21)

def csdr_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_kurt(base, 63)

def csdr_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_kurt(base, 126)

def csdr_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _rolling_kurt(base, 252)

def csdr_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(volume.pct_change(21), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_mean(base, 5)

def csdr_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_mean(base, 21)

def csdr_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_mean(base, 63)

def csdr_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_mean(base, 126)

def csdr_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_mean(base, 252)

def csdr_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _zscore_rolling(base, 5)

def csdr_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _zscore_rolling(base, 21)

def csdr_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _zscore_rolling(base, 63)

def csdr_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _zscore_rolling(base, 126)

def csdr_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _zscore_rolling(base, 252)

def csdr_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rank_pct(base, 5)

def csdr_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rank_pct(base, 21)

def csdr_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rank_pct(base, 63)

def csdr_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rank_pct(base, 126)

def csdr_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rank_pct(base, 252)

def csdr_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_skew(base, 5)

def csdr_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_skew(base, 21)

def csdr_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_skew(base, 63)

def csdr_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_skew(base, 126)

def csdr_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_skew(base, 252)

def csdr_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_kurt(base, 5)

def csdr_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_kurt(base, 21)

def csdr_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_kurt(base, 63)

def csdr_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_kurt(base, 126)

def csdr_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _rolling_kurt(base, 252)

def csdr_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(40), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _rolling_mean(base, 5)

def csdr_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _rolling_mean(base, 21)

def csdr_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _rolling_mean(base, 63)

def csdr_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _rolling_mean(base, 126)

def csdr_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _rolling_mean(base, 252)

def csdr_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _zscore_rolling(base, 5)

def csdr_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _zscore_rolling(base, 21)

def csdr_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _zscore_rolling(base, 63)

def csdr_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _zscore_rolling(base, 126)

def csdr_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(50), 252)
    return _zscore_rolling(base, 252)
