"""
94_94_holder_count_dynamics — Base Features 151-225
Domain: 94_holder_count_dynamics
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

def hcd_151_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 5)

def hcd_152_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 21)

def hcd_153_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 63)

def hcd_154_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 126)

def hcd_155_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 252)

def hcd_156_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 5)

def hcd_157_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 21)

def hcd_158_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 63)

def hcd_159_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 126)

def hcd_160_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 252)

def hcd_161_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 5)

def hcd_162_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 21)

def hcd_163_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 63)

def hcd_164_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 126)

def hcd_165_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 252)

def hcd_166_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 5))

def hcd_167_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 21))

def hcd_168_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 63))

def hcd_169_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 126))

def hcd_170_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 252))

def hcd_171_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hcd_172_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hcd_173_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hcd_174_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hcd_175_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hcd_176_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 5)

def hcd_177_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 21)

def hcd_178_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 63)

def hcd_179_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 126)

def hcd_180_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 252)

def hcd_181_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 5)

def hcd_182_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 21)

def hcd_183_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 63)

def hcd_184_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 126)

def hcd_185_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 252)

def hcd_186_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 5)

def hcd_187_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 21)

def hcd_188_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 63)

def hcd_189_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 126)

def hcd_190_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 252)

def hcd_191_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 5)

def hcd_192_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 21)

def hcd_193_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 63)

def hcd_194_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 126)

def hcd_195_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 252)

def hcd_196_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 5)

def hcd_197_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 21)

def hcd_198_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 63)

def hcd_199_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 126)

def hcd_200_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 252)

def hcd_201_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def hcd_202_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def hcd_203_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def hcd_204_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def hcd_205_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def hcd_206_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hcd_207_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hcd_208_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hcd_209_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hcd_210_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hcd_211_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 5)

def hcd_212_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 21)

def hcd_213_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 63)

def hcd_214_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 126)

def hcd_215_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 252)

def hcd_216_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def hcd_217_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def hcd_218_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def hcd_219_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def hcd_220_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def hcd_221_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 5)

def hcd_222_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 21)

def hcd_223_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 63)

def hcd_224_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 126)

def hcd_225_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 252)
