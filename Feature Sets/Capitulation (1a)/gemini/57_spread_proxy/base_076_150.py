"""
57_57_spread_proxy — Base Features 076-150
Domain: 57_spread_proxy
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

def sprd_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 5d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 5)

def sprd_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 21d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 21)

def sprd_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 63d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 63)

def sprd_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 126d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 126)

def sprd_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 252d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 252)

def sprd_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 5)

def sprd_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 21)

def sprd_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 63)

def sprd_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 126)

def sprd_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 252)

def sprd_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 5)

def sprd_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 21)

def sprd_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 63)

def sprd_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 126)

def sprd_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 252)

def sprd_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 5)

def sprd_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 21)

def sprd_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 63)

def sprd_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 126)

def sprd_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 252)

def sprd_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def sprd_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def sprd_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def sprd_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def sprd_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def sprd_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def sprd_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def sprd_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def sprd_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def sprd_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def sprd_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def sprd_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def sprd_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def sprd_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def sprd_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def sprd_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 5d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def sprd_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 21d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def sprd_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 63d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def sprd_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 126d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def sprd_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 252d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def sprd_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 5)

def sprd_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 21)

def sprd_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 63)

def sprd_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 126)

def sprd_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 57 spread proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 252)

def sprd_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def sprd_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def sprd_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def sprd_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def sprd_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 57 spread proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def sprd_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def sprd_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def sprd_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def sprd_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def sprd_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 57 spread proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def sprd_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def sprd_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def sprd_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def sprd_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def sprd_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 57 spread proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def sprd_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def sprd_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def sprd_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def sprd_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def sprd_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 57 spread proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def sprd_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 5d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def sprd_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 21d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def sprd_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 63d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def sprd_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 126d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def sprd_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 57 spread proxy over a 252d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def sprd_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 5d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def sprd_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 21d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def sprd_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 63d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def sprd_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 126d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def sprd_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 57 spread proxy by measuring deviations from the 252d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)
