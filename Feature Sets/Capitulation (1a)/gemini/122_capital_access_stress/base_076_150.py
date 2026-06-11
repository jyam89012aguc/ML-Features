"""
122_122_capital_access_stress — Base Features 076-150
Domain: 122_capital_access_stress
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

def cast_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.rolling(252).max() / close - 1
    return _zscore_rolling(base, 5)

def cast_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.rolling(252).max() / close - 1
    return _zscore_rolling(base, 21)

def cast_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.rolling(252).max() / close - 1
    return _zscore_rolling(base, 63)

def cast_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.rolling(252).max() / close - 1
    return _zscore_rolling(base, 126)

def cast_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.rolling(252).max() / close - 1
    return _zscore_rolling(base, 252)

def cast_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.rolling(252).max() / close - 1
    return _rank_pct(base, 5)

def cast_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.rolling(252).max() / close - 1
    return _rank_pct(base, 21)

def cast_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.rolling(252).max() / close - 1
    return _rank_pct(base, 63)

def cast_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.rolling(252).max() / close - 1
    return _rank_pct(base, 126)

def cast_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.rolling(252).max() / close - 1
    return _rank_pct(base, 252)

def cast_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_skew(base, 5)

def cast_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_skew(base, 21)

def cast_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_skew(base, 63)

def cast_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_skew(base, 126)

def cast_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_skew(base, 252)

def cast_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_kurt(base, 5)

def cast_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_kurt(base, 21)

def cast_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_kurt(base, 63)

def cast_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_kurt(base, 126)

def cast_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.rolling(252).max() / close - 1
    return _rolling_kurt(base, 252)

def cast_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(252).max() / close - 1
    return _safe_div(base, _rolling_std(base, 5))

def cast_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(252).max() / close - 1
    return _safe_div(base, _rolling_std(base, 21))

def cast_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(252).max() / close - 1
    return _safe_div(base, _rolling_std(base, 63))

def cast_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(252).max() / close - 1
    return _safe_div(base, _rolling_std(base, 126))

def cast_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.rolling(252).max() / close - 1
    return _safe_div(base, _rolling_std(base, 252))

def cast_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(252).max() / close - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(252).max() / close - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(252).max() / close - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(252).max() / close - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.rolling(252).max() / close - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 5)

def cast_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 21)

def cast_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 63)

def cast_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 126)

def cast_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 252)

def cast_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 5)

def cast_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 21)

def cast_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 63)

def cast_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 126)

def cast_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 252)

def cast_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 5)

def cast_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 21)

def cast_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 63)

def cast_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 126)

def cast_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 252)

def cast_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 5)

def cast_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 21)

def cast_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 63)

def cast_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 126)

def cast_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 252)

def cast_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 5)

def cast_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 21)

def cast_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 63)

def cast_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 126)

def cast_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 252)

def cast_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 5)

def cast_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 21)

def cast_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 63)

def cast_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 126)

def cast_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 252)

def cast_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 5)

def cast_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 21)

def cast_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 63)

def cast_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 126)

def cast_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 252)
