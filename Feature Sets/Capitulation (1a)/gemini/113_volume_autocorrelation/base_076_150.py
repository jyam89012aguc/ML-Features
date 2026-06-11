"""
113_113_volume_autocorrelation — Base Features 076-150
Domain: 113_volume_autocorrelation
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

def vaut_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 5d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 5)

def vaut_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 21d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 21)

def vaut_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 63d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 63)

def vaut_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 126d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 126)

def vaut_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 252d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 252)

def vaut_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 5)

def vaut_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 21)

def vaut_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 63)

def vaut_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 126)

def vaut_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 252)

def vaut_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 5)

def vaut_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 21)

def vaut_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 63)

def vaut_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 126)

def vaut_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 252)

def vaut_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 5)

def vaut_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 21)

def vaut_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 63)

def vaut_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 126)

def vaut_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 252)

def vaut_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def vaut_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def vaut_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def vaut_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def vaut_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def vaut_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vaut_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vaut_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vaut_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vaut_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vaut_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_mean(base, 5)

def vaut_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_mean(base, 21)

def vaut_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_mean(base, 63)

def vaut_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_mean(base, 126)

def vaut_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_mean(base, 252)

def vaut_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 5d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _zscore_rolling(base, 5)

def vaut_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 21d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _zscore_rolling(base, 21)

def vaut_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 63d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _zscore_rolling(base, 63)

def vaut_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 126d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _zscore_rolling(base, 126)

def vaut_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 252d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _zscore_rolling(base, 252)

def vaut_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rank_pct(base, 5)

def vaut_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rank_pct(base, 21)

def vaut_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rank_pct(base, 63)

def vaut_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rank_pct(base, 126)

def vaut_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 113 volume autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rank_pct(base, 252)

def vaut_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_skew(base, 5)

def vaut_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_skew(base, 21)

def vaut_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_skew(base, 63)

def vaut_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_skew(base, 126)

def vaut_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 113 volume autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_skew(base, 252)

def vaut_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_kurt(base, 5)

def vaut_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_kurt(base, 21)

def vaut_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_kurt(base, 63)

def vaut_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_kurt(base, 126)

def vaut_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 113 volume autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _rolling_kurt(base, 252)

def vaut_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def vaut_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def vaut_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def vaut_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def vaut_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 113 volume autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def vaut_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vaut_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vaut_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vaut_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vaut_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 113 volume autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=4), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vaut_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_mean(base, 5)

def vaut_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_mean(base, 21)

def vaut_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_mean(base, 63)

def vaut_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_mean(base, 126)

def vaut_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 113 volume autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_mean(base, 252)

def vaut_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 5d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 5)

def vaut_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 21d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 21)

def vaut_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 63d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 63)

def vaut_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 126d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 126)

def vaut_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 113 volume autocorrelation by measuring deviations from the 252d mean.
    """
    base = volume.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _zscore_rolling(base, 252)
