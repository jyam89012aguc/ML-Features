"""
115_115_volatility_term_structure — Base Features 076-150
Domain: 115_volatility_term_structure
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

def vts_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 5)

def vts_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 21)

def vts_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 63)

def vts_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 126)

def vts_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _zscore_rolling(base, 252)

def vts_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 5)

def vts_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 21)

def vts_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 63)

def vts_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 126)

def vts_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rank_pct(base, 252)

def vts_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 5)

def vts_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 21)

def vts_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 63)

def vts_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 126)

def vts_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_skew(base, 252)

def vts_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 5)

def vts_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 21)

def vts_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 63)

def vts_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 126)

def vts_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _rolling_kurt(base, 252)

def vts_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(5).std() / close.pct_change().rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 5)

def vts_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 21)

def vts_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 63)

def vts_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 126)

def vts_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_mean(base, 252)

def vts_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 5)

def vts_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 21)

def vts_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 63)

def vts_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 126)

def vts_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(20).std()
    return _zscore_rolling(base, 252)

def vts_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 5)

def vts_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 21)

def vts_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 63)

def vts_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 126)

def vts_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(20).std()
    return _rank_pct(base, 252)

def vts_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 5)

def vts_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 21)

def vts_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 63)

def vts_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 126)

def vts_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_skew(base, 252)

def vts_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 5)

def vts_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 21)

def vts_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 63)

def vts_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 126)

def vts_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(20).std()
    return _rolling_kurt(base, 252)

def vts_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(20).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(20).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 5)

def vts_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 21)

def vts_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 63)

def vts_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 126)

def vts_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_mean(base, 252)

def vts_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 5)

def vts_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 21)

def vts_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 63)

def vts_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 126)

def vts_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(25).std()
    return _zscore_rolling(base, 252)
