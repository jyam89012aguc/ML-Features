"""
74_74_fundamental_momentum — Base Features 076-150
Domain: 74_fundamental_momentum
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

def fmom_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 5)

def fmom_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 21)

def fmom_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 63)

def fmom_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 126)

def fmom_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 252)

def fmom_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 5)

def fmom_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 21)

def fmom_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 63)

def fmom_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 126)

def fmom_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 252)

def fmom_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 5)

def fmom_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 21)

def fmom_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 63)

def fmom_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 126)

def fmom_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 252)

def fmom_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 5)

def fmom_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 21)

def fmom_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 63)

def fmom_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 126)

def fmom_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 252)

def fmom_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def fmom_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def fmom_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def fmom_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def fmom_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def fmom_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 5)

def fmom_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 21)

def fmom_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 63)

def fmom_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 126)

def fmom_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 252)

def fmom_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 5)

def fmom_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 21)

def fmom_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 63)

def fmom_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 126)

def fmom_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 252)

def fmom_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 5)

def fmom_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 21)

def fmom_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 63)

def fmom_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 126)

def fmom_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 252)

def fmom_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 5)

def fmom_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 21)

def fmom_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 63)

def fmom_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 126)

def fmom_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 252)

def fmom_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 5)

def fmom_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 21)

def fmom_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 63)

def fmom_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 126)

def fmom_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 252)

def fmom_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def fmom_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def fmom_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def fmom_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def fmom_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def fmom_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 5)

def fmom_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 21)

def fmom_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 63)

def fmom_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 126)

def fmom_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 252)

def fmom_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 5)

def fmom_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 21)

def fmom_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 63)

def fmom_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 126)

def fmom_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 252)
