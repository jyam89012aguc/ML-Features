"""
118_118_drawdown_recovery_asymmetry — Base Features 076-150
Domain: 118_drawdown_recovery_asymmetry
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

def dras_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).skew()
    return _zscore_rolling(base, 5)

def dras_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).skew()
    return _zscore_rolling(base, 21)

def dras_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).skew()
    return _zscore_rolling(base, 63)

def dras_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).skew()
    return _zscore_rolling(base, 126)

def dras_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).skew()
    return _zscore_rolling(base, 252)

def dras_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).skew()
    return _rank_pct(base, 5)

def dras_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).skew()
    return _rank_pct(base, 21)

def dras_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).skew()
    return _rank_pct(base, 63)

def dras_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).skew()
    return _rank_pct(base, 126)

def dras_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).skew()
    return _rank_pct(base, 252)

def dras_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_skew(base, 5)

def dras_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_skew(base, 21)

def dras_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_skew(base, 63)

def dras_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_skew(base, 126)

def dras_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_skew(base, 252)

def dras_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_kurt(base, 5)

def dras_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_kurt(base, 21)

def dras_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_kurt(base, 63)

def dras_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_kurt(base, 126)

def dras_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_kurt(base, 252)

def dras_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).skew()
    return _safe_div(base, _rolling_std(base, 5))

def dras_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).skew()
    return _safe_div(base, _rolling_std(base, 21))

def dras_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).skew()
    return _safe_div(base, _rolling_std(base, 63))

def dras_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).skew()
    return _safe_div(base, _rolling_std(base, 126))

def dras_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).skew()
    return _safe_div(base, _rolling_std(base, 252))

def dras_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).skew()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).skew()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).skew()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).skew()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).skew()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_mean(base, 5)

def dras_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_mean(base, 21)

def dras_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_mean(base, 63)

def dras_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_mean(base, 126)

def dras_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_mean(base, 252)

def dras_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(40).skew()
    return _zscore_rolling(base, 5)

def dras_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(40).skew()
    return _zscore_rolling(base, 21)

def dras_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(40).skew()
    return _zscore_rolling(base, 63)

def dras_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(40).skew()
    return _zscore_rolling(base, 126)

def dras_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(40).skew()
    return _zscore_rolling(base, 252)

def dras_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).skew()
    return _rank_pct(base, 5)

def dras_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).skew()
    return _rank_pct(base, 21)

def dras_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).skew()
    return _rank_pct(base, 63)

def dras_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).skew()
    return _rank_pct(base, 126)

def dras_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(40).skew()
    return _rank_pct(base, 252)

def dras_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_skew(base, 5)

def dras_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_skew(base, 21)

def dras_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_skew(base, 63)

def dras_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_skew(base, 126)

def dras_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_skew(base, 252)

def dras_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_kurt(base, 5)

def dras_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_kurt(base, 21)

def dras_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_kurt(base, 63)

def dras_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_kurt(base, 126)

def dras_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(40).skew()
    return _rolling_kurt(base, 252)

def dras_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).skew()
    return _safe_div(base, _rolling_std(base, 5))

def dras_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).skew()
    return _safe_div(base, _rolling_std(base, 21))

def dras_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).skew()
    return _safe_div(base, _rolling_std(base, 63))

def dras_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).skew()
    return _safe_div(base, _rolling_std(base, 126))

def dras_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(40).skew()
    return _safe_div(base, _rolling_std(base, 252))

def dras_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).skew()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).skew()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).skew()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).skew()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(40).skew()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_mean(base, 5)

def dras_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_mean(base, 21)

def dras_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_mean(base, 63)

def dras_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_mean(base, 126)

def dras_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_mean(base, 252)

def dras_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(50).skew()
    return _zscore_rolling(base, 5)

def dras_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(50).skew()
    return _zscore_rolling(base, 21)

def dras_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(50).skew()
    return _zscore_rolling(base, 63)

def dras_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(50).skew()
    return _zscore_rolling(base, 126)

def dras_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(50).skew()
    return _zscore_rolling(base, 252)
