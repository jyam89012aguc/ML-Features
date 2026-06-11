"""
93_93_institutional_bottom_fish — Base Features 151-225
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

def ibf_151_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 5)

def ibf_152_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 21)

def ibf_153_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 63)

def ibf_154_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 126)

def ibf_155_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 252)

def ibf_156_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 5)

def ibf_157_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 21)

def ibf_158_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 63)

def ibf_159_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 126)

def ibf_160_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 252)

def ibf_161_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 5)

def ibf_162_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 21)

def ibf_163_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 63)

def ibf_164_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 126)

def ibf_165_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 252)

def ibf_166_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 5))

def ibf_167_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 21))

def ibf_168_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 63))

def ibf_169_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 126))

def ibf_170_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 252))

def ibf_171_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_172_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_173_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_174_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_175_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_176_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 5)

def ibf_177_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 21)

def ibf_178_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 63)

def ibf_179_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 126)

def ibf_180_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 252)

def ibf_181_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 5)

def ibf_182_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 21)

def ibf_183_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 63)

def ibf_184_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 126)

def ibf_185_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 252)

def ibf_186_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 5)

def ibf_187_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 21)

def ibf_188_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 63)

def ibf_189_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 126)

def ibf_190_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 252)

def ibf_191_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 5)

def ibf_192_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 21)

def ibf_193_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 63)

def ibf_194_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 126)

def ibf_195_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 252)

def ibf_196_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 5)

def ibf_197_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 21)

def ibf_198_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 63)

def ibf_199_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 126)

def ibf_200_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 252)

def ibf_201_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def ibf_202_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def ibf_203_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def ibf_204_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def ibf_205_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def ibf_206_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_207_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_208_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_209_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_210_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_211_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 5)

def ibf_212_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 21)

def ibf_213_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 63)

def ibf_214_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 126)

def ibf_215_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 252)

def ibf_216_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def ibf_217_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def ibf_218_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def ibf_219_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def ibf_220_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def ibf_221_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 5)

def ibf_222_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 21)

def ibf_223_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 63)

def ibf_224_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 126)

def ibf_225_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 252)
