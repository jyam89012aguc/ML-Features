"""
71_71_accruals_quality — Base Features 001-075
Domain: 71_accruals_quality
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

def accq_001_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 5d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def accq_002_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 21d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def accq_003_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 63d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def accq_004_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 126d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def accq_005_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 252d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def accq_006_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 5d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def accq_007_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 21d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def accq_008_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 63d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def accq_009_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 126d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def accq_010_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 252d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def accq_011_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def accq_012_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def accq_013_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def accq_014_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def accq_015_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def accq_016_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def accq_017_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def accq_018_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def accq_019_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def accq_020_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def accq_021_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def accq_022_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def accq_023_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def accq_024_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def accq_025_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def accq_026_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def accq_027_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def accq_028_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def accq_029_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def accq_030_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def accq_031_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def accq_032_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def accq_033_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def accq_034_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def accq_035_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def accq_036_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 5d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def accq_037_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 21d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def accq_038_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 63d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def accq_039_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 126d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def accq_040_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 252d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def accq_041_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 5d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def accq_042_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 21d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def accq_043_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 63d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def accq_044_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 126d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def accq_045_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 252d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def accq_046_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def accq_047_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def accq_048_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def accq_049_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def accq_050_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def accq_051_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def accq_052_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def accq_053_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def accq_054_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def accq_055_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def accq_056_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 5d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def accq_057_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 21d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def accq_058_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 63d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def accq_059_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 126d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def accq_060_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 252d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def accq_061_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def accq_062_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def accq_063_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def accq_064_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def accq_065_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def accq_066_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def accq_067_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def accq_068_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def accq_069_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def accq_070_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def accq_071_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 5d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def accq_072_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 21d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def accq_073_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 63d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def accq_074_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 126d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def accq_075_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 252d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)
