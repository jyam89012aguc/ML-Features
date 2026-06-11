"""
58_58_trading_intensity — Base Features 076-150
Domain: 58_trading_intensity
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

def tint_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def tint_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def tint_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def tint_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def tint_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def tint_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 5)

def tint_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 21)

def tint_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 63)

def tint_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 126)

def tint_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 252)

def tint_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def tint_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def tint_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def tint_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def tint_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def tint_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def tint_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def tint_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def tint_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def tint_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def tint_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def tint_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def tint_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def tint_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def tint_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def tint_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tint_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 5)

def tint_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 21)

def tint_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 63)

def tint_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 126)

def tint_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 252)

def tint_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 5)

def tint_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 21)

def tint_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 63)

def tint_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 126)

def tint_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 252)

def tint_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 5)

def tint_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 21)

def tint_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 63)

def tint_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 126)

def tint_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 252)

def tint_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 5)

def tint_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 21)

def tint_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 63)

def tint_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 126)

def tint_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 252)

def tint_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 5)

def tint_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 21)

def tint_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 63)

def tint_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 126)

def tint_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 252)

def tint_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 5))

def tint_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 21))

def tint_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 63))

def tint_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 126))

def tint_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 252))

def tint_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tint_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def tint_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def tint_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def tint_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def tint_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def tint_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def tint_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def tint_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def tint_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def tint_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 252)
