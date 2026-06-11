"""
63_63_cash_burn — Base Features 076-150
Domain: 63_cash_burn
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

def cbrn_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 5d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cbrn_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 21d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cbrn_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 63d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cbrn_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 126d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cbrn_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 252d mean.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cbrn_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cbrn_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cbrn_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cbrn_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cbrn_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cbrn_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def cbrn_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def cbrn_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def cbrn_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def cbrn_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def cbrn_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def cbrn_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def cbrn_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def cbrn_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def cbrn_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def cbrn_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def cbrn_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def cbrn_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def cbrn_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def cbrn_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def cbrn_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cbrn_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cbrn_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cbrn_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cbrn_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cbrn_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 5d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cbrn_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 21d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cbrn_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 63d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cbrn_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 126d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cbrn_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 252d horizon to identify extreme regimes.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cbrn_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 5d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cbrn_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 21d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cbrn_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 63d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cbrn_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 126d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cbrn_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 252d mean.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def cbrn_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cbrn_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cbrn_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cbrn_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cbrn_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cbrn_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def cbrn_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def cbrn_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def cbrn_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def cbrn_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def cbrn_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def cbrn_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def cbrn_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def cbrn_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def cbrn_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def cbrn_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def cbrn_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def cbrn_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def cbrn_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def cbrn_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def cbrn_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cbrn_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cbrn_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cbrn_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cbrn_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cbrn_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 5d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def cbrn_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 21d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def cbrn_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 63d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def cbrn_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 126d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def cbrn_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 252d horizon to identify extreme regimes.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def cbrn_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 5d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def cbrn_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 21d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def cbrn_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 63d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def cbrn_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 126d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def cbrn_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 252d mean.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _zscore_rolling(base, 252)
