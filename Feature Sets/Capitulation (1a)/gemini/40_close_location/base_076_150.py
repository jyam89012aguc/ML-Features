"""
40_40_close_location — Base Features 076-150
Domain: 40_close_location
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

def cloc_076_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 5d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cloc_077_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 21d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cloc_078_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 63d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cloc_079_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 126d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cloc_080_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 252d mean.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cloc_081_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def cloc_082_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def cloc_083_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def cloc_084_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def cloc_085_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def cloc_086_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def cloc_087_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def cloc_088_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def cloc_089_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def cloc_090_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def cloc_091_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def cloc_092_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def cloc_093_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def cloc_094_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def cloc_095_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def cloc_096_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def cloc_097_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def cloc_098_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def cloc_099_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def cloc_100_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def cloc_101_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cloc_102_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cloc_103_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cloc_104_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cloc_105_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cloc_106_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 5)

def cloc_107_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 21)

def cloc_108_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 63)

def cloc_109_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 126)

def cloc_110_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 252)

def cloc_111_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 5)

def cloc_112_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 21)

def cloc_113_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 63)

def cloc_114_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 126)

def cloc_115_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 252)

def cloc_116_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 5)

def cloc_117_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 21)

def cloc_118_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 63)

def cloc_119_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 126)

def cloc_120_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 252)

def cloc_121_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 5)

def cloc_122_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 21)

def cloc_123_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 63)

def cloc_124_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 126)

def cloc_125_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 252)

def cloc_126_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 5)

def cloc_127_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 21)

def cloc_128_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 63)

def cloc_129_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 126)

def cloc_130_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 252)

def cloc_131_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 5))

def cloc_132_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 21))

def cloc_133_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 63))

def cloc_134_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 126))

def cloc_135_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 252))

def cloc_136_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cloc_137_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cloc_138_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cloc_139_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cloc_140_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cloc_141_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 5)

def cloc_142_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 21)

def cloc_143_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 63)

def cloc_144_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 126)

def cloc_145_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 252)

def cloc_146_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 5)

def cloc_147_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 21)

def cloc_148_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 63)

def cloc_149_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 126)

def cloc_150_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 252)
