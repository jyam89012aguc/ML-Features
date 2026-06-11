"""
76_76_balance_sheet_decay — Base Features 001-075
Domain: 76_balance_sheet_decay
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

def bdec_001_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 5)

def bdec_002_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 21)

def bdec_003_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 63)

def bdec_004_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 126)

def bdec_005_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 252)

def bdec_006_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 5)

def bdec_007_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 21)

def bdec_008_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 63)

def bdec_009_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 126)

def bdec_010_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 252)

def bdec_011_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 5)

def bdec_012_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 21)

def bdec_013_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 63)

def bdec_014_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 126)

def bdec_015_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 252)

def bdec_016_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 5)

def bdec_017_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 21)

def bdec_018_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 63)

def bdec_019_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 126)

def bdec_020_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 252)

def bdec_021_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 5)

def bdec_022_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 21)

def bdec_023_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 63)

def bdec_024_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 126)

def bdec_025_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 252)

def bdec_026_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 5))

def bdec_027_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 21))

def bdec_028_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 63))

def bdec_029_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 126))

def bdec_030_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 252))

def bdec_031_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_032_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_033_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_034_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_035_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_036_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 5)

def bdec_037_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 21)

def bdec_038_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 63)

def bdec_039_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 126)

def bdec_040_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(21)
    return _rolling_mean(base, 252)

def bdec_041_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 5)

def bdec_042_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 21)

def bdec_043_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 63)

def bdec_044_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 126)

def bdec_045_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(21)
    return _zscore_rolling(base, 252)

def bdec_046_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 5)

def bdec_047_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 21)

def bdec_048_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 63)

def bdec_049_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 126)

def bdec_050_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(21)
    return _rank_pct(base, 252)

def bdec_051_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 5)

def bdec_052_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 21)

def bdec_053_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 63)

def bdec_054_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 126)

def bdec_055_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(21)
    return _rolling_skew(base, 252)

def bdec_056_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 5)

def bdec_057_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 21)

def bdec_058_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 63)

def bdec_059_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 126)

def bdec_060_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(21)
    return _rolling_kurt(base, 252)

def bdec_061_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_062_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_063_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_064_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_065_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(21)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_066_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_067_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_068_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_069_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_070_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(21)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_071_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 5)

def bdec_072_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 21)

def bdec_073_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 63)

def bdec_074_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 126)

def bdec_075_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.rolling(21).std()
    return _rolling_mean(base, 252)
