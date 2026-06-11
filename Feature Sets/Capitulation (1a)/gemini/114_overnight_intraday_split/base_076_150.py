"""
114_114_overnight_intraday_split — Base Features 076-150
Domain: 114_overnight_intraday_split
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

def onid_076_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 5)

def onid_077_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 21)

def onid_078_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 63)

def onid_079_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 126)

def onid_080_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 252)

def onid_081_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 5)

def onid_082_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 21)

def onid_083_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 63)

def onid_084_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 126)

def onid_085_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 252)

def onid_086_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_skew(base, 5)

def onid_087_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_skew(base, 21)

def onid_088_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_skew(base, 63)

def onid_089_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_skew(base, 126)

def onid_090_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_skew(base, 252)

def onid_091_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_kurt(base, 5)

def onid_092_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_kurt(base, 21)

def onid_093_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_kurt(base, 63)

def onid_094_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_kurt(base, 126)

def onid_095_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_kurt(base, 252)

def onid_096_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_097_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_098_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_099_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_100_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_101_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_102_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_103_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_104_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_105_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_106_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_mean(base, 5)

def onid_107_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_mean(base, 21)

def onid_108_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_mean(base, 63)

def onid_109_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_mean(base, 126)

def onid_110_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_mean(base, 252)

def onid_111_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(4) - 1)
    return _zscore_rolling(base, 5)

def onid_112_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(4) - 1)
    return _zscore_rolling(base, 21)

def onid_113_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(4) - 1)
    return _zscore_rolling(base, 63)

def onid_114_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(4) - 1)
    return _zscore_rolling(base, 126)

def onid_115_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(4) - 1)
    return _zscore_rolling(base, 252)

def onid_116_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(4) - 1)
    return _rank_pct(base, 5)

def onid_117_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(4) - 1)
    return _rank_pct(base, 21)

def onid_118_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(4) - 1)
    return _rank_pct(base, 63)

def onid_119_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(4) - 1)
    return _rank_pct(base, 126)

def onid_120_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(4) - 1)
    return _rank_pct(base, 252)

def onid_121_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_skew(base, 5)

def onid_122_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_skew(base, 21)

def onid_123_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_skew(base, 63)

def onid_124_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_skew(base, 126)

def onid_125_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_skew(base, 252)

def onid_126_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_kurt(base, 5)

def onid_127_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_kurt(base, 21)

def onid_128_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_kurt(base, 63)

def onid_129_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_kurt(base, 126)

def onid_130_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(4) - 1)
    return _rolling_kurt(base, 252)

def onid_131_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(4) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_132_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(4) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_133_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(4) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_134_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(4) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_135_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(4) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_136_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(4) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_137_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(4) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_138_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(4) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_139_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(4) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_140_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(4) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_141_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(5) - 1)
    return _rolling_mean(base, 5)

def onid_142_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(5) - 1)
    return _rolling_mean(base, 21)

def onid_143_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(5) - 1)
    return _rolling_mean(base, 63)

def onid_144_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(5) - 1)
    return _rolling_mean(base, 126)

def onid_145_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(5) - 1)
    return _rolling_mean(base, 252)

def onid_146_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(5) - 1)
    return _zscore_rolling(base, 5)

def onid_147_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(5) - 1)
    return _zscore_rolling(base, 21)

def onid_148_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(5) - 1)
    return _zscore_rolling(base, 63)

def onid_149_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(5) - 1)
    return _zscore_rolling(base, 126)

def onid_150_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(5) - 1)
    return _zscore_rolling(base, 252)
