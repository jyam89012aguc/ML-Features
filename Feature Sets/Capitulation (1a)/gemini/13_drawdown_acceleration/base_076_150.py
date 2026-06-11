"""
13_13_drawdown_acceleration — Base Features 076-150
Domain: 13_drawdown_acceleration
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

def dacc_076_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 5d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dacc_077_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 21d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dacc_078_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 63d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dacc_079_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 126d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dacc_080_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 252d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dacc_081_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def dacc_082_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def dacc_083_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def dacc_084_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def dacc_085_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def dacc_086_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def dacc_087_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def dacc_088_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def dacc_089_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def dacc_090_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def dacc_091_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def dacc_092_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def dacc_093_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def dacc_094_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def dacc_095_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def dacc_096_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def dacc_097_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def dacc_098_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def dacc_099_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def dacc_100_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def dacc_101_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dacc_102_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dacc_103_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dacc_104_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dacc_105_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dacc_106_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 5)

def dacc_107_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 21)

def dacc_108_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 63)

def dacc_109_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 126)

def dacc_110_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 252)

def dacc_111_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 5)

def dacc_112_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 21)

def dacc_113_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 63)

def dacc_114_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 126)

def dacc_115_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 252)

def dacc_116_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 5)

def dacc_117_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 21)

def dacc_118_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 63)

def dacc_119_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 126)

def dacc_120_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 13 drawdown acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 252)

def dacc_121_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 5)

def dacc_122_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 21)

def dacc_123_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 63)

def dacc_124_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 126)

def dacc_125_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 13 drawdown acceleration distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 252)

def dacc_126_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 5)

def dacc_127_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 21)

def dacc_128_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 63)

def dacc_129_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 126)

def dacc_130_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 13 drawdown acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 252)

def dacc_131_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dacc_132_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dacc_133_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dacc_134_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dacc_135_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 13 drawdown acceleration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dacc_136_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dacc_137_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dacc_138_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dacc_139_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dacc_140_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 13 drawdown acceleration over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dacc_141_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 5)

def dacc_142_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 21)

def dacc_143_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 63)

def dacc_144_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 126)

def dacc_145_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 13 drawdown acceleration over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 252)

def dacc_146_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 5)

def dacc_147_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 21)

def dacc_148_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 63)

def dacc_149_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 126)

def dacc_150_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 13 drawdown acceleration by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 252)
