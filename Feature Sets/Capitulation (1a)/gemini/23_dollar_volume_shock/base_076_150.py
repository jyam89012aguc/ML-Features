"""
23_23_dollar_volume_shock — Base Features 076-150
Domain: 23_dollar_volume_shock
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

def dvsh_076_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 5)

def dvsh_077_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 21)

def dvsh_078_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 63)

def dvsh_079_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 126)

def dvsh_080_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = volume / volume.rolling(63).max()
    return _zscore_rolling(base, 252)

def dvsh_081_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 5)

def dvsh_082_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 21)

def dvsh_083_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 63)

def dvsh_084_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 126)

def dvsh_085_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max()
    return _rank_pct(base, 252)

def dvsh_086_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_skew(base, 5)

def dvsh_087_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_skew(base, 21)

def dvsh_088_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_skew(base, 63)

def dvsh_089_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_skew(base, 126)

def dvsh_090_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_skew(base, 252)

def dvsh_091_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_kurt(base, 5)

def dvsh_092_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_kurt(base, 21)

def dvsh_093_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_kurt(base, 63)

def dvsh_094_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_kurt(base, 126)

def dvsh_095_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max()
    return _rolling_kurt(base, 252)

def dvsh_096_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max()
    return _safe_div(base, _rolling_std(base, 5))

def dvsh_097_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max()
    return _safe_div(base, _rolling_std(base, 21))

def dvsh_098_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max()
    return _safe_div(base, _rolling_std(base, 63))

def dvsh_099_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max()
    return _safe_div(base, _rolling_std(base, 126))

def dvsh_100_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max()
    return _safe_div(base, _rolling_std(base, 252))

def dvsh_101_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvsh_102_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvsh_103_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvsh_104_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvsh_105_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvsh_106_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 5)

def dvsh_107_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 21)

def dvsh_108_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 63)

def dvsh_109_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 126)

def dvsh_110_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_mean(base, 252)

def dvsh_111_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 5)

def dvsh_112_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 21)

def dvsh_113_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 63)

def dvsh_114_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 126)

def dvsh_115_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _zscore_rolling(base, 252)

def dvsh_116_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 5)

def dvsh_117_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 21)

def dvsh_118_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 63)

def dvsh_119_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 126)

def dvsh_120_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rank_pct(base, 252)

def dvsh_121_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 5)

def dvsh_122_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 21)

def dvsh_123_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 63)

def dvsh_124_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 126)

def dvsh_125_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_skew(base, 252)

def dvsh_126_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 5)

def dvsh_127_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 21)

def dvsh_128_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 63)

def dvsh_129_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 126)

def dvsh_130_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _rolling_kurt(base, 252)

def dvsh_131_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvsh_132_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvsh_133_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvsh_134_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvsh_135_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvsh_136_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvsh_137_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvsh_138_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvsh_139_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvsh_140_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(4).rolling(20).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvsh_141_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 5)

def dvsh_142_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 21)

def dvsh_143_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 63)

def dvsh_144_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 126)

def dvsh_145_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_mean(base, 252)

def dvsh_146_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 5)

def dvsh_147_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 21)

def dvsh_148_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 63)

def dvsh_149_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 126)

def dvsh_150_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _zscore_rolling(base, 252)
