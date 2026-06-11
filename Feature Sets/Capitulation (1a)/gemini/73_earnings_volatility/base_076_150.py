"""
73_73_earnings_volatility — Base Features 076-150
Domain: 73_earnings_volatility
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

def evolt_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 5d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 5)

def evolt_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 21d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 21)

def evolt_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 63d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 63)

def evolt_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 126d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 126)

def evolt_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 252d mean.
    """
    base = marketcap.rolling(21).std()
    return _zscore_rolling(base, 252)

def evolt_081_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 5)

def evolt_082_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 21)

def evolt_083_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 63)

def evolt_084_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 126)

def evolt_085_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.rolling(21).std()
    return _rank_pct(base, 252)

def evolt_086_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 5)

def evolt_087_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 21)

def evolt_088_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 63)

def evolt_089_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 126)

def evolt_090_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.rolling(21).std()
    return _rolling_skew(base, 252)

def evolt_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 5)

def evolt_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 21)

def evolt_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 63)

def evolt_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 126)

def evolt_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.rolling(21).std()
    return _rolling_kurt(base, 252)

def evolt_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def evolt_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def evolt_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def evolt_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def evolt_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def evolt_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evolt_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evolt_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evolt_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evolt_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evolt_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 5d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 5)

def evolt_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 21d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 21)

def evolt_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 63d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 63)

def evolt_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 126d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 126)

def evolt_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 252d horizon to identify extreme regimes.
    """
    base = netinc.rolling(21).std()
    return _rolling_mean(base, 252)

def evolt_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 5d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 5)

def evolt_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 21d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 21)

def evolt_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 63d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 63)

def evolt_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 126d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 126)

def evolt_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 252d mean.
    """
    base = netinc.rolling(21).std()
    return _zscore_rolling(base, 252)

def evolt_116_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 5)

def evolt_117_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 21)

def evolt_118_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 63)

def evolt_119_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 126)

def evolt_120_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 73 earnings volatility to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = netinc.rolling(21).std()
    return _rank_pct(base, 252)

def evolt_121_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 5d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 5)

def evolt_122_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 21d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 21)

def evolt_123_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 63d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 63)

def evolt_124_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 126d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 126)

def evolt_125_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 73 earnings volatility distribution over 252d to detect tail risk or exhaustion.
    """
    base = netinc.rolling(21).std()
    return _rolling_skew(base, 252)

def evolt_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 5d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 5)

def evolt_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 21d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 21)

def evolt_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 63d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 63)

def evolt_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 126d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 126)

def evolt_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 73 earnings volatility over 252d to capture explosive breakdown or reversal points.
    """
    base = netinc.rolling(21).std()
    return _rolling_kurt(base, 252)

def evolt_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def evolt_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def evolt_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def evolt_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def evolt_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 73 earnings volatility for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = netinc.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def evolt_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 5d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evolt_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 21d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evolt_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 63d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evolt_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 126d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evolt_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 73 earnings volatility over 252d to stabilize variance and capture exponential shifts.
    """
    base = netinc.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evolt_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 5d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 5)

def evolt_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 21d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 21)

def evolt_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 63d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 63)

def evolt_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 126d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 126)

def evolt_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 73 earnings volatility over a 252d horizon to identify extreme regimes.
    """
    base = ocf.rolling(21).std()
    return _rolling_mean(base, 252)

def evolt_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 5d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 5)

def evolt_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 21d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 21)

def evolt_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 63d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 63)

def evolt_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 126d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 126)

def evolt_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 73 earnings volatility by measuring deviations from the 252d mean.
    """
    base = ocf.rolling(21).std()
    return _zscore_rolling(base, 252)
