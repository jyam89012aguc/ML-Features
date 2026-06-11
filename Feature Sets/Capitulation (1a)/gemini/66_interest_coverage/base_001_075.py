"""
66_66_interest_coverage — Base Features 001-075
Domain: 66_interest_coverage
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

def icov_001_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def icov_002_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def icov_003_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def icov_004_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def icov_005_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def icov_006_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def icov_007_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def icov_008_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def icov_009_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def icov_010_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def icov_011_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def icov_012_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def icov_013_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def icov_014_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def icov_015_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def icov_016_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def icov_017_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def icov_018_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def icov_019_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def icov_020_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def icov_021_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def icov_022_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def icov_023_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def icov_024_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def icov_025_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def icov_026_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def icov_027_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def icov_028_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def icov_029_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def icov_030_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def icov_031_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_032_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_033_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_034_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_035_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_036_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def icov_037_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def icov_038_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def icov_039_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def icov_040_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_mean(base, 252)

def icov_041_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def icov_042_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def icov_043_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def icov_044_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def icov_045_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def icov_046_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 5)

def icov_047_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 21)

def icov_048_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 63)

def icov_049_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 126)

def icov_050_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rank_pct(base, 252)

def icov_051_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def icov_052_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def icov_053_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def icov_054_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def icov_055_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def icov_056_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def icov_057_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def icov_058_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def icov_059_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def icov_060_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def icov_061_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def icov_062_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def icov_063_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def icov_064_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def icov_065_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def icov_066_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_067_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_068_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_069_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_070_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = fcf / revenue.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_071_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 5)

def icov_072_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 21)

def icov_073_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 63)

def icov_074_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 126)

def icov_075_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = (netinc - ocf) / marketcap.replace(0, 1e-9)
    return _rolling_mean(base, 252)
