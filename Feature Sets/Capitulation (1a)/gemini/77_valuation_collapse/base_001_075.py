"""
77_77_valuation_collapse — Base Features 001-075
Domain: 77_valuation_collapse
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

def vcol_001_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 5d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 5)

def vcol_002_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 21d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 21)

def vcol_003_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 63d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 63)

def vcol_004_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 126d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 126)

def vcol_005_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 252d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 252)

def vcol_006_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 5d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 5)

def vcol_007_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 21d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 21)

def vcol_008_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 63d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 63)

def vcol_009_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 126d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 126)

def vcol_010_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 252d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 252)

def vcol_011_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 5)

def vcol_012_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 21)

def vcol_013_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 63)

def vcol_014_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 126)

def vcol_015_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 252)

def vcol_016_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 5)

def vcol_017_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 21)

def vcol_018_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 63)

def vcol_019_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 126)

def vcol_020_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 252)

def vcol_021_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 5)

def vcol_022_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 21)

def vcol_023_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 63)

def vcol_024_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 126)

def vcol_025_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 252)

def vcol_026_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 5))

def vcol_027_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 21))

def vcol_028_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 63))

def vcol_029_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 126))

def vcol_030_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 252))

def vcol_031_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vcol_032_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vcol_033_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vcol_034_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vcol_035_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vcol_036_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 5)

def vcol_037_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 21)

def vcol_038_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 63)

def vcol_039_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 126)

def vcol_040_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 252)

def vcol_041_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 5)

def vcol_042_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 21)

def vcol_043_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 63)

def vcol_044_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 126)

def vcol_045_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 77 valuation collapse by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 252)

def vcol_046_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 5)

def vcol_047_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 21)

def vcol_048_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 63)

def vcol_049_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 126)

def vcol_050_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 77 valuation collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 252)

def vcol_051_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 5)

def vcol_052_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 21)

def vcol_053_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 63)

def vcol_054_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 126)

def vcol_055_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 77 valuation collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 252)

def vcol_056_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 5)

def vcol_057_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 21)

def vcol_058_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 63)

def vcol_059_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 126)

def vcol_060_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 77 valuation collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 252)

def vcol_061_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 5))

def vcol_062_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 21))

def vcol_063_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 63))

def vcol_064_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 126))

def vcol_065_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 77 valuation collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 252))

def vcol_066_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vcol_067_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vcol_068_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vcol_069_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vcol_070_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 77 valuation collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vcol_071_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 5)

def vcol_072_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 21)

def vcol_073_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 63)

def vcol_074_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 126)

def vcol_075_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 77 valuation collapse over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 252)
