"""
62_62_margin_compression — Base Features 076-150
Domain: 62_margin_compression
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

def mcmp_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 5d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mcmp_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 21d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mcmp_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 63d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mcmp_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 126d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mcmp_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 252d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def mcmp_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def mcmp_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def mcmp_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def mcmp_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def mcmp_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def mcmp_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def mcmp_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def mcmp_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def mcmp_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def mcmp_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def mcmp_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def mcmp_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def mcmp_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def mcmp_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def mcmp_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def mcmp_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def mcmp_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def mcmp_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def mcmp_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def mcmp_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def mcmp_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mcmp_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mcmp_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mcmp_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mcmp_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mcmp_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 5d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def mcmp_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 21d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def mcmp_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 63d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def mcmp_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 126d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def mcmp_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 252d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def mcmp_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 5d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mcmp_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 21d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mcmp_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 63d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mcmp_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 126d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mcmp_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 252d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def mcmp_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def mcmp_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def mcmp_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def mcmp_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def mcmp_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 62 margin compression to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def mcmp_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def mcmp_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def mcmp_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def mcmp_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def mcmp_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 62 margin compression distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def mcmp_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def mcmp_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def mcmp_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def mcmp_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def mcmp_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 62 margin compression over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def mcmp_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def mcmp_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def mcmp_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def mcmp_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def mcmp_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 62 margin compression for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def mcmp_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mcmp_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mcmp_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mcmp_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mcmp_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 62 margin compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mcmp_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 5d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def mcmp_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 21d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def mcmp_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 63d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def mcmp_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 126d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def mcmp_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 62 margin compression over a 252d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def mcmp_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 5d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mcmp_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 21d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mcmp_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 63d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mcmp_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 126d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mcmp_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 62 margin compression by measuring deviations from the 252d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)
