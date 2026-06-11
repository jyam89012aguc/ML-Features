"""
56_56_zero_volume_days — Base Features 076-150
Domain: 56_zero_volume_days
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

def zvol_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 5d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def zvol_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 21d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def zvol_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 63d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def zvol_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 126d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def zvol_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 252d mean.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def zvol_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 5)

def zvol_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 21)

def zvol_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 63)

def zvol_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 126)

def zvol_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rank_pct(base, 252)

def zvol_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def zvol_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def zvol_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def zvol_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def zvol_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def zvol_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def zvol_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def zvol_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def zvol_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def zvol_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def zvol_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def zvol_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def zvol_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def zvol_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def zvol_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def zvol_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def zvol_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def zvol_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def zvol_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def zvol_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / volume.rolling(63).max().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def zvol_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 5d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 5)

def zvol_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 21d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 21)

def zvol_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 63d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 63)

def zvol_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 126d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 126)

def zvol_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 252d horizon to identify extreme regimes.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_mean(base, 252)

def zvol_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 5d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 5)

def zvol_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 21d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 21)

def zvol_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 63d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 63)

def zvol_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 126d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 126)

def zvol_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 252d mean.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _zscore_rolling(base, 252)

def zvol_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 5)

def zvol_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 21)

def zvol_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 63)

def zvol_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 126)

def zvol_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 56 zero volume days to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rank_pct(base, 252)

def zvol_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 5)

def zvol_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 21)

def zvol_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 63)

def zvol_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 126)

def zvol_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 56 zero volume days distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_skew(base, 252)

def zvol_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 5)

def zvol_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 21)

def zvol_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 63)

def zvol_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 126)

def zvol_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 56 zero volume days over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _rolling_kurt(base, 252)

def zvol_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 5))

def zvol_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 21))

def zvol_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 63))

def zvol_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 126))

def zvol_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 56 zero volume days for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 252))

def zvol_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def zvol_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def zvol_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def zvol_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def zvol_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 56 zero volume days over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume == 0).astype(int).rolling(21).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def zvol_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def zvol_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def zvol_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def zvol_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def zvol_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 56 zero volume days over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def zvol_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def zvol_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def zvol_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def zvol_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def zvol_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 56 zero volume days by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _zscore_rolling(base, 252)
