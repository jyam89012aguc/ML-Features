"""
67_67_working_capital_drain — Base Features 076-150
Domain: 67_working_capital_drain
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

def wcap_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def wcap_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def wcap_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def wcap_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def wcap_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def wcap_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def wcap_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def wcap_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def wcap_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def wcap_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def wcap_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 5d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def wcap_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 21d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def wcap_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 63d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def wcap_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 126d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def wcap_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 252d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def wcap_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 5d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def wcap_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 21d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def wcap_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 63d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def wcap_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 126d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def wcap_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 252d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def wcap_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def wcap_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def wcap_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def wcap_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def wcap_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def wcap_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 5d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wcap_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 21d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wcap_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 63d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wcap_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 126d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wcap_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 252d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wcap_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 5d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 5)

def wcap_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 21d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 21)

def wcap_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 63d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 63)

def wcap_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 126d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 126)

def wcap_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 252d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 252)

def wcap_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 5)

def wcap_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 21)

def wcap_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 63)

def wcap_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 126)

def wcap_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 252)

def wcap_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 5)

def wcap_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 21)

def wcap_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 63)

def wcap_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 126)

def wcap_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 252)

def wcap_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 5d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 5)

def wcap_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 21d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 21)

def wcap_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 63d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 63)

def wcap_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 126d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 126)

def wcap_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 252d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 252)

def wcap_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 5d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 5)

def wcap_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 21d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 21)

def wcap_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 63d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 63)

def wcap_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 126d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 126)

def wcap_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 252d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 252)

def wcap_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 5))

def wcap_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 21))

def wcap_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 63))

def wcap_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 126))

def wcap_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 252))

def wcap_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 5d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wcap_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 21d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wcap_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 63d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wcap_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 126d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wcap_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 252d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wcap_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 5d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def wcap_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 21d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def wcap_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 63d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def wcap_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 126d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def wcap_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 252d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def wcap_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def wcap_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def wcap_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def wcap_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def wcap_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)
