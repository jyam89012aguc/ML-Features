"""
93_93_institutional_bottom_fish — Base Features 001-075
Domain: 93_institutional_bottom_fish
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

def ibf_001_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 5)

def ibf_002_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 21)

def ibf_003_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 63)

def ibf_004_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 126)

def ibf_005_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 252)

def ibf_006_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 5)

def ibf_007_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 21)

def ibf_008_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 63)

def ibf_009_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 126)

def ibf_010_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 252)

def ibf_011_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 5)

def ibf_012_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 21)

def ibf_013_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 63)

def ibf_014_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 126)

def ibf_015_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 252)

def ibf_016_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 5)

def ibf_017_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 21)

def ibf_018_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 63)

def ibf_019_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 126)

def ibf_020_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 252)

def ibf_021_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 5)

def ibf_022_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 21)

def ibf_023_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 63)

def ibf_024_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 126)

def ibf_025_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 252)

def ibf_026_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def ibf_027_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def ibf_028_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def ibf_029_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def ibf_030_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def ibf_031_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_032_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_033_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_034_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_035_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_036_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 5)

def ibf_037_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 21)

def ibf_038_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 63)

def ibf_039_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 126)

def ibf_040_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 252)

def ibf_041_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 5)

def ibf_042_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 21)

def ibf_043_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 63)

def ibf_044_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 126)

def ibf_045_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 252)

def ibf_046_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 5)

def ibf_047_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 21)

def ibf_048_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 63)

def ibf_049_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 126)

def ibf_050_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 252)

def ibf_051_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 5)

def ibf_052_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 21)

def ibf_053_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 63)

def ibf_054_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 126)

def ibf_055_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 252)

def ibf_056_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 5)

def ibf_057_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 21)

def ibf_058_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 63)

def ibf_059_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 126)

def ibf_060_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 252)

def ibf_061_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def ibf_062_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def ibf_063_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def ibf_064_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def ibf_065_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def ibf_066_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_067_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_068_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_069_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_070_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_071_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 5)

def ibf_072_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 21)

def ibf_073_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 63)

def ibf_074_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 126)

def ibf_075_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 252)
