"""
106_106_support_violation — Base Features 076-150
Domain: 106_support_violation
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

def supv_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _zscore_rolling(base, 5)

def supv_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _zscore_rolling(base, 21)

def supv_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _zscore_rolling(base, 63)

def supv_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _zscore_rolling(base, 126)

def supv_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _zscore_rolling(base, 252)

def supv_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rank_pct(base, 5)

def supv_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rank_pct(base, 21)

def supv_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rank_pct(base, 63)

def supv_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rank_pct(base, 126)

def supv_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rank_pct(base, 252)

def supv_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_skew(base, 5)

def supv_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_skew(base, 21)

def supv_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_skew(base, 63)

def supv_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_skew(base, 126)

def supv_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_skew(base, 252)

def supv_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_kurt(base, 5)

def supv_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_kurt(base, 21)

def supv_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_kurt(base, 63)

def supv_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_kurt(base, 126)

def supv_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _rolling_kurt(base, 252)

def supv_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 5))

def supv_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 21))

def supv_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 63))

def supv_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 126))

def supv_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return _safe_div(base, _rolling_std(base, 252))

def supv_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close < low.rolling(21).min().shift(1)).astype(int)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_mean(base, 5)

def supv_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_mean(base, 21)

def supv_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_mean(base, 63)

def supv_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_mean(base, 126)

def supv_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_mean(base, 252)

def supv_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(40).min() - 1
    return _zscore_rolling(base, 5)

def supv_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(40).min() - 1
    return _zscore_rolling(base, 21)

def supv_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(40).min() - 1
    return _zscore_rolling(base, 63)

def supv_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(40).min() - 1
    return _zscore_rolling(base, 126)

def supv_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(40).min() - 1
    return _zscore_rolling(base, 252)

def supv_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(40).min() - 1
    return _rank_pct(base, 5)

def supv_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(40).min() - 1
    return _rank_pct(base, 21)

def supv_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(40).min() - 1
    return _rank_pct(base, 63)

def supv_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(40).min() - 1
    return _rank_pct(base, 126)

def supv_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(40).min() - 1
    return _rank_pct(base, 252)

def supv_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_skew(base, 5)

def supv_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_skew(base, 21)

def supv_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_skew(base, 63)

def supv_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_skew(base, 126)

def supv_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_skew(base, 252)

def supv_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_kurt(base, 5)

def supv_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_kurt(base, 21)

def supv_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_kurt(base, 63)

def supv_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_kurt(base, 126)

def supv_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(40).min() - 1
    return _rolling_kurt(base, 252)

def supv_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(40).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(40).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(40).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(40).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(40).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(40).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(40).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(40).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(40).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(40).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_mean(base, 5)

def supv_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_mean(base, 21)

def supv_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_mean(base, 63)

def supv_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_mean(base, 126)

def supv_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_mean(base, 252)

def supv_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(50).min() - 1
    return _zscore_rolling(base, 5)

def supv_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(50).min() - 1
    return _zscore_rolling(base, 21)

def supv_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(50).min() - 1
    return _zscore_rolling(base, 63)

def supv_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(50).min() - 1
    return _zscore_rolling(base, 126)

def supv_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(50).min() - 1
    return _zscore_rolling(base, 252)
