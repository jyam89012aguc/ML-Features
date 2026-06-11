"""
72_72_solvency_scores — Base Features 076-150
Domain: 72_solvency_scores
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

def solv_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 5d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 5)

def solv_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 21d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 21)

def solv_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 63d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 63)

def solv_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 126d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 126)

def solv_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 252d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 252)

def solv_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 5)

def solv_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 21)

def solv_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 63)

def solv_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 126)

def solv_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 252)

def solv_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 5)

def solv_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 21)

def solv_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 63)

def solv_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 126)

def solv_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 252)

def solv_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 5)

def solv_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 21)

def solv_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 63)

def solv_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 126)

def solv_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 252)

def solv_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def solv_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def solv_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def solv_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def solv_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def solv_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def solv_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def solv_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def solv_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def solv_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def solv_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 5d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 5)

def solv_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 21d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 21)

def solv_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 63d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 63)

def solv_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 126d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 126)

def solv_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 252d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 252)

def solv_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 5d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 5)

def solv_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 21d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 21)

def solv_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 63d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 63)

def solv_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 126d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 126)

def solv_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 252d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 252)

def solv_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 5)

def solv_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 21)

def solv_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 63)

def solv_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 126)

def solv_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 252)

def solv_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 5d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 5)

def solv_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 21d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 21)

def solv_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 63d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 63)

def solv_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 126d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 126)

def solv_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 252d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 252)

def solv_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 5d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 5)

def solv_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 21d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 21)

def solv_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 63d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 63)

def solv_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 126d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 126)

def solv_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 252d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 252)

def solv_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def solv_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def solv_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def solv_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def solv_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def solv_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 5d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def solv_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 21d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def solv_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 63d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def solv_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 126d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def solv_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 252d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def solv_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 5d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 5)

def solv_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 21d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 21)

def solv_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 63d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 63)

def solv_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 126d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 126)

def solv_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 252d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 252)

def solv_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 5d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 5)

def solv_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 21d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 21)

def solv_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 63d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 63)

def solv_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 126d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 126)

def solv_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 252d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 252)
