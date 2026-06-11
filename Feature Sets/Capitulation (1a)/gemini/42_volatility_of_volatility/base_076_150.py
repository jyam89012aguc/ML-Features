"""
42_42_volatility_of_volatility — Base Features 076-150
Domain: 42_volatility_of_volatility
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

def vov_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 5d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 5)

def vov_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 21d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 21)

def vov_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 63d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 63)

def vov_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 126d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 126)

def vov_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 252d mean.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _zscore_rolling(base, 252)

def vov_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 5)

def vov_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 21)

def vov_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 63)

def vov_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 126)

def vov_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rank_pct(base, 252)

def vov_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 5)

def vov_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 21)

def vov_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 63)

def vov_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 126)

def vov_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_skew(base, 252)

def vov_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 5)

def vov_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 21)

def vov_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 63)

def vov_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 126)

def vov_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _rolling_kurt(base, 252)

def vov_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def vov_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def vov_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def vov_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def vov_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def vov_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vov_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vov_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vov_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vov_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.minimum(close.pct_change(), 0).rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vov_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def vov_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def vov_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def vov_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def vov_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def vov_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 5d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def vov_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 21d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def vov_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 63d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def vov_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 126d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def vov_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 252d mean.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def vov_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 5)

def vov_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 21)

def vov_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 63)

def vov_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 126)

def vov_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 42 volatility of volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rank_pct(base, 252)

def vov_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def vov_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def vov_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def vov_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def vov_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 42 volatility of volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def vov_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def vov_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def vov_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def vov_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def vov_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 42 volatility of volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def vov_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def vov_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def vov_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def vov_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def vov_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 42 volatility of volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def vov_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vov_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vov_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vov_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vov_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 42 volatility of volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs() / (high - low).rolling(14).mean().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vov_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 5d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def vov_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 21d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def vov_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 63d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def vov_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 126d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def vov_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 42 volatility of volatility over a 252d horizon to identify extreme regimes.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def vov_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 5d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def vov_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 21d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def vov_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 63d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def vov_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 126d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def vov_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 42 volatility of volatility by measuring deviations from the 252d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)
