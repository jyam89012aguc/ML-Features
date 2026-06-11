"""
116_116_extreme_day_density — Base Features 076-150
Domain: 116_extreme_day_density
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

def exdd_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 5d mean.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _zscore_rolling(base, 5)

def exdd_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 21d mean.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _zscore_rolling(base, 21)

def exdd_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 63d mean.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _zscore_rolling(base, 63)

def exdd_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 126d mean.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _zscore_rolling(base, 126)

def exdd_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 252d mean.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _zscore_rolling(base, 252)

def exdd_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rank_pct(base, 5)

def exdd_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rank_pct(base, 21)

def exdd_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rank_pct(base, 63)

def exdd_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rank_pct(base, 126)

def exdd_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rank_pct(base, 252)

def exdd_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_skew(base, 5)

def exdd_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_skew(base, 21)

def exdd_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_skew(base, 63)

def exdd_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_skew(base, 126)

def exdd_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_skew(base, 252)

def exdd_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_kurt(base, 5)

def exdd_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_kurt(base, 21)

def exdd_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_kurt(base, 63)

def exdd_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_kurt(base, 126)

def exdd_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _rolling_kurt(base, 252)

def exdd_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _safe_div(base, _rolling_std(base, 5))

def exdd_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _safe_div(base, _rolling_std(base, 21))

def exdd_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _safe_div(base, _rolling_std(base, 63))

def exdd_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _safe_div(base, _rolling_std(base, 126))

def exdd_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return _safe_div(base, _rolling_std(base, 252))

def exdd_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def exdd_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def exdd_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def exdd_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def exdd_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change() > 2 * close.pct_change().rolling(252).std()).astype(int).rolling(63).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def exdd_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_mean(base, 5)

def exdd_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_mean(base, 21)

def exdd_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_mean(base, 63)

def exdd_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_mean(base, 126)

def exdd_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_mean(base, 252)

def exdd_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _zscore_rolling(base, 5)

def exdd_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _zscore_rolling(base, 21)

def exdd_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _zscore_rolling(base, 63)

def exdd_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _zscore_rolling(base, 126)

def exdd_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _zscore_rolling(base, 252)

def exdd_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rank_pct(base, 5)

def exdd_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rank_pct(base, 21)

def exdd_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rank_pct(base, 63)

def exdd_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rank_pct(base, 126)

def exdd_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 116 extreme day density to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rank_pct(base, 252)

def exdd_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_skew(base, 5)

def exdd_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_skew(base, 21)

def exdd_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_skew(base, 63)

def exdd_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_skew(base, 126)

def exdd_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 116 extreme day density distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_skew(base, 252)

def exdd_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_kurt(base, 5)

def exdd_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_kurt(base, 21)

def exdd_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_kurt(base, 63)

def exdd_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_kurt(base, 126)

def exdd_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 116 extreme day density over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _rolling_kurt(base, 252)

def exdd_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _safe_div(base, _rolling_std(base, 5))

def exdd_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _safe_div(base, _rolling_std(base, 21))

def exdd_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _safe_div(base, _rolling_std(base, 63))

def exdd_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _safe_div(base, _rolling_std(base, 126))

def exdd_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 116 extreme day density for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return _safe_div(base, _rolling_std(base, 252))

def exdd_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def exdd_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def exdd_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def exdd_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def exdd_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 116 extreme day density over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(40).mean()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def exdd_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _rolling_mean(base, 5)

def exdd_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _rolling_mean(base, 21)

def exdd_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _rolling_mean(base, 63)

def exdd_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _rolling_mean(base, 126)

def exdd_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 116 extreme day density over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _rolling_mean(base, 252)

def exdd_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _zscore_rolling(base, 5)

def exdd_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _zscore_rolling(base, 21)

def exdd_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _zscore_rolling(base, 63)

def exdd_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _zscore_rolling(base, 126)

def exdd_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 116 extreme day density by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs().rolling(50).mean()
    return _zscore_rolling(base, 252)
