"""
95_95_forced_selling_proxy — Base Features 001-075
Domain: 95_forced_selling_proxy
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

def fsel_001_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 5)

def fsel_002_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 21)

def fsel_003_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 63)

def fsel_004_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 126)

def fsel_005_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 252)

def fsel_006_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 5)

def fsel_007_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 21)

def fsel_008_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 63)

def fsel_009_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 126)

def fsel_010_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 252)

def fsel_011_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 5)

def fsel_012_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 21)

def fsel_013_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 63)

def fsel_014_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 126)

def fsel_015_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 252)

def fsel_016_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 5)

def fsel_017_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 21)

def fsel_018_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 63)

def fsel_019_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 126)

def fsel_020_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 252)

def fsel_021_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 5)

def fsel_022_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 21)

def fsel_023_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 63)

def fsel_024_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 126)

def fsel_025_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 252)

def fsel_026_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def fsel_027_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def fsel_028_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def fsel_029_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def fsel_030_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def fsel_031_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_032_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_033_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_034_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_035_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_036_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 5)

def fsel_037_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 21)

def fsel_038_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 63)

def fsel_039_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 126)

def fsel_040_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 252)

def fsel_041_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 5)

def fsel_042_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 21)

def fsel_043_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 63)

def fsel_044_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 126)

def fsel_045_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 252)

def fsel_046_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 5)

def fsel_047_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 21)

def fsel_048_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 63)

def fsel_049_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 126)

def fsel_050_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 252)

def fsel_051_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 5)

def fsel_052_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 21)

def fsel_053_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 63)

def fsel_054_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 126)

def fsel_055_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 252)

def fsel_056_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 5)

def fsel_057_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 21)

def fsel_058_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 63)

def fsel_059_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 126)

def fsel_060_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 252)

def fsel_061_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def fsel_062_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def fsel_063_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def fsel_064_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def fsel_065_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def fsel_066_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_067_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_068_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_069_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_070_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_071_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 5)

def fsel_072_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 21)

def fsel_073_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 63)

def fsel_074_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 126)

def fsel_075_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 252)
