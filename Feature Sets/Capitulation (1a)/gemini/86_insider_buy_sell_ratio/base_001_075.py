"""
86_86_insider_buy_sell_ratio — Base Features 001-075
Domain: 86_insider_buy_sell_ratio
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

def ibsr_001_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 5d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 5)

def ibsr_002_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 21d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 21)

def ibsr_003_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 63d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 63)

def ibsr_004_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 126d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 126)

def ibsr_005_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 252d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 252)

def ibsr_006_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 5d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 5)

def ibsr_007_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 21d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 21)

def ibsr_008_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 63d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 63)

def ibsr_009_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 126d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 126)

def ibsr_010_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 252d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 252)

def ibsr_011_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 5)

def ibsr_012_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 21)

def ibsr_013_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 63)

def ibsr_014_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 126)

def ibsr_015_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 252)

def ibsr_016_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 5)

def ibsr_017_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 21)

def ibsr_018_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 63)

def ibsr_019_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 126)

def ibsr_020_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 252)

def ibsr_021_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 5)

def ibsr_022_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 21)

def ibsr_023_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 63)

def ibsr_024_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 126)

def ibsr_025_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 252)

def ibsr_026_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def ibsr_027_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def ibsr_028_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def ibsr_029_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def ibsr_030_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def ibsr_031_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibsr_032_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibsr_033_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibsr_034_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibsr_035_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibsr_036_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 5)

def ibsr_037_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 21)

def ibsr_038_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 63)

def ibsr_039_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 126)

def ibsr_040_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 252)

def ibsr_041_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 5)

def ibsr_042_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 21)

def ibsr_043_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 63)

def ibsr_044_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 126)

def ibsr_045_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 252)

def ibsr_046_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 5)

def ibsr_047_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 21)

def ibsr_048_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 63)

def ibsr_049_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 126)

def ibsr_050_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 252)

def ibsr_051_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 5)

def ibsr_052_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 21)

def ibsr_053_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 63)

def ibsr_054_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 126)

def ibsr_055_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 252)

def ibsr_056_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 5)

def ibsr_057_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 21)

def ibsr_058_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 63)

def ibsr_059_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 126)

def ibsr_060_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 252)

def ibsr_061_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def ibsr_062_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def ibsr_063_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def ibsr_064_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def ibsr_065_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def ibsr_066_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibsr_067_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibsr_068_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibsr_069_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibsr_070_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibsr_071_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 5d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 5)

def ibsr_072_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 21d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 21)

def ibsr_073_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 63d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 63)

def ibsr_074_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 126d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 126)

def ibsr_075_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 252d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 252)
