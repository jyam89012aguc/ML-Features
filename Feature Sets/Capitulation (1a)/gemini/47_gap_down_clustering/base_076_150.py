"""
47_47_gap_down_clustering — Base Features 076-150
Domain: 47_gap_down_clustering
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

def gapc_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def gapc_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def gapc_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def gapc_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def gapc_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def gapc_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def gapc_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def gapc_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def gapc_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def gapc_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def gapc_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def gapc_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def gapc_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def gapc_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def gapc_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def gapc_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def gapc_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def gapc_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def gapc_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def gapc_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def gapc_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def gapc_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def gapc_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def gapc_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def gapc_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def gapc_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = (high - np.maximum(open, close)) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def gapc_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def gapc_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def gapc_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def gapc_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def gapc_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def gapc_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def gapc_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def gapc_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def gapc_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def gapc_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 5)

def gapc_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 21)

def gapc_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 63)

def gapc_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 126)

def gapc_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rank_pct(base, 252)

def gapc_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 5)

def gapc_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 21)

def gapc_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 63)

def gapc_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 126)

def gapc_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_skew(base, 252)

def gapc_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def gapc_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def gapc_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def gapc_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def gapc_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def gapc_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def gapc_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def gapc_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def gapc_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def gapc_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def gapc_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = (np.minimum(open, close) - low) / (high - low).replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def gapc_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def gapc_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def gapc_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def gapc_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def gapc_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def gapc_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def gapc_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def gapc_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def gapc_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)
