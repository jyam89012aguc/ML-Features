"""
61_61_revenue_deterioration — Base Features 001-075
Domain: 61_revenue_deterioration
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

def rdet_001_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue
    return _rolling_mean(base, 5)

def rdet_002_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue
    return _rolling_mean(base, 21)

def rdet_003_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue
    return _rolling_mean(base, 63)

def rdet_004_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue
    return _rolling_mean(base, 126)

def rdet_005_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue
    return _rolling_mean(base, 252)

def rdet_006_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue
    return _zscore_rolling(base, 5)

def rdet_007_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue
    return _zscore_rolling(base, 21)

def rdet_008_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue
    return _zscore_rolling(base, 63)

def rdet_009_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue
    return _zscore_rolling(base, 126)

def rdet_010_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue
    return _zscore_rolling(base, 252)

def rdet_011_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue
    return _rank_pct(base, 5)

def rdet_012_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue
    return _rank_pct(base, 21)

def rdet_013_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue
    return _rank_pct(base, 63)

def rdet_014_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue
    return _rank_pct(base, 126)

def rdet_015_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue
    return _rank_pct(base, 252)

def rdet_016_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue
    return _rolling_skew(base, 5)

def rdet_017_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue
    return _rolling_skew(base, 21)

def rdet_018_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue
    return _rolling_skew(base, 63)

def rdet_019_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue
    return _rolling_skew(base, 126)

def rdet_020_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue
    return _rolling_skew(base, 252)

def rdet_021_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue
    return _rolling_kurt(base, 5)

def rdet_022_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue
    return _rolling_kurt(base, 21)

def rdet_023_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue
    return _rolling_kurt(base, 63)

def rdet_024_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue
    return _rolling_kurt(base, 126)

def rdet_025_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue
    return _rolling_kurt(base, 252)

def rdet_026_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue
    return _safe_div(base, _rolling_std(base, 5))

def rdet_027_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue
    return _safe_div(base, _rolling_std(base, 21))

def rdet_028_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue
    return _safe_div(base, _rolling_std(base, 63))

def rdet_029_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue
    return _safe_div(base, _rolling_std(base, 126))

def rdet_030_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue
    return _safe_div(base, _rolling_std(base, 252))

def rdet_031_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_032_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_033_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_034_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_035_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_036_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def rdet_037_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def rdet_038_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def rdet_039_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def rdet_040_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def rdet_041_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def rdet_042_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def rdet_043_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def rdet_044_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def rdet_045_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def rdet_046_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def rdet_047_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def rdet_048_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def rdet_049_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def rdet_050_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def rdet_051_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def rdet_052_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def rdet_053_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def rdet_054_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def rdet_055_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def rdet_056_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def rdet_057_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def rdet_058_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def rdet_059_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def rdet_060_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def rdet_061_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_062_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_063_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_064_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_065_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_066_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_067_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_068_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_069_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_070_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = netinc / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_071_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def rdet_072_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def rdet_073_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def rdet_074_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def rdet_075_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = opinc / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 252)
