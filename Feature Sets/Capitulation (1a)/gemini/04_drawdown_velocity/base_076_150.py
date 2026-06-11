"""
04_04_drawdown_velocity — Base Features 076-150
Domain: 04_drawdown_velocity
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

def dvel_076_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 5d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dvel_077_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 21d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dvel_078_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 63d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dvel_079_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 126d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dvel_080_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 252d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dvel_081_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def dvel_082_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def dvel_083_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def dvel_084_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def dvel_085_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def dvel_086_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def dvel_087_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def dvel_088_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def dvel_089_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def dvel_090_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def dvel_091_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def dvel_092_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def dvel_093_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def dvel_094_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def dvel_095_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def dvel_096_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def dvel_097_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def dvel_098_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def dvel_099_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def dvel_100_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def dvel_101_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvel_102_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvel_103_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvel_104_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvel_105_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvel_106_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 5)

def dvel_107_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 21)

def dvel_108_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 63)

def dvel_109_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 126)

def dvel_110_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 252)

def dvel_111_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 5)

def dvel_112_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 21)

def dvel_113_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 63)

def dvel_114_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 126)

def dvel_115_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 252)

def dvel_116_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 5)

def dvel_117_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 21)

def dvel_118_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 63)

def dvel_119_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 126)

def dvel_120_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 252)

def dvel_121_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 5)

def dvel_122_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 21)

def dvel_123_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 63)

def dvel_124_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 126)

def dvel_125_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 252)

def dvel_126_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 5)

def dvel_127_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 21)

def dvel_128_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 63)

def dvel_129_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 126)

def dvel_130_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 252)

def dvel_131_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvel_132_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvel_133_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvel_134_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvel_135_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvel_136_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvel_137_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvel_138_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvel_139_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvel_140_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvel_141_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 5)

def dvel_142_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 21)

def dvel_143_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 63)

def dvel_144_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 126)

def dvel_145_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 252)

def dvel_146_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 5)

def dvel_147_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 21)

def dvel_148_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 63)

def dvel_149_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 126)

def dvel_150_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 252)
