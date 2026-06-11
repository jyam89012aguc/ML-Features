"""
92_92_ownership_concentration — Base Features 151-225
Domain: 92_ownership_concentration
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

def ocon_151_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 5)

def ocon_152_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 21)

def ocon_153_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 63)

def ocon_154_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 126)

def ocon_155_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 252)

def ocon_156_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 5)

def ocon_157_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 21)

def ocon_158_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 63)

def ocon_159_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 126)

def ocon_160_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 252)

def ocon_161_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 5)

def ocon_162_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 21)

def ocon_163_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 63)

def ocon_164_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 126)

def ocon_165_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 252)

def ocon_166_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 5))

def ocon_167_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 21))

def ocon_168_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 63))

def ocon_169_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 126))

def ocon_170_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 252))

def ocon_171_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocon_172_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocon_173_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocon_174_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocon_175_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocon_176_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 5)

def ocon_177_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 21)

def ocon_178_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 63)

def ocon_179_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 126)

def ocon_180_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 252)

def ocon_181_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 5)

def ocon_182_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 21)

def ocon_183_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 63)

def ocon_184_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 126)

def ocon_185_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 252)

def ocon_186_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 5)

def ocon_187_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 21)

def ocon_188_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 63)

def ocon_189_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 126)

def ocon_190_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 252)

def ocon_191_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 5)

def ocon_192_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 21)

def ocon_193_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 63)

def ocon_194_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 126)

def ocon_195_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 252)

def ocon_196_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 5)

def ocon_197_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 21)

def ocon_198_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 63)

def ocon_199_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 126)

def ocon_200_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 252)

def ocon_201_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def ocon_202_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def ocon_203_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def ocon_204_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def ocon_205_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def ocon_206_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocon_207_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocon_208_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocon_209_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocon_210_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocon_211_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 5)

def ocon_212_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 21)

def ocon_213_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 63)

def ocon_214_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 126)

def ocon_215_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 252)

def ocon_216_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def ocon_217_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def ocon_218_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def ocon_219_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def ocon_220_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def ocon_221_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 5)

def ocon_222_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 21)

def ocon_223_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 63)

def ocon_224_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 126)

def ocon_225_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 252)
