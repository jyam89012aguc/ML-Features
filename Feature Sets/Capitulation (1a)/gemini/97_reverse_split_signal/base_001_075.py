"""
97_97_reverse_split_signal — Base Features 001-075
Domain: 97_reverse_split_signal
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

def rvrs_001_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 5)

def rvrs_002_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 21)

def rvrs_003_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 63)

def rvrs_004_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 126)

def rvrs_005_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 252)

def rvrs_006_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 5)

def rvrs_007_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 21)

def rvrs_008_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 63)

def rvrs_009_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 126)

def rvrs_010_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 252)

def rvrs_011_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 5)

def rvrs_012_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 21)

def rvrs_013_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 63)

def rvrs_014_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 126)

def rvrs_015_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 252)

def rvrs_016_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 5)

def rvrs_017_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 21)

def rvrs_018_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 63)

def rvrs_019_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 126)

def rvrs_020_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 252)

def rvrs_021_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 5)

def rvrs_022_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 21)

def rvrs_023_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 63)

def rvrs_024_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 126)

def rvrs_025_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 252)

def rvrs_026_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_027_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_028_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_029_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_030_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_031_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_032_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_033_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_034_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_035_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_036_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 5)

def rvrs_037_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 21)

def rvrs_038_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 63)

def rvrs_039_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 126)

def rvrs_040_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 252)

def rvrs_041_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 5)

def rvrs_042_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 21)

def rvrs_043_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 63)

def rvrs_044_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 126)

def rvrs_045_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 252)

def rvrs_046_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 5)

def rvrs_047_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 21)

def rvrs_048_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 63)

def rvrs_049_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 126)

def rvrs_050_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 252)

def rvrs_051_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 5)

def rvrs_052_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 21)

def rvrs_053_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 63)

def rvrs_054_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 126)

def rvrs_055_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 252)

def rvrs_056_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 5)

def rvrs_057_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 21)

def rvrs_058_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 63)

def rvrs_059_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 126)

def rvrs_060_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 252)

def rvrs_061_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_062_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_063_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_064_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_065_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_066_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_067_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_068_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_069_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_070_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_071_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 5)

def rvrs_072_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 21)

def rvrs_073_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 63)

def rvrs_074_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 126)

def rvrs_075_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 252)
