"""
68_68_asset_quality — Base Features 076-150
Domain: 68_asset_quality
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

def aqal_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 5d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def aqal_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 21d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def aqal_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 63d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def aqal_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 126d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def aqal_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 252d mean.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def aqal_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def aqal_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def aqal_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def aqal_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def aqal_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def aqal_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def aqal_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def aqal_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def aqal_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def aqal_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def aqal_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 5d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def aqal_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 21d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def aqal_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 63d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def aqal_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 126d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def aqal_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 252d to capture explosive breakdown or reversal points.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def aqal_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def aqal_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def aqal_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def aqal_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def aqal_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def aqal_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def aqal_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def aqal_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def aqal_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def aqal_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def aqal_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 5d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 5)

def aqal_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 21d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 21)

def aqal_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 63d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 63)

def aqal_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 126d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 126)

def aqal_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 252d horizon to identify extreme regimes.
    """
    base = sharesbas.pct_change(21)
    return _rolling_mean(base, 252)

def aqal_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 5d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 5)

def aqal_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 21d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 21)

def aqal_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 63d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 63)

def aqal_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 126d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 126)

def aqal_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 252d mean.
    """
    base = sharesbas.pct_change(21)
    return _zscore_rolling(base, 252)

def aqal_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 5)

def aqal_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 21)

def aqal_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 63)

def aqal_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 126)

def aqal_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 68 asset quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = sharesbas.pct_change(21)
    return _rank_pct(base, 252)

def aqal_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 5)

def aqal_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 21)

def aqal_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 63)

def aqal_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 126)

def aqal_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 68 asset quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = sharesbas.pct_change(21)
    return _rolling_skew(base, 252)

def aqal_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 5d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 5)

def aqal_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 21d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 21)

def aqal_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 63d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 63)

def aqal_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 126d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 126)

def aqal_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 68 asset quality over 252d to capture explosive breakdown or reversal points.
    """
    base = sharesbas.pct_change(21)
    return _rolling_kurt(base, 252)

def aqal_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 5))

def aqal_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 21))

def aqal_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 63))

def aqal_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 126))

def aqal_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 68 asset quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = sharesbas.pct_change(21)
    return _safe_div(base, _rolling_std(base, 252))

def aqal_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def aqal_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def aqal_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def aqal_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def aqal_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 68 asset quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = sharesbas.pct_change(21)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def aqal_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 5d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def aqal_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 21d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def aqal_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 63d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def aqal_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 126d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def aqal_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 68 asset quality over a 252d horizon to identify extreme regimes.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def aqal_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 5d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def aqal_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 21d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def aqal_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 63d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def aqal_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 126d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def aqal_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 68 asset quality by measuring deviations from the 252d mean.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)
