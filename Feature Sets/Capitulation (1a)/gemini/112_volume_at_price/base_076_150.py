"""
112_112_volume_at_price — Base Features 076-150
Domain: 112_volume_at_price
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

def vapr_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _zscore_rolling(base, 5)

def vapr_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _zscore_rolling(base, 21)

def vapr_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _zscore_rolling(base, 63)

def vapr_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _zscore_rolling(base, 126)

def vapr_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _zscore_rolling(base, 252)

def vapr_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rank_pct(base, 5)

def vapr_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rank_pct(base, 21)

def vapr_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rank_pct(base, 63)

def vapr_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rank_pct(base, 126)

def vapr_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rank_pct(base, 252)

def vapr_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_skew(base, 5)

def vapr_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_skew(base, 21)

def vapr_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_skew(base, 63)

def vapr_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_skew(base, 126)

def vapr_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_skew(base, 252)

def vapr_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_kurt(base, 5)

def vapr_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_kurt(base, 21)

def vapr_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_kurt(base, 63)

def vapr_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_kurt(base, 126)

def vapr_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _rolling_kurt(base, 252)

def vapr_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _safe_div(base, _rolling_std(base, 5))

def vapr_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _safe_div(base, _rolling_std(base, 21))

def vapr_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _safe_div(base, _rolling_std(base, 63))

def vapr_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _safe_div(base, _rolling_std(base, 126))

def vapr_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return _safe_div(base, _rolling_std(base, 252))

def vapr_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * (close / _rolling_mean(close, 252))
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(4)
    return _rolling_mean(base, 5)

def vapr_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(4)
    return _rolling_mean(base, 21)

def vapr_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(4)
    return _rolling_mean(base, 63)

def vapr_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(4)
    return _rolling_mean(base, 126)

def vapr_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(4)
    return _rolling_mean(base, 252)

def vapr_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(4)
    return _zscore_rolling(base, 5)

def vapr_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(4)
    return _zscore_rolling(base, 21)

def vapr_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(4)
    return _zscore_rolling(base, 63)

def vapr_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(4)
    return _zscore_rolling(base, 126)

def vapr_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(4)
    return _zscore_rolling(base, 252)

def vapr_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(4)
    return _rank_pct(base, 5)

def vapr_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(4)
    return _rank_pct(base, 21)

def vapr_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(4)
    return _rank_pct(base, 63)

def vapr_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(4)
    return _rank_pct(base, 126)

def vapr_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(4)
    return _rank_pct(base, 252)

def vapr_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(4)
    return _rolling_skew(base, 5)

def vapr_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(4)
    return _rolling_skew(base, 21)

def vapr_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(4)
    return _rolling_skew(base, 63)

def vapr_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(4)
    return _rolling_skew(base, 126)

def vapr_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(4)
    return _rolling_skew(base, 252)

def vapr_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(4)
    return _rolling_kurt(base, 5)

def vapr_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(4)
    return _rolling_kurt(base, 21)

def vapr_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(4)
    return _rolling_kurt(base, 63)

def vapr_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(4)
    return _rolling_kurt(base, 126)

def vapr_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(4)
    return _rolling_kurt(base, 252)

def vapr_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(4)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(4)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(4)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(4)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(4)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(4)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(4)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(4)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(4)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(4)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(5)
    return _rolling_mean(base, 5)

def vapr_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(5)
    return _rolling_mean(base, 21)

def vapr_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(5)
    return _rolling_mean(base, 63)

def vapr_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(5)
    return _rolling_mean(base, 126)

def vapr_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(5)
    return _rolling_mean(base, 252)

def vapr_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(5)
    return _zscore_rolling(base, 5)

def vapr_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(5)
    return _zscore_rolling(base, 21)

def vapr_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(5)
    return _zscore_rolling(base, 63)

def vapr_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(5)
    return _zscore_rolling(base, 126)

def vapr_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(5)
    return _zscore_rolling(base, 252)
